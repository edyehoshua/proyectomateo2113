import { link, homeTopicLink } from "./helpers.js";
import { sections } from "../content/sections.js";

function renderHomeSection(key, number, label) {
  const section = sections[key];
  return `
    <section class="home-topic-section">
      <div class="home-topic-label"><span>${number}</span><strong>${label}</strong></div>
      <p class="home-section-copy">Artículos publicados. Cada uno responde a una pregunta principal.</p>
      <div class="home-topic-links">
        ${section.home.map(([title, href]) => homeTopicLink(title, href)).join("")}
        ${homeTopicLink("Ver todos los artículos →", `#/${key}`)}
      </div>
    </section>`;
}

export function renderHome() {
  return `
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-copy">
          <div class="eyebrow">Una invitación para quien sigue buscando</div>
          <h1>¿Hay preguntas en tu corazón, pero hay mucho ruido a tu alrededor?</h1>
          <p>Quizás has sido edificado. Quizás amas a Adonai Yehoshúa y has recibido mucho bien. Pero hay enseñanzas, prácticas o interpretaciones que todavía no terminan de cerrar en tu corazón, y el Ruaj de Elohim te ha inquietado a buscar.</p>
          <figure class="hero-figure">
            <img src="/images/montanas-techelet.webp" alt="Montañas en capas dibujadas en tinta tejelet sobre papel texturado" width="960" height="720" />
            <figcaption>Volver al texto: Es como escalar una montaña, un trabajo arduo pero al hacerlo ganas altura, contexto y calma antes de forzar una conclusión.</figcaption>
          </figure>
          <div class="hero-question">¿Y si esa incomodidad no fuera falta de fe, sino una invitación a volver a examinarlo todo?</div>
          <div class="hero-audience" aria-label="A quién está dirigida esta invitación">
            <p>Esto no es para confrontar un ministerio, eventos o agendas. Es para aquellos que tienen oídos para oír y están oyendo lo que desde hace tiempo Adonai Yehoshúa les ha hablado a sus corazones.</p>
          </div>
          <div class="hero-principles" aria-label="Principios de discernimiento">
            <p>Donde hay multitudes de gente, generalmente allí no es. El Adón Yehoshúa HaMashíaj dijo que son muy pocos los que hallan la puerta.</p>
            <p>Aunque las personas tengan buenas intenciones, si lo que enseñan, dicen y hacen no está alineado con las Escrituras, lamentablemente están en error.</p>
          </div>
          <div class="hero-actions">${link("#/conceptos", "Entrar por las preguntas", "button button-primary")}</div>
        </div>
      </div>
    </section>
    <section class="container home-index" aria-label="Secciones">
      <div class="home-index-heading">
        <div class="eyebrow">Secciones</div>
        <h2>Artículos, no un laberinto de títulos.</h2>
        <p>En cada sección verás los artículos. Dentro de cada artículo se agrupan las preguntas que responde.</p>
      </div>
      <div class="home-topic-sections home-topic-sections-three">
        ${renderHomeSection("conceptos", "01", "Conceptos clave")}
        ${renderHomeSection("profecia", "02", "Profecía")}
        ${renderHomeSection("torah", "03", "Torah y Evangelio")}
      </div>
    </section>`;
}
