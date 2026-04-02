PORT ?= 8080

.PHONY: install setup dev serve check

# Projeto estático: sem package.json e sem dependências para instalar
install setup:
	@echo "4Safety: projeto estático (sem npm/pnpm)."
	@echo "Comandos disponíveis:"
	@echo "  make dev    # sobe servidor e abre navegador"
	@echo "  make serve  # sobe servidor sem abrir navegador"
	@echo "  make check  # valida HTML e estrutura"

# Sobe servidor estático e abre o navegador (macOS: open)
dev:
	@echo "4Safety — http://127.0.0.1:$(PORT) (Ctrl+C para encerrar)"
	@(sleep 1; open "http://127.0.0.1:$(PORT)" 2>/dev/null || true) &
	python3 -m http.server $(PORT)

# Apenas o servidor, sem abrir o navegador
serve:
	python3 -m http.server $(PORT)

# Lint HTML (HTMLHint via npx + checagens Python)
check:
	@./scripts/check.sh
