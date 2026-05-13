import os
import re

# Configurações
ROOT_DIR = "/Users/nettomello/CODIGOS/projects/4safety"
INDEX_PATH = os.path.join(ROOT_DIR, "index.html")
PRODUTOS_DIR = os.path.join(ROOT_DIR, "produtos")


def extract_section(content, start_tag, end_tag):
    # Pega o link do whatsapp flutuante
    match = re.search(r"(<footer.*?>.*?</footer>)", content, re.DOTALL)
    return match.group(1) if match else None


def get_footer(content):
    match = re.search(r"(<footer.*?>.*?</footer>)", content, re.DOTALL)
    return match.group(1) if match else None


def get_wa_float(content):
    # Pega o link do whatsapp flutuante
    match = re.search(r"(<a\s+href=\"https://wa\.me/.*?</a>)", content, re.DOTALL)
    return match.group(1) if match else None


def get_reveal_script(content):
    # Pega a parte do script que contém o IntersectionObserver
    match = re.search(
        r"(// ── SCROLL REVEAL.*?observer\.observe\(el\)\);)",
        content,
        re.DOTALL,
    )
    return match.group(1) if match else ""


def get_nav_script(content):
    # Pega a lógica do menu mobile
    match = re.search(
        r"(// ── MENU MOBILE ──.*?updateNavGlass\(\);)", content, re.DOTALL
    )
    return match.group(1) if match else ""


def main():
    print("🚀 Iniciando Upgrade Premium para Páginas de Produtos...")

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        master_content = f.read()

    master_footer = get_footer(master_content)
    master_wa = get_wa_float(master_content)
    master_reveal = get_reveal_script(master_content)
    master_nav_script = get_nav_script(master_content)

    if not master_footer or not master_wa or not master_reveal or not master_nav_script:
        print("Erro: Componentes mestre não encontrados no index.html.")
        return

    # Coletar arquivos de produtos
    product_files = []
    for root, dirs, files in os.walk(PRODUTOS_DIR):
        for file in files:
            if file.endswith(".html"):
                product_files.append(os.path.join(root, file))

    print(f"Encontrados {len(product_files)} arquivos. Aplicando identidade visual...")

    for file_path in product_files:
        print(f"Refatorando: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Ajuste de Caminhos Relativos
        depth = os.path.relpath(ROOT_DIR, os.path.dirname(file_path))
        prefix = "" if depth == "." else depth + "/"

        # 2. Upgrade da Estrutura de Identidade Visual (Classes Reveal)
        # Remove eventuais classes reveal duplicadas antes de adicionar
        content = content.replace(
            'class="product-gallery reveal"', 'class="product-gallery"'
        )
        content = content.replace('class="product-info reveal"', 'class="product-info"')

        content = content.replace(
            'class="product-gallery"', 'class="product-gallery reveal"'
        )
        content = content.replace('class="product-info"', 'class="product-info reveal"')
        content = content.replace('class="specs-title"', 'class="specs-title reveal"')
        # Adiciona reveal nos spec-items (limita a 20 para evitar overkill se houver erro)
        content = re.sub(
            r'class="spec-item"', 'class="spec-item reveal"', content, count=20
        )

        # 3. Sincronizar Footer Premium
        local_footer = master_footer
        local_footer = local_footer.replace('src="images/', f'src="{prefix}images/')
        local_footer = local_footer.replace('href="#', f'href="{prefix}index.html#')
        # Corrige links de index.html no footer
        local_footer = local_footer.replace(
            'href="index.html"', f'href="{prefix}index.html"'
        )

        content = re.sub(
            r"<footer>.*?</footer>", local_footer, content, flags=re.DOTALL
        )

        # 4. Sincronizar Scripts (Nav + Reveal)
        reveal_logic = f"""
    <script>
      document.getElementById("footer-year").textContent = new Date().getFullYear();
      
      {master_nav_script}

      {master_reveal}
    </script>
"""
        # Substitui os scripts antigos
        nav_script_pattern = r"<script>\s*// ── MENU MOBILE ──.*?</script>"
        if re.search(nav_script_pattern, content, re.DOTALL):
            content = re.sub(nav_script_pattern, reveal_logic, content, flags=re.DOTALL)
        else:
            # Fallback
            content = content.replace("</body>", f"{reveal_logic}\n</body>")

        # 5. Garantir que o wa-float e back-to-top existam
        if "wa-float" not in content:
            local_wa = master_wa.replace('src="images/', f'src="{prefix}images/')
            content = content.replace("</footer>", f"</footer>\n    {local_wa}")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    print("✅ Upgrade concluído!")


if __name__ == "__main__":
    main()
