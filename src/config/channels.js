/**
 * Allowed audiovisual sources for this project.
 * Transcripts (Supadata) must only be fetched for these channels.
 * Full transcripts stay private in ~/shaul — the public site uses
 * links, timestamps, short quotes, and original analysis.
 */

export const channels = {
  eric: {
    id: "ericdejes",
    name: "Eric de Jesús Rodríguez Mendoza",
    url: "https://www.youtube.com/@EricdeJes%C3%BAsRodr%C3%ADguezMendoza",
    inventory: "~/shaul/data/inventories/ericdejes.json",
    transcripts: "~/shaul/private/transcripts/ericdejes"
  },
  natanael: {
    id: "somoselcuerpodelmesias",
    name: "Natanael Doldan · Somos el Cuerpo del Mesías",
    url: "https://www.youtube.com/@SomosElCuerpodelMesias",
    inventory: "~/shaul/data/inventories/somoselcuerpodelmesias.json",
    transcripts: "~/shaul/private/transcripts/somoselcuerpodelmesias"
  }
};

export const contentRoots = {
  shaul: "~/shaul",
  davar: "~/davar",
  scriptures: "~/shaul/docs/scriptures",
  davarTth: "~/davar/data/tth_2/json",
  davarOe: "~/davar/data/oe",
  davarDelitzsch: "~/davar/data/delitzsch"
};

export const supadata = {
  envFile: "~/.config/shaul/supadata.env",
  envVar: "SUPADATA_API_KEY",
  commands: {
    single: 'cd ~/shaul && python3 scripts/supadata_transcripts.py data/inventories/SOMOS_OR_ERIC.json --video-id VIDEO_ID',
    batch: "cd ~/shaul && python3 scripts/supadata_transcripts.py data/inventories/somoselcuerpodelmesias.json",
    search: 'cd ~/shaul && npm run sources:db:search -- "keyword"'
  },
  rule: "Only fetch transcripts for Eric de Jesús Rodríguez Mendoza and Somos el Cuerpo del Mesías (Natanael Doldan)."
};
