# 4Safety — Content Architecture v2.0

# Plug-and-play para agente de desenvolvimento

# Reposicionamento: operador de conformidade e risco → produto é OUTPUT de diagnóstico técnico

---

## DESIGN SYSTEM TOKENS

```
BRAND_TOKENS {
  logo_horizontal : "https://res.cloudinary.com/dqhheouq9/image/upload/q_auto/f_auto/v1775058467/Logo_4Safety-1_fsksep.png"
  logo_icon       : "https://res.cloudinary.com/dqhheouq9/image/upload/q_auto/f_auto/v1775058865/ico_4Safety-2_rzke4p.png"

  colors {
    primary     : "#FF4E00"   // laranja — CTAs, destaques, hover states
    black       : "#161412"   // texto / base escura (carvão quente, não preto puro)
    ink         : "#141210"   // fundo página e blocos escuros
    gray_900    : "#252220"   // cards e superfícies sobre escuro
    gray_700    : "#4a4540"   // texto body sobre fundo light
    gray_400    : "#9a948c"   // subtext, labels secundários
    gray_100    : "#ebe6df"   // apoio em seções claras
    paper       : "#f7f4ef"   // seção institucional clara
    institutional : "#e0d9d0" // faixa marcas / credibilidade (com gradiente para #d4cdc3)
    white       : "#FFFFFF"
  }

  typography {
    display  : "Source Sans 3"    // headlines hero e seção — pesos 600–800
    body     : "Source Sans 3"    // parágrafos, labels, UI (mesma família, ar corporativo)
    mono     : "JetBrains Mono"   // badges técnicos (CA, NR, ISO)
  }

  cta_primary {
    label : "Solicitar Orçamento"
    href  : "https://wa.me/5548999148413"
    icon  : "whatsapp"
  }

  cta_secondary {
    label : "Ver Produtos"
    href  : "/produtos"
  }

  whatsapp {
    numero      : "+5548999148413"
    link        : "https://wa.me/5548999148413"
    label_cta   : "Falar com especialista"
    responsavel : "Luis Claudio — 4Safety"
  }

  contato {
    telefone_fixo      : "(48) 3338-2929"
    telefone_comercial : "(48) 99914-8413"
    email              : "4safety@4safety.com.br"
    horario            : "Seg–Sex, 08h às 18h"
    cnpj               : "11.897.812/0001-06"
  }
}
```

---

## REGRAS DE COPY (aplicar em todas as páginas)

```
COPY_RULES {
  voz          : técnica, direta, sem floreio
  tom          : autoridade de especialista — não de vendedor
  evitar       : adjetivos vazios ("excelente", "ótimo", "completo")
  preferir     : termos normativos (NR, CA, INMETRO, ABNT), nomes de cenários reais
  CTA          : toda página termina com bloco de conversão → WhatsApp
  SEO_intent   : intenção antes de keyword
                 ex: "como detectar gás em espaço confinado" > "detector de gás"
  interlinking : produto ↔ segmento ↔ solução (triangular sempre)
}
```

---

## PAGE: `/` — HOME

