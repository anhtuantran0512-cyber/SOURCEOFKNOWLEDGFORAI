---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/asymmetric-splash/"
title: "Asymmetric Splash"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A hero section with real art direction: color blocks, an oversized display numeral and the headline all occupy overlapping grid regions at different…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Asymmetric Splash
Source: https://codefronts.com/layouts/css-grid-layouts/asymmetric-splash/

A hero section with real art direction: color blocks, an oversized display numeral and the headline all occupy overlapping grid regions at different z-layers, building the off-balance tension of poster design. Negative-space asymmetry from placement arithmetic — not from a designer's PNG export.
## HTML
```html
<section class="cgl-22" aria-label="Asymmetric splash hero demo">
  <div class="cgl-22__stage">
    <div class="cgl-22__slab" aria-hidden="true"></div>
    <div class="cgl-22__panel" aria-hidden="true"></div>
    <span class="cgl-22__numeral" aria-hidden="true">22</span>
    <h2 class="cgl-22__headline">Balance is<br>overrated</h2>
    <p class="cgl-22__caption">Four layers · one grid · zero absolute positioning</p>
  </div>
</section>
```
## CSS
```css
.cgl-22,
.cgl-22 *,
.cgl-22 *::before,
.cgl-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-22 {
  width: 100%;
  min-height: 100vh;
  --crimson: oklch(0.5 0.2 20);
  --cream: oklch(0.95 0.02 85);
  --ink: oklch(0.2 0.02 20);
  font-family: system-ui,sans-serif;
  background: var(--ink);
  padding: 1.6rem;
}

.cgl-22 .cgl-22__stage {
  display: grid;
  grid-template-columns: repeat(10,1fr);
  grid-template-rows: repeat(6,minmax(34px,auto));
  max-inline-size: 640px;
  margin-inline: auto;
  overflow: hidden;
}

.cgl-22 .cgl-22__slab {
  grid-column: 1/6;
  grid-row: 1/5;
  z-index: 1;
  background: var(--crimson);
}

.cgl-22 .cgl-22__panel {
  grid-column: 4/11;
  grid-row: 2/7;
  z-index: 2;
  background: var(--cream);
}

.cgl-22 .cgl-22__numeral {
  grid-column: 7/11;
  grid-row: 1/4;
  z-index: 3;
  font-size: clamp(5rem,16vw,9rem);
  font-weight: 900;
  line-height: .75;
  color: transparent;
  -webkit-text-stroke: 2px var(--crimson);
  justify-self: end;
  translate: 6% -12%;
}

.cgl-22 .cgl-22__headline {
  grid-column: 2/9;
  grid-row: 3/5;
  z-index: 4;
  align-self: center;
  font-size: clamp(1.8rem,5.5vw,3rem);
  line-height: 1.02;
  font-weight: 800;
  letter-spacing: -.02em;
  color: var(--ink);
}

.cgl-22 .cgl-22__caption {
  grid-column: 4/11;
  grid-row: 6/7;
  z-index: 4;
  align-self: end;
  font-family: ui-monospace,Menlo,monospace;
  font-size: .66rem;
  letter-spacing: .1em;
  color: color-mix(in oklab,var(--ink) 65%,var(--cream));
  padding: .8rem;
}

@media (max-width: 520px) {
  .cgl-22 .cgl-22__numeral {
    grid-column: 6/11;
  }

  .cgl-22 .cgl-22__headline {
    grid-column: 2/10;
  }
}
```

## JavaScript
```js
/* No JavaScript — four grid regions overlap at explicit z-layers; the outlined numeral bleeds off-canvas behind overflow:hidden. */
```
