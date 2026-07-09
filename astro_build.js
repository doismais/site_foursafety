#!/usr/bin/env node
"use strict";

async function main() {
  return import("file:///Users/nettomello/CODIGOS/node_modules/.pnpm/astro@7.3.1_@vercel+blob@2.3.0_rollup@4.60.3_terser@5.47.1_tsx@4.21.0/node_modules/astro/dist/cli/index.js")
    .then(({ cli }) => cli(process.argv))
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
}

main()
  .then(() => process.exit(0))
  .catch(() => process.exit(1));
