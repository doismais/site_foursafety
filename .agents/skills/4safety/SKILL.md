---
name: 4safety-routine
description: Regras de operação, rotina e limites técnicos para atuar no repositório do projeto 4Safety Astro. Acionada automaticamente em tarefas neste projeto.
---
<!-- markdownlint-disable MD003 MD007 MD013 MD022 MD023 MD025 MD029 MD032 MD033 MD034 -->

# Skill 4safety

```text
========================================
         4SAFETY · SKILL
========================================
Status: ACTIVE
Version: v1.0.7
========================================
```

## ⟠ Rotina

Como agir ao receber uma tarefa neste projeto:

1. **Leia os documentos de contexto**:
   - `AGENTS.md` para regras de comportamento.
   - `CONTEXT.md` para entender o histórico e arquitetura.
   - `SETUP.md` para instruções de ambiente e configurações do projeto.

2. **Execute a menor mudança funcional**:
   - Não reescreva arquivos inteiros se puder fazer uma edição pontual.
   - Mantenha o foco no objetivo da tarefa.

3. **Valide localmente**:
   - Sempre rode `pnpm build` (ou `make verify`) antes de dar a tarefa por concluída.
   - Verifique se não há quebras de rota ou imagens não resolvidas.

────────────────────────────────────────

## ⧉ Limites Técnicos

- Não crie arquivos HTML na pasta `public` sem autorização.
- Não use `/index.html` em links (use URLs limpas).
- Respeite o protocolo de navegação SPA do Astro (`astro:page-load`) e insira guards de inicialização em listeners.
- Respeite as regras de deploy FTP no `Makefile` (espelhamento em `.` com `chmod -R 755 images`).

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
