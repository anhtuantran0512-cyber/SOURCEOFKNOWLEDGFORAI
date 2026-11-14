---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/swiss-grid-department-store/"
title: "Department Store Mega Menu Grid"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "The dense case: many departments across four columns, each with its own sub-links."
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Department Store Mega Menu Grid
Source: https://codefronts.com/navigation/css-mega-menus/swiss-grid-department-store/

The dense case: many departments across four columns, each with its own sub-links. This is where column layout and scannability are genuinely hard, and where the shared-panel approach from demo 12 starts to earn its place. A strict typographic grid, ruled columns and a deliberate ceiling on how much any one column may hold.
## HTML
```html
<section class="mm-18" aria-labelledby="mm-18-title">
  <h2 class="mm-18__sr" id="mm-18-title">Sable and Vale</h2>

  <div class="mm-18__theme">
    <input class="mm-18__theme-input" type="checkbox" id="mm-18-theme">
    <label class="mm-18__theme-label" for="mm-18-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-18__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-18__header">
    <div class="mm-18__strip">
      <span>Free click and collect from 68 stores</span>
      <a href="#mm-18-title">Store finder</a>
      <a href="#mm-18-title">Account</a>
      <a href="#mm-18-title">Bag (0)</a>
    </div>

    <div class="mm-18__bar">
      <a class="mm-18__brand" href="#mm-18-title">SABLE &amp; VALE</a>

      <nav class="mm-18__nav" aria-label="Primary">
        <ul class="mm-18__list">
          <li class="mm-18__item">
            <button class="mm-18__trigger" type="button" id="mm-18-trigger-home" aria-expanded="false" aria-controls="mm-18-panel-home">Home</button>
            <div class="mm-18__panel" id="mm-18-panel-home" aria-labelledby="mm-18-trigger-home">
              <div class="mm-18__panel-inner">
                <section class="mm-18__col" aria-labelledby="mm-18-h-kitchen">
                  <h3 class="mm-18__col-head" id="mm-18-h-kitchen">Kitchen &amp; dining</h3>
                  <ul class="mm-18__links">
                    <li><a href="#mm-18-title">Cookware</a></li><li><a href="#mm-18-title">Knives</a></li><li><a href="#mm-18-title">Tableware</a></li><li><a href="#mm-18-title">Glassware</a></li><li><a href="#mm-18-title">Small appliances</a></li><li><a href="#mm-18-title">Storage</a></li><li><a href="#mm-18-title">Table linen</a></li>
                  </ul>
                </section>
                <section class="mm-18__col" aria-labelledby="mm-18-h-bed">
                  <h3 class="mm-18__col-head" id="mm-18-h-bed">Bed &amp; bath</h3>
                  <ul class="mm-18__links">
                    <li><a href="#mm-18-title">Duvets</a></li><li><a href="#mm-18-title">Bed linen</a></li><li><a href="#mm-18-title">Pillows</a></li><li><a href="#mm-18-title">Towels</a></li><li><a href="#mm-18-title">Bath mats</a></li><li><a href="#mm-18-title">Robes</a></li>
                  </ul>
                </section>
                <section class="mm-18__col" aria-labelledby="mm-18-h-furniture">
                  <h3 class="mm-18__col-head" id="mm-18-h-furniture">Furniture</h3>
                  <ul class="mm-18__links">
                    <li><a href="#mm-18-title">Sofas</a></li><li><a href="#mm-18-title">Dining tables</a></li><li><a href="#mm-18-title">Chairs</a></li><li><a href="#mm-18-title">Storage units</a></li><li><a href="#mm-18-title">Desks</a></li>
                  </ul>
                </section>
                <section class="mm-18__col" aria-labelledby="mm-18-h-decor">
                  <h3 class="mm-18__col-head" id="mm-18-h-decor">Decoration</h3>
                  <ul class="mm-18__links">
                    <li><a href="#mm-18-title">Lighting</a></li><li><a href="#mm-18-title">Rugs</a></li><li><a href="#mm-18-title">Mirrors</a></li><li><a href="#mm-18-title">Candles</a></li><li><a href="#mm-18-title">Frames</a></li><li><a href="#mm-18-title">Vases</a></li>
                  </ul>
                </section>
              </div>
              <div class="mm-18__foot">
                <a href="#mm-18-title">All home departments</a>
                <a href="#mm-18-title">Delivery and assembly</a>
                <a href="#mm-18-title">Returns</a>
                <a href="#mm-18-title">Gift registry</a>
              </div>
            </div>
          </li>

          <li class="mm-18__item">
            <button class="mm-18__trigger" type="button" id="mm-18-trigger-women" aria-expanded="false" aria-controls="mm-18-panel-women">Women</button>
            <div class="mm-18__panel" id="mm-18-panel-women" aria-labelledby="mm-18-trigger-women">
              <div class="mm-18__panel-inner">
                <section class="mm-18__col" aria-labelledby="mm-18-h-cloth">
                  <h3 class="mm-18__col-head" id="mm-18-h-cloth">Clothing</h3>
                  <ul class="mm-18__links"><li><a href="#mm-18-title">Coats</a></li><li><a href="#mm-18-title">Knitwear</a></li><li><a href="#mm-18-title">Dresses</a></li><li><a href="#mm-18-title">Trousers</a></li><li><a href="#mm-18-title">Denim</a></li></ul>
                </section>
                <section class="mm-18__col" aria-labelledby="mm-18-h-shoes">
                  <h3 class="mm-18__col-head" id="mm-18-h-shoes">Shoes</h3>
                  <ul class="mm-18__links"><li><a href="#mm-18-title">Boots</a></li><li><a href="#mm-18-title">Flats</a></li><li><a href="#mm-18-title">Trainers</a></li></ul>
                </section>
                <section class="mm-18__col" aria-labelledby="mm-18-h-acc">
                  <h3 class="mm-18__col-head" id="mm-18-h-acc">Accessories</h3>
                  <ul class="mm-18__links"><li><a href="#mm-18-title">Bags</a></li><li><a href="#mm-18-title">Scarves</a></li><li><a href="#mm-18-title">Jewellery</a></li><li><a href="#mm-18-title">Belts</a></li></ul>
                </section>
                <section class="mm-18__col" aria-labelledby="mm-18-h-brands">
                  <h3 class="mm-18__col-head" id="mm-18-h-brands">Brands</h3>
                  <ul class="mm-18__links"><li><a href="#mm-18-title">Meridian</a></li><li><a href="#mm-18-title">Fern</a></li><li><a href="#mm-18-title">Orbit</a></li><li><a href="#mm-18-title">Quill</a></li></ul>
                </section>
              </div>
              <div class="mm-18__foot"><a href="#mm-18-title">New in</a><a href="#mm-18-title">Sale</a><a href="#mm-18-title">Size guide</a></div>
            </div>
          </li>

          <li class="mm-18__item"><a class="mm-18__plain" href="#mm-18-title">Men</a></li>
          <li class="mm-18__item"><a class="mm-18__plain" href="#mm-18-title">Beauty</a></li>
          <li class="mm-18__item"><a class="mm-18__plain mm-18__plain--sale" href="#mm-18-title">Sale</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="mm-18__page">
    <div class="mm-18__editorial">
      <p class="mm-18__ed-k">Autumn edit</p>
      <h1 class="mm-18__ed-h">Sixty years of the Sable &amp; Vale winter table.</h1>
      <a class="mm-18__ed-cta" href="#mm-18-title">Shop the collection</a>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-18 {
  --mm-18-bg: #ffffff;
  --mm-18-surf: #ffffff;
  --mm-18-line: #111111;
  --mm-18-soft: #e8e8e8;
  --mm-18-ink: #111111;
  --mm-18-mut: #666666;
  --mm-18-acc: #e10600;
  --mm-18-acc: oklch(56% 0.24 28);
  --mm-18-rule: 1px;
  --mm-18-gap-x: clamp(1.25rem, 4vw, 3rem);
  --mm-18-gap-y: 0.35rem;
  --mm-18-font-display: "Archivo Narrow", "Roboto Condensed", "Helvetica Neue", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-18-bg);
  color: var(--mm-18-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.mm-18 *,
.mm-18 *::before,
.mm-18 *::after {
  box-sizing: border-box;
}

.mm-18 :focus-visible {
  outline: 2px solid var(--mm-18-acc);
  outline-offset: 2px;
}

.mm-18__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.mm-18:has(.mm-18__theme-input:checked) {
  --mm-18-bg: #0a0a0a;
  --mm-18-surf: #101010;
  --mm-18-line: #f0f0f0;
  --mm-18-soft: #242424;
  --mm-18-ink: #f0f0f0;
  --mm-18-mut: #9a9a9a;
  --mm-18-acc: #ff4d3d;
  --mm-18-acc: oklch(70% 0.19 32);
}

@media (prefers-color-scheme: dark) {
  .mm-18 {
    --mm-18-bg: #0a0a0a;
    --mm-18-surf: #101010;
    --mm-18-line: #f0f0f0;
    --mm-18-soft: #242424;
    --mm-18-ink: #f0f0f0;
    --mm-18-mut: #9a9a9a;
    --mm-18-acc: #ff4d3d;
    --mm-18-acc: oklch(70% 0.19 32);
  }

  .mm-18:has(.mm-18__theme-input:checked) {
    --mm-18-bg: #ffffff;
    --mm-18-surf: #ffffff;
    --mm-18-line: #111111;
    --mm-18-soft: #e8e8e8;
    --mm-18-ink: #111111;
    --mm-18-mut: #666666;
    --mm-18-acc: #e10600;
    --mm-18-acc: oklch(56% 0.24 28);
  }
}

@media (prefers-color-scheme: light) {
  .mm-18:has(.mm-18__theme-input:checked) {
    --mm-18-bg: #0a0a0a;
    --mm-18-surf: #101010;
    --mm-18-line: #f0f0f0;
    --mm-18-soft: #242424;
    --mm-18-ink: #f0f0f0;
    --mm-18-mut: #9a9a9a;
    --mm-18-acc: #ff4d3d;
    --mm-18-acc: oklch(70% 0.19 32);
  }
}

.mm-18__theme {
  position: absolute;
  inset-block-start: 42px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-18__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-18__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: var(--mm-18-rule) solid var(--mm-18-line);
  background: var(--mm-18-surf);
  color: var(--mm-18-ink);
  cursor: pointer;
}

.mm-18__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-18__theme-input:focus-visible + .mm-18__theme-label {
  outline: 2px solid var(--mm-18-acc);
  outline-offset: 3px;
}

.mm-18__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  border-block-end: 2px solid var(--mm-18-line);
  background: var(--mm-18-surf);
}

.mm-18__strip {
  inline-size: min(82rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  flex-wrap: wrap;
  min-block-size: 34px;
  border-block-end: var(--mm-18-rule) solid var(--mm-18-soft);
  font: 500 0.72rem/1 var(--mm-18-font-display);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mm-18-mut);
}

.mm-18__strip a {
  color: var(--mm-18-mut);
  text-decoration: none;
}

.mm-18__strip a:first-of-type {
  margin-inline-start: auto;
}

.mm-18__strip a:hover {
  color: var(--mm-18-acc);
}

.mm-18__bar {
  inline-size: min(82rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.75rem, 3vw, 2.5rem);
  flex-wrap: wrap;
  min-block-size: 62px;
  padding-inline-end: 60px;
}

.mm-18__brand {
  color: var(--mm-18-ink);
  text-decoration: none;
  font: 700 0.95rem/1 var(--mm-18-font-display);
  letter-spacing: 0.22em;
}

.mm-18__nav {
  min-inline-size: 0;
}

.mm-18__list {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(0.15rem, 1.5vw, 0.75rem);
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-18__item {
  position: static;
}

.mm-18__trigger,
.mm-18__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.5rem;
  border: 0;
  background: transparent;
  color: var(--mm-18-ink);
  font: 600 0.85rem/1 var(--mm-18-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
}

.mm-18__item--open > .mm-18__trigger,
.mm-18__item:hover > .mm-18__trigger,
.mm-18__item:focus-within > .mm-18__trigger {
  color: var(--mm-18-acc);
  box-shadow: inset 0 -3px 0 var(--mm-18-acc);
}

.mm-18__plain--sale {
  color: var(--mm-18-acc);
}

.mm-18__plain:hover,
.mm-18__trigger:hover {
  color: var(--mm-18-acc);
}

.mm-18__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-18-surf);
  border-block-end: var(--mm-18-rule) solid var(--mm-18-line);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 150ms ease, visibility 0s linear 150ms;
}

.mm-18__item--open > .mm-18__panel,
.mm-18__item:focus-within > .mm-18__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-18__item:hover > .mm-18__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transition-delay: 0s;
  }
}

.mm-18__panel-inner {
  inline-size: min(82rem, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
  grid-template-rows: auto minmax(0, 1fr);
  column-gap: var(--mm-18-gap-x);
  row-gap: var(--mm-18-gap-y);
  padding-block: clamp(1.1rem, 3vw, 1.9rem);
}

@media (min-width: 66rem) {
  .mm-18__panel-inner {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

.mm-18__col {
  min-inline-size: 0;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
  grid-row: span 2;
  gap: var(--mm-18-gap-y);
}

@supports (grid-template-rows: subgrid) {
  .mm-18__col {
    grid-template-rows: subgrid;
  }
}

.mm-18__col-head {
  margin: 0;
  padding-block-end: 0.4rem;
  border-block-end: 2px solid var(--mm-18-line);
  font: 700 0.74rem/1.2 var(--mm-18-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.mm-18__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  align-content: start;
}

.mm-18__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-18-mut);
  text-decoration: none;
  font: 400 0.88rem/1.3 system-ui, sans-serif;
  border-block-end: var(--mm-18-rule) solid var(--mm-18-soft);
  min-inline-size: 0;
}

.mm-18__links a:hover {
  color: var(--mm-18-acc);
}

.mm-18__foot {
  inline-size: min(82rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  flex-wrap: wrap;
  gap: clamp(0.75rem, 3vw, 2rem);
  padding-block: 0.5rem 0.9rem;
  border-block-start: var(--mm-18-rule) solid var(--mm-18-line);
}

.mm-18__foot a {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-18-ink);
  text-decoration: none;
  font: 600 0.72rem/1 var(--mm-18-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.mm-18__foot a:hover {
  color: var(--mm-18-acc);
}

.mm-18__page {
  inline-size: min(82rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(2.5rem, 8vw, 5rem);
}

.mm-18__editorial {
  max-inline-size: 40rem;
  display: grid;
  gap: 0.5rem;
}

.mm-18__ed-k {
  margin: 0;
  font: 700 0.7rem/1 var(--mm-18-font-display);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--mm-18-acc);
}

.mm-18__ed-h {
  margin: 0;
  font: 700 clamp(2rem, 6vw, 3.4rem)/1.05 var(--mm-18-font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.mm-18__ed-cta {
  justify-self: start;
  display: inline-flex;
  align-items: center;
  min-block-size: 48px;
  margin-block-start: 0.5rem;
  padding-inline: 1.4rem;
  background: var(--mm-18-ink);
  color: var(--mm-18-bg);
  text-decoration: none;
  font: 600 0.78rem/1 var(--mm-18-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

@media (max-width: 54rem) {
  .mm-18__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.5rem;
  }

  .mm-18__list {
    flex-direction: column;
  }

  .mm-18__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    display: none;
  }

  .mm-18__item--open > .mm-18__panel,
    .mm-18__item:focus-within > .mm-18__panel {
    display: block;
  }

  .mm-18__panel-inner,
    .mm-18__foot {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-18__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-18__trigger {
    position: relative;
  }

  .mm-18__item:hover > .mm-18__trigger::after,
    .mm-18__item:focus-within > .mm-18__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — columns wipe in strictly left to right on a linear grid clock */

.mm-18__col {
  clip-path: inset(0 100% 0 0);
  transition: clip-path 300ms linear;
}

.mm-18__item:hover > .mm-18__panel .mm-18__col,
.mm-18__item:focus-within > .mm-18__panel .mm-18__col,
.mm-18__item--open > .mm-18__panel .mm-18__col {
  clip-path: inset(-8px);
}

.mm-18__col:nth-child(1) {
  transition-delay: 0ms;
}

.mm-18__col:nth-child(2) {
  transition-delay: 90ms;
}

.mm-18__col:nth-child(3) {
  transition-delay: 180ms;
}

.mm-18__col:nth-child(4) {
  transition-delay: 270ms;
}

.mm-18__col:nth-child(5) {
  transition-delay: 360ms;
}

.mm-18__col:nth-child(n+6) {
  transition-delay: 360ms;
}

.mm-18__foot {
  opacity: 0;
  transition: opacity 200ms linear 420ms;
}

.mm-18__item:hover > .mm-18__panel .mm-18__foot,
.mm-18__item:focus-within > .mm-18__panel .mm-18__foot,
.mm-18__item--open > .mm-18__panel .mm-18__foot {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .mm-18__col,
    .mm-18__foot {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-18__col {
    clip-path: none;
  }

  .mm-18__foot {
    opacity: 1;
  }
}
```