```yaml
meta:
  title: "4Safety | Soluções Técnicas em Segurança do Trabalho"
  description:
    "Importação e distribuição especializada de EPIs, detectores de gás,
    equipamentos de fumigação e proteção para ambientes críticos.
    Conformidade técnica com marcas globais."

# ─── HERO ───────────────────────────────────────────────────────────
hero:
  eyebrow: "Especialista em ambientes críticos"
  headline: "Sua operação segura começa pela especificação correta"
  subheadline: >
    Distribuímos soluções técnicas para gestão de risco em altura,
    espaços confinados, fumigação e atmosferas perigosas.
    Marcas globais. CA válido. Suporte de engenharia.
  cta_primary:
    label: "Solicitar Orçamento"
    href: "https://wa.me/5548999148413"
  cta_secondary:
    label: "Conhecer Soluções"
    href: "#solucoes"
  visual_hint: >
    Background #0D0D0D. Logo icon laranja à direita decorativo.
    Efeito grid técnico sutil ou partícula.

# ─── TRUST BAR ──────────────────────────────────────────────────────
trust_bar:
  label: "Distribuidores autorizados de"
  items:
    - Uniphos
    - GFG Instrumentation
    - Sensidyne
    - Instantel
    - Thermo Fisher
    - MSA Safety
  visual_hint: "logos em cinza — hover revela cor original — scroll horizontal mobile"

# ─── SEÇÃO: CENÁRIOS CRÍTICOS ───────────────────────────────────────
section_scenarios:
  id: "solucoes"
  eyebrow: "Onde atuamos"
  headline: "Cada risco tem uma solução técnica específica"
  subheadline: "Não vendemos catálogo. Identificamos o cenário, indicamos o produto certificado."
  visual_hint: >
    Fundo branco institucional. Cards com borda cinza fina e traços laranja (#FF4E00)
    parciais (trecho superior + canto esquerdo, sem fechar o retângulo). Texto escuro para leitura.
  cards:
    - id: espaco_confinado
      icon: shield-warning
      headline: "Espaço Confinado"
      body: >
        Detecção de gás (O₂, CO, H₂S, explosividade),
        proteção respiratória e sistemas de resgate para NR-33.
      badge: "NR-33"
      cta: { label: "Ver equipamentos", href: "/solucoes/espaco-confinado" }

    - id: trabalho_em_altura
      icon: height
      headline: "Trabalho em Altura"
      body: >
        Trava-quedas, cinturões, linhas de vida e ancoragem
        para conformidade com NR-35.
      badge: "NR-35"
      cta: { label: "Ver equipamentos", href: "/solucoes/trabalho-em-altura" }

    - id: fumigacao
      icon: gas
      headline: "Fumigação Industrial"
      body: >
        Equipamentos homologados para aplicação de fumigantes
        em silos, armazéns e contêineres.
      badge: "MAPA / Anvisa"
      cta: { label: "Ver equipamentos", href: "/solucoes/fumigacao" }

    - id: ruido_industrial
      icon: ear
      headline: "Controle de Ruído"
      body: >
        Dosimetria, protetores auditivos com CA
        e medições para conformidade com NR-15.
      badge: "NR-15"
      cta: { label: "Ver equipamentos", href: "/produtos/protetor-auditivo" }

    - id: risco_quimico
      icon: flask
      headline: "Risco Químico e Térmico"
      body: >
        Proteção respiratória, luvas, roupas e óculos
        para manuseio de substâncias perigosas.
      badge: "NR-9"
      cta: { label: "Ver equipamentos", href: "/solucoes/risco-quimico" }

    - id: monitoramento_ambiental
      icon: chart
      headline: "Monitoramento Atmosférico"
      body: >
        Tubos colorimétricos Uniphos e bombas de detecção
        para análise quantitativa de atmosfera em campo.
      badge: "NR-33 / NR-15"
      cta: { label: "Ver equipamentos", href: "/produtos/tubo-colorimetrico" }

# ─── SEÇÃO: POR QUE 4SAFETY ─────────────────────────────────────────
section_diferenciais:
  eyebrow: "Por que a 4Safety"
  headline: "Distribuição técnica. Não só logística."
  items:
    - icon: certificate
      headline: "Portfólio com CA válido"
      body: >
        Todos os EPIs com Certificado de Aprovação INMETRO ativo.
        Consulta integrada diretamente no site.

    - icon: globe
      headline: "Marcas globais, entrega nacional"
      body: >
        Importação direta das fabricantes.
        Garantia original, documentação técnica e fichas de segurança.

    - icon: engineer
      headline: "Especificação técnica"
      body: >
        Nossa equipe indica o produto correto para o risco —
        não apenas o disponível em estoque.

    - icon: clock
      headline: "Atendimento comercial ágil"
      body: >
        Orçamento via WhatsApp. Resposta no mesmo dia.
        Seg–Sex, 08h às 18h.

# ─── BLOCO DE CONVERSÃO ─────────────────────────────────────────────
section_cta:
  headline: "Precisa de um orçamento técnico?"
  subheadline: >
    Descreva o cenário ou o produto.
    Luis Claudio responde com a especificação correta.
  cta_primary:
    label: "Falar no WhatsApp"
    href: "https://wa.me/5548999148413"
  cta_secondary:
    label: "Enviar por e-mail"
    href: "mailto:4safety@4safety.com.br"
  visual_hint: "Background #FF4E00. Texto branco. Sem bordas decorativas."

# ─── FOOTER ─────────────────────────────────────────────────────────
footer:
  logo: logo_horizontal
  tagline: "Segurança do trabalho com especificação técnica."
  nav_links:
    - { label: "Home", href: "/" }
    - { label: "Quem Somos", href: "/quem-somos" }
    - { label: "Soluções", href: "/solucoes" }
    - { label: "Produtos", href: "/produtos" }
    - { label: "Consulta CA", href: "/consulta-de-ca" }
    - { label: "Links", href: "/links" }
    - { label: "Parceiros", href: "/parceiros" }
    - { label: "Contato", href: "/contato" }
  contato:
    whatsapp: "https://wa.me/5548999148413"
    telefone: "(48) 3338-2929"
    email: "4safety@4safety.com.br"
    horario: "Seg–Sex, 08h às 18h"
  legal: "© 2025 4Safety. CNPJ 11.897.812/0001-06. Todos os direitos reservados."
```

