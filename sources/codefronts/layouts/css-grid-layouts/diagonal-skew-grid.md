---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/diagonal-skew-grid/"
title: "Diagonal Skew Grid"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "Sharp diagonal section transitions — the agency-site signature — done the maintainable way: the section skews, its children counter-skew, and the content…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diagonal Skew Grid
Source: https://codefronts.com/layouts/css-grid-layouts/diagonal-skew-grid/

Sharp diagonal section transitions — the agency-site signature — done the maintainable way: the section skews, its children counter-skew, and the content inside is an ordinary grid that never knows it's tilted. No SVG dividers, no clip-path seams that misalign at odd viewport widths.
## HTML
```html
<section class="cgl-21" aria-label="Diagonal skew grid demo">
  <div class="cgl-21__intro"><p>Ordinary flow above the band.</p></div>
  <div class="cgl-21__band">
    <div class="cgl-21__inner">
      <h3>Cut at 4 degrees</h3>
      <div class="cgl-21__stats">
        <article><strong>−4deg</strong><span>section skew</span></article>
        <article><strong>+4deg</strong><span>child counter-skew</span></article>
        <article><strong>tan(4°)</strong><span>overlap math</span></article>
      </div>
    </div>
  </div>
  <div class="cgl-21__outro"><p>Ordinary flow below. The band's edges are transforms — no SVG dividers, no seams.</p></div>
</section>
```
## CSS
```css
.cgl-21,
.cgl-21 *,
.cgl-21 *::before,
.cgl-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-21 {
  width: 100%;
  min-height: 100vh;
  --angle: 4deg;
  --electric: oklch(0.8 0.16 195);
  --ink: oklch(0.16 0.02 240);
  font-family: system-ui,sans-serif;
  background: oklch(0.96 0.008 220);
  overflow: hidden;
}

.cgl-21 .cgl-21__intro,
.cgl-21 .cgl-21__outro {
  padding: 2.2rem 1.6rem;
  color: oklch(0.4 0.03 230);
}

.cgl-21 .cgl-21__intro p,
.cgl-21 .cgl-21__outro p {
  font-size: .85rem;
}

.cgl-21 .cgl-21__band {
  transform: skewY(calc(var(--angle)*-1));
  background: linear-gradient(110deg,var(--ink),oklch(0.22 0.05 220));
  padding-block: 2.6rem;
  margin-block: 1rem;
}

.cgl-21 .cgl-21__band>* {
  transform: skewY(var(--angle));
}

.cgl-21 .cgl-21__inner {
  padding-inline: 1.6rem;
  max-inline-size: 640px;
  margin-inline: auto;
}

.cgl-21 h3 {
  color: var(--electric);
  font-size: clamp(1.3rem,3.5vw,1.8rem);
  margin-block-end: 1.2rem;
}

.cgl-21 .cgl-21__stats {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(150px,100%),1fr));
  gap: 12px;
}

.cgl-21 .cgl-21__stats article {
  background: oklch(1 0 0/.06);
  border: 1px solid color-mix(in oklab,var(--electric) 30%,transparent);
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: .3rem;
}

.cgl-21 .cgl-21__stats strong {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 1.2rem;
  color: var(--electric);
}

.cgl-21 .cgl-21__stats span {
  font-size: .72rem;
  color: oklch(0.7 0.02 220);
}
```

## JavaScript
```js
/* No JavaScript — skewY on the band, inverse skewY on its children; the inner grid renders level inside the tilt. */
```
