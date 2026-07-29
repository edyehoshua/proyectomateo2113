---
title: "Arquitectura de la página"
description: "Navegación y formato editorial para una página de información y testimonio"
date: 2026-07-27
tags:
  - web
  - arquitectura
  - editorial
---

# Navegación principal

La página no se presentará como un curso ni como una colección de estudios. Será un archivo de información y testimonio organizado por preguntas.

```text
Inicio
├── Conceptos
├── Profecía
├── Torah y Evangelio
└── Fuentes
```

La navbar muestra solo las secciones (no todos los artículos). Cada tema se abre desde la sección o desde el índice de inicio. No hay sección separada de “Textos”: los versículos van dentro de cada tema.

## Inicio

Mensaje inicial sugerido:

> No te pedimos que nos creas. Te invitamos a examinar las enseñanzas, leer los textos en contexto y conocer quién es Yehoshúa HaMashíaj.

La portada debe explicar el propósito en pocas líneas y ofrecer tres entradas directas:

- ¿Quién es Yehoshúa?
- ¿Cómo se debe leer la profecía?
- ¿Qué significa vivir bajo el Ruaj?

## Conceptos clave

Páginas implementadas o en desarrollo editorial:

- `#/benhaadam` — Bar Enash / Ben HaAdam
- `#/benhaelohim` — Ben Ha’Elohim
- `#/corporeidad` — corporeidad de Yehoshúa
- `#/nombre` — por qué se le llama Yehoshúa
- `#/israel` — Israel de Elohim
- `#/deidad` — Elohim y Adón
- `#/aba` — Abá y tefilah
- `#/menajem` — Menajem y Ruaj Ha’Kodesh
- `#/emunah` — emunah hebrea y pistis griega
- `#/ruaj` — vivir bajo el Ruaj
- `#/mandamientos-yehoshua` — los diez mandamientos como invitación a examinar la vida
- `#/lenguas` — lenguas y discernimiento
- `#/nicolaismo` — nicolaismo y autoridad
- `#/religion` — por qué el cristianismo es una religión

## Profecía

Páginas implementadas o en desarrollo editorial:

- `#/profecia` — guía general
- `#/apocalipsis` — símbolo, contexto y literalidad
- `#/benhaadam` — Daniel 7 y Bar Enash
- `#/isaias19` — Egipto, Asiria e Israel
- `#/isaias56` — casa de oración, extranjeros y eunucos

## Torah y Evangelio

Páginas implementadas o en desarrollo editorial:

- `#/torah` — Torah y Evangelio
- `#/mandamientos` — mandamientos y Evangelio
- `#/galatas` — Gálatas y judaizar
- `#/romanos11` — Romanos 11, Israel y las naciones
- `#/ruaj` — el Ruaj y la Torah
- `#/gratuito` — recibir y dar gratuitamente

## Dos preguntas transversales

La navegación debe ofrecer dos artículos de entrada que conecten identidad, nombre y pueblo:

- **¿Por qué se le llama Yehoshúa?** El nombre como señal de salvación y revelación, sin convertir una etimología en una fórmula mágica ni cerrar prematuramente las cuestiones de pronunciación.
- **¿Cuál es el Israel de Elohim?** El remanente, el olivo, las ramas naturales y las ramas injertadas, sin reemplazar a Israel por una institución ni borrar las promesas a las ramas naturales.

## Marco de fuentes

La ruta `#/textos` contiene una selección breve de citas de la TTH con atribución visible. En la Besorah, cada palabra destacada puede abrir su término griego y su correspondiente forma del hebreo de Delitzsch. En el Tanaj, la capa aramea se presenta separada y con su fuente específica; no se la debe confundir con la TTH.

Cada artículo lingüístico debe contener una tabla breve con cuatro niveles:

| Nivel | Pregunta |
| --- | --- |
| Texto griego | ¿Qué palabra y construcción aparecen realmente? |
| Tanaj citado o aludido | ¿Qué pasaje hebreo/arameo está detrás? |
| Contexto judío | ¿Qué mundo cultural presupone la escena? |
| Conclusión | ¿Qué se puede afirmar y qué queda pendiente? |

## Formato de cada página

Cada artículo debe responder una sola pregunta y contener:

1. **Pregunta principal**
2. **Enseñanza examinada**
3. **Fuente original**: video, enlace e instante
4. **Texto bíblico relevante**
5. **Contexto**
6. **Comparación**
7. **Veredicto**
8. **Preguntas para seguir leyendo**
9. **Fuentes y correcciones**

El veredicto debe utilizar una categoría explícita: confirmado, posible, no demostrado, contradice el contexto, contradice otros pasajes o práctica no probada por el texto.
