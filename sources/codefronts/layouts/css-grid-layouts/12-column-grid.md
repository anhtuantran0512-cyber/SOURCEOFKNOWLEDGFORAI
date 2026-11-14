---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/12-column-grid/"
title: "12-Column Grid"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A framework-free 12-column system in eight lines of CSS — with the column overlay every design tool shows, rendered live behind real content so students can…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 12-Column Grid
Source: https://codefronts.com/layouts/css-grid-layouts/12-column-grid/

A framework-free 12-column system in eight lines of CSS — with the column overlay every design tool shows, rendered live behind real content so students can SEE spans land on tracks. Utility classes .col-1 through .col-12, a gap variable, and none of Bootstrap's 12,000 lines.
## HTML
```html
<section class="cgl-08" aria-label="12-column grid system demo">
  <div class="cgl-08__frame">
    <div class="cgl-08__grid">
      <div class="cgl-08__block cgl-08-col-12"><code>span 12</code> — hero, nav, footer</div>
      <div class="cgl-08__block cgl-08-col-8"><code>span 8</code> — article</div>
      <div class="cgl-08__block cgl-08-col-4"><code>span 4</code> — sidebar</div>
      <div class="cgl-08__block cgl-08-col-4"><code>span 4</code></div>
      <div class="cgl-08__block cgl-08-col-4"><code>span 4</code></div>
      <div class="cgl-08__block cgl-08-col-4"><code>span 4</code></div>
      <div class="cgl-08__block cgl-08-col-6"><code>span 6</code></div>
      <div class="cgl-08__block cgl-08-col-3"><code>span 3</code></div>
      <div class="cgl-08__block cgl-08-col-3"><code>span 3</code></div>
    </div>
  </div>
</section>
```
## CSS
```css
.cgl-08,
.cgl-08 *,
.cgl-08 *::before,
.cgl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-08 {
  width: 100%;
  min-height: 100vh;
  --gap: 12px;
  --indigo: oklch(0.5 0.19 280);
  --paper: oklch(0.97 0.008 280);
  --overlay: oklch(0.65 0.24 350/.14);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  background: var(--paper);
  padding: 1.4rem;
}

.cgl-08 .cgl-08__frame {
  position: relative;
  border: 1px solid oklch(0.88 0.02 280);
  border-radius: 12px;
  padding: var(--gap);
  background: repeating-linear-gradient(90deg,var(--overlay) 0 calc((100% + var(--gap))/12 - var(--gap)),transparent calc((100% + var(--gap))/12 - var(--gap)) calc((100% + var(--gap))/12));
  background-origin: content-box;
  background-clip: content-box;
}

.cgl-08 .cgl-08__grid {
  display: grid;
  grid-template-columns: repeat(12,minmax(0,1fr));
  gap: var(--gap);
}

.cgl-08 .cgl-08-col-3 {
  grid-column: span 3;
}

.cgl-08 .cgl-08-col-4 {
  grid-column: span 4;
}

.cgl-08 .cgl-08-col-6 {
  grid-column: span 6;
}

.cgl-08 .cgl-08-col-8 {
  grid-column: span 8;
}

.cgl-08 .cgl-08-col-12 {
  grid-column: span 12;
}

.cgl-08 .cgl-08__block {
  background: color-mix(in oklab,var(--indigo) 8%,white);
  border: 1px solid color-mix(in oklab,var(--indigo) 35%,white);
  border-radius: 8px;
  padding: .8rem;
  min-block-size: 56px;
  display: grid;
  align-content: center;
  font-size: .72rem;
  color: oklch(0.35 0.1 280);
}

.cgl-08 .cgl-08__block code {
  font-weight: 700;
  color: var(--indigo);
}

@media (max-width: 560px) {
  .cgl-08 .cgl-08-col-3,
    .cgl-08 .cgl-08-col-4 {
    grid-column: span 6;
  }

  .cgl-08 .cgl-08-col-6,
    .cgl-08 .cgl-08-col-8 {
    grid-column: span 12;
  }
}
```

## JavaScript
```js
/* No JavaScript — repeat(12, minmax(0,1fr)) + span utilities; a calc()-based gradient renders the design-tool column overlay. */
```
