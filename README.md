# Proyecto Mateo 2113

Archivo público de información y testimonio: volver al texto para examinar enseñanzas sobre Yehoshúa HaMashíaj, la profecía, la Torah y la vida bajo el Ruaj.

## Contenido y fuentes

El trabajo editorial usa dos proyectos de apoyo (no se publican transcripciones completas):

| Repo | Uso |
| --- | --- |
| [Proyecto Shaul](https://shaul.vercel.app) | Notas, inventarios de video, transcripciones privadas, índice de fuentes |
| [Davar](https://davar.bible) | Corpus bíblico (TTH, OE, Delitzsch, etc.) para citar con rigor |

### Canales de video (únicos autorizados)

- [Eric de Jesús Rodríguez Mendoza](https://www.youtube.com/@EricdeJes%C3%BAsRodr%C3%ADguezMendoza)
- [Somos el Cuerpo del Mesías](https://www.youtube.com/@SomosElCuerpodelMesias) (Natanael Doldan)

Las transcripciones se descargan con **Supadata** solo para esos canales. La configuración de trabajo y sus instrucciones están documentadas en [Proyecto Shaul](https://shaul.vercel.app). Ver `AGENTS.md` y `src/config/channels.js`.

En el sitio público: enlace al video, marca de tiempo si aplica, cita breve y análisis propio.

## Estructura del código

```text
src/main.js              entrada
src/router.js            rutas hash
src/config/              canales y enlaces YouTube
src/content/             páginas, secciones, lecturas por tema
src/content/readings/    cuerpos de cada tema (modular)
src/views/               render HTML
src/data/                datos especiales (mandamientos)
styles.css
docs/                    tesis, inventario editorial, arquitectura
```

## Desarrollo local

```bash
bun install
bun run dev
```

Disponible en `http://127.0.0.1:2113`.

## Build y Cloudflare Pages

```bash
bun run build
bun run pages:dev
bun run deploy
```

Salida estática en `dist/`. Build command: `bun run build`, output directory: `dist`.
