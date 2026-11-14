---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/empty-data-table-no-rows-state/"
title: "Empty Data Table / No Rows State"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "The empty table done properly: real column headers stay, a single colspan cell carries the message, and ghost rows fade in behind it so the grid still reads…"
has_js: "true"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Empty Data Table / No Rows State
Source: https://codefronts.com/snippets/css-empty-states/empty-data-table-no-rows-state/

The empty table done properly: real column headers stay, a single colspan cell carries the message, and ghost rows fade in behind it so the grid still reads as a table rather than a hole. New invoice adds a genuine draft row and updates the footer count, so the demo covers the transition out of empty as well as the state itself.
## HTML
```html
<div class="est-05">
  <div class="est-05__page">
    <header class="est-05__phead">
      <div class="est-05__ptitle">
        <span class="est-05__crumbs">Billing<span aria-hidden="true">/</span>Invoices</span>
        <h1 class="est-05__h1">Invoices</h1>
      </div>
      <div class="est-05__phacts">
        <button class="est-05__ghost" type="button">Export</button>
        <button class="est-05__pri" type="button" id="est-05-new">New invoice</button>
      </div>
    </header>

    <div class="est-05__toolbar">
      <div class="est-05__seg" role="group" aria-label="Status">
        <button class="est-05__segb est-05__segb--on" type="button">Unpaid</button>
        <button class="est-05__segb" type="button">Paid</button>
        <button class="est-05__segb" type="button">Draft</button>
        <button class="est-05__segb" type="button">Void</button>
      </div>
      <label class="est-05__search">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.2" stroke="currentColor" stroke-width="1.7"/><path d="m15.8 15.8 3.6 3.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <input type="search" placeholder="Client, number or amount" aria-label="Search invoices">
      </label>
    </div>

    <div class="est-05__tablewrap">
      <table class="est-05__table">
        <thead>
          <tr>
            <th scope="col" class="est-05__thnum">Number</th>
            <th scope="col">Client</th>
            <th scope="col">Issued</th>
            <th scope="col">Due</th>
            <th scope="col" class="est-05__thr">Amount</th>
            <th scope="col">Status</th>
          </tr>
        </thead>
        <tbody id="est-05-body">
          <tr class="est-05__emptyrow">
            <td colspan="6">
              <div class="est-05__ghosts" aria-hidden="true">
                <span></span><span></span><span></span><span></span><span></span>
              </div>
              <div class="est-05__empty">
                <span class="est-05__glyph" aria-hidden="true">
                  <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 3.5h9l3.5 3.5v13.5H6z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M14.6 3.8V7.4h3.6M9 12h6M9 15.5h4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
                </span>
                <p class="est-05__eh">Nothing unpaid</p>
                <p class="est-05__ep">Every invoice issued this quarter has cleared. Drafts stay here until you send them.</p>
                <div class="est-05__eacts">
                  <button class="est-05__pri est-05__pri--sm" type="button" id="est-05-new2">New invoice</button>
                  <button class="est-05__ghost est-05__ghost--sm" type="button">Import from CSV</button>
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <footer class="est-05__pfoot">
      <span class="est-05__pinfo" id="est-05-info">No rows</span>
      <div class="est-05__pager">
        <button class="est-05__pbtn" type="button" disabled aria-label="Previous page">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="m14 7-5 5 5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <button class="est-05__pbtn" type="button" disabled aria-label="Next page">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="m10 7 5 5-5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
    </footer>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap');

.est-05 {
  --bg: #fbfbfc;
  --surface: #ffffff;
  --sunk: #f4f5f7;
  --line: #e6e8ec;
  --line-2: #d5d8de;
  --ink: #14161b;
  --muted: #5a5f6a;
  --faint: #8b909a;
  --accent: #1f3d7a;
  --ok: #2c6a4f;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-05 *,
.est-05 *::before,
.est-05 *::after {
  box-sizing: border-box;
}

.est-05 [hidden] {
  display: none !important;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-05 {
    --bg: oklch(0.988 0.002 265);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.968 0.004 265);
    --line: oklch(0.923 0.006 265);
    --line-2: oklch(0.872 0.008 265);
    --ink: oklch(0.175 0.01 265);
    --muted: oklch(0.465 0.012 265);
    --faint: oklch(0.63 0.013 265);
    --accent: oklch(0.38 0.095 262);
    --ok: oklch(0.48 0.08 155);
  }
}

.est-05__page {
  inline-size: min(76rem,100%);
  justify-self: center;
  padding: clamp(1.25rem,4vw,3rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: 1.15rem;
  align-content: start;
}

.est-05__phead {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: flex-end;
  justify-content: space-between;
}

.est-05__crumbs {
  display: flex;
  gap: .4rem;
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .7rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--faint);
}

.est-05__h1 {
  margin: .35rem 0 0;
  font-size: clamp(1.5rem,3.4vw,2.1rem);
  font-weight: 600;
  letter-spacing: -.035em;
  line-height: 1;
}

.est-05__phacts {
  display: flex;
  gap: .5rem;
}

.est-05__pri {
  min-block-size: 2.6rem;
  padding: .6rem 1rem;
  font: inherit;
  font-size: .86rem;
  font-weight: 500;
  cursor: pointer;
  color: #fff;
  background: var(--accent);
  border: 1px solid transparent;
  border-radius: 9px;
  box-shadow: 0 6px 14px -10px color-mix(in oklab, var(--accent) 80%, transparent);
  transition: translate .16s, background .16s;
}

.est-05__pri:hover {
  translate: 0 -1px;
  background: color-mix(in oklab, var(--accent) 88%, #000);
}

.est-05__ghost {
  min-block-size: 2.6rem;
  padding: .6rem 1rem;
  font: inherit;
  font-size: .86rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 9px;
  transition: background .16s;
}

.est-05__ghost:hover {
  background: var(--sunk);
}

.est-05__pri--sm,
.est-05__ghost--sm {
  min-block-size: 2.4rem;
  padding: .5rem .85rem;
  font-size: .82rem;
}

.est-05__toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem 1rem;
  align-items: center;
  justify-content: space-between;
}

.est-05__seg {
  display: flex;
  padding: .2rem;
  background: var(--sunk);
  border: 1px solid var(--line);
  border-radius: 10px;
}

.est-05__segb {
  padding: .42rem .75rem;
  font: inherit;
  font-size: .82rem;
  font-weight: 500;
  cursor: pointer;
  color: var(--muted);
  background: transparent;
  border: 0;
  border-radius: 7px;
  transition: color .16s, background .16s;
}

.est-05__segb:hover {
  color: var(--ink);
}

.est-05__segb--on {
  color: var(--ink);
  background: var(--surface);
  box-shadow: 0 1px 2px rgba(20,22,27,.08);
}

.est-05__search {
  display: flex;
  align-items: center;
  gap: .5rem;
  flex: 1 1 16rem;
  max-inline-size: 22rem;
  padding: .5rem .7rem;
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 9px;
}

.est-05__search svg {
  inline-size: 1rem;
  block-size: 1rem;
  color: var(--faint);
  flex: none;
}

.est-05__search input {
  flex: 1 1 auto;
  min-inline-size: 0;
  font: inherit;
  font-size: .85rem;
  color: var(--ink);
  background: none;
  border: 0;
  outline: none;
}

.est-05__search:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--accent) 12%, transparent);
}

.est-05__tablewrap {
  overflow: auto;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: 0 1px 2px rgba(20,22,27,.04);
}

.est-05__table {
  inline-size: 100%;
  border-collapse: separate;
  border-spacing: 0;
  min-inline-size: 44rem;
}

.est-05__table th {
  position: sticky;
  inset-block-start: 0;
  z-index: 1;
  text-align: start;
  padding: .7rem 1rem;
  background: var(--sunk);
  border-block-end: 1px solid var(--line);
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .68rem;
  font-weight: 500;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--faint);
  white-space: nowrap;
}

.est-05__thr {
  text-align: end;
}

.est-05__thnum {
  inline-size: 8rem;
}

.est-05__emptyrow td {
  position: relative;
  padding: 0;
}

.est-05__ghosts {
  position: absolute;
  inset: 0;
  display: grid;
  grid-auto-rows: 3.25rem;
  overflow: hidden;
  mask-image: linear-gradient(180deg,#000,transparent 85%);
}

.est-05__ghosts span {
  border-block-end: 1px solid var(--line);
  position: relative;
}

.est-05__ghosts span::before {
  content: '';
  position: absolute;
  inset-block-start: 1.35rem;
  inset-inline-start: 1rem;
  block-size: .55rem;
  inline-size: min(38%,14rem);
  border-radius: 3px;
  background: linear-gradient(90deg,var(--sunk),color-mix(in oklab,var(--line) 70%,transparent),var(--sunk));
  background-size: 200% 100%;
  animation: est-05-shim 4.5s linear infinite;
}

.est-05__ghosts span:nth-child(even)::before {
  inline-size: min(26%,10rem);
  animation-delay: .6s;
}

@keyframes est-05-shim {
  to {
    background-position: -200% 0;
  }
}

.est-05__empty {
  position: relative;
  z-index: 1;
  display: grid;
  justify-items: center;
  text-align: center;
  gap: .4rem;
  padding: clamp(2.5rem,9vh,5rem) 1.25rem clamp(2rem,7vh,4rem);
  animation: est-05-in .5s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-05-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-05__glyph {
  inline-size: 3.5rem;
  block-size: 3.5rem;
  display: grid;
  place-items: center;
  margin-block-end: .55rem;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 7%, var(--surface));
  border: 1px solid color-mix(in oklab, var(--accent) 18%, var(--line));
  border-radius: 12px;
}

.est-05__glyph svg {
  inline-size: 1.5rem;
  block-size: 1.5rem;
}

.est-05__eh {
  margin: 0;
  font-size: 1.08rem;
  font-weight: 600;
  letter-spacing: -.022em;
}

.est-05__ep {
  margin: 0;
  max-inline-size: 40ch;
  font-size: .88rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.est-05__eacts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  margin-block-start: .85rem;
}

.est-05__row td {
  padding: .85rem 1rem;
  border-block-end: 1px solid var(--line);
  font-size: .87rem;
  vertical-align: middle;
}

.est-05__row:last-child td {
  border-block-end: 0;
}

.est-05__row:hover td {
  background: var(--sunk);
}

.est-05__num {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .8rem;
  color: var(--muted);
}

.est-05__amt {
  text-align: end;
  font-variant-numeric: tabular-nums;
}

.est-05__st {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  padding: .2rem .5rem;
  font-size: .74rem;
  border-radius: 6px;
  background: var(--sunk);
  border: 1px solid var(--line);
  color: var(--muted);
  white-space: nowrap;
}

.est-05__st i {
  inline-size: .4rem;
  block-size: .4rem;
  border-radius: 50%;
  background: var(--faint);
}

.est-05__st--draft i {
  background: #b4813f;
}

.est-05__pfoot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.est-05__pinfo {
  font-family: 'Geist Mono',ui-monospace,monospace;
  font-size: .72rem;
  letter-spacing: .02em;
  color: var(--faint);
}

.est-05__pager {
  display: flex;
  gap: .35rem;
}

.est-05__pbtn {
  inline-size: 2.2rem;
  block-size: 2.2rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  color: var(--muted);
  background: var(--surface);
  border: 1px solid var(--line-2);
  border-radius: 8px;
}

.est-05__pbtn svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.est-05__pbtn:disabled {
  opacity: .45;
  cursor: not-allowed;
}

.est-05__pri:focus-visible,
.est-05__ghost:focus-visible,
.est-05__segb:focus-visible,
.est-05__pbtn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .est-05 *,
    .est-05 *::before,
    .est-05 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-05__tablewrap,
    .est-05__glyph,
    .est-05__pri {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.est-05'); if(!root) return;
  var body = root.querySelector('#est-05-body'), info = root.querySelector('#est-05-info');
  var emptyRow = body.querySelector('.est-05__emptyrow');
  var seq = 0;
  var clients = [['Meridian Studio','2 400.00'],['Harbour Foods','980.00'],['Ottoline Press','1 150.00']];
  function addRow(){
    var c = clients[seq % clients.length]; seq++;
    var tr = document.createElement('tr');
    tr.className = 'est-05__row';
    tr.innerHTML = '<td class="est-05__num">INV-20' + (26 + seq) + '-' + (104 + seq) + '</td>' +
      '<td>' + c[0] + '</td><td>Today</td><td>In 30 days</td>' +
      '<td class="est-05__amt">' + c[1] + '</td>' +
      '<td><span class="est-05__st est-05__st--draft"><i></i>Draft</span></td>';
    emptyRow.hidden = true;
    body.appendChild(tr);
    info.textContent = seq + (seq === 1 ? ' draft row' : ' draft rows');
  }
  root.querySelectorAll('#est-05-new, #est-05-new2').forEach(function(b){ b.addEventListener('click', addRow); });
})();
```
