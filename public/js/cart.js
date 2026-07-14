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
  localStorage.removeItem("4safety_cart");

  // Remove o ícone flutuante e o modal antigo se eles existirem
  const oldFab = document.getElementById("cart-fab");
  if (oldFab) oldFab.remove();

  const oldModal = document.getElementById("cart-modal");
  if (oldModal) oldModal.remove();

  // Escuta os cliques em qualquer botão de "Adicionar" do site
  document.body.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-cart-add]");
    if (btn) {
      e.preventDefault();

      const productName = btn.getAttribute("data-product-name") || "um produto";
      const productSlug = btn.getAttribute("data-product-slug");

      let message = `Olá *4Safety!*\n`;
      message += `Gostaria de solicitar um orçamento ou mais informações para o seguinte item:\n\n`;
      message += `• ${productName}`;
      if (productSlug) {
        message += `\n🔗 https://4safety.com.br/produtos/${productSlug}`;
      }

      const url = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(message)}`;
      window.open(url, "_blank");
    }
  });
});
