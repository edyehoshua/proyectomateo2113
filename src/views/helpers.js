export function link(href, label, className = "button button-secondary") {
  const external = /^https?:\/\//i.test(href);
  return `<a class="${className}" href="${href}"${external ? ' target="_blank" rel="noopener noreferrer"' : ""}>${label}</a>`;
}

export function homeTopicLink(title, href) {
  return `<a class="home-topic-link" href="${href}"><span>${title}</span><b>↗</b></a>`;
}
