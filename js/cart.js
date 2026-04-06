/**
 * 4Safety — NΞØ PROTOCOL
 * Global Cart Logic (localStorage-based)
 * Supports: Home -> Product Page -> Cart -> WhatsApp
 */

document.addEventListener("DOMContentLoaded", () => {
  const CART_KEY = "4safety_cart";
  let cart = JSON.parse(localStorage.getItem(CART_KEY)) || [];

  const WA_NUMBER = "5548999148413";

  const styles = `
    .cart-fab {
      position: fixed;
      right: 1.5rem;
      bottom: 6rem;
      width: 60px;
      height: 60px;
      background: #ff4e00;
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 12px 30px rgba(255, 78, 0, 0.4);
      z-index: 999;
      cursor: pointer;
      transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      border: 2px solid rgba(255, 255, 255, 0.2);
    }
    .cart-fab:hover { transform: scale(1.1); }
    .cart-badge {
      position: absolute;
      top: -5px;
      right: -5px;
      background: #161412;
      color: white;
      min-width: 24px;
      height: 24px;
      border-radius: 12px;
      font-size: 0.75rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 2px solid white;
    }
    .cart-modal {
      position: fixed;
      inset: 0;
      background: rgba(22, 20, 18, 0.85);
      backdrop-filter: blur(10px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }
    .cart-modal.active { display: flex; animation: fadeIn 0.3s ease; }
    .cart-content {
      background: white;
      color: #161412;
      width: 100%;
      max-width: 450px;
      border-radius: 24px;
      padding: 2rem;
      position: relative;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }
    .cart-close { position: absolute; top: 1.5rem; right: 1.5rem; cursor: pointer; color: #9a948c; }
    .cart-title { font-size: 1.5rem; font-weight: 800; margin-bottom: 1.5rem; }
    .cart-items { max-height: 350px; overflow-y: auto; margin-bottom: 1.5rem; }
    .cart-item {
      display: flex;
      align-items: center;
      gap: 1rem;
      padding: 0.75rem 0;
      border-bottom: 1px solid #ebe6df;
    }
    .cart-item img { width: 45px; height: 45px; border-radius: 8px; object-fit: cover; }
    .cart-item-details { flex: 1; display: flex; justify-content: space-between; align-items: center; }
    .cart-item-name { font-weight: 700; font-size: 0.85rem; padding-right: 10px; }
    .cart-item-remove { 
      color: #ff4e00; 
      font-size: 0.7rem; 
      cursor: pointer; 
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .cart-empty { text-align: center; color: #9a948c; padding: 2rem 0; }
    .btn-wa-final {
      background: #25d366;
      color: white;
      text-decoration: none;
      padding: 1rem;
      border-radius: 12px;
      font-weight: 700;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.7rem;
      transition: background 0.3s, transform 0.2s;
    }
    .btn-wa-final:hover { background: #20ba59; transform: translateY(-2px); }

    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
  `;

  const styleSheet = document.createElement("style");
  styleSheet.innerText = styles;
  document.head.appendChild(styleSheet);

  const updateCartCount = () => {
    const countEl = document.getElementById("cart-count");
    if (countEl) countEl.innerText = cart.length;
    
    const fab = document.getElementById("cart-fab");
    if (fab) fab.style.display = cart.length > 0 ? "flex" : "none";
  };

  const toggleModal = () => {
    const modal = document.getElementById("cart-modal");
    modal.classList.toggle("active");
    if (modal.classList.contains("active")) renderItems();
  };

  const renderItems = () => {
    const list = document.getElementById("cart-items-list");
    if (cart.length === 0) {
      list.innerHTML = `<div class="cart-empty">Sua lista de orçamentos está vazia.</div>`;
      return;
    }

    list.innerHTML = cart.map((item, index) => `
      <div class="cart-item">
        <img src="${item.img}" alt="${item.name}">
        <div class="cart-item-details">
          <div class="cart-item-name">${item.name}</div>
          <div class="cart-item-remove" data-index="${index}">Remover</div>
        </div>
      </div>
    `).join("");

    list.querySelectorAll(".cart-item-remove").forEach(btn => {
      btn.addEventListener("click", (e) => {
        const idx = e.target.getAttribute("data-index");
        removeItem(idx);
      });
    });
  };

  const removeItem = (index) => {
    cart.splice(index, 1);
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartCount();
    renderItems();
    if (cart.length === 0) {
        setTimeout(toggleModal, 500);
    }
    updateAddButtons();
  };

  const renderCartUI = () => {
    let fab = document.getElementById("cart-fab");
    if (!fab) {
      fab = document.createElement("div");
      fab.id = "cart-fab";
      fab.className = "cart-fab";
      fab.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
        <span class="cart-badge" id="cart-count">0</span>
      `;
      document.body.appendChild(fab);
      fab.addEventListener("click", toggleModal);
    }

    let modal = document.getElementById("cart-modal");
    if (!modal) {
      modal = document.createElement("div");
      modal.id = "cart-modal";
      modal.className = "cart-modal";
      modal.innerHTML = `
        <div class="cart-content">
          <div class="cart-close">
             <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </div>
          <h2 class="cart-title">Sua Cotação</h2>
          <div id="cart-items-list" class="cart-items"></div>
          <div class="cart-footer">
            <a href="#" id="cart-to-wa" class="btn-wa-final">Solicitar Orçamento no WhatsApp</a>
          </div>
        </div>
      `;
      document.body.appendChild(modal);
      modal.querySelector(".cart-close").addEventListener("click", toggleModal);
      document.getElementById("cart-to-wa").addEventListener("click", sendToWA);
    }
    updateCartCount();
  };

  const sendToWA = (e) => {
    e.preventDefault();
    if (cart.length === 0) return;
    let message = "Olá 4Safety! Gostaria de uma cotação para os seguintes itens:\n\n";
    cart.forEach(item => { message += `• ${item.name}\n`; });
    const url = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(message)}`;
    window.open(url, "_blank");
  };

  const updateAddButtons = () => {
    document.querySelectorAll("[data-cart-add]").forEach(btn => {
      const name = btn.getAttribute("data-product-name");
      const isAdded = cart.some(item => item.name === name);
      btn.innerText = isAdded ? "Item Adicionado" : (btn.getAttribute("data-original-text") || "Adicionar à Cotação");
      if (isAdded) {
          btn.style.opacity = "0.6";
          btn.style.background = "#ebe6df";
          btn.style.color = "#161412";
      } else {
          btn.style.opacity = "";
          btn.style.background = "";
          btn.style.color = "";
      }
    });
  };

  renderCartUI();

  document.body.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-cart-add]");
    if (btn) {
      e.preventDefault();
      const product = {
        name: btn.getAttribute("data-product-name"),
        img: btn.getAttribute("data-product-img"),
        slug: btn.getAttribute("data-product-slug")
      };
      if (!cart.some(item => item.name === product.name)) {
          cart.push(product);
          localStorage.setItem(CART_KEY, JSON.stringify(cart));
          updateCartCount();
          updateAddButtons();
      } else {
          toggleModal();
      }
    }
  });

  document.querySelectorAll("[data-cart-add]").forEach(btn => {
    btn.setAttribute("data-original-text", btn.innerText);
  });
  updateAddButtons();
});
