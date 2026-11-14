---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/floating-cart-badge/"
title: "Floating Cart Button with Live Badge Counter CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "The mobile-commerce pattern: a persistent cart button that shows count and running total, and an add-to-cart that physically throws the product thumbnail…"
has_js: "true"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Cart Button with Live Badge Counter CSS
Source: https://codefronts.com/components/css-floating-buttons/floating-cart-badge/

The mobile-commerce pattern: a persistent cart button that shows count and running total, and an add-to-cart that physically throws the product thumbnail into it. The flight uses the Web Animations API with a cubic path, the badge bumps on arrival, and the total counts up rather than snapping — three cheap cues that make the basket feel real.
## HTML
```html
<section class="fb-22" aria-label="Floating cart button demo">
  <div class="fb-22__shop">
    <header class="fb-22__head">
      <p class="fb-22__eyebrow">Web Animations API · arced flight</p>
      <h2 class="fb-22__title">Throw it in the basket</h2>
      <p class="fb-22__sub">Add anything. The thumbnail arcs into the cart, the badge bumps on arrival, and the total rolls instead of snapping.</p>
    </header>
    <ul class="fb-22__grid">
      <li class="fb-22__card">
        <img class="fb-22__img" src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=500&auto=format&fit=crop" alt="Red high-top trainer" loading="lazy">
        <div class="fb-22__info"><b>Court Hi Trainer</b><span>£128.00</span></div>
        <button class="fb-22__add" type="button" data-fb-price="128" data-fb-name="Court Hi Trainer">Add</button>
      </li>
      <li class="fb-22__card">
        <img class="fb-22__img" src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=500&auto=format&fit=crop" alt="Analogue wristwatch" loading="lazy">
        <div class="fb-22__info"><b>Field Watch 38</b><span>£196.00</span></div>
        <button class="fb-22__add" type="button" data-fb-price="196" data-fb-name="Field Watch 38">Add</button>
      </li>
      <li class="fb-22__card">
        <img class="fb-22__img" src="https://images.unsplash.com/photo-1560343090-f0409e92791a?q=80&w=500&auto=format&fit=crop" alt="Leather crossbody bag" loading="lazy">
        <div class="fb-22__info"><b>Everyday Crossbody</b><span>£84.00</span></div>
        <button class="fb-22__add" type="button" data-fb-price="84" data-fb-name="Everyday Crossbody">Add</button>
      </li>
    </ul>
    <p class="fb-22__sr" id="fb-22-status" role="status" aria-live="polite"></p>
  </div>
  <button class="fb-22__cart" id="fb-22-cart" type="button" aria-label="Basket, empty">
    <span class="fb-22__cIco" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M4 5h2.2l2 10h9.4l2-7H7" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/><circle cx="9.5" cy="19" r="1.7" fill="currentColor"/><circle cx="17" cy="19" r="1.7" fill="currentColor"/></svg></span>
    <span class="fb-22__total" id="fb-22-total">£0</span>
    <span class="fb-22__badge" id="fb-22-badge" data-zero="true">0</span>
  </button>
</section>
```
## CSS
```css
.fb-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-22-bg);
  --fb-22-bg: oklch(0.97 0.008 85);
  --fb-22-brand: oklch(0.32 0.05 155);
  --fb-22-accent: oklch(0.66 0.16 145);
  --fb-22-ink: oklch(0.22 0.02 85);
  --fb-22-mut: oklch(0.53 0.015 85);
  --fb-22-card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-22-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,52px);
  overflow: hidden;
}

.fb-22 *,
.fb-22 *::before,
.fb-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-22__shop {
  width: min(100%,880px);
  display: grid;
  gap: clamp(18px,3vw,30px);
  justify-items: center;
}

.fb-22__head {
  display: grid;
  gap: 10px;
  justify-items: center;
  text-align: center;
  max-width: 52ch;
}

.fb-22__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-22-brand);
}

.fb-22__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-22__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-22-mut);
  text-wrap: pretty;
}

.fb-22__grid {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(190px,1fr));
  gap: clamp(12px,2.5vw,20px);
  width: 100%;
}

.fb-22__card {
  display: grid;
  gap: 11px;
  padding: 11px;
  border-radius: 20px;
  background: var(--fb-22-card);
  border: 1px solid oklch(0.22 0.02 85/.08);
  box-shadow: 0 16px 40px -30px oklch(0.22 0.02 85/.9);
}

.fb-22__img {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  border-radius: 14px;
  background: oklch(0.93 0.01 85);
  display: block;
}

.fb-22__info {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 8px;
  padding: 0 4px;
}

.fb-22__info b {
  font-size: 13.8px;
  font-weight: 640;
  letter-spacing: -.01em;
}

.fb-22__info span {
  font-size: 13px;
  color: var(--fb-22-mut);
  font-variant-numeric: tabular-nums;
}

.fb-22__add {
  min-height: 44px;
  border: 0;
  border-radius: 13px;
  background: var(--fb-22-brand);
  color: oklch(0.98 0.01 155);
  font-size: 13.5px;
  font-weight: 650;
  font-family: inherit;
  cursor: pointer;
  transition: background .18s ease,transform .18s ease;
}

.fb-22__add:hover {
  background: oklch(0.42 0.09 152);
}

.fb-22__add:active {
  transform: scale(.97);
}

.fb-22__add:focus-visible {
  outline: 3px solid var(--fb-22-brand);
  outline-offset: 2px;
}

.fb-22__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fb-22__cart {
  position: absolute;
  right: clamp(16px,3.5vw,36px);
  bottom: calc(clamp(16px,3.5vw,36px) + env(safe-area-inset-bottom));
  z-index: 6;
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 60px;
  padding: 0 20px 0 16px;
  border: 0;
  border-radius: 99px;
  cursor: pointer;
  color: oklch(0.98 0.01 155);
  background: linear-gradient(150deg,oklch(0.42 0.09 150),var(--fb-22-brand));
  box-shadow: 0 14px 34px -12px oklch(0.32 0.05 155/.9),0 2px 6px oklch(0.2 0.03 155/.3);
  transition: transform .28s cubic-bezier(.2,1.3,.4,1),box-shadow .28s ease;
}

.fb-22__cIco {
  display: grid;
  place-items: center;
}

.fb-22__cIco svg {
  width: 25px;
  height: 25px;
}

.fb-22__total {
  font-size: 15px;
  font-weight: 680;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.01em;
}

.fb-22__cart:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 44px -12px oklch(0.32 0.05 155/.95);
}

.fb-22__cart:active {
  transform: scale(.96);
}

.fb-22__cart:focus-visible {
  outline: 3px solid var(--fb-22-brand);
  outline-offset: 4px;
}

.fb-22__badge {
  position: absolute;
  top: -6px;
  right: -4px;
  min-width: 24px;
  height: 24px;
  padding: 0 7px;
  border-radius: 99px;
  background: var(--fb-22-accent);
  color: oklch(0.18 0.05 150);
  font-size: 12px;
  font-weight: 750;
  line-height: 24px;
  text-align: center;
  font-variant-numeric: tabular-nums;
  box-shadow: 0 0 0 3px oklch(0.96 0.008 85);
  transition: scale .26s cubic-bezier(.2,1.6,.4,1),opacity .2s ease;
}

.fb-22__badge[data-zero="true"] {
  scale: 0;
  opacity: 0;
}

.fb-22__badge[data-bump="true"] {
  animation: fb-22-bump .36s cubic-bezier(.2,1.6,.4,1);
}

@keyframes fb-22-bump {
  0% {
    scale: 1;
  }

  42% {
    scale: 1.36;
  }

  100% {
    scale: 1;
  }
}

.fb-22-fly {
  position: fixed;
  z-index: 99;
  border-radius: 12px;
  object-fit: cover;
  pointer-events: none;
  box-shadow: 0 12px 26px -10px oklch(0.22 0.02 85/.8);
}

@media (prefers-reduced-motion: reduce) {
  .fb-22 * {
    transition: none !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const cart = document.getElementById('fb-22-cart');
  const badge = document.getElementById('fb-22-badge');
  const totalEl = document.getElementById('fb-22-total');
  const status = document.getElementById('fb-22-status');
  if (!cart || cart.dataset.fbWired) return;
  cart.dataset.fbWired = '1';
  const money = new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP', maximumFractionDigits: 0 });
  const calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let count = 0, total = 0, shown = 0;
  const roll = (to) => {
    const from = shown, t0 = performance.now();
    const step = (t) => {
      const p = Math.min((t - t0) / 420, 1);
      shown = from + (to - from) * (1 - Math.pow(1 - p, 3));
      totalEl.textContent = money.format(Math.round(shown));
      if (p < 1) requestAnimationFrame(step);
    };
    if (calm) { shown = to; totalEl.textContent = money.format(to); return; }
    requestAnimationFrame(step);
  };
  const land = () => {
    badge.textContent = String(count);
    badge.dataset.zero = String(count === 0);
    badge.dataset.bump = 'true';
    setTimeout(() => { badge.dataset.bump = 'false'; }, 400);
  };
  document.querySelectorAll('.fb-22__add').forEach((btn) => {
    btn.addEventListener('click', () => {
      const card = btn.closest('.fb-22__card');
      const img = card.querySelector('.fb-22__img');
      const price = Number(btn.dataset.fbPrice);
      count += 1; total += price;
      const a = img.getBoundingClientRect(), b = cart.getBoundingClientRect();
      if (!calm) {
        const fly = img.cloneNode();
        fly.className = 'fb-22-fly';
        fly.style.cssText += 'left:' + a.left + 'px;top:' + a.top + 'px;width:' + a.width + 'px;height:' + a.height + 'px;';
        document.body.append(fly);
        const dx = b.left + b.width / 2 - (a.left + a.width / 2);
        const dy = b.top + b.height / 2 - (a.top + a.height / 2);
        const anim = fly.animate([
          { transform: 'translate(0,0) scale(1)', opacity: 1 },
          { transform: 'translate(' + dx * 0.5 + 'px,' + (dy * 0.5 - 90) + 'px) scale(.6)', opacity: .95, offset: .55 },
          { transform: 'translate(' + dx + 'px,' + dy + 'px) scale(.14)', opacity: .3 }
        ], { duration: 640, easing: 'cubic-bezier(.4,.05,.6,1)' });
        anim.onfinish = () => { fly.remove(); land(); };
      } else { land(); }
      roll(total);
      cart.setAttribute('aria-label', 'Basket, ' + count + (count === 1 ? ' item, ' : ' items, ') + money.format(total));
      status.textContent = 'Added ' + btn.dataset.fbName + '. Basket: ' + count + (count === 1 ? ' item, ' : ' items, ') + money.format(total) + '.';
    });
  });
})();
```
