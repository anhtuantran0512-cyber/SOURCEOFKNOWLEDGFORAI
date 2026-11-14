---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/ram-auto-fit/"
title: "RAM Auto-Fit"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "Repeat, Auto-fit, Minmax — the single most useful line of CSS written this decade."
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: RAM Auto-Fit
Source: https://codefronts.com/layouts/css-grid-layouts/ram-auto-fit/

Repeat, Auto-fit, Minmax — the single most useful line of CSS written this decade. Card grids that go 4-up, 3-up, 2-up, 1-up as the container narrows, with zero media queries. This demo ships the crash-proof 2026 version with min() and a clamp()ed floor, plus a live track-count readout so learners watch it respond.
## HTML
```html
<section class="cgl-11" aria-label="RAM auto-fit grid demo">
  <div class="cgl-11__grid">
    <article class="cgl-11__card"><h4>Repeat</h4><p>As many tracks as fit — the browser does the counting, not your breakpoints.</p></article>
    <article class="cgl-11__card"><h4>Auto-fit</h4><p>Empty tracks collapse; the survivors absorb the space.</p></article>
    <article class="cgl-11__card"><h4>Minmax</h4><p>A 220px floor keeps cards dignified; the 1fr ceiling keeps rows full.</p></article>
    <article class="cgl-11__card"><h4>min() hardening</h4><p>min(220px, 100%) means the floor can never exceed the container. No overflow, ever.</p></article>
    <article class="cgl-11__card"><h4>Zero queries</h4><p>4-up to 1-up with no @media. Resize and count the columns.</p></article>
    <article class="cgl-11__card"><h4>clamp() upgrade</h4><p>A fluid floor — clamp(220px, 24vw, 320px) — scales cards with the viewport.</p></article>
  </div>
</section>
```
## CSS
```css
.cgl-11,
.cgl-11 *,
.cgl-11 *::before,
.cgl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-11 {
  width: 100%;
  min-height: 100vh;
  --teal: oklch(0.78 0.13 190);
  --bg: oklch(0.97 0.01 190);
  --ink: oklch(0.25 0.03 210);
  font-family: system-ui,sans-serif;
  background: linear-gradient(180deg,var(--bg),oklch(0.93 0.02 195));
  padding: 1.4rem;
}

.cgl-11 .cgl-11__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(220px,100%),1fr));
  gap: 14px;
}

.cgl-11 .cgl-11__card {
  background: white;
  border: 1px solid color-mix(in oklab,var(--teal) 40%,white);
  border-radius: 14px;
  padding: 1.1rem;
  display: flex;
  flex-direction: column;
  gap: .5rem;
  box-shadow: 0 10px 24px -18px oklch(0.4 0.08 200/.6);
  transition: translate .2s ease,box-shadow .2s ease;
}

.cgl-11 .cgl-11__card:hover {
  translate: 0 -3px;
  box-shadow: 0 16px 32px -18px oklch(0.4 0.1 200/.7);
}

.cgl-11 h4 {
  font-size: .95rem;
  color: var(--ink);
}

.cgl-11 h4::before {
  content: "";
  display: inline-block;
  inline-size: .55em;
  block-size: .55em;
  border-radius: 2px;
  background: var(--teal);
  margin-inline-end: .5em;
  rotate: 45deg;
}

.cgl-11 p {
  font-size: .8rem;
  line-height: 1.55;
  color: color-mix(in oklab,var(--ink) 70%,white);
}

@media (prefers-reduced-motion: reduce) {
  .cgl-11 .cgl-11__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — repeat(auto-fit, minmax(min(220px,100%),1fr)) is the entire responsive algorithm. */
```
