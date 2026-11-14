---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/selected-work-grid/"
title: "Brutalist Portfolio Grid"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A \"Selected Work\" index built as numbered rows with heavy horizontal rules, oversized titles and monospace metadata."
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Portfolio Grid
Source: https://codefronts.com/design-styles/css-brutalist/selected-work-grid/

A "Selected Work" index built as numbered rows with heavy horizontal rules, oversized titles and monospace metadata. Hovering or focusing a row inverts it to black and reveals a thumbnail that follows the row — a pure-CSS preview with no JavaScript, no mouse tracking and no layout shift.
## HTML
```html
<div class="brt-18">
  <input class="brt-18__sr" type="checkbox" id="brt-18-dark">
  <label class="brt-18__theme" for="brt-18-dark">
    <svg class="brt-18__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-18__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-18__vh">Dark theme</span>
  </label>

  <div class="brt-18__stage">
    <section class="brt-18__wrap" aria-labelledby="brt-18-h">
      <header class="brt-18__head">
        <h1 class="brt-18__h" id="brt-18-h">SELECTED<br>WORK</h1>
        <p class="brt-18__meta">Studio Halden · 2019—2026 · Bristol / Oslo<br>Six of forty-one. Full index on request.</p>
      </header>

      <ol class="brt-18__list">
        <li class="brt-18__row">
          <h2 class="brt-18__t"><a href="#brt-18-h">Harbourline Freight</a></h2>
          <p class="brt-18__cat">Identity, Wayfinding</p>
          <p class="brt-18__yr">2026</p>
          <img class="brt-18__thumb" src="https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?w=360&amp;h=240&amp;fit=crop&amp;auto=format" width="360" height="240" alt="" aria-hidden="true" loading="lazy" decoding="async">
        </li>
        <li class="brt-18__row">
          <h2 class="brt-18__t"><a href="#brt-18-h">Ninth Street Records</a></h2>
          <p class="brt-18__cat">Art direction, Sleeve design</p>
          <p class="brt-18__yr">2025</p>
          <img class="brt-18__thumb" src="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=360&amp;h=240&amp;fit=crop&amp;auto=format" width="360" height="240" alt="" aria-hidden="true" loading="lazy" decoding="async">
        </li>
        <li class="brt-18__row">
          <h2 class="brt-18__t"><a href="#brt-18-h">Kettle Row Bakery</a></h2>
          <p class="brt-18__cat">Packaging, Signage</p>
          <p class="brt-18__yr">2025</p>
          <img class="brt-18__thumb" src="https://images.unsplash.com/photo-1509440159596-0249088772ff?w=360&amp;h=240&amp;fit=crop&amp;auto=format" width="360" height="240" alt="" aria-hidden="true" loading="lazy" decoding="async">
        </li>
        <li class="brt-18__row">
          <h2 class="brt-18__t"><a href="#brt-18-h">Meridian Type Foundry</a></h2>
          <p class="brt-18__cat">Website, Specimen</p>
          <p class="brt-18__yr">2024</p>
          <img class="brt-18__thumb" src="https://images.unsplash.com/photo-1516414447565-b14be0adf13e?w=360&amp;h=240&amp;fit=crop&amp;auto=format" width="360" height="240" alt="" aria-hidden="true" loading="lazy" decoding="async">
        </li>
        <li class="brt-18__row">
          <h2 class="brt-18__t"><a href="#brt-18-h">Peartree Labs</a></h2>
          <p class="brt-18__cat">Product design</p>
          <p class="brt-18__yr">2023</p>
          <img class="brt-18__thumb" src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?w=360&amp;h=240&amp;fit=crop&amp;auto=format" width="360" height="240" alt="" aria-hidden="true" loading="lazy" decoding="async">
        </li>
        <li class="brt-18__row">
          <h2 class="brt-18__t"><a href="#brt-18-h">Civic Archive, Oslo</a></h2>
          <p class="brt-18__cat">Exhibition, Print</p>
          <p class="brt-18__yr">2021</p>
          <img class="brt-18__thumb" src="https://images.unsplash.com/photo-1481277542470-605612bd2d61?w=360&amp;h=240&amp;fit=crop&amp;auto=format" width="360" height="240" alt="" aria-hidden="true" loading="lazy" decoding="async">
        </li>
      </ol>

      <p class="brt-18__foot">ENQUIRIES — [email protected] — +44 117 000 0000</p>
    </section>
  </div>
</div>
```
## CSS
```css
.brt-18 {
  --page: #efeeea;
  --panel: #ffffff;
  --ink: #000000;
  --muted: #3c3c3c;
  --edge: #000000;
  --sh: #000000;
  --rule: 4px;
  --mono: ui-monospace,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,'Segoe UI',Arial,sans-serif;
  font-size: 16px;
}

.brt-18 *,
.brt-18 *::before,
.brt-18 *::after {
  box-sizing: border-box;
  border-radius: 0;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-18 {
    --page: oklch(0.946 0.004 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0 0 0);
    --muted: oklch(0.35 0 0);
  }
}

.brt-18__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-18__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-18__theme {
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
  border: 3px solid var(--edge);
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
}

.brt-18__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-18__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-18__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-18__sr:focus-visible + .brt-18__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-18__sun {
  display: none;
}

.brt-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(1rem,3vw,2.75rem);
}

.brt-18__wrap {
  inline-size: min(74rem,100%);
}

.brt-18__head {
  display: grid;
  gap: 1rem;
  padding-inline-end: 3.5rem;
  padding-block-end: 1.25rem;
  border-block-end: var(--rule) solid var(--edge);
}

@media (min-width: 48rem) {
  .brt-18__head {
    grid-template-columns: 1fr auto;
    align-items: end;
  }
}

.brt-18__h {
  margin: 0;
  font-size: clamp(2.4rem,9vw,5.5rem);
  font-weight: 700;
  letter-spacing: -.045em;
  line-height: .86;
  text-transform: uppercase;
}

.brt-18__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .76rem;
  line-height: 1.7;
  letter-spacing: .06em;
  color: var(--muted);
}

.brt-18__list {
  list-style: none;
  margin: 0;
  padding: 0;
  counter-reset: brt18;
}

.brt-18__row {
  position: relative;
  counter-increment: brt18;
  display: grid;
  grid-template-columns: 3.2rem minmax(0,1fr);
  gap: .15rem 1rem;
  align-items: baseline;
  padding: 1.1rem .75rem 1.15rem 0;
  border-block-end: var(--rule) solid var(--edge);
}

@media (min-width: 48rem) {
  .brt-18__row {
    grid-template-columns: 4rem minmax(0,1fr) 14rem 5rem;
  }
}

.brt-18__row::before {
  content: counter(brt18,decimal-leading-zero);
  grid-row: 1 / span 3;
  grid-column: 1;
  font-family: var(--mono);
  font-size: .86rem;
  letter-spacing: .08em;
  font-variant-numeric: tabular-nums;
  color: var(--muted);
}

@media (min-width: 48rem) {
  .brt-18__row::before {
    grid-row: 1;
  }
}

@media (hover: hover) {
  .brt-18__row:hover {
    background: var(--ink);
    color: var(--panel);
  }

  .brt-18__row:hover::before,
    .brt-18__row:hover .brt-18__cat,
    .brt-18__row:hover .brt-18__yr {
    color: var(--panel);
  }

  .brt-18__row:hover .brt-18__thumb {
    opacity: 1;
    scale: 1;
  }

  .brt-18__row:hover {
    padding-inline-start: .75rem;
  }
}

.brt-18__row:focus-within {
  background: var(--ink);
  color: var(--panel);
  padding-inline-start: .75rem;
}

.brt-18__row:focus-within::before,
.brt-18__row:focus-within .brt-18__cat,
.brt-18__row:focus-within .brt-18__yr {
  color: var(--panel);
}

.brt-18__row:focus-within .brt-18__thumb {
  opacity: 1;
  scale: 1;
}

.brt-18__t {
  margin: 0;
  font-size: clamp(1.5rem,4.6vw,2.6rem);
  font-weight: 700;
  letter-spacing: -.035em;
  line-height: 1.02;
}

.brt-18__t a {
  color: inherit;
  text-decoration: none;
}

.brt-18__t a::after {
  content: '';
  position: absolute;
  inset: 0;
}

.brt-18__t a:focus-visible {
  outline: none;
}

.brt-18__row:focus-within .brt-18__t a::after {
  outline: 3px solid currentColor;
  outline-offset: -6px;
}

.brt-18__cat,
.brt-18__yr {
  margin: 0;
  font-family: var(--mono);
  font-size: .78rem;
  letter-spacing: .08em;
  color: var(--muted);
}

@media (min-width: 48rem) {
  .brt-18__yr {
    text-align: end;
  }
}

.brt-18__thumb {
  position: absolute;
  inset-inline-end: .75rem;
  inset-block-start: 50%;
  translate: 0 -50%;
  inline-size: 9rem;
  aspect-ratio: 3/2;
  object-fit: cover;
  display: none;
  border: 3px solid var(--panel);
  opacity: 0;
  scale: .95;
  pointer-events: none;
  transition: opacity .14s linear, scale .14s ease;
}

@media (min-width: 64rem) {
  .brt-18__thumb {
    display: block;
    inset-inline-end: 6rem;
  }
}

.brt-18__foot {
  margin: 1.75rem 0 0;
  font-family: var(--mono);
  font-size: .76rem;
  letter-spacing: .12em;
  color: var(--muted);
}

.brt-18:has(#brt-18-dark:checked) {
  --page: #000000;
  --panel: #0a0a0a;
  --ink: #ffffff;
  --muted: #bdbdbd;
  --edge: #ffffff;
  --sh: #ffffff;
}

.brt-18:has(#brt-18-dark:checked) .brt-18__moon {
  display: none;
}

.brt-18:has(#brt-18-dark:checked) .brt-18__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-18:not(:has(#brt-18-dark:checked)) {
    --page: #000000;
    --panel: #0a0a0a;
    --ink: #ffffff;
    --muted: #bdbdbd;
    --edge: #ffffff;
    --sh: #ffffff;
  }

  .brt-18:not(:has(#brt-18-dark:checked)) .brt-18__moon {
    display: none;
  }

  .brt-18:not(:has(#brt-18-dark:checked)) .brt-18__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-18 *,
    .brt-18 *::before,
    .brt-18 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-18__row:hover,
    .brt-18__row:focus-within {
    background: Canvas;
    color: CanvasText;
  }

  .brt-18__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-18__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
