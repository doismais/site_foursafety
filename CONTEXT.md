<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

# Contexto 4safety

```text
========================================
         4SAFETY · WORKSPACE
========================================
Status: ACTIVE
Version: v1.0.5
========================================
```

## ⟠ Contexto

Este workspace contém o site institucional e catálogo de produtos da 4Safety.
O projeto foi migrado para o framework Astro para garantir melhor performance,
modularização e manutenção.

Leia este arquivo quando a pergunta for:
"onde estou e por que isto existe?"

────────────────────────────────────────

## ⧉ Arquitetura

O projeto segue a estrutura padrão do Astro:

```text
neo-astro-safety/
├── public/              # Arquivos estáticos (imagens, js/cart.js)
├── src/
│   ├── components/      # Componentes compartilhados
│   ├── layouts/         # Layout principal (Layout.astro)
│   ├── pages/           # Páginas e rotas do site
│   └── styles/          # Estilos CSS (global, products)
└── astro.config.mjs     # Configuração do Astro
```

As páginas de produtos estão localizadas dentro de `src/pages/produtos/`
para manter URLs limpas e fáceis de gerenciar.

────────────────────────────────────────

## ⨷ Coisas Proibidas

- Criar arquivos HTML soltos na pasta `public` (use arquivos `.astro`).
- Usar `/index.html` nos links internos.
- Quebrar o padrão de design premium e glassmorphism estabelecido.
- Commitar sem antes validar o build localmente.

────────────────────────────────────────

## ◬ Assinatura

```text
▓▓▓ NΞØ MELLØ
────────────────────────────────────────
Core Architect · NΞØ Protocol
neo@neoprotocol.space

"Code is law. Expand until
chaos becomes protocol."

Security by design.
Exploits find no refuge here.
────────────────────────────────────────
```
