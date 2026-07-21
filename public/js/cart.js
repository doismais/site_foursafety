/**
 * ========================================
 *        4SAFETY · WHATSAPP ENGINE
 * ========================================
 * Architect : Neo Mello
 * Protocol  : NΞØ Protocol (Code is Law)
 * Agency    : Dois Mais Agency
 * ========================================
 * Direct WhatsApp Redirect Logic (No Cart)
 * Replaces the old localStorage cart system.
 */

document.addEventListener("astro:page-load", () => {
  const WA_NUMBER = "5548999148413";

  // Limpa o cache antigo do navegador do usuário caso ele já tivesse itens na sacola
  try {
    localStorage.removeItem("4safety_cart");
  } catch (err) {
    console.warn("[WhatsApp Engine] LocalStorage access blocked:", err);
  }

  // Remove o ícone flutuante e o modal antigo se eles existirem
  document.getElementById("cart-fab")?.remove();
  document.getElementById("cart-modal")?.remove();

  // Garante que o event listener não seja duplicado no Astro View Transitions
  if (document.body.dataset.waListenerAttached === "true") return;
  document.body.dataset.waListenerAttached = "true";

  // Escuta os cliques em qualquer botão de "Adicionar" do site
  document.body.addEventListener("click", (e) => {
    const target = e.target;
    const btn = target && typeof target.closest === "function" ? target.closest("[data-cart-add]") : null;
    if (btn) {
      e.preventDefault();

      const rawName = btn.getAttribute("data-product-name")?.trim() || "um produto";
      const rawSlug = btn.getAttribute("data-product-slug")?.trim();

      // Sanitização contra caracteres de controle
      const productName = rawName.replace(/[\r\n\t]/g, " ");

      let message = `Olá *4Safety!*\n`;
      message += `Gostaria de solicitar um orçamento ou mais informações para o seguinte item:\n\n`;
      message += `• ${productName}`;
      if (rawSlug && /^[a-z0-9-]+$/i.test(rawSlug)) {
        message += `\n🔗 https://4safety.com.br/produtos/${encodeURIComponent(rawSlug)}`;
      }

      const url = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(message)}`;
      window.open(url, "_blank", "noopener,noreferrer");
    }
  });
});

