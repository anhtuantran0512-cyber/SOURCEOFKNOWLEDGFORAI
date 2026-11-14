---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/quick-view-product-modal/"
title: "Quick View Product Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "An e-commerce Quick View product modal with a signature Morphing Button Elastic entrance — the trigger button visually \"stretches and expands\" into the modal…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Quick View Product Modal
Source: https://codefronts.com/components/css-modals/quick-view-product-modal/

An e-commerce Quick View product modal with a signature Morphing Button Elastic entrance — the trigger button visually "stretches and expands" into the modal card via an elastic scale + border-radius animation, creating a satisfying spatial connection between click point and modal (unlike modals that just fade in from nowhere). Product image + variant selector + Add to Cart in a compact card. Full intensity — product discovery moments warrant delight.
## HTML
```html
<div class="md-11">
  <button class="md-11__trigger" id="md-11-open">Quick view</button>
  <div class="md-11__backdrop" id="md-11-dialog" role="dialog" aria-modal="true" aria-labelledby="md-11-title">
    <div class="md-11__modal">
      <button class="md-11__x md-11__close" aria-label="Close">✕</button>
      <div class="md-11__grid">
        <div class="md-11__gallery">
          <div class="md-11__hero" style="--g:linear-gradient(135deg,#fce7f3,#c7d2fe)">
            <span aria-hidden="true">👜</span>
          </div>
          <div class="md-11__swatches" role="radiogroup" aria-label="Color">
            <button class="md-11__sw" style="--sw:#1e293b" aria-label="Slate" role="radio" aria-checked="true"></button>
            <button class="md-11__sw" style="--sw:#ff6b6b" aria-label="Coral" role="radio" aria-checked="false"></button>
            <button class="md-11__sw" style="--sw:#84cc16" aria-label="Olive" role="radio" aria-checked="false"></button>
            <button class="md-11__sw" style="--sw:#eab308" aria-label="Mustard" role="radio" aria-checked="false"></button>
          </div>
        </div>
        <div class="md-11__info">
          <p class="md-11__brand">Terra Studio</p>
          <h2 class="md-11__title" id="md-11-title">Everyday Crossbody</h2>
          <p class="md-11__price">
            <span class="md-11__price-now">$128</span>
            <span class="md-11__price-was">$168</span>
          </p>
          <p class="md-11__desc">Vegetable-tanned leather · Recycled brass hardware · Fits a 13-inch laptop.</p>
          <div class="md-11__sizes" role="radiogroup" aria-label="Size">
            <button class="md-11__size" role="radio" aria-checked="false">S</button>
            <button class="md-11__size md-11__size--sel" role="radio" aria-checked="true">M</button>
            <button class="md-11__size" role="radio" aria-checked="false">L</button>
          </div>
          <button class="md-11__cta md-11__close">Add to cart · $128</button>
          <a class="md-11__more" href="#">View full details →</a>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-11 {
  --page-bg: #fdf7f4;
  --card: #fafaf7;
  --ink: #1e293b;
  --sub: #64748b;
  --brand: #ff6b6b;
  --brand-dark: #ee5253;
  --line: #e5e0d5;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.md-11 *,
.md-11 *::before,
.md-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-11 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-11__trigger {
  padding: 11px 22px;
  border: 1px solid var(--ink);
  border-radius: 8px;
  background: transparent;
  color: var(--ink);
  font-family: inherit;
  font-size: .9rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-11__trigger:hover {
  background: var(--ink);
  color: var(--card);
}

.md-11__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(30,41,59,.5);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s linear .3s;
}

.md-11__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .3s ease,visibility 0s linear 0s;
}

.md-11__modal {
  position: relative;
  width: min(720px,100%);
  background: var(--card);
  box-shadow: 0 40px 60px -20px rgba(30,41,59,.35);
  will-change: transform;
  /* Signature entrance: Morphing Button Elastic — button-shape morphs to card */
  opacity: 0;
  transform: scale(.08) translateY(200px);
  border-radius: 50%;
  transform-origin: center bottom;
  transition: opacity .3s ease, transform .65s cubic-bezier(.68,-0.55,.32,1.55), border-radius .65s cubic-bezier(.68,-0.55,.32,1.55);
}

.md-11__backdrop.is-open .md-11__modal {
  opacity: 1;
  transform: scale(1) translateY(0);
  border-radius: 16px;
}

.md-11__x {
  position: absolute;
  top: 14px;
  right: 14px;
  z-index: 2;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 8px;
  background: rgba(255,255,255,.7);
  color: var(--sub);
  font-family: inherit;
  font-size: 15px;
  cursor: pointer;
  backdrop-filter: blur(4px);
  transition: background .18s ease,color .18s ease;
}

.md-11__x:hover {
  background: #fff;
  color: var(--ink);
}

.md-11__grid {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 0;
  overflow: hidden;
  border-radius: 16px;
}

@media (max-width: 560px) {
  .md-11__grid {
    grid-template-columns: 1fr;
  }
}

.md-11__gallery {
  padding: 24px;
  background: linear-gradient(180deg,#f5efe0,#eee5d0);
}

.md-11__hero {
  aspect-ratio: 1/1;
  border-radius: 11px;
  background: var(--g);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 88px;
}

.md-11__swatches {
  display: flex;
  gap: 8px;
  margin-top: 14px;
  justify-content: center;
}

.md-11__sw {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--sw);
  border: 2px solid rgba(255,255,255,.9);
  box-shadow: 0 0 0 1px var(--line);
  cursor: pointer;
  transition: transform .18s ease,box-shadow .18s ease;
}

.md-11__sw[aria-checked=true] {
  box-shadow: 0 0 0 2px var(--ink);
  transform: scale(1.15);
}

.md-11__sw:hover {
  transform: scale(1.1);
}

.md-11__info {
  padding: 28px 26px 24px;
  display: flex;
  flex-direction: column;
}

.md-11__brand {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 6px;
}

.md-11__title {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.15;
  margin-bottom: 10px;
}

.md-11__price {
  display: flex;
  align-items: baseline;
  gap: 10px;
  margin-bottom: 12px;
}

.md-11__price-now {
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--brand);
}

.md-11__price-was {
  font-size: .9rem;
  color: var(--sub);
  text-decoration: line-through;
}

.md-11__desc {
  font-size: .82rem;
  color: var(--sub);
  line-height: 1.55;
  margin-bottom: 16px;
}

.md-11__sizes {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}

.md-11__size {
  min-width: 44px;
  padding: 9px 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  font-family: inherit;
  font-size: .85rem;
  font-weight: 700;
  cursor: pointer;
  transition: border-color .18s ease,background .18s ease;
}

.md-11__size:hover {
  border-color: var(--ink);
}

.md-11__size--sel {
  background: var(--ink);
  color: var(--card);
  border-color: var(--ink);
}

.md-11__cta {
  margin-top: auto;
  padding: 14px 20px;
  border: none;
  border-radius: 9px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .95rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 18px -6px rgba(255,107,107,.5);
  transition: background .18s ease,transform .12s ease;
}

.md-11__cta:hover {
  background: var(--brand-dark);
  transform: translateY(-1px);
}

.md-11__cta:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.md-11__more {
  text-align: center;
  margin-top: 10px;
  font-size: .78rem;
  color: var(--sub);
  text-decoration: none;
}

.md-11__more:hover {
  color: var(--ink);
  text-decoration: underline;
}

@media (prefers-reduced-motion: reduce) {
  .md-11__backdrop,
    .md-11__modal {
    transition: opacity .2s ease!important;
  }

  .md-11__modal {
    transform: none!important;
    border-radius: 16px!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-11');
  if (!root) return;
  var openBtn = root.querySelector('#md-11-open');
  var dialog = root.querySelector('#md-11-dialog');
  var closeBtns = root.querySelectorAll('.md-11__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    // Focus close — Quick View is exploratory, close is common next action
    var closeBtn = dialog.querySelector('.md-11__x');
    if (closeBtn) closeBtn.focus();
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
