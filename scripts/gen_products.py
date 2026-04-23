"""
Module for generating product pages from templates.
Part of the 4Safety Project — NΞØ Protocol.
"""
import os

# Configurações de Caminho
BASE_DIR = "/Users/nettomello/CODIGOS/projects/4safety"
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates/product.template.html")

def load_template():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

# Definição dos Produtos
products = [
    {
        "path": "produtos/deteccao-de-gas/tubo-colorimetrico/index.html",
        "slug": "tubo-colorimetrico",
        "category": "gas",
        "title": "Tubo Colorimétrico Uniphos",
        "tag": "Detecção de Gás — NR-33",
        "desc": "Solução de alta precisão para análise quantitativa de gases em campo. Ideal para ambientes industriais e espaços confinados.",
        "img": "images/products/produto-tubo-colorimetrico-uniphos.jpg",
        "meta": ["Alta Precisão", "Gases Tóxicos", "NR-33"],
        "specs": [
            ("Marca", "Uniphos"),
            ("Amostragem", "Manual (Bomba)"),
            ("Validade", "2 anos"),
            ("Gases", "+150 tipos"),
            ("Fabricação", "Conformidade Global")
        ],
        "related": ["bomba-deteccao", "detector-portatil", "respiratorio"],
        "depth": 3
    },
    {
        "path": "produtos/deteccao-de-gas/bomba-deteccao/index.html",
        "slug": "bomba-deteccao",
        "category": "gas",
        "title": "Bomba de Detecção de Gás",
        "tag": "Detecção de Gás — NR-33",
        "desc": "Bombas manuais e automáticas projetadas para amostragem precisa com tubos colorimétricos em espaços confinados.",
        "img": "images/products/produto-bomba-deteccao-gas.png",
        "meta": ["NR-33", "Amostragem Ativa", "Manual/Auto"],
        "specs": [
            ("Tipo", "Manual / Automática"),
            ("Compatibilidade", "Uniphos / Gastec"),
            ("Volume", "100ml padrão"),
            ("Material", "ABS Reforçado"),
            ("Acessórios", "Mangueira inclusa")
        ],
        "related": ["tubo-colorimetrico", "detector-portatil", "respiratorio"],
        "depth": 3
    },
    {
        "path": "produtos/deteccao-de-gas/detector-portatil/index.html",
        "slug": "detector-portatil",
        "category": "gas",
        "title": "Detector de Gás Portátil",
        "tag": "Monitoramento Contínuo — NR-33",
        "desc": "Detector multigás robusto para monitoramento simultâneo de O2, CO, H2S e gases combustíveis (LEL).",
        "img": "images/products/produto-detector-gas-portatil.png",
        "meta": ["IP68", "Alarmes 360°", "Até 4 Gases"],
        "specs": [
            ("Sensores", "Eletroquímicos"),
            ("Bateria", "Lítio (18h+)"),
            ("Certificação", "INMETRO Ex ia"),
            ("Gases", "O2, LEL, CO, H2S"),
            ("Display", "LCD iluminado")
        ],
        "related": ["tubo-colorimetrico", "bomba-deteccao", "respiratorio"],
        "depth": 3
    },
    {
        "path": "produtos/fumigacao/index.html",
        "slug": "fumigacao",
        "category": "fumigacao",
        "title": "Equipamentos de Fumigação",
        "tag": "Controle Fitossanitário",
        "desc": "Linha completa de aplicadores e dosadores para fumigação em silos, armazéns e contêineres.",
        "img": "images/products/produto-fumigacao.png",
        "meta": ["Norma MAPA", "Dosagem Precisa", "EPIs Inclusos"],
        "specs": [
            ("Uso", "Silos e Armazéns"),
            ("Equipamento", "Dosadores Fosfina"),
            ("Certificação", "ANVISA / MAPA"),
            ("Tecnologia", "Aplicação Controlada"),
            ("Suporte", "Treinamento Técnico")
        ],
        "related": ["descartaveis", "respiratorio", "manual"],
        "depth": 2
    },
    {
        "path": "produtos/respiratorio/index.html",
        "slug": "respiratorio",
        "category": "respiratorio",
        "title": "Proteção Respiratória",
        "tag": "Segurança Pulmonar — NR-6",
        "desc": "Representamos alguns tipos de máscaras respiratórias. A disponibilidade e a indicação da linha ideal são confirmadas sob consulta técnica.",
        "img": "images/products/produto-protecao-respiratoria.jpg",
        "meta": ["Silicone Soft", "Filtros P3", "NR-6"],
        "specs": [
            ("Tipo", "Facial / Semifacial"),
            ("Material", "Silicone Grau Médico"),
            ("Normas", "NBR 13694 / 13695"),
            ("Ajuste", "4 Pontos"),
            ("Filtros", "Químicos/Mecânicos")
        ],
        "related": ["detector-portatil", "visual", "manual"],
        "depth": 2
    },
    {
        "path": "produtos/altura/index.html",
        "slug": "altura",
        "category": "altura",
        "title": "Equipamentos para Altura",
        "tag": "Trabalho Seguro — NR-35",
        "desc": "Cinturões paraquedistas e dispositivos trava-quedas certificados para máxima segurança em planos elevados.",
        "img": "images/products/produto-equipamentos-altura.png",
        "meta": ["NR-35", "NBR 15836", "Alta Resistência"],
        "specs": [
            ("Cinturão", "5 pontos de ajuste"),
            ("Material", "Poliéster Tenacidade"),
            ("Ferragem", "Aço Carbono"),
            ("Trava-quedas", "Corda / Cabo Aço"),
            ("CA", "Certificação Ativa")
        ],
        "related": ["calcados", "visual", "manual"],
        "depth": 2
    },
    {
        "path": "produtos/calcados/index.html",
        "slug": "calcados",
        "category": "calcados",
        "title": "Botas e Calçados de Segurança",
        "tag": "Proteção para os Pés — NR-6",
        "desc": "Calçados profissionais com biqueira de proteção e solado antiderrapante para diversos ambientes de trabalho.",
        "img": "images/products/produto-botas-calzados.png",
        "meta": ["Bidensidade", "Biqueira Composite", "NR-6"],
        "specs": [
            ("Material", "Couro Relax"),
            ("Solado", "PU Bidensidade"),
            ("Palmilha", "Antiperfurante"),
            ("Tamanhos", "34 ao 46"),
            ("Resistência", "Hidrocarbonetos")
        ],
        "related": ["altura", "manual", "visual"],
        "depth": 2
    },
    {
        "path": "produtos/auditivo/index.html",
        "slug": "auditivo",
        "category": "auditivo",
        "title": "Protetor Auditivo",
        "tag": "Proteção contra Ruído — NR-15",
        "desc": "Protetores circum-auriculares (concha) e de inserção de alta atenuação para conforto prolongado.",
        "img": "images/products/produto-protetor-auditivo.png",
        "meta": ["Alta Atenuação", "Hipoalergênico", "NR-15"],
        "specs": [
            ("Tipo", "Concha / Plug"),
            ("Atenuação", "Até 28dB"),
            ("Norma", "ANSI S12.6"),
            ("Ajuste", "Universal"),
            ("Cores", "Alta Visibilidade")
        ],
        "related": ["visual", "respiratorio", "calcados"],
        "depth": 2
    },
    {
        "path": "produtos/visual/index.html",
        "slug": "visual",
        "category": "visual",
        "title": "Óculos de Proteção",
        "tag": "Proteção Ocular — NR-6",
        "desc": "Lentes de policarbonato com tratamento anti-risco e anti-embaçante para clareza visual total.",
        "img": "images/products/produto-oculos-protecao.png",
        "meta": ["ANSI Z87.1", "Proteção UV", "Anti-embaçante"],
        "specs": [
            ("Lente", "Policarbonato"),
            ("Filtro", "UVA / UVB"),
            ("Impacto", "Alta Velocidade"),
            ("Tratamento", "Anti-risco"),
            ("Estilo", "Esportivo/Clássico")
        ],
        "related": ["manual", "auditivo", "respiratorio"],
        "depth": 2
    },
    {
        "path": "produtos/manual/index.html",
        "slug": "manual",
        "category": "manual",
        "title": "Luvas de Proteção",
        "tag": "Proteção para as Mãos — NR-6",
        "desc": "Linha completa de luvas para riscos mecânicos, químicos e biológicos. Performance técnica por aplicação.",
        "img": "images/products/produto-luvas-protecao.png",
        "meta": ["EN 388", "Nitrílica/Látex", "Destreza"],
        "specs": [
            ("Aplicação", "Logística / Química"),
            ("Revestimento", "PU / Nitrilo"),
            ("Resistência", "Corte / Abrasão"),
            ("Grade", "XP ao XG"),
            ("Grip", "Antiderrapante")
        ],
        "related": ["visual", "calcados", "descartaveis"],
        "depth": 2
    },
    {
        "path": "produtos/descartaveis/index.html",
        "slug": "descartaveis",
        "category": "descartaveis",
        "title": "Vestimentas Descartáveis",
        "tag": "Barreira de Proteção — Tyvek",
        "desc": "Macacões e aventais projetados para proteção contra partículas secas e sprays líquidos limitados.",
        "img": "images/products/produto-descartaveis.png",
        "meta": ["Tipo 5/6", "Anti-estático", "Respirável"],
        "specs": [
            ("Material", "Polietileno"),
            ("Proteção", "> 1 mícron"),
            ("Modelo", "Com Capuz"),
            ("Vedação", "Zíper Protegido"),
            ("Uso", "Indústria Química")
        ],
        "related": ["manual", "respiratorio", "fumigacao"],
        "depth": 2
    },
    {
        "path": "produtos/termica/index.html",
        "slug": "termica",
        "category": "termica",
        "title": "Proteção Térmica",
        "tag": "Ambientes de Calor Extremo",
        "desc": "EPIs aluminizados e de aramida para proteção contra calor radiante, chamas e respingos de metal fundido.",
        "img": "images/products/produto-protecao-termica.png",
        "meta": ["Conformidade NR-15", "Conformidade NR-33", "Certificação Inmetro"],
        "specs": [
            ("Vestimenta", "Capa, Calça e Capuz"),
            ("Luvas", "Aramida com Carbono"),
            ("Refletividade", "95% do calor radiante"),
            ("Normas", "EN 407 / EN 531"),
            ("Uso", "Siderurgia e Fundição")
        ],
        "related": ["respiratorio", "calcados", "manual"],
        "depth": 2
    }
]

