---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-hexagon-honeycomb-menu-with-clip-path/"
title: "Tailwind CSS Hexagon Honeycomb Menu with clip-path"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A game class picker laid out as true honeycomb: six regular flat-top hexagons lock around a centre hex, each cut with one clip-path and placed with the same…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Hexagon Honeycomb Menu with clip-path
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-hexagon-honeycomb-menu-with-clip-path/

A game class picker laid out as true honeycomb: six regular flat-top hexagons lock around a centre hex, each cut with one clip-path and placed with the same ring trig as every circle menu &mdash; hexagons are a 60&deg; radial layout. A radio group underneath gives arrow-key cycling, and the focus ring is a larger hexagon behind the cell, because outlines can&rsquo;t follow a clip-path.
## HTML
```html
<section class="tcm-19 w-full min-h-svh grid place-items-center bg-tcm19-bg bg-[radial-gradient(55%_50%_at_50%_45%,var(--color-tcm19-glow),transparent_72%)] px-4 py-14 font-tcm19-sans text-tcm19-ink antialiased" aria-label="Hexagon honeycomb menu demo">
  <div id="tcm-19-picker" class="grid w-full justify-items-center gap-7">
    <header class="grid justify-items-center gap-1.5 text-center">
      <p class="font-tcm19-mono text-[11px] tracking-[0.18em] text-tcm19-acc-ink uppercase">New character · Step 2 of 4</p>
      <h2 class="text-[clamp(1.5rem,4vw,2rem)] font-bold tracking-[-0.03em]">Choose your class</h2>
    </header>
    <fieldset class="relative size-[min(21rem,92vw)] [--cell:min(6.5rem,27vw)]">
      <legend class="sr-only">Character class</legend>
      <div class="absolute top-1/2 left-1/2 grid h-[calc(var(--cell)*0.866)] w-(--cell) -translate-1/2 place-content-center justify-items-center gap-0.5 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-core text-center">
        <span class="font-tcm19-mono text-[9.5px] tracking-[0.28em] text-tcm19-mut uppercase">Class</span>
        <output data-out aria-live="polite" class="text-[15px] font-extrabold text-tcm19-acc-ink">Ranger</output>
      </div>
        <div class="tcm19-polar absolute top-1/2 left-1/2 -mt-[calc(var(--cell)*0.433)] -ml-[calc(var(--cell)/2)] h-[calc(var(--cell)*0.866)] w-(--cell) [--i:0] [--a:calc(60deg*var(--i)-90deg)] [--r:calc(var(--cell)*0.866+0.4rem)] transition-[scale] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:z-10 has-checked:scale-108 motion-reduce:transition-none">
          <input type="radio" name="tcm-19-class" id="tcm-19-c0" value="Ranger" data-stats="ATK 7 · DEF 4 · SPD 9" class="peer sr-only" checked>
          <span aria-hidden="true" class="absolute -inset-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-ring opacity-0 peer-focus-visible:opacity-100"></span>
          <label for="tcm-19-c0" class="absolute inset-0 grid cursor-pointer place-content-center justify-items-center gap-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-cell text-[12.5px] font-bold tracking-[0.03em] text-tcm19-ink transition-[background-color,color] duration-200 hover:bg-tcm19-cell-hi peer-checked:bg-linear-to-b peer-checked:from-tcm19-a peer-checked:to-tcm19-b peer-checked:text-tcm19-on"><svg viewBox="0 0 24 24" class="size-[22px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 19L19 5M19 5h-5M19 5v5M6 13l5 5M4 15l5 5"/></svg>Ranger</label>
        </div>
        <div class="tcm19-polar absolute top-1/2 left-1/2 -mt-[calc(var(--cell)*0.433)] -ml-[calc(var(--cell)/2)] h-[calc(var(--cell)*0.866)] w-(--cell) [--i:1] [--a:calc(60deg*var(--i)-90deg)] [--r:calc(var(--cell)*0.866+0.4rem)] transition-[scale] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:z-10 has-checked:scale-108 motion-reduce:transition-none">
          <input type="radio" name="tcm-19-class" id="tcm-19-c1" value="Mage" data-stats="ATK 9 · DEF 3 · SPD 5" class="peer sr-only">
          <span aria-hidden="true" class="absolute -inset-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-ring opacity-0 peer-focus-visible:opacity-100"></span>
          <label for="tcm-19-c1" class="absolute inset-0 grid cursor-pointer place-content-center justify-items-center gap-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-cell text-[12.5px] font-bold tracking-[0.03em] text-tcm19-ink transition-[background-color,color] duration-200 hover:bg-tcm19-cell-hi peer-checked:bg-linear-to-b peer-checked:from-tcm19-a peer-checked:to-tcm19-b peer-checked:text-tcm19-on"><svg viewBox="0 0 24 24" class="size-[22px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3.5l1.9 5 5.1 1.6-5.1 1.7L12 17l-1.9-5.2L5 10.1l5.1-1.6z"/></svg>Mage</label>
        </div>
        <div class="tcm19-polar absolute top-1/2 left-1/2 -mt-[calc(var(--cell)*0.433)] -ml-[calc(var(--cell)/2)] h-[calc(var(--cell)*0.866)] w-(--cell) [--i:2] [--a:calc(60deg*var(--i)-90deg)] [--r:calc(var(--cell)*0.866+0.4rem)] transition-[scale] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:z-10 has-checked:scale-108 motion-reduce:transition-none">
          <input type="radio" name="tcm-19-class" id="tcm-19-c2" value="Knight" data-stats="ATK 6 · DEF 9 · SPD 3" class="peer sr-only">
          <span aria-hidden="true" class="absolute -inset-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-ring opacity-0 peer-focus-visible:opacity-100"></span>
          <label for="tcm-19-c2" class="absolute inset-0 grid cursor-pointer place-content-center justify-items-center gap-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-cell text-[12.5px] font-bold tracking-[0.03em] text-tcm19-ink transition-[background-color,color] duration-200 hover:bg-tcm19-cell-hi peer-checked:bg-linear-to-b peer-checked:from-tcm19-a peer-checked:to-tcm19-b peer-checked:text-tcm19-on"><svg viewBox="0 0 24 24" class="size-[22px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/></svg>Knight</label>
        </div>
        <div class="tcm19-polar absolute top-1/2 left-1/2 -mt-[calc(var(--cell)*0.433)] -ml-[calc(var(--cell)/2)] h-[calc(var(--cell)*0.866)] w-(--cell) [--i:3] [--a:calc(60deg*var(--i)-90deg)] [--r:calc(var(--cell)*0.866+0.4rem)] transition-[scale] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:z-10 has-checked:scale-108 motion-reduce:transition-none">
          <input type="radio" name="tcm-19-class" id="tcm-19-c3" value="Rogue" data-stats="ATK 8 · DEF 3 · SPD 10" class="peer sr-only">
          <span aria-hidden="true" class="absolute -inset-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-ring opacity-0 peer-focus-visible:opacity-100"></span>
          <label for="tcm-19-c3" class="absolute inset-0 grid cursor-pointer place-content-center justify-items-center gap-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-cell text-[12.5px] font-bold tracking-[0.03em] text-tcm19-ink transition-[background-color,color] duration-200 hover:bg-tcm19-cell-hi peer-checked:bg-linear-to-b peer-checked:from-tcm19-a peer-checked:to-tcm19-b peer-checked:text-tcm19-on"><svg viewBox="0 0 24 24" class="size-[22px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M14.5 4l5.5 5.5-9 9H5.5V13zM4 20l3-3"/></svg>Rogue</label>
        </div>
        <div class="tcm19-polar absolute top-1/2 left-1/2 -mt-[calc(var(--cell)*0.433)] -ml-[calc(var(--cell)/2)] h-[calc(var(--cell)*0.866)] w-(--cell) [--i:4] [--a:calc(60deg*var(--i)-90deg)] [--r:calc(var(--cell)*0.866+0.4rem)] transition-[scale] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:z-10 has-checked:scale-108 motion-reduce:transition-none">
          <input type="radio" name="tcm-19-class" id="tcm-19-c4" value="Cleric" data-stats="ATK 4 · DEF 6 · SPD 5" class="peer sr-only">
          <span aria-hidden="true" class="absolute -inset-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-ring opacity-0 peer-focus-visible:opacity-100"></span>
          <label for="tcm-19-c4" class="absolute inset-0 grid cursor-pointer place-content-center justify-items-center gap-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-cell text-[12.5px] font-bold tracking-[0.03em] text-tcm19-ink transition-[background-color,color] duration-200 hover:bg-tcm19-cell-hi peer-checked:bg-linear-to-b peer-checked:from-tcm19-a peer-checked:to-tcm19-b peer-checked:text-tcm19-on"><svg viewBox="0 0 24 24" class="size-[22px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 3v18M7 8h10M9 21h6"/></svg>Cleric</label>
        </div>
        <div class="tcm19-polar absolute top-1/2 left-1/2 -mt-[calc(var(--cell)*0.433)] -ml-[calc(var(--cell)/2)] h-[calc(var(--cell)*0.866)] w-(--cell) [--i:5] [--a:calc(60deg*var(--i)-90deg)] [--r:calc(var(--cell)*0.866+0.4rem)] transition-[scale] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] has-checked:z-10 has-checked:scale-108 motion-reduce:transition-none">
          <input type="radio" name="tcm-19-class" id="tcm-19-c5" value="Bard" data-stats="ATK 5 · DEF 5 · SPD 7" class="peer sr-only">
          <span aria-hidden="true" class="absolute -inset-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-ring opacity-0 peer-focus-visible:opacity-100"></span>
          <label for="tcm-19-c5" class="absolute inset-0 grid cursor-pointer place-content-center justify-items-center gap-1 [clip-path:polygon(25%_0,75%_0,100%_50%,75%_100%,25%_100%,0_50%)] bg-tcm19-cell text-[12.5px] font-bold tracking-[0.03em] text-tcm19-ink transition-[background-color,color] duration-200 hover:bg-tcm19-cell-hi peer-checked:bg-linear-to-b peer-checked:from-tcm19-a peer-checked:to-tcm19-b peer-checked:text-tcm19-on"><svg viewBox="0 0 24 24" class="size-[22px]" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M9 18V6l10-2v12M9 18a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0zM19 16a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/></svg>Bard</label>
        </div>
    </fieldset>
    <p data-stats class="rounded-full bg-tcm19-card px-4 py-2 font-tcm19-mono text-[12.5px] text-tcm19-ink tabular-nums ring-1 ring-tcm19-line">ATK 7 · DEF 4 · SPD 9</p>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm19-card px-3.5 py-2 text-center font-tcm19-mono text-[11.5px] text-tcm19-mut ring-1 ring-tcm19-line ">regular flat-top hex · [--r:calc(var(--cell)*0.866+0.4rem)] · peer-checked:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm19-bg: #fbf6ea;
  --color-tcm19-bg: oklch(0.974 0.017 88);
  --color-tcm19-glow: #fde68ab3;
  --color-tcm19-glow: oklch(0.924 0.115 95.7 / 0.7);
  --color-tcm19-card: #fffdf6;
  --color-tcm19-card: oklch(0.994 0.009 93.6);
  --color-tcm19-core: #f3e7c9;
  --color-tcm19-core: oklch(0.93 0.042 88.8);
  --color-tcm19-cell: #ffffff;
  --color-tcm19-cell: oklch(1 0 0);
  --color-tcm19-cell-hi: #fff4d6;
  --color-tcm19-cell-hi: oklch(0.968 0.041 90.2);
  --color-tcm19-ink: #2b200a;
  --color-tcm19-ink: oklch(0.251 0.039 82.6);
  --color-tcm19-mut: #6e5f3f;
  --color-tcm19-mut: oklch(0.492 0.051 85.5);
  --color-tcm19-line: #eadfc4;
  --color-tcm19-line: oklch(0.905 0.038 88.5);
  --color-tcm19-a: #f59e0b;
  --color-tcm19-a: oklch(0.769 0.165 70.1);
  --color-tcm19-b: #d97706;
  --color-tcm19-b: oklch(0.666 0.157 58.3);
  --color-tcm19-on: #2b1a02;
  --color-tcm19-on: oklch(0.235 0.047 73.4);
  --color-tcm19-acc-ink: #a15c07;
  --color-tcm19-acc-ink: oklch(0.543 0.123 61.8);
  --color-tcm19-ring: #a15c07;
  --color-tcm19-ring: oklch(0.543 0.123 61.8);
  --font-tcm19-sans: 'Rubik', system-ui, sans-serif;
  --font-tcm19-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-19 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm19-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: dark honey: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-19:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm19-bg: #151109;
    --color-tcm19-bg: oklch(0.18 0.017 84.3);
    --color-tcm19-glow: #92400e59;
    --color-tcm19-glow: oklch(0.473 0.125 46.2 / 0.35);
    --color-tcm19-card: #221b0f;
    --color-tcm19-card: oklch(0.227 0.024 80.5);
    --color-tcm19-core: #33280f;
    --color-tcm19-core: oklch(0.283 0.042 85.7);
    --color-tcm19-cell: #2a2213;
    --color-tcm19-cell: oklch(0.257 0.028 82.5);
    --color-tcm19-cell-hi: #3a2e18;
    --color-tcm19-cell-hi: oklch(0.309 0.039 81.6);
    --color-tcm19-ink: #fbf2dd;
    --color-tcm19-ink: oklch(0.963 0.029 87.5);
    --color-tcm19-mut: #c2b08a;
    --color-tcm19-mut: oklch(0.763 0.055 85.6);
    --color-tcm19-line: #3b301c;
    --color-tcm19-line: oklch(0.316 0.036 81.7);
    --color-tcm19-a: #fbbf24;
    --color-tcm19-a: oklch(0.837 0.164 84.4);
    --color-tcm19-b: #f59e0b;
    --color-tcm19-b: oklch(0.769 0.165 70.1);
    --color-tcm19-on: #2b1a02;
    --color-tcm19-on: oklch(0.235 0.047 73.4);
    --color-tcm19-acc-ink: #fcd34d;
    --color-tcm19-acc-ink: oklch(0.879 0.153 91.6);
    --color-tcm19-ring: #fcd34d;
    --color-tcm19-ring: oklch(0.879 0.153 91.6);
  }
}

.tcm-19[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm19-bg: #151109;
  --color-tcm19-bg: oklch(0.18 0.017 84.3);
  --color-tcm19-glow: #92400e59;
  --color-tcm19-glow: oklch(0.473 0.125 46.2 / 0.35);
  --color-tcm19-card: #221b0f;
  --color-tcm19-card: oklch(0.227 0.024 80.5);
  --color-tcm19-core: #33280f;
  --color-tcm19-core: oklch(0.283 0.042 85.7);
  --color-tcm19-cell: #2a2213;
  --color-tcm19-cell: oklch(0.257 0.028 82.5);
  --color-tcm19-cell-hi: #3a2e18;
  --color-tcm19-cell-hi: oklch(0.309 0.039 81.6);
  --color-tcm19-ink: #fbf2dd;
  --color-tcm19-ink: oklch(0.963 0.029 87.5);
  --color-tcm19-mut: #c2b08a;
  --color-tcm19-mut: oklch(0.763 0.055 85.6);
  --color-tcm19-line: #3b301c;
  --color-tcm19-line: oklch(0.316 0.036 81.7);
  --color-tcm19-a: #fbbf24;
  --color-tcm19-a: oklch(0.837 0.164 84.4);
  --color-tcm19-b: #f59e0b;
  --color-tcm19-b: oklch(0.769 0.165 70.1);
  --color-tcm19-on: #2b1a02;
  --color-tcm19-on: oklch(0.235 0.047 73.4);
  --color-tcm19-acc-ink: #fcd34d;
  --color-tcm19-acc-ink: oklch(0.879 0.153 91.6);
  --color-tcm19-ring: #fcd34d;
  --color-tcm19-ring: oklch(0.879 0.153 91.6);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-19-picker');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const out = root.querySelector('[data-out]'), stats = root.querySelector('p[data-stats]');
  root.addEventListener('change', (e) => {
    if (e.target.name !== 'tcm-19-class') return;
    out.textContent = e.target.value;
    stats.textContent = e.target.dataset.stats;
  });
})();
```
