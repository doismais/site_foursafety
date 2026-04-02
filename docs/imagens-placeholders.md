# Imagens a produzir — 4Safety

Referência dos **placeholders** em `index.html`: bloco hero (área direita) e **12 cards** da seção **Portfólio técnico** (`#produtos`). Logos do site seguem no **Cloudinary**; os arquivos abaixo são para **substituir** os retângulos com texto `FOTO` / `FOTO HERO`.

---

## Convenções

| Item | Sugestão |
| Formato | **WebP** (fallback JPG se precisar de compatibilidade antiga) |
| Nomenclatura | minúsculas, hífens, prefixo de pasta implícito no nome (`hero-…`, `produto-…`) |
| Tamanho | Cards de produto: **quadrado ou 4:3**, ~800–1200px no maior lado; hero: **horizontal** (ver nota) |

---

## Estrutura de pastas (`images/`)

```
images/
├── brand/          ← logos e ícones já existentes (export/local)
├── decor/          ← elementos decorativos (ex.: linhas)
├── hero/           ← foto principal do hero (a preencher)
└── products/       ← fotos dos 12 produtos (a preencher)
```

### Já existentes (reorganizados)

| Arquivo | Uso |
| `brand/Logo_4Safety-1.png` | Logo horizontal (backup local; produção pode usar Cloudinary) |
| `brand/ico_4Safety-2.png` | Ícone / marca reduzida |
| `decor/lines-4safety.png` | Linhas decorativas (antes `lines_4safaty.png`) |

---

## 1. Hero — `images/hero/`

Substitui o bloco `.hero-placeholder` (texto auxiliar **FOTO HERO** no CSS).

| Salvar como | Brief |
| `hero-ambient-critico.webp` | Cena técnica: equipe/EPI/detector em ambiente industrial ou espaço confinado; tom escuro compatível com fundo `#0D0D0D`; **composição com peso visual à direita** (o layout recorta a área direita ~55% com `clip-path`). |

**Orientação:** preferir **landscape** (16:9 ou 3:2). Evitar rosto ou texto de marca de terceiros sem autorização.

---

## 2. Produtos — `images/products/` (12 arquivos)

Ordem igual à do `index.html` (de cima para baixo).

| # | Salvar como | Card no site |
|---|-------------|--------------|
| 01 | `produto-tubo-colorimetrico-uniphos.webp` | Tubo Colorimétrico Uniphos |
| 02 | `produto-bomba-deteccao-gas.webp` | Bomba de Detecção de Gás |
| 03 | `produto-detector-gas-portatil.webp` | Detector de Gás Portátil |
| 04 | `produto-fumigacao.webp` | Equipamentos de Fumigação |
| 05 | `produto-protecao-respiratoria.webp` | Proteção Respiratória |
| 06 | `produto-equipamentos-altura.webp` | Equipamentos para Altura |
| 07 | `produto-botas-calzados.webp` | Botas e Calçados |
| 08 | `produto-protetor-auditivo.webp` | Protetor Auditivo |
| 09 | `produto-oculos-protecao.webp` | Óculos de Proteção |
| 10 | `produto-luvas-protecao.webp` | Luvas de Proteção |
| 11 | `produto-descartaveis.webp` | Descartáveis |
| 12 | `produto-protecao-termica.webp` | Proteção Térmica |

**Checklist rápido:** foto nítida, fundo neutro ou contextual, produto legível; respeitar direitos de imagem das marcas (catálogo autorizado ou foto própria).

---

## 3. Opcional (não é placeholder hoje)

A **trust bar** e **parceiros** usam texto (`UNIPHOS`, pills, etc.), não imagens. Se no futuro quiser **logotipos** das marcas em cinza:

- Criar pasta sugerida: `images/brands/` (SVG ou PNG transparente, altura uniforme ~24–32px).
- Nomes sugeridos: `brand-uniphos.svg`, `brand-gfg.svg`, … (um por marca exibida).

Isso exigiria alteração no HTML — fora do escopo deste inventário.

---

## Próximo passo no código

Quando os arquivos estiverem na pasta, substituir em `index.html`:

- Hero: trocar `.hero-placeholder` por `<img>` ou `background-image` apontando para `images/hero/hero-ambient-critico.webp`.
- Cards: trocar `<div class="produto-img">FOTO</div>` por `<img class="produto-img" src="…" alt="…">` com `alt` igual ao título do produto.
