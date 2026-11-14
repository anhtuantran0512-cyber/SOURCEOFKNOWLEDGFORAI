---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/data-table-pagination-bar/"
title: "Data Table Pagination Bar"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "The footer bar every admin table grows: record range on the left, page control on the right, both hanging off the same card."
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data Table Pagination Bar
Source: https://codefronts.com/navigation/css-pagination/data-table-pagination-bar/

The footer bar every admin table grows: record range on the left, page control on the right, both hanging off the same card. Paging is pure CSS — hidden radios plus a :has() rule hide every row whose data-page does not match — so arrow-key traversal comes free and the state survives a repaint.
## HTML
```html
<section class="pgn-10" aria-label="Data Table / Admin Dashboard Pagination Bar demo">
  <div class="pgn-10__stage">
    <input class="pgn-10__radio" type="radio" name="pgn-10" id="pgn-10-p1" checked>
    <input class="pgn-10__radio" type="radio" name="pgn-10" id="pgn-10-p2">
    <input class="pgn-10__radio" type="radio" name="pgn-10" id="pgn-10-p3">

    <header class="pgn-10__head">
      <div>
        <h2 class="pgn-10__title">Invoices</h2>
        <p class="pgn-10__sub">Server-side paging, 3 pages · 9 records</p>
      </div>
      <span class="pgn-10__pill">Live</span>
    </header>

    <div class="pgn-10__tablewrap">
      <table class="pgn-10__table">
        <caption class="pgn-10__caption">Invoice ledger, paginated</caption>
        <thead>
          <tr><th scope="col">Invoice</th><th scope="col">Client</th><th scope="col">Status</th><th scope="col" class="pgn-10__right">Amount</th></tr>
        </thead>
        <tbody>
          <tr data-page="1"><td>INV-2041</td><td>Alex Chen</td><td><span class="pgn-10__tag pgn-10__tag--ok">Paid</span></td><td class="pgn-10__right">$4,280.00</td></tr>
          <tr data-page="1"><td>INV-2040</td><td>Priya Sharma</td><td><span class="pgn-10__tag">Pending</span></td><td class="pgn-10__right">$1,150.00</td></tr>
          <tr data-page="1"><td>INV-2039</td><td>Jordan Lee</td><td><span class="pgn-10__tag pgn-10__tag--ok">Paid</span></td><td class="pgn-10__right">$860.00</td></tr>
          <tr data-page="2"><td>INV-2038</td><td>Sam Rivera</td><td><span class="pgn-10__tag pgn-10__tag--due">Overdue</span></td><td class="pgn-10__right">$2,940.00</td></tr>
          <tr data-page="2"><td>INV-2037</td><td>Alex Chen</td><td><span class="pgn-10__tag pgn-10__tag--ok">Paid</span></td><td class="pgn-10__right">$515.00</td></tr>
          <tr data-page="2"><td>INV-2036</td><td>Priya Sharma</td><td><span class="pgn-10__tag">Pending</span></td><td class="pgn-10__right">$7,320.00</td></tr>
          <tr data-page="3"><td>INV-2035</td><td>Jordan Lee</td><td><span class="pgn-10__tag pgn-10__tag--ok">Paid</span></td><td class="pgn-10__right">$1,995.00</td></tr>
          <tr data-page="3"><td>INV-2034</td><td>Sam Rivera</td><td><span class="pgn-10__tag pgn-10__tag--ok">Paid</span></td><td class="pgn-10__right">$430.00</td></tr>
          <tr data-page="3"><td>INV-2033</td><td>Alex Chen</td><td><span class="pgn-10__tag pgn-10__tag--due">Overdue</span></td><td class="pgn-10__right">$12,600.00</td></tr>
        </tbody>
      </table>
    </div>

    <div class="pgn-10__bar">
      <p class="pgn-10__range"><span class="pgn-10__r1">1–3</span><span class="pgn-10__r2">4–6</span><span class="pgn-10__r3">7–9</span> of 9 records</p>
      <nav class="pgn-10__nav" aria-label="Table pagination">
        <ol class="pgn-10__list">
          <li><label class="pgn-10__page" for="pgn-10-p1">1</label></li>
          <li><label class="pgn-10__page" for="pgn-10-p2">2</label></li>
          <li><label class="pgn-10__page" for="pgn-10-p3">3</label></li>
        </ol>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.pgn-10 {
  --bg: #f7f7f8;
  --surface: #ffffff;
  --surface-2: #f4f4f5;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #18181b;
  --acc-fg: #ffffff;
  --ring: #6366f1;
  --ok: #15803d;
  --due: #b91c1c;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-10 {
    --bg: oklch(97.5% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96.5% .003 286);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(22% .008 286);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
    --ok: oklch(52% .13 150);
    --due: oklch(53% .2 27);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-10:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --surface-2: #1c1c20;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #fafafa;
    --acc-fg: #09090b;
    --ring: #818cf8;
    --ok: #4ade80;
    --due: #f87171;
  }
}

.pgn-10[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --surface-2: #1c1c20;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
  --ok: #4ade80;
  --due: #f87171;
}

.pgn-10 {
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

.pgn-10,
.pgn-10 *,
.pgn-10 *::before,
.pgn-10 *::after {
  box-sizing: border-box;
}

.pgn-10__stage {
  width: 100%;
  max-width: 56rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
  overflow: hidden;
}

.pgn-10__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.pgn-10__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1.25rem 1.35rem;
}

.pgn-10__title {
  margin: 0 0 .25rem;
  font-size: 1.125rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.pgn-10__sub {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
}

.pgn-10__pill {
  padding: .3rem .6rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  font-size: .6875rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-10__tablewrap {
  overflow-x: auto;
  border-block: 1px solid var(--line);
}

.pgn-10__table {
  width: 100%;
  border-collapse: collapse;
  font-size: .875rem;
}

.pgn-10__caption {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.pgn-10__table th {
  padding: .7rem 1.35rem;
  text-align: left;
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  background: var(--surface-2);
  white-space: nowrap;
}

.pgn-10__table td {
  padding: .95rem 1.35rem;
  border-top: 1px solid var(--line);
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.pgn-10__right {
  text-align: right;
}

.pgn-10__tag {
  display: inline-block;
  padding: .2rem .55rem;
  border-radius: .375rem;
  background: var(--surface-2);
  font-size: .75rem;
  color: var(--muted);
}

.pgn-10__tag--ok {
  color: var(--ok);
  background: color-mix(in oklab,var(--ok) 14%,transparent);
}

.pgn-10__tag--due {
  color: var(--due);
  background: color-mix(in oklab,var(--due) 14%,transparent);
}

.pgn-10__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .9rem 1.35rem;
}

.pgn-10__range {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pgn-10__list {
  display: flex;
  gap: .3rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-10__page {
  display: grid;
  place-items: center;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .5rem;
  border: 1px solid var(--line);
  border-radius: .5rem;
  background: var(--surface);
  font-size: .875rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .16s ease, border-color .16s ease;
}

.pgn-10__page:hover {
  background: var(--surface-2);
}

#pgn-10-p1:focus-visible ~ .pgn-10__bar [for="pgn-10-p1"],
#pgn-10-p2:focus-visible ~ .pgn-10__bar [for="pgn-10-p2"],
#pgn-10-p3:focus-visible ~ .pgn-10__bar [for="pgn-10-p3"] {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-10:has(#pgn-10-p1:checked) tbody tr:not([data-page="1"]),
.pgn-10:has(#pgn-10-p2:checked) tbody tr:not([data-page="2"]),
.pgn-10:has(#pgn-10-p3:checked) tbody tr:not([data-page="3"]) {
  display: none;
}

.pgn-10:has(#pgn-10-p1:checked) [for="pgn-10-p1"],
.pgn-10:has(#pgn-10-p2:checked) [for="pgn-10-p2"],
.pgn-10:has(#pgn-10-p3:checked) [for="pgn-10-p3"] {
  background: var(--acc);
  border-color: transparent;
  color: var(--acc-fg);
}

.pgn-10__r1,
.pgn-10__r2,
.pgn-10__r3 {
  display: none;
}

.pgn-10:has(#pgn-10-p1:checked) .pgn-10__r1,
.pgn-10:has(#pgn-10-p2:checked) .pgn-10__r2,
.pgn-10:has(#pgn-10-p3:checked) .pgn-10__r3 {
  display: inline;
}

@media (prefers-reduced-motion: reduce) {
  .pgn-10 * {
    animation: none !important;
    transition: none !important;
  }
}
```
