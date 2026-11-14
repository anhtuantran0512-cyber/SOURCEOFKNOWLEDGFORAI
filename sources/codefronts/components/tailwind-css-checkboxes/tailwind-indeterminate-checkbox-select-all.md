---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/tailwind-indeterminate-checkbox-select-all/"
title: "Tailwind Indeterminate Checkbox — Select All with Tri-State"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "The \"select all\" pattern with a real mixed state: peer-indeterminate:bg-tcb05-acc fills the master box and group-has-indeterminate:opacity-100 reveals its dash."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Indeterminate Checkbox — Select All with Tri-State
Source: https://codefronts.com/components/tailwind-css-checkboxes/tailwind-indeterminate-checkbox-select-all/

The "select all" pattern with a real mixed state: peer-indeterminate:bg-tcb05-acc fills the master box and group-has-indeterminate:opacity-100 reveals its dash. A 20-line controller syncs parent and children — and now announces "2 of 4 selected" through a polite live region.
## HTML
```html
<section class="tcb-05 w-full min-h-svh grid place-items-center bg-tcb05-bg px-5 py-14 font-tcb05-sans text-tcb05-ink selection:bg-tcb05-acc selection:text-white" data-tcb05 aria-label="Select all with indeterminate state">
  <div class="w-full max-w-[26rem] rounded-2xl border border-tcb05-line bg-white p-2 shadow-tcb05-panel">
    <div class="flex items-center justify-between gap-3 border-b border-tcb05-line px-3.5 pb-2.5 pt-1.5">
      <label class="group flex min-h-11 cursor-pointer items-center gap-3 text-[15px] font-semibold">
        <input type="checkbox" class="peer sr-only" data-master>
        <span aria-hidden="true" class="relative grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb05-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb05-acc peer-checked:bg-tcb05-acc peer-indeterminate:border-tcb05-acc peer-indeterminate:bg-tcb05-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb05-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="absolute size-3.5 opacity-0 transition-opacity group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" class="absolute size-3.5 opacity-0 transition-opacity group-has-indeterminate:opacity-100"><path d="M6 12h12"/></svg></span>
        Select all recipients
      </label>
      <span class="text-[13px] font-medium tabular-nums text-tcb05-mut" aria-live="polite" data-count></span>
    </div>
    <div class="pl-5 pt-1">
      <label class="group flex min-h-11 cursor-pointer items-center gap-3 rounded-lg px-3.5 text-sm transition-colors hover:bg-tcb05-hover has-checked:bg-tcb05-sel"><input type="checkbox" class="peer sr-only" data-child checked><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb05-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb05-acc peer-checked:bg-tcb05-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb05-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 opacity-0 transition-opacity group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span>[email protected]</label>
      <label class="group flex min-h-11 cursor-pointer items-center gap-3 rounded-lg px-3.5 text-sm transition-colors hover:bg-tcb05-hover has-checked:bg-tcb05-sel"><input type="checkbox" class="peer sr-only" data-child><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb05-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb05-acc peer-checked:bg-tcb05-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb05-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 opacity-0 transition-opacity group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span>[email protected]</label>
      <label class="group flex min-h-11 cursor-pointer items-center gap-3 rounded-lg px-3.5 text-sm transition-colors hover:bg-tcb05-hover has-checked:bg-tcb05-sel"><input type="checkbox" class="peer sr-only" data-child checked><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb05-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb05-acc peer-checked:bg-tcb05-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb05-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 opacity-0 transition-opacity group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span>[email protected]</label>
      <label class="group flex min-h-11 cursor-pointer items-center gap-3 rounded-lg px-3.5 text-sm transition-colors hover:bg-tcb05-hover has-checked:bg-tcb05-sel"><input type="checkbox" class="peer sr-only" data-child><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb05-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb05-acc peer-checked:bg-tcb05-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb05-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 opacity-0 transition-opacity group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span>[email protected]</label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb05-bg: #f4f5f7;
  --color-tcb05-bg: oklch(0.97 0.004 260);
  --color-tcb05-ink: #2a2f3a;
  --color-tcb05-ink: oklch(0.3 0.02 265);
  --color-tcb05-mut: #5d6472;
  --color-tcb05-mut: oklch(0.49 0.02 265);
  --color-tcb05-line: #eceef2;
  --color-tcb05-line: oklch(0.945 0.006 265);
  --color-tcb05-hover: #f6f7f9;
  --color-tcb05-hover: oklch(0.975 0.003 265);
  --color-tcb05-sel: #eef4fd;
  --color-tcb05-sel: oklch(0.965 0.015 255);
  --color-tcb05-box: #b9bfc9;
  --color-tcb05-box: oklch(0.8 0.015 265);
  --color-tcb05-acc: #2f7de1;
  --color-tcb05-acc: oklch(0.6 0.17 255);
  --font-tcb05-sans: 'Geist', system-ui, sans-serif;
  --shadow-tcb05-panel: 0 18px 40px -30px rgb(16 24 40 / 0.5);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-05 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tcb05]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const master = root.querySelector('[data-master]');
    const kids = [...root.querySelectorAll('[data-child]')];
    const count = root.querySelector('[data-count]');
    const sync = () => {
      const n = kids.filter((k) => k.checked).length;
      master.checked = n === kids.length;
      master.indeterminate = n > 0 && n < kids.length;
      count.textContent = n + ' of ' + kids.length + ' selected';
    };
    master.addEventListener('change', () => {
      kids.forEach((k) => { k.checked = master.checked; });
      sync();
    });
    kids.forEach((k) => k.addEventListener('change', sync));
    sync();
  });
})();
```