---

## PAGE: `/quem-somos` — QUEM SOMOS

```yaml
meta:
  title: "Quem Somos | 4Safety — Especialistas em Segurança do Trabalho"
  description: >
    A 4Safety distribui soluções técnicas para segurança ocupacional
    com foco em ambientes críticos, certificação e marcas globais.

hero:
  eyebrow: "Nossa empresa"
  headline: "Especialistas em risco. Não em catálogo."
  subheadline: >
    A 4Safety nasceu para resolver um problema específico:
    a distância entre o produto disponível no mercado
    e o produto tecnicamente correto para cada risco.

section_historia:
  headline: "O que nos define"
  body: >
    Somos uma importadora e distribuidora de produtos e soluções
    para segurança do trabalho com foco em ambientes de alta criticidade:
    espaços confinados, trabalho em altura, fumigação industrial
    e monitoramento atmosférico.

    Nossa operação é construída sobre três pilares:
    portfólio técnico especializado, parceria com fabricantes globais
    e atendimento de engenharia — não apenas comercial.

    Acreditamos que o EPI correto começa na especificação, não na prateleira.

section_valores:
  headline: "Como operamos"
  items:
    - icon: check-shield
      headline: "Conformidade como premissa"
      body: >
        CA válido, documentação técnica e rastreabilidade
        em cada produto distribuído.

    - icon: partners
      headline: "Parcerias duradouras"
      body: >
        Relações de longo prazo com fabricantes, clientes e colaboradores.
        Crescimento orgânico, não especulativo.

    - icon: update
      headline: "Atualização contínua"
      body: >
        Acompanhamos revisões normativas (NRs, ABNT, INMETRO)
        e incorporamos inovações ao portfólio com critério técnico.

    - icon: speed
      headline: "Agilidade comercial"
      body: "Orçamento no mesmo dia. Especificação técnica sem burocracia."

section_marcas:
  eyebrow: "Nosso portfólio de marcas"
  headline: "Distribuímos os líderes globais"
  subheadline: >
    Importação direta com garantia original,
    fichas técnicas e suporte de fabricante.
  visual_hint: "grid de logos — cinza default, hover colore — link para /parceiros"

section_cta:
  headline: "Fale com nossa equipe técnica"
  subheadline: "Descreva o risco ou o ambiente. Indicamos o produto certificado."
  cta_primary:
    label: "Solicitar Orçamento via WhatsApp"
    href: "https://wa.me/5548999148413"
```

---

## PAGE: `/produtos` — HUB DE PRODUTOS

