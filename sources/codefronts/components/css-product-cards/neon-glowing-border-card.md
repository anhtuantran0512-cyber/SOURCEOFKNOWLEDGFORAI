---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/neon-glowing-border-card/"
title: "Neon Glowing Border Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A dark card wrapped in a rotating conic-gradient neon border that ignites and spins on hover, with a matching box-shadow pulse."
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glowing Border Card
Source: https://codefronts.com/components/css-product-cards/neon-glowing-border-card/

A dark card wrapped in a rotating conic-gradient neon border that ignites and spins on hover, with a matching box-shadow pulse. The futuristic glowing-outline effect crypto, gaming and product-launch pages search for.
## HTML
```html
<article class="cpc-09">
  <div class="cpc-09__card">
    <div class="cpc-09__face">
      <div class="cpc-09__media" role="img" aria-label="Product photo: Flux mechanical watch"><span>product shot</span></div>
      <div class="cpc-09__body">
        <p class="cpc-09__brand">Flux</p>
        <h3 class="cpc-09__name">Flux Automatic Watch</h3>
        <div class="cpc-09__row"><p class="cpc-09__price">$460</p><button class="cpc-09__cta" type="button">Add to Cart</button></div>
      </div>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-09,
.cpc-09 *,
.cpc-09 *::before,
.cpc-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-09 ::selection {
  background: oklch(0.72 0.24 330);
  color: #fff;
}

@property --angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.cpc-09 {
  --c1: oklch(0.82 0.16 200);
  --c2: oklch(0.72 0.24 330);
  --c3: oklch(0.85 0.18 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: radial-gradient(120% 120% at 50% 20%,#0c0b12,#050408);
}

.cpc-09__card {
  position: relative;
  width: 320px;
  border-radius: 20px;
  padding: 2px;
  isolation: isolate;
}

.cpc-09__card::before,
.cpc-09__card::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 20px;
  z-index: -1;
  background: conic-gradient(from var(--angle),var(--c1),var(--c2),var(--c3),var(--c1));
  animation: cpc-09-spin 6s linear infinite paused;
  opacity: .5;
  transition: opacity .4s;
}

.cpc-09__card::after {
  filter: blur(18px);
  opacity: .25;
}

.cpc-09__card:hover::before,
.cpc-09__card:hover::after {
  animation-play-state: running;
}

.cpc-09__card:hover::before {
  opacity: 1;
}

.cpc-09__card:hover::after {
  opacity: .7;
}

@keyframes cpc-09-spin {
  to {
    --angle: 360deg;
  }
}

.cpc-09__face {
  border-radius: 18px;
  overflow: hidden;
  background: #0b0a11;
}

.cpc-09__media {
  aspect-ratio: 16/11;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#171522,#0f0e18),repeating-linear-gradient(45deg,rgba(255,255,255,.04) 0 14px,transparent 14px 28px);
}

.cpc-09__media {
  background-image: url("https://images.unsplash.com/photo-1502823403499-6ccfcf4fb453?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-09__media span {
  display: none;
}

.cpc-09__body {
  padding: 20px 22px 22px;
}

.cpc-09__brand {
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--c2);
}

.cpc-09__name {
  margin-top: 6px;
  font-size: 18px;
  font-weight: 600;
  color: #f1eefb;
}

.cpc-09__row {
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cpc-09__price {
  font-size: 22px;
  font-weight: 800;
  color: #fff;
}

.cpc-09__cta {
  height: 44px;
  padding: 0 22px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: linear-gradient(120deg,var(--c1),var(--c2));
  color: #0a0713;
  font-size: 14px;
  font-weight: 700;
}

.cpc-09__cta:hover {
  filter: brightness(1.08);
}

.cpc-09__cta:focus-visible {
  outline: 3px solid var(--c1);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cpc-09__card::before,
    .cpc-09__card::after {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a registered @property --angle spins a conic-gradient border on :hover. */
```
