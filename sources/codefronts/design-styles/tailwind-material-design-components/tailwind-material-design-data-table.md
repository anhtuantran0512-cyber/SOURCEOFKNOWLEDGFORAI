---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-data-table/"
title: "Tailwind Material Design Data Table"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "A real data table: sticky header, sortable columns keyed off aria-sort, row selection that tints the row through has-checked:, status badges, inline progress…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Data Table
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-data-table/

A real data table: sticky header, sortable columns keyed off aria-sort, row selection that tints the row through has-checked:, status badges, inline progress and a pagination footer. The port's win is that selection and sort state live on the elements the platform already uses &mdash; a checkbox and aria-sort &mdash; so no row ever carries an .is-selected class.
## HTML
```html
<section class="tmd-06 w-full min-h-svh bg-tmd06-bg font-tmd06-sans text-tmd06-onsurface px-5 py-9" aria-label="Material Design data table demo">
  <div class="w-[min(1080px,100%)] mx-auto grid gap-4">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Data table</h2>
      <p class="text-sm text-tmd06-onvariant">Sort keyed off <code class="font-tmd06-mono text-[12px]">aria-sort</code>, selection off <code class="font-tmd06-mono text-[12px]">has-checked:</code>, density off one custom property.</p>
    </header>

    <div class="group grid rounded-3xl overflow-hidden bg-tmd06-surface shadow-tmd06-1 [--row-h:56px]">
      <div class="flex flex-wrap items-center gap-2 px-4 py-3 border-b border-tmd06-outlinevariant">
        <span class="text-[17px] font-medium">Station readings</span>
        <span class="font-tmd06-mono text-[11px] text-tmd06-onvariant">18 rows</span>
        <label class="ml-auto flex items-center gap-2 min-h-11 text-xs font-medium text-tmd06-onvariant cursor-pointer">
          <input type="checkbox" id="tmd06-dense" class="w-4 h-4 accent-tmd06-primary cursor-pointer">Compact
        </label>
        <div class="relative">
          <span class="font-tmd06-icon absolute left-3 top-1/2 [transform:translateY(-50%)] text-[18px] leading-none text-tmd06-onvariant pointer-events-none" aria-hidden="true">search</span>
          <input type="search" aria-label="Filter rows" placeholder="Filter" class="min-h-11 pl-10 pr-3 rounded-full bg-tmd06-surface2 border border-transparent font-tmd06-sans text-sm text-tmd06-onsurface outline-none transition-colors duration-150 focus:border-tmd06-primary">
        </div>
      </div>

      <div class="overflow-x-auto overscroll-x-contain">
        <table class="w-full border-collapse text-sm">
          <caption class="sr-only">Station readings, sortable by station, depth and status</caption>
          <thead>
            <tr>
              <th scope="col" class="sticky top-0 z-1 h-13 w-12 px-3 bg-tmd06-surface border-b border-tmd06-outlinevariant text-left"><input type="checkbox" data-all aria-label="Select all rows" class="w-4 h-4 accent-tmd06-primary cursor-pointer"></th>
              <th scope="col" aria-sort="ascending" data-sort="text" class="sticky top-0 z-1 h-13 px-3 bg-tmd06-surface border-b border-tmd06-outlinevariant text-left font-medium text-tmd06-onvariant cursor-pointer select-none transition-colors duration-150 hover:text-tmd06-onsurface aria-[sort=ascending]:text-tmd06-primary aria-[sort=descending]:text-tmd06-primary"><button type="button" class="inline-flex items-center gap-1 bg-transparent border-0 p-0 font-inherit text-inherit cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd06-primary">Station<span class="font-tmd06-icon text-[16px] leading-none" data-arrow aria-hidden="true">arrow_upward</span></button></th>
              <th scope="col" data-sort="text" class="sticky top-0 z-1 h-13 px-3 bg-tmd06-surface border-b border-tmd06-outlinevariant text-left font-medium text-tmd06-onvariant cursor-pointer select-none hover:text-tmd06-onsurface aria-[sort=ascending]:text-tmd06-primary aria-[sort=descending]:text-tmd06-primary"><button type="button" class="inline-flex items-center gap-1 bg-transparent border-0 p-0 font-inherit text-inherit cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd06-primary">Region<span class="font-tmd06-icon text-[16px] leading-none" data-arrow aria-hidden="true">arrow_upward</span></button></th>
              <th scope="col" data-sort="num" class="sticky top-0 z-1 h-13 px-3 bg-tmd06-surface border-b border-tmd06-outlinevariant text-right font-medium text-tmd06-onvariant cursor-pointer select-none hover:text-tmd06-onsurface aria-[sort=ascending]:text-tmd06-primary aria-[sort=descending]:text-tmd06-primary"><button type="button" class="inline-flex items-center gap-1 bg-transparent border-0 p-0 font-inherit text-inherit cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd06-primary">Depth (m)<span class="font-tmd06-icon text-[16px] leading-none" data-arrow aria-hidden="true">arrow_upward</span></button></th>
              <th scope="col" class="sticky top-0 z-1 h-13 px-3 bg-tmd06-surface border-b border-tmd06-outlinevariant text-left font-medium text-tmd06-onvariant">Calibration</th>
              <th scope="col" class="sticky top-0 z-1 h-13 px-3 bg-tmd06-surface border-b border-tmd06-outlinevariant text-left font-medium text-tmd06-onvariant">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-b border-tmd06-outlinevariant transition-colors duration-150 hover:bg-tmd06-rowhover has-checked:bg-tmd06-rowselected">
              <td class="h-[var(--row-h)] px-3"><input type="checkbox" aria-label="Select ST-014" class="w-4 h-4 accent-tmd06-primary cursor-pointer"></td>
              <td class="h-[var(--row-h)] px-3 font-medium">ST-014</td>
              <td class="h-[var(--row-h)] px-3 text-tmd06-onvariant">North Atlantic</td>
              <td class="h-[var(--row-h)] px-3 text-right tabular-nums">1 240</td>
              <td class="h-[var(--row-h)] px-3"><div class="flex items-center gap-2"><div class="w-24 h-1 rounded-full bg-tmd06-outlinevariant overflow-hidden"><div class="h-full w-[86%] rounded-full bg-tmd06-primary"></div></div><span class="font-tmd06-mono text-[11px] tabular-nums text-tmd06-onvariant">86%</span></div></td>
              <td class="h-[var(--row-h)] px-3"><span class="inline-flex items-center gap-1 h-6 px-2.5 rounded-full bg-tmd06-okbg text-tmd06-okink text-[11px] font-medium">Online</span></td>
            </tr>
            <tr class="border-b border-tmd06-outlinevariant transition-colors duration-150 hover:bg-tmd06-rowhover has-checked:bg-tmd06-rowselected">
              <td class="h-[var(--row-h)] px-3"><input type="checkbox" aria-label="Select ST-022" checked class="w-4 h-4 accent-tmd06-primary cursor-pointer"></td>
              <td class="h-[var(--row-h)] px-3 font-medium">ST-022</td>
              <td class="h-[var(--row-h)] px-3 text-tmd06-onvariant">Baltic</td>
              <td class="h-[var(--row-h)] px-3 text-right tabular-nums">86</td>
              <td class="h-[var(--row-h)] px-3"><div class="flex items-center gap-2"><div class="w-24 h-1 rounded-full bg-tmd06-outlinevariant overflow-hidden"><div class="h-full w-[42%] rounded-full bg-tmd06-warnink"></div></div><span class="font-tmd06-mono text-[11px] tabular-nums text-tmd06-onvariant">42%</span></div></td>
              <td class="h-[var(--row-h)] px-3"><span class="inline-flex items-center gap-1 h-6 px-2.5 rounded-full bg-tmd06-warnbg text-tmd06-warnink text-[11px] font-medium">Drifting</span></td>
            </tr>
            <tr class="border-b border-tmd06-outlinevariant transition-colors duration-150 hover:bg-tmd06-rowhover has-checked:bg-tmd06-rowselected">
              <td class="h-[var(--row-h)] px-3"><input type="checkbox" aria-label="Select ST-031" class="w-4 h-4 accent-tmd06-primary cursor-pointer"></td>
              <td class="h-[var(--row-h)] px-3 font-medium">ST-031</td>
              <td class="h-[var(--row-h)] px-3 text-tmd06-onvariant">Mediterranean</td>
              <td class="h-[var(--row-h)] px-3 text-right tabular-nums">640</td>
              <td class="h-[var(--row-h)] px-3"><div class="flex items-center gap-2"><div class="w-24 h-1 rounded-full bg-tmd06-outlinevariant overflow-hidden"><div class="h-full w-[100%] rounded-full bg-tmd06-primary"></div></div><span class="font-tmd06-mono text-[11px] tabular-nums text-tmd06-onvariant">100%</span></div></td>
              <td class="h-[var(--row-h)] px-3"><span class="inline-flex items-center gap-1 h-6 px-2.5 rounded-full bg-tmd06-okbg text-tmd06-okink text-[11px] font-medium">Online</span></td>
            </tr>
            <tr class="border-b border-tmd06-outlinevariant transition-colors duration-150 hover:bg-tmd06-rowhover has-checked:bg-tmd06-rowselected">
              <td class="h-[var(--row-h)] px-3"><input type="checkbox" aria-label="Select ST-047" class="w-4 h-4 accent-tmd06-primary cursor-pointer"></td>
              <td class="h-[var(--row-h)] px-3 font-medium">ST-047</td>
              <td class="h-[var(--row-h)] px-3 text-tmd06-onvariant">Norwegian Sea</td>
              <td class="h-[var(--row-h)] px-3 text-right tabular-nums">2 010</td>
              <td class="h-[var(--row-h)] px-3"><div class="flex items-center gap-2"><div class="w-24 h-1 rounded-full bg-tmd06-outlinevariant overflow-hidden"><div class="h-full w-[12%] rounded-full bg-tmd06-errink"></div></div><span class="font-tmd06-mono text-[11px] tabular-nums text-tmd06-onvariant">12%</span></div></td>
              <td class="h-[var(--row-h)] px-3"><span class="inline-flex items-center gap-1 h-6 px-2.5 rounded-full bg-tmd06-errbg text-tmd06-errink text-[11px] font-medium">Offline</span></td>
            </tr>
            <tr class="border-b border-tmd06-outlinevariant transition-colors duration-150 hover:bg-tmd06-rowhover has-checked:bg-tmd06-rowselected">
              <td class="h-[var(--row-h)] px-3"><input type="checkbox" aria-label="Select ST-059" class="w-4 h-4 accent-tmd06-primary cursor-pointer"></td>
              <td class="h-[var(--row-h)] px-3 font-medium">ST-059</td>
              <td class="h-[var(--row-h)] px-3 text-tmd06-onvariant">Irish Shelf</td>
              <td class="h-[var(--row-h)] px-3 text-right tabular-nums">312</td>
              <td class="h-[var(--row-h)] px-3"><div class="flex items-center gap-2"><div class="w-24 h-1 rounded-full bg-tmd06-outlinevariant overflow-hidden"><div class="h-full w-[68%] rounded-full bg-tmd06-primary"></div></div><span class="font-tmd06-mono text-[11px] tabular-nums text-tmd06-onvariant">68%</span></div></td>
              <td class="h-[var(--row-h)] px-3"><span class="inline-flex items-center gap-1 h-6 px-2.5 rounded-full bg-tmd06-okbg text-tmd06-okink text-[11px] font-medium">Online</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="flex flex-wrap items-center justify-end gap-4 px-4 py-3 text-xs text-tmd06-onvariant">
        <span><b data-selected class="font-tmd06-mono tabular-nums text-tmd06-primary">1</b> selected</span>
        <span class="font-tmd06-mono tabular-nums">1&ndash;5 of 18</span>
        <div class="flex gap-1">
          <button type="button" aria-label="Previous page" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd06-onvariant focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd06-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd06-icon text-[20px] leading-none" aria-hidden="true">chevron_left</span></button>
          <button type="button" aria-label="Next page" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-full border-0 bg-transparent cursor-pointer text-tmd06-onvariant focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd06-primary before:absolute before:inset-1 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd06-icon text-[20px] leading-none" aria-hidden="true">chevron_right</span></button>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd06-bg: #e1f5fe;
  --color-tmd06-bg: oklch(0.958 0.024 226.5);
  --color-tmd06-surface: #ffffff;
  --color-tmd06-surface: oklch(1 0 89.9);
  --color-tmd06-surface2: #eef6fb;
  --color-tmd06-surface2: oklch(0.969 0.011 234.8);
  --color-tmd06-primary: #0277bd;
  --color-tmd06-primary: oklch(0.551 0.139 245.4);
  --color-tmd06-onsurface: #14212b;
  --color-tmd06-onsurface: oklch(0.241 0.026 242.3);
  --color-tmd06-onvariant: #546e7a;
  --color-tmd06-onvariant: oklch(0.522 0.036 227.9);
  --color-tmd06-outlinevariant: #cfdee6;
  --color-tmd06-outlinevariant: oklch(0.892 0.02 230.7);
  --color-tmd06-rowhover: #eaf4fb;
  --color-tmd06-rowhover: oklch(0.962 0.014 238);
  --color-tmd06-rowselected: #ddeefa;
  --color-tmd06-rowselected: oklch(0.94 0.024 238.4);
  --color-tmd06-zebra: #f5fafd;
  --color-tmd06-zebra: oklch(0.982 0.007 233.6);
  --color-tmd06-okbg: #d7f2e0;
  --color-tmd06-okbg: oklch(0.937 0.037 156.4);
  --color-tmd06-okink: #12653a;
  --color-tmd06-okink: oklch(0.448 0.103 154.8);
  --color-tmd06-warnbg: #ffe8cc;
  --color-tmd06-warnbg: oklch(0.942 0.045 72.7);
  --color-tmd06-warnink: #8a4b00;
  --color-tmd06-warnink: oklch(0.479 0.112 59.9);
  --color-tmd06-errbg: #ffdad6;
  --color-tmd06-errbg: oklch(0.918 0.042 25.2);
  --color-tmd06-errink: #93000a;
  --color-tmd06-errink: oklch(0.417 0.17 27.4);
  --font-tmd06-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd06-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd06-icon: 'Material Symbols Outlined';
  --shadow-tmd06-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
}

.tmd-06 {
  width: 100%;
  min-height: 100svh;
}

.tmd-06 .font-tmd06-icon {
  font-feature-settings: 'liga';
}
/* Density: the toggle is a sibling of the table wrapper, so the property is set from
   a :has() rule — the one relationship no variant can express from inside the wrapper. */

.tmd-06 .group:has(#tmd06-dense:checked) {
  --row-h: 40px;
}
/* Sort arrows: hidden until the column carries aria-sort, and flipped when descending.
   A pseudo-element rotation keyed off an ancestor attribute has no variant form. */

.tmd-06 th [data-arrow] {
  opacity: 0;
  transition: opacity .15s, rotate .2s;
}

.tmd-06 th[aria-sort] [data-arrow] {
  opacity: 1;
}

.tmd-06 th[aria-sort="descending"] [data-arrow] {
  rotate: 180deg;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tmd-06').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var table = root.querySelector('table'),
        body = table.tBodies[0],
        all = root.querySelector('[data-all]'),
        count = root.querySelector('[data-selected]');
    function boxes() { return Array.prototype.slice.call(body.querySelectorAll('input[type=checkbox]')); }
    function sync() {
      var b = boxes(), n = b.filter(function (x) { return x.checked; }).length;
      count.textContent = String(n);
      all.checked = n === b.length && n > 0;
      all.indeterminate = n > 0 && n < b.length;
    }
    all.addEventListener('change', function () {
      boxes().forEach(function (x) { x.checked = all.checked; });
      sync();
    });
    body.addEventListener('change', sync);
    table.querySelectorAll('th[data-sort]').forEach(function (th, i) {
      th.querySelector('button').addEventListener('click', function () {
        var dir = th.getAttribute('aria-sort') === 'ascending' ? -1 : 1,
            idx = Array.prototype.indexOf.call(th.parentNode.children, th),
            num = th.dataset.sort === 'num',
            rows = Array.prototype.slice.call(body.rows);
        table.querySelectorAll('th[aria-sort]').forEach(function (o) { o.removeAttribute('aria-sort'); });
        th.setAttribute('aria-sort', dir === 1 ? 'ascending' : 'descending');
        rows.sort(function (a, b) {
          var x = a.cells[idx].textContent.trim(), y = b.cells[idx].textContent.trim();
          if (num) return (parseFloat(x.replace(/\s/g, '')) - parseFloat(y.replace(/\s/g, ''))) * dir;
          return x.localeCompare(y) * dir;
        });
        rows.forEach(function (r) { body.appendChild(r); });
      });
    });
    sync();
  });
})();
```