```yaml
meta:
  title: "Produtos | 4Safety — EPIs e Equipamentos para Segurança do Trabalho"
  description: >
    Detectores de gás, equipamentos de fumigação, proteção respiratória,
    EPIs para altura, auditivo, visual e térmico. Todos com CA válido INMETRO.

hero:
  eyebrow: "Portfólio técnico"
  headline: "Produto certo para o risco certo"
  subheadline: >
    12 linhas de produto. Todos os itens com Certificado de Aprovação ativo.
    Especificação técnica inclusa no atendimento.

filter_bar:
  label: "Filtrar por categoria"
  options:
    - { label: "Todos", value: "all" }
    - { label: "Detecção de Gás", value: "gas" }
    - { label: "Proteção Respiratória", value: "respiratorio" }
    - { label: "Altura", value: "altura" }
    - { label: "Auditivo", value: "auditivo" }
    - { label: "Ocular", value: "ocular" }
    - { label: "Mãos", value: "luvas" }
    - { label: "Pés", value: "calcados" }
    - { label: "Térmico", value: "termico" }
    - { label: "Fumigação", value: "fumigacao" }

categories:
  - id: tubo_colorimetrico
    headline: "Tubo Colorimétrico Uniphos"
    body: "Análise quantitativa de atmosfera — detecção de gases tóxicos e explosivos em campo."
    badge_marca: "Uniphos"
    badge_norma: "NR-33 / NR-15"
    href: "/produtos/tubo-colorimetrico"

  - id: fumigacao
    headline: "Equipamentos de Fumigação"
    body: "Aplicadores, dosadores e EPIs para fumigação de silos, armazéns e ambientes industriais."
    badge_marca: "Importação direta"
    badge_norma: "MAPA / Anvisa"
    href: "/produtos/equipamentos-de-fumigacao"

  - id: bomba_deteccao
    headline: "Bomba de Detecção de Gás"
    body: "Bombas manuais e automáticas para amostragem com tubos colorimétricos em espaços confinados."
    badge_marca: "Sensidyne / GFG"
    badge_norma: "NR-33"
    href: "/produtos/bomba-de-deteccao-de-gas"

  - id: detector_portatil
    headline: "Detector de Gás Portátil"
    body: "Monitoramento contínuo de O₂, CO, H₂S e gases explosivos. Alarme sonoro e visual."
    badge_marca: "Multi-gás disponível"
    badge_norma: "NR-33"
    href: "/produtos/detector-de-gas-portatil"

  - id: protecao_respiratoria
    headline: "Proteção Respiratória"
    body: "Máscaras semifaciais, faceiras inteiras e respiradores para vapores, aerossóis e partículas."
    badge_marca: "CA INMETRO"
    badge_norma: "NR-6 / NR-9"
    href: "/produtos/protecao-respiratoria"

  - id: altura
    headline: "Equipamentos para Altura"
    body: "Trava-quedas, cinturões paraquedistas, longas e sistemas de ancoragem."
    badge_marca: "CA INMETRO"
    badge_norma: "NR-35"
    href: "/produtos/altura"

  - id: botas_calcados
    headline: "Botas e Calçados"
    body: "Calçados de segurança com bico de aço, antiderrapante e resistência química."
    badge_marca: "CA INMETRO"
    badge_norma: "NR-6"
    href: "/produtos/botas-e-calcados"

  - id: protetor_auditivo
    headline: "Protetor Auditivo"
    body: "Protetores tipo concha e plug com NRRsf certificado para ambientes industriais."
    badge_marca: "CA INMETRO"
    badge_norma: "NR-15 / NR-6"
    href: "/produtos/protetor-auditivo"

  - id: oculos
    headline: "Óculos de Proteção"
    body: "Proteção ocular contra impacto, radiação UV e respingos químicos."
    badge_marca: "CA INMETRO"
    badge_norma: "NR-6"
    href: "/produtos/oculos"

  - id: luvas
    headline: "Luvas de Proteção"
    body: "Proteção para riscos mecânicos, químicos, térmicos e elétricos — por aplicação."
    badge_marca: "CA INMETRO"
    badge_norma: "NR-6"
    href: "/produtos/luvas"

  - id: descartaveis
    headline: "Descartáveis"
    body: "Macacões Tyvek, toucas, protetores de calçado e kits para contaminantes."
    badge_marca: "CA INMETRO"
    badge_norma: "NR-6"
    href: "/produtos/descartaveis"

  - id: protecao_termica
    headline: "Proteção Térmica"
    body: "Luvas, aventais e roupas aluminizadas para exposição a calor intenso e fagulhas."
    badge_marca: "CA INMETRO"
    badge_norma: "NR-6 / NR-15"
    href: "/produtos/protecao-termica"

section_cta:
  headline: "Não encontrou o que precisava?"
  subheadline: "Fale com nosso especialista. Indicamos o produto correto para o seu risco."
  cta_primary:
    label: "Falar no WhatsApp"
    href: "https://wa.me/5548999148413"
```

---

## PAGE: `/produtos/[slug]` — TEMPLATE PRODUTO (12 páginas)

