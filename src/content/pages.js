import { renderHome } from "../views/home.js";
import { renderSectionPage } from "../views/section.js";
import { renderReading } from "../views/reading.js";
import { renderYehoshuaCommandments } from "../views/commandments.js";
import { renderSources } from "../views/sources.js";

function reading(key) {
  return () => renderReading(key, pages[key]);
}

export const pages = {
  inicio: {
    title: "Volver al texto.",
    eyebrow: "Información · testimonio · discernimiento",
    description: "Un archivo para examinar enseñanzas sobre Yehoshúa HaMashíaj, la profecía, la Torah y la vida bajo el Ruaj.",
    render: renderHome
  },
  conceptos: {
    title: "Conceptos clave",
    eyebrow: "Sección",
    description: "Las palabras y preguntas que sostienen la lectura de Yehoshúa y de la asamblea.",
    render: () => renderSectionPage("conceptos", pages.conceptos)
  },
  profecia: {
    title: "Profecía",
    eyebrow: "Sección",
    description: "Cómo leer Apocalipsis (Sodot), Isaías (Ieshaiáhu) y las imágenes del Tanaj sin forzar el texto.",
    render: () => renderSectionPage("profecia", pages.profecia)
  },
  torah: {
    title: "Torah y Evangelio",
    eyebrow: "Sección",
    description: "Gracia, obediencia, Israel, Gálatas y la vida que el Ruaj produce.",
    render: () => renderSectionPage("torah", pages.torah)
  },
  benhaadam: {
    title: "¿Por qué es tan importante Ben Ha’Adam?",
    eyebrow: "Conceptos",
    description: "Bar Enash, Ben HaAdam y ὁ υἱὸς τοῦ ἀνθρώπου: un título que no puede reducirse a ‘humano’.",
    render: reading("benhaadam")
  },
  benhaelohim: {
    title: "¿Qué significa Ben Ha’Elohim?",
    eyebrow: "Conceptos",
    description: "El Hijo de Elohim, la filiación y la identidad del Mesías.",
    render: reading("benhaelohim")
  },
  corporeidad: {
    title: "¿Qué significa la corporeidad de Yehoshúa HaMashíaj?",
    eyebrow: "Conceptos",
    description: "Qué significa que Elohim se haya manifestado corporalmente en Yehoshúa.",
    render: reading("corporeidad")
  },
  nombre: {
    title: "¿Por qué se le llama Yehoshúa?",
    eyebrow: "Conceptos",
    description: "El nombre del Mesías, la salvación y la revelación del Nombre.",
    render: reading("nombre")
  },
  israel: {
    title: "¿Cuál es el Israel de Elohim?",
    eyebrow: "Conceptos",
    description: "El remanente, el olivo y la reunión de los hijos de Elohim alrededor del Mesías.",
    render: reading("israel")
  },
  religion: {
    title: "¿Por qué el cristianismo es una religión?",
    eyebrow: "Torah y Evangelio",
    description: "Institución, tradición y la diferencia entre religión y vida de asamblea.",
    render: reading("religion")
  },
  deidad: {
    title: "¿Quién es Yehoshúa: Elohim y Adón?",
    eyebrow: "Conceptos",
    description: "Nombre, gloria, obras y confesión del Mesías.",
    render: reading("deidad")
  },
  aba: {
    title: "¿Qué es Abá?",
    eyebrow: "Conceptos",
    description: "Fuente y promesa; tefilah como entrar en juicio; cómo leer “oraba” y “Padre” en Juan (Yojanán) y Marcos (Markos).",
    render: reading("aba")
  },
  menajem: {
    title: "¿Quién es el Menajem?",
    eyebrow: "Conceptos",
    description: "El Consolador y la promesa del Ruaj Ha’Kodesh.",
    render: reading("menajem")
  },
  emunah: {
    title: "¿Qué es la Emunah hebrea?",
    eyebrow: "Conceptos",
    description: "Emunah, pistis y una confianza que no depende de la emoción.",
    render: reading("emunah")
  },
  ruaj: {
    title: "¿Qué significa vivir bajo el Ruaj?",
    eyebrow: "Conceptos",
    description: "Mandamientos, fruto y la diferencia entre Ruaj y emocionalismo.",
    render: reading("ruaj")
  },
  mandamientos: {
    title: "¿Qué relación tienen Torah y Evangelio?",
    eyebrow: "Torah y Evangelio",
    description: "La obediencia como fruto de la gracia.",
    render: reading("mandamientos")
  },
  "mandamientos-yehoshua": {
    title: "¿Quieres caminar en los mandamientos de Yehoshúa?",
    eyebrow: "Torah y Evangelio",
    description: "Diez palabras para examinar la vida.",
    render: () => renderYehoshuaCommandments(pages["mandamientos-yehoshua"])
  },
  lenguas: {
    title: "¿Qué lugar tienen las lenguas?",
    eyebrow: "Torah y Evangelio",
    description: "Dones, interpretación, orden y edificación.",
    render: reading("lenguas")
  },
  nicolaismo: {
    title: "¿Cuándo la autoridad se vuelve dominio?",
    eyebrow: "Torah y Evangelio",
    description: "Dominación, plataforma y enseñoreamiento sobre la asamblea.",
    render: reading("nicolaismo")
  },
  apocalipsis: {
    title: "¿Cómo leer Apocalipsis (Sodot)?",
    eyebrow: "Profecía",
    description: "Símbolo, contexto y Tanaj contra el literalismo sin prueba.",
    render: reading("apocalipsis")
  },
  isaias19: {
    title: "¿Qué anuncia Isaías (Ieshaiáhu) 19?",
    eyebrow: "Profecía",
    description: "Mitzráim, Ashur e Israel: nombres, juicio, sanidad y representación.",
    render: reading("isaias19")
  },
  isaias56: {
    title: "¿Qué significa una casa de oración?",
    eyebrow: "Profecía",
    description: "Extranjeros, eunucos, justicia y fidelidad.",
    render: reading("isaias56")
  },
  galatas: {
    title: "¿Qué significa realmente judaizar?",
    eyebrow: "Torah y Evangelio",
    description: "Promesa, Torah, carne y fidelidad.",
    render: reading("galatas")
  },
  romanos11: {
    title: "¿Quién es Israel en Romanos 11?",
    eyebrow: "Torah y Evangelio",
    description: "Remanente, raíz, ramas naturales y ramas injertadas.",
    render: reading("romanos11")
  },
  gratuito: {
    title: "¿Se puede cobrar el acceso al conocimiento?",
    eyebrow: "Torah y Evangelio",
    description: "Conocimiento, dinero y la responsabilidad de enseñar sin vender a Elohim.",
    render: reading("gratuito")
  },
  fuentes: {
    title: "¿De dónde sale cada afirmación?",
    eyebrow: "Trazabilidad",
    description: "Fuentes audiovisuales y notas de enseñanza, con elaboración propia.",
    render: () => renderSources(pages.fuentes)
  }
};
