---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-battery-saver-toggle-live-fill-meter/"
title: "Tailwind Battery Saver Toggle with Live Fill Meter"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A switch that shows what it buys you: turning on low-power mode recolours the battery amber and extends the projected runtime from 4h 10m to 6h 45m, with the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Battery Saver Toggle with Live Fill Meter
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-battery-saver-toggle-live-fill-meter/

A switch that shows what it buys you: turning on low-power mode recolours the battery amber and extends the projected runtime from 4h 10m to 6h 45m, with the estimate bar physically growing. The consequence is the interface.
## HTML
```html
<section class="ttg-45 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg45-bg font-ttg45-sans" aria-label="Battery saver toggle">
  <label for="ttg-45-sw" class="w-[min(370px,100%)] flex flex-col gap-5 p-7 rounded-[24px] cursor-pointer bg-white border border-ttg45-edge shadow-[0_24px_50px_-36px_oklch(0.4_0.04_150/0.5)] has-checked:[&_.ttg45-cell]:bg-ttg45-saver has-checked:[&_.ttg45-fill]:w-[62%] has-checked:[&_.ttg45-fill]:bg-ttg45-saver has-checked:[&_.ttg45-now]:opacity-0 has-checked:[&_.ttg45-saved]:opacity-100 has-checked:[&_.ttg45-mode]:text-ttg45-saver">
    <span class="flex items-center justify-between gap-5">
      <span class="flex items-center gap-3">
        <span aria-hidden="true" class="relative flex items-center gap-[3px] w-11 h-6 px-1 rounded-md border-2 border-ttg45-shell after:content-[''] after:absolute after:-right-[5px] after:top-1/2 after:-mt-1.5 after:w-[3px] after:h-3 after:rounded-r-sm after:bg-ttg45-shell">
          <i class="ttg45-cell flex-1 h-3 rounded-[2px] bg-ttg45-ok transition-colors duration-300"></i>
          <i class="ttg45-cell flex-1 h-3 rounded-[2px] bg-ttg45-ok transition-colors duration-300"></i>
          <i class="ttg45-cell flex-1 h-3 rounded-[2px] bg-ttg45-ok transition-colors duration-300"></i>
        </span>
        <span class="flex flex-col gap-0.5">
          <b class="text-[15.5px] font-bold text-ttg45-ink">Low power mode</b>
          <span class="ttg45-mode text-[12.5px] text-ttg45-mute transition-colors duration-300">Throttles background sync</span>
        </span>
      </span>
      <input type="checkbox" id="ttg-45-sw" role="switch" aria-label="Low power mode" class="appearance-none shrink-0 w-13 h-7.5 rounded-full bg-ttg45-trackoff relative cursor-pointer transition-colors duration-300 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-6.5 before:h-6.5 before:rounded-full before:bg-white before:shadow-[0_2px_5px_oklch(0.3_0.03_150/0.35)] before:transition-transform before:duration-300 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg45-saver checked:before:translate-x-[22px] focus-visible:outline-3 focus-visible:outline-ttg45-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
    </span>
    <span class="flex flex-col gap-2 pt-4 border-t border-ttg45-edge">
      <span class="flex items-baseline justify-between gap-4">
        <span class="text-[12px] tracking-[0.08em] uppercase text-ttg45-mute">Estimated runtime</span>
        <span class="relative block w-28 h-7">
          <b class="ttg45-now absolute inset-0 text-right text-[19px] font-extrabold text-ttg45-ink transition-opacity duration-300">4h 10m</b>
          <b class="ttg45-saved absolute inset-0 text-right text-[19px] font-extrabold text-ttg45-saver opacity-0 transition-opacity duration-300">6h 45m</b>
        </span>
      </span>
      <span aria-hidden="true" class="block h-2.5 rounded-full bg-ttg45-meter overflow-hidden">
        <i class="ttg45-fill block h-full w-[38%] rounded-full bg-ttg45-ok transition-[width,background-color] duration-500 ease-[cubic-bezier(0.3,1,0.35,1.02)] motion-reduce:transition-none"></i>
      </span>
    </span>
  </label>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg45-bg: #eef3ef;
  --color-ttg45-bg: oklch(0.95 0.01 155);
  --color-ttg45-edge: #e4eae6;
  --color-ttg45-edge: oklch(0.93 0.008 155);
  --color-ttg45-shell: #9aa39d;
  --color-ttg45-shell: oklch(0.68 0.012 155);
  --color-ttg45-ok: #2f9e63;
  --color-ttg45-ok: oklch(0.63 0.16 155);
  --color-ttg45-saver: #c07a12;
  --color-ttg45-saver: oklch(0.62 0.14 75);
  --color-ttg45-meter: #e6ebe7;
  --color-ttg45-meter: oklch(0.93 0.008 155);
  --color-ttg45-trackoff: #dde3df;
  --color-ttg45-trackoff: oklch(0.9 0.008 155);
  --color-ttg45-ink: #1f2a24;
  --color-ttg45-ink: oklch(0.26 0.015 155);
  --color-ttg45-mute: #6f7a74;
  --color-ttg45-mute: oklch(0.56 0.012 155);
  --color-ttg45-focus: #2a6fd6;
  --color-ttg45-focus: oklch(0.54 0.17 255);
  --font-ttg45-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-45 {
  width: 100%;
  min-height: 100svh;
}

.ttg-45 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