```yaml
# Variáveis entre {{ }} são substituídas por dados de cada produto.

meta:
  title: "{{ product.headline }} | 4Safety"
  description: >
    {{ product.meta_description }} —
    CA INMETRO válido, especificação técnica e orçamento via WhatsApp.

hero:
  eyebrow: "{{ product.norma_ref }}"
  headline: "{{ product.headline }}"
  subheadline: "{{ product.body }}"
  badge_ca: "CA INMETRO"
  badge_marca: "{{ product.badge_marca }}"

section_tecnico:
  headline: "Para que serve"
  body: "{{ product.descricao_longa }}"
  specs:
    - { label: "Norma de referência", value: "{{ product.norma_ref }}" }
    - { label: "Certificação", value: "CA INMETRO ativo" }
    - { label: "Fabricante / Marca", value: "{{ product.marca }}" }
    - { label: "Aplicação típica", value: "{{ product.aplicacao }}" }

section_cenarios:
  headline: "Quando usar"
  items:
    - "{{ scenario_1 }}"
    - "{{ scenario_2 }}"
    - "{{ scenario_3 }}"

section_ca:
  headline: "Verifique o CA do produto"
  body: >
    Consulte o Certificado de Aprovação diretamente no sistema INMETRO
    antes de especificar.
  cta:
    label: "Consultar CA"
    href: "/consulta-de-ca"

section_relacionados:
  headline: "Produtos complementares"
  visual_hint: "cards horizontais com scroll — máx 4 itens"

section_cta:
  headline: "Solicitar orçamento para {{ product.headline }}"
  subheadline: >
    Informe a quantidade, a aplicação e o ambiente.
    Respondemos com especificação técnica.
  cta_primary:
    label: "Falar no WhatsApp"
    href: "https://wa.me/5548999148413"
  cta_secondary:
    label: "Enviar por e-mail"
    href: "mailto:4safety@4safety.com.br"
```

---

## PAGE: `/solucoes/[segmento]` — SEGMENTOS (NOVAS — motor SEO)

```yaml
# Páginas novas. Não existem no site atual.
# São o principal nó de SEO semântico por intenção.
# Criar para: espaco-confinado | trabalho-em-altura | fumigacao | risco-quimico | ruido-industrial

meta:
  title: "Segurança em {{ segmento.nome }} | 4Safety"
  description: >
    Equipamentos certificados para {{ segmento.nome }}.
    Soluções técnicas para conformidade com {{ segmento.norma_principal }}.

hero:
  eyebrow: "{{ segmento.norma_principal }}"
  headline: "{{ segmento.hero_headline }}"
  subheadline: "{{ segmento.hero_subheadline }}"

section_risco:
  headline: "O que a norma exige"
  body: "{{ segmento.descricao_normativa }}"
  requisitos:
    - "{{ requisito_1 }}"
    - "{{ requisito_2 }}"
    - "{{ requisito_3 }}"

section_solucao:
  headline: "Nossa solução para {{ segmento.nome }}"
  body: "{{ segmento.solucao_descricao }}"
  produtos_vinculados:
    - href: "/produtos/{{ produto_1 }}"
    - href: "/produtos/{{ produto_2 }}"
    - href: "/produtos/{{ produto_3 }}"

section_cta:
  headline: "Monte o kit para {{ segmento.nome }}"
  subheadline: >
    Informe o tamanho da equipe e a frequência de uso.
    Fazemos a especificação completa.
  cta_primary:
    label: "Solicitar especificação no WhatsApp"
    href: "https://wa.me/5548999148413"

# ── DADOS PREENCHIDOS: Espaço Confinado ─────────────────────────────
espaco_confinado:
  nome: "Espaço Confinado"
  norma_principal: "NR-33"
  hero_headline: "Gestão de atmosfera segura em espaço confinado"
  hero_subheadline: >
    Detecção de gás, proteção respiratória e resgate.
    O que a NR-33 exige, a 4Safety entrega com CA válido.
  descricao_normativa: >
    A NR-33 exige monitoramento contínuo da atmosfera antes e durante
    o trabalho em espaço confinado. Isso inclui medição de oxigênio
    (O₂ entre 19,5% e 23,5%), gases tóxicos (CO, H₂S)
    e explosivos (LEL < 10%).
  requisitos:
    - "Medição de O₂, gases tóxicos e explosivos antes da entrada"
    - "Monitoramento contínuo durante toda a operação"
    - "EPI respiratório conforme nível de risco identificado"
    - "Tripé e sistema de resgate para entrada em espaço não-permissível"
  produtos_vinculados:
    - /produtos/detector-de-gas-portatil
    - /produtos/bomba-de-deteccao-de-gas
    - /produtos/tubo-colorimetrico
    - /produtos/protecao-respiratoria

# ── DADOS PREENCHIDOS: Trabalho em Altura ───────────────────────────
trabalho_em_altura:
  nome: "Trabalho em Altura"
  norma_principal: "NR-35"
  hero_headline: "Proteção completa para trabalho em altura"
  hero_subheadline: >
    Trava-quedas, cinturões e ancoragem com CA INMETRO.
    Conformidade com NR-35 em cada componente.
  descricao_normativa: >
    A NR-35 determina requisitos mínimos para qualquer atividade
    acima de 2 metros do piso inferior, quando há risco de queda.
    Todo sistema de proteção deve ser composto por ponto de ancoragem,
    conector, trava-queda e cinturão paraquedista com CA válido.
  produtos_vinculados:
    - /produtos/altura

# ── DADOS PREENCHIDOS: Fumigação ────────────────────────────────────
fumigacao:
  nome: "Fumigação Industrial"
  norma_principal: "MAPA / Anvisa"
  hero_headline: "Equipamentos certificados para fumigação de ambientes"
  hero_subheadline: >
    Aplicação segura de fumigantes em silos, armazéns e contêineres.
    EPIs homologados e equipamentos de precisão.
  produtos_vinculados:
    - /produtos/equipamentos-de-fumigacao
    - /produtos/protecao-respiratoria
    - /produtos/luvas
    - /produtos/descartaveis
```

