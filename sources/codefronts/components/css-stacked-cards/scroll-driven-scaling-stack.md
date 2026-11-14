---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/scroll-driven-scaling-stack/"
title: "Scroll-Driven Scaling Stack"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "The storytelling landing-page hero: as the reader scrolls, each card pins to the viewport with position:sticky while the card beneath it scales down and…"
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Driven Scaling Stack
Source: https://codefronts.com/components/css-stacked-cards/scroll-driven-scaling-stack/

The storytelling landing-page hero: as the reader scrolls, each card pins to the viewport with position:sticky while the card beneath it scales down and darkens, mimicking physical compression and depth — all driven by native scroll-driven animations, no scroll library.
## HTML
```html
<section class="scd-01" aria-label="Scroll-driven scaling card stack">
  <div class="scd-01__scene">
    <p class="scd-01__hint">Scroll ↓ inside this panel</p>
    <article class="scd-01__card" style="--i:0"><span class="scd-01__num">01</span><h3>Capture</h3><p>Every idea starts as a rough note. We pin it before it escapes.</p></article>
    <article class="scd-01__card" style="--i:1"><span class="scd-01__num">02</span><h3>Shape</h3><p>Notes compress into a plan — the earlier one settles quietly behind.</p></article>
    <article class="scd-01__card" style="--i:2"><span class="scd-01__num">03</span><h3>Ship</h3><p>The plan surfaces on top, in focus, ready to hand off.</p></article>
    <article class="scd-01__card" style="--i:3"><span class="scd-01__num">04</span><h3>Reflect</h3><p>What worked stacks up as depth you can scroll back through.</p></article>
    <div class="scd-01__end">Fin.</div>
  </div>
</section>
```
## CSS
```css
.scd-01,
.scd-01 *,
.scd-01 *::before,
.scd-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-01 {
  --accent: oklch(0.62 0.17 264);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #eef0f4;
  width: 100%;
  height: 100vh;
  overflow-y: auto;
  scroll-behavior: smooth;
  padding: 0 20px;
}

.scd-01__scene {
  width: min(520px,100%);
  margin: 0 auto;
  padding: 14vh 0 40vh;
}

.scd-01__hint {
  position: sticky;
  top: 16px;
  text-align: center;
  font-size: 12px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #8a90a0;
  margin-bottom: 6vh;
}

.scd-01__card {
  position: sticky;
  top: calc(90px + var(--i) * 16px);
  height: 260px;
  margin-bottom: 60px;
  border-radius: 22px;
  padding: 34px;
  color: #fff;
  background: linear-gradient(135deg,var(--accent),oklch(0.55 0.16 292));
  box-shadow: 0 30px 60px -34px rgba(20,24,50,.7);
  animation: scd-01-shrink linear both;
  animation-timeline: view();
  animation-range: exit;
}

.scd-01__card:nth-child(3) {
  background: linear-gradient(135deg,oklch(0.66 0.15 200),oklch(0.6 0.16 250));
}

.scd-01__card:nth-child(4) {
  background: linear-gradient(135deg,oklch(0.7 0.15 150),oklch(0.62 0.15 200));
}

.scd-01__card:nth-child(5) {
  background: linear-gradient(135deg,oklch(0.72 0.16 60),oklch(0.64 0.17 30));
}

.scd-01__num {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .2em;
  opacity: .7;
}

.scd-01__card h3 {
  font-size: 30px;
  font-weight: 800;
  margin: 14px 0 10px;
  letter-spacing: -.02em;
}

.scd-01__card p {
  font-size: 16px;
  line-height: 1.55;
  max-width: 34ch;
  opacity: .92;
}

.scd-01__end {
  text-align: center;
  font-size: 14px;
  color: #a0a6b4;
  padding-top: 12vh;
}

@keyframes scd-01-shrink {
  to {
    transform: scale(.9);
    filter: brightness(.72);
  }
}

@media (prefers-reduced-motion: reduce) {
  .scd-01 {
    width: 100%;
    min-height: 100vh;
    scroll-behavior: auto;
  }

  .scd-01__card {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — position:sticky pins each card and a scroll-driven view() timeline scales and darkens it as the next card covers it. Falls back to a plain sticky stack where unsupported. */
```
