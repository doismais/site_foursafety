PORT ?= 8080
PYTHON ?= python3
PNPM ?= pnpm

.DEFAULT_GOAL := help

.PHONY: help install setup dev serve build sync-nav visuals check audit

help:
	@echo "4Safety — comandos disponíveis"
	@echo "──────────────────────────────"
	@echo "make install   # instala o ferramental Node do projeto"
	@echo "make dev       # sobe servidor local e abre navegador no macOS"
	@echo "make serve     # sobe servidor local sem abrir navegador"
	@echo "make build     # regenera páginas do catálogo em produtos/"
	@echo "make sync-nav  # sincroniza navegação entre páginas HTML"
	@echo "make visuals   # executa script auxiliar de ajustes visuais"
	@echo "make check     # valida todas as páginas HTML do projeto"
	@echo "make audit     # roda auditoria do ferramental Node"

# Instala o ferramental leve usado em validação e auditoria
install setup:
	@echo "4Safety: instalando dependências com pnpm..."
	@$(PNPM) install --ignore-workspace
	@echo "Pronto. Use: make dev, make build, make check"

# Sobe servidor estático e abre o navegador (macOS: open)
dev:
	@echo "4Safety — http://127.0.0.1:$(PORT) (Ctrl+C para encerrar)"
	@(sleep 1; open "http://127.0.0.1:$(PORT)" 2>/dev/null || true) &
	@$(PYTHON) -m http.server $(PORT)

# Apenas o servidor, sem abrir o navegador
serve:
	@$(PYTHON) -m http.server $(PORT)

# Regenera páginas internas do catálogo
build:
	@echo "4Safety: regenerando catálogo interno..."
	@$(PYTHON) scripts/gen_products.py

# Sincroniza navegação entre páginas HTML
sync-nav:
	@echo "4Safety: sincronizando navegação..."
	@$(PYTHON) scripts/sync_nav.py

# Script auxiliar de refinamento visual
visuals:
	@echo "4Safety: aplicando ajustes visuais auxiliares..."
	@$(PYTHON) scripts/apply_premium_visuals.py

# Auditoria de segurança do ferramental Node
audit:
	@$(PNPM) audit --ignore-workspace

# Lint HTML (HTMLHint via pnpm/npx + checagens Python)
check:
	@./scripts/check.sh
