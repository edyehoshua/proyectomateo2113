/**
 * Section indexes: list articles (real pages), each with the questions it answers.
 * One href = one published article. Questions are grouped under the article.
 */

export const sections = {
  conceptos: {
    title: "Conceptos clave",
    intro: "Aquí hay artículos, no un menú de títulos sueltos. Cada bloque es un artículo; debajo, las preguntas que ese artículo responde.",
    home: [
      ["¿Quién es Yehoshúa: Elohim y Adón?", "#/deidad"],
      ["¿Por qué se le llama Yehoshúa?", "#/nombre"],
      ["¿Por qué es tan importante Ben Ha’Adam?", "#/benhaadam"],
      ["¿Qué significa la corporeidad de Yehoshúa HaMashíaj?", "#/corporeidad"],
      ["¿Cuál es el Israel de Elohim?", "#/israel"],
      ["¿Qué significa vivir bajo el Ruaj?", "#/ruaj"]
    ],
    articles: [
      {
        title: "¿Quién es Yehoshúa: Elohim y Adón?",
        href: "#/deidad",
        questions: [
          "¿Quién es Yehoshúa: Elohim y Adón?",
          "¿Quién es realmente Yehoshúa HaMashíaj?",
          "¿Qué significa que Adonai Elohim es Uno?",
          "¿Cómo se leen las obras, la gloria y la confesión del Mesías?"
        ]
      },
      {
        title: "¿Por qué se le llama Yehoshúa?",
        href: "#/nombre",
        questions: [
          "¿Por qué se le llama Yehoshúa?",
          "¿Qué une el nombre a la salvación?",
          "¿Qué no debe monopolizar la discusión del Nombre?"
        ]
      },
      {
        title: "¿Por qué es tan importante Ben Ha’Adam?",
        href: "#/benhaadam",
        questions: [
          "¿Por qué es tan importante Ben Ha’Adam?",
          "¿Qué significa Bar Enash?",
          "¿Qué tiene que ver Daniel 7 con este título?"
        ]
      },
      {
        title: "¿Qué significa Ben Ha’Elohim?",
        href: "#/benhaelohim",
        questions: [
          "¿Qué significa Ben Ha’Elohim?",
          "¿Es solo cercanía o confesión de identidad?"
        ]
      },
      {
        title: "¿Qué es Abá?",
        href: "#/aba",
        questions: [
          "¿Qué es Abá?",
          "¿A quién oraba Yehoshúa?",
          "¿Qué significa hacer tefilah?",
          "Cuando el texto dice “oraba” o “Padre”, ¿cómo se puede leer?"
        ]
      },
      {
        title: "¿Quién es el Menajem?",
        href: "#/menajem",
        questions: [
          "¿Quién es el Menajem?",
          "¿Qué significa Ruaj Ha’Kodesh en esa promesa?",
          "¿Cómo se distingue del emocionalismo?"
        ]
      },
      {
        title: "¿Qué es la Emunah hebrea?",
        href: "#/emunah",
        questions: [
          "¿Qué es la Emunah hebrea?",
          "¿Cómo se relaciona con pistis?",
          "¿Por qué no nace solo de la emoción?"
        ]
      },
      {
        title: "¿Qué significa vivir bajo el Ruaj?",
        href: "#/ruaj",
        questions: [
          "¿Qué significa vivir bajo el Ruaj?",
          "¿Cómo se diferencia del emocionalismo?"
        ]
      },
      {
        title: "¿Qué significa la corporeidad de Yehoshúa HaMashíaj?",
        href: "#/corporeidad",
        questions: [
          "¿Qué significa la corporeidad de Yehoshúa?",
          "¿Qué es el Adam del cielo?",
          "¿Qué pasa con la semilla, el vientre y la sangre?",
          "¿Cómo porta el pecado del mundo?"
        ]
      },
      {
        title: "¿Cuál es el Israel de Elohim?",
        href: "#/israel",
        questions: [
          "¿Cuál es el Israel de Elohim?",
          "¿Puede la “iglesia” reemplazar a Israel?",
          "¿Qué son el remanente, el olivo y las ramas injertadas?"
        ]
      }
    ]
  },

  profecia: {
    title: "Profecía",
    intro: "Artículos publicados. Cada uno agrupa las preguntas que trata; no hay enlaces que lleven a otra página con otro título.",
    home: [
      ["¿Cómo leer Apocalipsis (Sodot)?", "#/apocalipsis"],
      ["¿Por qué es tan importante Ben Ha’Adam?", "#/benhaadam"],
      ["¿Qué anuncia Isaías (Ieshaiáhu) 19?", "#/isaias19"],
      ["¿Qué significa una casa de oración?", "#/isaias56"],
      ["¿Cuál es el Israel de Elohim?", "#/israel"]
    ],
    articles: [
      {
        title: "¿Cómo leer Apocalipsis (Sodot)?",
        href: "#/apocalipsis",
        questions: [
          "¿Cómo leer Apocalipsis (Sodot)?",
          "¿Qué son los símbolos, bestias, sellos y trompetas?",
          "¿Cómo se leen las siete asambleas?",
          "¿Qué es el literalismo sin fundamento?",
          "¿Cómo se lee desde Daniel, Isaías (Ieshaiáhu), Ezequiel (Iejezqel) y Zacarías?"
        ]
      },
      {
        title: "¿Por qué es tan importante Ben Ha’Adam?",
        href: "#/benhaadam",
        questions: [
          "¿Por qué es tan importante Ben Ha’Adam?",
          "¿Qué anuncia Daniel 7 con Bar Enash?"
        ]
      },
      {
        title: "¿Qué anuncia Isaías (Ieshaiáhu) 19?",
        href: "#/isaias19",
        questions: [
          "¿Qué anuncia Isaías (Ieshaiáhu) 19?",
          "¿Qué pasa con Mitzráim, Ashur e Israel?",
          "¿Pueden las naciones ser representación en el lenguaje profético?"
        ]
      },
      {
        title: "¿Qué significa una casa de oración?",
        href: "#/isaias56",
        questions: [
          "¿Qué significa una casa de oración?",
          "¿Qué dice Isaías (Ieshaiáhu) 56 sobre extranjeros y eunucos?",
          "¿Cómo usa Yehoshúa esa frase en el Templo?"
        ]
      },
      {
        title: "¿Cuál es el Israel de Elohim?",
        href: "#/israel",
        questions: [
          "¿Cuál es el Israel de Elohim?",
          "¿Cómo se relaciona la profecía con el Estado moderno?",
          "¿Qué es remanente frente a reemplazo?"
        ]
      }
    ]
  },

  torah: {
    title: "Torah y Evangelio",
    intro: "Lista de artículos. Debajo de cada uno, las preguntas que ese artículo responde.",
    home: [
      ["¿Qué relación tienen Torah y Evangelio?", "#/mandamientos"],
      ["¿Quieres caminar en los mandamientos de Yehoshúa?", "#/mandamientos-yehoshua"],
      ["¿Qué significa realmente judaizar?", "#/galatas"],
      ["¿Quién es Israel en Romanos 11?", "#/romanos11"],
      ["¿Cuándo la autoridad se vuelve dominio?", "#/nicolaismo"],
      ["¿Se puede cobrar el acceso al conocimiento?", "#/gratuito"]
    ],
    articles: [
      {
        title: "¿Qué relación tienen Torah y Evangelio?",
        href: "#/mandamientos",
        questions: [
          "¿Qué relación tienen Torah y Evangelio?",
          "¿La Torah fue abolida?",
          "¿Qué producen la gracia y la obediencia?"
        ]
      },
      {
        title: "¿Quieres caminar en los mandamientos de Yehoshúa?",
        href: "#/mandamientos-yehoshua",
        questions: [
          "¿Quieres caminar en los mandamientos de Yehoshúa?",
          "¿Cómo examinar la vida con las diez palabras?"
        ]
      },
      {
        title: "¿Qué significa realmente judaizar?",
        href: "#/galatas",
        questions: [
          "¿Qué significa realmente judaizar?",
          "¿Qué discute Gálatas sobre promesa, simiente y fidelidad?"
        ]
      },
      {
        title: "¿Quién es Israel en Romanos 11?",
        href: "#/romanos11",
        questions: [
          "¿Quién es Israel en Romanos 11?",
          "¿Qué es el olivo, la raíz y las ramas?"
        ]
      },
      {
        title: "¿Qué lugar tienen las lenguas?",
        href: "#/lenguas",
        questions: [
          "¿Qué lugar tienen las lenguas?",
          "¿Qué piden interpretación, orden y edificación?"
        ]
      },
      {
        title: "¿Cuándo la autoridad se vuelve dominio?",
        href: "#/nicolaismo",
        questions: [
          "¿Cuándo la autoridad se vuelve dominio?",
          "¿Qué es el nicolaismo?",
          "¿Qué tiene que ver Balaam y el enseñoreamiento?"
        ]
      },
      {
        title: "¿Se puede cobrar el acceso al conocimiento?",
        href: "#/gratuito",
        questions: [
          "¿Se puede cobrar el acceso al conocimiento?",
          "¿Qué significa “de gracia recibisteis, dad de gracia”?"
        ]
      },
      {
        title: "¿Por qué el cristianismo es una religión?",
        href: "#/religion",
        questions: [
          "¿Por qué el cristianismo es una religión?",
          "¿Qué es la neoidolatría de tradiciones del olam?"
        ]
      },
      {
        title: "¿Qué significa vivir bajo el Ruaj?",
        href: "#/ruaj",
        questions: [
          "¿Qué significa vivir bajo el Ruaj?",
          "¿Cómo se relaciona con obediencia y emocionalismo?"
        ]
      },
      {
        title: "¿Qué es la Emunah hebrea?",
        href: "#/emunah",
        questions: [
          "¿Qué es la Emunah hebrea?",
          "¿Qué tienen que ver fidelidad y perseverancia?"
        ]
      },
      {
        title: "¿De dónde sale cada afirmación?",
        href: "#/fuentes",
        questions: [
          "¿De dónde sale cada afirmación?",
          "¿Cómo se usan TTH, hebreo, griego y arameo?"
        ]
      }
    ]
  }
};

export const sectionRoutes = {
  conceptos: ["benhaadam", "benhaelohim", "corporeidad", "nombre", "israel", "deidad", "aba", "menajem", "emunah", "ruaj"],
  profecia: ["apocalipsis", "isaias19", "isaias56", "benhaadam", "israel"],
  torah: ["mandamientos", "mandamientos-yehoshua", "galatas", "romanos11", "lenguas", "nicolaismo", "gratuito", "religion", "ruaj", "emunah", "fuentes"]
};
