---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/e-commerce-checkout-live-stock-and-sales-counter/"
title: "E-commerce Checkout Live Stock & Sales Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "The scarcity block that lifts checkout conversion without lying to the shopper: a live \"only N left\" readout that ticks down as other carts claim units, a…"
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-commerce Checkout Live Stock & Sales Counter
Source: https://codefronts.com/motion/css-number-counter-animations/e-commerce-checkout-live-stock-and-sales-counter/

The scarcity block that lifts checkout conversion without lying to the shopper: a live "only N left" readout that ticks down as other carts claim units, a sold-today counter that climbs, and a stock bar that shifts hue from calm to urgent through a single color-mix() interpolation. Every change is announced politely once, never on every frame.
## HTML
```html
<section class="cnc-03" aria-label="Ecommerce live stock and sales counter demo">
  <div class="cnc-03__stage">
    <article class="cnc-03__card" data-left="ok" style="--cnc-03-cap:40">
      <div class="cnc-03__media">
        <img class="cnc-03__img" alt="Charcoal running shoe on a neutral background" loading="lazy" decoding="async"
          src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=800&auto=format&fit=crop">
        <span class="cnc-03__badge">Best seller</span>
      </div>
      <div class="cnc-03__body">
        <p class="cnc-03__brand">Atlas Athletics</p>
        <h3 class="cnc-03__name">Meridian Runner — Slate</h3>
        <p class="cnc-03__price">$148.00 <s class="cnc-03__was">$185.00</s></p>
        <div class="cnc-03__stock">
          <div class="cnc-03__meter" role="meter" aria-valuemin="0" aria-valuemax="40" aria-valuenow="12" aria-label="Units remaining in stock">
            <span class="cnc-03__fill"></span>
          </div>
          <p class="cnc-03__line">
            <span class="cnc-03__pill"><span class="cnc-03__dot" aria-hidden="true"></span><b class="cnc-03__left" aria-hidden="true">12</b> left in stock</span>
            <span class="cnc-03__sold"><b class="cnc-03__soldn" aria-hidden="true">86</b> sold today</span>
          </p>
        </div>
        <button class="cnc-03__cta" type="button">Add to cart</button>
        <p class="cnc-03__ship">Free next-day delivery · 60-day returns</p>
        <p class="cnc-03__sr" role="status" aria-live="polite"></p>
      </div>
    </article>
    <p class="cnc-03__chip" aria-hidden="true">color-mix() ramp · :has() state · single custom property drives bar + hue</p>
  </div>
</section>
```
## CSS
```css
.cnc-03,
.cnc-03 *,
.cnc-03 *::before,
.cnc-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-03-bg: oklch(0.97 0.006 95);
  --cnc-03-card: oklch(1 0 0);
  --cnc-03-ink: oklch(0.2 0.015 265);
  --cnc-03-mut: oklch(0.55 0.015 265);
  --cnc-03-ok: oklch(0.72 0.16 155);
  --cnc-03-warn: oklch(0.68 0.2 35);
  background: var(--cnc-03-bg);
  color: var(--cnc-03-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 22px;
  padding: clamp(18px,4vw,48px);
}

.cnc-03__card {
  display: grid;
  grid-template-columns: minmax(0,0.9fr) minmax(0,1.1fr);
  width: min(100%,720px);
  border-radius: 24px;
  overflow: hidden;
  background: var(--cnc-03-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 26px 60px oklch(0.4 0.03 265/.16);
  transition: box-shadow .4s;
}

.cnc-03__card[data-left="low"] {
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 26px 60px color-mix(in oklch,var(--cnc-03-warn) 28%,transparent);
}

.cnc-03__media {
  position: relative;
  min-height: 260px;
  background: linear-gradient(145deg,oklch(0.9 0.03 95),oklch(0.82 0.04 60));
}

.cnc-03__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cnc-03__badge {
  position: absolute;
  top: 14px;
  left: 14px;
  padding: 6px 11px;
  border-radius: 99px;
  background: oklch(0.2 0.015 265/.82);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  color: oklch(0.99 0 0);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.cnc-03__body {
  padding: clamp(20px,3vw,30px);
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.cnc-03__brand {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--cnc-03-mut);
}

.cnc-03__name {
  font-size: 20px;
  font-weight: 660;
  letter-spacing: -.02em;
}

.cnc-03__price {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.cnc-03__was {
  font-size: 14px;
  font-weight: 400;
  color: var(--cnc-03-mut);
  margin-left: 6px;
}

.cnc-03__stock {
  margin-top: 6px;
  display: grid;
  gap: 10px;
}

.cnc-03__meter {
  height: 8px;
  border-radius: 99px;
  background: oklch(0 0 0/.08);
  overflow: hidden;
}

.cnc-03__fill {
  display: block;
  height: 100%;
  border-radius: 99px;
  inline-size: calc(var(--cnc-03-left,12) / var(--cnc-03-cap) * 100%);
  background: color-mix(in oklch,var(--cnc-03-ok),var(--cnc-03-warn) calc(100% - (var(--cnc-03-left,12) / var(--cnc-03-cap) * 100%)));
  transition: inline-size .7s cubic-bezier(.16,1,.3,1),background .7s;
}

.cnc-03__line {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  font-size: 13.5px;
  color: var(--cnc-03-mut);
}

.cnc-03__pill {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 5px 11px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cnc-03-ok) 14%,transparent);
  color: color-mix(in oklch,var(--cnc-03-ok) 60%,black);
  font-weight: 640;
  transition: background .5s,color .5s;
}

.cnc-03__card[data-left="low"] .cnc-03__pill {
  background: color-mix(in oklch,var(--cnc-03-warn) 16%,transparent);
  color: color-mix(in oklch,var(--cnc-03-warn) 65%,black);
}

.cnc-03__dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: currentColor;
}

.cnc-03__card[data-left="low"] .cnc-03__dot {
  animation: cnc-03-pulse 1.5s ease-in-out infinite;
}

@keyframes cnc-03-pulse {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: .35;
    transform: scale(1.35);
  }
}

.cnc-03__left,
.cnc-03__soldn {
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
  font-weight: 750;
  color: var(--cnc-03-ink);
  display: inline-block;
}

.cnc-03__pill .cnc-03__left {
  color: inherit;
}

.cnc-03__bump {
  animation: cnc-03-bump .45s cubic-bezier(.16,1,.3,1);
}

@keyframes cnc-03-bump {
  0% {
    transform: translateY(0);
  }

  40% {
    transform: translateY(-4px) scale(1.08);
  }

  100% {
    transform: none;
  }
}

.cnc-03__cta {
  margin-top: 8px;
  min-height: 48px;
  border: 0;
  border-radius: 12px;
  background: var(--cnc-03-ink);
  color: oklch(0.99 0 0);
  font: inherit;
  font-size: 15px;
  font-weight: 660;
  cursor: pointer;
  transition: transform .2s,background .2s;
}

.cnc-03__cta:hover {
  background: color-mix(in oklch,var(--cnc-03-ink) 84%,var(--cnc-03-warn));
  transform: translateY(-1px);
}

.cnc-03__cta:active {
  transform: translateY(0) scale(.99);
}

.cnc-03__cta:focus-visible {
  outline: 3px solid var(--cnc-03-warn);
  outline-offset: 3px;
}

.cnc-03__ship {
  font-size: 12px;
  color: var(--cnc-03-mut);
}

.cnc-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-03__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-03-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (max-width: 640px) {
  .cnc-03__card {
    grid-template-columns: 1fr;
  }

  .cnc-03__media {
    min-height: 200px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnc-03 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.cnc-03__card').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const cap = +getComputedStyle(card).getPropertyValue('--cnc-03-cap') || 40;
    const leftEl = card.querySelector('.cnc-03__left');
    const soldEl = card.querySelector('.cnc-03__soldn');
    const meter = card.querySelector('.cnc-03__meter');
    const say = card.querySelector('.cnc-03__sr');
    let left = 12, sold = 86, sayTimer = 0;

    const tween = (el, from, to, ms) => {          // short rAF roll, integers only
      if (reduce || from === to) { el.textContent = to; return; }
      const t0 = performance.now();
      const step = (t) => {
        const p = Math.min(1, (t - t0) / ms);
        el.textContent = Math.round(from + (to - from) * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };

    const render = () => {
      card.style.setProperty('--cnc-03-left', left);
      card.dataset.left = left <= cap * 0.25 ? 'low' : 'ok';
      meter.setAttribute('aria-valuenow', left);
      leftEl.classList.remove('cnc-03__bump');
      void leftEl.offsetWidth;                      // restart the bump animation
      leftEl.classList.add('cnc-03__bump');
      clearTimeout(sayTimer);                       // announce once, after it settles
      sayTimer = setTimeout(() => { say.textContent = left + ' left in stock, ' + sold + ' sold today'; }, 700);
    };
    render();

    const tick = () => {
      if (document.visibilityState !== 'visible') return;
      if (left > 2 && Math.random() > 0.35) { const p = left; left -= 1; tween(leftEl, p, left, 500); }
      const ps = sold; sold += Math.random() > 0.5 ? 2 : 1; tween(soldEl, ps, sold, 600);
      render();
    };
    const id = setInterval(tick, 4200);
    card.querySelector('.cnc-03__cta').addEventListener('click', () => {
      if (left > 0) { const p = left; left -= 1; tween(leftEl, p, left, 400); const ps = sold; sold += 1; tween(soldEl, ps, sold, 400); render(); }
    });
    addEventListener('pagehide', () => clearInterval(id), { once: true });
  });
})();
```
