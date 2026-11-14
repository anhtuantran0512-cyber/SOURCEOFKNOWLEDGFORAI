---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/bento-box/"
title: "Bento Box"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The Apple-keynote bento: a dark grid of feature tiles where one 2×2 hero anchors the composition and satellites of varied spans orbit it."
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Box
Source: https://codefronts.com/layouts/css-grid-layouts/bento-box/

The Apple-keynote bento: a dark grid of feature tiles where one 2×2 hero anchors the composition and satellites of varied spans orbit it. Each tile owns a different oklch accent glow, hover lifts are compositor-only, and the whole board reflows to a clean 2-column stack on phones.
## HTML
```html
<section class="cgl-09" aria-label="Bento box grid demo">
  <div class="cgl-09__board">
    <article class="cgl-09__tile cgl-09__tile--hero" style="--glow:oklch(0.7 0.19 300)">
      <h3>One grid.<br>Every tile.</h3><p>The 2×2 hero anchors the bento; satellites auto-place around it.</p>
    </article>
    <article class="cgl-09__tile" style="--glow:oklch(0.78 0.16 200)"><h4>Auto rows</h4><p>minmax(96px, auto) — floors, not ceilings.</p></article>
    <article class="cgl-09__tile" style="--glow:oklch(0.8 0.17 140)"><h4>Spans</h4><p>span 2 wide, span 2 tall.</p></article>
    <article class="cgl-09__tile cgl-09__tile--tall" style="--glow:oklch(0.75 0.17 60)"><h4>Tall satellite</h4><p>grid-row: span 2 gives vertical rhythm without fixed heights.</p></article>
    <article class="cgl-09__tile cgl-09__tile--wide" style="--glow:oklch(0.68 0.2 20)"><h4>Wide satellite</h4><p>grid-column: span 2 — stats, charts, marquees.</p></article>
    <article class="cgl-09__tile" style="--glow:oklch(0.72 0.15 250)"><h4>Theming</h4><p>One --glow variable per tile.</p></article>
  </div>
</section>
```
## CSS
```css
.cgl-09,
.cgl-09 *,
.cgl-09 *::before,
.cgl-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-09 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.14 0.015 290);
  --txt: oklch(0.95 0.01 290);
  --dim: oklch(0.68 0.02 290);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.4rem;
}

.cgl-09 .cgl-09__board {
  display: grid;
  grid-template-columns: repeat(4,minmax(0,1fr));
  grid-auto-rows: minmax(96px,auto);
  gap: 12px;
}

.cgl-09 .cgl-09__tile {
  --glow: oklch(0.7 0.15 290);
  position: relative;
  border-radius: 16px;
  padding: 1.1rem;
  color: var(--txt);
  background: radial-gradient(140% 120% at 15% 0%,color-mix(in oklab,var(--glow) 16%,transparent),transparent 55%),oklch(0.19 0.02 290);
  border: 1px solid color-mix(in oklab,var(--glow) 28%,oklch(0.3 0.02 290));
  display: flex;
  flex-direction: column;
  gap: .45rem;
  justify-content: flex-end;
  transition: translate .25s ease,box-shadow .25s ease;
}

.cgl-09 .cgl-09__tile:hover {
  translate: 0 -3px;
  box-shadow: 0 18px 36px -18px color-mix(in oklab,var(--glow) 45%,transparent);
}

.cgl-09 .cgl-09__tile--hero {
  grid-column: span 2;
  grid-row: span 2;
  justify-content: center;
}

.cgl-09 .cgl-09__tile--wide {
  grid-column: span 2;
}

.cgl-09 .cgl-09__tile--tall {
  grid-row: span 2;
}

.cgl-09 h3 {
  font-size: clamp(1.3rem,3vw,1.8rem);
  line-height: 1.15;
  color: color-mix(in oklab,var(--glow) 70%,white);
}

.cgl-09 h4 {
  font-size: .95rem;
  color: color-mix(in oklab,var(--glow) 70%,white);
}

.cgl-09 p {
  font-size: .78rem;
  line-height: 1.55;
  color: var(--dim);
}

@media (max-width: 560px) {
  .cgl-09 .cgl-09__board {
    grid-template-columns: repeat(2,minmax(0,1fr));
  }

  .cgl-09 .cgl-09__tile--hero {
    grid-column: span 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgl-09 .cgl-09__tile {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — span geometry builds the bento; each tile re-themes through a single --glow custom property. */
```
