<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

# Agentes 4safety

```text
========================================
       4SAFETY · AGENTS REGISTRY
========================================
Status: ACTIVE
Version: v1.0.6
========================================
```

## ⟠ Objetivo

Fornecer o contexto operacional e regras de comportamento para agentes de IA
no projeto 4Safety.

Leia este arquivo antes de qualquer ação no repositório.

────────────────────────────────────────

## ⨷ Regras para Agentes

1. **Respeitar a arquitetura Astro.**
   O projeto foi migrado de HTML estático para Astro.
   Novas páginas devem ser criadas em `src/pages/` como arquivos `.astro`.
   Não misture arquivos HTML legados na pasta `public` sem autorização.

2. **Seguir o padrão de URLs limpas.**
   Não utilize `/index.html` nos links internos.
   O Astro resolve as rotas automaticamente baseado no nome do arquivo.

3. **Preservar a identidade visual.**
   Mantenha os estilos premium, glassmorphism e micro-animações.
   Estilos específicos de produto devem ir para `src/styles/products.css`.
   Estilos globais ficam em `src/styles/global.css`.

4. **Protocolo Git NΞØ.**
   Antes de commitar, execute validações e builds locais.
   Não faça push se houver erros de build.

5. **Uso de Imagens (Astro `<Image />` vs `<img>`).**
   Imagens armazenadas na pasta `public/` (ex: `/images/products/...`) devem continuar usando a tag HTML padrão `<img>`. Não tente migrá-las para o componente `<Image />` do Astro (`astro:assets`) mantendo caminhos relativos de string, pois isso causará o erro de build `MissingImageDimension`. Apenas use `<Image />` se as imagens forem movidas para a pasta `src/` (ex: `src/assets/`) e importadas no frontmatter.

────────────────────────────────────────

## ⧉ Estrutura do Projeto

```text
src/
├── components/          # Componentes Astro reutilizáveis
├── layouts/             # Layouts principais (Layout.astro)
├── pages/               # Rotas do site (Astro)
│   ├── produtos/       # Páginas de produtos específicos
│   └── index.astro      # Home
└── styles/             # Arquivos CSS (global, products)
```

────────────────────────────────────────

## ⍟ Protocolo de Commit

Sempre siga o fluxo de segurança antes de enviar mudanças:
1. Verifique vulnerabilidades com `pnpm audit`.
2. Valide tipos com `make check` (`pnpm run check`).
3. Valide o build com `make build`.
4. Siga o padrão Conventional Commits.
5. Ou use `make safe-push` para executar tudo automaticamente.

────────────────────────────────────────

## ◬ Assinatura

```text
▓▓▓ NΞØ MELLØ
────────────────────────────────────────
Core Architect · NΞØ Protocol
neo@neoprotocol.space

"Code is law. "
────────────────────────────────────────
```
