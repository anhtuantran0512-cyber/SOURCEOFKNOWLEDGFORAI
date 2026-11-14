---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/tailwind-slide-toggle-on-off-labels/"
title: "Tailwind Slide Toggle with ON/OFF Labels — GPU translate3d"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "A wider switch that prints ON and OFF inside its own track via before:content-['ON'] / after:content-['OFF'], cross-fading on group-has-checked:."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide Toggle with ON/OFF Labels — GPU translate3d
Source: https://codefronts.com/components/tailwind-css-checkboxes/tailwind-slide-toggle-on-off-labels/

A wider switch that prints ON and OFF inside its own track via before:content-['ON'] / after:content-['OFF'], cross-fading on group-has-checked:. The thumb glides on transform-gpu with will-change-transform, and each row card picks up an accent edge when on.
## HTML
```html
<section class="tcb-07 w-full min-h-svh grid place-items-center bg-tcb07-bg px-5 py-14 font-tcb07-sans text-tcb07-ink selection:bg-tcb07-acc selection:text-white" aria-label="Smooth slide toggles">
  <div class="flex w-full max-w-[25rem] flex-col gap-3.5">
    <label class="group flex min-h-15 cursor-pointer items-center justify-between gap-4 rounded-xl border border-tcb07-line bg-white px-4.5 py-3.5 transition-colors duration-300 has-checked:border-tcb07-acc/40"><span class="text-[15px] font-semibold">Auto-save drafts</span>
      <input type="checkbox" class="peer sr-only" checked>
      <span aria-hidden="true" class="relative h-[30px] w-[66px] flex-none overflow-hidden rounded-full bg-tcb07-off font-tcb07-mono text-[10px] font-bold tracking-[0.1em] transition-colors duration-300 peer-checked:bg-tcb07-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb07-acc before:absolute before:left-[11px] before:top-0 before:flex before:h-full before:items-center before:text-white before:opacity-0 before:transition-opacity before:content-['ON'] after:absolute after:right-[10px] after:top-0 after:flex after:h-full after:items-center after:text-tcb07-offink after:transition-opacity after:content-['OFF'] group-has-checked:before:opacity-100 group-has-checked:after:opacity-0 motion-reduce:transition-none">
        <span class="absolute left-[3px] top-[3px] size-6 transform-gpu rounded-full bg-white shadow-tcb07-thumb transition-transform duration-300 ease-[cubic-bezier(.4,.9,.3,1)] will-change-transform group-has-checked:translate-x-9 motion-reduce:transition-none"></span>
      </span>
    </label>
    <label class="group flex min-h-15 cursor-pointer items-center justify-between gap-4 rounded-xl border border-tcb07-line bg-white px-4.5 py-3.5 transition-colors duration-300 has-checked:border-tcb07-acc/40"><span class="text-[15px] font-semibold">Compact density</span>
      <input type="checkbox" class="peer sr-only">
      <span aria-hidden="true" class="relative h-[30px] w-[66px] flex-none overflow-hidden rounded-full bg-tcb07-off font-tcb07-mono text-[10px] font-bold tracking-[0.1em] transition-colors duration-300 peer-checked:bg-tcb07-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb07-acc before:absolute before:left-[11px] before:top-0 before:flex before:h-full before:items-center before:text-white before:opacity-0 before:transition-opacity before:content-['ON'] after:absolute after:right-[10px] after:top-0 after:flex after:h-full after:items-center after:text-tcb07-offink after:transition-opacity after:content-['OFF'] group-has-checked:before:opacity-100 group-has-checked:after:opacity-0 motion-reduce:transition-none">
        <span class="absolute left-[3px] top-[3px] size-6 transform-gpu rounded-full bg-white shadow-tcb07-thumb transition-transform duration-300 ease-[cubic-bezier(.4,.9,.3,1)] will-change-transform group-has-checked:translate-x-9 motion-reduce:transition-none"></span>
      </span>
    </label>
    <label class="group flex min-h-15 cursor-pointer items-center justify-between gap-4 rounded-xl border border-tcb07-line bg-white px-4.5 py-3.5 transition-colors duration-300 has-checked:border-tcb07-acc/40"><span class="text-[15px] font-semibold">Beta features</span>
      <input type="checkbox" class="peer sr-only">
      <span aria-hidden="true" class="relative h-[30px] w-[66px] flex-none overflow-hidden rounded-full bg-tcb07-off font-tcb07-mono text-[10px] font-bold tracking-[0.1em] transition-colors duration-300 peer-checked:bg-tcb07-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb07-acc before:absolute before:left-[11px] before:top-0 before:flex before:h-full before:items-center before:text-white before:opacity-0 before:transition-opacity before:content-['ON'] after:absolute after:right-[10px] after:top-0 after:flex after:h-full after:items-center after:text-tcb07-offink after:transition-opacity after:content-['OFF'] group-has-checked:before:opacity-100 group-has-checked:after:opacity-0 motion-reduce:transition-none">
        <span class="absolute left-[3px] top-[3px] size-6 transform-gpu rounded-full bg-white shadow-tcb07-thumb transition-transform duration-300 ease-[cubic-bezier(.4,.9,.3,1)] will-change-transform group-has-checked:translate-x-9 motion-reduce:transition-none"></span>
      </span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb07-bg: #eef2f3;
  --color-tcb07-bg: oklch(0.957 0.005 210);
  --color-tcb07-ink: #28323a;
  --color-tcb07-ink: oklch(0.3 0.02 230);
  --color-tcb07-line: #dde3e5;
  --color-tcb07-line: oklch(0.9 0.008 210);
  --color-tcb07-off: #cdd5d8;
  --color-tcb07-off: oklch(0.86 0.01 210);
  --color-tcb07-offink: #3f4c52;
  --color-tcb07-offink: oklch(0.41 0.02 220);
  --color-tcb07-acc: #137f8f;
  --color-tcb07-acc: oklch(0.54 0.1 205);
  --font-tcb07-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcb07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcb07-thumb: 0 2px 6px rgb(20 30 40 / 0.4);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-07 {
  width: 100%;
  min-height: 100svh;
}
```
