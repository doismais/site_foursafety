<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

# Contexto 4safety

```text
========================================
         4SAFETY · WORKSPACE
========================================
Status: ACTIVE
Version: v1.0.7
========================================
```

## ⟠ Contexto

Este workspace contém o site institucional e catálogo de produtos da **4Safety**.
O projeto foi migrado para o framework **Astro** para garantir melhor performance, modularização, SEO avançado e manutenção simplificada.

Leia este arquivo quando a pergunta for: *"onde estou, qual é o histórico e como o projeto funciona?"*

────────────────────────────────────────

## ⧉ Arquitetura do Projeto

```text
4safety/
├── public/              # Arquivos estáticos servidos diretamente pelo servidor
│   ├── .htaccess        # Configurações do Apache KingHost (Security headers, 404, Gzip/Cache)
│   ├── sw.js            # Service Worker de cache e fallback offline
│   ├── sitemap.xml      # Sitemap de SEO com URLs canônicas com barra final (/)
│   ├── robots.txt       # Diretivas para motores de busca
│   ├── js/cart.js       # Engine do carrinho de orçamento via WhatsApp
│   └── images/          # Imagens de hero, parceiros, marcas e produtos
├── src/
│   ├── components/      # Componentes Astro (Nav, Hero, Cenarios, Numeros, Footer, etc.)
│   ├── layouts/         # Layout principal (Layout.astro com Astro View Transitions)
│   ├── pages/           # Rotas do site (index.astro, produtos.astro, quem-somos.astro, etc.)
│   └── styles/          # Estilos CSS (global.css, products.css)
├── Makefile             # Automação de tarefas (make check, build, verify, deploy-ftp)
└── astro.config.mjs     # Configuração do Astro
```

────────────────────────────────────────

## ⨷ Histórico de Evolução & Regras Operacionais

### 1. **Deploy FTP (KingHost)**
- **Servidor:** `ftp.4safety.com.br` (User: `4safety`).
- **Pasta Pública:** A conexão FTP faz login diretamente na pasta pública do servidor (`/www/`). O parâmetro do `lftp` no `Makefile` deve utilizar a raiz `.` e espelhar o diretório `dist/` com `chmod -R 755 images` para evitar erros `403 Forbidden` nas imagens.
- **Dotfiles do Sistema:** Arquivos como `.bash_extras` pertencem ao root do sistema KingHost. O `lftp` usa `--exclude '^\.bash'` para evitar erros de permissão 550 durante a limpeza remota.

### 2. **Astro View Transitions & Scripts Client-Side**
- O projeto utiliza navegabilidade SPA (`astro:page-load`).
- **Guarda de Inicialização (Dataset Guard):** Todos os event listeners acoplados ao `document` ou `window` (como o carrinho do WhatsApp em `cart.js`, o scroll da barra de navegação em `Nav.astro` e as animações no `Footer.astro`) devem utilizar um atributo de guarda (ex: `if (el.dataset.waInit) return; el.dataset.waInit = "true";`) para prevenir acúmulo e vazamento de memória a cada navegação de página.
- **Timers Globais:** Intervalos (ex: autoplay do `Hero.astro`) devem ser limpos no evento `astro:before-swap` ou armazenados no objeto `window`.

### 3. **Imagens e Performance**
- Imagens em `public/` devem ser referenciadas com tags `<img>` padrão (não misturar com `<Image />` do `astro:assets` mantendo caminhos relativos de string).
- Animações e Scroll Reveals foram otimizados com `reduced-motion` e sem propriedade `will-change` excessiva.

### 4. **Filtro Dinâmico de Produtos por URL**
- A página `/produtos` suporta parâmetros de URL (`?filter=fumigacao`, `?categoria=fumigacao`, `?filtro=fumigacao`, e hash `#fumigacao`).
- Ao acessar um desses parâmetros, a aba correspondente é ativada e a lista de produtos é filtrada automaticamente no lado do cliente.

---

## ⨷ Coisas Proibidas

- Criar arquivos HTML soltos na pasta `public/` (use rotas `.astro` em `src/pages/`).
- Utilizar `/index.html` nos links internos.
- Alterar a estrutura do `public/.htaccess` sem testar os headers de segurança e redirecionamentos no Apache KingHost.
- Fazer push ou deploy sem validar o build e os tipos (`make verify` ou `pnpm run check`).

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