---

## PAGE: `/parceiros` — PARCEIROS

```yaml
meta:
  title: "Parceiros | 4Safety — Marcas Globais em Segurança do Trabalho"
  description: >
    Distribuidores autorizados de Uniphos, GFG, Sensidyne, Instantel,
    Thermo Fisher e mais de 30 fabricantes globais de EPI e equipamentos.

hero:
  eyebrow: "Nosso portfólio de marcas"
  headline: "Líderes globais. Distribuição nacional."
  subheadline: >
    Parcerias diretas com fabricantes.
    Garantia original, fichas técnicas e suporte técnico em cada produto.

section_marcas:
  visual_hint: >
    Grid responsivo de logos — cinza padrão — hover colorido.
    Click abre modal com descrição da marca e produtos relacionados.
  lista_completa:
    - MGCinto
    - Air Safety
    - Uniphos
    - Magee
    - AethLabs
    - Scott (SE)
    - Instantel
    - Zefon
    - Hagner
    - InSitu
    - Unitec
    - Thermo Fisher
    - ACS
    - ION Science
    - BGI
    - BIOS
    - Mesa Labs
    - LSI
    - Thisch
    - GFG Instrumentation
    - TS
    - Sensidyne
    - Svantek
    - Talge
    - Softworks
    - Promat
    - Prevemax
    - Mavaro
    - Marluvas
    - Maicol
    - Kapilso
    - Fujiwara
    - Montana
    - Delta Plus
    - Danny
    - Agena

section_cta:
  headline: "Precisa de um produto específico dessas marcas?"
  cta_primary:
    label: "Falar com especialista"
    href: "https://wa.me/5548999148413"
```

---

## PAGE: `/consulta-de-ca` — CONSULTA DE CA

```yaml
meta:
  title: "Consulta de CA | 4Safety — Certificado de Aprovação INMETRO"
  description: >
    Consulte o Certificado de Aprovação (CA) de EPIs no sistema INMETRO.
    Verifique validade, fabricante e escopo de proteção.

hero:
  eyebrow: "Conformidade normativa"
  headline: "Consulte o CA antes de especificar"
  subheadline: >
    O Certificado de Aprovação é obrigatório para todo EPI
    comercializado no Brasil. Verifique a validade diretamente no INMETRO.

section_instrucoes:
  headline: "Como consultar"
  steps:
    - "Digite o número do CA no campo abaixo"
    - "O sistema INMETRO retorna fabricante, produto, escopo e validade"
    - "CA vencido = EPI fora de conformidade legal"

component_consulta:
  type: "iframe ou redirect"
  target: "https://consultaca.inmetro.gov.br/"
  nota_agente: >
    Verificar política de embed do INMETRO.
    Se iframe não for permitido, usar link direto com botão estilizado.

section_cta:
  headline: "Precisa de EPI com CA válido?"
  subheadline: "Todos os produtos 4Safety têm Certificado de Aprovação ativo."
  cta_primary:
    label: "Ver Produtos com CA"
    href: "/produtos"
  cta_secondary:
    label: "Solicitar Orçamento"
    href: "https://wa.me/5548999148413"
```

---

## PAGE: `/links` — HUB DE LINKS

