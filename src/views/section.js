import { sections } from "../content/sections.js";

export function renderSectionPage(key, page) {
  const section = sections[key];
  const articles = section.articles || [];

  return `
    <section class="topic-hero">
      <div class="container">
        <div class="eyebrow">${page.eyebrow}</div>
        <h1>${section.title || page.title}</h1>
        <p class="topic-lead">${section.intro}</p>
      </div>
    </section>
    <section class="container section-index">
      <div class="section-article-list">
        ${articles.map((article, index) => {
          const questions = article.questions?.length
            ? article.questions
            : [article.title, ...(article.covers || [])];
          return `
          <article class="section-article-card">
            <div class="section-article-meta">
              <span class="section-topic-num">${String(index + 1).padStart(2, "0")}</span>
              <a class="section-article-title" href="${article.href}">${article.title}</a>
            </div>
            <div class="section-questions">
              <span class="section-questions-label">Preguntas que responde</span>
              <ul>
                ${questions.map((q) => `<li>${q}</li>`).join("")}
              </ul>
            </div>
            <a class="section-article-open" href="${article.href}">Abrir artículo →</a>
          </article>`;
        }).join("")}
      </div>
    </section>`;
}
