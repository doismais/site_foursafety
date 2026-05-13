import os
import re


# Configurações
ROOT_DIR = "/Users/nettomello/CODIGOS/projects/4safety"
INDEX_PATH = os.path.join(ROOT_DIR, "index.html")


NAV_SCRIPT_BLOCK = """<!-- Global Navigation Script -->
<script id="global-nav-script">
  (() => {
    const nav = document.getElementById("main-nav");
    const toggle = document.getElementById("nav-toggle");
    const menu = document.getElementById("nav-menu");
    const overlay = document.getElementById("nav-overlay");

    function updateNavGlass() {
      if (!nav) return;
      nav.classList.toggle("nav--scrolled", window.scrollY > 40);
    }

    function closeMenu() {
      if (!toggle || !menu || !overlay) return;
      toggle.classList.remove("active");
      menu.classList.remove("active");
      overlay.classList.remove("active");
      document.body.classList.remove("no-scroll");
    }

    function toggleMenu() {
      if (!toggle || !menu || !overlay) return;
      const isActive = !menu.classList.contains("active");
      toggle.classList.toggle("active", isActive);
      menu.classList.toggle("active", isActive);
      overlay.classList.toggle("active", isActive);
      document.body.classList.toggle("no-scroll", isActive);
    }

    if (toggle && menu && overlay) {
      toggle.addEventListener("click", toggleMenu);
      overlay.addEventListener("click", closeMenu);
      menu.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", closeMenu);
      });
    }

    window.addEventListener("scroll", updateNavGlass, { passive: true });
    updateNavGlass();
  })();
</script>
"""

NAV_SCRIPT_BLOCK_RE = re.compile(
    r"\s*<!--\s*Global Navigation Script\s*-->\s*<script\b[^>]*id=[\"']global-nav-script[\"'][^>]*>.*?</script>",
    re.DOTALL,
)
LEGACY_NAV_SCRIPT_RE = re.compile(
    r"\s*<!--\s*Global Navigation Script\s*-->\s*<script\b[^>]*>.*?MENU MOBILE.*?</script>",
    re.DOTALL,
)


def get_nav_html(content):
    # Pega o bloco <nav>...</nav>
    match = re.search(r"(<nav id=\"main-nav\".*?>.*?</nav>)", content, re.DOTALL)
    return match[1] if match else None


def get_nav_css(content):
    # Pega o CSS do Nav
    patterns = [
        r"(/\* ── NAV: topo = branco 100%.*?/\* ── HERO)",
        r"(/\* ── NAV ── \*/.*?/\* ── HERO ── \*/)"
    ]
    for p in patterns:
        match = re.search(p, content, re.DOTALL)
        if match: return match.group(1)
    return None


def get_footer_html(content):
    # Pega o bloco <footer>...</footer>
    match = re.search(r"(<footer id=\"contato\".*?>.*?</footer>)", content, re.DOTALL)
    return match[1] if match else None


def get_footer_css(content):
    """Extrai o bloco de CSS dedicado ao Footer do index.html."""
    # Pega o bloco de CSS do Footer
    match = re.search(r"(/\* ── FOOTER ── \*/.*?)(?=\s*/\* ── WA FLOAT)", content, re.DOTALL)
    return match[1] if match else None


