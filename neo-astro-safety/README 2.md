# neomello-control-plane

Control plane pessoal do workspace local `~/neomello`.

Este repositório existe para versionar contexto,
governança operacional,
rotinas de agentes,
templates de IA,
padrões visuais
e ferramentas locais portáveis.

Remote previsto:

```text
https://github.com/neomello/neomello-control-plane.git
```

---

## Objetivo

`~/neomello` é uma raiz multi-repo.

Ela contém organizações,
clones soberanos,
stacks de produto,
control planes internos
e material pessoal de operação.

Este control-plane **não** deve capturar as organizações.
Ele deve versionar apenas a camada transversal segura.

---

## Regra Dura

É expressamente proibido apagar:

```text
.gcloud/
.claude/settings.local.json
.playwright-mcp/
.venv/
secrets/
*.pem
*.key
redis_ca.pem
.DS_Store
00_STRUCTURE.txt
01_FULL_INDEX.txt
02_HIDDEN_ONLY.txt
table.csv
.git.BACKUP-*/
```

Esses itens podem ser ignorados pelo Git.
Ignorar não significa remover.

---

## O Que Entra

```text
AGENTS.md      -> regras globais para agentes
CONTEXT.md     -> mapa mental macro
MEMORY.md      -> decisões persistidas
SKILL.md       -> rotina operacional global
README.md      -> guia humano do control-plane
SVG.md         -> padrão global de banner/identidade visual
.editorconfig  -> padrão de formatação
mise.toml      -> runtime local declarativo
docs/          -> memória e governança global
neo-ai/        -> template/ontologia de contexto para agentes
infra/         -> somente partes limpas e portáveis
```

`neo-avatar-project/` será avaliado separadamente.
Por enquanto, deve ficar fora do bootstrap automático.

---

## Infra Portável

Incluir:

```text
infra/bin/delta-watch
infra/gateway-bridge.coffee
infra/test-bridge.coffee
infra/lib/client-glmpartner.js
infra/lib/package.json
infra/lib/pnpm-lock.yaml
```

Não incluir:

```text
infra/.venice-config.json
infra/node_modules/
infra/lib/node_modules/
infra/.test-perm
infra/var/
```

Arquivos de infra podem apontar para secrets por caminho,
mas nunca devem carregar valores sensíveis no Git.

---

## Repositórios Soberanos

Estas pastas são organizações ou repos soberanos.
Não entram no control-plane pessoal:

```text
NEO-PROTOCOL/
NEO-FlowOFF/
flowpay-system/
neo-smart-factory/
neo-growth-system/
wodxpro/
FluxxDAO/
Chat-as-a-Protocol/
mypersonal_multiagents/
neo-avatar-project/
```

Se alguma delas precisar de coordenação,
a coordenação deve ser descrita aqui,
mas o código do produto permanece no repo próprio.

---

## `.gitignore` Recomendado

Modelo seguro por allowlist:

```gitignore
# Ignore everything by default
/*

# Allow root control-plane files
!/.gitignore
!/.editorconfig
!/AGENTS.md
!/CONTEXT.md
!/MEMORY.md
!/SKILL.md
!/README.md
!/SVG.md
!/mise.toml

# Allow curated directories
!/docs/
!/docs/**
!/neo-ai/
!/neo-ai/**
!/infra/
!/infra/bin/
!/infra/bin/**
!/infra/lib/
!/infra/lib/client-glmpartner.js
!/infra/lib/package.json
!/infra/lib/pnpm-lock.yaml
!/infra/*.coffee

# Never track secrets, local state, generated indexes, caches
**/.DS_Store
**/node_modules/
**/.pnpm-store/
**/.venv/
.gcloud/
.claude/
.playwright-mcp/
secrets/
**/secrets/
*.pem
*.key
redis_ca.pem
*.sock
*.pid
*.log
00_STRUCTURE.txt
01_FULL_INDEX.txt
02_HIDDEN_ONLY.txt
table.csv
.git.BACKUP-*/
infra/.venice-config.json
infra/.test-perm
infra/var/

# Sovereign repos and organization folders
/NEO-PROTOCOL/
/NEO-FlowOFF/
/flowpay-system/
/neo-smart-factory/
/neo-growth-system/
/wodxpro/
/FluxxDAO/
/Chat-as-a-Protocol/
/mypersonal_multiagents/
/neo-avatar-project/
```

---

## Leitura Para Agentes

Rota obrigatória:

```text
AGENTS.md  -> como agir
CONTEXT.md -> onde estou e por que existe
MEMORY.md  -> o que já foi decidido
SKILL.md   -> como executar com segurança
```

Ao entrar em uma organização ou repo filho,
sempre ler os arquivos equivalentes mais próximos.

---

## Comandos Seguros

Diagnóstico do hub NEO-PROTOCOL:

```bash
cd /Users/nettomello/neomello/NEO-PROTOCOL
pnpm run workspace:doctor
```

Validação da topologia canônica:

```bash
cd /Users/nettomello/neomello/NEO-PROTOCOL/neobot-orchestrator
pnpm analyze
```

Validação do Nexus:

```bash
cd /Users/nettomello/neomello/NEO-PROTOCOL/neo-nexus
pnpm build
pnpm lint
pnpm test
```

---

## Decisão De Bootstrap

Este workspace pode virar um repositório pessoal independente.

O bootstrap seguro deve:

1. Criar `.gitignore` por allowlist.
2. Confirmar `git status` antes de qualquer `git add`.
3. Adicionar apenas arquivos permitidos.
4. Nunca adicionar organizações soberanas.
5. Nunca apagar arquivos sensíveis ou locais.
6. Subir para `neomello/neomello-control-plane`.

---

## Próxima Leitura

Depois deste README:

1. Leia `AGENTS.md`.
2. Leia `CONTEXT.md`.
3. Leia `MEMORY.md`.
4. Leia `SKILL.md`.
