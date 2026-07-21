# ========================================
#          4SAFETY · MAKEFILE
# ========================================
# Status: ACTIVE
# Version: v1.0.4
# ========================================

PNPM ?= pnpm

.DEFAULT_GOAL := help

.PHONY: help install dev build preview clean clean-cache check lint verify safe-push deploy-ftp

help:
	@echo "4Safety (Astro) — comandos disponíveis"
	@echo "──────────────────────────────────────"
	@echo "make install     # Instala as dependências do projeto"
	@echo "make dev         # Inicia o servidor de desenvolvimento"
	@echo "make build       # Gera o build de produção"
	@echo "make preview     # Visualiza o build de produção localmente"
	@echo "make clean       # Limpa node_modules, dist, .astro e todos os caches"
	@echo "make clean-cache # Limpa apenas caches de build (.astro, .vite, dist)"
	@echo "make check       # Valida tipos TypeScript + arquivos Astro"
	@echo "make lint        # Alias para make check"
	@echo "make verify      # Valida tipos e gera build limpo"
	@echo "make deploy-ftp  # Envia o build (dist/) para o FTP apagando arquivos antigos"
	@echo "make safe-push   # NΞØ Protocol: Audit -> Check -> Build -> Status"

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
	@echo "Limpando node_modules, dist e todos os artefatos de cache..."
	@rm -rf node_modules dist .astro .vercel .cache *.tsbuildinfo
	@echo "✅ Limpeza completa concluída (node_modules, dist e caches removidos)."

clean-cache:
	@echo "Limpando apenas caches de build..."
	@rm -rf node_modules/.cache node_modules/.vite .astro dist .vercel *.tsbuildinfo
	@echo "✅ Caches de build limpos com sucesso."

check:
	@echo "Verificando tipos TypeScript e arquivos Astro..."
	@$(PNPM) run check || (echo "❌ Erros de tipo encontrados!" && exit 1)
	@echo "✅ Verificação de tipos concluída sem erros."

lint: check

verify: clean-cache check build

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

deploy-ftp: verify
	@echo "Enviando build para o servidor FTP e ajustando permissões..."
	@lftp -u 4safety,'Jmartins@13' ftp.4safety.com.br -e "set ssl:verify-certificate no; mirror -R --delete --exclude '^\.bash' --exclude '^\.ftp' --exclude '^logs' --verbose dist/ .; chmod -R 755 images; quit"
	@echo "🚀 Deploy via FTP concluído com sucesso!"
