import { sourceCatalog } from "../config/sources.js";

export function renderSources(page) {
  return `
    <section class="topic-hero">
      <div class="container">
        <div class="eyebrow">${page.eyebrow}</div>
        <h1>${page.title}</h1>
        <p class="sources-opening">Esta es una invitación, pero para afirmarte: sí, hay mucho más que conocer sobre Yehoshúa HaMashíaj; tienes que ser diligente y te va a costar todo.</p>
        <p class="topic-lead">${page.description}</p>
      </div>
    </section>
    <section class="container section">
      <p class="lead-text" style="max-width:720px;margin-bottom:28px">Las enseñanzas audiovisuales de trabajo proceden de <strong>Eric de Jesús Rodríguez Mendoza</strong> y de <strong>Natanael Doldan</strong> (Somos el Cuerpo del Mesías). El sitio no es oficial ni habla en su nombre. Aquí solo hay enlaces, citas breves y síntesis propia. El material editorial puede consultarse en <a href="https://shaul.vercel.app" target="_blank" rel="noopener noreferrer">Proyecto Shaul</a> y el texto bíblico se coteja con <a href="https://davar.bible" target="_blank" rel="noopener noreferrer">Davar</a>.</p>
      <div class="source-list">${sourceCatalog.map(([title, detail, href]) => `<div class="source-item"><strong>${title}</strong><span>${detail}</span><a class="button button-secondary source-video-link" href="${href}" target="_blank" rel="noreferrer">Abrir video original →</a></div>`).join("")}</div>
      <div class="callout" style="margin-top:34px">
        <div>
          <div class="eyebrow">Método</div>
          <h2>Una afirmación debe poder rastrearse.</h2>
          <p>Fuente, instante, texto, contexto y veredicto.</p>
        </div>
        <div class="callout-quote">El griego se lee dentro de las Escrituras y del mundo hebraico, arameo y judío que el texto presupone.</div>
      </div>
    </section>`;
}
