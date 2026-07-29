import { sections } from "../content/sections.js";

function renderTopicMenu(key, label) {
  const section = sections[key];
  return `
    <div class="nav-topic-menu">
      <a class="nav-topic-link" data-section="${key}" href="#/${key}">${label}</a>
      <button class="nav-topic-toggle" type="button" aria-expanded="false" aria-controls="nav-panel-${key}" aria-label="Mostrar artículos de ${label}"><span aria-hidden="true">＋</span></button>
      <div class="nav-topic-panel" id="nav-panel-${key}" hidden>
        <a class="nav-section-link" href="#/${key}">Ver todos los artículos <span aria-hidden="true">↗</span></a>
        ${(section.articles || []).map((article) => `<a class="nav-article-link" href="${article.href}">${article.title}</a>`).join("")}
      </div>
    </div>`;
}

export function renderNav() {
  return `
    <a href="#/inicio">Inicio</a>
    ${renderTopicMenu("conceptos", "Conceptos")}
    ${renderTopicMenu("profecia", "Profecía")}
    ${renderTopicMenu("torah", "Torah y Evangelio")}
    <a href="#/fuentes">Fuentes</a>`;
}
