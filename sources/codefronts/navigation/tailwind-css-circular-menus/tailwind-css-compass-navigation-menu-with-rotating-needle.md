---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-compass-navigation-menu-with-rotating-needle/"
title: "Tailwind CSS Compass Navigation Menu with Rotating Needle"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A brass-and-paper compass for a travel guide: four destinations sit at N/E/S/W, the needle swings the shortest way to the one you pick, and a bearing readout…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Compass Navigation Menu with Rotating Needle
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-compass-navigation-menu-with-rotating-needle/

A brass-and-paper compass for a travel guide: four destinations sit at N/E/S/W, the needle swings the shortest way to the one you pick, and a bearing readout ticks along like an instrument. The dial&rsquo;s 60 ticks and four cardinal marks are two masked repeating-conic-gradients; the destinations are a radio group whose arrow keys match the metaphor.
## HTML
```html
<section class="tcm-22 w-full min-h-svh grid place-items-center bg-tcm22-bg bg-[radial-gradient(55%_50%_at_50%_45%,var(--color-tcm22-glow),transparent_72%)] px-4 py-14 font-tcm22-sans text-tcm22-ink antialiased" aria-label="Compass navigation menu demo">
  <div id="tcm-22-rose" class="grid w-full justify-items-center gap-6">
    <header class="grid justify-items-center gap-1 text-center">
      <p class="text-[11px] font-semibold tracking-[0.24em] text-tcm22-mut uppercase">Atlas · Lisbon day trips</p>
      <h2 class="font-tcm22-serif text-[clamp(1.9rem,5vw,2.6rem)] leading-none font-medium">Where to, today?</h2>
    </header>
    <fieldset class="relative size-[min(23rem,96vw)] p-[3.4rem]">
      <legend class="sr-only">Choose a destination</legend>
      <div class="absolute top-0 left-1/2 -translate-x-1/2 z-10">
        <input type="radio" name="tcm-22-dest" id="tcm-22-n" value="0" data-place="Highlands" data-sub="12 km · Sintra hills" class="peer sr-only" checked>
        <label for="tcm-22-n" class="grid min-h-11 cursor-pointer place-items-center rounded-full bg-tcm22-chip px-3.5 font-tcm22-serif text-[15px] italic text-tcm22-ink shadow-tcm22-chip ring-1 ring-tcm22-brass/60 transition-[background-color,color] duration-200 hover:ring-tcm22-ink peer-checked:bg-tcm22-ink peer-checked:not-italic peer-checked:text-tcm22-paper peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm22-red">Highlands</label>
      </div>
      <div class="absolute top-1/2 right-0 -translate-y-1/2 z-10">
        <input type="radio" name="tcm-22-dest" id="tcm-22-e" value="90" data-place="Coast" data-sub="8 km · Cascais shore" class="peer sr-only">
        <label for="tcm-22-e" class="grid min-h-11 cursor-pointer place-items-center rounded-full bg-tcm22-chip px-3.5 font-tcm22-serif text-[15px] italic text-tcm22-ink shadow-tcm22-chip ring-1 ring-tcm22-brass/60 transition-[background-color,color] duration-200 hover:ring-tcm22-ink peer-checked:bg-tcm22-ink peer-checked:not-italic peer-checked:text-tcm22-paper peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm22-red">Coast</label>
      </div>
      <div class="absolute bottom-0 left-1/2 -translate-x-1/2 z-10">
        <input type="radio" name="tcm-22-dest" id="tcm-22-s" value="180" data-place="Old Town" data-sub="2 km · Alfama" class="peer sr-only">
        <label for="tcm-22-s" class="grid min-h-11 cursor-pointer place-items-center rounded-full bg-tcm22-chip px-3.5 font-tcm22-serif text-[15px] italic text-tcm22-ink shadow-tcm22-chip ring-1 ring-tcm22-brass/60 transition-[background-color,color] duration-200 hover:ring-tcm22-ink peer-checked:bg-tcm22-ink peer-checked:not-italic peer-checked:text-tcm22-paper peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm22-red">Old Town</label>
      </div>
      <div class="absolute top-1/2 left-0 -translate-y-1/2 z-10">
        <input type="radio" name="tcm-22-dest" id="tcm-22-w" value="270" data-place="Vineyards" data-sub="30 km · Colares" class="peer sr-only">
        <label for="tcm-22-w" class="grid min-h-11 cursor-pointer place-items-center rounded-full bg-tcm22-chip px-3.5 font-tcm22-serif text-[15px] italic text-tcm22-ink shadow-tcm22-chip ring-1 ring-tcm22-brass/60 transition-[background-color,color] duration-200 hover:ring-tcm22-ink peer-checked:bg-tcm22-ink peer-checked:not-italic peer-checked:text-tcm22-paper peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tcm22-red">Vineyards</label>
      </div>
      <div aria-hidden="true" class="relative grid size-full place-items-center rounded-full bg-[radial-gradient(circle_at_38%_30%,var(--color-tcm22-paper),var(--color-tcm22-paper2))] shadow-tcm22-dial">
        <span class="absolute inset-[4%] rounded-full bg-[repeating-conic-gradient(from_-0.5deg,var(--color-tcm22-ink)_0_1deg,transparent_1deg_6deg)] [mask-image:radial-gradient(circle,transparent_82%,black_83%)] opacity-70"></span>
        <span class="absolute inset-[4%] rounded-full bg-[repeating-conic-gradient(from_-1deg,var(--color-tcm22-red)_0_2deg,transparent_2deg_90deg)] [mask-image:radial-gradient(circle,transparent_76%,black_77%)]"></span>
        <svg viewBox="0 0 100 100" class="absolute inset-[24%] size-[52%] text-tcm22-brass/45"><path d="M50 4 58 42 96 50 58 58 50 96 42 58 4 50 42 42Z" fill="currentColor"/></svg>
          <span class="absolute top-1/2 left-1/2 -translate-1/2 font-tcm22-serif text-[1.35rem] font-semibold text-tcm22-red" style="margin-left:0%;margin-top:-34%">N</span>
          <span class="absolute top-1/2 left-1/2 -translate-1/2 font-tcm22-serif text-[1.35rem] font-semibold text-tcm22-ink" style="margin-left:34%;margin-top:0%">E</span>
          <span class="absolute top-1/2 left-1/2 -translate-1/2 font-tcm22-serif text-[1.35rem] font-semibold text-tcm22-ink" style="margin-left:0%;margin-top:34%">S</span>
          <span class="absolute top-1/2 left-1/2 -translate-1/2 font-tcm22-serif text-[1.35rem] font-semibold text-tcm22-ink" style="margin-left:-34%;margin-top:0%">W</span>
        <span data-needle class="absolute top-1/2 left-1/2 h-[64%] w-3 -translate-1/2 rotate-(--rot) transition-[rotate] duration-900 ease-[cubic-bezier(.34,1.45,.5,1)] [--rot:0deg] motion-reduce:transition-none">
          <span class="absolute top-0 left-0 h-1/2 w-full bg-tcm22-red [clip-path:polygon(50%_0,100%_100%,0_100%)] drop-shadow-[0_2px_2px_oklch(0.3_0.1_25/0.4)]"></span>
          <span class="absolute bottom-0 left-0 h-1/2 w-full bg-tcm22-ink/80 [clip-path:polygon(0_0,100%_0,50%_100%)]"></span>
        </span>
        <span class="absolute size-4 rounded-full bg-[radial-gradient(circle_at_35%_30%,#fff3cf,var(--color-tcm22-brass))] shadow-[0_1px_3px_oklch(0_0_0/0.4)]"></span>
      </div>
    </fieldset>
    <div class="grid w-full max-w-[20rem] grid-cols-[auto_1fr] items-center gap-x-4 rounded-2xl bg-tcm22-chip px-5 py-3.5 shadow-tcm22-chip ring-1 ring-tcm22-brass/40">
      <p class="row-span-2 font-tcm22-mono text-[1.6rem] font-semibold tabular-nums"><output data-deg>000</output>°</p>
      <p data-place class="font-tcm22-serif text-[1.15rem] leading-tight">Highlands</p>
      <p data-sub aria-live="polite" class="text-[12.5px] text-tcm22-mut">12 km · Sintra hills</p>
    </div>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm22-card px-3.5 py-2 text-center font-tcm22-mono text-[11.5px] text-tcm22-mut ring-1 ring-tcm22-line ">rotate-(--rot) needle · repeating-conic-gradient ticks + mask · peer-checked:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm22-bg: #f4eedf;
  --color-tcm22-bg: oklch(0.95 0.021 88.7);
  --color-tcm22-glow: #fde68a80;
  --color-tcm22-glow: oklch(0.924 0.115 95.7 / 0.5);
  --color-tcm22-paper: #fffaf0;
  --color-tcm22-paper: oklch(0.986 0.014 84.6);
  --color-tcm22-paper2: #efe4cb;
  --color-tcm22-paper2: oklch(0.921 0.035 87.1);
  --color-tcm22-chip: #fffcf5;
  --color-tcm22-chip: oklch(0.991 0.01 87.5);
  --color-tcm22-brass: #b8892f;
  --color-tcm22-brass: oklch(0.66 0.118 79.9);
  --color-tcm22-red: #b91c1c;
  --color-tcm22-red: oklch(0.505 0.19 27.5);
  --color-tcm22-ink: #2c2416;
  --color-tcm22-ink: oklch(0.265 0.027 81.1);
  --color-tcm22-mut: #6b5d45;
  --color-tcm22-mut: oklch(0.485 0.04 80.9);
  --color-tcm22-card: #fffcf5;
  --color-tcm22-card: oklch(0.991 0.01 87.5);
  --color-tcm22-line: #e2d5b8;
  --color-tcm22-line: oklch(0.876 0.041 86.7);
  --font-tcm22-sans: 'Inter', system-ui, sans-serif;
  --font-tcm22-serif: 'Newsreader', Georgia, serif;
  --font-tcm22-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tcm22-dial: 0 0 0 7px var(--color-tcm22-brass), 0 0 0 8.5px oklch(0.45 0.08 70), 0 26px 50px -20px oklch(0.35 0.06 70 / 0.65), inset 0 2px 6px oklch(1 0 0 / 0.6);
  --shadow-tcm22-chip: 0 6px 14px -8px oklch(0.4 0.06 70 / 0.5);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-22 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: lantern night: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-22:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm22-bg: #14110b;
    --color-tcm22-bg: oklch(0.179 0.013 84.5);
    --color-tcm22-glow: #78350f59;
    --color-tcm22-glow: oklch(0.414 0.105 45.9 / 0.35);
    --color-tcm22-paper: #2c2618;
    --color-tcm22-paper: oklch(0.271 0.026 87.4);
    --color-tcm22-paper2: #1b170e;
    --color-tcm22-paper2: oklch(0.206 0.018 86.7);
    --color-tcm22-chip: #221d13;
    --color-tcm22-chip: oklch(0.233 0.02 84.4);
    --color-tcm22-brass: #d6a84a;
    --color-tcm22-brass: oklch(0.756 0.123 82.7);
    --color-tcm22-red: #f87171;
    --color-tcm22-red: oklch(0.711 0.166 22.2);
    --color-tcm22-ink: #f3ead6;
    --color-tcm22-ink: oklch(0.939 0.028 86.6);
    --color-tcm22-mut: #bcae90;
    --color-tcm22-mut: oklch(0.755 0.044 85.9);
    --color-tcm22-card: #221d13;
    --color-tcm22-card: oklch(0.233 0.02 84.4);
    --color-tcm22-line: #3a3220;
    --color-tcm22-line: oklch(0.32 0.032 86.6);
  }
}

.tcm-22[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm22-bg: #14110b;
  --color-tcm22-bg: oklch(0.179 0.013 84.5);
  --color-tcm22-glow: #78350f59;
  --color-tcm22-glow: oklch(0.414 0.105 45.9 / 0.35);
  --color-tcm22-paper: #2c2618;
  --color-tcm22-paper: oklch(0.271 0.026 87.4);
  --color-tcm22-paper2: #1b170e;
  --color-tcm22-paper2: oklch(0.206 0.018 86.7);
  --color-tcm22-chip: #221d13;
  --color-tcm22-chip: oklch(0.233 0.02 84.4);
  --color-tcm22-brass: #d6a84a;
  --color-tcm22-brass: oklch(0.756 0.123 82.7);
  --color-tcm22-red: #f87171;
  --color-tcm22-red: oklch(0.711 0.166 22.2);
  --color-tcm22-ink: #f3ead6;
  --color-tcm22-ink: oklch(0.939 0.028 86.6);
  --color-tcm22-mut: #bcae90;
  --color-tcm22-mut: oklch(0.755 0.044 85.9);
  --color-tcm22-card: #221d13;
  --color-tcm22-card: oklch(0.233 0.02 84.4);
  --color-tcm22-line: #3a3220;
  --color-tcm22-line: oklch(0.32 0.032 86.6);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-22-rose');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const needle = root.querySelector('[data-needle]');
  const deg = root.querySelector('[data-deg]'), place = root.querySelector('[data-place]'), sub = root.querySelector('[data-sub]');
  let rot = 0, shown = 0, raf = 0;
  const tween = (target) => {
    cancelAnimationFrame(raf);
    const from = shown, delta = ((target - from) % 360 + 540) % 360 - 180, t0 = performance.now();
    const step = (t) => {
      const k = Math.min(1, (t - t0) / 850), e = 1 - Math.pow(1 - k, 3);
      shown = (from + delta * e + 360) % 360;
      deg.textContent = String(Math.round(shown) % 360).padStart(3, '0');
      if (k < 1) raf = requestAnimationFrame(step);
    };
    raf = requestAnimationFrame(step);
  };
  root.addEventListener('change', (e) => {
    if (e.target.name !== 'tcm-22-dest') return;
    const target = Number(e.target.value);
    rot += ((target - ((rot % 360) + 360) % 360) % 360 + 540) % 360 - 180;
    needle.style.setProperty('--rot', rot + 'deg');
    place.textContent = e.target.dataset.place;
    sub.textContent = e.target.dataset.sub;
    tween(target);
  });
})();
```
