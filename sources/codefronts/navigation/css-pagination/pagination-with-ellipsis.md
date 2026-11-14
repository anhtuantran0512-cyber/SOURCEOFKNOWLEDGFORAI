---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/pagination-with-ellipsis/"
title: "Pagination with Ellipsis"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "Twenty-four page buttons in a row is unusable, so this one renders a sliding window — first, a three-page neighbourhood around the current page, last, and an…"
has_js: "true"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pagination with Ellipsis
Source: https://codefronts.com/navigation/css-pagination/pagination-with-ellipsis/

Twenty-four page buttons in a row is unusable, so this one renders a sliding window — first, a three-page neighbourhood around the current page, last, and an ellipsis wherever the sequence actually skips. Under forty lines of dependency-free JavaScript, with disabled edges, a live-announced status line and ellipsis nodes that stay out of the tab order.
## HTML
```html
<section class="pgn-02" aria-label="Pagination with Ellipsis for Large Page Ranges demo">
  <div class="pgn-02__stage">
    <header class="pgn-02__head">
      <p class="pgn-02__eyebrow">24 pages · 1,152 records</p>
      <h2 class="pgn-02__title">Windowed page list with ellipsis gaps</h2>
    </header>

    <nav class="pgn-02__nav" aria-label="Pagination">
      <button class="pgn-02__edge" type="button" data-prev aria-label="Previous page">
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span>Prev</span>
      </button>
      <ol class="pgn-02__list" data-list></ol>
      <button class="pgn-02__edge" type="button" data-next aria-label="Next page">
        <span>Next</span>
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </nav>

    <p class="pgn-02__status" role="status" aria-live="polite" data-status>Page 7 of 24</p>
  </div>
</section>
```
## CSS
```css
.pgn-02 {
  --bg: #fafafa;
  --surface: #ffffff;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #4338ca;
  --acc-fg: #ffffff;
  --ring: #6366f1;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-02 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(48% .18 277);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-02:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #6366f1;
    --acc-fg: #ffffff;
    --ring: #818cf8;
  }
}

.pgn-02[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #6366f1;
  --acc-fg: #ffffff;
  --ring: #818cf8;
}

.pgn-02 {
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

.pgn-02,
.pgn-02 *,
.pgn-02 *::before,
.pgn-02 *::after {
  box-sizing: border-box;
}

.pgn-02__stage {
  width: 100%;
  max-width: 46rem;
  display: grid;
  gap: 1.75rem;
  justify-items: center;
  text-align: center;
}

.pgn-02__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pgn-02__title {
  margin: 0;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.pgn-02__nav {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  padding: .5rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
}

.pgn-02__list {
  display: flex;
  align-items: center;
  gap: .25rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-02__num,
.pgn-02__edge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .35rem;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .75rem;
  border: 1px solid transparent;
  border-radius: .625rem;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .16s ease, color .16s ease;
}

.pgn-02__edge {
  color: var(--muted);
}

.pgn-02__num:hover,
.pgn-02__edge:not(:disabled):hover {
  background: color-mix(in oklab,var(--text) 7%,transparent);
}

.pgn-02__num:focus-visible,
.pgn-02__edge:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-02__num[aria-current="page"] {
  background: var(--acc);
  color: var(--acc-fg);
}

.pgn-02__edge:disabled {
  opacity: .38;
  cursor: not-allowed;
}

.pgn-02__edge svg {
  width: 1.125rem;
  height: 1.125rem;
}

.pgn-02__gap {
  display: grid;
  place-items: end center;
  min-width: 1.75rem;
  height: 2.75rem;
  padding-bottom: .55rem;
  color: var(--muted);
  letter-spacing: .1em;
}

.pgn-02__status {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

@media (max-width: 34rem) {
  .pgn-02__edge span {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip-path: inset(50%);
  }

  .pgn-02__edge {
    padding: 0;
    min-width: 2.75rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pgn-02 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.pgn-02');
  if (!root) return;
  const list = root.querySelector('[data-list]');
  const prev = root.querySelector('[data-prev]');
  const next = root.querySelector('[data-next]');
  const status = root.querySelector('[data-status]');
  const total = 24;
  let current = 7;
  const window_ = (c) => {
    const start = Math.max(2, c - 1), end = Math.min(total - 1, c + 1), out = [1];
    if (start > 2) out.push('gap');
    for (let i = start; i <= end; i++) out.push(i);
    if (end < total - 1) out.push('gap');
    out.push(total);
    return out;
  };
  const render = () => {
    list.replaceChildren(...window_(current).map((p) => {
      const li = document.createElement('li');
      if (p === 'gap') { li.className = 'pgn-02__gap'; li.ariaHidden = 'true'; li.textContent = '…'; return li; }
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'pgn-02__num'; b.textContent = p;
      b.setAttribute('aria-label', 'Go to page ' + p);
      if (p === current) b.setAttribute('aria-current', 'page');
      b.addEventListener('click', () => { current = p; render(); });
      li.append(b); return li;
    }));
    prev.disabled = current === 1; next.disabled = current === total;
    status.textContent = 'Page ' + current + ' of ' + total;
  };
  prev.addEventListener('click', () => { if (current > 1) { current--; render(); } });
  next.addEventListener('click', () => { if (current < total) { current++; render(); } });
  render();
})();
```
