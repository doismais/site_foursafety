# 4Safety — site estático

Landing e conteúdo de **Soluções Técnicas em Segurança do Trabalho**. O projeto é HTML/CSS em um único arquivo, sem build. A checagem de código usa **HTMLHint** via `npx` (opcional) e **Python 3** (obrigatório para validações locais).

## Documentação de conteúdo e marca

Especificação de copy, tokens de design e arquitetura de páginas: [`docs/copy_and_context.md`](docs/copy_and_context.md).

Lista preliminar de badges do portfólio: [`docs/badges.md`](docs/badges.md).

## Desenvolvimento local

Requisito: **Python 3** (servidor HTTP embutido e scripts de automação).

### Servidor de Desenvolvimento
```bash
make dev
```
Abre o navegador em `http://127.0.0.1:8080`.

### Automação de Conteúdo
O site utiliza scripts Python para manter a consistência entre páginas:

- **Gerador de Produtos**: `python3 scripts/gen_products.py`
  Gera as páginas individuais em `produtos/` a partir de `templates/product.template.html`.
- **Sincronizador de Navegação**: `python3 scripts/sync_nav.py`
  Garante que o menu, os scripts e o CSS global sejam idênticos em todas as páginas HTML do projeto.


Variável opcional:

```bash
make dev PORT=3000
```

Sem Make, use:

```bash
python3 -m http.server 8080
```

Depois acesse `http://127.0.0.1:8080/` no navegador.

### Checagem de código

```bash
make check
```

Roda [`scripts/check.sh`](scripts/check.sh): [HTMLHint](https://htmlhint.com/) (se `npx` estiver disponível, lê [`.htmlhintrc`](.htmlhintrc)) e validações em Python (`DOCTYPE`, `<html>`, `<title>`, `alt` em `<img>`, etc.). Requer **Python 3**; para o lint completo, **Node.js** com `npx`.

### Outros sistemas

- **Linux:** se `make dev` não abrir o navegador, abra manualmente a URL mostrada no terminal (ou instale `xdg-open` e adapte o `Makefile`).

## Estrutura do Projeto

| Caminho | Descrição |
| :--- | :--- |
| `index.html` | Landing page principal |
| `produtos/` | Páginas de produtos (geradas automaticamente) |
| `templates/` | Template mestre para páginas de produtos |
| `scripts/` | Motores de automação (Python) |
| `css/products.css` | Estilização premium do catálogo |
| `quem-somos/` | Página institucional |
| `consulta-de-ca/` | Ferramenta de consulta de CA |
| `images/products/` | Fotos reais e placeholders dos produtos |
| `docs/` | Guias de copy, design e badges |

## Fluxo de Publicação (NΞØ Protocol)

Antes de cada commit, o protocolo exige:
1. **Segurança**: `pnpm audit`
2. **Build**: Execução dos scripts de automação (`gen_products.py`)
3. **Commits**: Seguir o padrão [Conventional Commits](https://www.conventionalcommits.org/)
4. **Push**: Deploy automático via Vercel na branch `main`

---
*Mantido sob os padrões do NΞØ Protocol.*
