import { defineConfig } from "vite";

export default defineConfig({
  server: {
    host: "127.0.0.1",
    port: 2113,
  },
  preview: {
    host: "127.0.0.1",
    port: 2113,
  },
  build: {
    outDir: "dist",
    emptyOutDir: true,
  },
});
