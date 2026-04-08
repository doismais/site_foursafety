#!/usr/bin/env node

/**
 * Color sync utility for static projects.
 *
 * Replaces one base color across:
 * - Hex tokens (#ff4e00)
 * - rgb()/rgba() comma syntax (rgba(255, 78, 0, 0.2))
 * - rgb()/rgba() space syntax (rgb(255 78 0 / 0.2))
 *
 * Default behavior is DRY-RUN.
 * Use --apply to write changes to disk.
 *
 * Examples:
 *   node scripts/sync_color.mjs --old ff4e00 --new ff0000
 *   node scripts/sync_color.mjs --old #ff4e00 --new #ff0000 --apply
 *   node scripts/sync_color.mjs --old ff4e00 --new ff0000 --apply --ext html,css,js
 */

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const cwd = process.cwd();
const selfPath = fileURLToPath(import.meta.url);

const DEFAULT_EXTENSIONS = new Set([".html", ".css", ".js", ".mjs", ".svg"]);
const DEFAULT_IGNORED_DIRS = new Set([
  ".git",
  "node_modules",
  ".pnpm-store",
  ".vercel",
  ".claude",
]);

function parseArgs(argv) {
  const args = {
    old: null,
    next: null,
    apply: false,
    extensions: new Set(DEFAULT_EXTENSIONS),
    include: ["."],
  };

  for (let i = 0; i < argv.length; i += 1) {
    const raw = argv[i];
    if (raw === "--apply") {
      args.apply = true;
      continue;
    }
    if (raw === "--old") {
      args.old = argv[i + 1];
      i += 1;
      continue;
    }
    if (raw === "--new") {
      args.next = argv[i + 1];
      i += 1;
      continue;
    }
    if (raw === "--ext") {
      const value = argv[i + 1] || "";
      i += 1;
      args.extensions = new Set(
        value
          .split(",")
          .map((x) => x.trim())
          .filter(Boolean)
          .map((x) => (x.startsWith(".") ? x.toLowerCase() : `.${x.toLowerCase()}`)),
      );
      continue;
    }
    if (raw === "--include") {
      const value = argv[i + 1] || "";
      i += 1;
      args.include = value
        .split(",")
        .map((x) => x.trim())
        .filter(Boolean);
      continue;
    }
  }

  if (!args.old || !args.next) {
    throw new Error(
      "Uso: node scripts/sync_color.mjs --old <hex> --new <hex> [--apply] [--ext html,css,js] [--include .]",
    );
  }

  return args;
}

function normalizeHex(input) {
  const clean = String(input || "").trim().replace(/^#/, "").toLowerCase();
  if (!/^[0-9a-f]{6}$/.test(clean)) {
    throw new Error(`Hex inválido: ${input}`);
  }
  return clean;
}

function hexToRgb(hex) {
  return {
    r: Number.parseInt(hex.slice(0, 2), 16),
    g: Number.parseInt(hex.slice(2, 4), 16),
    b: Number.parseInt(hex.slice(4, 6), 16),
  };
}

function replaceColorInContent(content, oldHex, nextHex) {
  const oldRgb = hexToRgb(oldHex);
  const nextRgb = hexToRgb(nextHex);
  let nextContent = content;
  let replacements = 0;

  // 1) Hex (#ff4e00)
  const hexRegex = new RegExp(`#${oldHex}\\b`, "gi");
  nextContent = nextContent.replace(hexRegex, () => {
    replacements += 1;
    return `#${nextHex}`;
  });

  // 2) rgb()/rgba() comma syntax:
  //    rgba(255, 78, 0, 0.2)
  //    rgb(255, 78, 0)
  const commaRegex = new RegExp(
    String.raw`(rgb|rgba)\(\s*${oldRgb.r}\s*,\s*${oldRgb.g}\s*,\s*${oldRgb.b}(?:\s*,\s*([^)]+?))?\s*\)`,
    "gi",
  );
  nextContent = nextContent.replace(commaRegex, (_, fn, alphaRaw) => {
    replacements += 1;
    if (alphaRaw !== undefined) {
      return `rgba(${nextRgb.r}, ${nextRgb.g}, ${nextRgb.b}, ${alphaRaw.trim()})`;
    }
    return `rgb(${nextRgb.r}, ${nextRgb.g}, ${nextRgb.b})`;
  });

  // 3) rgb()/rgba() space syntax:
  //    rgb(255 78 0 / 0.2)
  //    rgb(255 78 0)
  const spaceRegex = new RegExp(
    String.raw`(rgb|rgba)\(\s*${oldRgb.r}\s+${oldRgb.g}\s+${oldRgb.b}(?:\s*\/\s*([^)]+?))?\s*\)`,
    "gi",
  );
  nextContent = nextContent.replace(spaceRegex, (_, _fn, alphaRaw) => {
    replacements += 1;
    if (alphaRaw !== undefined) {
      return `rgb(${nextRgb.r} ${nextRgb.g} ${nextRgb.b} / ${alphaRaw.trim()})`;
    }
    return `rgb(${nextRgb.r} ${nextRgb.g} ${nextRgb.b})`;
  });

  return { content: nextContent, replacements };
}

async function walkFiles(startPath, extensions, acc = []) {
  const stat = await fs.stat(startPath);
  if (stat.isFile()) {
    if (extensions.has(path.extname(startPath).toLowerCase())) {
      acc.push(startPath);
    }
    return acc;
  }

  const entries = await fs.readdir(startPath, { withFileTypes: true });
  for (const entry of entries) {
    const full = path.join(startPath, entry.name);
    if (entry.isDirectory()) {
      if (DEFAULT_IGNORED_DIRS.has(entry.name)) continue;
      await walkFiles(full, extensions, acc);
    } else if (entry.isFile()) {
      if (extensions.has(path.extname(entry.name).toLowerCase())) {
        acc.push(full);
      }
    }
  }
  return acc;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const oldHex = normalizeHex(args.old);
  const nextHex = normalizeHex(args.next);

  const includeRoots = args.include.map((p) => path.resolve(cwd, p));
  const files = [];

  for (const root of includeRoots) {
    await walkFiles(root, args.extensions, files);
  }

  let totalFiles = 0;
  let totalReplacements = 0;
  const touched = [];

  for (const file of files) {
    if (path.resolve(file) === path.resolve(selfPath)) continue;

    const raw = await fs.readFile(file, "utf8");
    const { content, replacements } = replaceColorInContent(raw, oldHex, nextHex);
    if (replacements === 0) continue;

    totalFiles += 1;
    totalReplacements += replacements;
    touched.push({
      file: path.relative(cwd, file),
      replacements,
    });

    if (args.apply) {
      await fs.writeFile(file, content, "utf8");
    }
  }

  const mode = args.apply ? "APPLY" : "DRY-RUN";
  console.log(`[sync_color] mode=${mode}`);
  console.log(`[sync_color] old=#${oldHex} -> new=#${nextHex}`);
  console.log(`[sync_color] arquivos afetados=${totalFiles}, substituições=${totalReplacements}`);

  for (const item of touched) {
    console.log(` - ${item.file} (${item.replacements})`);
  }
}

main().catch((err) => {
  console.error(`[sync_color] erro: ${err.message}`);
  process.exit(1);
});
