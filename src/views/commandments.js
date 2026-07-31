import { yehoshuaCommandments } from "../data/commandments.js";

function cleanCommandmentText(text) {
  return text.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹]+/gu, "");
}

function renderCommandmentCard(commandment) {
  return `<details class="commandment-card"><summary><span class="commandment-number">${commandment.number}</span><span class="commandment-title">${commandment.title}</span><span class="commandment-open">abrir +</span></summary><div class="commandment-body"><div class="commandment-reference">${commandment.reference}</div><p class="commandment-text">“${cleanCommandmentText(commandment.text)}”</p><p class="commandment-question">${commandment.question}</p><label class="commandment-check"><input type="checkbox" data-commandment-id="${commandment.number}" /> <span>Quiero examinarlo delante de Adonai.</span></label></div></details>`;
}

export function renderYehoshuaCommandments(page) {
  return `
    <section class="topic-hero">
      <div class="container">
        <div class="eyebrow">${page.eyebrow}</div>
        <h1>${page.title}</h1>
        <p class="topic-lead">Esta no es una escalera para comprar salvación. El Mesías nos amó y se entregó por nosotros. Por eso podemos mirar sus palabras con gratitud y deseo de caminar en ellas.</p>
      </div>
    </section>
    <section class="topic-visual">
      <div class="container">
        <figure class="topic-figure large">
          <img src="/images/fuego-techelet.webp" alt="Árbol en llamas dibujado en tinta tejelet" loading="lazy" />
          <figcaption>
            <strong>Por qué esta imagen</strong>
            <span>La palabra prueba y orienta la vida. Cada mandamiento cita el texto y abre una pregunta para examinar el corazón.</span>
          </figcaption>
        </figure>
      </div>
    </section>
    <section class="container topic-body commandments-page">
      <article class="article article-wide">
        <div class="commandment-intro">
          <p class="commandment-context">Estos mandamientos pertenecen al testimonio de la Torah que Yehoshúa enseñó, resumió en amor y llamó a guardar: Matityahu 5:17–20; 19:17; Markos 12:29–31; Yojanán 14:15.</p>
        </div>
        <div class="commandment-grid">${yehoshuaCommandments.map(renderCommandmentCard).join("")}</div>
        <div class="commandment-closing">
          <div>
            <div class="eyebrow">Después de marcar</div>
            <h2>¿Cómo quieres caminar?</h2>
            <p>No hace falta responder todo de una vez. Elige una palabra, vuelve al texto y pregunta a Adonai cómo llevarla a la vida cotidiana.</p>
          </div>
          <div class="commandment-prompts">
            <span>¿Qué ya practicas?</span>
            <span>¿Qué quieres retomar?</span>
            <span>¿Qué te gustaría aprender?</span>
          </div>
        </div>
        <section class="topic-sources" aria-label="Enseñanzas en video">
          <p class="topic-sources-label">Enseñanzas en video:</p>
          <p class="topic-sources-empty">Todavía no hay una enseñanza en video catalogada para este tema.</p>
        </section>
      </article>
    </section>`;
}
