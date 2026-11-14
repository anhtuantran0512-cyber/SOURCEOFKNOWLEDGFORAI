---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/e-commerce-grid-pagination/"
title: "E-Commerce Grid Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "A category-page footer that does the two things shoppers actually need: a stable card grid that never reflows as images land, and a \"Showing 1–4 of 96…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Grid Pagination
Source: https://codefronts.com/navigation/css-pagination/e-commerce-grid-pagination/

A category-page footer that does the two things shoppers actually need: a stable card grid that never reflows as images land, and a "Showing 1–4 of 96 products" line that says where you are in the catalogue. Auto-fit columns, locked 4:3 imagery, a windowed number row with an ellipsis, and no media queries anywhere.
## HTML
```html
<section class="pgn-11" aria-label="E-Commerce Product Grid Pagination with Item Count demo">
  <div class="pgn-11__stage">
    <header class="pgn-11__head">
      <div>
        <p class="pgn-11__eyebrow">Audio</p>
        <h2 class="pgn-11__title">Headphones &amp; wearables</h2>
      </div>
      <p class="pgn-11__count">Showing <b>1–4</b> of <b>96</b> products</p>
    </header>

    <ul class="pgn-11__grid">
      <li class="pgn-11__card">
        <img class="pgn-11__img" src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&auto=format" alt="Over-ear wireless headphones on a yellow background" width="400" height="300" loading="lazy" decoding="async">
        <div class="pgn-11__body"><h3>Wireless Headphones</h3><p>Studio ANC · 40h</p><p class="pgn-11__price">$249</p></div>
      </li>
      <li class="pgn-11__card">
        <img class="pgn-11__img" src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&auto=format" alt="Minimal analogue smartwatch with a white strap" width="400" height="300" loading="lazy" decoding="async">
        <div class="pgn-11__body"><h3>Field Watch 38</h3><p>Sapphire · 5 ATM</p><p class="pgn-11__price">$180</p></div>
      </li>
      <li class="pgn-11__card">
        <img class="pgn-11__img" src="https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=400&auto=format" alt="Smartwatch with a dark case showing a colourful face" width="400" height="300" loading="lazy" decoding="async">
        <div class="pgn-11__body"><h3>Trail Tracker S2</h3><p>GPS · 7-day battery</p><p class="pgn-11__price">$329</p></div>
      </li>
      <li class="pgn-11__card">
        <img class="pgn-11__img" src="https://images.unsplash.com/photo-1498049794561-7780e7231661?w=400&auto=format" alt="Headphones and a phone arranged on a white desk" width="400" height="300" loading="lazy" decoding="async">
        <div class="pgn-11__body"><h3>Desk Bundle</h3><p>Pad · cable · stand</p><p class="pgn-11__price">$74</p></div>
      </li>
    </ul>

    <nav class="pgn-11__nav" aria-label="Product pagination">
      <button class="pgn-11__edge" type="button" disabled aria-label="Previous page">Previous</button>
      <ol class="pgn-11__list">
        <li><button class="pgn-11__num" type="button" aria-current="page">1</button></li>
        <li><button class="pgn-11__num" type="button">2</button></li>
        <li><button class="pgn-11__num" type="button">3</button></li>
        <li aria-hidden="true" class="pgn-11__gap">…</li>
        <li><button class="pgn-11__num" type="button">24</button></li>
      </ol>
      <button class="pgn-11__edge" type="button" aria-label="Next page">Next</button>
    </nav>
  </div>
</section>
```
## CSS
```css
.pgn-11 {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f4f4f5;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #18181b;
  --acc-fg: #ffffff;
  --ring: #6366f1;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-11 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96.5% .003 286);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(22% .008 286);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-11:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --surface-2: #1c1c20;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #fafafa;
    --acc-fg: #09090b;
    --ring: #818cf8;
  }
}

.pgn-11[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --surface-2: #1c1c20;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
}

.pgn-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,5vw,4rem);
  background: var(--bg);
  color: var(--text);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.pgn-11,
.pgn-11 *,
.pgn-11 *::before,
.pgn-11 *::after {
  box-sizing: border-box;
}

.pgn-11__stage {
  width: 100%;
  max-width: 60rem;
  display: grid;
  gap: 1.5rem;
}

.pgn-11__head {
  display: flex;
  flex-wrap: wrap;
  align-items: end;
  justify-content: space-between;
  gap: .75rem;
}

.pgn-11__eyebrow {
  margin: 0 0 .35rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-11__title {
  margin: 0;
  font-size: clamp(1.35rem,3vw,1.75rem);
  font-weight: 600;
  letter-spacing: -.025em;
}

.pgn-11__count {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pgn-11__count b {
  color: var(--text);
  font-weight: 600;
}

.pgn-11__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(12rem,1fr));
  gap: 1rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-11__card {
  display: grid;
  grid-template-rows: auto 1fr;
  overflow: hidden;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: .875rem;
  transition: border-color .2s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.pgn-11__card:hover {
  border-color: color-mix(in oklab,var(--text) 24%,var(--line));
  translate: 0 -2px;
}

.pgn-11__img {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  background: var(--surface-2);
  display: block;
}

.pgn-11__body {
  display: grid;
  gap: .2rem;
  padding: .85rem .95rem 1rem;
}

.pgn-11__body h3 {
  margin: 0;
  font-size: .9375rem;
  font-weight: 550;
  letter-spacing: -.01em;
}

.pgn-11__body p {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
}

.pgn-11__price {
  margin-top: .35rem !important;
  color: var(--text) !important;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.pgn-11__nav {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--line);
}

.pgn-11__list {
  display: flex;
  align-items: center;
  gap: .3rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-11__num,
.pgn-11__edge {
  display: inline-grid;
  place-items: center;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .9rem;
  border: 1px solid var(--line);
  border-radius: .625rem;
  background: var(--surface);
  color: var(--text);
  font: inherit;
  font-size: .875rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .16s ease, border-color .16s ease;
}

.pgn-11__num {
  padding: 0 .5rem;
}

.pgn-11__num:hover,
.pgn-11__edge:not(:disabled):hover {
  background: var(--surface-2);
}

.pgn-11__num:focus-visible,
.pgn-11__edge:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-11__num[aria-current="page"] {
  background: var(--acc);
  border-color: transparent;
  color: var(--acc-fg);
}

.pgn-11__edge:disabled {
  opacity: .36;
  cursor: not-allowed;
}

.pgn-11__gap {
  display: grid;
  place-items: end center;
  min-width: 1.5rem;
  height: 2.75rem;
  padding-bottom: .6rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .pgn-11 * {
    animation: none !important;
    transition: none !important;
  }
}
```
