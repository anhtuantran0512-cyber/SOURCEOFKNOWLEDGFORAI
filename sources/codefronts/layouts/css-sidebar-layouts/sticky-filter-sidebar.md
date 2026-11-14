---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/sticky-filter-sidebar/"
title: "Responsive E-Commerce Product Filter Sidebar with Native Accordion Menu"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "A storefront filter rail built entirely on native <details>/<summary> — every accordion section is keyboard-operable, screen-reader-announced, and crawlable…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive E-Commerce Product Filter Sidebar with Native Accordion Menu
Source: https://codefronts.com/layouts/css-sidebar-layouts/sticky-filter-sidebar/

A storefront filter rail built entirely on native <details>/<summary> — every accordion section is keyboard-operable, screen-reader-announced, and crawlable with ZERO script. The panels animate open with the brand-new interpolate-size / height:auto transition, the chevrons rotate on [open], and the whole rail is position:sticky so filters ride along the product grid.
## HTML
```html
<section class="sbl-03">
  <aside class="sbl-03__rail" aria-label="Product filters">
    <h2 class="sbl-03__title">Filters <button class="sbl-03__clear" type="button">Clear all</button></h2>
    <details class="sbl-03__group" name="filters" open>
      <summary>Category <span class="sbl-03__count">128</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></summary>
      <div class="sbl-03__body">
        <label><input type="checkbox" checked>Sneakers <span>64</span></label>
        <label><input type="checkbox">Running <span>38</span></label>
        <label><input type="checkbox">Trail <span>26</span></label>
      </div>
    </details>
    <details class="sbl-03__group" name="filters">
      <summary>Price <span class="sbl-03__count">$40–220</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></summary>
      <div class="sbl-03__body">
        <input class="sbl-03__range" type="range" min="40" max="220" value="120" aria-label="Maximum price">
        <label><input type="checkbox">Under $80 <span>31</span></label>
        <label><input type="checkbox">$80–$150 <span>57</span></label>
      </div>
    </details>
    <details class="sbl-03__group" name="filters">
      <summary>Brand <span class="sbl-03__count">12</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></summary>
      <div class="sbl-03__body">
        <label><input type="checkbox">Veloce <span>44</span></label>
        <label><input type="checkbox">Northpeak <span>29</span></label>
        <label><input type="checkbox">Atlasform <span>18</span></label>
      </div>
    </details>
  </aside>
  <main class="sbl-03__grid" aria-label="Products">
    <article class="sbl-03__product"><div class="sbl-03__ph"></div><h3>Veloce Cloudrunner</h3><p>$128</p></article>
    <article class="sbl-03__product"><div class="sbl-03__ph"></div><h3>Northpeak Trail 2</h3><p>$156</p></article>
    <article class="sbl-03__product"><div class="sbl-03__ph"></div><h3>Atlasform Daily</h3><p>$92</p></article>
    <article class="sbl-03__product"><div class="sbl-03__ph"></div><h3>Veloce Street LX</h3><p>$110</p></article>
  </main>
</section>
```
## CSS
```css
.sbl-03,
.sbl-03 *,
.sbl-03 *::before,
.sbl-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-03 {
  --ink: oklch(0.26 0.015 265);
  --mut: oklch(0.55 0.012 265);
  --line: oklch(0.91 0.006 265);
  --accent: oklch(0.55 0.19 25);
  interpolate-size: allow-keywords;
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 28px;
  height: 100vh;
  height: 100dvh;
  overflow-y: auto;
  padding: 28px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.98 0.003 100);
  color: var(--ink);
}

.sbl-03__rail {
  position: sticky;
  top: 0;
  align-self: start;
  max-height: calc(100dvh - 56px);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.sbl-03__title {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font: 700 15px/1 system-ui,sans-serif;
  padding: 4px 2px 14px;
}

.sbl-03__clear {
  border: none;
  background: none;
  color: var(--accent);
  font: 500 12.5px/1 system-ui,sans-serif;
  cursor: pointer;
  text-decoration: underline;
  text-underline-offset: 3px;
}

.sbl-03__clear:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 4px;
}

.sbl-03__group {
  border-top: 1px solid var(--line);
}

.sbl-03__group summary {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 14px 2px;
  font: 600 13.5px/1 system-ui,sans-serif;
  cursor: pointer;
  list-style: none;
}

.sbl-03__group summary::-webkit-details-marker {
  display: none;
}

.sbl-03__group summary:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 6px;
}

.sbl-03__count {
  margin-left: auto;
  font: 500 11.5px/1 system-ui,sans-serif;
  color: var(--mut);
}

.sbl-03__group summary svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: var(--mut);
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: rotate .25s ease;
}

.sbl-03__group[open] summary svg {
  rotate: 180deg;
}

.sbl-03__group::details-content {
  height: 0;
  overflow: clip;
  transition: height .3s ease,content-visibility .3s allow-discrete;
}

.sbl-03__group[open]::details-content {
  height: auto;
}

.sbl-03__body {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 2px 2px 16px;
}

.sbl-03__body label {
  display: flex;
  align-items: center;
  gap: 9px;
  font: 400 13.5px/1 system-ui,sans-serif;
  cursor: pointer;
}

.sbl-03__body label span {
  margin-left: auto;
  color: var(--mut);
  font-size: 11.5px;
}

.sbl-03__body input[type="checkbox"] {
  width: 16px;
  height: 16px;
  accent-color: var(--accent);
}

.sbl-03__range {
  width: 100%;
  accent-color: var(--accent);
}

.sbl-03__body input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-03__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(160px,1fr));
  gap: 18px;
  align-content: start;
}

.sbl-03__product h3 {
  font: 600 13.5px/1.3 system-ui,sans-serif;
  margin-top: 10px;
}

.sbl-03__product p {
  font: 500 13px/1 system-ui,sans-serif;
  color: var(--mut);
  margin-top: 4px;
}

.sbl-03__ph {
  aspect-ratio: 1;
  border-radius: 12px;
  background: linear-gradient(135deg,oklch(0.93 0.01 265),oklch(0.88 0.015 265));
}

@media (prefers-reduced-motion: reduce) {
  .sbl-03__group::details-content,
    .sbl-03__group summary svg {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — native <details name="filters"> gives an exclusive, accessible accordion; ::details-content + interpolate-size animates height:auto. */
```
