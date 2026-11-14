---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/digital-coupon-discount-card/"
title: "Digital Coupon / Discount Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A ticket-shaped discount card whose promo code sits blurred behind a frosted strip — move your cursor (or focus it) and a Liquid Glass lens travels across…"
has_js: "true"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Digital Coupon / Discount Card
Source: https://codefronts.com/components/css-liquid-glass-cards/digital-coupon-discount-card/

A ticket-shaped discount card whose promo code sits blurred behind a frosted strip — move your cursor (or focus it) and a Liquid Glass lens travels across the strip, sharpening and magnifying the code beneath it like a scratch-off reveal. Perforated edge notches and a dashed tear line complete the ticket look.
## HTML
```html
<section class="lg-15" aria-label="Liquid glass digital coupon card demo">
  <article class="lg-15__ticket" id="lg-15-ticket">
    <div class="lg-15__left">
      <p class="lg-15__brand">CodeFronts Store</p>
      <p class="lg-15__off">25% OFF</p>
      <p class="lg-15__desc">First order · all component packs</p>
    </div>
    <div class="lg-15__perf" aria-hidden="true"></div>
    <div class="lg-15__right">
      <p class="lg-15__cap">Promo code</p>
      <div class="lg-15__codewrap">
        <span class="lg-15__code" id="lg-15-code">GLASS25</span>
        <span class="lg-15__frost" aria-hidden="true"></span>
        <span class="lg-15__lens" id="lg-15-lens" aria-hidden="true"><span class="lg-15__lenscode">GLASS25</span></span>
      </div>
      <button class="lg-15__copy" id="lg-15-copy" type="button">Copy code</button>
      <p class="lg-15__live" id="lg-15-live" aria-live="polite"></p>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-15,
.lg-15 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-15 {
  width: 100%;
  --accent: oklch(0.72 0.19 25);
  --r: 52px;
  display: grid;
  place-items: center;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 80% 10%,#fb923c,#b91c1c 55%,#450a0a);
}

.lg-15__ticket {
  position: relative;
  display: flex;
  width: min(420px,100%);
  border-radius: 20px;
  overflow: hidden;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 13%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.55),0 28px 58px -28px rgba(0,0,0,.7);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
}

.lg-15__left {
  flex: 1;
  padding: 22px;
}

.lg-15__brand {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,255,255,.8);
}

.lg-15__off {
  font-size: 40px;
  font-weight: 900;
  letter-spacing: -.03em;
  margin: 6px 0;
  text-shadow: 0 2px 12px rgba(0,0,0,.35);
}

.lg-15__desc {
  font-size: 12.5px;
  color: rgba(255,255,255,.82);
  max-width: 22ch;
}

.lg-15__perf {
  width: 2px;
  border-left: 2px dashed rgba(255,255,255,.55);
  position: relative;
}

.lg-15__perf::before,
.lg-15__perf::after {
  content: "";
  position: absolute;
  left: -9px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #8f1717;
}

.lg-15__perf::before {
  top: -9px;
}

.lg-15__perf::after {
  bottom: -9px;
}

.lg-15__right {
  width: 172px;
  padding: 22px 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background: rgba(255,255,255,.06);
}

.lg-15__cap {
  font-size: 10px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
}

.lg-15__codewrap {
  position: relative;
  margin: 10px 0 14px;
  width: 130px;
  height: 44px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  background: rgba(0,0,0,.22);
  overflow: hidden;
  cursor: crosshair;
}

.lg-15__code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 20px;
  font-weight: 800;
  letter-spacing: .14em;
  color: #fff;
}

.lg-15__frost {
  position: absolute;
  inset: 0;
  backdrop-filter: blur(5px) brightness(1.05);
  -webkit-backdrop-filter: blur(5px) brightness(1.05);
  background: rgba(255,255,255,.08);
}

.lg-15__lens {
  position: absolute;
  top: 50%;
  left: var(--lx,50%);
  width: var(--r);
  height: var(--r);
  border-radius: 50%;
  transform: translate(-50%,-50%) scale(0);
  transform-origin: center;
  overflow: hidden;
  display: grid;
  place-items: center;
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.7);
  box-shadow: inset 0 2px 6px rgba(255,255,255,.6),0 6px 14px -4px rgba(0,0,0,.5);
  transition: transform .18s ease;
}

.lg-15__codewrap:hover .lg-15__lens,
.lg-15__ticket.is-reveal .lg-15__lens {
  transform: translate(-50%,-50%) scale(1);
}

.lg-15__lenscode {
  position: absolute;
  left: calc(65px - var(--lx,65px));
  top: 50%;
  transform: translateY(-50%);
  font-family: ui-monospace,Menlo,monospace;
  font-size: 20px;
  font-weight: 800;
  letter-spacing: .14em;
  color: #fff;
  white-space: nowrap;
  text-shadow: 0 1px 3px rgba(0,0,0,.4);
}

.lg-15__copy {
  min-height: 40px;
  padding: 0 16px;
  border: 0;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 700;
  font-size: 13px;
  color: #fff;
  background: var(--accent);
  box-shadow: 0 8px 20px -8px var(--accent);
}

.lg-15__copy:hover {
  filter: brightness(1.08);
}

.lg-15__copy:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.lg-15__live {
  font-size: 11px;
  color: #ffe;
  min-height: 1.1em;
  margin-top: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-15__lens {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const wrap = document.querySelector('.lg-15__codewrap');
  const ticket = document.querySelector('#lg-15-ticket');
  const lens = document.querySelector('#lg-15-lens');
  const lensCode = lens && lens.querySelector('.lg-15__lenscode');
  const copy = document.querySelector('#lg-15-copy');
  const live = document.querySelector('#lg-15-live');
  const code = document.querySelector('#lg-15-code');
  if (!wrap) return;
  wrap.addEventListener('pointermove', (e) => {
    const r = wrap.getBoundingClientRect();
    const x = Math.max(0, Math.min(r.width, e.clientX - r.left));
    wrap.style.setProperty('--lx', x + 'px');
    if (lensCode) lensCode.style.left = (r.width/2 - x) + 'px';
  });
  wrap.addEventListener('focus', () => ticket.classList.add('is-reveal'));
  wrap.addEventListener('blur', () => ticket.classList.remove('is-reveal'));
  copy.addEventListener('click', () => {
    const text = code.textContent.trim();
    const done = () => { live.textContent = 'Copied “' + text + '” to clipboard'; };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done).catch(done);
    else done();
  });
})();
```
