---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/subgrid-card/"
title: "Subgrid Card"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The card-alignment problem, finally solved: titles of different lengths, descriptions of different depths — yet every title baseline, every description block…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Subgrid Card
Source: https://codefronts.com/layouts/css-grid-layouts/subgrid-card/

The card-alignment problem, finally solved: titles of different lengths, descriptions of different depths — yet every title baseline, every description block and every button aligns PERFECTLY across cards, because each card inherits the parent's row tracks with grid-template-rows: subgrid. The demo shows misaligned vs aligned side by side.
## HTML
```html
<section class="cgl-15" aria-label="Subgrid card alignment demo">
  <div class="cgl-15__grid">
    <article class="cgl-15__card">
      <p class="cgl-15__eyebrow">Starter</p>
      <h4>Ship your first project</h4>
      <p class="cgl-15__desc">Every card spans the same four parent rows.</p>
      <a href="#0" class="cgl-15__btn">Choose Starter</a>
    </article>
    <article class="cgl-15__card cgl-15__card--hot">
      <p class="cgl-15__eyebrow">Studio · most popular</p>
      <h4>A much longer title that wraps onto two full lines</h4>
      <p class="cgl-15__desc">The title track grows for the tallest title — and every sibling's title track grows with it. That is subgrid.</p>
      <a href="#0" class="cgl-15__btn">Choose Studio</a>
    </article>
    <article class="cgl-15__card">
      <p class="cgl-15__eyebrow">Agency</p>
      <h4>Scale it</h4>
      <p class="cgl-15__desc">Short title, short copy — the button still lands on the shared final track, perfectly level with its neighbours.</p>
      <a href="#0" class="cgl-15__btn">Choose Agency</a>
    </article>
  </div>
</section>
```
## CSS
```css
.cgl-15,
.cgl-15 *,
.cgl-15 *::before,
.cgl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-15 {
  width: 100%;
  min-height: 100vh;
  --mint: oklch(0.85 0.12 165);
  --ink: oklch(0.24 0.03 180);
  --bg: oklch(0.2 0.03 175);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.4rem;
}

.cgl-15 .cgl-15__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(190px,100%),1fr));
  grid-auto-rows: auto;
  gap: 14px;
}

.cgl-15 .cgl-15__card {
  grid-row: span 4;
  display: grid;
  grid-template-rows: subgrid;
  row-gap: .6rem;
  background: oklch(0.25 0.03 175);
  border: 1px solid color-mix(in oklab,var(--mint) 25%,transparent);
  border-radius: 16px;
  padding: 1.2rem;
}

.cgl-15 .cgl-15__card--hot {
  background: color-mix(in oklab,var(--mint) 14%,oklch(0.25 0.03 175));
  border-color: var(--mint);
}

.cgl-15 .cgl-15__eyebrow {
  font-size: .66rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--mint);
}

.cgl-15 h4 {
  font-size: 1.05rem;
  line-height: 1.3;
  color: white;
  text-wrap: balance;
}

.cgl-15 .cgl-15__desc {
  font-size: .8rem;
  line-height: 1.6;
  color: oklch(0.75 0.02 175);
}

.cgl-15 .cgl-15__btn {
  align-self: end;
  justify-self: start;
  font-size: .82rem;
  font-weight: 600;
  color: var(--ink);
  background: var(--mint);
  text-decoration: none;
  padding: .55rem 1rem;
  border-radius: 999px;
  min-block-size: 2.4rem;
  display: inline-grid;
  align-items: center;
}

.cgl-15 .cgl-15__btn:hover {
  background: color-mix(in oklab,var(--mint) 85%,white);
}

.cgl-15 .cgl-15__btn:focus-visible {
  outline: 2px solid var(--mint);
  outline-offset: 3px;
}

@supports not (grid-template-rows: subgrid) {
  .cgl-15 .cgl-15__card {
    grid-template-rows: auto auto 1fr auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid-template-rows: subgrid makes all cards share the parent's row tracks, aligning every section across cards. */
```
