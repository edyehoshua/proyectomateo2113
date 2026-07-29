import { conceptosReadings } from "./conceptos.js";
import { profeciaReadings } from "./profecia.js";
import { torahReadings } from "./torah.js";

export const readings = {
...conceptosReadings,
...profeciaReadings,
...torahReadings
};
