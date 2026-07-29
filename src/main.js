import { bindNav, render } from "./router.js";
import { renderNav } from "./views/nav.js";

document.querySelector("#main-nav").innerHTML = renderNav();
bindNav();
render();
