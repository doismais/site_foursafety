import os
import re


# Configurações
ROOT_DIR = "/Users/nettomello/CODIGOS/projects/4safety"
INDEX_PATH = os.path.join(ROOT_DIR, "index.html")


def get_nav_html(content):
    # Pega o bloco <nav>...</nav>
    match = re.search(r"(<nav id=\"main-nav\".*?>.*?</nav>)", content, re.DOTALL)
    return match.group(1) if match else None


def get_nav_script(content):
    # Pega o script do menu mobile
    # Tenta vários marcadores possíveis
    patterns = [
        r"(// ── MENU MOBILE ──.*?updateNavGlass\(\);)",
        r"(// ── MOBILE MENU LOGIC ──.*?updateNavGlass\(\);)"
    ]
    for p in patterns:
        match = re.search(p, content, re.DOTALL)
        if match: return match.group(1)
    return None


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


def main():
    print("Iniciando sincronização global da Navegação (HTML, CSS, JS)...")
    
    if not os.path.exists(INDEX_PATH):
        print(f"Erro: Arquivo principal {INDEX_PATH} não encontrado.")
        return

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        master_content = f.read()

    master_nav_html = get_nav_html(master_content)
    master_script = get_nav_script(master_content)
    master_css = get_nav_css(master_content)

    if not master_nav_html:
        print("Erro: Não foi possível extrair o HTML do Nav do index.html")
        return
    if not master_script:
        print("Erro: Não foi possível extrair o Script do Nav do index.html")
        return
    if not master_css:
        print("Erro: Não foi possível extrair o CSS do Nav do index.html")
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

                # 3. Aplicar Script JS
                # Substitui entre os marcadores se existirem, senão tenta inserir antes do </script> original ou fim do body
                script_pattern = r"(// ── MENU MOBILE ──.*?updateNavGlass\(\);|// ── MOBILE MENU LOGIC ──.*?updateNavGlass\(\);)"
                if re.search(script_pattern, content, re.DOTALL):
                    content = re.sub(script_pattern, master_script, content, flags=re.DOTALL)
                else:
                    print(f"  [Aviso] Script de nav não encontrado em {file}. Inserindo novo bloco.")
                    # Insere antes da tag de fecho </script> se existir, ou antes de </body>
                    new_script = f"\n      {master_script}\n"
                    if "</script>" in content:
                        # Insere no ÚLTIMO script do body ou onde encontrar
                        content = content.replace("</script>", new_script + "</script>", 1)
                    else:
                        content = content.replace("</body>", f"<script>{new_script}</script>\n</body>")

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