products_by_slug = {product["slug"]: product for product in products}

def build_specs_html(specs):
    items = "".join([
        f"""
            <div class="spec-row">
              <span class="spec-label">{label}</span>
              <span class="spec-value">{value}</span>
            </div>"""
        for label, value in specs
    ])
    return f'<div class="specs-card"><div class="specs-list">{items}\n            </div></div>'

def build_related_html(product, prefix):
    related_cards = []
    for slug in product.get("related", []):
        related = products_by_slug.get(slug)
        if not related:
            continue
        related_cards.append(f"""
            <a class="related-card" href="{prefix}{related['path']}">
              <div class="related-card-media">
                <img src="{prefix}{related['img']}" alt="{related['title']}" />
              </div>
              <div class="related-card-copy">
                <span class="related-card-tag">{related['tag']}</span>
                <h3>{related['title']}</h3>
                <p>{related['desc']}</p>
              </div>
            </a>""")
    return "".join(related_cards)

def generate():
    template = load_template()
    print(f"🚀 Gerando {len(products)} páginas de produtos...")

    for p in products:
        p_path = os.path.join(BASE_DIR, p['path'])
        os.makedirs(os.path.dirname(p_path), exist_ok=True)
        
        prefix = "../" * p['depth']
        
        # Meta Badges HTML
        meta_html = "".join([f'<span class="meta-badge">{m}</span>' for m in p['meta']])
        
        specs_html = build_specs_html(p["specs"])
        related_html = build_related_html(p, prefix)
        
        # Replacements
        html = template.replace("[[TITLE]]", p['title'])
        html = html.replace("[[TAG]]", p['tag'])
        html = html.replace("[[DESCRIPTION]]", p['desc'])
        html = html.replace("[[IMAGE]]", prefix + p['img'])
        html = html.replace("[[PREFIX]]", prefix)
        html = html.replace("[[META_BADGES]]", meta_html)
        html = html.replace("[[SPECS]]", specs_html)
        html = html.replace("[[RELATED_PRODUCTS]]", related_html)
        
        with open(p_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ Criado: {p['path']}")

if __name__ == "__main__":
    generate()
