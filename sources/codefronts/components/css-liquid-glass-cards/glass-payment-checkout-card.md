---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/glass-payment-checkout-card/"
title: "Glass Payment Checkout Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A digital credit card that looks physically cut from Liquid Glass — a translucent frosted slab that catches and reflects the gradient behind it, with a…"
has_js: "false"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass Payment Checkout Card
Source: https://codefronts.com/components/css-liquid-glass-cards/glass-payment-checkout-card/

A digital credit card that looks physically cut from Liquid Glass — a translucent frosted slab that catches and reflects the gradient behind it, with a moving specular streak sweeping across its face like light on real glass. The card number, holder and chip sit on the tinted surface with full contrast.
## HTML
```html
<section class="lg-10" aria-label="Glass payment checkout card demo">
  <article class="lg-10__card" aria-label="Glass credit card ending 4921">
    <div class="lg-10__row1"><span class="lg-10__chip" aria-hidden="true"></span><span class="lg-10__net" aria-hidden="true">))) </span></div>
    <p class="lg-10__num">4921 •••• •••• 7043</p>
    <div class="lg-10__row2"><div><span class="lg-10__cap">Card holder</span><span class="lg-10__val">A. RIVERA</span></div><div><span class="lg-10__cap">Expires</span><span class="lg-10__val">08/29</span></div></div>
  </article>
</section>
```
## CSS
```css
.lg-10,
.lg-10 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-10 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  perspective: 1000px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 40deg at 60% 30%,#0891b2,#6d28d9,#db2777,#f59e0b,#0891b2);
  background-size: 210% 210%;
  animation: lg-10-bg 18s ease-in-out infinite;
}

@keyframes lg-10-bg {
  50% {
    background-position: 100% 100%;
  }
}

.lg-10__card {
  position: relative;
  width: min(320px,100%);
  aspect-ratio: 1.6/1;
  padding: 24px;
  border-radius: 22px;
  overflow: hidden;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 14%,transparent);
  border: 1px solid rgba(255,255,255,.45);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6),inset 0 -20px 40px rgba(0,0,0,.12),0 30px 60px -26px rgba(0,0,0,.7);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  transition: transform .5s ease;
  transform-style: preserve-3d;
}

.lg-10__card:hover {
  transform: rotateY(-10deg) rotateX(5deg);
}

.lg-10__card::before {
  content: "";
  position: absolute;
  top: -60%;
  left: -30%;
  width: 60%;
  height: 220%;
  background: linear-gradient(90deg,transparent,rgba(255,255,255,.5),transparent);
  transform: rotate(20deg);
  animation: lg-10-sheen 5s ease-in-out infinite;
  pointer-events: none;
}

@keyframes lg-10-sheen {
  0%,
    60% {
    left: -40%;
  }

  100% {
    left: 120%;
  }
}

.lg-10__card::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(120% 90% at 0% 0%,rgba(255,255,255,.28),transparent 45%);
  pointer-events: none;
}

.lg-10__row1 {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: relative;
}

.lg-10__chip {
  width: 42px;
  height: 32px;
  border-radius: 7px;
  background: linear-gradient(135deg,#fde68a,#d4a017);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.4);
}

.lg-10__net {
  font-size: 22px;
  font-weight: 900;
  letter-spacing: -2px;
  transform: rotate(90deg);
  opacity: .85;
}

.lg-10__num {
  position: relative;
  font-size: 21px;
  font-weight: 600;
  letter-spacing: .12em;
  margin-top: auto;
  padding-top: 34px;
  font-variant-numeric: tabular-nums;
  text-shadow: 0 1px 6px rgba(0,0,0,.35);
}

.lg-10__row2 {
  display: flex;
  justify-content: space-between;
  margin-top: 18px;
  position: relative;
}

.lg-10__cap {
  display: block;
  font-size: 9px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(255,255,255,.7);
}

.lg-10__val {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .05em;
}

@media (prefers-reduced-motion: reduce) {
  .lg-10 {
    animation: none;
  }

  .lg-10__card::before {
    animation: none;
    opacity: 0;
  }

  .lg-10__card:hover {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a frosted slab over a rich mesh gradient reflects colour through the glass, an animated ::before specular streak sweeps the face, and a hover perspective tilt shifts the reflection. */
```