```yaml
meta:
  title: "Links | 4Safety — Acesso Direto"
  description: >
    Acesso direto aos canais e soluções da 4Safety:
    orçamento, consulta de CA e portfólio técnico em um só lugar.

hero:
  eyebrow: "Links diretos"
  headline: "Acesso rápido ao que resolve agora"
  subheadline: >
    Orçamento, consulta de CA e portfólio técnico em um único ponto.
    Menos clique, mais decisão.

blocks:
  - type: "cta_principal"
    headline: "Orçamento técnico no mesmo dia"
    body: >
      Descreva o cenário, o risco ou o produto. A equipe responde com
      especificação correta e preço direto.
    cta_primary:
      label: "Falar no WhatsApp"
      href: "https://wa.me/5548999148413"
    cta_secondary:
      label: "Enviar detalhes do cenário"
      href: "/contato"

  - type: "consulta_ca"
    headline: "Consulta de CA oficial"
    body: "Verifique a validade do Certificado de Aprovação antes de especificar."
    cta_primary:
      label: "Abrir página de consulta"
      href: "/consulta-de-ca"
    cta_secondary:
      label: "Sistema do MTE"
      href: "https://caepi.mte.gov.br/internet/ConsultaCAInternet.aspx"

  - type: "portfolio"
    headline: "Portfólio e soluções"
    cta_primary:
      label: "Ver produtos"
      href: "/produtos"
    cta_secondary:
      label: "Ver soluções"
      href: "/solucoes"
```

---

## PAGE: `/contato` — CONTATO

```yaml
meta:
  title: "Contato | 4Safety — Orçamento e Atendimento Técnico"
  description: >
    Entre em contato com a 4Safety para orçamentos, especificação técnica
    e dúvidas sobre EPIs e equipamentos de segurança do trabalho.

hero:
  eyebrow: "Fale com a 4Safety"
  headline: "Orçamento técnico no mesmo dia"
  subheadline: >
    Descreva o ambiente, o risco ou o produto.
    Respondemos com especificação correta e preço justo.

section_whatsapp:
  visual_hint: "Bloco destacado — fundo #FF4E00 ou borda laranja espessa"
  headline: "Canal preferencial: WhatsApp"
  body: >
    Resposta mais rápida. Atendimento com Luis Claudio — especialista técnico.
  cta:
    label: "Falar no WhatsApp agora"
    href: "https://wa.me/5548999148413"
    numero_display: "(48) 99914-8413"

section_formulario:
  headline: "Ou envie uma mensagem"
  fields:
    - { id: nome, label: "Nome", type: text, required: true }
    - { id: empresa, label: "Empresa", type: text, required: false }
    - { id: email, label: "E-mail", type: email, required: true }
    - { id: telefone, label: "Telefone / WhatsApp", type: tel, required: false }
    - {
        id: assunto,
        label: "Assunto",
        type: select,
        required: true,
        options: - "Orçamento"
          - "Especificação técnica"
          - "Dúvida sobre CA"
          - "Outro",
      }
    - {
        id: mensagem,
        label: "Descreva o ambiente ou produto",
        type: textarea,
        required: true,
      }
  cta_submit:
    label: "Enviar mensagem"

section_info:
  items:
    - {
        icon: whatsapp,
        label: "WhatsApp",
        value: "(48) 99914-8413",
        href: "https://wa.me/5548999148413",
      }
    - {
        icon: phone,
        label: "Telefone",
        value: "(48) 3338-2929",
        href: "tel:+554833382929",
      }
    - {
        icon: email,
        label: "E-mail",
        value: "4safety@4safety.com.br",
        href: "mailto:4safety@4safety.com.br",
      }
    - { icon: clock, label: "Atendimento", value: "Seg–Sex, 08h às 18h" }
```

---

## COMPONENTES GLOBAIS

