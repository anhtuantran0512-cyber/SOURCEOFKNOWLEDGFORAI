---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/ios-style-tailwind-tab-close-button/"
title: "iOS-Style Tailwind Tab Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Safari's tab-overview dismiss: a 28px translucent systemGray circle with backdrop-blur-md, legible over any page thumbnail."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS-Style Tailwind Tab Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/ios-style-tailwind-tab-close-button/

Safari's tab-overview dismiss: a 28px translucent systemGray circle with backdrop-blur-md, legible over any page thumbnail. The port fixes the original's biggest flaw — a 28px tap target — by making the button a 44px size-11 hit area and the circle a child span, and shows two tabs side by side so you can judge legibility over light and dark thumbnails.
## HTML
```html
<section class="tcb-03 w-full min-h-svh grid place-items-center bg-tcb03-bg bg-[radial-gradient(120%_130%_at_20%_0%,var(--color-tcb03-glow1),transparent_55%),radial-gradient(110%_120%_at_90%_100%,var(--color-tcb03-glow2),transparent_55%)] px-6 py-12 font-tcb03-sans" aria-label="iOS-style tab close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <ul class="grid w-full max-w-[36rem] grid-cols-2 gap-4 max-[26rem]:grid-cols-1" aria-label="Open tabs">
      <li class="relative aspect-4/3 overflow-hidden rounded-[1.25rem] bg-[linear-gradient(150deg,var(--color-tcb03-t1a),var(--color-tcb03-t1b)_55%,var(--color-tcb03-t1c))] shadow-[0_24px_50px_-24px_rgb(0_0_0/0.6)]">
        <div aria-hidden="true" class="absolute inset-x-4 top-14 grid gap-2"><span class="h-2 w-3/4 rounded-full bg-white/70"></span><span class="h-2 w-1/2 rounded-full bg-white/50"></span></div>
        <button type="button" aria-label="Close tab: apple.com" class="group absolute top-1 end-1 grid size-11 cursor-pointer place-items-center rounded-full focus-visible:outline-none">
          <span aria-hidden="true" class="relative size-7 rounded-full bg-[rgb(120_120_128/0.36)] backdrop-blur-md transition duration-250 ease-[cubic-bezier(.34,1.56,.64,1)] before:absolute before:top-1/2 before:left-1/2 before:h-[1.5px] before:w-3 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-white/92 after:absolute after:top-1/2 after:left-1/2 after:h-[1.5px] after:w-3 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-white/92 group-hover:bg-[rgb(120_120_128/0.5)] group-active:scale-88 group-active:duration-120 group-focus-visible:outline-[2.5px] group-focus-visible:outline-offset-2 group-focus-visible:outline-white motion-reduce:transition-none"></span>
        </button>
        <div class="absolute inset-x-0 bottom-0 bg-[rgb(30_30_36/0.45)] px-3.5 py-3 backdrop-blur-md"><span class="text-[13px] font-medium text-white">apple.com</span></div>
      </li>
      <li class="relative aspect-4/3 overflow-hidden rounded-[1.25rem] bg-[linear-gradient(160deg,var(--color-tcb03-t2a),var(--color-tcb03-t2b))] shadow-[0_24px_50px_-24px_rgb(0_0_0/0.6)]">
        <div aria-hidden="true" class="absolute inset-x-4 top-14 grid grid-cols-3 gap-2"><span class="aspect-square rounded-lg bg-white/85"></span><span class="aspect-square rounded-lg bg-white/60"></span><span class="aspect-square rounded-lg bg-white/85"></span></div>
        <button type="button" aria-label="Close tab: notes.example.com" class="group absolute top-1 end-1 grid size-11 cursor-pointer place-items-center rounded-full focus-visible:outline-none">
          <span aria-hidden="true" class="relative size-7 rounded-full bg-[rgb(120_120_128/0.36)] backdrop-blur-md transition duration-250 ease-[cubic-bezier(.34,1.56,.64,1)] before:absolute before:top-1/2 before:left-1/2 before:h-[1.5px] before:w-3 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-white/92 after:absolute after:top-1/2 after:left-1/2 after:h-[1.5px] after:w-3 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-white/92 group-hover:bg-[rgb(120_120_128/0.5)] group-active:scale-88 group-active:duration-120 group-focus-visible:outline-[2.5px] group-focus-visible:outline-offset-2 group-focus-visible:outline-white motion-reduce:transition-none"></span>
        </button>
        <div class="absolute inset-x-0 bottom-0 bg-[rgb(30_30_36/0.45)] px-3.5 py-3 backdrop-blur-md"><span class="text-[13px] font-medium text-white">notes.example.com</span></div>
      </li>
    </ul>
    <p aria-hidden="true" class="rounded-full bg-black/25 px-3.5 py-2 font-tcb03-mono text-[11.5px] text-white/90 ring-1 ring-white/15">size-11 hit area · size-7 circle · backdrop-blur-md · active:scale-88</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb03-bg: #3b2f5c;
  --color-tcb03-bg: oklch(0.35 0.06 280);
  --color-tcb03-glow1: #4f86d6;
  --color-tcb03-glow1: oklch(0.6 0.14 250);
  --color-tcb03-glow2: #a2479f;
  --color-tcb03-glow2: oklch(0.55 0.16 320);
  --color-tcb03-t1a: #b6d6f2;
  --color-tcb03-t1a: oklch(0.85 0.06 230);
  --color-tcb03-t1b: #9187d6;
  --color-tcb03-t1b: oklch(0.7 0.1 280);
  --color-tcb03-t1c: #a0629e;
  --color-tcb03-t1c: oklch(0.6 0.13 320);
  --color-tcb03-t2a: #f4efe4;
  --color-tcb03-t2a: oklch(0.95 0.015 85);
  --color-tcb03-t2b: #d9c9a8;
  --color-tcb03-t2b: oklch(0.83 0.05 80);
  --font-tcb03-sans: 'Geist', system-ui, sans-serif;
  --font-tcb03-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-03 {
  width: 100%;
  min-height: 100svh;
}
```
