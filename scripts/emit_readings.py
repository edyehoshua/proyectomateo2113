#!/usr/bin/env python3
"""Emit accessible reading modules with lexicon + historical for every topic."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "content" / "readings"

def j(s):
    return json.dumps(s, ensure_ascii=False)

def emit(name: str, t: dict, indent: int = 2) -> str:
    sp = " " * indent
    lines = [f"{sp}{name}: {{"]
    order = [
        "lead", "question", "visual", "intro", "passages",
        "method", "lexicon", "historical", "sections", "answer", "sources"
    ]
    present = [k for k in order if k in t]
    for i, k in enumerate(present):
        v = t[k]
        comma = "," if i < len(present) - 1 else ""
        if k in ("lead", "question", "intro", "answer"):
            lines.append(f"{sp}  {k}: {j(v)}{comma}")
        elif k == "visual":
            lines.append(f"{sp}  visual: {{")
            lines.append(f"{sp}    src: {j(v['src'])},")
            lines.append(f"{sp}    alt: {j(v['alt'])},")
            lines.append(f"{sp}    why: {j(v['why'])}")
            lines.append(f"{sp}  }}{comma}")
        elif k == "passages":
            lines.append(f"{sp}  passages: [")
            for n, p in enumerate(v):
                c = "," if n < len(v) - 1 else ""
                lines.append(
                    f"{sp}    {{ ref: {j(p['ref'])}, text: {j(p['text'])}, note: {j(p['note'])} }}{c}"
                )
            lines.append(f"{sp}  ]{comma}")
        elif k == "method":
            arr = ",\n".join(f"{sp}    {j(s)}" for s in v)
            lines.append(f"{sp}  method: [\n{arr}\n{sp}  ]{comma}")
        elif k in ("lexicon", "historical"):
            rows = [f"{sp}    [{j(a)}, {j(b)}]" for a, b in v]
            lines.append(f"{sp}  {k}: [\n" + ",\n".join(rows) + f"\n{sp}  ]{comma}")
        elif k == "sections":
            lines.append(f"{sp}  sections: [")
            for n, (title, body) in enumerate(v):
                c = "," if n < len(v) - 1 else ""
                if isinstance(body, list):
                    arr = ",\n".join(f"{sp}      {j(p)}" for p in body)
                    lines.append(f"{sp}    [{j(title)}, [\n{arr}\n{sp}    ]]{c}")
                else:
                    lines.append(f"{sp}    [{j(title)}, {j(body)}]{c}")
            lines.append(f"{sp}  ]{comma}")
        elif k == "sources":
            parts = [f"[sourceLinks.{hk}, {j(lab)}]" for hk, lab in v]
            lines.append(f"{sp}  sources: [{', '.join(parts)}]{comma}")
    lines.append(f"{sp}}}")
    return "\n".join(lines)

def write_module(filename: str, export_name: str, topics: dict, order: list[str]):
    header = (
        'import { sourceLinks } from "../../config/sources.js";\n\n'
        f"/** Readings — beginner-accessible lexicon + historical sources */\n"
        f"export const {export_name} = {{\n"
    )
    body = ",\n".join(emit(k, topics[k]) for k in order)
    path = OUT / filename
    path.write_text(header + body + "\n};\n", encoding="utf-8")
    print("wrote", path, "bytes", path.stat().st_size)

# Shared helpers for plain-language base terms used across topics
BASE = {
  "tanaj": "Tanaj: el conjunto de Escrituras hebreas (Torah, Profetas y Escritos). En las iglesias suele llamarse “Antiguo Testamento”.",
  "besorah": "Besorah / Evangelio: el anuncio de las buenas noticias del Mesías; también los relatos de Matityahu, Markos, Lucas y Yojanán.",
  "segundo_templo": "Segundo Templo: período judío aproximadamente del siglo VI a.e.c. al año 70 e.c., cuando existía el Templo reconstruido en Yerushaláyim. Yehoshúa y los enviados vivieron al final de ese mundo.",
  "lxx": "Septuaginta (LXX): traducción antigua del Tanaj al griego, hecha por judíos siglos antes del Mesías. Sirve para ver qué palabras griegas usaban para ideas hebreas.",
  "mishna": "Mishná: colección de enseñanzas y normas judías escritas hacia el año 200 e.c. No es Escritura; es literatura histórica y jurídica del judaísmo. Se cita cuando ayuda a entender el idioma o la cultura, no como autoridad por encima del texto bíblico.",
  "talmud": "Talmud: comentarios y discusiones rabínicas posteriores a la Mishná. Es fuente histórica/cultural, no un reemplazo del Tanaj ni del Evangelio.",
  "targum": "Targum: traducciones/paráfrasis arameas del Tanaj usadas en sinagogas cuando mucha gente hablaba arameo. Muestran cómo se entendía un pasaje en ese mundo.",
  "arameo": "Arameo: idioma semítico hermano del hebreo, común en el Segundo Templo. Algunas palabras del Evangelio (como Aba) son arameas.",
  "hebreo": "Hebreo: idioma principal del Tanaj y del pensamiento de Israel. Muchas ideas del Evangelio se entienden mejor desde el hebreo aunque el manuscrito griego sea el que tenemos.",
  "griego": "Griego del Evangelio: el texto de los Evangelios y cartas se transmitió en griego. No es “griego de Atenas puro”: lleva mentalidad semítica detrás de las palabras.",
  "tth": "TTH: Traducción Textual del Hebreo (Natanael Doldan), usada con permiso para citar en español cercano al hebreo.",
}

# ========== CONCEPTOS ==========
C = {}

C["benhaadam"] = {
  "lead": "Si nunca oíste “Ben Ha’Adam”, no pasa nada. Es un título del Mesías. El peligro es reducirlo a “un humano cualquiera” y perder Daniel 7.",
  "question": "¿Qué significa Ben Ha’Adam / Bar Enash, y por qué Yehoshúa lo usa con autoridad de cielo y no solo como “hombre”?",
  "visual": {
    "src": "/images/montanas-techelet.webp",
    "alt": "Montañas en tinta tejelet",
    "why": "Daniel 7 muestra una figura que viene con las nubes. La imagen de altura recuerda que el título no nace del polvo."
  },
  "intro": "En muchas Biblias lees “Hijo del Hombre” y piensas: “significa que era humano”. Esa lectura es demasiado corta. En el Tanaj, Daniel 7 presenta a alguien “como un hijo de hombre” que recibe dominio eterno. Los Evangelios toman ese título. Esta página explica las palabras y el contexto histórico para quien llega por primera vez.",
  "passages": [
    {"ref": "Daniel 7:13–14 · TTH", "text": "…con las nubes de los cielos como un hijo de hombre venía… Y a Él fue dado dominio, y honor, y reinado.", "note": "Aquí nace el peso del título: nubes, autoridad y reino — no “ciudadano cualquiera”."},
    {"ref": "Markos 2:10 · TTH", "text": "…el Hijo del Hombre tiene autoridad en la tierra para perdonar pecados…", "note": "Yehoshúa usa el título para reclamar autoridad de perdonar. Si solo significara “humano”, la frase se debilita."},
    {"ref": "Yojanán 5:27 · TTH", "text": "Y también le dio autoridad de hacer juicio, porque es el Hijo del Hombre.", "note": "Otra vez: el título se une al juicio."},
    {"ref": "1 Corintios 15:47 · TTH", "text": "El primer hombre es del polvo de la tierra; el segundo hombre es del cielo.", "note": "Pablo distingue el Adam del polvo y el Adam del cielo. Eso protege de confusiones."},
  ],
  "method": [
    "Lee primero Daniel 7 completo, no solo la frase “hijo de hombre”.",
    "Luego lee los Evangelios donde Yehoshúa usa el título (perdón, juicio, venida).",
    "Pregunta: ¿esta escena habla de debilidad humana o de autoridad celestial?",
    "Compara con 1 Corintios 15: polvo vs cielo.",
  ],
  "lexicon": [
    ["בן־האדם · Ben Ha’Adam", "Hebreo: “hijo del Adam / del hombre”. En los Evangelios funciona como título, no como apodo casual."],
    ["בַּר אֱנָשׁ · Bar Enash", "Arameo de Daniel 7: “hijo de hombre”. Es la forma del libro de Daniel (escrito en parte en arameo)."],
    ["ὁ υἱὸς τοῦ ἀνθρώπου", "Griego de los Evangelios: “el Hijo del Hombre”, con artículo; no es un humano genérico sin contexto."],
    ["אָדָם · Adam", "Puede ser el primer hombre, la humanidad o “hombre” según el pasaje. No siempre significa “pecador por definición”."],
    ["Anciano de días", "Figura de Daniel 7: majestad y trono del juicio. El “como hijo de hombre” se acerca a esa escena."],
    ["ἄνθρωπος · anthrōpos", "Griego: hombre/humano. La clase advierte no traducirlo automáticamente como “humano caído”."],
  ],
  "historical": [
    ["Daniel 7 en su mundo", "Daniel es un libro del Tanaj con visiones de imperios y juicio. En el capítulo 7, bestias representan reinos; luego aparece una figura humana que recibe un reino eterno. Ese marco es anterior a Yehoshúa y era conocido en el judaísmo del Segundo Templo."],
    [BASE["segundo_templo"], "En ese período se leían Daniel y se esperaba intervención de Elohim. Los Evangelios no inventan el título desde cero: dialogan con ese horizonte."],
    [BASE["arameo"], "Daniel 7 está en arameo. Por eso “Bar Enash” importa: es la forma original de esa visión, no un invento griego."],
    [BASE["griego"], "Los Evangelios están en griego, pero el título “Hijo del Hombre” arrastra el peso de Daniel, no solo el diccionario griego de “hombre”."],
    [BASE["lxx"], "La Septuaginta ayuda a ver cómo lectores judíos de lengua griega encontraban Daniel y otras Escrituras."],
  ],
  "sections": [
    ["Si es tu primera vez con este título", [
      "No necesitas saber hebreo para empezar. Necesitas no borrar Daniel 7.",
      "“Hijo del Hombre” suena humilde en castellano; en Daniel suena a autoridad recibida del cielo.",
    ]],
    ["Qué se pierde si solo dices “era humano”", [
      "Se pierde el dominio, el juicio y la venida con las nubes.",
      "Se confunde semejanza visible con origen adámico corrupto.",
    ]],
    ["Cómo se conecta con el Adam del cielo", [
      "Pablo habla de un primer Adam del polvo y un segundo del cielo.",
      "Ben Ha’Adam puede señalar corporeidad real sin decir “pecador como el primer Adam”.",
    ]],
  ],
  "answer": "Ben Ha’Adam / Bar Enash es un título que une corporeidad real con autoridad de arriba, anclado en Daniel 7. No es un sinónimo de “humano caído”.",
  "sources": [("benHaAdam", "Eric · Ben HaAdam"), ("yojananCuerpo", "Eric · 1 Corintios 15 / Adam del cielo")],
}

C["corporeidad"] = {
  "lead": "Corporeidad significa que Yehoshúa tuvo cuerpo real. La pregunta siguiente es: ¿de qué origen es ese cuerpo, y qué implica para pecado y sacrificio?",
  "question": "¿Qué significa la corporeidad de Yehoshúa? ¿Cuerpo real? ¿Adam del cielo? ¿Semilla, vientre y sangre?",
  "visual": {
    "src": "/images/montanas-techelet.webp",
    "alt": "Montañas en capas",
    "why": "Hay que sostener a la vez origen de arriba y manifestación real abajo."
  },
  "intro": "Algunas personas niegan que el Mesías tuviera cuerpo de verdad (como si solo “pareciera” humano). Otras lo tratan como un hombre común del linaje de la corrupción. El Evangelio y las cartas obligan a separar preguntas: cuerpo real; origen; pecado; sangre y ofrenda.",
  "passages": [
    {"ref": "Yojanán 1:14 · TTH", "text": "Y la Palabra se hizo carne, y habitó entre nosotros…", "note": "Carne y habitación: no es un fantasma."},
    {"ref": "Filipenses 2:6–8 · TTH", "text": "…siendo en forma de Elohim… se despojó… hecho semejante a los hombres…", "note": "Disminución real como siervo, no pérdida de deidad."},
    {"ref": "Hebreos 2:14 · TTH", "text": "…participó de carne y sangre…", "note": "Participación real junto a los hijos."},
    {"ref": "Hebreos 10:5 · TTH", "text": "…me preparaste cuerpo.", "note": "El cuerpo es preparado; no se reduce a un producto automático del linaje adámico."},
    {"ref": "1 Corintios 15:44–47 · TTH", "text": "…cuerpo anímico… cuerpo espiritual… el segundo hombre es del cielo.", "note": "Hay corporeidad antes y después de la resurrección; y hay dos Adams."},
  ],
  "method": [
    "Separa: ¿hubo cuerpo real? (sí) ¿eso implica pecado propio? (no automáticamente).",
    "Lee los relatos de muerte y resurrección corporal (Lucas 24, Yojanán 20).",
    "Lee 1 Corintios 15 sin saltar el “segundo hombre del cielo”.",
    "Lee Isaías 53 y Yojanán 1:29 sobre portar/quitar pecado.",
  ],
  "lexicon": [
    ["σῶμα · sōma", "Griego: cuerpo. En los textos puede ser el cuerpo físico y, en Pablo, también el cuerpo resucitado."],
    ["σάρξ · sarx", "Griego: carne. A veces “cuerpo humano”, a veces “condición humana débil”, a veces “pecado” según contexto. No siempre = pecado."],
    ["μορφή · morphē", "Forma/condición (Filipenses 2): forma de Elohim / forma de siervo."],
    ["Postrer Adam", "Título de 1 Corintios 15: el Mesías como nuevo comienzo de humanidad, del cielo."],
    ["Semilla (en esta enseñanza)", "Unidad de vida de arriba; no se explica como “espermatozoide de Yosef” ni como “óvulo de Miryam” como origen."],
    ["Docetismo (error histórico)", "Herejía antigua que decía que el Mesías solo “parecía” tener cuerpo. El Evangelio la contradice."],
  ],
  "historical": [
    ["Por qué existió la discusión sobre el cuerpo", "En el mundo griego y en algunos grupos tempranos, lo material se despreciaba. Algunos intentaron decir que el Mesías no tuvo cuerpo real. Las cartas (p. ej. 1 Yojanán) confrontan negaciones de la venida en carne."],
    [BASE["griego"], "Palabras como sarx y sōma deben leerse pasaje por pasaje, no con un diccionario moderno de “pecado = carne” siempre."],
    [BASE["hebreo"], "El Tanaj no desprecia el cuerpo creado; la corrupción entra por el pecado, no porque la materia sea mala en sí."],
    ["Filipenses y el himno del siervo", "Filipenses 2 usa un lenguaje denso de forma, vaciamiento y exaltación. Las clases lo leen como disminución voluntaria del Mesías, no como invención de un segundo dios menor."],
    [BASE["tth"], "Usamos TTH para citar en español sin perder el sabor hebreo de los términos."],
  ],
  "sections": [
    ["Cuerpo real, no disfraz", [
      "Comió, se cansó, sufrió, murió y resucitó. Negar el cuerpo contradice los relatos.",
      "Cuerpo real no significa automáticamente “hombre adámico bajo pecado”.",
    ]],
    ["Semilla, vientre y sangre (explicado simple)", [
      "Vientre: lugar de gestación. No por eso el origen de la semilla es Miryam o Yosef.",
      "Sangre: medio de la muerte y de la ofrenda; no prueba automática de naturaleza adámica pecaminosa.",
      "Portar el pecado: asumir juicio y carga ajenos, no volverse moralmente impuro como el pecador.",
    ]],
  ],
  "answer": "La corporeidad de Yehoshúa es real. Es el Adam del cielo, no un hombre común del linaje de la corrupción. Por eso puede portar el pecado del mundo sin ser pecador.",
  "sources": [("semilla", "Eric · Semilla y origen"), ("vientre", "Eric · Vientre"), ("sangre", "Eric · Sangre"), ("deidadParte4", "Eric · Corporeidad")],
}

C["nombre"] = {
  "lead": "El nombre no es magia de sonidos ni un detalle de registro civil. El texto une el nombre a la salvación.",
  "question": "¿Por qué se le llama Yehoshúa? ¿Qué une el nombre a la misión, y qué no debe monopolizar la discusión?",
  "visual": {
    "src": "/images/fuego-techelet.webp",
    "alt": "Árbol en llamas",
    "why": "El Nombre se revela con misión: fuego, promesa y salvación van juntos."
  },
  "intro": "Si vienes del castellano, quizás solo conoces “Jesús”. Yehoshúa es la forma hebrea del nombre del Mesías. La página no pelea por magia de pronunciación: muestra que Matityahu une el nombre a “salvará a su pueblo”.",
  "passages": [
    {"ref": "Matityahu 1:21 · TTH", "text": "…llamarás su nombre Yehoshúa, porque Él salvará a su pueblo de sus pecados.", "note": "El “porque” es teológico: nombre y salvación unidos."},
    {"ref": "Shemot 3:14–15 · TTH", "text": "Yo seré el que seré… Este es mi Nombre para siempre…", "note": "El Nombre de יהוה no es adorno; la misión del Mesías se lee en continuidad con esa revelación."},
    {"ref": "Yojanán 17:6 · TTH", "text": "He manifestado tu nombre a los hombres…", "note": "Manifestar el Nombre es revelar quién es Elohim, no solo pronunciar un sonido."},
    {"ref": "Hechos 4:12 · TTH", "text": "…no hay otro nombre bajo el cielo… en que podamos ser salvos.", "note": "El nombre identifica a la persona por quien Elohim salva."},
  ],
  "method": [
    "Separa tres preguntas: forma escrita; sentido del nombre; obras del que lo lleva.",
    "No conviertas la pronunciación en el centro del evangelio.",
    "Lee Matityahu 1:21 antes de debatir transliteraciones.",
  ],
  "lexicon": [
    ["יְהוֹשֻׁעַ · Yehoshúa", "Nombre hebreo del Mesías. Relacionado con “יהוה salva / es salvación” en el uso bíblico y etimológico."],
    ["יֵשׁוּעַ · Yeshúa", "Forma corta del mismo nombre, común en textos posteriores y en muchas enseñanzas."],
    ["שם · shem", "Nombre, fama, reputación, revelación de quién es alguien — no solo etiqueta."],
    ["Tetragrámaton · יהוה", "Las cuatro letras del Nombre de Elohim en el Tanaj. Se escribe; la pronunciación exacta es discutida. No debe convertirse en superstición."],
    ["Ἰησοῦς · Iēsous", "Forma griega del nombre en el NT. Es cómo se escribió en griego, no una “otra persona”."],
  ],
  "historical": [
    ["Nombres hebreos en un mundo bilingüe", "En el Segundo Templo se hablaba hebreo, arameo y griego. Un mismo nombre podía escribirse de formas distintas según el idioma, sin cambiar de persona."],
    [BASE["hebreo"], "El sentido del nombre se oye mejor en hebreo: salvación unida a יהוה."],
    [BASE["griego"], "El NT usa Iēsous porque se escribió en griego para un mundo que leía griego."],
    ["Por qué hay debates de pronunciación", "Al dejar de pronunciar el Tetragrámaton en voz alta en ciertas tradiciones, y al pasar por griego y latín, se abrió espacio a discusiones. La página prioriza misión y persona sobre pelea de sonidos."],
    [BASE["tth"], "TTH mantiene “Yehoshúa” y el Tetragrámaton de forma consciente."],
  ],
  "sections": [
    ["Qué responde el título", [
      "Se le llama Yehoshúa porque su nombre está unido a salvar al pueblo (Matityahu 1:21).",
    ]],
    ["Qué no debe monopolizar la discusión", [
      "La pronunciación exacta y las guerras de transliteración.",
      "Tratar el nombre como amuleto separado de la obediencia y del testimonio.",
    ]],
  ],
  "answer": "Se le llama Yehoshúa porque el nombre está unido a la salvación y a la revelación de Elohim. La etimología ayuda; no reemplaza al Mesías ni a sus obras.",
  "sources": [("nombre", "Eric · Nombre"), ("abaYojanan14", "Eric · Nombre en Yojanán 14")],
}

C["israel"] = {
  "lead": "“Israel de Elohim” no es un eslogan político ni un club religioso. Es una pregunta sobre promesa, remanente y fidelidad.",
  "question": "¿Cuál es el Israel de Elohim? ¿Puede una institución “reemplazar” a Israel?",
  "visual": {
    "src": "/images/fruto-techelet.webp",
    "alt": "Árbol con frutos",
    "why": "El olivo es la imagen: raíz, ramas e injerto."
  },
  "intro": "Si no conoces el debate: algunas teologías dicen que “la iglesia” reemplazó a Israel. Pablo en Romanos 11 dice que Elohim no rechazó a su pueblo. Las naciones pueden ser injertadas; no deben jactarse contra la raíz.",
  "passages": [
    {"ref": "Romanos 11:1–2 · TTH", "text": "¿Acaso rechazó Elohim a su pueblo? ¡Profanación sea a nosotros!", "note": "La respuesta inicial es no."},
    {"ref": "Romanos 11:17–18 · TTH", "text": "…fuiste injertado… no te jactes contra las ramas.", "note": "Injerto = entrada por gracia; jactancia = error."},
    {"ref": "Yojanán 11:52 · TTH", "text": "…reunir en uno a los hijos de Elohim que estaban dispersos.", "note": "Reunión, no borrado."},
    {"ref": "Efesios 2:14–16 · TTH", "text": "…de ambos pueblos hizo uno…", "note": "Unificación en el Mesías, no asimilación forzada ni reemplazo."},
  ],
  "method": [
    "Define las palabras: Israel, remanente, naciones, iglesia/asamblea, Estado moderno.",
    "Lee Romanos 9–11 como un solo argumento.",
    "Pregunta si tu conclusión jacta a las naciones contra la raíz.",
  ],
  "lexicon": [
    ["Israel", "Nombre del pueblo de la promesa (Jacob y sus descendientes) y, en sentido más amplio, del pueblo de Elohim según el contexto del pasaje."],
    ["Remanente", "Parte del pueblo preservada por gracia, no “todo el mundo con el mismo pasaporte”."],
    ["Olivo", "Imagen de Romanos 11: un árbol con raíz y ramas; unas se desgajan, otras se injertan."],
    ["Injerto", "Técnica agrícola: unir una rama de un árbol a otro. Pablo la usa para explicar cómo entran las naciones."],
    ["Teología del reemplazo", "Idea de que la iglesia sustituyó a Israel en las promesas. Esta página la examina y la rechaza como lectura de Romanos 11."],
    ["Asamblea / ekklēsia", "Reunión de llamados; no automáticamente “la institución cristiana medieval o moderna”."],
  ],
  "historical": [
    ["Por qué surgió el reemplazo", "Cuando el mensaje se extendió entre naciones y crecieron tensiones con comunidades judías, algunos maestros cristianos antiguos releyeron las promesas como si Israel hubiera sido descartado. Esa historia es larga; no es el único resultado posible del texto."],
    [BASE["segundo_templo"], "Israel vivía bajo imperios (persa, griego, romano). “Pueblo”, “tierra” y “remanente” ya eran temas vivos antes del Mesías."],
    ["Pablo como judío que cree en el Mesías", "Pablo no se presenta como fundador de una religión anti-Israel; discute promesa, Torah y naciones desde las Escrituras de Israel."],
    ["Estado moderno de Israel", "Nació en el siglo XX. No es idéntico automáticamente al “Israel” de cada profecía. Hay que distinguir pueblo, remanente, gobierno y cumplimiento."],
    [BASE["tanaj"], "Las promesas a Abraham, Isaac y Jacob y las imágenes del olivo/remanente vienen del Tanaj antes de cualquier teología eclesial."],
  ],
  "sections": [
    ["Errores opuestos", [
      "Reemplazar a Israel por una institución.",
      "Absolutizar un Estado o un grupo actual sin remanente, Mesías, Torah y testimonio.",
    ]],
    ["Qué sí sostiene el texto", [
      "Remanente por gracia.",
      "Ramas naturales y naciones injertadas.",
      "Humildad de lo injertado.",
      "Torah y testimonio como marcas de fidelidad.",
    ]],
  ],
  "answer": "El Israel de Elohim no es reemplazado por una institución. Es el pueblo de la promesa reunido alrededor de Yehoshúa: remanente, ramas naturales y naciones injertadas, con Torah y testimonio.",
  "sources": [("romanos", "Eric · Romanos"), ("reemplazo1", "Natanael · Reemplazo 1"), ("reemplazo2", "Natanael · Reemplazo 2")],
}

C["deidad"] = {
  "lead": "La pregunta no es “repite una fórmula”. Es: ¿el testimonio presenta a Yehoshúa como Elohim y Adón sin romper el Shemá?",
  "question": "¿Quién es Yehoshúa: Elohim y Adón? ¿Cómo se sostiene junto con Aba?",
  "visual": {
    "src": "/images/fuego-techelet.webp",
    "alt": "Árbol en llamas",
    "why": "La deidad se discute con obras, gloria y confesión, no con adornos dogmáticos."
  },
  "intro": "Si nunca estudiaste esto: el Shemá dice que יהוה es uno. A la vez, el Evangelio da a Yehoshúa obras y confesiones que pertenecen a Elohim. Algunas tradiciones resolvieron eso con “tres personas”. Las clases de trabajo piden volver al texto: obras, confesión, unidad y misión de siervo — sin inventar tres dioses.",
  "passages": [
    {"ref": "Devarim 6:4 · TTH", "text": "Escucha Israel, יהוה nuestro Elohim, יהוה es uno.", "note": "Base: unidad. Cualquier confesión sobre el Mesías vive aquí."},
    {"ref": "Yojanán 1:1, 14 · TTH", "text": "…Elohim era la Palabra… Y la Palabra se hizo carne…", "note": "Identidad y corporeidad juntas."},
    {"ref": "Yojanán 5:21–23 · TTH", "text": "…el Hijo da vida… para que todos honren al Hijo como honran al Padre.", "note": "Dar vida y recibir honra no es lenguaje de mensajero menor."},
    {"ref": "Yojanán 20:28 · TTH", "text": "¡Adón mío y Elohim mío!", "note": "Confesión registrada sin corrección."},
  ],
  "method": [
    "Pon en la mesa el Shemá y los textos de obras/confesión a la vez.",
    "No uses solo escenas de humillación ni solo de gloria.",
    "Pregunta qué significa “ver al Padre” en Yojanán 14.",
    "Examina si tu fórmula multiplica dioses o borra al Mesías.",
  ],
  "lexicon": [
    ["Shemá", "Devarim 6:4: “Escucha Israel… יהוה es uno”. Confesión central de la unidad de Elohim."],
    ["אֱלֹהִים · Elohim", "Palabra hebrea a menudo traducida “Dios”. En las clases: puede ser amor manifiesto, y en otros contextos jueces/mensajeros. El contexto decide."],
    ["אָדוֹן · Adón / κύριος · kyrios", "Señor. En el NT, kyrios a veces traduce el Nombre; no siempre automáticamente — hay que mirar el pasaje."],
    ["Palabra / λόγος · logos", "En Yojanán 1: la expresión/palabra de Elohim que era en el principio y se hizo carne."],
    ["Trinidad (fórmula posterior)", "Doctrina que habla de tres personas en un Dios. Se consolidó en siglos posteriores en el cristianismo. Aquí se examina si esa fórmula es la única lectura del texto."],
    ["Manifestación / siervo", "El Mesías puede ser Elohim revelado en condición de siervo (oración, obediencia) sin ser “otro dios”."],
  ],
  "historical": [
    ["Por qué hay fórmulas trinitarias", "Cuando el mensaje entró en el mundo griego-romano, se usaron categorías de “persona”, “esencia” y concilios. Eso es historia real. No por ser historia se vuelve automáticamente la mejor lectura del Tanaj y del Evangelio."],
    [BASE["segundo_templo"], "El judaísmo del tiempo de Yehoshúa confesaba un solo Elohim y leía al Mesías, la Palabra y la presencia de formas propias, no idénticas a los concilios del siglo IV."],
    [BASE["hebreo"] + " " + BASE["arameo"], "Aba, Elohim, Adón y el Nombre se entienden primero en semítico."],
    [BASE["griego"], "Logos y kyrios deben leerse con el Tanaj abierto, no solo con filosofía griega."],
    ["Natanael Doldan sobre la trinidad", "Enseñanza reciente que confronta adornos de “tres personas / tres maneras” cuando chocan con el Shemá. Se cita como fuente audiovisual de trabajo, no como autoridad canónica."],
  ],
  "sections": [
    ["Dos extremos que fallan", [
      "Reducir a Yehoshúa a un mensajero menor ignorando obras y confesión.",
      "Resolver todo con tres dioses o tres personas sin el Shemá.",
    ]],
    ["Qué sí se puede decir con el texto", [
      "El Mesías recibe honra, da vida y es confesado Elohim y Adón.",
      "Aba se ve en Él; Él ora y obedece como siervo.",
      "Uno no anula lo otro.",
    ]],
  ],
  "answer": "El testimonio no separa a Yehoshúa de toda identidad divina ni multiplica dioses. Se le confiesa Elohim y Adón bajo la unidad del Elohim de Israel, con misión de siervo delante de Aba.",
  "sources": [("deidad", "Eric · Deidad"), ("trinidad", "Natanael · Santísima trinidad"), ("trinidadShema", "Natanael · Shemá"), ("abaDeidad", "Eric · Elohim y Aba")],
}

# Aba - keep rich version with clearer historical for beginners
C["aba"] = {
  "lead": "Si el texto dice “Padre” u “oraba”, no asumas el castellano moderno. Aba y tefilah tienen un campo semítico más amplio.",
  "question": "¿Qué es Aba? ¿Qué es tefilah? ¿Qué fuentes de idioma e historia usa la clase?",
  "visual": {
    "src": "/images/aguas-techelet.webp",
    "alt": "Aguas",
    "why": "Aba como fuente; tefilah como presentarse ante esa Fuente en juicio."
  },
  "intro": "Aba es una palabra aramea que el Evangelio conserva. No significa solo “papá”. En las clases de Eric (Yojanán y Marcos), Aba nombra la Fuente y la plenitud de la promesa. Tefilah no es solo charlar: se explica como entrar en juicio ante el cielo. Abajo se explican las palabras y las fuentes para quien nunca las oyó.",
  "passages": [
    {"ref": "Tehilim 106:30 · TTH", "text": "Y se puso de pie Pinjas y medió (O, juzgó)…", "note": "Raíz פלל: mediar/juzgar — ancla para tefilah como juicio."},
    {"ref": "Markos 1:35 · TTH", "text": "…y allí oró.", "note": "proseuchomai: en la clase se lee vía LXX como presentarse (lehitpallel), no como charla moderna."},
    {"ref": "Markos 14:36 · TTH", "text": "¡Aba, Padre! … no lo que yo quiero, sino lo que tú.", "note": "Presentarse ante la Fuente y allanarse a la voluntad."},
    {"ref": "Tehilim 119:89 · TTH", "text": "…tu palabra se establece en los cielos.", "note": "Palabra inamovible: la tefilah no pelea contra ella."},
    {"ref": "Yojanán 14:9–10 · TTH", "text": "El que me ha visto a Mí, ha visto al Padre…", "note": "Padre = Fuente vista en el Mesías."},
    {"ref": "Yojanán 10:37–38 · TTH", "text": "…las obras… mi Padre es en Mí, y Yo en Él.", "note": "Aba se conoce por las obras de la promesa."},
    {"ref": "Yojanán 14:28 · TTH", "text": "…mi Padre es más grande que Yo.", "note": "Plenitud de promesa, no dios menor."},
  ],
  "method": [
    "No empieces por el castellano “orar = hablar con Dios”.",
    "Mira el griego del pasaje y su eco en la Septuaginta.",
    "Pregunta qué hebreo suele estar detrás (concordancias griego–hebreo; en clase se menciona Hatch–Redpath).",
    "Lee Aba con ejemplos de “padre = origen/principio”, no solo progenitor.",
    "Cuando leas “oraba, Padre”, prueba las sustituciones de la sección final.",
  ],
  "lexicon": [
    ["אַבָּא · Aba", "Arameo: padre. En la enseñanza: Fuente, origen, plenitud de la promesa de Elohim — no solo cariño doméstico."],
    ["אָב · av", "Hebreo: padre, origen, primer grado, principal de una cadena."],
    ["תְּפִלָּה · tefilah", "Oración. En la clase: presentarse y someterse a juicio (raíz פלל), no solo “hablar”."],
    ["לְהִתְפַּלֵּל · lehitpallel", "Forma verbal: presentarse en juicio / confesar. Equivalencia semítica detrás de proseuchomai en la lectura de clase."],
    ["προσεύχομαι · proseuchomai", "Griego del Evangelio para “orar”. Se interpreta con ayuda de la LXX y el hebreo, no solo con el diccionario moderno."],
    ["אבות מלאכות · avot melakhot", "En la Mishná: 39 categorías “padre” del trabajo prohibido en Shabat. Ejemplo de que “padre” puede significar categoría principal, no papá."],
    ["אַב בֵּית דִּין · av beit din", "“Padre de la casa de juicio”: el principal de un tribunal judío. Ejemplo institucional de “padre” como autoridad/principio."],
    ["εὐλογέω / בָּרַךְ", "Bendecir: confesar a Elohim como fuente de provisión (p. ej. pan y copa)."],
    ["ἐντυγχάνω · entynchano", "En Yojanán 17: gestionar/procurar a favor de otros según promesas, no “rogar” genérico."],
  ],
  "historical": [
    [BASE["arameo"], "Aba es arameo. El Evangelio a veces conserva palabras arameas porque formaban parte del habla real del ambiente de Yehoshúa."],
    [BASE["segundo_templo"], "En ese mundo se oraba, se leía la Torah y se pensaba en juicio y presencia de Elohim. “Presentarse ante el cielo” no es una idea inventada en la Edad Media."],
    [BASE["mishna"], "Se usa solo como ejemplo de idioma y cultura: avot melakhot muestra usos de “padre” = categoría originante. No es autoridad por encima de la Escritura."],
    ["Av beit din (institución judía)", "En la organización de tribunales, el “padre de la casa de juicio” es un cargo. Sirve de ejemplo lingüístico: padre = principal de un tribunal."],
    [BASE["lxx"] + " Hatch–Redpath es una concordancia impresa que lista qué hebreo suele corresponder a cada griego de la LXX. La clase usa esa lógica de trabajo: griego → LXX → hebreo."],
    ["Tribunal en el Tanaj", "Zacarías 3 describe un protocolo de corte celestial; Daniel 7 muestra tronos y juicio; Tehilim 110 trae un edicto. Eso da marco literario a “presentarse al cielo”."],
    ["Tehilim 106:30", "Pinjas “juzga/media”: ancla bíblica para conectar tefilah con juicio/mediación."],
    ["Advertencia de rigor", "No todo lo mencionado en una clase oral está cotejado al detalle (p. ej. algunas citas de Zohar o Targum). Aquí priorizamos lo anclado en Tanaj, Evangelio, mishná como ejemplo cultural y método LXX."],
  ],
  "sections": [
    ["Cuando leas “oraba” o “Padre”", [
      "oraba → se presentó · entró en juicio · se sometió a la palabra.",
      "Padre → Aba · Fuente · origen de la promesa · palabra en los cielos.",
      "oraba al Padre → se presentó ante la Fuente y se allanó a su voluntad.",
      "el Padre es mayor → la plenitud de la Fuente es mayor que la manifestación en siervo.",
      "el que me ve ha visto al Padre → ver al Mesías es ver la Fuente manifestada.",
    ]],
    ["Tefilah en Getsemaní", [
      "“Pase esta copa” es presión real.",
      "“No lo que yo quiero” es entrar bajo la palabra, no evadir el juicio.",
    ]],
  ],
  "answer": "Aba es la Fuente y la plenitud de la promesa. Tefilah es presentarse y entrar en juicio ante esa Fuente. Se sostiene con léxico semítico, ejemplos culturales judíos (explicados) y el método griego→LXX→hebreo. “Oraba, Padre” puede oírse: se presentó ante la Fuente y se allanó a su voluntad.",
  "sources": [
    ("abaYojanan10puerta", "Eric · Yojanán 10 puerta"),
    ("abaYojanan10obras", "Eric · Yojanán 10 obras"),
    ("abaYojanan14", "Eric · Yojanán 14"),
    ("tribunalCelestial", "Eric · Tribunal y verbos"),
    ("tribunalCelestial2", "Eric · Continuidad"),
    ("abaDeidad", "Eric · Elohim y Aba"),
  ],
}

C["benhaelohim"] = {
  "lead": "“Hijo de Elohim” no es un cumplido vago. En el Evangelio provoca confesión, acusación y gloria.",
  "question": "¿Qué significa Ben Ha’Elohim? ¿Adopción sentimental o confesión de identidad y revelación?",
  "visual": {
    "src": "/images/montanas-techelet.webp",
    "alt": "Montañas",
    "why": "La filiación se ve en gloria y obras, no en un apodo suave."
  },
  "intro": "En castellano, “hijo” suele evocar biología o cariño. En la Escritura, “hijo de…” también puede marcar herencia, representación y origen. Cuando el Evangelio dice “Hijo de Elohim”, hay que mirar qué entienden discípulos y opositores en la escena.",
  "passages": [
    {"ref": "Matityahu 16:16 · TTH", "text": "Tú eres el Mesías, el Hijo del Elohim viviente.", "note": "Confesión de identidad, no piropo."},
    {"ref": "Yojanán 5:18 · TTH", "text": "…a Elohim llamaba su propio Padre, haciéndose igual a Elohim.", "note": "Los oyentes oyeron igualdad. Esa reacción es parte del testimonio."},
    {"ref": "Yojanán 10:36 · TTH", "text": "…dije: Hijo de Elohim soy.", "note": "Yehoshúa sostiene el título bajo acusación."},
    {"ref": "Hebreos 1:3 · TTH", "text": "…resplandor de su gloria e impronta de su sustancia…", "note": "El Hijo expresa; no solo informa."},
  ],
  "method": [
    "Lee la confesión de Kefa y las acusaciones de igualdad en el mismo mapa.",
    "Compara con títulos de Israel como “hijo” (Éxodo 4:22) y pregunta qué es distinto en el Mesías.",
    "Mantén el Shemá: un Elohim, no dos.",
  ],
  "lexicon": [
    ["בֶּן · ben", "Hijo, heredero, portador. Puede ser literal o de función según el contexto."],
    ["υἱὸς τοῦ θεοῦ · huios tou theou", "Griego: Hijo de Dios/Elohim."],
    ["Monogenēs / yajid", "“Único / de una sola clase”. En discusiones de Yojanán: singularidad del Hijo, no “un hijo más del montón”."],
    ["Filiación de Israel", "Israel es llamado hijo (Éxodo 4:22). Eso no borra la filiación singular del Mesías; da marco de promesa."],
  ],
  "historical": [
    [BASE["segundo_templo"], "Había expectativas mesiánicas y debates sobre quién es el Mesías y cómo se relaciona con Elohim."],
    ["Acusaciones de blasfemia en los Evangelios", "Cuando opositores oyen “igual a Elohim”, el narrador registra un conflicto real del siglo I, no un debate medieval."],
    [BASE["hebreo"], "Ben y títulos de herencia se entienden en el mundo de la promesa a David e Israel."],
    [BASE["griego"], "El título griego debe leerse con el Tanaj abierto."],
  ],
  "sections": [
    ["Qué no es", [
      "Solo “alguien que Dios quiere mucho”.",
      "Un segundo Elohim en pelea con Aba.",
    ]],
    ["Qué sí muestra", [
      "Origen y envío.",
      "Autoridad y revelación.",
      "Unidad con Aba vista en obras.",
    ]],
  ],
  "answer": "Ben Ha’Elohim es confesión de identidad y revelación del Mesías, no una metáfora blanda. Se lee con el Shemá: un Elohim, el Hijo que lo manifiesta.",
  "sources": [("benHaAdam", "Eric · títulos"), ("deidad", "Eric · Deidad")],
}

C["menajem"] = {
  "lead": "Menajem no es “emoción fuerte en el culto”. Es el Consolador prometido: Ruaj de verdad.",
  "question": "¿Quién es el Menajem? ¿Cómo se distingue de un ambiente emotivo?",
  "visual": {
    "src": "/images/aguas-techelet.webp",
    "alt": "Aguas",
    "why": "El Consolador da vida y verdad; no se fabrica con volumen."
  },
  "intro": "Si solo conoces la palabra “Espíritu Santo” en contextos de gritos o música, esta página baja el ritmo. En Yojanán 14–16 Yehoshúa promete un Consolador que enseña, recuerda y glorifica al Mesías. Menajem es la forma hebrea/TTH de ese título.",
  "passages": [
    {"ref": "Yojanán 14:16–17 · TTH", "text": "…otro Consolador… el Espíritu de verdad…", "note": "Promesa de presencia y verdad, no de atmósfera."},
    {"ref": "Yojanán 14:26 · TTH", "text": "…él os enseñará todas las cosas, y os recordará…", "note": "Criterio: enseña y recuerda las palabras de Yehoshúa."},
    {"ref": "Yojanán 16:13–14 · TTH", "text": "…me glorificará…", "note": "Si el centro se mueve al líder o a la sensación, hay que discernir."},
    {"ref": "Gálatas 5:22–23 · TTH", "text": "…fruto del Ruaj… dominio propio.", "note": "El fruto se examina con el tiempo."},
  ],
  "method": [
    "Lee Yojanán 14–16 completo antes de definir “Espíritu” por tu experiencia de culto.",
    "Lista los verbos: enseñar, recordar, glorificar, guiar.",
    "Compara con el fruto de Gálatas 5.",
  ],
  "lexicon": [
    ["מְנַחֵם · Menajem", "Consolador, el que da consuelo/fortaleza. En TTH traduce el título del Paráclito."],
    ["παράκλητος · paraklētos", "Griego: llamado al lado — defensor, abogado, consolador."],
    ["רוּחַ הַקֹּדֶשׁ · Ruaj Ha’Kodesh", "Espíritu/aliento santo de Elohim. “Santo” = apartado, no “espectacular”."],
    ["ἄλλος · allos", "Otro del mismo tipo (en discusiones de “otro Consolador”); no necesariamente “otro rival”."],
    ["Emocionalismo", "Usar la intensidad del sentimiento como prueba automática de verdad. El texto no lo autoriza como criterio final."],
  ],
  "historical": [
    ["Consolación en el Tanaj", "La raíz de consuelo (נחם) aparece en contextos de restauración y alivio real, no solo de “sentirse bien” un momento."],
    [BASE["griego"], "Paraklētos era una palabra entendible en el mundo griego; el Evangelio la llena con la promesa de Yehoshúa."],
    ["Por qué hay abusos modernos", "En siglos recientes, algunos movimientos hicieron de la emoción pública la marca del Ruaj. La página vuelve a Yojanán y a Pablo para medir."],
    [BASE["tth"], "Menajem es la forma que ayuda a oír el título en clave hebrea."],
  ],
  "sections": [
    ["Cómo reconocerlo", [
      "Guía a la verdad de Yehoshúa.",
      "Produce fruto examinable.",
      "No exige apagar el discernimiento.",
    ]],
  ],
  "answer": "El Menajem es el Ruaj Ha’Kodesh prometido: Consolador y Espíritu de verdad que enseña, recuerda y glorifica a Yehoshúa. No es sinónimo de emoción religiosa.",
  "sources": [("abaYojanan14", "Eric · Menajem en Yojanán 14")],
}

C["emunah"] = {
  "lead": "Emunah no es “sentir fuerte que algo es verdad”. Es firmeza y fidelidad recibidas al oír.",
  "question": "¿Qué es la emunah hebrea frente a una fe solo emocional o solo mental?",
  "visual": {
    "src": "/images/aguas-techelet.webp",
    "alt": "Aguas",
    "why": "La emunah se recibe y sostiene; no se inventa en el momento."
  },
  "intro": "En muchas iglesias, “fe” suena a emoción o a esfuerzo interior. En hebreo, emunah se relaciona con firmeza y fidelidad (la misma familia de “amén”). El griego pistis del Evangelio debe leerse dentro de ese mundo, no como “opinión religiosa”.",
  "passages": [
    {"ref": "Romanos 10:17 · TTH", "text": "…la emunah proviene del oír… por la Palabra del Mesías.", "note": "Origen: oír la Palabra."},
    {"ref": "Markos 11:22 · TTH", "text": "Haya para ustedes emunah de Elohim.", "note": "Se recibe en relación con Elohim."},
    {"ref": "Gálatas 5:22 · TTH", "text": "…fruto del Rúaj… emunah…", "note": "También es fruto que crece."},
    {"ref": "Habacuc 2:4 · marco", "text": "El justo por su emunah vivirá.", "note": "Línea profética: modo de vida, no un instante emotivo."},
  ],
  "method": [
    "Pregunta en cada pasaje: ¿confianza, fidelidad, perseverancia, o fidelidad de Elohim?",
    "No uses solo “yo siento que…”.",
    "Mira el fruto con el tiempo.",
  ],
  "lexicon": [
    ["אֱמוּנָה · emunah", "Firmeza, fidelidad, confianza estable. Familia de אמן (amén: “es firme/verdadero”)."],
    ["πίστις · pistis", "Griego: fe/fidelidad/confianza según contexto."],
    ["אָמֵן · amén", "Asentimiento a lo firme y verdadero; no una fórmula mágica."],
    ["Oír (shema)", "En la Escritura, oír implica recibir y responder, no solo percibir sonido."],
  ],
  "historical": [
    [BASE["hebreo"], "La raíz de emunah está en el Tanaj mucho antes del castellano “fe”."],
    [BASE["griego"], "Pablo escribe pistis en griego a comunidades mixtas, pero cita y piensa con el Tanaj."],
    ["Habacuc y Pablo", "“El justo por su emunah vivirá” es un puente clásico entre profetas y cartas; muestra continuidad, no una religión nueva de emociones."],
    [BASE["tth"], "TTH prefiere “emunah” para no aplanar el término a “fe” sentimental."],
  ],
  "sections": [
    ["Por qué no nace de la emoción", [
      "La emoción puede acompañar.",
      "La fuente es el oír y el Ruaj.",
      "Una “fe” que solo existe en el ambiente del culto no es la emunah del texto.",
    ]],
  ],
  "answer": "La emunah es firmeza y fidelidad recibidas al oír la Palabra del Mesías. No es autosugestión emocional.",
  "sources": [],
}

C["ruaj"] = {
  "lead": "“Vivir bajo el Ruaj” no significa vivir de subidones. Significa vida que produce obediencia y fruto.",
  "question": "¿Qué significa vivir bajo el Ruaj frente al emocionalismo?",
  "visual": {
    "src": "/images/fruto-techelet.webp",
    "alt": "Fruto",
    "why": "El fruto se ve con el tiempo."
  },
  "intro": "Ruaj en hebreo puede ser viento, aliento o espíritu según el contexto. En la promesa de Yejezqel, Elohim pone su Ruaj para hacer andar en sus estatutos. Eso es muy distinto de usar la emoción como autoridad.",
  "passages": [
    {"ref": "Yejezqel 36:26–27 · TTH", "text": "…pondré mi Ruaj… y haré que andéis en mis estatutos…", "note": "Ruaj unido a andar en los estatutos."},
    {"ref": "Gálatas 5:16–17 · TTH", "text": "Andad en el Ruaj, y no satisfagáis el deseo de la carne.", "note": "Dirección de vida, no clima de reunión."},
    {"ref": "Gálatas 5:22–23 · TTH", "text": "…fruto del Ruaj… dominio propio.", "note": "Lista examinable."},
    {"ref": "1 Yojanán 4:1 · TTH", "text": "…probad los espíritus…", "note": "Mandato de prueba."},
  ],
  "method": [
    "Define Ruaj por promesa y fruto, no por gritos.",
    "Pregunta: ¿esta experiencia produce obediencia y dominio propio?",
    "Prueba los espíritus con la Escritura.",
  ],
  "lexicon": [
    ["רוּחַ · ruaj", "Viento, aliento, espíritu, a veces ánimo/mente según el pasaje."],
    ["πνεῦμα · pneuma", "Griego: espíritu/aliento. En el NT traduce el campo de Ruaj."],
    ["Fruto", "Resultado visible y sostenido en el carácter (Gálatas 5), no un momento de euforia."],
    ["Carne (sarx) en Pablo", "A veces el cuerpo, a veces la tendencia al pecado. El contexto decide."],
  ],
  "historical": [
    ["Profetas y el Ruaj", "El Tanaj habla del Ruaj de יהוה sobre jueces, profetas y en promesas de renovación (Yejezqel, Yoel). No es un invento del siglo XX."],
    ["Movimientos modernos de emoción pública", "Algunos avivamientos y corrientes pentecostales/carismáticas hicieron de la intensidad la prueba. Hay que medirlos con el texto, no al revés."],
    [BASE["hebreo"], "Ruaj es más flexible que la palabra castellana “espíritu”."],
    [BASE["griego"], "Pneuma en Pablo se entiende con el Tanaj abierto."],
  ],
  "sections": [
    ["Qué no significa", [
      "Que toda emoción sea del Ruaj.",
      "Que el orden y el discernimiento queden abolidos.",
    ]],
  ],
  "answer": "Vivir bajo el Ruaj es recibir vida que produce obediencia, verdad y fruto. No es sinónimo de ambiente emotivo.",
  "sources": [],
}

write_module("conceptos.js", "conceptosReadings", C, [
  "benhaadam","corporeidad","nombre","israel","deidad","aba",
  "benhaelohim","menajem","emunah","ruaj"
])

print("conceptos done")
