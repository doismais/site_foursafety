PNPM ?= pnpm

.DEFAULT_GOAL := help

.PHONY: help install dev build preview safe-push

help:
	@echo "4Safety (Astro) — comandos disponíveis"
	@echo "──────────────────────────────────────"
	@echo "make install    # Instala as dependências do projeto"
	@echo "make dev        # Inicia o servidor de desenvolvimento"
	@echo "make build      # Gera o build de produção"
	@echo "make preview    # Visualiza o build de produção localmente"
	@echo "make clean      # Limpa o cache e arquivos temporários do Astro"
	@echo "make safe-push  # Protocolo NΞØ: Audit -> Build -> Status"

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
	@$(PNPM) run astro clean

safe-push:
	@echo "1. Verificando vulnerabilidades..."
	@$(PNPM) audit || (echo "⚠️ Vulnerabilidades encontradas!" && exit 1)
	@echo "2. Executando build..."
	@$(PNPM) run build || (echo "❌ Erro no build!" && exit 1)
	@echo "3. Status do Git:"
	@git status
	@echo "🚀 Build bem-sucedido e sem vulnerabilidades críticas!"
	@echo "👉 Agora você pode fazer o commit e push das mudanças."
