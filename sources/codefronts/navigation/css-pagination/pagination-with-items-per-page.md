---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/pagination-with-items-per-page/"
title: "Pagination with Items Per Page"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "The three-part bar every admin list converges on: page size on the left, a record range in the middle, a compact stepper on the right."
has_js: "true"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pagination with Items Per Page
Source: https://codefronts.com/navigation/css-pagination/pagination-with-items-per-page/

The three-part bar every admin list converges on: page size on the left, a record range in the middle, a compact stepper on the right. Changing the page size resets to page one and recomputes the window — the exact contract an offset-based API expects — and the native <select> is restyled without losing its real menu or keyboard type-ahead.
## HTML
```html
<section class="pgn-06" aria-label="Pagination with Items-Per-Page Selector Dropdown demo">
  <div class="pgn-06__stage">
    <header class="pgn-06__head">
      <p class="pgn-06__eyebrow">Orders</p>
      <h2 class="pgn-06__title">288 results</h2>
      <p class="pgn-06__sub">Changing page size resets to page one and recalculates the record window — the same contract every server-side list API expects.</p>
    </header>

    <div class="pgn-06__bar">
      <div class="pgn-06__size">
        <label class="pgn-06__label" for="pgn-06-per">Rows per page</label>
        <div class="pgn-06__selectwrap">
          <select class="pgn-06__select" id="pgn-06-per">
            <option value="12">12</option>
            <option value="24" selected>24</option>
            <option value="48">48</option>
            <option value="96">96</option>
          </select>
          <svg class="pgn-06__caret" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M5.5 8 10 12.5 14.5 8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </div>
      </div>

      <p class="pgn-06__range" role="status" aria-live="polite" data-range>1–24 of 288</p>

      <nav class="pgn-06__nav" aria-label="Pagination">
        <button class="pgn-06__btn" type="button" data-prev aria-label="Previous page">
          <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <p class="pgn-06__count" data-count>Page 1 of 12</p>
        <button class="pgn-06__btn" type="button" data-next aria-label="Next page">
          <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.pgn-06 {
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
  .pgn-06 {
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
  .pgn-06:not([data-theme="light"]) {
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

.pgn-06[data-theme="dark"] {
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

.pgn-06 {
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

.pgn-06,
.pgn-06 *,
.pgn-06 *::before,
.pgn-06 *::after {
  box-sizing: border-box;
}

.pgn-06__stage {
  width: 100%;
  max-width: 52rem;
  display: grid;
  gap: 2rem;
}

.pgn-06__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-06__title {
  margin: 0 0 .55rem;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
  font-variant-numeric: tabular-nums;
}

.pgn-06__sub {
  margin: 0;
  max-width: 36rem;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-06__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .75rem .9rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
}

.pgn-06__size {
  display: flex;
  align-items: center;
  gap: .6rem;
}

.pgn-06__label {
  font-size: .8125rem;
  color: var(--muted);
  white-space: nowrap;
}

.pgn-06__selectwrap {
  position: relative;
  display: inline-grid;
  align-items: center;
}

.pgn-06__select {
  appearance: none;
  height: 2.75rem;
  padding: 0 2.25rem 0 .85rem;
  border: 1px solid var(--line);
  border-radius: .625rem;
  background: var(--surface-2);
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
}

.pgn-06__caret {
  position: absolute;
  right: .7rem;
  width: 1.05rem;
  height: 1.05rem;
  color: var(--muted);
  pointer-events: none;
}

.pgn-06__range {
  margin: 0;
  font-size: .875rem;
  color: var(--text);
  font-variant-numeric: tabular-nums;
}

.pgn-06__nav {
  display: flex;
  align-items: center;
  gap: .4rem;
}

.pgn-06__count {
  margin: 0 .35rem;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  min-width: 7.5rem;
  text-align: center;
}

.pgn-06__btn {
  display: inline-grid;
  place-items: center;
  width: 2.75rem;
  height: 2.75rem;
  border: 1px solid var(--line);
  border-radius: .625rem;
  background: var(--surface);
  color: var(--text);
  cursor: pointer;
  transition: background .16s ease, border-color .16s ease;
}

.pgn-06__btn svg {
  width: 1.125rem;
  height: 1.125rem;
}

.pgn-06__btn:not(:disabled):hover {
  background: var(--surface-2);
  border-color: color-mix(in oklab,var(--text) 28%,var(--line));
}

.pgn-06__btn:disabled {
  opacity: .36;
  cursor: not-allowed;
}

.pgn-06__btn:focus-visible,
.pgn-06__select:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

@media (max-width: 38rem) {
  .pgn-06__bar {
    justify-content: center;
    text-align: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pgn-06 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.pgn-06');
  if (!root) return;
  const select = root.querySelector('#pgn-06-per');
  const range = root.querySelector('[data-range]');
  const count = root.querySelector('[data-count]');
  const prev = root.querySelector('[data-prev]');
  const next = root.querySelector('[data-next]');
  const total = 288;
  let per = Number(select.value), page = 1;
  const paint = () => {
    const pages = Math.ceil(total / per);
    const from = (page - 1) * per + 1;
    const to = Math.min(page * per, total);
    range.textContent = from + '–' + to + ' of ' + total;
    count.textContent = 'Page ' + page + ' of ' + pages;
    prev.disabled = page === 1; next.disabled = page === pages;
  };
  select.addEventListener('change', () => { per = Number(select.value); page = 1; paint(); });
  prev.addEventListener('click', () => { if (page > 1) { page--; paint(); } });
  next.addEventListener('click', () => { if (page < Math.ceil(total / per)) { page++; paint(); } });
  paint();
})();
```
