# 4Safety

Site institucional e comercial estático da 4Safety, com foco em segurança do trabalho, catálogo técnico e conversão para atendimento via WhatsApp.

## Estado atual

- Site estático em HTML/CSS/JS.
- Home manual em [index.html](/Users/nettomello/CODIGOS/projects/4safety/index.html).
- Páginas institucionais em `quem-somos/`, `consulta-de-ca/` e `links/`.
- Catálogo interno em `produtos/`, gerado a partir de template Python.
- Validação local via `make check`.

## Estrutura principal

- `index.html`: landing principal.
- `quem-somos/`: página institucional.
- `consulta-de-ca/`: página de apoio comercial e normativa.
- `links/`: hub de acesso rápido.
- `produtos/`: páginas internas do catálogo.
- `templates/`: template base do catálogo.
- `scripts/`: geração, sincronização e checagem.
- `css/`: estilos compartilhados do catálogo.
- `js/`: scripts de interação, incluindo orçamento/carrinho.
- `images/`: marca, hero, decor e produtos.
- `docs/`: suporte editorial e operacional.

## Automação real do projeto

### Geração de catálogo
`scripts/gen_products.py` gera as páginas de `produtos/` usando `templates/product.template.html`.

### Sincronização de navegação
`scripts/sync_nav.py` sincroniza apenas a navegação, o CSS do nav e o bloco de JS correspondente entre páginas HTML.

### Validação
`make check` executa `scripts/check.sh`, que hoje valida todas as páginas HTML encontradas no repositório.

## Comandos úteis

```bash
make install
make dev
make serve
make check
make audit
```

## Links do projeto

### Produção (Vercel)

- Home: `https://4safety.vercel.app/`
- Quem somos: `https://4safety.vercel.app/quem-somos/`
- Produtos: `https://4safety.vercel.app/produtos/`
- Consulta de CA: `https://4safety.vercel.app/consulta-de-ca/`
- Hub de links: `https://4safety.vercel.app/links/`

### Âncoras de navegação (home)

- Soluções: `https://4safety.vercel.app/#solucoes`
- Parceiros: `https://4safety.vercel.app/#parceiros`
- Contato: `https://4safety.vercel.app/#contato`
- Produtos: `https://4safety.vercel.app/#produtos`

### Links externos operacionais usados no site

- WhatsApp comercial: `https://wa.me/5548999148413`
- Consulta oficial de CA (MTE): `https://caepi.mte.gov.br/internet/ConsultaCAInternet.aspx`
- Agência parceira (rodapé): `https://doismais.com.br/`

## Observações

- O catálogo interno é automatizado, mas a vitrine de produtos exibida na home continua sendo mantida manualmente.
- O deploy depende do repositório remoto conectado à Vercel.
- Para configuração e fluxo técnico detalhado, veja [SETUP.md](/Users/nettomello/CODIGOS/projects/4safety/SETUP.md).
