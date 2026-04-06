PORT ?= 8080

.PHONY: install setup dev serve check audit

# Comandos core
install setup:
	@echo "4Safety: instalando dependências com pnpm..."
	pnpm install
	@echo "Pronto! Comandos disponíveis: make dev, make serve, make check"

# Sobe servidor estático e abre o navegador (macOS: open)
dev:
	@echo "4Safety — http://127.0.0.1:$(PORT) (Ctrl+C para encerrar)"
	@(sleep 1; open "http://127.0.0.1:$(PORT)" 2>/dev/null || true) &
	python3 -m http.server $(PORT)

# Apenas o servidor, sem abrir o navegador
serve:
	python3 -m http.server $(PORT)

# Auditoria de segurança
audit:
	pnpm audit

# Lint HTML (HTMLHint via npx + checagens Python)
check:
	@./scripts/check.sh
