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
- **URLs Limpas**: Decidimos remover o `/index.html` de todas as rotas e links
  internos, aproveitando o roteamento baseado em arquivos do Astro.
- **Páginas de Produtos**: Todas as páginas de produtos específicos foram
  migradas para Astro e estão funcionais em `src/pages/produtos/`.
- **Estilos Isolados**: O CSS específico das páginas de produtos foi movido
  para `src/styles/products.css`.
- **SEO Avançado**: Adicionamos o endereço no footer com Microdata e no JSON-LD
  do Layout para fortalecer o SEO local.
- **Rastreamento**: Adicionamos slots para o Google Tag Manager e tags de
  preconnect para fontes no `Layout.astro`.

────────────────────────────────────────

## ⧉ Padrões

- Usar `Layout.astro` para manter o cabeçalho e rodapé consistentes.
- Novas páginas de produtos devem seguir a estrutura de pastas em `src/pages/produtos/`.
- Imagens devem ser referenciadas a partir da raiz (ex: `/images/...`).

────────────────────────────────────────

## ◬ Próximos Passos

1. Validar o build final localmente (aguardando ambiente do usuário).
2. Adicionar as tags reais do GTM e Pixel quando fornecidas pelo gestor.
3. Seguir com o protocolo de Commit e Push Seguro.

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