def main():
    """Função principal que coordena a sincronização de Nav e Footer."""
    print("Iniciando sincronização global da Navegação (HTML, CSS, JS)...")
    
    if not os.path.exists(INDEX_PATH):
        print(f"Erro: Arquivo principal {INDEX_PATH} não encontrado.")
        return

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        master_content = f.read()

    master_nav_html = get_nav_html(master_content)
    master_css = get_nav_css(master_content)
    master_footer_html = get_footer_html(master_content)
    master_footer_css = get_footer_css(master_content)

    if not master_nav_html:
        print("Erro: Não foi possível extrair o HTML do Nav do index.html")
        return
    if not master_css:
        print("Erro: Não foi possível extrair o CSS do Nav do index.html")
        return
    if not master_footer_html:
        print("Erro: Não foi possível extrair o HTML do Footer do index.html")
        return

    print("Componentes extraídos com sucesso. Sincronizando arquivos...")

    # Percorre todos os arquivos HTML
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".html") and file_path != INDEX_PATH:
                count += 1
                print(f"Processando: {file_path}")
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Ajustar caminhos relativos no HTML do Nav
                depth = os.path.relpath(ROOT_DIR, root)
                if depth == ".":
                    prefix = ""
                else:
                    prefix = depth + "/"
                
                # Ajuste de prefixo (segurança extra)
                prefix = prefix.replace("\\", "/") # Para windows se necessário
                
                local_nav = master_nav_html
                # Corrigir hrefs comuns
                local_nav = local_nav.replace('href="index.html"', f'href="{prefix}index.html"')
                local_nav = local_nav.replace('href="consulta-de-ca/', f'href="{prefix}consulta-de-ca/')
                local_nav = local_nav.replace('href="quem-somos/', f'href="{prefix}quem-somos/')
                local_nav = local_nav.replace('href="contato/', f'href="{prefix}contato/')
                # Corrigir imagens
                local_nav = local_nav.replace('src="images/', f'src="{prefix}images/')
                
                # Se for uma âncora (#produtos), ela deve ir para index.html#produtos se não estiver na home
                if prefix != "":
                    local_nav = local_nav.replace('href="#', f'href="{prefix}index.html#')

                # 2. Aplicar Nav HTML
                content = re.sub(r"<nav.*?>.*?</nav>", local_nav, content, flags=re.DOTALL)

                # 2.5 Aplicar Footer HTML
                local_footer = master_footer_html
                # Corrigir hrefs comuns no footer também
                local_footer = local_footer.replace('href="index.html"', f'href="{prefix}index.html"')
                local_footer = local_footer.replace('href="consulta-de-ca/', f'href="{prefix}consulta-de-ca/')
                local_footer = local_footer.replace('href="quem-somos/', f'href="{prefix}quem-somos/')
                local_footer = local_footer.replace('href="contato/', f'href="{prefix}contato/')
                # Corrigir imagens
                local_footer = local_footer.replace('src="images/', f'src="{prefix}images/')
                
                # Se for uma âncora (#produtos), ela deve ir para index.html#produtos se não estiver na home
                if prefix != "":
                    local_footer = local_footer.replace('href="#', f'href="{prefix}index.html#')
                    local_footer = local_footer.replace('href="index.html#', f'href="{prefix}index.html#')

                content = re.sub(r"<footer.*?>.*?</footer>", local_footer, content, flags=re.DOTALL)

                # 2.6 Aplicar CSS do Footer
                if master_footer_css:
                    pattern = r"(/\* ── FOOTER ── \*/.*?)(?=\s*/\* ── WA FLOAT)"
                    if re.search(pattern, content, re.DOTALL):
                        content = re.sub(pattern, master_footer_css, content, flags=re.DOTALL)
                    else:
                        # Se não tiver o bloco, insere no final do style
                        content = content.replace("</style>", f"\n{master_footer_css}\n</style>")

                # 3. Aplicar Script JS em bloco dedicado e isolado (sem tocar scripts existentes)
                if NAV_SCRIPT_BLOCK_RE.search(content):
                    content = NAV_SCRIPT_BLOCK_RE.sub("\n" + NAV_SCRIPT_BLOCK + "\n", content, count=1)
                elif LEGACY_NAV_SCRIPT_RE.search(content):
                    content = LEGACY_NAV_SCRIPT_RE.sub("\n" + NAV_SCRIPT_BLOCK + "\n", content, count=1)
                else:
                    print(f"  [Aviso] Script de nav não encontrado em {file}. Inserindo bloco dedicado antes de </body>.")
                    if "</body>" in content:
                        content = content.replace("</body>", f"\n{NAV_SCRIPT_BLOCK}\n</body>", 1)
                    else:
                        content += "\n" + NAV_SCRIPT_BLOCK + "\n"

                # 4. Aplicar CSS
                # Procura por bloco entre marcadores
                css_pattern = r"(/\* ── NAV: topo = branco 100%.*?/\* ── HERO|/\* ── NAV ── \*/.*?/\* ── HERO ── \*/)"
                if re.search(css_pattern, content, re.DOTALL):
                    content = re.sub(css_pattern, master_css, content, flags=re.DOTALL)
                else:
                    print(f"  [Aviso] Bloco CSS de nav não encontrado em {file}. Inserindo no <style>.")
                    # Insere no início do bloco <style>
                    if "<style>" in content:
                        content = content.replace("<style>", "<style>\n" + master_css, 1)

                # 5. Garantir HOME no menu (já está no master_nav_html, mas validamos)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

    print(f"Sincronização concluída para {count} arquivos!")


if __name__ == "__main__":
    main()
