// @ts-check
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  redirects: {
    "/produtos/respiratorio": "/produtos/mascaras-respiradores",
  },
});

