# Guia Técnico de Configuração e Desenvolvimento

Este documento descreve as especificações técnicas, requisitos de ambiente e
procedimentos de automação para o projeto 4Safety (Astro).

────────────────────────────────────────

## Requisitos de Ambiente

- **Node.js 22+**: Runtime principal do projeto.
- **pnpm**: Gerenciador de pacotes. Instale com `npm i -g pnpm` se necessário.
- **Astro**: Framework SSG. Já incluído como dependência do projeto.

────────────────────────────────────────

## Comandos de Desenvolvimento

Todos os comandos devem ser executados a partir da raiz do projeto via `make`:

| Comando          | Ação                                                     |
| :--------------- | :------------------------------------------------------- |
| `make install`   | Instala as dependências via `pnpm install`               |
| `make dev`       | Inicia o servidor de desenvolvimento em `localhost:4321` |
| `make build`     | Gera o site estático em `./dist/`                        |
| `make preview`   | Visualiza o build de produção localmente                 |
| `make clean`     | Limpa o cache e arquivos temporários do Astro            |
| `make check`     | Valida tipos TypeScript e arquivos `.astro`              |
| `make safe-push` | Protocolo NΞØ: Audit → Check → Build → Status            |
  
────────────────────────────────────────

## Estrutura de Arquivos

```text
4safety/
├── public/                  # Arquivos estáticos (imagens, cart.js)
│   ├── images/              # Brand, products, hero
│   └── js/                  # Scripts client-side (cart.js)
├── src/
│   ├── components/          # Componentes Astro reutilizáveis
│   │   ├── Hero.astro
│   │   ├── Nav.astro
│   │   ├── Footer.astro
│   │   ├── Produtos.astro
│   │   ├── Cenarios.astro
│   │   └── Numeros.astro
│   ├── layouts/             # Layout principal
│   │   └── Layout.astro
│   ├── pages/               # Rotas do site (geradas pelo Astro)
│   │   ├── index.astro      # Home
│   │   ├── produtos.astro   # Catálogo completo
│   │   ├── quem-somos.astro
│   │   ├── consulta-de-ca.astro
│   │   └── produtos/        # Páginas internas por produto
│   └── styles/
│       ├── global.css       # Estilos globais do site
│       └── products.css     # Estilos das páginas de produto
├── astro.config.mjs         # Configuração do Astro
├── package.json             # Dependências e scripts
├── tsconfig.json            # Configuração TypeScript
└── Makefile                 # Automação de tarefas (NΞØ Protocol)
```

────────────────────────────────────────

## Fluxo de Publicação (Protocolo NΞØ)

Fluxo obrigatório antes de qualquer push:

1. `make install` — garante dependências atualizadas.
2. `make check` — valida tipos TypeScript e arquivos `.astro`.
3. `make build` — confirma que o build de produção passa sem erros.
4. Commit com mensagem no padrão Conventional Commits (`feat:`, `fix:`, etc.).
5. Push — o deploy contínuo acontece automaticamente via Vercel.

Ou simplesmente: **`make safe-push`** executa a auditoria, a verificação de tipos e o build, exibindo o status do git no final.

────────────────────────────────────────

## Notas Importantes

- O `tsconfig.json` usa `"extends": "./.astro/tsconfig.json"` (gerado pelo Astro).
- O cache do Vite fica em `node_modules/.vite/`. Limpe com `make clean` em caso
  de erros `504 Outdated Optimize Dep` no servidor de dev.
- O deploy é feito via **Vercel** com build automático a partir do branch `main`.

### Autenticação do Git (Push)

Caso haja erro de autenticação (`Invalid username or token`) ao fazer push para o repositório, você pode usar o `GITHUB_TOKEN` já configurado no seu `.env` rodando o seguinte comando:

```bash
set -a; source .env; set +a; git push https://doismais:${GITHUB_TOKEN}@github.com/doismais/site_foursafety.git main
```

```bash
git add .
git commit -m "fix: finaliza ajustes finos do PDF, converte banner para png e atualiza textos"
set -a; source .env; set +a; git push https://doismais:${GITHUB_TOKEN}@github.com/doismais/site_foursafety.git main
```
