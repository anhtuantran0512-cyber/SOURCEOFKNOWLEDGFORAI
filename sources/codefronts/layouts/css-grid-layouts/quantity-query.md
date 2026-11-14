---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/quantity-query/"
title: "Quantity Query"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A grid that restyles itself based on HOW MANY children it has — pure CSS, via :has() and child-counting selectors."
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Quantity Query
Source: https://codefronts.com/layouts/css-grid-layouts/quantity-query/

A grid that restyles itself based on HOW MANY children it has — pure CSS, via :has() and child-counting selectors. Three tags render as roomy feature cards; six or more automatically compact into a dense chip wall. The CMS-proof layout: editors add items, the design responds, nobody files a ticket.
## HTML
```html
<section class="cgl-12" aria-label="Quantity query demo">
  <p class="cgl-12__label">3 items → feature cards</p>
  <ul class="cgl-12__grid">
    <li><strong>Design</strong><span>Roomy, confident, editorial.</span></li>
    <li><strong>Engineering</strong><span>Same class, same stylesheet.</span></li>
    <li><strong>Research</strong><span>No modifiers, no JS.</span></li>
  </ul>
  <p class="cgl-12__label">8 items → the grid self-compacts via :has(> :nth-child(5))</p>
  <ul class="cgl-12__grid">
    <li><strong>Design</strong></li><li><strong>Engineering</strong></li><li><strong>Research</strong></li><li><strong>Ops</strong></li>
    <li><strong>Data</strong></li><li><strong>Support</strong></li><li><strong>Legal</strong></li><li><strong>Growth</strong></li>
  </ul>
</section>
```
## CSS
```css
.cgl-12,
.cgl-12 *,
.cgl-12 *::before,
.cgl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-12 {
  width: 100%;
  min-height: 100vh;
  --amber: oklch(0.78 0.15 75);
  --coal: oklch(0.2 0.01 75);
  --card: oklch(0.25 0.015 75);
  font-family: system-ui,sans-serif;
  background: var(--coal);
  padding: 1.4rem;
  display: flex;
  flex-direction: column;
  gap: .8rem;
}

.cgl-12 .cgl-12__label {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .68rem;
  color: color-mix(in oklab,var(--amber) 70%,white);
  letter-spacing: .08em;
}

.cgl-12 .cgl-12__grid {
  --floor: 200px;
  --pad: 1.1rem;
  --fs: .95rem;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(var(--floor),100%),1fr));
  gap: 12px;
  margin-block-end: .6rem;
}

.cgl-12 .cgl-12__grid:has(>:nth-child(5)) {
  --floor: 104px;
  --pad: .6rem;
  --fs: .78rem;
  gap: 8px;
}

.cgl-12 .cgl-12__grid li {
  background: var(--card);
  border: 1px solid color-mix(in oklab,var(--amber) 25%,var(--card));
  border-radius: 12px;
  padding: var(--pad);
  display: flex;
  flex-direction: column;
  gap: .4rem;
}

.cgl-12 .cgl-12__grid li strong {
  font-size: var(--fs);
  color: var(--amber);
}

.cgl-12 .cgl-12__grid li span {
  font-size: .78rem;
  line-height: 1.5;
  color: oklch(0.75 0.02 75);
}

.cgl-12 .cgl-12__grid:has(>:nth-child(5)) li {
  align-items: center;
  text-align: center;
  justify-content: center;
}
/* Legacy (pre-:has) equivalent: li:first-child:nth-last-child(n+5), li:first-child:nth-last-child(n+5) ~ li { ... } */
```

## JavaScript
```js
/* No JavaScript — .grid:has(> :nth-child(5)) detects the item count and flips custom properties for the compact state. */
```
