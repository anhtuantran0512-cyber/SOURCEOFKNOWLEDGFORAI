---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/radial-ripple-expand-tailwind-hamburger-menu/"
title: "Radial Ripple Expand Tailwind Hamburger Menu"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Five action buttons fan out along a perfect quarter-circle arc, their positions computed by the browser itself &mdash; sin() and cos() turn an index and a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Radial Ripple Expand Tailwind Hamburger Menu
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/radial-ripple-expand-tailwind-hamburger-menu/

Five action buttons fan out along a perfect quarter-circle arc, their positions computed by the browser itself &mdash; sin() and cos() turn an index and a radius into coordinates, with no JS math and no hand-tuned offsets. This is the per-item index pattern at its most extreme: every button carries only its --i, and one arbitrary translate utility does the geometry.
## HTML
```html
<section class="thb-24 w-full min-h-svh grid justify-center content-start bg-thb24-bg font-thb24-sans text-thb24-ink px-5 py-9" aria-label="Radial ripple fan menu demo">
  <div class="group relative w-[min(400px,88vw)] h-130 rounded-3xl overflow-hidden bg-thb24-bg border border-thb24-edge">
    <input type="checkbox" id="thb24-t" class="peer absolute w-px h-px overflow-hidden whitespace-nowrap [clip-path:inset(50%)]">
    <div class="absolute inset-0" aria-hidden="true">
      <div class="absolute inset-0 bg-thb24-bg [background-image:radial-gradient(120%_90%_at_70%_20%,oklch(0.3_0.05_230/0.8),transparent_55%),repeating-linear-gradient(0deg,transparent_0_46px,oklch(1_0_0/0.045)_46px_47px),repeating-linear-gradient(90deg,transparent_0_46px,oklch(1_0_0/0.045)_46px_47px)] after:content-[''] after:absolute after:-left-[10%] after:top-[30%] after:w-[120%] after:h-22.5 after:-rotate-14 after:rounded-full after:bg-[oklch(0.45_0.07_230/0.35)] after:blur-[2px]"></div>
      <div class="absolute left-[24%] top-[30%] w-2.75 h-2.75 -rotate-45 rounded-[50%_50%_50%_0] bg-thb24-acc2 shadow-[0_0_0_3px_oklch(0.7_0.14_210/0.25)]"></div>
      <div class="absolute left-[62%] top-[22%] w-2.75 h-2.75 -rotate-45 rounded-[50%_50%_50%_0] bg-thb24-acc2 shadow-[0_0_0_3px_oklch(0.7_0.14_210/0.25)]"></div>
      <div class="absolute left-[45%] top-[56%] w-2.75 h-2.75 -rotate-45 rounded-[50%_50%_50%_0] bg-thb24-acc2 shadow-[0_0_0_3px_oklch(0.7_0.14_210/0.25)]"></div>
    </div>
    <div class="absolute right-11 bottom-11 w-0 h-0 pointer-events-none" aria-hidden="true">
      <i class="absolute -left-13.5 -top-13.5 w-27 h-27 rounded-full border-[1.5px] border-[color-mix(in_oklch,var(--color-thb24-acc)_60%,transparent)] scale-30 opacity-0 group-has-checked:animate-thb24-ripple motion-reduce:animate-none"></i>
      <i class="absolute -left-13.5 -top-13.5 w-27 h-27 rounded-full border-[1.5px] border-[color-mix(in_oklch,var(--color-thb24-acc)_60%,transparent)] scale-30 opacity-0 delay-[120ms] group-has-checked:animate-thb24-ripple group-has-checked:[animation-delay:120ms] motion-reduce:animate-none"></i>
      <i class="absolute -left-13.5 -top-13.5 w-27 h-27 rounded-full border-[1.5px] border-[color-mix(in_oklch,var(--color-thb24-acc)_60%,transparent)] scale-30 opacity-0 group-has-checked:animate-thb24-ripple group-has-checked:[animation-delay:240ms] motion-reduce:animate-none"></i>
    </div>
    <nav aria-label="Quick actions" class="absolute right-11 bottom-11 w-0 h-0">
      <a href="#route" style="--i:0" class="group/i absolute -left-6 -top-6 grid place-items-center w-12 h-12 rounded-full bg-thb24-item border border-thb24-itemedge text-thb24-ink no-underline scale-40 opacity-0 pointer-events-none [--n:5] [--arc:90deg] [--r:108px] [--a:calc(90deg+(var(--i)/(var(--n)-1))*var(--arc))] [transition:translate_.5s_var(--ease-thb24),scale_.4s_var(--ease-thb24),opacity_.25s,background_.2s,border-color_.2s] hover:bg-thb24-itemhover hover:border-thb24-acc focus-visible:border-thb24-acc focus-visible:outline-2 focus-visible:outline-thb24-acc focus-visible:outline-offset-2 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:pointer-events-auto group-has-checked:[translate:calc(cos(var(--a))*var(--r))_calc(sin(var(--a))*var(--r)*-1)] group-has-checked:[transition-delay:calc(var(--i)*45ms)] motion-reduce:[transition:opacity_.15s]">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H14a3 3 0 0 0 0-6h-4a3 3 0 0 1 0-6h5.5"/></svg>
        <span class="absolute right-[calc(100%+10px)] top-1/2 -translate-y-1/2 px-2.5 py-1.25 rounded-[7px] bg-thb24-chip text-thb24-chipink text-[11.5px] font-bold whitespace-nowrap opacity-0 scale-90 pointer-events-none transition-[opacity,scale] duration-150 group-hover/i:opacity-100 group-hover/i:scale-100 group-focus-visible/i:opacity-100 group-focus-visible/i:scale-100">Route</span>
      </a>
      <a href="#layers" style="--i:1" class="group/i absolute -left-6 -top-6 grid place-items-center w-12 h-12 rounded-full bg-thb24-item border border-thb24-itemedge text-thb24-ink no-underline scale-40 opacity-0 pointer-events-none [--n:5] [--arc:90deg] [--r:108px] [--a:calc(90deg+(var(--i)/(var(--n)-1))*var(--arc))] [transition:translate_.5s_var(--ease-thb24),scale_.4s_var(--ease-thb24),opacity_.25s,background_.2s,border-color_.2s] hover:bg-thb24-itemhover hover:border-thb24-acc focus-visible:border-thb24-acc focus-visible:outline-2 focus-visible:outline-thb24-acc focus-visible:outline-offset-2 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:pointer-events-auto group-has-checked:[translate:calc(cos(var(--a))*var(--r))_calc(sin(var(--a))*var(--r)*-1)] group-has-checked:[transition-delay:calc(var(--i)*45ms)] motion-reduce:[transition:opacity_.15s]">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="m12 3 9 5-9 5-9-5Z"/><path d="m5.5 11.5-2.5 1.5 9 5 9-5-2.5-1.5"/></svg>
        <span class="absolute right-[calc(100%+10px)] top-1/2 -translate-y-1/2 px-2.5 py-1.25 rounded-[7px] bg-thb24-chip text-thb24-chipink text-[11.5px] font-bold whitespace-nowrap opacity-0 scale-90 pointer-events-none transition-[opacity,scale] duration-150 group-hover/i:opacity-100 group-hover/i:scale-100 group-focus-visible/i:opacity-100 group-focus-visible/i:scale-100">Layers</span>
      </a>
      <a href="#pin" style="--i:2" class="group/i absolute -left-6 -top-6 grid place-items-center w-12 h-12 rounded-full bg-thb24-item border border-thb24-itemedge text-thb24-ink no-underline scale-40 opacity-0 pointer-events-none [--n:5] [--arc:90deg] [--r:108px] [--a:calc(90deg+(var(--i)/(var(--n)-1))*var(--arc))] [transition:translate_.5s_var(--ease-thb24),scale_.4s_var(--ease-thb24),opacity_.25s,background_.2s,border-color_.2s] hover:bg-thb24-itemhover hover:border-thb24-acc focus-visible:border-thb24-acc focus-visible:outline-2 focus-visible:outline-thb24-acc focus-visible:outline-offset-2 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:pointer-events-auto group-has-checked:[translate:calc(cos(var(--a))*var(--r))_calc(sin(var(--a))*var(--r)*-1)] group-has-checked:[transition-delay:calc(var(--i)*45ms)] motion-reduce:[transition:opacity_.15s]">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="M12 21s-6.5-5.5-6.5-11a6.5 6.5 0 0 1 13 0C18.5 15.5 12 21 12 21Z"/><circle cx="12" cy="10" r="2.2"/></svg>
        <span class="absolute right-[calc(100%+10px)] top-1/2 -translate-y-1/2 px-2.5 py-1.25 rounded-[7px] bg-thb24-chip text-thb24-chipink text-[11.5px] font-bold whitespace-nowrap opacity-0 scale-90 pointer-events-none transition-[opacity,scale] duration-150 group-hover/i:opacity-100 group-hover/i:scale-100 group-focus-visible/i:opacity-100 group-focus-visible/i:scale-100">Drop pin</span>
      </a>
      <a href="#measure" style="--i:3" class="group/i absolute -left-6 -top-6 grid place-items-center w-12 h-12 rounded-full bg-thb24-item border border-thb24-itemedge text-thb24-ink no-underline scale-40 opacity-0 pointer-events-none [--n:5] [--arc:90deg] [--r:108px] [--a:calc(90deg+(var(--i)/(var(--n)-1))*var(--arc))] [transition:translate_.5s_var(--ease-thb24),scale_.4s_var(--ease-thb24),opacity_.25s,background_.2s,border-color_.2s] hover:bg-thb24-itemhover hover:border-thb24-acc focus-visible:border-thb24-acc focus-visible:outline-2 focus-visible:outline-thb24-acc focus-visible:outline-offset-2 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:pointer-events-auto group-has-checked:[translate:calc(cos(var(--a))*var(--r))_calc(sin(var(--a))*var(--r)*-1)] group-has-checked:[transition-delay:calc(var(--i)*45ms)] motion-reduce:[transition:opacity_.15s]">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><path d="m4 17 13-13 3 3-13 13H4Z"/><path d="m9.5 8.5 1.5 1.5M12.5 5.5 14 7"/></svg>
        <span class="absolute right-[calc(100%+10px)] top-1/2 -translate-y-1/2 px-2.5 py-1.25 rounded-[7px] bg-thb24-chip text-thb24-chipink text-[11.5px] font-bold whitespace-nowrap opacity-0 scale-90 pointer-events-none transition-[opacity,scale] duration-150 group-hover/i:opacity-100 group-hover/i:scale-100 group-focus-visible/i:opacity-100 group-focus-visible/i:scale-100">Measure</span>
      </a>
      <a href="#share" style="--i:4" class="group/i absolute -left-6 -top-6 grid place-items-center w-12 h-12 rounded-full bg-thb24-item border border-thb24-itemedge text-thb24-ink no-underline scale-40 opacity-0 pointer-events-none [--n:5] [--arc:90deg] [--r:108px] [--a:calc(90deg+(var(--i)/(var(--n)-1))*var(--arc))] [transition:translate_.5s_var(--ease-thb24),scale_.4s_var(--ease-thb24),opacity_.25s,background_.2s,border-color_.2s] hover:bg-thb24-itemhover hover:border-thb24-acc focus-visible:border-thb24-acc focus-visible:outline-2 focus-visible:outline-thb24-acc focus-visible:outline-offset-2 group-has-checked:scale-100 group-has-checked:opacity-100 group-has-checked:pointer-events-auto group-has-checked:[translate:calc(cos(var(--a))*var(--r))_calc(sin(var(--a))*var(--r)*-1)] group-has-checked:[transition-delay:calc(var(--i)*45ms)] motion-reduce:[transition:opacity_.15s]">
        <svg viewBox="0 0 24 24" class="w-4.75 h-4.75 fill-none stroke-current stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]" aria-hidden="true"><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="m8.3 10.8 7.4-3.6M8.3 13.2l7.4 3.6"/></svg>
        <span class="absolute right-[calc(100%+10px)] top-1/2 -translate-y-1/2 px-2.5 py-1.25 rounded-[7px] bg-thb24-chip text-thb24-chipink text-[11.5px] font-bold whitespace-nowrap opacity-0 scale-90 pointer-events-none transition-[opacity,scale] duration-150 group-hover/i:opacity-100 group-hover/i:scale-100 group-focus-visible/i:opacity-100 group-focus-visible/i:scale-100">Share</span>
      </a>
    </nav>
    <label for="thb24-t" class="absolute right-4 bottom-4 grid place-items-center w-14 h-14 rounded-full bg-linear-[150deg,var(--color-thb24-acc),oklch(0.62_0.14_190)] text-thb24-bg cursor-pointer select-none shadow-[0_16px_32px_-12px_color-mix(in_oklch,var(--color-thb24-acc)_55%,transparent)] transition-[rotate,scale] duration-400 ease-thb24 hover:scale-106 active:scale-94 peer-focus-visible:outline-2 peer-focus-visible:outline-thb24-acc peer-focus-visible:outline-offset-3 group-has-checked:rotate-135 motion-reduce:transition-none">
      <span class="relative block w-4.5 h-3" aria-hidden="true">
        <i class="absolute left-0 top-0 w-4.5 h-[2.2px] rounded-sm bg-current transition-[translate,rotate] duration-300 group-has-checked:translate-y-[5px] group-has-checked:rotate-45 motion-reduce:transition-none"></i>
        <i class="absolute left-0 top-[5px] w-4.5 h-[2.2px] rounded-sm bg-current transition-[opacity] duration-200 group-has-checked:opacity-0 motion-reduce:transition-none"></i>
        <i class="absolute left-0 top-2.5 w-4.5 h-[2.2px] rounded-sm bg-current transition-[translate,rotate] duration-300 group-has-checked:-translate-y-[5px] group-has-checked:-rotate-45 motion-reduce:transition-none"></i>
      </span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb24-bg: #2b3444;
  --color-thb24-bg: oklch(0.23 0.03 250);
  --color-thb24-edge: #454f61;
  --color-thb24-edge: oklch(0.33 0.03 250);
  --color-thb24-item: #3a4457;
  --color-thb24-item: oklch(0.3 0.035 250);
  --color-thb24-itemedge: #5d6979;
  --color-thb24-itemedge: oklch(0.42 0.04 250);
  --color-thb24-itemhover: #48536a;
  --color-thb24-itemhover: oklch(0.36 0.05 250);
  --color-thb24-ink: #f0f1f5;
  --color-thb24-ink: oklch(0.95 0.008 250);
  --color-thb24-chip: #f0f1f5;
  --color-thb24-chip: oklch(0.95 0.008 250);
  --color-thb24-chipink: #2a3140;
  --color-thb24-chipink: oklch(0.22 0.02 250);
  --color-thb24-acc: #63e0a8;
  --color-thb24-acc: oklch(0.8 0.15 150);
  --color-thb24-acc2: #4fbcd8;
  --color-thb24-acc2: oklch(0.7 0.14 210);
  --font-thb24-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb24-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb24: cubic-bezier(0.25, 1.3, 0.35, 1);
  --animate-thb24-ripple: thb24-ripple 1s cubic-bezier(0.2, 0.7, 0.3, 1) forwards;
}
/* Keyframes are a rule, not a value — the @theme --animate-* entry above only names this. */

@keyframes thb24-ripple {
  0% {
    scale: 0.3;
    opacity: 0.9;
  }

  100% {
    scale: 2.6;
    opacity: 0;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-24 {
  width: 100%;
  min-height: 100svh;
}
```
