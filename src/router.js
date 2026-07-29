import { pages } from "./content/pages.js";
import { sectionRoutes } from "./content/sections.js";

export function getRoute() {
  const raw = window.location.hash.replace(/^#\/?/, "").split("/")[0];
  return raw || "inicio";
}

function isSectionActive(href, route) {
  if (href === `#/${route}`) return true;
  if (href === "#/conceptos") return sectionRoutes.conceptos.includes(route);
  if (href === "#/profecia") return sectionRoutes.profecia.includes(route);
  if (href === "#/torah") return sectionRoutes.torah.includes(route);
  return false;
}

export function render() {
  const route = getRoute();
  const page = pages[route] || pages.inicio;
  document.title = `${page.title} · Proyecto Mateo 2113`;
  const app = document.querySelector("#app");
  app.classList.remove("route-enter");
  app.innerHTML = page.render();
  document.querySelectorAll(".nav-topic-menu.is-open").forEach((menu) => {
    menu.classList.remove("is-open");
    menu.querySelector(".nav-topic-toggle")?.setAttribute("aria-expanded", "false");
    const panel = menu.querySelector(".nav-topic-panel");
    if (panel) panel.hidden = true;
  });
  requestAnimationFrame(() => app.classList.add("route-enter"));
  document.querySelectorAll(".main-nav a, .nav-topic-toggle").forEach((item) => {
    const section = item.dataset.section;
    const active = section
      ? route === section || sectionRoutes[section]?.includes(route)
      : isSectionActive(item.getAttribute("href"), route);
    item.classList.toggle("active", Boolean(active));
  });
  app.focus({ preventScroll: true });
  window.scrollTo({ top: 0, behavior: "smooth" });
}

export function bindNav() {
  const mainNav = document.querySelector(".main-nav");
  const menuToggle = document.querySelector(".menu-toggle");

  const closeTopicMenus = () => {
    mainNav.querySelectorAll(".nav-topic-menu.is-open").forEach((menu) => {
      menu.classList.remove("is-open");
      const button = menu.querySelector(".nav-topic-toggle");
      const panel = menu.querySelector(".nav-topic-panel");
      button?.setAttribute("aria-expanded", "false");
      if (panel) panel.hidden = true;
    });
  };

  const closeMobileNav = () => {
    mainNav.classList.remove("open");
    menuToggle.setAttribute("aria-expanded", "false");
  };

  menuToggle.addEventListener("click", () => {
    const open = mainNav.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(open));
  });

  mainNav.addEventListener("click", (event) => {
    const toggle = event.target.closest(".nav-topic-toggle");
    if (toggle) {
      const menu = toggle.closest(".nav-topic-menu");
      const panel = menu.querySelector(".nav-topic-panel");
      const open = !menu.classList.contains("is-open");
      closeTopicMenus();
      menu.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      panel.hidden = !open;
      return;
    }

    if (event.target.closest("a")) {
      closeTopicMenus();
      closeMobileNav();
    }
  });

  document.addEventListener("click", (event) => {
    if (!event.target.closest(".main-nav")) closeTopicMenus();
  });

  window.addEventListener("hashchange", render);
}
