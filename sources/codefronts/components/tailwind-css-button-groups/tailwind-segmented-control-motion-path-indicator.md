---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-segmented-control-motion-path-indicator/"
title: "Tailwind Segmented Control with Motion-Path Comet Indicator"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A four-way mode switch whose thumb travels an arc instead of a straight line, trailed by a blurred comet tail that lags behind on a slower curve."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Segmented Control with Motion-Path Comet Indicator
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-segmented-control-motion-path-indicator/

A four-way mode switch whose thumb travels an arc instead of a straight line, trailed by a blurred comet tail that lags behind on a slower curve. The motion path is an arbitrary property — [offset-path:path('M43,28C123,6,203,6,283,28')] — and each radio moves it with group-has-[#tbg02-3:checked]/seg:[offset-distance:66.666%]. A live status line under the control reports the active mode, still with no JavaScript.
## HTML
```html
<section class="tbg-02 w-full min-h-svh grid place-items-center bg-tbg02-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-tbg02-glow),transparent_70%)] px-5 py-14 font-tbg02-sans text-tbg02-ink" aria-label="Motion-path comet segmented control demo">
  <div class="group/wrap grid gap-4">
    <p id="tbg02-label" class="ml-1 text-xs font-bold uppercase tracking-[0.16em] text-tbg02-acc">Signal mode</p>
    <div role="radiogroup" aria-labelledby="tbg02-label" class="group/seg relative grid w-fit max-w-full grid-cols-[repeat(4,80px)] rounded-2xl border border-tbg02-line bg-tbg02-well p-1.5 shadow-[inset_0_2px_8px_rgb(0_0_0/0.5)]">
      <label class="relative z-2 grid min-h-11 cursor-pointer place-items-center rounded-lg text-[14.5px] font-semibold text-tbg02-mut transition-colors duration-300 hover:text-tbg02-ink has-checked:text-tbg02-on has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tbg02-acc"><input type="radio" name="tbg02" id="tbg02-1" class="sr-only" checked>Live</label>
      <label class="relative z-2 grid min-h-11 cursor-pointer place-items-center rounded-lg text-[14.5px] font-semibold text-tbg02-mut transition-colors duration-300 hover:text-tbg02-ink has-checked:text-tbg02-on has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tbg02-acc"><input type="radio" name="tbg02" id="tbg02-2" class="sr-only">Pulse</label>
      <label class="relative z-2 grid min-h-11 cursor-pointer place-items-center rounded-lg text-[14.5px] font-semibold text-tbg02-mut transition-colors duration-300 hover:text-tbg02-ink has-checked:text-tbg02-on has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tbg02-acc"><input type="radio" name="tbg02" id="tbg02-3" class="sr-only">Wave</label>
      <label class="relative z-2 grid min-h-11 cursor-pointer place-items-center rounded-lg text-[14.5px] font-semibold text-tbg02-mut transition-colors duration-300 hover:text-tbg02-ink has-checked:text-tbg02-on has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tbg02-acc"><input type="radio" name="tbg02" id="tbg02-4" class="sr-only">Idle</label>
      <span aria-hidden="true" class="pointer-events-none absolute top-0 left-0 z-0 h-11 w-[74px] rounded-[11px] bg-linear-120 from-tbg02-acc to-tbg02-acc3 opacity-60 blur-[9px] [offset-path:path('M43,28C123,6,203,6,283,28')] [offset-rotate:0deg] [offset-distance:0%] transition-[offset-distance] duration-800 ease-[cubic-bezier(.5,0,.2,1)] group-has-[#tbg02-2:checked]/seg:[offset-distance:33.333%] group-has-[#tbg02-3:checked]/seg:[offset-distance:66.666%] group-has-[#tbg02-4:checked]/seg:[offset-distance:100%] motion-reduce:duration-200 motion-reduce:[offset-path:path('M43,28L283,28')]"></span>
      <span aria-hidden="true" class="pointer-events-none absolute top-0 left-0 z-1 h-11 w-[74px] rounded-[11px] bg-linear-120 from-tbg02-acc to-tbg02-acc2 shadow-[0_4px_18px_-4px_var(--color-tbg02-acc)] [offset-path:path('M43,28C123,6,203,6,283,28')] [offset-rotate:0deg] [offset-distance:0%] transition-[offset-distance] duration-500 ease-[cubic-bezier(.5,0,.2,1)] group-has-[#tbg02-2:checked]/seg:[offset-distance:33.333%] group-has-[#tbg02-3:checked]/seg:[offset-distance:66.666%] group-has-[#tbg02-4:checked]/seg:[offset-distance:100%] motion-reduce:duration-200 motion-reduce:[offset-path:path('M43,28L283,28')]"></span>
    </div>
    <p class="ml-1 flex items-center gap-2.5 font-tbg02-mono text-xs text-tbg02-mut">
      <span aria-hidden="true" class="size-2 rounded-full bg-tbg02-acc shadow-[0_0_10px_var(--color-tbg02-acc)] group-has-[#tbg02-4:checked]/wrap:bg-tbg02-mut group-has-[#tbg02-4:checked]/wrap:shadow-none"></span>
      <span class="group-has-[#tbg02-1:checked]/wrap:inline hidden">Streaming · 60 Hz refresh</span>
      <span class="group-has-[#tbg02-2:checked]/wrap:inline hidden">Heartbeat · every 5 s</span>
      <span class="group-has-[#tbg02-3:checked]/wrap:inline hidden">Batched · rolling 1 min</span>
      <span class="group-has-[#tbg02-4:checked]/wrap:inline hidden">Paused · no data sent</span>
    </p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg02-bg: #06070f;
  --color-tbg02-glow: #12163a;
  --color-tbg02-well: #12142a;
  --color-tbg02-line: #222647;
  --color-tbg02-ink: #e6e9ff;
  --color-tbg02-mut: #9aa2cc;
  --color-tbg02-mut: oklch(0.72 0.05 275);
  --color-tbg02-on: #04121c;
  --color-tbg02-acc: #38f2c0;
  --color-tbg02-acc: oklch(0.86 0.16 170);
  --color-tbg02-acc2: #3aa0ff;
  --color-tbg02-acc2: oklch(0.69 0.17 250);
  --color-tbg02-acc3: #8a5bff;
  --color-tbg02-acc3: oklch(0.6 0.23 290);
  --font-tbg02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tbg02-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-02 {
  width: 100%;
  min-height: 100svh;
}
```
