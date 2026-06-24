# ========================================
#          4SAFETY · MAKEFILE
# ========================================
# Status: ACTIVE
# Version: v1.0.4
# ========================================

PNPM ?= pnpm

.DEFAULT_GOAL := help

.PHONY: help install dev build preview clean check safe-push

help:
	@echo "4Safety (Astro) — comandos disponíveis"
	@echo "──────────────────────────────────────"
	@echo "make install    # Instala as dependências do projeto"
	@echo "make dev        # Inicia o servidor de desenvolvimento"
	@echo "make build      # Gera o build de produção"
	@echo "make preview    # Visualiza o build de produção localmente"
	@echo "make clean      # Limpa o cache e arquivos temporários do Astro"
	@echo "make check      # Valida tipos TypeScript + arquivos Astro"
	@echo "make safe-push  # NΞØ Protocol: Audit -> Check -> Build -> Status"

install:
	@echo "Instalando dependências..."
	@$(PNPM) install

dev:
	@echo "Iniciando servidor de desenvolvimento..."
	@$(PNPM) run dev

build:
	@echo "Gerando build de produção..."
	@$(PNPM) run build

preview:
	@echo "Iniciando preview do build..."
	@$(PNPM) run preview

clean:
	@echo "Limpando cache e arquivos temporários..."
	@rm -rf node_modules/.vite .astro dist
	@echo "✅ Cache limpo."

check:
	@echo "Verificando tipos TypeScript e arquivos Astro..."
	@$(PNPM) run check || (echo "❌ Erros de tipo encontrados!" && exit 1)
	@echo "✅ Verificação de tipos concluída sem erros."

safe-push:
	@echo "1. Verificando vulnerabilidades..."
	@$(PNPM) audit --audit-level=high || (echo "⚠️ Vulnerabilidades HIGH/CRITICAL encontradas!" && exit 1)
	@echo "2. Verificando tipos TypeScript..."
	@$(PNPM) run check || (echo "❌ Erros de tipo encontrados!" && exit 1)
	@echo "3. Executando build..."
	@$(PNPM) run build || (echo "❌ Erro no build!" && exit 1)
	@echo "4. Status do Git:"
	@git status
	@echo "🚀 Tudo certo! Sem vulnerabilidades, sem erros de tipo e build bem-sucedido."
	@echo "👉 Agora você pode fazer o commit e push das mudanças."
