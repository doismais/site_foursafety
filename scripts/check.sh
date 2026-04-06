#!/usr/bin/env bash
# Checagem de código — HTML (HTMLHint + validações locais em Python).
# Uso: ./scripts/check.sh   |   make check
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
mapfile -t HTML_FILES < <(rg --files -g '*.html' . | sort)

echo "4Safety — checagem de código"
echo "────────────────────────────"
echo ""

if [[ "${#HTML_FILES[@]}" -eq 0 ]]; then
  echo "ERRO: nenhum arquivo HTML encontrado em $ROOT" >&2
  exit 1
fi

EXIT=0

if command -v pnpm >/dev/null 2>&1; then
  echo "→ HTMLHint (pnpm dlx)"
  if ! pnpm dlx htmlhint "${HTML_FILES[@]}"; then
    EXIT=1
  fi
elif command -v npx >/dev/null 2>&1; then
  echo "→ HTMLHint (npx)"
  if ! npx --yes htmlhint "${HTML_FILES[@]}"; then
    EXIT=1
  fi
elif command -v htmlhint >/dev/null 2>&1; then
  echo "→ HTMLHint (PATH)"
  if ! htmlhint "${HTML_FILES[@]}"; then
    EXIT=1
  fi
else
  echo "AVISO: pnpm/npx/htmlhint não encontrados — instale Node.js para rodar HTMLHint." >&2
  echo "        Checagens em Python continuam abaixo." >&2
fi

echo ""
echo "→ Estrutura e acessibilidade (Python)"
if ! python3 - "${HTML_FILES[@]}" <<'PY'
import re
import sys
from pathlib import Path

had_errors = False

for file_arg in sys.argv[1:]:
    path = Path(file_arg)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"ERRO [{path}]: leitura: {e}", file=sys.stderr)
        had_errors = True
        continue

    errs: list[str] = []
    strip = text.lstrip()
    if not strip.upper().startswith("<!DOCTYPE"):
        errs.append("O arquivo deve começar com <!DOCTYPE …>")
    low = text.lower()
    if low.count("<html") < 1:
        errs.append("Falta elemento <html>")
    if low.count("</html>") < 1:
        errs.append("Falta </html>")
    if "<head" not in low:
        errs.append("Falta <head>")
    if "<body" not in low:
        errs.append("Falta <body>")
    if "<title" not in low:
        errs.append("Falta <title>")

    for i, m in enumerate(re.finditer(r"<img\b[^>]*>", text, re.IGNORECASE), start=1):
        tag = m.group(0)
        if not re.search(r"\balt\s*=", tag, re.IGNORECASE):
            errs.append(f'<img> #{i} sem atributo alt')

    if errs:
        had_errors = True
        for e in errs:
            print(f"ERRO [{path}]: {e}", file=sys.stderr)

if had_errors:
    sys.exit(1)
print("OK")
PY
then
  EXIT=1
fi

echo ""
if [[ "$EXIT" -eq 0 ]]; then
  echo "Todas as checagens passaram."
else
  echo "Checagem concluída com erros." >&2
fi
exit "$EXIT"
