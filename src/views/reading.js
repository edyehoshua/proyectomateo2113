import { readings } from "../content/readings/index.js";
import { link } from "./helpers.js";

function cleanPassageText(text) {
  return text
    .replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]+/gu, "")
    .replace(/__([^_]+)__/g, "<em>$1</em>");
}

function renderPassage(passage) {
  const text = cleanPassageText(passage.text);

  return `
    <figure class="passage-block">
      <figcaption class="passage-ref">${passage.ref}</figcaption>
      <blockquote class="passage-text">${text}</blockquote>
      ${passage.note ? `<p class="passage-note">${passage.note}</p>` : ""}
    </figure>`;
}

function renderSectionBody(body) {
  if (Array.isArray(body)) {
    return body.map((paragraph) => `<p>${paragraph}</p>`).join("");
  }
  return `<p>${body}</p>`;
}

function renderLexicon(rows) {
  if (!rows?.length) return "";
  return `
    <section class="evidence-block" aria-label="Palabras clave">
      <h2>Palabras que debes entender</h2>
      <p class="evidence-intro">Si nunca oíste estos términos, empieza aquí. Cada uno se explica en lenguaje sencillo.</p>
      <div class="evidence-table">
        <div class="evidence-row evidence-head">
          <span>Palabra</span><span>Qué significa aquí</span>
        </div>
        ${rows.map(([term, sense]) => `
          <div class="evidence-row">
            <span class="evidence-term">${term}</span>
            <span>${sense}</span>
          </div>
        `).join("")}
      </div>
    </section>`;
}

function renderHistorical(items) {
  if (!items?.length) return "";
  return `
    <section class="evidence-block" aria-label="Historia e idioma">
      <h2>Historia e idioma (sin dar por sabido nada)</h2>
      <p class="evidence-intro">No bastan nombres técnicos. Cada fuente se explica: qué es, de cuándo es y por qué importa para esta pregunta.</p>
      <div class="evidence-list">
        ${items.map(([title, body]) => `
          <div class="evidence-item">
            <strong>${title}</strong>
            <p>${body}</p>
          </div>
        `).join("")}
      </div>
    </section>`;
}

function renderMethod(steps) {
  if (!steps?.length) return "";
  return `
    <section class="evidence-block" aria-label="Cómo se lee">
      <h2>Cómo se lee este tema</h2>
      <p class="evidence-intro">Pasos que puedes seguir al examinar el texto.</p>
      <ol class="evidence-method">
        ${steps.map((step) => `<li>${step}</li>`).join("")}
      </ol>
    </section>`;
}

export function renderReading(key, page) {
  const reading = readings[key];
  if (!reading) {
    return `<section class="container"><p>Tema en preparación.</p></section>`;
  }

  const visual = reading.visual
    ? `<section class="topic-visual">
        <div class="container">
          <figure class="topic-figure large">
            <img src="${reading.visual.src}" alt="${reading.visual.alt}" loading="lazy" />
            ${reading.visual.why ? `<figcaption>${reading.visual.why}</figcaption>` : ""}
          </figure>
        </div>
      </section>`
    : "";

  const passages = reading.passages?.length
    ? `<section class="passage-stack" aria-label="Textos">
        ${reading.passages.map(renderPassage).join("")}
      </section>`
    : "";

  const sectionsMarkup = (reading.sections || [])
  .map(([title, body]) => `<h2>${title}</h2>${renderSectionBody(body)}`)
  .join("");

  const answer = reading.answer
    ? `<p class="topic-answer">${reading.answer}</p>`
    : "";

  const sourceLinks = reading.sources?.length
    ? `<div class="topic-source-links">${reading.sources.map(([href, label]) => link(href, label)).join("")}</div>`
    : `<p class="topic-sources-empty">Todavía no hay una enseñanza en video catalogada para este tema.</p>`;
  const sources = `<section class="topic-sources" aria-label="Enseñanzas en video">
      <p class="topic-sources-label">Enseñanzas en video:</p>
      ${sourceLinks}
    </section>`;

  return `
    <section class="topic-hero">
      <div class="container">
        <div class="eyebrow">${page.eyebrow}</div>
        <h1>${page.title}</h1>
        <p class="topic-lead">${reading.lead || page.description}</p>
      </div>
    </section>
    ${visual}
    <section class="container topic-body">
      <article class="article article-wide">
        ${reading.intro ? `<p class="lead-text">${reading.intro}</p>` : ""}
        ${passages}
        ${renderMethod(reading.method)}
        ${renderLexicon(reading.lexicon)}
        ${renderHistorical(reading.historical)}
        ${sectionsMarkup}
        ${answer}
        ${sources}
      </article>
    </section>`;
}
