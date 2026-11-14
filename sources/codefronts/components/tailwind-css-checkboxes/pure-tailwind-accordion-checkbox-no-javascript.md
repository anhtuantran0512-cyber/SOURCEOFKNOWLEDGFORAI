---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/pure-tailwind-accordion-checkbox-no-javascript/"
title: "Pure Tailwind CSS Accordion with Checkbox — No JavaScript"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "A smooth-height FAQ accordion with zero script: each panel animates grid-rows-[0fr] → peer-checked:grid-rows-[1fr], the only reliable way to transition to…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind CSS Accordion with Checkbox — No JavaScript
Source: https://codefronts.com/components/tailwind-css-checkboxes/pure-tailwind-accordion-checkbox-no-javascript/

A smooth-height FAQ accordion with zero script: each panel animates grid-rows-[0fr] → peer-checked:grid-rows-[1fr], the only reliable way to transition to auto height. The chevron chip flips and fills from group-has-checked:.
## HTML
```html
<section class="tcb-04 w-full min-h-svh grid place-items-center bg-tcb04-bg px-5 py-14 font-tcb04-sans text-tcb04-ink selection:bg-tcb04-acc selection:text-white" aria-label="Frequently asked questions">
  <div class="w-full max-w-[35rem]">
    <h2 class="mb-5 text-[26px] font-bold tracking-[-0.02em]">Questions, answered</h2>
    <div class="divide-y divide-tcb04-line overflow-hidden rounded-2xl border border-tcb04-line bg-white shadow-tcb04-panel">
      <div class="group">
        <input type="checkbox" class="peer sr-only" id="tcb04-1" checked>
        <label for="tcb04-1" class="flex min-h-15 cursor-pointer items-center justify-between gap-4 px-5.5 py-4 text-[15px] font-semibold transition-colors hover:bg-tcb04-hover peer-focus-visible:outline-3 peer-focus-visible:-outline-offset-3 peer-focus-visible:outline-tcb04-acc">What browsers are supported?
          <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tcb04-chip text-tcb04-mut transition-colors duration-300 group-has-checked:bg-tcb04-acc group-has-checked:text-white"><span class="size-2.5 -translate-y-0.5 rotate-45 border-r-[2.5px] border-b-[2.5px] border-current transition-transform duration-300 group-has-checked:translate-y-0.5 group-has-checked:rotate-[-135deg] motion-reduce:transition-none"></span></span>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="px-5.5 pb-5 text-[14px] leading-relaxed text-tcb04-mut">Every evergreen browser — Chrome, Edge, Safari and Firefox. The grid-row reveal degrades to an instant open in legacy engines.</p></div>
        </div>
      </div>
      <div class="group">
        <input type="checkbox" class="peer sr-only" id="tcb04-2">
        <label for="tcb04-2" class="flex min-h-15 cursor-pointer items-center justify-between gap-4 px-5.5 py-4 text-[15px] font-semibold transition-colors hover:bg-tcb04-hover peer-focus-visible:outline-3 peer-focus-visible:-outline-offset-3 peer-focus-visible:outline-tcb04-acc">Is there any JavaScript?
          <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tcb04-chip text-tcb04-mut transition-colors duration-300 group-has-checked:bg-tcb04-acc group-has-checked:text-white"><span class="size-2.5 -translate-y-0.5 rotate-45 border-r-[2.5px] border-b-[2.5px] border-current transition-transform duration-300 group-has-checked:translate-y-0.5 group-has-checked:rotate-[-135deg] motion-reduce:transition-none"></span></span>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="px-5.5 pb-5 text-[14px] leading-relaxed text-tcb04-mut">None. The open/close state is the checkbox itself, and the height animation is pure CSS via grid-template-rows.</p></div>
        </div>
      </div>
      <div class="group">
        <input type="checkbox" class="peer sr-only" id="tcb04-3">
        <label for="tcb04-3" class="flex min-h-15 cursor-pointer items-center justify-between gap-4 px-5.5 py-4 text-[15px] font-semibold transition-colors hover:bg-tcb04-hover peer-focus-visible:outline-3 peer-focus-visible:-outline-offset-3 peer-focus-visible:outline-tcb04-acc">Can multiple panels stay open?
          <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tcb04-chip text-tcb04-mut transition-colors duration-300 group-has-checked:bg-tcb04-acc group-has-checked:text-white"><span class="size-2.5 -translate-y-0.5 rotate-45 border-r-[2.5px] border-b-[2.5px] border-current transition-transform duration-300 group-has-checked:translate-y-0.5 group-has-checked:rotate-[-135deg] motion-reduce:transition-none"></span></span>
        </label>
        <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-350 ease-out peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
          <div class="min-h-0 overflow-hidden"><p class="px-5.5 pb-5 text-[14px] leading-relaxed text-tcb04-mut">Yes — these are independent checkboxes. Swap them for radios with a shared name to force a single-open accordion.</p></div>
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
  --color-tcb04-bg: #f4f5f7;
  --color-tcb04-bg: oklch(0.97 0.004 260);
  --color-tcb04-ink: #1f2430;
  --color-tcb04-ink: oklch(0.25 0.02 265);
  --color-tcb04-mut: #555c69;
  --color-tcb04-mut: oklch(0.46 0.02 265);
  --color-tcb04-line: #eceef2;
  --color-tcb04-line: oklch(0.945 0.006 265);
  --color-tcb04-hover: #f8f9fb;
  --color-tcb04-hover: oklch(0.982 0.003 265);
  --color-tcb04-chip: #f0f2f5;
  --color-tcb04-chip: oklch(0.96 0.005 265);
  --color-tcb04-acc: #2f7de1;
  --color-tcb04-acc: oklch(0.6 0.17 255);
  --font-tcb04-sans: 'DM Sans', system-ui, sans-serif;
  --shadow-tcb04-panel: 0 18px 40px -30px rgb(16 24 40 / 0.5);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-04 {
  width: 100%;
  min-height: 100svh;
}
```
