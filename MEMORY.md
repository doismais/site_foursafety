<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

# Memória 4safety

```text
========================================
         4SAFETY · MEMORY
========================================
Status: ACTIVE
Version: v1.0.0
========================================
```

## ⟠ Decisões Tomadas

- **Migração para Astro**: O projeto foi migrado de HTML estático para
  Astro para facilitar a manutenção e reutilização de componentes.
- **URLs Limpas**: Removemos `/index.html` de todas as rotas e links
  internos, aproveitando o roteamento baseado em arquivos do Astro.
- **Páginas de Produtos**: Todas as páginas de produtos específicos foram
  migradas para Astro em `src/pages/produtos/`.
- **Expansão do Catálogo**: Produtos separados em 13 páginas independentes 
  com conteúdo detalhado injetado via dados ricos (sem carrosseis genéricos).
- **Simplificação de UX**: Remoção de filtros complexos na página `/produtos` 
  para exibir a vitrine direta.
- **Estilos Isolados**: CSS específico das páginas de produtos em
  `src/styles/products.css`. Estilos globais em `src/styles/global.css`.
- **SEO Avançado**: Endereço no footer com Microdata e JSON-LD no Layout.
- **Rastreamento**: Slots para Google Tag Manager no `Layout.astro`.
- **TypeScript Limpo**: Todos os 38 erros de tipo corrigidos nos componentes
  e páginas. `make check` passa com 0 erros.
- **Makefile Completo**: Adicionado `make check` (validação de tipos) e
  integrado ao `make safe-push` (audit → check → build → status).
- **Footer Reorganizado**: Dois blocos alinhados: copyright + links legais
  (linha 1) e endereço + crédito (linha 2).
- **Cenários (Onde Atuamos)**: Grid 2 colunas no mobile com ícones SVG
  por categoria.
- **Hero Mobile**: Imagem de fundo 100% altura da tela, sem retornoângulo
  de glassmorphism.
- **Correção de CSP**: Removida a tag `<meta>` de CSP com `frame-ancestors` do `Layout.astro` (inválida em meta tags) e migrada para cabeçalhos reais no `vercel.json`.
- **Cabeçalhos de Segurança**: Adicionados `Content-Security-Policy` (frame-ancestors), `X-Frame-Options` e `X-Content-Type-Options` no `vercel.json`.
- **Ajuste Mobile na Consulta de CA**: Corrigido alinhamento do Hero no mobile na página de consulta de CA para centralizar o eyebrow e os textos, resolvendo a desconfiguração visual.

────────────────────────────────────────

## ⧉ Padrões

- Usar `Layout.astro` para manter o cabeçalho e rodapé consistentes.
- Novas páginas de produtos devem seguir a estrutura de pastas em `src/pages/produtos/`.
- Imagens devem ser referenciadas a partir da raiz (ex: `/images/...`).

────────────────────────────────────────

## ◬ Próximos Passos

1. Adicionar as tags reais do GTM e Pixel quando fornecidas pelo gestor.
2. Continuar melhorias de UX mobile conforme feedback.
3. Monitorar performance via Vercel Analytics após deploy.

────────────────────────────────────────

## ◬ Assinatura

```text
▓▓▓ NΞØ MELLØ
────────────────────────────────────────
Core Architect · NΞØ Protocol
neo@neoprotocol.space

"Code is law. 
────────────────────────────────────────
```
