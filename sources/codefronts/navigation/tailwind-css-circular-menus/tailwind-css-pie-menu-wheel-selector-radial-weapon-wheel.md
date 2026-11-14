---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-pie-menu-wheel-selector-radial-weapon-wheel/"
title: "Tailwind CSS Pie Menu Wheel Selector (Radial Weapon Wheel)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A game-style selection wheel for a sketchpad: six pie slices cut with one [clip-path:polygon(&hellip;)] each, a radio group underneath so &larr;/&rarr; spin…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Pie Menu Wheel Selector (Radial Weapon Wheel)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-pie-menu-wheel-selector-radial-weapon-wheel/

A game-style selection wheel for a sketchpad: six pie slices cut with one [clip-path:polygon(&hellip;)] each, a radio group underneath so &larr;/&rarr; spin the selection natively, and the picked slice slides outward along its own bisector with a gradient fill and a warm drop shadow. A three-line script mirrors the choice into the centre readout &mdash; everything else is utilities.
## HTML
```html
<section class="tcm-03 w-full min-h-svh grid place-items-center bg-tcm03-bg bg-[radial-gradient(60%_55%_at_50%_40%,var(--color-tcm03-glow),transparent_70%)] px-5 py-14 font-tcm03-sans text-tcm03-ink antialiased" aria-label="Pie menu wheel selector demo">
  <div id="tcm-03-wheel" class="grid w-full justify-items-center gap-7">
    <header class="grid justify-items-center gap-1.5 text-center">
      <p class="font-tcm03-mono text-[11px] tracking-[0.16em] text-tcm03-acc-ink uppercase">Sketchpad · Tool wheel</p>
      <h2 class="text-[clamp(1.5rem,4vw,2rem)] font-bold tracking-[-0.03em]">Pick a tool, any way you like</h2>
    </header>
    <fieldset class="relative">
      <legend class="sr-only">Drawing tool</legend>
      <div class="relative size-[19.5rem] rounded-full bg-tcm03-rim p-2 shadow-tcm03-wheel ring-1 ring-tcm03-line sm:size-[21rem]">
        <div class="relative size-full">
        <div class="group/s pointer-events-none absolute inset-0 rotate-[calc(var(--i)*60deg)] [--i:0] [--a:calc(var(--i)*60deg-90deg)] transition-[translate] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:tcm03-nudge hover:tcm03-nudge-sm motion-reduce:transition-none">
          <input type="radio" name="tcm-03-tool" id="tcm-03-t0" value="Brush" class="peer sr-only" checked>
          <label for="tcm-03-t0" class="pointer-events-auto absolute inset-0 cursor-pointer rounded-full bg-tcm03-slice [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] transition-[background-color,color] duration-200 hover:bg-tcm03-slice-hi peer-checked:bg-linear-to-b peer-checked:from-tcm03-acc peer-checked:to-tcm03-acc2 peer-checked:text-tcm03-on">
            <span class="absolute top-[11%] left-1/2 grid -translate-x-1/2 justify-items-center gap-1 rotate-[calc(var(--i)*-60deg)] text-[11.5px] font-semibold tracking-[0.02em]"><svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 20c2 0 4-1 4-3 0-1.2-.8-2-2-2-2 0-3 2-2 5zM8 15l9.5-9.5a2 2 0 0 1 3 3L11 18"/></svg>Brush</span>
          </label>
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] ring-0 peer-focus-visible:shadow-[inset_0_0_0_3px_var(--color-tcm03-ring)]"></span>
        </div>
        <div class="group/s pointer-events-none absolute inset-0 rotate-[calc(var(--i)*60deg)] [--i:1] [--a:calc(var(--i)*60deg-90deg)] transition-[translate] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:tcm03-nudge hover:tcm03-nudge-sm motion-reduce:transition-none">
          <input type="radio" name="tcm-03-tool" id="tcm-03-t1" value="Eraser" class="peer sr-only">
          <label for="tcm-03-t1" class="pointer-events-auto absolute inset-0 cursor-pointer rounded-full bg-tcm03-slice [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] transition-[background-color,color] duration-200 hover:bg-tcm03-slice-hi peer-checked:bg-linear-to-b peer-checked:from-tcm03-acc peer-checked:to-tcm03-acc2 peer-checked:text-tcm03-on">
            <span class="absolute top-[11%] left-1/2 grid -translate-x-1/2 justify-items-center gap-1 rotate-[calc(var(--i)*-60deg)] text-[11.5px] font-semibold tracking-[0.02em]"><svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 20h13M5.5 15.5l9-9a2 2 0 0 1 2.8 0l2.2 2.2a2 2 0 0 1 0 2.8L12 19H8z"/></svg>Eraser</span>
          </label>
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] ring-0 peer-focus-visible:shadow-[inset_0_0_0_3px_var(--color-tcm03-ring)]"></span>
        </div>
        <div class="group/s pointer-events-none absolute inset-0 rotate-[calc(var(--i)*60deg)] [--i:2] [--a:calc(var(--i)*60deg-90deg)] transition-[translate] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:tcm03-nudge hover:tcm03-nudge-sm motion-reduce:transition-none">
          <input type="radio" name="tcm-03-tool" id="tcm-03-t2" value="Fill" class="peer sr-only">
          <label for="tcm-03-t2" class="pointer-events-auto absolute inset-0 cursor-pointer rounded-full bg-tcm03-slice [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] transition-[background-color,color] duration-200 hover:bg-tcm03-slice-hi peer-checked:bg-linear-to-b peer-checked:from-tcm03-acc peer-checked:to-tcm03-acc2 peer-checked:text-tcm03-on">
            <span class="absolute top-[11%] left-1/2 grid -translate-x-1/2 justify-items-center gap-1 rotate-[calc(var(--i)*-60deg)] text-[11.5px] font-semibold tracking-[0.02em]"><svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12l7-7 7 7-7 7zM19 15s2 2.3 2 3.5a2 2 0 0 1-4 0c0-1.2 2-3.5 2-3.5z"/></svg>Fill</span>
          </label>
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] ring-0 peer-focus-visible:shadow-[inset_0_0_0_3px_var(--color-tcm03-ring)]"></span>
        </div>
        <div class="group/s pointer-events-none absolute inset-0 rotate-[calc(var(--i)*60deg)] [--i:3] [--a:calc(var(--i)*60deg-90deg)] transition-[translate] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:tcm03-nudge hover:tcm03-nudge-sm motion-reduce:transition-none">
          <input type="radio" name="tcm-03-tool" id="tcm-03-t3" value="Text" class="peer sr-only">
          <label for="tcm-03-t3" class="pointer-events-auto absolute inset-0 cursor-pointer rounded-full bg-tcm03-slice [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] transition-[background-color,color] duration-200 hover:bg-tcm03-slice-hi peer-checked:bg-linear-to-b peer-checked:from-tcm03-acc peer-checked:to-tcm03-acc2 peer-checked:text-tcm03-on">
            <span class="absolute top-[11%] left-1/2 grid -translate-x-1/2 justify-items-center gap-1 rotate-[calc(var(--i)*-60deg)] text-[11.5px] font-semibold tracking-[0.02em]"><svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 6V4h14v2M12 4v16M9 20h6"/></svg>Text</span>
          </label>
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] ring-0 peer-focus-visible:shadow-[inset_0_0_0_3px_var(--color-tcm03-ring)]"></span>
        </div>
        <div class="group/s pointer-events-none absolute inset-0 rotate-[calc(var(--i)*60deg)] [--i:4] [--a:calc(var(--i)*60deg-90deg)] transition-[translate] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:tcm03-nudge hover:tcm03-nudge-sm motion-reduce:transition-none">
          <input type="radio" name="tcm-03-tool" id="tcm-03-t4" value="Shapes" class="peer sr-only">
          <label for="tcm-03-t4" class="pointer-events-auto absolute inset-0 cursor-pointer rounded-full bg-tcm03-slice [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] transition-[background-color,color] duration-200 hover:bg-tcm03-slice-hi peer-checked:bg-linear-to-b peer-checked:from-tcm03-acc peer-checked:to-tcm03-acc2 peer-checked:text-tcm03-on">
            <span class="absolute top-[11%] left-1/2 grid -translate-x-1/2 justify-items-center gap-1 rotate-[calc(var(--i)*-60deg)] text-[11.5px] font-semibold tracking-[0.02em]"><svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3l4 7H8zM4 14h7v7H4zM17.5 14a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7z"/></svg>Shapes</span>
          </label>
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] ring-0 peer-focus-visible:shadow-[inset_0_0_0_3px_var(--color-tcm03-ring)]"></span>
        </div>
        <div class="group/s pointer-events-none absolute inset-0 rotate-[calc(var(--i)*60deg)] [--i:5] [--a:calc(var(--i)*60deg-90deg)] transition-[translate] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:tcm03-nudge hover:tcm03-nudge-sm motion-reduce:transition-none">
          <input type="radio" name="tcm-03-tool" id="tcm-03-t5" value="Crop" class="peer sr-only">
          <label for="tcm-03-t5" class="pointer-events-auto absolute inset-0 cursor-pointer rounded-full bg-tcm03-slice [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] transition-[background-color,color] duration-200 hover:bg-tcm03-slice-hi peer-checked:bg-linear-to-b peer-checked:from-tcm03-acc peer-checked:to-tcm03-acc2 peer-checked:text-tcm03-on">
            <span class="absolute top-[11%] left-1/2 grid -translate-x-1/2 justify-items-center gap-1 rotate-[calc(var(--i)*-60deg)] text-[11.5px] font-semibold tracking-[0.02em]"><svg viewBox="0 0 24 24" class="size-5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 2v16h16M2 6h16v16"/></svg>Crop</span>
          </label>
          <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-full [clip-path:polygon(50%_50%,22.5%_0,77.5%_0)] ring-0 peer-focus-visible:shadow-[inset_0_0_0_3px_var(--color-tcm03-ring)]"></span>
        </div>
          <div class="absolute top-1/2 left-1/2 z-10 grid size-[38%] -translate-1/2 place-content-center justify-items-center gap-0.5 rounded-full bg-tcm03-card text-center shadow-tcm03-hub ring-1 ring-tcm03-line">
            <span class="text-[10px] font-semibold tracking-[0.18em] text-tcm03-mut uppercase">Tool</span>
            <output data-out for="tcm-03-t0 tcm-03-t1 tcm-03-t2 tcm-03-t3 tcm-03-t4 tcm-03-t5" aria-live="polite" class="bg-linear-to-r from-tcm03-acc-ink to-tcm03-acc2 bg-clip-text text-xl font-bold tracking-[-0.02em] text-transparent">Brush</output>
          </div>
        </div>
      </div>
    </fieldset>
    <p class="flex flex-wrap items-center justify-center gap-1.5 text-[13px] text-tcm03-mut">Click a slice, or focus the wheel and press <kbd class="rounded-md bg-tcm03-card px-1.5 py-0.5 font-tcm03-mono text-[11px] text-tcm03-ink ring-1 ring-tcm03-line">←</kbd><kbd class="rounded-md bg-tcm03-card px-1.5 py-0.5 font-tcm03-mono text-[11px] text-tcm03-ink ring-1 ring-tcm03-line">→</kbd></p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm03-card px-3.5 py-2 text-center font-tcm03-mono text-[11.5px] text-tcm03-mut ring-1 ring-tcm03-line ">[clip-path:polygon(…)] · peer-checked: · has-checked:tcm03-nudge</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm03-bg: #fff5ef;
  --color-tcm03-bg: oklch(0.976 0.013 53.4);
  --color-tcm03-glow: #fed7aab3;
  --color-tcm03-glow: oklch(0.901 0.073 70.7 / 0.7);
  --color-tcm03-card: #fffdfb;
  --color-tcm03-card: oklch(0.995 0.003 67.8);
  --color-tcm03-rim: #fde7da;
  --color-tcm03-rim: oklch(0.942 0.03 52.7);
  --color-tcm03-slice: #fff9f5;
  --color-tcm03-slice: oklch(0.986 0.008 56.3);
  --color-tcm03-slice-hi: #ffeadf;
  --color-tcm03-slice-hi: oklch(0.951 0.027 49.6);
  --color-tcm03-ink: #2c160d;
  --color-tcm03-ink: oklch(0.229 0.04 42.7);
  --color-tcm03-mut: #7a5444;
  --color-tcm03-mut: oklch(0.483 0.057 43.7);
  --color-tcm03-line: #f3d9ca;
  --color-tcm03-line: oklch(0.903 0.035 52);
  --color-tcm03-acc: #ea580c;
  --color-tcm03-acc: oklch(0.646 0.194 41.1);
  --color-tcm03-acc2: #e11d48;
  --color-tcm03-acc2: oklch(0.586 0.222 17.6);
  --color-tcm03-acc-ink: #c2410c;
  --color-tcm03-acc-ink: oklch(0.553 0.174 38.4);
  --color-tcm03-on: #ffffff;
  --color-tcm03-on: oklch(1 0 0);
  --color-tcm03-ring: #c2410c;
  --color-tcm03-ring: oklch(0.553 0.174 38.4);
  --font-tcm03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcm03-mono: 'Space Mono', ui-monospace, monospace;
  --shadow-tcm03-wheel: 0 30px 60px -28px oklch(0.5 0.18 40 / 0.5), inset 0 2px 0 oklch(1 0 0 / 0.5);
  --shadow-tcm03-hub: 0 12px 28px -12px oklch(0.45 0.15 40 / 0.55), inset 0 1px 0 oklch(1 0 0 / 0.6);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-03 {
  width: 100%;
  min-height: 100svh;
}
/* A slice slides outward along its own bisector: --a is the slice's mid-angle, set per slice. */

@utility tcm03-nudge {
  translate: calc(cos(var(--a)) * 10px) calc(sin(var(--a)) * 10px);
  filter: drop-shadow(0 8px 14px oklch(0.55 0.2 30 / 0.45));
  z-index: 1;
}

@utility tcm03-nudge-sm {
  translate: calc(cos(var(--a)) * 4px) calc(sin(var(--a)) * 4px);
}
/* Dark theme: ember night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-03:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm03-bg: #1a0e09;
    --color-tcm03-bg: oklch(0.179 0.023 43.6);
    --color-tcm03-glow: #9a341266;
    --color-tcm03-glow: oklch(0.47 0.143 37.3 / 0.4);
    --color-tcm03-card: #26150e;
    --color-tcm03-card: oklch(0.217 0.031 43.1);
    --color-tcm03-rim: #331c12;
    --color-tcm03-rim: oklch(0.255 0.041 44);
    --color-tcm03-slice: #2a1810;
    --color-tcm03-slice: oklch(0.231 0.033 44.7);
    --color-tcm03-slice-hi: #3d2316;
    --color-tcm03-slice-hi: oklch(0.286 0.046 46.9);
    --color-tcm03-ink: #fff1e8;
    --color-tcm03-ink: oklch(0.967 0.019 55.2);
    --color-tcm03-mut: #d4ab97;
    --color-tcm03-mut: oklch(0.773 0.056 47.4);
    --color-tcm03-line: #4a2b1d;
    --color-tcm03-line: oklch(0.325 0.052 44.8);
    --color-tcm03-acc: #f97316;
    --color-tcm03-acc: oklch(0.705 0.187 47.6);
    --color-tcm03-acc2: #f43f5e;
    --color-tcm03-acc2: oklch(0.645 0.215 16.4);
    --color-tcm03-acc-ink: #fdba74;
    --color-tcm03-acc-ink: oklch(0.837 0.117 66.3);
    --color-tcm03-on: #ffffff;
    --color-tcm03-on: oklch(1 0 0);
    --color-tcm03-ring: #fdba74;
    --color-tcm03-ring: oklch(0.837 0.117 66.3);
  }
}

.tcm-03[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm03-bg: #1a0e09;
  --color-tcm03-bg: oklch(0.179 0.023 43.6);
  --color-tcm03-glow: #9a341266;
  --color-tcm03-glow: oklch(0.47 0.143 37.3 / 0.4);
  --color-tcm03-card: #26150e;
  --color-tcm03-card: oklch(0.217 0.031 43.1);
  --color-tcm03-rim: #331c12;
  --color-tcm03-rim: oklch(0.255 0.041 44);
  --color-tcm03-slice: #2a1810;
  --color-tcm03-slice: oklch(0.231 0.033 44.7);
  --color-tcm03-slice-hi: #3d2316;
  --color-tcm03-slice-hi: oklch(0.286 0.046 46.9);
  --color-tcm03-ink: #fff1e8;
  --color-tcm03-ink: oklch(0.967 0.019 55.2);
  --color-tcm03-mut: #d4ab97;
  --color-tcm03-mut: oklch(0.773 0.056 47.4);
  --color-tcm03-line: #4a2b1d;
  --color-tcm03-line: oklch(0.325 0.052 44.8);
  --color-tcm03-acc: #f97316;
  --color-tcm03-acc: oklch(0.705 0.187 47.6);
  --color-tcm03-acc2: #f43f5e;
  --color-tcm03-acc2: oklch(0.645 0.215 16.4);
  --color-tcm03-acc-ink: #fdba74;
  --color-tcm03-acc-ink: oklch(0.837 0.117 66.3);
  --color-tcm03-on: #ffffff;
  --color-tcm03-on: oklch(1 0 0);
  --color-tcm03-ring: #fdba74;
  --color-tcm03-ring: oklch(0.837 0.117 66.3);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-03-wheel');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const out = root.querySelector('[data-out]');
  root.addEventListener('change', (e) => { if (e.target.name === 'tcm-03-tool') out.textContent = e.target.value; });
})();
```
