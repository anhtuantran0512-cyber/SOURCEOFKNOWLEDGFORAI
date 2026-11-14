---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-clock-time-picker-circular-hour-selector/"
title: "Tailwind CSS Clock Time Picker (Circular Hour Selector)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "The Material time picker rebuilt for a delivery slot: twelve hour stops on a steel dial, a red hand that sweeps to your choice the short way round, an AM/PM…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Clock Time Picker (Circular Hour Selector)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-clock-time-picker-circular-hour-selector/

The Material time picker rebuilt for a delivery slot: twelve hour stops on a steel dial, a red hand that sweeps to your choice the short way round, an AM/PM segmented control and a digital readout. Hours are real radios &mdash; booked slots are disabled and struck through with peer-disabled:line-through &mdash; so arrow keys skip them natively and the choice submits with any form.
## HTML
```html
<section class="tcm-25 w-full min-h-svh grid place-items-center bg-tcm25-bg bg-[radial-gradient(55%_50%_at_50%_45%,var(--color-tcm25-glow),transparent_72%)] px-4 py-14 font-tcm25-sans text-tcm25-ink antialiased" aria-label="Clock time picker demo">
  <div id="tcm-25-watch" class="grid w-full max-w-[24rem] justify-items-center gap-6 rounded-[2rem] bg-tcm25-card p-6 shadow-tcm25-card ring-1 ring-tcm25-line">
    <header class="flex w-full items-start justify-between gap-4">
      <div><p class="font-tcm25-mono text-[11px] tracking-[0.16em] text-tcm25-acc-ink uppercase">Delivery slot</p><h2 class="mt-1 text-xl font-semibold tracking-[-0.02em]">Pick an hour</h2></div>
      <fieldset class="flex rounded-full bg-tcm25-sunk p-1 ring-1 ring-tcm25-line"><legend class="sr-only">Morning or afternoon</legend>
        <label class="relative"><input type="radio" name="tcm-25-ampm" value="AM" class="peer sr-only"><span class="grid h-9 min-w-11 cursor-pointer place-items-center rounded-full px-3 font-tcm25-mono text-[12px] font-semibold text-tcm25-mut transition-colors peer-checked:bg-tcm25-card peer-checked:text-tcm25-ink peer-checked:shadow-tcm25-seg peer-focus-visible:outline-2 peer-focus-visible:outline-tcm25-ring">AM</span></label>
        <label class="relative"><input type="radio" name="tcm-25-ampm" value="PM" class="peer sr-only" checked><span class="grid h-9 min-w-11 cursor-pointer place-items-center rounded-full px-3 font-tcm25-mono text-[12px] font-semibold text-tcm25-mut transition-colors peer-checked:bg-tcm25-card peer-checked:text-tcm25-ink peer-checked:shadow-tcm25-seg peer-focus-visible:outline-2 peer-focus-visible:outline-tcm25-ring">PM</span></label>
      </fieldset>
    </header>
    <fieldset class="relative size-[min(19rem,80vw)] rounded-full bg-[radial-gradient(circle_at_40%_30%,var(--color-tcm25-face-hi),var(--color-tcm25-face))] shadow-tcm25-dial [--r:min(7.1rem,30vw)]">
      <legend class="sr-only">Hour</legend>
      <span aria-hidden="true" class="absolute inset-[4%] rounded-full bg-[repeating-conic-gradient(var(--color-tcm25-tick)_0_0.6deg,transparent_0.6deg_6deg)] [mask-image:radial-gradient(circle,transparent_88%,black_89%)]"></span>
      <span data-hand aria-hidden="true" class="absolute top-1/2 left-1/2 h-[30%] w-1.5 -ml-[3px] origin-bottom -translate-y-full rotate-(--rot) rounded-t-full bg-linear-to-t from-tcm25-acc2 to-tcm25-acc transition-[rotate] duration-700 ease-[cubic-bezier(.34,1.45,.5,1)] [--rot:0deg] motion-reduce:transition-none after:absolute after:-top-1 after:left-1/2 after:size-3 after:-translate-x-1/2 after:rounded-full after:bg-tcm25-acc after:shadow-tcm25-pick"></span>
      <span aria-hidden="true" class="absolute top-1/2 left-1/2 size-4 -translate-1/2 rounded-full bg-tcm25-card shadow-[0_1px_3px_oklch(0_0_0/0.35)] ring-4 ring-tcm25-acc"></span>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:1] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h1" value="1" class="peer sr-only">
          <label for="tcm-25-h1" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">1</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:2] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h2" value="2" class="peer sr-only" disabled>
          <label for="tcm-25-h2" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">2</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:3] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h3" value="3" class="peer sr-only">
          <label for="tcm-25-h3" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">3</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:4] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h4" value="4" class="peer sr-only">
          <label for="tcm-25-h4" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">4</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:5] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h5" value="5" class="peer sr-only" disabled>
          <label for="tcm-25-h5" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">5</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:6] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h6" value="6" class="peer sr-only">
          <label for="tcm-25-h6" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">6</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:7] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h7" value="7" class="peer sr-only">
          <label for="tcm-25-h7" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">7</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:8] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h8" value="8" class="peer sr-only">
          <label for="tcm-25-h8" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">8</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:9] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h9" value="9" class="peer sr-only">
          <label for="tcm-25-h9" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">9</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:10] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h10" value="10" class="peer sr-only">
          <label for="tcm-25-h10" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">10</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:11] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h11" value="11" class="peer sr-only">
          <label for="tcm-25-h11" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">11</label>
        </div>
        <div class="tcm25-polar absolute top-1/2 left-1/2 size-0 [--h:12] [--a:calc(var(--h)*30deg-90deg)]">
          <input type="radio" name="tcm-25-hour" id="tcm-25-h12" value="12" class="peer sr-only" checked>
          <label for="tcm-25-h12" class="grid size-11 -translate-1/2 cursor-pointer place-items-center rounded-full text-[15px] font-semibold tabular-nums text-tcm25-ink transition-[background-color,color,scale] duration-200 hover:bg-tcm25-acc/12 peer-checked:scale-110 peer-checked:bg-linear-to-br peer-checked:from-tcm25-acc peer-checked:to-tcm25-acc2 peer-checked:text-white peer-checked:shadow-tcm25-pick peer-disabled:cursor-not-allowed peer-disabled:text-tcm25-mut/45 peer-disabled:line-through peer-disabled:hover:bg-transparent peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm25-ring">12</label>
        </div>
      <p class="pointer-events-none absolute top-[66%] left-1/2 -translate-x-1/2 rounded-lg bg-tcm25-ink px-3 py-1.5 text-center"><output data-digital aria-live="polite" class="block font-tcm25-mono text-[16px] font-semibold tracking-[0.06em] text-tcm25-card tabular-nums">12:00 PM</output></p>
    </fieldset>
    <p class="text-[13px] text-tcm25-mut">Struck-out hours are fully booked</p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm25-card px-3.5 py-2 text-center font-tcm25-mono text-[11.5px] text-tcm25-mut ring-1 ring-tcm25-line ">12 radios on tcm25-polar · rotate-(--rot) hand · peer-disabled:line-through</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm25-bg: #eef1f6;
  --color-tcm25-bg: oklch(0.957 0.007 260.7);
  --color-tcm25-glow: #fecaca80;
  --color-tcm25-glow: oklch(0.885 0.059 18.3 / 0.5);
  --color-tcm25-card: #ffffff;
  --color-tcm25-card: oklch(1 0 0);
  --color-tcm25-sunk: #f1f3f8;
  --color-tcm25-sunk: oklch(0.964 0.007 268.5);
  --color-tcm25-face: #e9edf3;
  --color-tcm25-face: oklch(0.945 0.009 258.3);
  --color-tcm25-face-hi: #ffffff;
  --color-tcm25-face-hi: oklch(1 0 0);
  --color-tcm25-tick: #5b6476;
  --color-tcm25-tick: oklch(0.502 0.031 264.2);
  --color-tcm25-ink: #161b26;
  --color-tcm25-ink: oklch(0.222 0.023 265.6);
  --color-tcm25-mut: #5b6476;
  --color-tcm25-mut: oklch(0.502 0.031 264.2);
  --color-tcm25-line: #dde2ea;
  --color-tcm25-line: oklch(0.911 0.012 259.8);
  --color-tcm25-acc: #ef4444;
  --color-tcm25-acc: oklch(0.637 0.208 25.3);
  --color-tcm25-acc2: #be123c;
  --color-tcm25-acc2: oklch(0.514 0.198 16.9);
  --color-tcm25-acc-ink: #b91c1c;
  --color-tcm25-acc-ink: oklch(0.505 0.19 27.5);
  --color-tcm25-ring: #b91c1c;
  --color-tcm25-ring: oklch(0.505 0.19 27.5);
  --font-tcm25-sans: 'Geist', system-ui, sans-serif;
  --font-tcm25-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tcm25-card: 0 1px 2px oklch(0.3 0.03 260 / 0.06), 0 30px 60px -28px oklch(0.3 0.05 260 / 0.4);
  --shadow-tcm25-dial: 0 0 0 8px var(--color-tcm25-sunk), 0 0 0 9px var(--color-tcm25-line), inset 0 2px 8px oklch(1 0 0 / 0.5), inset 0 -10px 24px oklch(0.4 0.03 260 / 0.12);
  --shadow-tcm25-pick: 0 6px 16px -6px oklch(0.55 0.22 20 / 0.7);
  --shadow-tcm25-seg: 0 1px 3px oklch(0.3 0.03 260 / 0.2);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-25 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm25-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: steel chronograph: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-25:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm25-bg: #0b0e14;
    --color-tcm25-bg: oklch(0.163 0.014 264.1);
    --color-tcm25-glow: #7f1d1d59;
    --color-tcm25-glow: oklch(0.396 0.133 25.7 / 0.35);
    --color-tcm25-card: #151a24;
    --color-tcm25-card: oklch(0.218 0.021 264);
    --color-tcm25-sunk: #1c2230;
    --color-tcm25-sunk: oklch(0.253 0.028 266.4);
    --color-tcm25-face: #141924;
    --color-tcm25-face: oklch(0.214 0.023 265.5);
    --color-tcm25-face-hi: #262d3d;
    --color-tcm25-face-hi: oklch(0.298 0.031 266.2);
    --color-tcm25-tick: #8a93a6;
    --color-tcm25-tick: oklch(0.662 0.03 265.3);
    --color-tcm25-ink: #eef1f7;
    --color-tcm25-ink: oklch(0.958 0.009 264.5);
    --color-tcm25-mut: #a1a9ba;
    --color-tcm25-mut: oklch(0.734 0.026 265.5);
    --color-tcm25-line: #262d3c;
    --color-tcm25-line: oklch(0.297 0.029 265.2);
    --color-tcm25-acc: #f87171;
    --color-tcm25-acc: oklch(0.711 0.166 22.2);
    --color-tcm25-acc2: #e11d48;
    --color-tcm25-acc2: oklch(0.586 0.222 17.6);
    --color-tcm25-acc-ink: #fca5a5;
    --color-tcm25-acc-ink: oklch(0.808 0.103 19.6);
    --color-tcm25-ring: #fca5a5;
    --color-tcm25-ring: oklch(0.808 0.103 19.6);
  }
}

.tcm-25[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm25-bg: #0b0e14;
  --color-tcm25-bg: oklch(0.163 0.014 264.1);
  --color-tcm25-glow: #7f1d1d59;
  --color-tcm25-glow: oklch(0.396 0.133 25.7 / 0.35);
  --color-tcm25-card: #151a24;
  --color-tcm25-card: oklch(0.218 0.021 264);
  --color-tcm25-sunk: #1c2230;
  --color-tcm25-sunk: oklch(0.253 0.028 266.4);
  --color-tcm25-face: #141924;
  --color-tcm25-face: oklch(0.214 0.023 265.5);
  --color-tcm25-face-hi: #262d3d;
  --color-tcm25-face-hi: oklch(0.298 0.031 266.2);
  --color-tcm25-tick: #8a93a6;
  --color-tcm25-tick: oklch(0.662 0.03 265.3);
  --color-tcm25-ink: #eef1f7;
  --color-tcm25-ink: oklch(0.958 0.009 264.5);
  --color-tcm25-mut: #a1a9ba;
  --color-tcm25-mut: oklch(0.734 0.026 265.5);
  --color-tcm25-line: #262d3c;
  --color-tcm25-line: oklch(0.297 0.029 265.2);
  --color-tcm25-acc: #f87171;
  --color-tcm25-acc: oklch(0.711 0.166 22.2);
  --color-tcm25-acc2: #e11d48;
  --color-tcm25-acc2: oklch(0.586 0.222 17.6);
  --color-tcm25-acc-ink: #fca5a5;
  --color-tcm25-acc-ink: oklch(0.808 0.103 19.6);
  --color-tcm25-ring: #fca5a5;
  --color-tcm25-ring: oklch(0.808 0.103 19.6);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-25-watch');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const hand = root.querySelector('[data-hand]'), out = root.querySelector('[data-digital]');
  let rot = 0;
  const paint = () => {
    const h = root.querySelector('input[name="tcm-25-hour"]:checked');
    const m = root.querySelector('input[name="tcm-25-ampm"]:checked');
    out.textContent = h.value + ':00 ' + m.value;
  };
  root.addEventListener('change', (e) => {
    if (e.target.name === 'tcm-25-hour') {
      const target = (Number(e.target.value) % 12) * 30;
      rot += ((target - ((rot % 360) + 360) % 360) % 360 + 540) % 360 - 180;
      hand.style.setProperty('--rot', rot + 'deg');
    }
    paint();
  });
})();
```
