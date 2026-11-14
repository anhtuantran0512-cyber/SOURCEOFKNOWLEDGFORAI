---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/invoice-history-table-downloads/"
title: "Invoice History Table with Downloads"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A polished billing-history table with status filter chips (pure CSS via :has), row selection with a live 'N selected' count from CSS counters, a select-all…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Invoice History Table with Downloads
Source: https://codefronts.com/layouts/css-settings-pages/invoice-history-table-downloads/

A polished billing-history table with status filter chips (pure CSS via :has), row selection with a live 'N selected' count from CSS counters, a select-all checkbox with a true indeterminate state, and per-row PDF download buttons that animate through idle → preparing → downloaded. Under 640px the table reflows into stacked invoice cards with a container query — no duplicate markup.
## HTML
```html
<section class="csp-04">
  <div class="csp-04__wrap">
    <header class="csp-04__head">
      <div><h1>Invoices</h1><p>Download receipts for your records or your accounts team.</p></div>
      <p class="csp-04__total"><span>Paid in 2026</span><b>$1,920.00</b></p>
    </header>

    <div class="csp-04__toolbar">
      <fieldset class="csp-04__chips">
        <legend class="csp-04__sr">Filter by status</legend>
        <input type="radio" name="csp04-f" id="csp04-all" checked><label for="csp04-all">All</label>
        <input type="radio" name="csp04-f" id="csp04-paid"><label for="csp04-paid">Paid</label>
        <input type="radio" name="csp04-f" id="csp04-due"><label for="csp04-due">Due</label>
        <input type="radio" name="csp04-f" id="csp04-refunded"><label for="csp04-refunded">Refunded</label>
      </fieldset>
      <div class="csp-04__bulk" aria-live="polite"><button type="button" class="csp-04__btn" data-bulk>Download selected</button></div>
    </div>

    <div class="csp-04__card">
      <table class="csp-04__table">
        <thead>
          <tr><th class="csp-04__chk"><input type="checkbox" data-all aria-label="Select all invoices"></th><th>Invoice</th><th>Date</th><th>Plan</th><th>Status</th><th class="csp-04__num">Amount</th><th><span class="csp-04__sr">Download</span></th></tr>
        </thead>
        <tbody>
          <tr data-status="due"><td class="csp-04__chk"><input type="checkbox" aria-label="Select INV-2026-010"></td><td data-label="Invoice"><b>INV-2026-010</b></td><td data-label="Date">Oct 14, 2026</td><td data-label="Plan">Pro · 8 seats</td><td data-label="Status"><span class="csp-04__status" data-s="due">Due</span></td><td data-label="Amount" class="csp-04__num">$192.00</td><td><button type="button" class="csp-04__dl" data-dl="INV-2026-010" aria-label="Download invoice INV-2026-010"><span>PDF</span></button></td></tr>
          <tr data-status="paid"><td class="csp-04__chk"><input type="checkbox" aria-label="Select INV-2026-009"></td><td data-label="Invoice"><b>INV-2026-009</b></td><td data-label="Date">Sep 14, 2026</td><td data-label="Plan">Pro · 8 seats</td><td data-label="Status"><span class="csp-04__status" data-s="paid">Paid</span></td><td data-label="Amount" class="csp-04__num">$192.00</td><td><button type="button" class="csp-04__dl" data-dl="INV-2026-009" aria-label="Download invoice INV-2026-009"><span>PDF</span></button></td></tr>
          <tr data-status="paid"><td class="csp-04__chk"><input type="checkbox" aria-label="Select INV-2026-008"></td><td data-label="Invoice"><b>INV-2026-008</b></td><td data-label="Date">Aug 14, 2026</td><td data-label="Plan">Pro · 8 seats</td><td data-label="Status"><span class="csp-04__status" data-s="paid">Paid</span></td><td data-label="Amount" class="csp-04__num">$192.00</td><td><button type="button" class="csp-04__dl" data-dl="INV-2026-008" aria-label="Download invoice INV-2026-008"><span>PDF</span></button></td></tr>
          <tr data-status="refunded"><td class="csp-04__chk"><input type="checkbox" aria-label="Select INV-2026-007"></td><td data-label="Invoice"><b>INV-2026-007</b></td><td data-label="Date">Jul 22, 2026</td><td data-label="Plan">Seat add-on · 2</td><td data-label="Status"><span class="csp-04__status" data-s="refunded">Refunded</span></td><td data-label="Amount" class="csp-04__num">−$48.00</td><td><button type="button" class="csp-04__dl" data-dl="INV-2026-007" aria-label="Download invoice INV-2026-007"><span>PDF</span></button></td></tr>
          <tr data-status="paid"><td class="csp-04__chk"><input type="checkbox" aria-label="Select INV-2026-006"></td><td data-label="Invoice"><b>INV-2026-006</b></td><td data-label="Date">Jul 14, 2026</td><td data-label="Plan">Pro · 6 seats</td><td data-label="Status"><span class="csp-04__status" data-s="paid">Paid</span></td><td data-label="Amount" class="csp-04__num">$144.00</td><td><button type="button" class="csp-04__dl" data-dl="INV-2026-006" aria-label="Download invoice INV-2026-006"><span>PDF</span></button></td></tr>
          <tr data-status="paid"><td class="csp-04__chk"><input type="checkbox" aria-label="Select INV-2026-005"></td><td data-label="Invoice"><b>INV-2026-005</b></td><td data-label="Date">Jun 14, 2026</td><td data-label="Plan">Pro · 6 seats</td><td data-label="Status"><span class="csp-04__status" data-s="paid">Paid</span></td><td data-label="Amount" class="csp-04__num">$144.00</td><td><button type="button" class="csp-04__dl" data-dl="INV-2026-005" aria-label="Download invoice INV-2026-005"><span>PDF</span></button></td></tr>
        </tbody>
      </table>
      <p class="csp-04__empty">No invoices match this filter.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.csp-04,
.csp-04 *,
.csp-04 *::before,
.csp-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-04 {
  --bg: oklch(0.98 0.004 85);
  --surface: #fff;
  --ink: oklch(0.23 0.015 60);
  --muted: oklch(0.52 0.015 60);
  --line: oklch(0.92 0.008 80);
  --accent: oklch(0.5 0.15 250);
  color-scheme: light;
  container-type: inline-size;
  counter-reset: csp04-sel;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 24px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: var(--bg);
  color: var(--ink);
  accent-color: var(--accent);
  width: 100%;
}

.csp-04__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.csp-04__wrap {
  max-width: 980px;
  margin-inline: auto;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.csp-04__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px;
}

.csp-04__head h1 {
  font: 700 30px/1.1 system-ui,sans-serif;
  letter-spacing: -.025em;
}

.csp-04__head p {
  font: 400 14.5px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-04__total {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.csp-04__total span {
  font: 600 11px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.csp-04__total b {
  font: 700 24px/1 system-ui,sans-serif;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.02em;
}

.csp-04__toolbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 44px;
}

.csp-04__chips {
  border: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.csp-04__chips input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.csp-04__chips label {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  padding: 0 14px;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--surface);
  font: 550 13.5px/1 system-ui,sans-serif;
  color: var(--muted);
  cursor: pointer;
  transition: all .15s;
}

.csp-04__chips label:hover {
  color: var(--ink);
  border-color: oklch(0.85 0.01 80);
}

.csp-04__chips input:checked+label {
  color: #fff;
  background: var(--ink);
  border-color: var(--ink);
}

.csp-04__chips input:focus-visible+label {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-04__bulk {
  display: flex;
  align-items: center;
  gap: 12px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: var(--muted);
  opacity: 0;
  translate: 0 4px;
  pointer-events: none;
  transition: opacity .2s,translate .2s;
}

.csp-04__bulk::before {
  content: counter(csp04-sel) " selected";
}

.csp-04:has(tbody input:checked) .csp-04__bulk {
  opacity: 1;
  translate: 0 0;
  pointer-events: auto;
}

.csp-04__btn {
  min-height: 40px;
  padding: 0 14px;
  border: 0;
  border-radius: 10px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: #fff;
  background: var(--accent);
  cursor: pointer;
}

.csp-04__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-04__card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 1px 2px oklch(0 0 0/.03),0 12px 32px -24px oklch(0.3 0.03 60/.3);
}

.csp-04__table {
  width: 100%;
  border-collapse: collapse;
  font: 400 14px/1.4 system-ui,sans-serif;
}

.csp-04__table th {
  padding: 12px 16px;
  text-align: left;
  font: 600 12px/1 system-ui,sans-serif;
  letter-spacing: .02em;
  color: var(--muted);
  background: oklch(0.985 0.004 85);
  border-bottom: 1px solid var(--line);
}

.csp-04__table td {
  padding: 14px 16px;
  border-bottom: 1px solid var(--line);
  white-space: nowrap;
}

.csp-04__table tbody tr {
  transition: background .15s;
}

.csp-04__table tbody tr:hover {
  background: oklch(0.985 0.006 85);
}

.csp-04__table tbody tr:has(input:checked) {
  background: oklch(0.97 0.02 250);
}

.csp-04__table tbody tr:last-child td {
  border-bottom: 0;
}

.csp-04__table td b {
  font-weight: 600;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
}

.csp-04 tbody input:checked {
  counter-increment: csp04-sel;
}

.csp-04__chk {
  width: 48px;
}

.csp-04__chk input {
  width: 18px;
  height: 18px;
  cursor: pointer;
  vertical-align: middle;
}

.csp-04__num {
  text-align: right!important;
  font-variant-numeric: tabular-nums;
  font-weight: 600;
}

.csp-04__status {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 999px;
  font: 600 12px/1 system-ui,sans-serif;
}

.csp-04__status::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}

.csp-04__status[data-s="paid"] {
  color: oklch(0.45 0.12 155);
  background: oklch(0.95 0.04 155);
}

.csp-04__status[data-s="due"] {
  color: oklch(0.5 0.13 65);
  background: oklch(0.96 0.05 85);
}

.csp-04__status[data-s="refunded"] {
  color: var(--muted);
  background: oklch(0.95 0.005 80);
}

.csp-04__dl {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-width: 76px;
  min-height: 36px;
  padding: 0 12px;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: var(--surface);
  font: 600 12.5px/1 system-ui,sans-serif;
  color: var(--ink);
  cursor: pointer;
  transition: background .15s,border-color .15s,color .15s;
}

.csp-04__dl::before {
  content: "";
  width: 14px;
  height: 14px;
  background: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M8 2v8m0 0L5 7m3 3 3-3M3 13h10' fill='none' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M8 2v8m0 0L5 7m3 3 3-3M3 13h10' fill='none' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat;
}

.csp-04__dl:hover {
  border-color: var(--ink);
}

.csp-04__dl:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-04__dl[data-state="loading"]::before {
  -webkit-mask: none;
  mask: none;
  background: none;
  border: 2px solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  width: 12px;
  height: 12px;
  animation: csp04-spin .7s linear infinite;
}

.csp-04__dl[data-state="done"] {
  color: oklch(0.45 0.12 155);
  border-color: oklch(0.85 0.06 155);
  background: oklch(0.97 0.03 155);
}

.csp-04__dl[data-state="done"]::before {
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='m3.5 8.5 3 3 6-7' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
  mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='m3.5 8.5 3 3 6-7' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
}

.csp-04__empty {
  display: none;
  padding: 40px 16px;
  text-align: center;
  font: 500 14px/1.4 system-ui,sans-serif;
  color: var(--muted);
}

.csp-04:has(#csp04-paid:checked) tbody tr:not([data-status="paid"]),
.csp-04:has(#csp04-due:checked) tbody tr:not([data-status="due"]),
.csp-04:has(#csp04-refunded:checked) tbody tr:not([data-status="refunded"]) {
  display: none;
}

@keyframes csp04-spin {
  to {
    rotate: 1turn;
  }
}

@container (max-width: 640px) {
  .csp-04__table thead {
    display: none;
  }

  .csp-04__table,
    .csp-04__table tbody {
    display: block;
  }

  .csp-04__table tbody tr {
    display: grid;
    grid-template-columns: auto 1fr auto;
    gap: 6px 12px;
    padding: 16px;
    border-bottom: 1px solid var(--line);
  }

  .csp-04__table td {
    padding: 0;
    border: 0;
    white-space: normal;
  }

  .csp-04__table td.csp-04__chk {
    grid-row: span 3;
    width: auto;
  }

  .csp-04__table td[data-label="Invoice"] {
    grid-column: 2;
  }

  .csp-04__table td[data-label="Status"] {
    grid-column: 3;
    grid-row: 1;
  }

  .csp-04__table td[data-label="Date"],
    .csp-04__table td[data-label="Plan"] {
    grid-column: 2;
    color: var(--muted);
    font-size: 13px;
  }

  .csp-04__table td[data-label="Amount"] {
    grid-column: 3;
    grid-row: 2;
  }

  .csp-04__table td:last-child {
    grid-column: 3;
    grid-row: 3;
    justify-self: end;
  }
}

@media (prefers-reduced-motion: reduce) {
  .csp-04 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-04');
  var all = root.querySelector('[data-all]');
  var empty = root.querySelector('.csp-04__empty');
  var visibleBoxes = function () {
    return Array.prototype.filter.call(root.querySelectorAll('tbody input[type=checkbox]'), function (c) { return c.closest('tr').offsetParent !== null; });
  };
  function sync() {
    var boxes = visibleBoxes(), on = boxes.filter(function (c) { return c.checked; }).length;
    all.checked = boxes.length > 0 && on === boxes.length;
    all.indeterminate = on > 0 && on < boxes.length;
    empty.style.display = boxes.length ? 'none' : 'block';
  }
  all.addEventListener('change', function () { visibleBoxes().forEach(function (c) { c.checked = all.checked; }); sync(); });
  root.addEventListener('change', function (e) {
    if (e.target.name === 'csp04-f') root.querySelectorAll('tbody input').forEach(function (c) { c.checked = false; });
    if (e.target !== all) sync();
  });

  function download(id, btn) {
    btn.dataset.state = 'loading';
    btn.querySelector('span').textContent = 'Preparing';
    setTimeout(function () {
      var blob = new Blob(['Invoice ' + id + '\nNorthwind Inc.\nThank you for your business.'], { type: 'text/plain' });
      var url = URL.createObjectURL(blob), a = document.createElement('a');
      a.href = url; a.download = id + '.txt'; document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
      btn.dataset.state = 'done';
      btn.querySelector('span').textContent = 'Saved';
      setTimeout(function () { btn.removeAttribute('data-state'); btn.querySelector('span').textContent = 'PDF'; }, 2400);
    }, 900);
  }
  root.querySelectorAll('[data-dl]').forEach(function (btn) {
    btn.addEventListener('click', function () { if (!btn.dataset.state) download(btn.dataset.dl, btn); });
  });
  root.querySelector('[data-bulk]').addEventListener('click', function () {
    root.querySelectorAll('tbody tr').forEach(function (tr) {
      if (tr.querySelector('input').checked) tr.querySelector('[data-dl]').click();
    });
  });
  sync();
})();
```
