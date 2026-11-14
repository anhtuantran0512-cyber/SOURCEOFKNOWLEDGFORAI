---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/add-to-cart-confirmation-modal/"
title: "Add to Cart Confirmation Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "An e-commerce \"added to cart\" confirmation modal with a signature Liquid Morph / Metaball entrance — the modal materializes through an SVG filter-based…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Add to Cart Confirmation Modal
Source: https://codefronts.com/components/css-modals/add-to-cart-confirmation-modal/

An e-commerce "added to cart" confirmation modal with a signature Liquid Morph / Metaball entrance — the modal materializes through an SVG filter-based liquid blob effect (gooey/metaball merge). Product image + name + price on the left, cart summary + View Cart / Continue Shopping actions on the right. Clean e-commerce palette (white card + coral CTA + neutral gray body). Full intensity — e-commerce success moments reward delight.
## HTML
```html
<div class="md-10">
  <svg width="0" height="0" style="position:absolute" aria-hidden="true">
    <defs>
      <filter id="md-10-goo">
        <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur" />
        <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="goo" />
        <feComposite in="SourceGraphic" in2="goo" operator="atop" />
      </filter>
    </defs>
  </svg>
  <button class="md-10__trigger" id="md-10-open">Add to cart · $89</button>
  <div class="md-10__backdrop" id="md-10-dialog" role="dialog" aria-modal="true" aria-labelledby="md-10-title">
    <div class="md-10__modal">
      <button class="md-10__x md-10__close" aria-label="Close">✕</button>
      <div class="md-10__check-badge">
        <span class="md-10__check" aria-hidden="true">✓</span>
        <span>Added to cart</span>
      </div>
      <h2 class="md-10__title" id="md-10-title">You're all set</h2>
      <div class="md-10__product">
        <div class="md-10__product-img" style="--g:linear-gradient(135deg,#fce7f3,#fef3c7)">
          <span aria-hidden="true">👟</span>
        </div>
        <div class="md-10__product-info">
          <p class="md-10__product-name">Terra Runner · Slate / Coral</p>
          <p class="md-10__product-meta">Size 10 · Qty 1</p>
          <p class="md-10__product-price">$89.00</p>
        </div>
      </div>
      <div class="md-10__summary">
        <div class="md-10__row">
          <span>Cart subtotal (2 items)</span>
          <strong>$168.00</strong>
        </div>
        <div class="md-10__row md-10__row--good">
          <span>Free shipping unlocked</span>
          <span>🎉</span>
        </div>
      </div>
      <div class="md-10__actions">
        <button class="md-10__btn md-10__btn--ghost md-10__close">Continue shopping</button>
        <button class="md-10__btn md-10__btn--primary md-10__close">View cart →</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-10 {
  --page-bg: #fdf7f4;
  --card: #ffffff;
  --ink: #1e293b;
  --sub: #64748b;
  --brand: #ff6b6b;
  --brand-dark: #ee5253;
  --good: #059669;
  --line: #eef1f5;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: radial-gradient(60% 100% at 100% 0%, rgba(255,107,107,.08) 0%, transparent 60%), var(--page-bg);
  color: var(--ink);
}

.md-10 *,
.md-10 *::before,
.md-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-10 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-10__trigger {
  padding: 13px 26px;
  border: none;
  border-radius: 9px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 10px 22px -6px rgba(255,107,107,.5);
  transition: background .18s ease,transform .12s ease;
}

.md-10__trigger:hover {
  background: var(--brand-dark);
  transform: translateY(-1px);
}

.md-10__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(30,41,59,.5);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .25s ease,visibility 0s linear .25s;
}

.md-10__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .25s ease,visibility 0s linear 0s;
}

.md-10__modal {
  position: relative;
  width: min(460px,100%);
  padding: 28px 28px 24px;
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 40px 60px -20px rgba(30,41,59,.35);
  /* Signature entrance: Liquid Morph / Metaball via SVG filter */
  opacity: 0;
  transform: scale(.6);
  filter: url(#md-10-goo);
  transition: opacity .3s ease,transform .5s cubic-bezier(.34,1.56,.64,1),filter 0s linear .5s;
}

.md-10__backdrop.is-open .md-10__modal {
  opacity: 1;
  transform: scale(1);
  filter: none;
}

.md-10__x {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: var(--sub);
  font-family: inherit;
  font-size: 15px;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-10__x:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.md-10__check-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 5px 12px 5px 6px;
  border-radius: 999px;
  background: rgba(5,150,105,.12);
  color: var(--good);
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .03em;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.md-10__check {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--good);
  color: #fff;
  font-size: 11px;
}

.md-10__title {
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.15;
  margin-bottom: 18px;
}

.md-10__product {
  display: flex;
  gap: 14px;
  align-items: center;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: #fafbfc;
  margin-bottom: 14px;
}

.md-10__product-img {
  flex-shrink: 0;
  width: 72px;
  height: 72px;
  border-radius: 9px;
  background: var(--g);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
}

.md-10__product-info {
  flex: 1;
  min-width: 0;
}

.md-10__product-name {
  font-size: .88rem;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 2px;
}

.md-10__product-meta {
  font-size: .74rem;
  color: var(--sub);
  margin-bottom: 3px;
}

.md-10__product-price {
  font-size: .95rem;
  font-weight: 800;
  color: var(--brand);
}

.md-10__summary {
  padding: 14px 16px;
  border: 1px solid var(--line);
  border-radius: 9px;
  margin-bottom: 16px;
}

.md-10__row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: .82rem;
  color: var(--ink);
}

.md-10__row + .md-10__row {
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px solid var(--line);
}

.md-10__row strong {
  font-weight: 800;
}

.md-10__row--good {
  color: var(--good);
}

.md-10__actions {
  display: flex;
  gap: 10px;
}

.md-10__btn {
  flex: 1;
  padding: 12px 14px;
  border: none;
  border-radius: 9px;
  font-family: inherit;
  font-size: .88rem;
  font-weight: 700;
  cursor: pointer;
  transition: background .18s ease,transform .12s ease;
}

.md-10__btn:active {
  transform: translateY(1px);
}

.md-10__btn--ghost {
  background: #f1f5f9;
  color: var(--ink);
}

.md-10__btn--ghost:hover {
  background: #e2e8f0;
}

.md-10__btn--primary {
  background: var(--brand);
  color: #fff;
}

.md-10__btn--primary:hover {
  background: var(--brand-dark);
}

.md-10__btn--primary:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .md-10__backdrop,
    .md-10__modal {
    transition: none!important;
  }

  .md-10__modal {
    filter: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-10');
  if (!root) return;
  var openBtn = root.querySelector('#md-10-open');
  var dialog = root.querySelector('#md-10-dialog');
  var closeBtns = root.querySelectorAll('.md-10__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Focus View Cart — natural next step after adding
    var view = dialog.querySelector('.md-10__btn--primary');
    if (view) view.focus();
    document.addEventListener('keydown', onKey);
  }
  function close() {
    dialog.classList.remove('is-open');
    document.documentElement.style.overflow = '';
    document.removeEventListener('keydown', onKey);
    if (lastFocus) lastFocus.focus();
  }
  function onKey(e) { if (e.key === 'Escape') close(); }

  openBtn.addEventListener('click', open);
  closeBtns.forEach(function(b){ b.addEventListener('click', close); });
  dialog.addEventListener('click', function(e){ if (e.target === dialog) close(); });
})();
```
