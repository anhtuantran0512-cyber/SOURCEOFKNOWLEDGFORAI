---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/card-stack-overlay/"
title: "Card Stack Overlay"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "Editorial layering without position: absolute — two cards and a caption share overlapping grid tracks, so the composition is responsive, reflowable and…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Card Stack Overlay
Source: https://codefronts.com/layouts/css-grid-layouts/card-stack-overlay/

Editorial layering without position: absolute — two cards and a caption share overlapping grid tracks, so the composition is responsive, reflowable and reorderable. Line-number placement (grid-column: 1 / 8 vs 6 / 13) creates the overlap; z-index and a backdrop-blur chip finish the art direction.
## HTML
```html
<section class="cgl-06" aria-label="Card stack overlay demo">
  <div class="cgl-06__canvas">
    <figure class="cgl-06__plate" role="img" aria-label="Abstract plum gradient artwork"></figure>
    <article class="cgl-06__card">
      <p class="cgl-06__eyebrow">Field Notes · 04</p>
      <h3>Layers are grid cells, not absolute hacks</h3>
      <p>Both cards share tracks 6–8. The overlap is computed by the grid engine, so it scales with the layout instead of drifting.</p>
      <a href="#0" class="cgl-06__link">Read the breakdown →</a>
    </article>
    <p class="cgl-06__chip">grid-column: 6 / 13</p>
  </div>
</section>
```
## CSS
```css
.cgl-06,
.cgl-06 *,
.cgl-06 *::before,
.cgl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-06 {
  width: 100%;
  min-height: 100vh;
  --plum: oklch(0.42 0.13 330);
  --gold: oklch(0.8 0.13 85);
  --paper: oklch(0.96 0.01 90);
  --ink: oklch(0.25 0.03 330);
  font-family: system-ui,sans-serif;
  background: linear-gradient(170deg,oklch(0.93 0.02 340),oklch(0.9 0.025 320));
  padding: 2rem 1.4rem;
}

.cgl-06 .cgl-06__canvas {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-template-rows: repeat(8,minmax(30px,auto));
  max-inline-size: 640px;
  margin-inline: auto;
}

.cgl-06 .cgl-06__plate {
  grid-column: 1/9;
  grid-row: 1/7;
  z-index: 1;
  border-radius: 16px;
  background: radial-gradient(120% 100% at 20% 10%,oklch(0.6 0.16 350),transparent 55%),radial-gradient(100% 120% at 90% 90%,oklch(0.35 0.12 300),transparent 60%),var(--plum);
  box-shadow: 0 24px 50px -24px oklch(0.3 0.1 330/.6);
}

.cgl-06 .cgl-06__card {
  grid-column: 6/13;
  grid-row: 4/9;
  z-index: 2;
  background: var(--paper);
  color: var(--ink);
  border-radius: 14px;
  padding: 1.4rem;
  display: flex;
  flex-direction: column;
  gap: .7rem;
  box-shadow: 0 20px 44px -20px oklch(0.3 0.08 330/.55);
}

.cgl-06 .cgl-06__eyebrow {
  font-size: .68rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--plum);
}

.cgl-06 h3 {
  font-size: clamp(1.05rem,2.6vw,1.35rem);
  line-height: 1.25;
  text-wrap: balance;
}

.cgl-06 .cgl-06__card>p:not(.cgl-06__eyebrow) {
  font-size: .85rem;
  line-height: 1.6;
  color: color-mix(in oklab,var(--ink) 75%,var(--paper));
}

.cgl-06 .cgl-06__link {
  font-size: .82rem;
  font-weight: 600;
  color: var(--plum);
  text-decoration: none;
  margin-block-start: auto;
}

.cgl-06 .cgl-06__link:hover {
  text-decoration: underline;
}

.cgl-06 .cgl-06__link:focus-visible {
  outline: 2px solid var(--plum);
  outline-offset: 3px;
}

.cgl-06 .cgl-06__chip {
  grid-column: 2/6;
  grid-row: 6/7;
  z-index: 3;
  align-self: center;
  justify-self: start;
  font-family: ui-monospace,Menlo,monospace;
  font-size: .68rem;
  color: oklch(0.98 0.005 90);
  background: oklch(0.3 0.08 330/.55);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid oklch(1 0 0/.25);
  border-radius: 999px;
  padding: .35rem .7rem;
}

@media (max-width: 520px) {
  .cgl-06 .cgl-06__plate {
    grid-column: 1/13;
    grid-row: 1/6;
  }

  .cgl-06 .cgl-06__card {
    grid-column: 2/12;
    grid-row: 4/9;
  }
}
```

## JavaScript
```js
/* No JavaScript — overlapping line-based placement creates the layered composition; z-index orders the stack. */
```
