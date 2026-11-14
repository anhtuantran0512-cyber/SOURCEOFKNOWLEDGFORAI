---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/pulse-ring-checkbox-tailwind-live-status/"
title: "Pulse Ring Checkbox in Tailwind CSS — Live Status Indicator"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Round checkboxes that broadcast when on: two rings pulse outward half a cycle apart ([animation-delay:1s]), and checked rows gain a red LIVE chip."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pulse Ring Checkbox in Tailwind CSS — Live Status Indicator
Source: https://codefronts.com/components/tailwind-css-checkboxes/pulse-ring-checkbox-tailwind-live-status/

Round checkboxes that broadcast when on: two rings pulse outward half a cycle apart ([animation-delay:1s]), and checked rows gain a red LIVE chip. The rings live behind the box as siblings, so no negative z-index games.
## HTML
```html
<section class="tcb-23 w-full min-h-svh grid place-items-center bg-tcb23-bg px-5 py-14 font-tcb23-sans text-tcb23-ink selection:bg-tcb23-acc selection:text-white" aria-label="Pulse ring checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb23-line bg-white px-4 py-3">
    <label class="group flex min-h-15 cursor-pointer items-center gap-4.5 px-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-full peer-focus-visible:outline-3 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-tcb23-acc"><span class="col-start-1 row-start-1 size-6 rounded-full border-2 border-tcb23-acc opacity-0 group-has-checked:animate-tcb23-pulse motion-reduce:hidden"></span><span class="col-start-1 row-start-1 size-6 rounded-full border-2 border-tcb23-acc opacity-0 [animation-delay:1s] group-has-checked:animate-tcb23-pulse motion-reduce:hidden"></span><span class="col-start-1 row-start-1 grid size-6 place-items-center rounded-full border-2 border-tcb23-box bg-white text-white transition-colors duration-250 group-has-checked:border-tcb23-acc group-has-checked:bg-tcb23-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></span><span class="flex-1 text-[15px] group-has-checked:font-semibold">Go live now</span><span class="hidden items-center rounded-md bg-tcb23-acc px-2 py-0.5 font-tcb23-mono text-[10.5px] font-bold tracking-[0.12em] text-white group-has-checked:inline-flex">LIVE</span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-4.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-full peer-focus-visible:outline-3 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-tcb23-acc"><span class="col-start-1 row-start-1 size-6 rounded-full border-2 border-tcb23-acc opacity-0 group-has-checked:animate-tcb23-pulse motion-reduce:hidden"></span><span class="col-start-1 row-start-1 size-6 rounded-full border-2 border-tcb23-acc opacity-0 [animation-delay:1s] group-has-checked:animate-tcb23-pulse motion-reduce:hidden"></span><span class="col-start-1 row-start-1 grid size-6 place-items-center rounded-full border-2 border-tcb23-box bg-white text-white transition-colors duration-250 group-has-checked:border-tcb23-acc group-has-checked:bg-tcb23-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></span><span class="flex-1 text-[15px] group-has-checked:font-semibold">Broadcast status</span><span class="hidden items-center rounded-md bg-tcb23-acc px-2 py-0.5 font-tcb23-mono text-[10.5px] font-bold tracking-[0.12em] text-white group-has-checked:inline-flex">LIVE</span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-4.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-full peer-focus-visible:outline-3 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-tcb23-acc"><span class="col-start-1 row-start-1 size-6 rounded-full border-2 border-tcb23-acc opacity-0 group-has-checked:animate-tcb23-pulse motion-reduce:hidden"></span><span class="col-start-1 row-start-1 size-6 rounded-full border-2 border-tcb23-acc opacity-0 [animation-delay:1s] group-has-checked:animate-tcb23-pulse motion-reduce:hidden"></span><span class="col-start-1 row-start-1 grid size-6 place-items-center rounded-full border-2 border-tcb23-box bg-white text-white transition-colors duration-250 group-has-checked:border-tcb23-acc group-has-checked:bg-tcb23-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></span><span class="flex-1 text-[15px] group-has-checked:font-semibold">Ping teammates</span><span class="hidden items-center rounded-md bg-tcb23-acc px-2 py-0.5 font-tcb23-mono text-[10.5px] font-bold tracking-[0.12em] text-white group-has-checked:inline-flex">LIVE</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb23-bg: #faf4f4;
  --color-tcb23-bg: oklch(0.97 0.008 15);
  --color-tcb23-ink: #3a2727;
  --color-tcb23-ink: oklch(0.29 0.03 15);
  --color-tcb23-line: #f0dddd;
  --color-tcb23-line: oklch(0.92 0.02 15);
  --color-tcb23-box: #d49a9a;
  --color-tcb23-box: oklch(0.74 0.07 18);
  --color-tcb23-acc: #d7263d;
  --color-tcb23-acc: oklch(0.56 0.21 18);
  --font-tcb23-sans: 'Geist', system-ui, sans-serif;
  --font-tcb23-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tcb23-pulse: tcb23-pulse 2s ease-out infinite;

  @keyframes tcb23-pulse {
    0% {
      opacity: 0.5;
      scale: 1;
    }

    100% {
      opacity: 0;
      scale: 2.4;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-23 {
  width: 100%;
  min-height: 100svh;
}
```
