# Deploy 4Safety → KingHost (FTP)

## Dados de Acesso FTP

Host FTP         : ftp.4safety.com.br
Host alternativo : ftp.web10f13.kinghost.net
Usuário          : 4safety
Caminho servidor : /home/4safety/public_html/
Porta            : 21 (padrão FTP)

> ⚠️ A senha está no `.env` do projeto — nunca commite esse arquivo.

---

## Fluxo Completo de Deploy

### 1. Build de produção

```bash
make build
```

O Astro gera todos os arquivos estáticos na pasta `dist/`.

### 2. Upload via `lftp` (recomendado)

```bash
lftp -u 4safety,SUA_SENHA ftp.4safety.com.br -e \
  "set ssl:verify-certificate no; \
   mirror --reverse --delete --verbose dist/ public_html/; \
   bye"
```

  --ssl:verify-certificate no  Ignora certificado auto-assinado da KingHost
  --reverse                    Envia do local → servidor (não o contrário)
  --delete                     Remove do servidor arquivos ausentes no dist/
  --verbose                    Mostra cada arquivo transferido

### 3. Verificar o deploy

```bash
# Páginas principais devem retornar 200
curl -o /dev/null -s -w "%{http_code} %{url_effective}\n" https://4safety.com.br/
curl -o /dev/null -s -w "%{http_code} %{url_effective}\n" https://4safety.com.br/produtos
curl -o /dev/null -s -w "%{http_code} %{url_effective}\n" https://4safety.com.br/quem-somos

# HTTP deve redirecionar para HTTPS (301)
curl -o /dev/null -s -w "%{http_code} → %{redirect_url}\n" http://4safety.com.br/

# Headers de segurança devem estar presentes
curl -s -I https://4safety.com.br/ | grep -iE "x-frame|x-content|strict-transport"
```

---

## Makefile Target (opcional)

Adicione ao `Makefile` para automatizar:

```makefile
deploy:
 @echo "Building..."
 @$(MAKE) build
 @echo "Uploading to KingHost..."
 @lftp -u 4safety,$(FTP_PASS) ftp.4safety.com.br -e \
   "set ssl:verify-certificate no; mirror --reverse --delete dist/ public_html/; bye"
 @echo "Done."
```

Uso: `FTP_PASS=suasenha make deploy`

---

## Regras

- Sempre `make build` antes do upload — nunca envie `src/` diretamente
- O arquivo `public/.htaccess` é incluído no build e configura HTTPS redirect, headers de segurança e cache
- O `lftp --delete` remove arquivos antigos do servidor automaticamente
- Evite subir arquivos `.DS_Store` — adicione ao `.gitignore` e use `--exclude .DS_Store` no lftp
- Após o deploy, teste sempre em aba anônima para evitar cache do browser
