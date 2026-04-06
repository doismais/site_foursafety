# Guia Técnico de Configuração e Desenvolvimento

Este documento descreve as especificações técnicas, requisitos de ambiente e procedimentos de automação para o projeto 4Safety.

## Requisitos de Ambiente

- **Python 3.10+**: Necessário para execução dos motores de automação e servidor local.
- **Node.js & pnpm**: Necessário para auditoria de segurança e verificação de integridade (Protocolo NΞØ).

## Comandos de Desenvolvimento

### Servidor Local
```bash
make dev
```
Inicia o servidor em `http://127.0.0.1:8080` com suporte a live-reload manual.

### Verificação de Integridade
```bash
make check
```
Executa o `scripts/check.sh` que valida a semântica do HTML (DOCTYPE, tags obrigatórias, acessibilidade básica).

## Arquitetura de Automação

O projeto utiliza um motor de geração estática customizado em Python para garantir performance e consistência:

### 1. Motor de Geração (`scripts/gen_products.py`)
- Consome o arquivo mestre `templates/product.template.html`.
- Injeta metadados técnicos (Title, Tags, Specs) de forma programática.
- Resolve caminhos relativos dinâmicos (`prefix`) para garantir que assets (CSS/Imagens) funcionem em qualquer profundidade de diretório.

### 2. Sincronização Global (`scripts/sync_nav.py`)
- Injeta o menu de navegação e componentes globais em todas as páginas.
- Garante que mudanças na barra de navegação ou rodapé sejam propagadas instantaneamente para todo o ecossistema.

## Estrutura de Arquivos

| Diretório/Arquivo | Função |
| :--- | :--- |
| `index.html` | Entry point da aplicação (Landing Page). |
| `produtos/` | Saída final das páginas de catálogo geradas. |
| `templates/` | Blueprint HTML para componentes dinâmicos. |
| `scripts/` | Lógica de build e manutenção. |
| `css/` | Tokens de design e folhas de estilo (Products/Global). |
| `images/` | Assets otimizados por categoria. |

## Fluxo de Publicação (NΞØ Protocol)

Toda alteração deve seguir rigorosamente a este fluxo:
1. **Security Audit**: `pnpm audit` para garantir zero vulnerabilidades.
2. **Build Stage**: Execução de `gen_products.py` para atualizar o catálogo.
3. **Convention**: Commits seguindo o padrão `feat:`, `fix:`, `style:`, etc.
4. **Deploy**: Push direto para a branch `main` com entrega contínua via Vercel.
