# Guia Técnico de Configuração e Desenvolvimento

Este documento descreve as especificações técnicas, requisitos de ambiente e procedimentos de automação para o projeto 4Safety.

## Requisitos de Ambiente

- **Python 3.10+**: Necessário para o servidor local, validações e scripts de automação em `scripts/`.
- **Node.js + pnpm**: Necessário para instalar a ferramenta de validação HTML e executar auditoria via `pnpm audit`.

## Comandos de Desenvolvimento

### Instalação

```bash
make install
```

Instala o ferramental leve do projeto via `pnpm install`. O projeto continua estático, sem bundler ou framework frontend.

### Servidor Local

```bash
make dev
```

Inicia o servidor estático em `http://127.0.0.1:8080` e abre o navegador no macOS.

### Verificação de Integridade

```bash
make check
```

Executa o `scripts/check.sh`, validando todas as páginas HTML do repositório com HTMLHint e checagens estruturais locais (DOCTYPE, `html`, `head`, `body`, `title` e `alt` em imagens).

### Auditoria

```bash
make audit
```

Executa `pnpm audit` para verificar vulnerabilidades do ferramental Node utilizado no projeto.

## Arquitetura de Automação

O projeto combina páginas estáticas autorais com automações localizadas para catálogo e sincronização de interface:

### 1. Motor de Geração (`scripts/gen_products.py`)

- Consome o arquivo mestre `templates/product.template.html`.
- Gera as páginas internas em `produtos/` com metadados técnicos, especificações e caminhos relativos dinâmicos.
- Não gera a seção de produtos da home. A vitrine principal em `index.html` continua sendo mantida manualmente.

### 2. Sincronização Global (`scripts/sync_nav.py`)

- Sincroniza `nav`, CSS relacionado ao `nav` e o trecho de JS correspondente a partir de `index.html`.
- Não sincroniza o footer completo nem outros blocos globais fora da navegação.

### 3. Ajuste Visual (`scripts/apply_premium_visuals.py`)

- Script auxiliar para refino visual localizado quando necessário.
- Deve ser tratado como utilitário de manutenção, não como etapa obrigatória de build.

## Estrutura de Arquivos

| Diretório/Arquivo | Função |
| :--- | :--- |
| `index.html` | Entry point da aplicação (Landing Page). |
| `quem-somos/`, `consulta-de-ca/`, `links/` | Páginas institucionais e de conversão. |
| `produtos/` | Páginas internas do catálogo geradas a partir do template. |
| `templates/` | Blueprint HTML para componentes dinâmicos. |
| `scripts/` | Lógica de geração, sincronização e validação. |
| `css/` | Folhas de estilo compartilhadas, especialmente do catálogo. |
| `js/` | Scripts de interação do site, como orçamento/carrinho. |
| `images/` | Assets da marca, produtos, hero e decorativos. |
| `docs/` | Referências de copy, placeholders e convenções auxiliares. |

## Fluxo de Publicação (NΞØ Protocol)

Fluxo recomendado para alterações:

1. **Install**: `make install` quando o ambiente ainda não estiver preparado.
2. **Audit**: `make audit` quando houver mudança de tooling ou revisão operacional.
3. **Build**: execute `scripts/gen_products.py` apenas se houver mudanças no template ou no catálogo interno.
4. **Validate**: `make check` antes de commitar.
5. **Commit**: use mensagens claras no padrão `feat:`, `fix:`, `docs:`, `style:`, etc.
6. **Push/Deploy**: publique apenas quando autorizado. O deploy contínuo depende do repositório remoto conectado à Vercel.
