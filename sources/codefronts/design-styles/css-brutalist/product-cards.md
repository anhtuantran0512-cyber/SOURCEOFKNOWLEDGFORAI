---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/product-cards/"
title: "Brutalist Product Card Grid"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "Raw e-commerce: Times body copy, zero radius, visible black frames on every image and prices set in plain bold."
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Product Card Grid
Source: https://codefronts.com/design-styles/css-brutalist/product-cards/

Raw e-commerce: Times body copy, zero radius, visible black frames on every image and prices set in plain bold. The spacing is deliberately uneven — 1rem here, 3rem there — because brutalism is anti-design, and evenly-distributed comfort is exactly the thing it refuses. Everything still works: focus states, semantic structure, real product data.
## HTML
```html
<div class="brt-15">
  <input class="brt-15__sr" type="checkbox" id="brt-15-dark">
  <label class="brt-15__theme" for="brt-15-dark">
    <svg class="brt-15__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-15__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-15__vh">Dark theme</span>
  </label>

  <div class="brt-15__stage">
    <section class="brt-15__wrap" aria-labelledby="brt-15-h">
      <header class="brt-15__head">
        <h1 class="brt-15__h" id="brt-15-h">GOODS / INDEX</h1>
        <p class="brt-15__meta">6 items. Prices include VAT. Shipped from Leeds on Tuesdays.</p>
        <ul class="brt-15__tags">
          <li><a class="brt-15__tag" href="#brt-15-h" aria-current="true">ALL</a></li>
          <li><a class="brt-15__tag" href="#brt-15-h">BAGS</a></li>
          <li><a class="brt-15__tag" href="#brt-15-h">PAPER</a></li>
          <li><a class="brt-15__tag" href="#brt-15-h">TOOLS</a></li>
        </ul>
      </header>

      <ul class="brt-15__grid">
        <li class="brt-15__card">
          <figure class="brt-15__frame"><img class="brt-15__shot" src="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=520&amp;h=520&amp;fit=crop&amp;auto=format" width="520" height="520" alt="Canvas tote bag standing upright on a concrete floor" loading="lazy" decoding="async"></figure>
          <h2 class="brt-15__name"><a href="#brt-15-h">Warehouse Tote, 18oz canvas</a></h2>
          <p class="brt-15__spec">Undyed. Repaired free, forever.</p>
          <p class="brt-15__price">£48.00</p>
        </li>
        <li class="brt-15__card">
          <figure class="brt-15__frame"><img class="brt-15__shot" src="https://images.unsplash.com/photo-1531891437562-4301cf35b7e4?w=520&amp;h=520&amp;fit=crop&amp;auto=format" width="520" height="520" alt="Stack of hardbound notebooks on a plain surface" loading="lazy" decoding="async"></figure>
          <h2 class="brt-15__name"><a href="#brt-15-h">Grid Notebook, A5, 160pp</a></h2>
          <p class="brt-15__spec">100gsm. Lies flat. No branding.</p>
          <p class="brt-15__price">£14.00</p>
        </li>
        <li class="brt-15__card" data-stock="out">
          <figure class="brt-15__frame"><img class="brt-15__shot" src="https://images.unsplash.com/photo-1581244277943-fe4a9c777189?w=520&amp;h=520&amp;fit=crop&amp;auto=format" width="520" height="520" alt="Metal ruler and drawing tools arranged on paper" loading="lazy" decoding="async"></figure>
          <h2 class="brt-15__name"><a href="#brt-15-h">Steel Rule, 300mm</a></h2>
          <p class="brt-15__spec">Etched, not printed. Made in Sheffield.</p>
          <p class="brt-15__price">£22.00 <span class="brt-15__out">SOLD OUT</span></p>
        </li>
        <li class="brt-15__card">
          <figure class="brt-15__frame"><img class="brt-15__shot" src="https://images.unsplash.com/photo-1503602642458-232111445657?w=520&amp;h=520&amp;fit=crop&amp;auto=format" width="520" height="520" alt="Enamel mug on a wooden bench" loading="lazy" decoding="async"></figure>
          <h2 class="brt-15__name"><a href="#brt-15-h">Enamel Mug, 350ml</a></h2>
          <p class="brt-15__spec">Chips. That is the point.</p>
          <p class="brt-15__price">£11.50</p>
        </li>
        <li class="brt-15__card">
          <figure class="brt-15__frame"><img class="brt-15__shot" src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=520&amp;h=520&amp;fit=crop&amp;auto=format" width="520" height="520" alt="Compact camera resting on a shelf" loading="lazy" decoding="async"></figure>
          <h2 class="brt-15__name"><a href="#brt-15-h">Reload Camera, fixed 32mm</a></h2>
          <p class="brt-15__spec">No screen. No settings. One button.</p>
          <p class="brt-15__price">£96.00</p>
        </li>
        <li class="brt-15__card">
          <figure class="brt-15__frame"><img class="brt-15__shot" src="https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=520&amp;h=520&amp;fit=crop&amp;auto=format" width="520" height="520" alt="Folded print poster on a flat surface" loading="lazy" decoding="async"></figure>
          <h2 class="brt-15__name"><a href="#brt-15-h">Wall Print, 50 × 70cm</a></h2>
          <p class="brt-15__spec">Risograph, two passes, 200 made.</p>
          <p class="brt-15__price">£34.00</p>
        </li>
      </ul>
      <p class="brt-15__foot">Returns within 30 days. Email [email protected] — a person replies.</p>
    </section>
  </div>
</div>
```
## CSS
```css
.brt-15 {
  --page: #f2f1ec;
  --panel: #ffffff;
  --ink: #000000;
  --muted: #3a3a3a;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Times New Roman',Times,Georgia,serif;
  font-size: 17px;
}

.brt-15 *,
.brt-15 *::before,
.brt-15 *::after {
  box-sizing: border-box;
  border-radius: 0;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-15 {
    --page: oklch(0.957 0.006 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0 0 0);
    --muted: oklch(0.34 0 0);
  }
}

.brt-15__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-15__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-15__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
}

.brt-15__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-15__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-15__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-15__sr:focus-visible + .brt-15__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-15__sun {
  display: none;
}

.brt-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(1rem,3vw,2.5rem);
}

.brt-15__wrap {
  inline-size: min(72rem,100%);
}

.brt-15__head {
  padding-block-end: .5rem;
  padding-inline-end: 3.5rem;
  border-block-end: 5px solid var(--edge);
}

.brt-15__h {
  margin: 0;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  font-size: clamp(2rem,7vw,4rem);
  font-weight: 700;
  letter-spacing: -.03em;
  line-height: .95;
  text-transform: uppercase;
}

.brt-15__meta {
  margin: .35rem 0 1.25rem;
  font-size: 1rem;
  line-height: 1.45;
  color: var(--muted);
}

.brt-15__tags {
  list-style: none;
  margin: 0 0 .5rem;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0;
}

.brt-15__tag {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .5rem .9rem;
  font-family: ui-monospace,'SF Mono',Menlo,Consolas,monospace;
  font-size: .82rem;
  letter-spacing: .1em;
  color: var(--ink);
  text-decoration: none;
  border: var(--bw) solid var(--edge);
  border-inline-end: 0;
}

.brt-15__tags li:last-child .brt-15__tag {
  border-inline-end: var(--bw) solid var(--edge);
}

.brt-15__tag[aria-current="true"],
.brt-15__tag:hover {
  background: var(--ink);
  color: var(--page);
}

.brt-15__tag:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: -6px;
}

.brt-15__grid {
  list-style: none;
  margin: 2.5rem 0 0;
  padding: 0;
  display: grid;
  gap: 3px;
  grid-template-columns: repeat(auto-fill,minmax(min(15rem,100%),1fr));
}

.brt-15__card {
  position: relative;
  padding: .75rem .75rem 1.5rem;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
}

.brt-15__card:hover,
.brt-15__card:focus-within {
  background: var(--ink);
  color: var(--page);
}

.brt-15__card:hover .brt-15__shot,
.brt-15__card:focus-within .brt-15__shot {
  filter: invert(1) grayscale(1);
}

.brt-15__card:hover .brt-15__spec,
.brt-15__card:focus-within .brt-15__spec {
  color: var(--page);
}

.brt-15__frame {
  position: relative;
  margin: 0 0 .9rem;
  border: var(--bw) solid currentColor;
  background: var(--page);
}

.brt-15__shot {
  display: block;
  inline-size: 100%;
  aspect-ratio: 1;
  object-fit: cover;
}

.brt-15__card[data-stock="out"] .brt-15__frame::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(45deg, transparent 0 9px, currentColor 9px 11px);
}

.brt-15__name {
  margin: 0;
  font-size: 1.15rem;
  font-weight: 700;
  line-height: 1.25;
}

.brt-15__name a {
  color: inherit;
  text-decoration: underline;
  text-decoration-thickness: 2px;
  text-underline-offset: 3px;
}

.brt-15__name a::after {
  content: '';
  position: absolute;
  inset: 0;
}

.brt-15__name a:focus-visible {
  outline: none;
}

.brt-15__card:focus-within .brt-15__name a::after {
  outline: 3px solid currentColor;
  outline-offset: -6px;
}

.brt-15__spec {
  margin: .35rem 0 0;
  font-size: .98rem;
  line-height: 1.45;
  color: var(--muted);
}

.brt-15__price {
  margin: 1.75rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  align-items: center;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  font-size: 1.3rem;
  font-weight: 700;
}

.brt-15__out {
  padding: .15rem .4rem;
  border: 2px solid currentColor;
  font-family: ui-monospace,Menlo,monospace;
  font-size: .72rem;
  letter-spacing: .12em;
}

.brt-15__foot {
  margin: 2rem 0 0;
  padding-block-start: .75rem;
  border-block-start: var(--bw) solid var(--edge);
  font-size: .95rem;
  color: var(--muted);
}

.brt-15:has(#brt-15-dark:checked) {
  --page: #000000;
  --panel: #0a0a0a;
  --ink: #ffffff;
  --muted: #c2c2c2;
  --edge: #ffffff;
  --sh: #ffffff;
}

.brt-15:has(#brt-15-dark:checked) .brt-15__moon {
  display: none;
}

.brt-15:has(#brt-15-dark:checked) .brt-15__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-15:not(:has(#brt-15-dark:checked)) {
    --page: #000000;
    --panel: #0a0a0a;
    --ink: #ffffff;
    --muted: #c2c2c2;
    --edge: #ffffff;
    --sh: #ffffff;
  }

  .brt-15:not(:has(#brt-15-dark:checked)) .brt-15__moon {
    display: none;
  }

  .brt-15:not(:has(#brt-15-dark:checked)) .brt-15__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-15 *,
    .brt-15 *::before,
    .brt-15 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-15__card,
    .brt-15__frame,
    .brt-15__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .brt-15__card:hover {
    background: Canvas;
    color: CanvasText;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-15__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
