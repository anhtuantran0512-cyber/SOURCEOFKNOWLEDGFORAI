---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-pagination-with-rows-per-page-select-dropdown/"
title: "Tailwind Pagination with Rows Per Page Select Dropdown"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "The three-part footer every admin list converges on — a rows per page select, a live record range and a first / prev / next / last stepper — attached to an…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pagination with Rows Per Page Select Dropdown
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-pagination-with-rows-per-page-select-dropdown/

The three-part footer every admin list converges on — a rows per page select, a live record range and a first / prev / next / last stepper — attached to an orders table that actually re-renders. The native <select> is restyled with appearance-none and a pointer-events-none caret, the stepper's edges disable through native disabled, and status chips are styled by data-[status=paid]: variants so the script never touches a class.
## HTML
```html
<section class="tpg-06 w-full min-h-svh grid place-items-center bg-tpg06-bg bg-[radial-gradient(70%_55%_at_50%_0%,var(--color-tpg06-glow),transparent_72%)] px-5 py-14 font-tpg06-sans text-tpg06-ink antialiased" aria-label="Rows per page pagination demo">
  <div class="grid w-full justify-items-center gap-7">
    <div id="tpg-06-orders" class="w-full max-w-[56rem] overflow-hidden rounded-2xl bg-tpg06-card shadow-tpg06-card ring-1 ring-tpg06-acc/15 transition duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
      <header class="flex flex-wrap items-end justify-between gap-x-6 gap-y-3 px-5 pt-5 pb-4 sm:px-6">
        <div>
          <p class="text-[11px] font-bold tracking-[0.16em] text-tpg06-mut uppercase">Orders</p>
          <h2 class="mt-1 text-xl font-bold tracking-[-0.02em] tabular-nums">288 orders <span class="font-medium text-tpg06-mut">· last 30 days</span></h2>
        </div>
        <p class="flex items-center gap-2 text-[13px] text-tpg06-mut"><span aria-hidden="true" class="size-2 rounded-full bg-tpg06-ok shadow-[0_0_0_3px_var(--color-tpg06-ok-halo)]"></span>Synced 2 min ago</p>
      </header>

      <div data-scroll class="max-h-[20rem] overflow-auto border-y border-tpg06-line [scrollbar-width:thin]">
        <table class="w-full border-separate border-spacing-0 text-left text-sm">
          <caption class="sr-only">Orders, one page at a time</caption>
          <thead class="sticky top-0 z-10 bg-tpg06-sunk/95 backdrop-blur-sm">
            <tr class="text-[11px] font-bold tracking-[0.1em] text-tpg06-mut uppercase">
              <th scope="col" class="border-b border-tpg06-line px-5 py-2.5 font-bold max-sm:hidden sm:px-6">Order</th>
              <th scope="col" class="border-b border-tpg06-line py-2.5 pr-3 pl-5 font-bold sm:pl-3">Customer</th>
              <th scope="col" class="border-b border-tpg06-line px-3 py-2.5 font-bold max-sm:hidden">Date</th>
              <th scope="col" class="border-b border-tpg06-line px-3 py-2.5 font-bold">Status</th>
              <th scope="col" class="border-b border-tpg06-line px-5 py-2.5 text-right font-bold sm:px-6">Total</th>
            </tr>
          </thead>
          <tbody>
            <tr class="transition-colors hover:bg-tpg06-sunk/70">
              <td class="border-b border-tpg06-line/70 px-5 py-3 font-tpg06-mono text-[13px] text-tpg06-mut tabular-nums max-sm:hidden sm:px-6">#24180</td>
              <td class="border-b border-tpg06-line/70 py-3 pr-3 pl-5 font-semibold whitespace-nowrap sm:pl-3">Maya Okafor</td>
              <td class="border-b border-tpg06-line/70 px-3 py-3 whitespace-nowrap text-tpg06-mut tabular-nums max-sm:hidden">Oct 13</td>
              <td class="border-b border-tpg06-line/70 px-3 py-3"><span data-status="paid" class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-xs font-semibold capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current data-[status=paid]:bg-tpg06-ok/10 data-[status=paid]:text-tpg06-ok data-[status=paid]:ring-tpg06-ok/25 data-[status=pending]:bg-tpg06-warn/10 data-[status=pending]:text-tpg06-warn data-[status=pending]:ring-tpg06-warn/25 data-[status=refunded]:bg-tpg06-sunk data-[status=refunded]:text-tpg06-mut data-[status=refunded]:ring-tpg06-line data-[status=shipped]:bg-tpg06-acc/10 data-[status=shipped]:text-tpg06-acc data-[status=shipped]:ring-tpg06-acc/25">paid</span></td>
              <td class="border-b border-tpg06-line/70 px-5 py-3 text-right font-semibold tabular-nums sm:px-6">$19.50</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="relative h-0.5 bg-tpg06-acc/10" aria-hidden="true"><span data-bar class="absolute inset-y-0 left-0 w-[calc(var(--tpg06-p,0.083)*100%)] rounded-r-full bg-linear-to-r from-tpg06-acc to-tpg06-acc2 shadow-[0_0_14px_var(--color-tpg06-acc)] transition-[width] duration-500 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none"></span></div>

      <div class="flex flex-wrap items-center justify-between gap-x-6 gap-y-3 px-5 py-3.5 sm:px-6">
        <div class="flex items-center gap-3">
          <label for="tpg-06-per" class="text-[13px] font-medium whitespace-nowrap text-tpg06-mut">Rows per page</label>
          <div class="relative">
            <select id="tpg-06-per" class="h-11 cursor-pointer appearance-none rounded-lg bg-tpg06-sunk pr-9 pl-3 text-sm font-semibold text-tpg06-ink tabular-nums ring-1 ring-tpg06-acc/20 transition-shadow hover:ring-tpg06-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg06-ring">
              <option value="12">12</option>
              <option value="24" selected>24</option>
              <option value="48">48</option>
              <option value="96">96</option>
            </select>
            <svg class="pointer-events-none absolute top-1/2 right-2.5 size-4 -translate-y-1/2 text-tpg06-mut" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M6 8l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
          <p data-range role="status" class="ml-1 text-[13px] whitespace-nowrap text-tpg06-mut tabular-nums sm:ml-3"><b class="font-semibold text-tpg06-ink">1–24</b> of 288</p>
        </div>

        <nav aria-label="Pagination" class="max-sm:w-full">
          <ul class="flex items-center gap-1.5 max-sm:justify-between">
            <li><button type="button" data-go="first" aria-label="First page" disabled class="grid size-11 cursor-pointer place-items-center rounded-lg bg-tpg06-card text-tpg06-acc-ink shadow-[0_1px_2px_oklch(0.4_0.1_10/0.1)] ring-1 ring-tpg06-acc/25 transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] enabled:hover:-translate-y-0.5 enabled:hover:bg-tpg06-acc/8 enabled:hover:ring-tpg06-acc/50 enabled:hover:shadow-[0_10px_20px_-10px_var(--color-tpg06-acc)] enabled:active:translate-y-0 enabled:active:scale-95 disabled:cursor-not-allowed disabled:bg-tpg06-sunk disabled:text-tpg06-mut disabled:opacity-60 disabled:shadow-none disabled:ring-tpg06-line focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg06-ring motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M15 5l-5 5 5 5M9 5L4 10l5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></button></li>
            <li><button type="button" data-go="prev" aria-label="Previous page" disabled class="grid size-11 cursor-pointer place-items-center rounded-lg bg-tpg06-card text-tpg06-acc-ink shadow-[0_1px_2px_oklch(0.4_0.1_10/0.1)] ring-1 ring-tpg06-acc/25 transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] enabled:hover:-translate-y-0.5 enabled:hover:bg-tpg06-acc/8 enabled:hover:ring-tpg06-acc/50 enabled:hover:shadow-[0_10px_20px_-10px_var(--color-tpg06-acc)] enabled:active:translate-y-0 enabled:active:scale-95 disabled:cursor-not-allowed disabled:bg-tpg06-sunk disabled:text-tpg06-mut disabled:opacity-60 disabled:shadow-none disabled:ring-tpg06-line focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg06-ring motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 5L7.5 10l5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></button></li>
            <li class="min-w-[7.5rem] px-1 text-center text-[13px] text-tpg06-mut tabular-nums">Page <b data-page class="mx-0.5 inline-grid h-7 min-w-7 place-items-center rounded-full bg-linear-to-br from-tpg06-acc to-tpg06-acc2 px-2 font-bold text-tpg06-on shadow-[inset_0_1px_0_oklch(1_0_0/0.3),0_6px_16px_-4px_var(--color-tpg06-acc)]">1</b> of <b data-pages class="font-semibold text-tpg06-ink">12</b></li>
            <li><button type="button" data-go="next" aria-label="Next page" class="grid size-11 cursor-pointer place-items-center rounded-lg bg-tpg06-card text-tpg06-acc-ink enabled:bg-linear-to-br enabled:from-tpg06-acc enabled:to-tpg06-acc2 enabled:text-tpg06-on enabled:ring-0 enabled:shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_8px_20px_-8px_var(--color-tpg06-acc)] enabled:hover:shadow-[inset_0_1px_0_oklch(1_0_0/0.25),0_14px_26px_-10px_var(--color-tpg06-acc)] shadow-[0_1px_2px_oklch(0.4_0.1_10/0.1)] ring-1 ring-tpg06-acc/25 transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] enabled:hover:-translate-y-0.5 enabled:hover:bg-tpg06-acc/8 enabled:hover:ring-tpg06-acc/50 enabled:hover:shadow-[0_10px_20px_-10px_var(--color-tpg06-acc)] enabled:active:translate-y-0 enabled:active:scale-95 disabled:cursor-not-allowed disabled:bg-tpg06-sunk disabled:text-tpg06-mut disabled:opacity-60 disabled:shadow-none disabled:ring-tpg06-line focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg06-ring motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></button></li>
            <li><button type="button" data-go="last" aria-label="Last page" class="grid size-11 cursor-pointer place-items-center rounded-lg bg-tpg06-card text-tpg06-acc-ink shadow-[0_1px_2px_oklch(0.4_0.1_10/0.1)] ring-1 ring-tpg06-acc/25 transition duration-200 ease-[cubic-bezier(.16,1,.3,1)] enabled:hover:-translate-y-0.5 enabled:hover:bg-tpg06-acc/8 enabled:hover:ring-tpg06-acc/50 enabled:hover:shadow-[0_10px_20px_-10px_var(--color-tpg06-acc)] enabled:active:translate-y-0 enabled:active:scale-95 disabled:cursor-not-allowed disabled:bg-tpg06-sunk disabled:text-tpg06-mut disabled:opacity-60 disabled:shadow-none disabled:ring-tpg06-line focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg06-ring motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M5 5l5 5-5 5M11 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></button></li>
          </ul>
        </nav>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tpg06-card px-3.5 py-2 text-center font-tpg06-mono text-[11.5px] text-tpg06-mut ring-1 ring-tpg06-line">appearance-none · enabled: · data-[status]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg06-bg: #fff4f5;
  --color-tpg06-bg: oklch(0.975 0.012 10);
  --color-tpg06-glow: #ffd7e0b3;
  --color-tpg06-glow: oklch(0.92 0.05 5 / 0.7);
  --color-tpg06-card: #fffcfd;
  --color-tpg06-card: oklch(0.995 0.004 10);
  --color-tpg06-sunk: #fdf0f1;
  --color-tpg06-sunk: oklch(0.965 0.014 10);
  --color-tpg06-ink: #2f171b;
  --color-tpg06-ink: oklch(0.24 0.04 10);
  --color-tpg06-mut: #725458;
  --color-tpg06-mut: oklch(0.48 0.04 10);
  --color-tpg06-line: #eed8da;
  --color-tpg06-line: oklch(0.9 0.025 10);
  --color-tpg06-acc: #e11d48;
  --color-tpg06-acc: oklch(0.586 0.222 17.6);
  --color-tpg06-acc2: #db2777;
  --color-tpg06-acc2: oklch(0.592 0.218 0.6);
  --color-tpg06-acc-ink: #b6143f;
  --color-tpg06-acc-ink: oklch(0.5 0.19 15);
  --color-tpg06-on: #ffffff;
  --color-tpg06-on: oklch(1 0 0);
  --color-tpg06-ring: #b6143f;
  --color-tpg06-ring: oklch(0.5 0.19 15);
  --color-tpg06-ok: #21763c;
  --color-tpg06-ok: oklch(0.5 0.12 150);
  --color-tpg06-ok-halo: #21763c2e;
  --color-tpg06-ok-halo: oklch(0.5 0.12 150 / 0.18);
  --color-tpg06-warn: #935a11;
  --color-tpg06-warn: oklch(0.52 0.11 65);
  --font-tpg06-sans: 'Manrope', system-ui, sans-serif;
  --font-tpg06-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tpg06-card: 0 1px 2px oklch(0.4 0.1 10 / 0.08), 0 28px 56px -24px oklch(0.5 0.2 10 / 0.35);
}
/* Dark "wine night": re-point the same tokens, so every utility (and every /10 opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tpg-06:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tpg06-bg: #1c080c;
    --color-tpg06-bg: oklch(0.17 0.035 10);
    --color-tpg06-glow: #540f2280;
    --color-tpg06-glow: oklch(0.3 0.1 10 / 0.5);
    --color-tpg06-card: #291115;
    --color-tpg06-card: oklch(0.215 0.04 10);
    --color-tpg06-sunk: #35191e;
    --color-tpg06-sunk: oklch(0.255 0.045 10);
    --color-tpg06-ink: #f8eff0;
    --color-tpg06-ink: oklch(0.96 0.01 10);
    --color-tpg06-mut: #cfadb1;
    --color-tpg06-mut: oklch(0.78 0.04 10);
    --color-tpg06-line: #4b2a2f;
    --color-tpg06-line: oklch(0.33 0.05 10);
    --color-tpg06-acc: #fb718c;
    --color-tpg06-acc: oklch(0.72 0.17 10);
    --color-tpg06-acc2: #f77cb0;
    --color-tpg06-acc2: oklch(0.74 0.16 355);
    --color-tpg06-acc-ink: #ff9cac;
    --color-tpg06-acc-ink: oklch(0.8 0.12 10);
    --color-tpg06-on: #280b11;
    --color-tpg06-on: oklch(0.2 0.05 10);
    --color-tpg06-ring: #ff9cac;
    --color-tpg06-ring: oklch(0.8 0.12 10);
    --color-tpg06-ok: #7cd591;
    --color-tpg06-ok: oklch(0.8 0.13 150);
    --color-tpg06-ok-halo: #7cd59126;
    --color-tpg06-ok-halo: oklch(0.8 0.13 150 / 0.15);
    --color-tpg06-warn: #f5bc69;
    --color-tpg06-warn: oklch(0.83 0.12 75);
  }
}

.tpg-06[data-theme="dark"] {
  color-scheme: dark;
  --color-tpg06-bg: #1c080c;
  --color-tpg06-bg: oklch(0.17 0.035 10);
  --color-tpg06-glow: #540f2280;
  --color-tpg06-glow: oklch(0.3 0.1 10 / 0.5);
  --color-tpg06-card: #291115;
  --color-tpg06-card: oklch(0.215 0.04 10);
  --color-tpg06-sunk: #35191e;
  --color-tpg06-sunk: oklch(0.255 0.045 10);
  --color-tpg06-ink: #f8eff0;
  --color-tpg06-ink: oklch(0.96 0.01 10);
  --color-tpg06-mut: #cfadb1;
  --color-tpg06-mut: oklch(0.78 0.04 10);
  --color-tpg06-line: #4b2a2f;
  --color-tpg06-line: oklch(0.33 0.05 10);
  --color-tpg06-acc: #fb718c;
  --color-tpg06-acc: oklch(0.72 0.17 10);
  --color-tpg06-acc2: #f77cb0;
  --color-tpg06-acc2: oklch(0.74 0.16 355);
  --color-tpg06-acc-ink: #ff9cac;
  --color-tpg06-acc-ink: oklch(0.8 0.12 10);
  --color-tpg06-on: #280b11;
  --color-tpg06-on: oklch(0.2 0.05 10);
  --color-tpg06-ring: #ff9cac;
  --color-tpg06-ring: oklch(0.8 0.12 10);
  --color-tpg06-ok: #7cd591;
  --color-tpg06-ok: oklch(0.8 0.13 150);
  --color-tpg06-ok-halo: #7cd59126;
  --color-tpg06-ok-halo: oklch(0.8 0.13 150 / 0.15);
  --color-tpg06-warn: #f5bc69;
  --color-tpg06-warn: oklch(0.83 0.12 75);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-06 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tpg-06-orders');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const $ = (s) => root.querySelector(s);
  const select = $('#tpg-06-per'), body = $('tbody'), scroller = $('[data-scroll]');
  const proto = body.rows[0].cloneNode(true);
  const total = 288;
  const names = ['Maya Okafor', 'Liam Chen', 'Ana Souza', 'Noah Brandt', 'Isla Murray', 'Ravi Iyer', 'Elena Petrova', 'Owen Hughes', 'Zara Ahmed'];
  const states = ['paid', 'shipped', 'paid', 'pending', 'paid', 'refunded', 'shipped'];
  let per = Number(select.value), page = 1;
  const pages = () => Math.ceil(total / per);
  const fill = (tr, i) => {
    const c = tr.cells;
    c[0].textContent = '#' + (24180 - i);
    c[1].textContent = names[(i * 7) % names.length];
    c[2].textContent = new Date(2026, 9, 13 - Math.floor(i / 9)).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    const chip = c[3].firstElementChild;
    chip.dataset.status = chip.textContent = states[i % states.length];
    c[4].textContent = '$' + (((i * 4153) % 38000) / 100 + 19.5).toFixed(2);
    return tr;
  };
  const paint = () => {
    const from = (page - 1) * per + 1, to = Math.min(page * per, total), rows = [];
    for (let i = from - 1; i < to; i++) rows.push(fill(proto.cloneNode(true), i));
    body.replaceChildren(...rows);
    scroller.scrollTop = 0;
    $('[data-range]').firstChild.textContent = from + '–' + to;
    $('[data-page]').textContent = page;
    $('[data-pages]').textContent = pages();
    $('[data-bar]').style.setProperty('--tpg06-p', to / total);
    root.querySelectorAll('[data-go]').forEach((b) => {
      b.disabled = ['first', 'prev'].includes(b.dataset.go) ? page === 1 : page === pages();
    });
  };
  select.addEventListener('change', () => {
    const first = (page - 1) * per;
    per = Number(select.value);
    page = Math.floor(first / per) + 1;
    paint();
  });
  root.querySelectorAll('[data-go]').forEach((b) => b.addEventListener('click', () => {
    const k = b.dataset.go;
    page = k === 'first' ? 1 : k === 'last' ? pages() : page + (k === 'next' ? 1 : -1);
    paint();
  }));
  paint();
})();
```
