---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/glassmorphism-frosted-glass-cards/"
title: "Glassmorphism Frosted Glass Cards"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Ultra-premium frosted glass pricing: translucent cards float over slowly drifting color blobs, with backdrop-filter blur doing the frosting and the moving…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Frosted Glass Cards
Source: https://codefronts.com/components/css-pricing-tables/glassmorphism-frosted-glass-cards/

Ultra-premium frosted glass pricing: translucent cards float over slowly drifting color blobs, with backdrop-filter blur doing the frosting and the moving background proving the glass is real — the aesthetic every AI/fintech landing page is shipping right now.
## HTML
```html
<section class="prc-15" aria-label="Frosted glass pricing cards">
  <div class="prc-15__blob prc-15__blob--1" aria-hidden="true"></div>
  <div class="prc-15__blob prc-15__blob--2" aria-hidden="true"></div>
  <div class="prc-15__blob prc-15__blob--3" aria-hidden="true"></div>
  <div class="prc-15__grid">
    <article class="prc-15__card"><h3>Glass</h3><p class="prc-15__price">$18<small>/mo</small></p><ul><li>5 seats</li><li>Core models</li><li>Community</li></ul><a href="#" class="prc-15__cta">Choose Glass</a></article>
    <article class="prc-15__card prc-15__card--hot"><span class="prc-15__flag">Popular</span><h3>Prism</h3><p class="prc-15__price">$48<small>/mo</small></p><ul><li>20 seats</li><li>All models</li><li>Priority queue</li><li>API</li></ul><a href="#" class="prc-15__cta prc-15__cta--hot">Choose Prism</a></article>
    <article class="prc-15__card"><h3>Aurora</h3><p class="prc-15__price">$120<small>/mo</small></p><ul><li>Unlimited seats</li><li>Fine-tuning</li><li>VPC deploy</li></ul><a href="#" class="prc-15__cta">Choose Aurora</a></article>
  </div>
</section>
```
## CSS
```css
.prc-15,
.prc-15 *,
.prc-15 *::before,
.prc-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-15 {
  position: relative;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0e1018;
  color: #f2f4fb;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  overflow: hidden;
}

.prc-15__blob {
  position: absolute;
  width: 44vmax;
  height: 44vmax;
  border-radius: 50%;
  filter: blur(60px);
  opacity: .55;
  will-change: transform;
}

.prc-15__blob--1 {
  background: radial-gradient(circle,oklch(0.6 0.22 300),transparent 65%);
  top: -12%;
  left: -8%;
  animation: prc-15-drift1 19s ease-in-out infinite alternate;
}

.prc-15__blob--2 {
  background: radial-gradient(circle,oklch(0.65 0.18 230),transparent 65%);
  bottom: -18%;
  right: -6%;
  animation: prc-15-drift2 23s ease-in-out infinite alternate;
}

.prc-15__blob--3 {
  background: radial-gradient(circle,oklch(0.7 0.16 25),transparent 65%);
  top: 30%;
  left: 44%;
  animation: prc-15-drift3 27s ease-in-out infinite alternate;
}

@keyframes prc-15-drift1 {
  to {
    transform: translate(14vw,10vh) scale(1.15);
  }
}

@keyframes prc-15-drift2 {
  to {
    transform: translate(-12vw,-12vh) scale(.9);
  }
}

@keyframes prc-15-drift3 {
  to {
    transform: translate(-10vw,8vh) scale(1.2);
  }
}

.prc-15__grid {
  position: relative;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 22px;
  width: min(880px,100%);
}

.prc-15__card {
  position: relative;
  background: rgba(255,255,255,.08);
  backdrop-filter: blur(22px) saturate(1.4);
  -webkit-backdrop-filter: blur(22px) saturate(1.4);
  border: 1px solid rgba(255,255,255,.16);
  border-top-color: rgba(255,255,255,.35);
  border-radius: 22px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  box-shadow: 0 24px 60px -30px rgba(0,0,0,.8);
  transition: transform .3s,background .3s;
}

.prc-15__card:hover {
  transform: translateY(-6px);
  background: rgba(255,255,255,.12);
}

.prc-15__card--hot {
  background: rgba(255,255,255,.13);
  border-color: rgba(255,255,255,.3);
}

.prc-15__flag {
  position: absolute;
  top: -11px;
  right: 22px;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 4px 11px;
  border-radius: 99px;
  background: rgba(255,255,255,.9);
  color: #1a1c2c;
}

.prc-15__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(255,255,255,.65);
}

.prc-15__price {
  font-size: 44px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-15__price small {
  font-size: 15px;
  font-weight: 600;
  color: rgba(255,255,255,.55);
}

.prc-15__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
  font-size: 13.5px;
  color: rgba(255,255,255,.8);
  flex: 1;
}

.prc-15__card li::before {
  content: "✦";
  color: rgba(255,255,255,.5);
  margin-right: 9px;
  font-size: 11px;
}

.prc-15__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,.25);
  color: #f2f4fb;
  transition: background .25s;
}

.prc-15__cta:hover {
  background: rgba(255,255,255,.14);
}

.prc-15__cta--hot {
  background: rgba(255,255,255,.92);
  color: #14162a;
  border-color: transparent;
}

.prc-15__cta--hot:hover {
  background: #fff;
}

.prc-15__cta:focus-visible {
  outline: 3px solid rgba(255,255,255,.8);
  outline-offset: 2px;
}

@media (prefers-reduced-transparency: reduce) {
  .prc-15__card {
    background: #1c1f30;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .prc-15__blob {
    animation: none;
  }

  .prc-15__card {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — three blurred radial blobs drift on infinite transform loops behind backdrop-filter:blur() cards; the frost samples the moving color live. prefers-reduced-transparency swaps to solid fills. */
```
