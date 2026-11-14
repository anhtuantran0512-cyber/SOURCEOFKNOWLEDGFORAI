---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/pagination-with-jump-to-page-input/"
title: "Pagination with Jump to Page Input"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "Once a list runs to sixty-four pages, numbered buttons stop helping — you need a box to type into."
has_js: "true"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pagination with Jump to Page Input
Source: https://codefronts.com/navigation/css-pagination/pagination-with-jump-to-page-input/

Once a list runs to sixty-four pages, numbered buttons stop helping — you need a box to type into. This bar pairs Previous/Next with a bounded number input and a Go button, validates the entry in JavaScript (because min/max outside a form validate nothing), and reports both the error and the new record range to assistive tech.
## HTML
```html
<section class="pgn-05" aria-label="Pagination with Jump to Page Input Field demo">
  <div class="pgn-05__stage">
    <header class="pgn-05__head">
      <p class="pgn-05__eyebrow">Audit log · 1,536 entries</p>
      <h2 class="pgn-05__title" data-title>Page 12 of 64</h2>
    </header>

    <nav class="pgn-05__nav" aria-label="Pagination">
      <button class="pgn-05__edge" type="button" data-prev>Previous</button>

      <div class="pgn-05__jump">
        <label class="pgn-05__label" for="pgn-05-input">Jump to</label>
        <input class="pgn-05__input" id="pgn-05-input" type="number" inputmode="numeric" min="1" max="64" value="12" aria-describedby="pgn-05-range">
        <span class="pgn-05__of" id="pgn-05-range">/ 64</span>
        <button class="pgn-05__go" type="button" data-go>Go</button>
      </div>

      <button class="pgn-05__edge" type="button" data-next>Next</button>
    </nav>

    <p class="pgn-05__msg" data-msg hidden>Enter a page between 1 and 64.</p>
    <p class="pgn-05__status" role="status" aria-live="polite" data-status>Showing entries 265–288</p>
  </div>
</section>
```
## CSS
```css
.pgn-05 {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f4f4f5;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #18181b;
  --acc-fg: #ffffff;
  --ring: #6366f1;
  --warn: #b91c1c;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-05 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96.5% .003 286);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(22% .008 286);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
    --warn: oklch(53% .2 27);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-05:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --surface-2: #1c1c20;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #fafafa;
    --acc-fg: #09090b;
    --ring: #818cf8;
    --warn: #f87171;
  }
}

.pgn-05[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --surface-2: #1c1c20;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
  --warn: #f87171;
}

.pgn-05 {
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

.pgn-05,
.pgn-05 *,
.pgn-05 *::before,
.pgn-05 *::after {
  box-sizing: border-box;
}

.pgn-05__stage {
  width: 100%;
  max-width: 44rem;
  display: grid;
  gap: 1.5rem;
  justify-items: center;
  text-align: center;
}

.pgn-05__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pgn-05__title {
  margin: 0;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
  font-variant-numeric: tabular-nums;
}

.pgn-05__nav {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  justify-content: center;
  gap: .5rem;
  padding: .5rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
}

.pgn-05__edge,
.pgn-05__go {
  display: inline-grid;
  place-items: center;
  height: 2.75rem;
  padding: 0 1rem;
  border: 1px solid var(--line);
  border-radius: .625rem;
  background: var(--surface);
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  cursor: pointer;
  transition: background .16s ease, border-color .16s ease;
}

.pgn-05__go {
  background: var(--acc);
  border-color: transparent;
  color: var(--acc-fg);
}

.pgn-05__edge:not(:disabled):hover {
  border-color: color-mix(in oklab,var(--text) 28%,var(--line));
}

.pgn-05__go:hover {
  opacity: .88;
}

.pgn-05__edge:disabled {
  opacity: .38;
  cursor: not-allowed;
}

.pgn-05__edge:focus-visible,
.pgn-05__go:focus-visible,
.pgn-05__input:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-05__jump {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: 0 .35rem;
}

.pgn-05__label {
  font-size: .8125rem;
  color: var(--muted);
}

.pgn-05__input {
  width: 4.25rem;
  height: 2.75rem;
  padding: 0 .55rem;
  text-align: center;
  border: 1px solid var(--line);
  border-radius: .625rem;
  background: var(--surface-2);
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
}

.pgn-05__input[aria-invalid="true"] {
  border-color: var(--warn);
}

.pgn-05__of {
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pgn-05__msg {
  margin: 0;
  font-size: .8125rem;
  color: var(--warn);
}

.pgn-05 [hidden] {
  display: none !important;
}

.pgn-05__msg:not([hidden]) {
  display: block;
  transition: opacity .2s ease, translate .2s ease;
}

@supports (transition-behavior: allow-discrete) {
  .pgn-05__msg:not([hidden]) {
    @starting-style {
      opacity: 0;
      translate: 0 -.35rem;
    }
  }
}

.pgn-05__status {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

@media (prefers-reduced-motion: reduce) {
  .pgn-05 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.pgn-05');
  if (!root) return;
  const input = root.querySelector('#pgn-05-input');
  const msg = root.querySelector('[data-msg]');
  const title = root.querySelector('[data-title]');
  const status = root.querySelector('[data-status]');
  const prev = root.querySelector('[data-prev]');
  const next = root.querySelector('[data-next]');
  const total = 64, per = 24;
  let current = 12;
  const paint = () => {
    input.value = current;
    title.textContent = 'Page ' + current + ' of ' + total;
    status.textContent = 'Showing entries ' + ((current - 1) * per + 1) + '–' + (current * per);
    prev.disabled = current === 1; next.disabled = current === total;
  };
  const jump = () => {
    const n = Number.parseInt(input.value, 10);
    const ok = Number.isInteger(n) && n >= 1 && n <= total;
    msg.hidden = ok;
    input.setAttribute('aria-invalid', String(!ok));
    if (ok) { current = n; paint(); }
  };
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); jump(); } });
  root.querySelector('[data-go]').addEventListener('click', jump);
  prev.addEventListener('click', () => { if (current > 1) { current--; paint(); } });
  next.addEventListener('click', () => { if (current < total) { current++; paint(); } });
  paint();
})();
```
