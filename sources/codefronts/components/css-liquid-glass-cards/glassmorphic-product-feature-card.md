---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/glassmorphic-product-feature-card/"
title: "Glassmorphic Product Feature Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A premium product card where a frosted Liquid Glass panel cuts diagonally across a product image, distorting the part of the shot behind it to create real…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphic Product Feature Card
Source: https://codefronts.com/components/css-liquid-glass-cards/glassmorphic-product-feature-card/

A premium product card where a frosted Liquid Glass panel cuts diagonally across a product image, distorting the part of the shot behind it to create real depth — the 'Apple-like' presentation e-commerce teams chase. Copy on the glass stays crisp; the product reads as sitting behind the pane.
## HTML
```html
<section class="lg-03" aria-label="Glassmorphic product feature card demo">
  <article class="lg-03__card">
    <div class="lg-03__shot" role="img" aria-label="Product photo: over-ear headphones in graphite"><span class="lg-03__ph">product shot</span></div>
    <div class="lg-03__glass">
      <p class="lg-03__brand">AURA · Studio</p>
      <h3 class="lg-03__name">Halo One Headphones</h3>
      <div class="lg-03__row"><span class="lg-03__price">$349</span><span class="lg-03__cta">View →</span></div>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-03,
.lg-03 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-03 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 80% 10%,#fca5a5,#7f1d1d 60%,#1c0808);
}

.lg-03__card {
  position: relative;
  width: min(300px,100%);
  aspect-ratio: 3/4;
  border-radius: 26px;
  overflow: hidden;
  isolation: isolate;
  box-shadow: 0 34px 70px -30px rgba(0,0,0,.8);
  border: 1px solid rgba(255,255,255,.25);
}

.lg-03__shot {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(60deg,#5b6472,#5b6472 12px,#6c7686 12px,#6c7686 24px);
  display: grid;
  place-items: center;
}

.lg-03__ph {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  color: rgba(255,255,255,.7);
  letter-spacing: .05em;
}

.lg-03__glass {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 22px 22px 24px;
  clip-path: polygon(0 28%,100% 0,100% 100%,0 100%);
  isolation: isolate;
  background: color-mix(in oklab,white 14%,transparent);
  border-top: 1px solid rgba(255,255,255,.5);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6);
  backdrop-filter: blur(16px) saturate(200%);
  -webkit-backdrop-filter: blur(16px) saturate(200%);
}

.lg-03__glass::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(120deg,rgba(255,255,255,.35),transparent 40%);
  pointer-events: none;
  mix-blend-mode: screen;
}

.lg-03__brand {
  position: relative;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(255,255,255,.8);
  margin-top: 14px;
}

.lg-03__name {
  position: relative;
  color: #fff;
  font-size: 21px;
  font-weight: 800;
  letter-spacing: -.01em;
  margin: 6px 0 14px;
}

.lg-03__row {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.lg-03__price {
  color: #fff;
  font-size: 22px;
  font-weight: 800;
}

.lg-03__cta {
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  padding: 8px 14px;
  border-radius: 999px;
  background: rgba(255,255,255,.2);
  border: 1px solid rgba(255,255,255,.4);
}
```

## JavaScript
```js
/* No JavaScript — a clip-path glass panel with backdrop-filter blur()+saturate() overlaps the product photo and distorts the pixels behind it. Swap the striped placeholder for your own shot. */
```
