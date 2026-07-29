# Proyecto Mateo 2113 — agent guide

## Purpose

Public information and testimony site. Editorial synthesis, not an official channel of its teachers.

## Content sources (required)

| Role | Path | Use |
| --- | --- | --- |
| Study notes, inventories, transcripts | `~/shaul` | Primary private workbench |
| Scripture corpora (TTH, OE, Delitzsch, …) | `~/davar` | Verse text for citations |
| Local scripture mirror in shaul | `~/shaul/docs/scriptures` | Prefer when already synced from davar |

### Audiovisual teachers

Transcripts and class notes come from these YouTube channels **only**:

1. **Eric de Jesús Rodríguez Mendoza** — https://www.youtube.com/@EricdeJes%C3%BAsRodr%C3%ADguezMendoza  
   - Inventory: `~/shaul/data/inventories/ericdejes.json`  
   - Transcripts: `~/shaul/private/transcripts/ericdejes/`
2. **Natanael Doldan · Somos el Cuerpo del Mesías** — https://www.youtube.com/@SomosElCuerpodelMesias  
   - TTH translation used with permission for verse quotes  
   - Inventory: `~/shaul/data/inventories/somoselcuerpodelmesias.json`  
   - Transcripts: `~/shaul/private/transcripts/somoselcuerpodelmesias/`

Do **not** fetch or publish transcripts from other channels with project credits.

### Supadata

- API key is already configured (env `SUPADATA_API_KEY` or `~/.config/shaul/supadata.env`).
- Run transcript jobs **from `~/shaul`**, not from this repo:

```bash
cd ~/shaul
npm run transcript -- "https://www.youtube.com/watch?v=VIDEO_ID"
# or batch against an inventory
npm run supadata -- data/inventories/ericdejes.json --video-id VIDEO_ID
npm run sources:db:search -- "keyword"
```

- Credits are limited: fetch only what you need for a topic under development.
- **Never publish full transcripts.** Public site uses: video link, optional timestamp, short quote, original analysis.

### Publication rules

- Site does not speak for the teachers.
- Prefer TTH wording for Spanish scripture quotes when available (credit Natanael Doldan / TTH).
- Hebrew/Greek study: use davar/shaul scripture JSON before inventing text.
- Tetragrammaton as יהוה in content when the divine name is written.

## Code layout (modular)

```text
src/
  main.js                 entry
  router.js               hash routes
  config/
    channels.js           allowed channels + shaul/davar paths
    sources.js            public YouTube links + catalog
  content/
    pages.js              route metadata + render binding
    sections.js           section indexes
    readings/
      conceptos.js        topic bodies (conceptos)
      profecia.js
      torah.js
      index.js
  data/
    commandments.js      mandamientos special page data
  views/                  HTML renderers
styles.css
index.html
docs/                     editorial notes
```

### Reading shape

Each topic in `src/content/readings/*.js`:

- `lead` — opens under the question  
- `visual` — `{ src, alt, why }`  
- `intro`  
- `passages` — `[{ ref, text, note }]` (cite and explain)  
- `sections` — `[[title, body], …]`  
- `sources` — optional `[[url, label], …]`

Edit one section file when developing a topic. Keep pages large and scroll-friendly: question → image → passages → body.

## UI rules (current)

- Navbar: Inicio · Conceptos · Profecía · Torah y Evangelio · Fuentes  
- No separate “Textos” section; verses live inside each topic  
- No “ruta sugerida” sidebars  
- Minimal home: three sections, not every topic listed

## Dev

```bash
bun install
bun run dev    # http://127.0.0.1:2113
bun run build
```
