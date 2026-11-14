---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/full-width-fluid-pagination/"
title: "Full-Width Fluid Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "The docs-footer layout: previous and next articles pinned to the outer edges with their titles, page numbers exactly in the middle."
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Width Fluid Pagination
Source: https://codefronts.com/navigation/css-pagination/full-width-fluid-pagination/

The docs-footer layout: previous and next articles pinned to the outer edges with their titles, page numbers exactly in the middle. Flexbox cannot actually do this — the centre drifts as soon as the two labels differ in length — so it is a three-track grid, which stays centred at any width and folds to a two-column stack on narrow screens.
## HTML
```html
<section class="pgn-18" aria-label="Full-Width Fluid Pagination (Prev Left, Numbers Center, Next Right) demo">
  <div class="pgn-18__stage">
    <header class="pgn-18__head">
      <p class="pgn-18__eyebrow">Documentation index</p>
      <h2 class="pgn-18__title">Edge-anchored, centre-balanced</h2>
      <p class="pgn-18__sub">A three-column grid with 1fr on both sides keeps the number list optically centred no matter how wide the frame gets or how long the edge labels are.</p>
    </header>

    <nav class="pgn-18__nav" aria-label="Pagination">
      <button class="pgn-18__edge" type="button">
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="pgn-18__edgetext"><b>Previous</b><i>Styling form controls</i></span>
      </button>

      <ol class="pgn-18__list">
        <li><button class="pgn-18__num" type="button" aria-label="Page 5">5</button></li>
        <li><button class="pgn-18__num" type="button" aria-label="Page 6">6</button></li>
        <li><button class="pgn-18__num" type="button" aria-current="page" aria-label="Page 7, current page">7</button></li>
        <li><button class="pgn-18__num" type="button" aria-label="Page 8">8</button></li>
        <li><button class="pgn-18__num" type="button" aria-label="Page 9">9</button></li>
      </ol>

      <button class="pgn-18__edge pgn-18__edge--next" type="button">
        <span class="pgn-18__edgetext"><b>Next</b><i>Anchor positioning</i></span>
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </nav>
  </div>
</section>
```
## CSS
```css
.pgn-18 {
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
  .pgn-18 {
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
  .pgn-18:not([data-theme="light"]) {
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

.pgn-18[data-theme="dark"] {
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

.pgn-18 {
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

.pgn-18,
.pgn-18 *,
.pgn-18 *::before,
.pgn-18 *::after {
  box-sizing: border-box;
}

.pgn-18__stage {
  width: 100%;
  max-width: 72rem;
  display: grid;
  gap: 2.5rem;
}

.pgn-18__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-18__title {
  margin: 0 0 .55rem;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
}

.pgn-18__sub {
  margin: 0;
  max-width: 38rem;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-18__nav {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 1rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
}

.pgn-18__list {
  display: flex;
  gap: .3rem;
  list-style: none;
  margin: 0;
  padding: 0;
  justify-content: center;
}

.pgn-18__edge {
  display: inline-flex;
  align-items: center;
  gap: .7rem;
  justify-self: start;
  min-height: 3.25rem;
  padding: .5rem .9rem;
  border: 1px solid transparent;
  border-radius: .75rem;
  background: transparent;
  color: var(--text);
  font: inherit;
  text-align: left;
  cursor: pointer;
  transition: background .18s ease, border-color .18s ease;
}

.pgn-18__edge--next {
  justify-self: end;
  text-align: right;
}

.pgn-18__edge:hover {
  background: var(--surface);
  border-color: var(--line);
}

.pgn-18__edge:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-18__edge svg {
  width: 1.15rem;
  height: 1.15rem;
  color: var(--muted);
  flex: none;
}

.pgn-18__edgetext {
  display: grid;
  gap: .1rem;
}

.pgn-18__edgetext b {
  font-size: .75rem;
  font-weight: 500;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-18__edgetext i {
  font-style: normal;
  font-size: .9375rem;
  font-weight: 550;
  letter-spacing: -.01em;
}

.pgn-18__num {
  display: grid;
  place-items: center;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .5rem;
  border: 1px solid var(--line);
  border-radius: .625rem;
  background: var(--surface);
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .16s ease, border-color .16s ease;
}

.pgn-18__num:hover {
  background: var(--surface-2);
}

.pgn-18__num:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-18__num[aria-current="page"] {
  background: var(--acc);
  border-color: transparent;
  color: var(--acc-fg);
  font-weight: 600;
}

@media (max-width: 46rem) {
  .pgn-18__nav {
    grid-template-columns: 1fr 1fr;
    row-gap: 1.25rem;
  }

  .pgn-18__list {
    grid-column: 1/-1;
    order: -1;
  }

  .pgn-18__edgetext i {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pgn-18 * {
    animation: none !important;
    transition: none !important;
  }
}
```
