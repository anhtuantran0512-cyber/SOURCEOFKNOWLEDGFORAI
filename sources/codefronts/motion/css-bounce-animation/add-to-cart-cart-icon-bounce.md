---
source: "codefronts"
url: "https://codefronts.com/motion/css-bounce-animation/add-to-cart-cart-icon-bounce/"
title: "Add to Cart Cart Icon Bounce"
section: "motion"
category: "css-bounce-animation"
category_name: "CSS Bounce Animations"
description: "The Shopify / Etsy Add-to-Cart pattern — clicking Add to Cart triggers a bounce on the cart icon plus a badge-count increment."
has_js: "true"
---

Here's a working CSS Bounce Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Add to Cart Cart Icon Bounce
Source: https://codefronts.com/motion/css-bounce-animation/add-to-cart-cart-icon-bounce/

The Shopify / Etsy Add-to-Cart pattern — clicking Add to Cart triggers a bounce on the cart icon plus a badge-count increment. Users get immediate visual confirmation the item landed in the cart. The demo shows a compact cart icon + Add to Cart button pair as the hero — the bounce reads as "item just landed."
## HTML
```html
<div class="bn-08">
  <p class="bn-08__label">Click "Add to cart" to trigger the bounce</p>
  <div class="bn-08__cart-row">
    <button class="bn-08__cart" id="bn-08-cart" type="button" aria-label="Cart, 0 items">
      <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <circle cx="9" cy="21" r="1"/>
        <circle cx="20" cy="21" r="1"/>
        <path d="M1 1h4l2.7 13.4a2 2 0 002 1.6h9.7a2 2 0 002-1.6L23 6H6"/>
      </svg>
      <span class="bn-08__badge" id="bn-08-badge">0</span>
    </button>
  </div>
  <button class="bn-08__add" id="bn-08-add" type="button">Add to cart · $168</button>
  <div class="bn-08__live" role="status" aria-live="polite" id="bn-08-live"></div>
</div>
```
## CSS
```css
.bn-08 {
  --page-bg: #fafafa;
  --surface: #ffffff;
  --ink: #1c1917;
  --sub: #78716c;
  --brand: #065f46;
  --brand-dark: #064e3b;
  --accent: #dc2626;
  --line: #e7e5e0;
  font-family: -apple-system,BlinkMacSystemFont,'Inter','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.bn-08 *,
.bn-08 *::before,
.bn-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bn-08 ::selection {
  background: var(--brand);
  color: #fff;
}

.bn-08__label {
  font-size: .9rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.bn-08__cart-row {
  display: flex;
  justify-content: center;
  padding: 24px 40px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--surface);
  box-shadow: 0 8px 20px -8px rgba(28,25,23,.1);
}

.bn-08__cart {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 60px;
  border: none;
  border-radius: 12px;
  background: transparent;
  color: var(--ink);
  cursor: pointer;
  transition: background .18s ease;
  will-change: transform;
}

.bn-08__cart:hover {
  background: #f5f5f4;
}

.bn-08__cart:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.bn-08__cart.is-bouncing {
  animation: bn-08-cart-shake .55s ease-out;
}

@keyframes bn-08-cart-shake {
  0% {
    transform: translateY(0) rotate(0);
  }

  20% {
    transform: translateY(-6px) rotate(-12deg);
  }

  40% {
    transform: translateY(-3px) rotate(8deg);
  }

  60% {
    transform: translateY(-4px) rotate(-6deg);
  }

  80% {
    transform: translateY(-1px) rotate(3deg);
  }

  100% {
    transform: translateY(0) rotate(0);
  }
}

.bn-08__badge {
  position: absolute;
  top: 6px;
  right: 2px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 22px;
  height: 22px;
  padding: 0 6px;
  border-radius: 11px;
  background: var(--accent);
  color: #fff;
  font-size: .72rem;
  font-weight: 800;
  border: 2px solid var(--surface);
  font-variant-numeric: tabular-nums;
  will-change: transform;
}

.bn-08__badge.is-bouncing {
  animation: bn-08-badge-pop .4s cubic-bezier(.34,1.56,.64,1) .1s;
}

@keyframes bn-08-badge-pop {
  0% {
    transform: scale(1) rotate(0);
  }

  40% {
    transform: scale(1.5) rotate(6deg);
  }

  70% {
    transform: scale(.9) rotate(-2deg);
  }

  100% {
    transform: scale(1) rotate(0);
  }
}

.bn-08__add {
  padding: 14px 28px;
  border: none;
  border-radius: 11px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 12px 28px -8px rgba(6,95,70,.4);
  transition: background .18s ease,transform .12s ease;
}

.bn-08__add:hover {
  background: var(--brand-dark);
  transform: translateY(-1px);
}

.bn-08__add:active {
  transform: translateY(1px);
}

.bn-08__add:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.bn-08__live {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

@media (prefers-reduced-motion: reduce) {
  .bn-08__cart.is-bouncing,
    .bn-08__badge.is-bouncing {
    animation: none!important;
    transform: none!important;
  }

  .bn-08__badge.is-bouncing {
    background: #fca5a5!important;
    transition: background .3s ease!important;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.bn-08');
  if (!root) return;
  var addBtn = root.querySelector('#bn-08-add');
  var cartBtn = root.querySelector('#bn-08-cart');
  var badge = root.querySelector('#bn-08-badge');
  var live = root.querySelector('#bn-08-live');
  if (!addBtn || !cartBtn || !badge) return;
  var count = 0;
  var busy = false;
  function trigger(){
    if (busy) return;
    busy = true;
    count++;
    badge.textContent = String(count);
    cartBtn.setAttribute('aria-label', 'Cart, ' + count + ' items');
    if (live) live.textContent = 'Added to cart. ' + count + ' items in cart.';
    cartBtn.classList.add('is-bouncing');
    badge.classList.add('is-bouncing');
    setTimeout(function(){
      cartBtn.classList.remove('is-bouncing');
      badge.classList.remove('is-bouncing');
      busy = false;
    }, 800);
  }
  addBtn.addEventListener('click', trigger);
  // Auto-cycle so gallery + preview show the pattern
  setInterval(function(){
    if (count >= 5) { count = 0; badge.textContent = '0'; return; }
    trigger();
  }, 2500);
})();
```
