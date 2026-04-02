# 4Safety — site estático

Landing e conteúdo de **Soluções Técnicas em Segurança do Trabalho**. O projeto é HTML/CSS em um único arquivo, sem build. A checagem de código usa **HTMLHint** via `npx` (opcional) e **Python 3** (obrigatório para validações locais).

## Documentação de conteúdo e marca

Especificação de copy, tokens de design e arquitetura de páginas: [`docs/copy_and_context.md`](docs/copy_and_context.md).

Lista preliminar de badges do portfólio: [`docs/badges.md`](docs/badges.md).

## Desenvolvimento local

Requisito: **Python 3** (servidor HTTP embutido).

```bash
make dev
```

Abre o navegador em `http://127.0.0.1:8080` e sobe o servidor na pasta do projeto. Para encerrar, use `Ctrl+C`.

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

## Estrutura

| Caminho                        | Descrição                                           |
| ------------------------------ | --------------------------------------------------- |
| `index.html`                   | Página principal                                    |
| `quem-somos/index.html`        | Página institucional                                |
| `consulta-de-ca/index.html`    | Página de consulta de CA                            |
| `links/index.html`             | Hub de links com CTA direto                         |
| `images/brand/`                | Logos e ícones locais                               |
| `images/decor/`                | Elementos decorativos                               |
| `images/hero/`                 | Foto do hero (placeholder — ver doc abaixo)         |
| `images/products/`             | Fotos dos cards de produto (placeholders)           |
| `docs/imagens-placeholders.md` | Nomes de arquivo e brief das imagens a produzir     |
| `docs/copy_and_context.md`     | Guia de conteúdo e design (não servido em produção) |
