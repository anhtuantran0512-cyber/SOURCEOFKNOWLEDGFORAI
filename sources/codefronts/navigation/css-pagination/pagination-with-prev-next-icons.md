---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/pagination-with-prev-next-icons/"
title: "Pagination with Prev Next Icons"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "The four-control bracket every data view eventually needs — first, previous, next, last — drawn as inline SVG chevrons around a number row."
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pagination with Prev Next Icons
Source: https://codefronts.com/navigation/css-pagination/pagination-with-prev-next-icons/

The four-control bracket every data view eventually needs — first, previous, next, last — drawn as inline SVG chevrons around a number row. Boundary state uses the native disabled attribute rather than a class, hit targets are a full 44 px, and every icon-only control carries a real accessible name.
## HTML
```html
<section class="pgn-04" aria-label="Pagination with First / Last / Prev / Next Icon Buttons demo">
  <div class="pgn-04__stage">
    <header class="pgn-04__head">
      <p class="pgn-04__eyebrow">Search results</p>
      <h2 class="pgn-04__title">Page 1 of 18</h2>
      <p class="pgn-04__sub">First and Previous are disabled on the boundary — the state is real, not decorative.</p>
    </header>

    <nav class="pgn-04__nav" aria-label="Pagination">
      <button class="pgn-04__icon" type="button" aria-label="First page" disabled>
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M15 4.5 9.5 10l5.5 5.5M9 4.5 3.5 10 9 15.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <button class="pgn-04__icon" type="button" aria-label="Previous page" disabled>
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>

      <ol class="pgn-04__list">
        <li><button class="pgn-04__num" type="button" aria-current="page">1</button></li>
        <li><button class="pgn-04__num" type="button">2</button></li>
        <li><button class="pgn-04__num" type="button">3</button></li>
        <li><button class="pgn-04__num" type="button">4</button></li>
        <li><button class="pgn-04__num" type="button">5</button></li>
      </ol>

      <button class="pgn-04__icon" type="button" aria-label="Next page">
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <button class="pgn-04__icon" type="button" aria-label="Last page">
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M5 4.5 10.5 10 5 15.5M11 4.5 16.5 10 11 15.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </nav>

    <p class="pgn-04__legend">Icon-only controls carry an aria-label; the tooltip text below each is a title-free CSS layer.</p>
  </div>
</section>
```
## CSS
```css
.pgn-04 {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f4f4f5;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #0f766e;
  --acc-fg: #ffffff;
  --ring: #14b8a6;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-04 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96.5% .003 286);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(48% .09 183);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(70% .13 183);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-04:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --surface-2: #1c1c20;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #2dd4bf;
    --acc-fg: #09090b;
    --ring: #5eead4;
  }
}

.pgn-04[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --surface-2: #1c1c20;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #2dd4bf;
  --acc-fg: #09090b;
  --ring: #5eead4;
}

.pgn-04 {
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

.pgn-04,
.pgn-04 *,
.pgn-04 *::before,
.pgn-04 *::after {
  box-sizing: border-box;
}

.pgn-04__stage {
  width: 100%;
  max-width: 44rem;
  display: grid;
  gap: 1.75rem;
  justify-items: center;
  text-align: center;
}

.pgn-04__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-04__title {
  margin: 0 0 .55rem;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
  font-variant-numeric: tabular-nums;
}

.pgn-04__sub {
  margin: 0;
  max-width: 32rem;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-04__nav {
  display: flex;
  align-items: center;
  gap: .375rem;
  flex-wrap: wrap;
  justify-content: center;
  padding: .5rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
}

.pgn-04__list {
  display: flex;
  gap: .25rem;
  list-style: none;
  margin: 0 .25rem;
  padding: 0;
}

.pgn-04__icon,
.pgn-04__num {
  display: inline-grid;
  place-items: center;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .5rem;
  border: 1px solid transparent;
  border-radius: .625rem;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .16s ease, color .16s ease, scale .16s cubic-bezier(.16,1,.3,1);
}

.pgn-04__icon {
  color: var(--muted);
}

.pgn-04__icon svg {
  width: 1.15rem;
  height: 1.15rem;
}

.pgn-04__icon:not(:disabled):hover,
.pgn-04__num:hover {
  background: var(--surface-2);
  color: var(--text);
}

.pgn-04__icon:not(:disabled):active,
.pgn-04__num:active {
  scale: .94;
}

.pgn-04__icon:focus-visible,
.pgn-04__num:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-04__icon:disabled {
  opacity: .32;
  cursor: not-allowed;
}

.pgn-04__num[aria-current="page"] {
  background: var(--acc);
  color: var(--acc-fg);
}

.pgn-04__legend {
  margin: 0;
  max-width: 30rem;
  font-size: .75rem;
  line-height: 1.6;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .pgn-04 * {
    animation: none !important;
    transition: none !important;
  }
}
```