```yaml
# ─── NAVBAR ─────────────────────────────────────────────────────────
navbar:
  logo_desktop: logo_horizontal
  logo_mobile: logo_icon
  links:
    - label: "Soluções"
      href: "/solucoes"
      dropdown: true
      items:
        - { label: "Espaço Confinado", href: "/solucoes/espaco-confinado" }
        - { label: "Trabalho em Altura", href: "/solucoes/trabalho-em-altura" }
        - { label: "Fumigação", href: "/solucoes/fumigacao" }
        - { label: "Risco Químico", href: "/solucoes/risco-quimico" }
        - { label: "Ruído Industrial", href: "/solucoes/ruido-industrial" }
    - label: "Produtos"
      href: "/produtos"
      dropdown: true
    - { label: "Quem Somos", href: "/quem-somos" }
    - { label: "Consulta CA", href: "/consulta-de-ca" }
    - { label: "Parceiros", href: "/parceiros" }
  cta:
    label: "Solicitar Orçamento"
    href: "https://wa.me/5548999148413"
    style: "button filled #FF4E00 — texto branco"
  visual_hint: "sticky — fundo #0D0D0D — border-bottom sutil ao scroll"

# ─── WHATSAPP FLUTUANTE ──────────────────────────────────────────────
whatsapp_float:
  href: "https://wa.me/5548999148413"
  tooltip: "Falar com especialista"
  visual_hint: "botão fixo bottom-right — ícone WA branco — fundo #FF4E00 — z-index alto"

# ─── BADGE CA ────────────────────────────────────────────────────────
badge_ca:
  label: "CA INMETRO"
  tooltip: "Produto com Certificado de Aprovação válido"
  visual_hint: "pill pequeno — fundo gray_100 — texto JetBrains Mono #FF4E00"
```

---

## SEO CLUSTERS

```yaml
cluster_espaco_confinado:
  pillar: "/solucoes/espaco-confinado"
  supporting:
    - /produtos/detector-de-gas-portatil
    - /produtos/bomba-de-deteccao-de-gas
    - /produtos/tubo-colorimetrico
    - /produtos/protecao-respiratoria
  intents:
    - "detector de gás espaço confinado NR-33"
    - "equipamento medição oxigênio silo"
    - "kit segurança espaço confinado completo"
    - "monitor multi-gás portátil H2S CO"

cluster_altura:
  pillar: "/solucoes/trabalho-em-altura"
  supporting:
    - /produtos/altura
  intents:
    - "trava-quedas NR-35"
    - "cinturão paraquedista CA INMETRO"
    - "equipamento linha de vida altura"

cluster_fumigacao:
  pillar: "/solucoes/fumigacao"
  supporting:
    - /produtos/equipamentos-de-fumigacao
    - /produtos/protecao-respiratoria
  intents:
    - "equipamento fumigação armazém"
    - "EPI fumigação fosfina"
    - "aplicador fumigante homologado MAPA"

cluster_ca:
  pillar: "/consulta-de-ca"
  intents:
    - "consultar CA EPI INMETRO"
    - "verificar certificado de aprovação EPI"
    - "CA vencido EPI multa NR-6"
    - "como saber se CA está válido"
```

---

## NOTAS PARA O AGENTE DE DESENVOLVIMENTO

```
AGENT_INSTRUCTIONS {

  STACK SUGERIDA
  ──────────────
  → Next.js 14+ (App Router) ou Astro — performance + SEO
  → Tailwind CSS com tokens do design system acima
  → Fontes via Google Fonts:
      Syne (400, 700, 800) → display/headlines
      DM Sans (400, 500)   → body/UI
      JetBrains Mono (400) → badges técnicos
  → Imagens: next/image ou @astrojs/image com lazy load
  → Formulário: React Hook Form + API route → email / n8n webhook
  → Analytics: GA4 + Search Console desde o deploy dia 1

  PRIORIDADE DE BUILD
  ───────────────────
  Fase 1 → Home + Quem Somos + Contato + Produtos (hub + 12 páginas)
  Fase 2 → Páginas de Segmento (5 novas) + hub /solucoes
  Fase 3 → Blog técnico + Consulta CA integrada + multilíngue

  REGRAS DE IMPLEMENTAÇÃO
  ────────────────────────
  → Toda página deve ter 1+ CTA para WhatsApp:
    href="https://wa.me/5548999148413"

  → WhatsApp float: componente global em TODAS as páginas.
    Fundo #FF4E00. Ícone branco. z-index > modal.

  → Badge CA: aparece em todo card de produto.
    Estilo pill mono JetBrains. Cor #FF4E00.

  → Logo horizontal: usar em navbar desktop e footer.
  → Logo ícone: usar em navbar mobile e favicon.

  → Imagens de produto: reusar do WP enquanto não houver novas.
    Base: http://www.4safety.com.br/wp-content/uploads/2018/01/

  → Multilíngue: EN e ES (existia no site atual).
    Implementar com next-intl ou i18next. Prioridade Fase 3.

  → Acessibilidade: alt text em todas as imagens.
    aria-label em todos os CTAs. Contraste mínimo WCAG AA.

  → Dark mode: hero e navbar em #0D0D0D.
    Seções de conteúdo alternando #FFFFFF e #F2F2F2.
    Nunca fundo branco no hero.
}
```
