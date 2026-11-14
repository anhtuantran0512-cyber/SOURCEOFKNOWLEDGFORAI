---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-table-state-no-rows-found/"
title: "Tailwind CSS Empty Table State (No Rows Found)"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "An invoices table with no unpaid rows, kept a real <table> throughout: the empty message lives in a single colspan cell, layered over ghost rows so the user…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Empty Table State (No Rows Found)
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-table-state-no-rows-found/

An invoices table with no unpaid rows, kept a real <table> throughout: the empty message lives in a single colspan cell, layered over ghost rows so the user still sees the shape data will take. Add an invoice and the empty row hides itself with has-[[data-row]]: — the table decides when it's empty, not the script.
## HTML
```html
<div class="tes-05 w-full min-h-svh bg-tes05-bg font-tes05-sans text-tes05-ink antialiased">
  <div class="mx-auto grid w-full max-w-6xl gap-6 px-[clamp(1rem,4vw,3rem)] py-[clamp(1.5rem,5vw,3.5rem)]">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div class="grid gap-1">
        <span class="flex gap-1.5 text-xs text-tes05-mut">Billing<span aria-hidden="true">/</span>Invoices</span>
        <h1 class="text-[clamp(1.6rem,3vw,2.1rem)] font-semibold tracking-tight">Invoices</h1>
      </div>
      <div class="flex gap-2">
        <button type="button" class="min-h-11 rounded-lg border border-tes05-line bg-tes05-card px-4 text-sm shadow-xs transition hover:bg-tes05-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes05-acc">Export</button>
        <button type="button" data-new class="inline-flex min-h-11 items-center gap-1.5 rounded-lg bg-tes05-acc px-4 text-sm font-medium text-white shadow-sm transition hover:bg-tes05-acc2 active:scale-[.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes05-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14"/></svg>New invoice</button>
      </div>
    </header>
    <div class="flex flex-wrap items-center justify-between gap-3">
      <div role="group" aria-label="Status" class="flex rounded-xl bg-tes05-sunk p-1">
        <button type="button" aria-pressed="true" class="min-h-10 rounded-lg px-3.5 text-sm text-tes05-mut transition aria-pressed:bg-tes05-card aria-pressed:font-medium aria-pressed:text-tes05-ink aria-pressed:shadow-xs focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes05-acc">Unpaid <span class="font-tes05-mono text-xs">0</span></button>
        <button type="button" aria-pressed="false" class="min-h-10 rounded-lg px-3.5 text-sm text-tes05-mut transition hover:text-tes05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes05-acc">Paid <span class="font-tes05-mono text-xs">48</span></button>
        <button type="button" aria-pressed="false" class="min-h-10 rounded-lg px-3.5 text-sm text-tes05-mut transition hover:text-tes05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes05-acc">Draft</button>
        <button type="button" aria-pressed="false" class="min-h-10 rounded-lg px-3.5 text-sm text-tes05-mut transition hover:text-tes05-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes05-acc">Void</button>
      </div>
      <label class="flex min-h-11 w-full items-center gap-2 rounded-lg border border-tes05-line bg-tes05-card px-3 shadow-xs focus-within:border-tes05-acc focus-within:ring-3 focus-within:ring-tes05-acc/15 sm:w-72">
        <svg class="size-4 flex-none text-tes05-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/></svg>
        <input type="search" placeholder="Client, number or amount" aria-label="Search invoices" class="min-w-0 flex-1 bg-transparent text-sm outline-none placeholder:text-tes05-mut">
      </label>
    </div>
    <div class="overflow-x-auto rounded-2xl border border-tes05-line bg-tes05-card shadow-[0_1px_2px_oklch(0.3_0.02_160/0.05)]">
      <table class="w-full min-w-[40rem] border-collapse text-left text-sm">
        <thead class="border-b border-tes05-line bg-tes05-sunk/60 text-xs text-tes05-mut">
          <tr><th scope="col" class="px-4 py-3 font-medium">Number</th><th scope="col" class="px-4 py-3 font-medium">Client</th><th scope="col" class="px-4 py-3 font-medium">Issued</th><th scope="col" class="px-4 py-3 font-medium">Due</th><th scope="col" class="px-4 py-3 text-right font-medium">Amount</th><th scope="col" class="px-4 py-3 font-medium">Status</th></tr>
        </thead>
        <tbody id="tes05-body" class="divide-y divide-tes05-line">
          <tr class="[tbody:has([data-row])_&amp;]:hidden">
            <td colspan="6" class="p-0">
              <div class="grid">
              <div aria-hidden="true" class="col-start-1 row-start-1 grid content-start gap-px [mask-image:linear-gradient(#000_10%,transparent_90%)]">
                <span class="h-13 border-b border-dashed border-tes05-line bg-[linear-gradient(90deg,var(--color-tes05-sunk)_0_14%,transparent_14%_18%,var(--color-tes05-sunk)_18%_40%,transparent_40%)] bg-size-[100%_10px] bg-center bg-no-repeat"></span>
                <span class="h-13 border-b border-dashed border-tes05-line bg-[linear-gradient(90deg,var(--color-tes05-sunk)_0_12%,transparent_12%_18%,var(--color-tes05-sunk)_18%_34%,transparent_34%)] bg-size-[100%_10px] bg-center bg-no-repeat"></span>
                <span class="h-13 border-b border-dashed border-tes05-line bg-[linear-gradient(90deg,var(--color-tes05-sunk)_0_15%,transparent_15%_18%,var(--color-tes05-sunk)_18%_44%,transparent_44%)] bg-size-[100%_10px] bg-center bg-no-repeat"></span>
                <span class="h-13 border-b border-dashed border-tes05-line"></span>
                <span class="h-13"></span>
              </div>
              <div class="col-start-1 row-start-1 grid place-items-center p-6 sm:p-10">
                <div class="grid max-w-sm justify-items-center rounded-2xl bg-tes05-card/90 px-6 py-5 text-center backdrop-blur-sm">
                  <span aria-hidden="true" class="grid size-13 place-items-center rounded-xl bg-tes05-acc/10 text-tes05-acc ring-1 ring-tes05-acc/20"><svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 3.5h7l4 4V19a1.5 1.5 0 0 1-1.5 1.5h-9.5A1.5 1.5 0 0 1 5.5 19V5A1.5 1.5 0 0 1 7 3.5z"/><path d="m9 13.5 2 2 4-4"/></svg></span>
                  <p class="mt-3.5 text-base font-semibold">Nothing unpaid</p>
                  <p class="mt-1 text-[13px]/5 text-tes05-mut text-pretty">Every invoice issued this quarter has cleared. Drafts stay here until you send them.</p>
                  <div class="mt-4 flex flex-wrap justify-center gap-2">
                    <button type="button" data-new class="min-h-11 rounded-lg bg-tes05-acc px-4 text-sm font-medium text-white transition hover:bg-tes05-acc2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes05-acc">New invoice</button>
                    <button type="button" class="min-h-11 rounded-lg border border-tes05-line px-4 text-sm transition hover:bg-tes05-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes05-acc">Import from CSV</button>
                  </div>
                </div>
              </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <footer class="flex items-center justify-between gap-3 text-xs text-tes05-mut">
      <span id="tes05-info" role="status">No rows</span>
      <div class="flex gap-1">
        <button type="button" disabled aria-label="Previous page" class="grid size-11 place-items-center rounded-lg border border-tes05-line bg-tes05-card disabled:opacity-40"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m14 6-6 6 6 6"/></svg></button>
        <button type="button" disabled aria-label="Next page" class="grid size-11 place-items-center rounded-lg border border-tes05-line bg-tes05-card disabled:opacity-40"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m10 6 6 6-6 6"/></svg></button>
      </div>
    </footer>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes05-bg: #f7f8f7;
  --color-tes05-bg: oklch(0.977 0.003 160);
  --color-tes05-card: #ffffff;
  --color-tes05-card: oklch(1 0 0);
  --color-tes05-sunk: #eff1ef;
  --color-tes05-sunk: oklch(0.953 0.004 160);
  --color-tes05-line: #e1e4e1;
  --color-tes05-line: oklch(0.91 0.006 160);
  --color-tes05-ink: #18201c;
  --color-tes05-ink: oklch(0.22 0.012 160);
  --color-tes05-mut: #58625c;
  --color-tes05-mut: oklch(0.47 0.015 160);
  --color-tes05-acc: #0f7a55;
  --color-tes05-acc: oklch(0.51 0.11 162);
  --color-tes05-acc2: #0b6646;
  --color-tes05-acc2: oklch(0.45 0.1 162);
  --color-tes05-warn: #a8660b;
  --color-tes05-warn: oklch(0.58 0.12 70);
  --font-tes05-sans: 'Geist', system-ui, sans-serif;
  --font-tes05-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-05 {
  width: 100%;
  min-height: 100svh;
}

.tes-05 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-05');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const body = root.querySelector('#tes05-body');
  const info = root.querySelector('#tes05-info');
  const clients = [['Meridian Studio', '2,400.00'], ['Harbour Foods', '980.00'], ['Ottoline Press', '1,150.00']];
  let seq = 0;
  const addRow = () => {
    const c = clients[seq % clients.length];
    seq++;
    const tr = document.createElement('tr');
    tr.setAttribute('data-row', '');
    tr.className = 'transition-colors duration-700 hover:bg-tes05-sunk/50 starting:bg-tes05-acc/15';
    tr.innerHTML = '<td class="px-4 py-3.5 font-tes05-mono text-xs">INV-2026-' + (104 + seq) + '</td>' +
      '<td class="px-4 py-3.5 font-medium">' + c[0] + '</td><td class="px-4 py-3.5 text-tes05-mut">Today</td><td class="px-4 py-3.5 text-tes05-mut">In 30 days</td>' +
      '<td class="px-4 py-3.5 text-right tabular-nums">\u00a3' + c[1] + '</td>' +
      '<td class="px-4 py-3.5"><span class="inline-flex items-center gap-1.5 rounded-full bg-tes05-warn/10 px-2.5 py-1 text-xs font-medium text-tes05-warn"><i class="size-1.5 rounded-full bg-current"></i>Draft</span></td>';
    body.appendChild(tr);
    info.textContent = seq + (seq === 1 ? ' draft row' : ' draft rows');
  };
  root.querySelectorAll('[data-new]').forEach((b) => b.addEventListener('click', addRow));
})();
```
