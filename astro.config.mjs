// @ts-check
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  site: "https://4safety.com.br",
  redirects: {
    "/produtos/respiratorio": "/produtos/mascaras-respiradores",
  },
});

