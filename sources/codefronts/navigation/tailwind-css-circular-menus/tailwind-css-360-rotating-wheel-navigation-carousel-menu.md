---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-360-rotating-wheel-navigation-carousel-menu/"
title: "Tailwind CSS 360° Rotating Wheel Navigation (Carousel Menu)"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A streaming-TV section wheel: eight destinations ride a full circle, and choosing one &mdash; by click, the centre arrows or &larr;/&rarr; &mdash; rotates…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS 360° Rotating Wheel Navigation (Carousel Menu)
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-360-rotating-wheel-navigation-carousel-menu/

A streaming-TV section wheel: eight destinations ride a full circle, and choosing one &mdash; by click, the centre arrows or &larr;/&rarr; &mdash; rotates the whole wheel so it glides under a fixed red pointer. One custom property, --rot, turns the ring with rotate-(--rot) and keeps every label upright with rotate-[calc(var(--rot)*-1)], and the script always takes the shortest way round.
## HTML
```html
<section class="tcm-11 w-full min-h-svh grid place-items-center overflow-hidden bg-tcm11-bg bg-[radial-gradient(55%_50%_at_50%_45%,var(--color-tcm11-glow),transparent_72%)] px-4 py-14 font-tcm11-sans text-tcm11-ink antialiased" aria-label="360 degree rotating wheel navigation demo">
  <div class="grid w-full justify-items-center gap-6">
    <header class="flex w-full max-w-[26rem] items-center justify-between">
      <p class="text-[1.35rem] font-extrabold tracking-[-0.04em]">lumen<span class="text-tcm11-acc">.</span>tv</p>
      <p class="font-tcm11-mono text-[11px] tracking-[0.12em] text-tcm11-mut uppercase">Use ← → to spin</p>
    </header>
    <nav id="tcm-11-wheel" class="relative grid size-[min(23rem,92vw)] place-items-center [--n:8] [--r:min(9.75rem,38vw)] [--rot:0deg]" aria-label="Sections">
      <span aria-hidden="true" class="absolute top-[calc(50%-var(--r)-2.4rem)] left-1/2 z-10 -translate-x-1/2 border-x-[9px] border-t-[12px] border-x-transparent border-t-tcm11-acc drop-shadow-[0_2px_6px_var(--color-tcm11-acc)]"></span>
      <ul class="absolute inset-0 rotate-(--rot) transition-[rotate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
        <li aria-hidden="true" class="absolute inset-[calc(50%-var(--r))] rounded-full border border-tcm11-line"></li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:0] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-stop aria-pressed="true" class="tcm11-polar pointer-events-auto min-h-11 cursor-pointer rounded-full bg-tcm11-chip px-4 text-[13.5px] font-semibold whitespace-nowrap text-tcm11-mut ring-1 ring-tcm11-line backdrop-blur-md rotate-[calc(var(--rot)*-1)] transition-[rotate,background-color,color,scale,box-shadow] duration-700 ease-[cubic-bezier(.16,1,.3,1)] hover:text-tcm11-ink hover:ring-tcm11-acc/60 aria-pressed:scale-110 aria-pressed:bg-linear-to-br aria-pressed:from-tcm11-acc aria-pressed:to-tcm11-acc2 aria-pressed:text-tcm11-on aria-pressed:shadow-tcm11-glow aria-pressed:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm11-ring motion-reduce:transition-none">Home</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:1] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-stop aria-pressed="false" class="tcm11-polar pointer-events-auto min-h-11 cursor-pointer rounded-full bg-tcm11-chip px-4 text-[13.5px] font-semibold whitespace-nowrap text-tcm11-mut ring-1 ring-tcm11-line backdrop-blur-md rotate-[calc(var(--rot)*-1)] transition-[rotate,background-color,color,scale,box-shadow] duration-700 ease-[cubic-bezier(.16,1,.3,1)] hover:text-tcm11-ink hover:ring-tcm11-acc/60 aria-pressed:scale-110 aria-pressed:bg-linear-to-br aria-pressed:from-tcm11-acc aria-pressed:to-tcm11-acc2 aria-pressed:text-tcm11-on aria-pressed:shadow-tcm11-glow aria-pressed:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm11-ring motion-reduce:transition-none">Series</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:2] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-stop aria-pressed="false" class="tcm11-polar pointer-events-auto min-h-11 cursor-pointer rounded-full bg-tcm11-chip px-4 text-[13.5px] font-semibold whitespace-nowrap text-tcm11-mut ring-1 ring-tcm11-line backdrop-blur-md rotate-[calc(var(--rot)*-1)] transition-[rotate,background-color,color,scale,box-shadow] duration-700 ease-[cubic-bezier(.16,1,.3,1)] hover:text-tcm11-ink hover:ring-tcm11-acc/60 aria-pressed:scale-110 aria-pressed:bg-linear-to-br aria-pressed:from-tcm11-acc aria-pressed:to-tcm11-acc2 aria-pressed:text-tcm11-on aria-pressed:shadow-tcm11-glow aria-pressed:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm11-ring motion-reduce:transition-none">Films</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:3] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-stop aria-pressed="false" class="tcm11-polar pointer-events-auto min-h-11 cursor-pointer rounded-full bg-tcm11-chip px-4 text-[13.5px] font-semibold whitespace-nowrap text-tcm11-mut ring-1 ring-tcm11-line backdrop-blur-md rotate-[calc(var(--rot)*-1)] transition-[rotate,background-color,color,scale,box-shadow] duration-700 ease-[cubic-bezier(.16,1,.3,1)] hover:text-tcm11-ink hover:ring-tcm11-acc/60 aria-pressed:scale-110 aria-pressed:bg-linear-to-br aria-pressed:from-tcm11-acc aria-pressed:to-tcm11-acc2 aria-pressed:text-tcm11-on aria-pressed:shadow-tcm11-glow aria-pressed:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm11-ring motion-reduce:transition-none">Live</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:4] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-stop aria-pressed="false" class="tcm11-polar pointer-events-auto min-h-11 cursor-pointer rounded-full bg-tcm11-chip px-4 text-[13.5px] font-semibold whitespace-nowrap text-tcm11-mut ring-1 ring-tcm11-line backdrop-blur-md rotate-[calc(var(--rot)*-1)] transition-[rotate,background-color,color,scale,box-shadow] duration-700 ease-[cubic-bezier(.16,1,.3,1)] hover:text-tcm11-ink hover:ring-tcm11-acc/60 aria-pressed:scale-110 aria-pressed:bg-linear-to-br aria-pressed:from-tcm11-acc aria-pressed:to-tcm11-acc2 aria-pressed:text-tcm11-on aria-pressed:shadow-tcm11-glow aria-pressed:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm11-ring motion-reduce:transition-none">Sports</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:5] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-stop aria-pressed="false" class="tcm11-polar pointer-events-auto min-h-11 cursor-pointer rounded-full bg-tcm11-chip px-4 text-[13.5px] font-semibold whitespace-nowrap text-tcm11-mut ring-1 ring-tcm11-line backdrop-blur-md rotate-[calc(var(--rot)*-1)] transition-[rotate,background-color,color,scale,box-shadow] duration-700 ease-[cubic-bezier(.16,1,.3,1)] hover:text-tcm11-ink hover:ring-tcm11-acc/60 aria-pressed:scale-110 aria-pressed:bg-linear-to-br aria-pressed:from-tcm11-acc aria-pressed:to-tcm11-acc2 aria-pressed:text-tcm11-on aria-pressed:shadow-tcm11-glow aria-pressed:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm11-ring motion-reduce:transition-none">Kids</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:6] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-stop aria-pressed="false" class="tcm11-polar pointer-events-auto min-h-11 cursor-pointer rounded-full bg-tcm11-chip px-4 text-[13.5px] font-semibold whitespace-nowrap text-tcm11-mut ring-1 ring-tcm11-line backdrop-blur-md rotate-[calc(var(--rot)*-1)] transition-[rotate,background-color,color,scale,box-shadow] duration-700 ease-[cubic-bezier(.16,1,.3,1)] hover:text-tcm11-ink hover:ring-tcm11-acc/60 aria-pressed:scale-110 aria-pressed:bg-linear-to-br aria-pressed:from-tcm11-acc aria-pressed:to-tcm11-acc2 aria-pressed:text-tcm11-on aria-pressed:shadow-tcm11-glow aria-pressed:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm11-ring motion-reduce:transition-none">Music</button>
        </li>
        <li class="absolute inset-0 grid place-items-center pointer-events-none [--i:7] [--a:calc(360deg/var(--n)*var(--i)-90deg)]">
          <button type="button" data-stop aria-pressed="false" class="tcm11-polar pointer-events-auto min-h-11 cursor-pointer rounded-full bg-tcm11-chip px-4 text-[13.5px] font-semibold whitespace-nowrap text-tcm11-mut ring-1 ring-tcm11-line backdrop-blur-md rotate-[calc(var(--rot)*-1)] transition-[rotate,background-color,color,scale,box-shadow] duration-700 ease-[cubic-bezier(.16,1,.3,1)] hover:text-tcm11-ink hover:ring-tcm11-acc/60 aria-pressed:scale-110 aria-pressed:bg-linear-to-br aria-pressed:from-tcm11-acc aria-pressed:to-tcm11-acc2 aria-pressed:text-tcm11-on aria-pressed:shadow-tcm11-glow aria-pressed:ring-transparent focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcm11-ring motion-reduce:transition-none">My list</button>
        </li>
      </ul>
      <div class="relative grid size-[min(11.5rem,44vw)] place-content-center justify-items-center gap-1 rounded-full bg-[radial-gradient(circle_at_38%_30%,var(--color-tcm11-face-hi),var(--color-tcm11-face))] text-center shadow-tcm11-face ring-1 ring-tcm11-line">
        <span class="font-tcm11-mono text-[10px] tracking-[0.22em] text-tcm11-mut uppercase">Now browsing</span>
        <strong data-current class="text-[clamp(1.2rem,5vw,1.6rem)] leading-tight font-bold tracking-[-0.02em]">Home</strong>
        <div class="mt-1.5 flex gap-2">
          <button type="button" data-step="-1" aria-label="Previous section" class="grid size-11 cursor-pointer place-items-center rounded-full bg-tcm11-chip text-tcm11-ink ring-1 ring-tcm11-line transition-colors hover:bg-tcm11-acc hover:text-tcm11-on focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm11-ring"><svg viewBox="0 0 24 24" class="size-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M15 6l-6 6 6 6"/></svg></button>
          <button type="button" data-step="1" aria-label="Next section" class="grid size-11 cursor-pointer place-items-center rounded-full bg-tcm11-chip text-tcm11-ink ring-1 ring-tcm11-line transition-colors hover:bg-tcm11-acc hover:text-tcm11-on focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcm11-ring"><svg viewBox="0 0 24 24" class="size-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6"/></svg></button>
        </div>
      </div>
      <p data-live aria-live="polite" class="sr-only"></p>
    </nav>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm11-card px-3.5 py-2 text-center font-tcm11-mono text-[11.5px] text-tcm11-mut ring-1 ring-tcm11-line ">rotate-(--rot) · rotate-[calc(var(--rot)*-1)] · shortest-path delta</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm11-bg: #fbf3f3;
  --color-tcm11-bg: oklch(0.97 0.009 17.3);
  --color-tcm11-glow: #fecaca99;
  --color-tcm11-glow: oklch(0.885 0.059 18.3 / 0.6);
  --color-tcm11-chip: #ffffffcc;
  --color-tcm11-chip: oklch(1 0 0 / 0.8);
  --color-tcm11-face: #fff7f6;
  --color-tcm11-face: oklch(0.982 0.009 26);
  --color-tcm11-face-hi: #ffffff;
  --color-tcm11-face-hi: oklch(1 0 0);
  --color-tcm11-ink: #2a1214;
  --color-tcm11-ink: oklch(0.219 0.04 15.6);
  --color-tcm11-mut: #6f5154;
  --color-tcm11-mut: oklch(0.468 0.041 12.1);
  --color-tcm11-line: #f0d9da;
  --color-tcm11-line: oklch(0.904 0.026 14.6);
  --color-tcm11-acc: #dc2626;
  --color-tcm11-acc: oklch(0.577 0.215 27.3);
  --color-tcm11-acc2: #e11d48;
  --color-tcm11-acc2: oklch(0.586 0.222 17.6);
  --color-tcm11-on: #ffffff;
  --color-tcm11-on: oklch(1 0 0);
  --color-tcm11-ring: #b91c1c;
  --color-tcm11-ring: oklch(0.505 0.19 27.5);
  --color-tcm11-card: #fffafa;
  --color-tcm11-card: oklch(0.989 0.005 17.2);
  --font-tcm11-sans: 'Outfit', system-ui, sans-serif;
  --font-tcm11-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcm11-glow: 0 0 0 4px oklch(0.6 0.22 25 / 0.15), 0 10px 26px -8px oklch(0.58 0.22 25 / 0.7);
  --shadow-tcm11-face: 0 30px 60px -24px oklch(0.3 0.1 20 / 0.45), inset 0 1px 0 oklch(1 0 0 / 0.5);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-11 {
  width: 100%;
  min-height: 100svh;
}
/* The radial formula, as a real utility: position = (cos a · r, sin a · r). Items set --a and --r. */

@utility tcm11-polar {
  translate: calc(cos(var(--a)) * var(--r)) calc(sin(var(--a)) * var(--r));
}
/* Dark theme: theatre black: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-11:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm11-bg: #130a0b;
    --color-tcm11-bg: oklch(0.158 0.016 11.7);
    --color-tcm11-glow: #7f1d1d73;
    --color-tcm11-glow: oklch(0.396 0.133 25.7 / 0.45);
    --color-tcm11-chip: #ffffff12;
    --color-tcm11-chip: oklch(1 0 0 / 0.07);
    --color-tcm11-face: #1c1011;
    --color-tcm11-face: oklch(0.19 0.02 13.7);
    --color-tcm11-face-hi: #2d1a1c;
    --color-tcm11-face-hi: oklch(0.244 0.031 12.7);
    --color-tcm11-ink: #fdeeee;
    --color-tcm11-ink: oklch(0.961 0.016 17.4);
    --color-tcm11-mut: #c8a3a6;
    --color-tcm11-mut: oklch(0.75 0.044 12.7);
    --color-tcm11-line: #3a2224;
    --color-tcm11-line: oklch(0.284 0.037 14.3);
    --color-tcm11-acc: #ef4444;
    --color-tcm11-acc: oklch(0.637 0.208 25.3);
    --color-tcm11-acc2: #f43f5e;
    --color-tcm11-acc2: oklch(0.645 0.215 16.4);
    --color-tcm11-on: #ffffff;
    --color-tcm11-on: oklch(1 0 0);
    --color-tcm11-ring: #fca5a5;
    --color-tcm11-ring: oklch(0.808 0.103 19.6);
    --color-tcm11-card: #1c1011;
    --color-tcm11-card: oklch(0.19 0.02 13.7);
  }
}

.tcm-11[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm11-bg: #130a0b;
  --color-tcm11-bg: oklch(0.158 0.016 11.7);
  --color-tcm11-glow: #7f1d1d73;
  --color-tcm11-glow: oklch(0.396 0.133 25.7 / 0.45);
  --color-tcm11-chip: #ffffff12;
  --color-tcm11-chip: oklch(1 0 0 / 0.07);
  --color-tcm11-face: #1c1011;
  --color-tcm11-face: oklch(0.19 0.02 13.7);
  --color-tcm11-face-hi: #2d1a1c;
  --color-tcm11-face-hi: oklch(0.244 0.031 12.7);
  --color-tcm11-ink: #fdeeee;
  --color-tcm11-ink: oklch(0.961 0.016 17.4);
  --color-tcm11-mut: #c8a3a6;
  --color-tcm11-mut: oklch(0.75 0.044 12.7);
  --color-tcm11-line: #3a2224;
  --color-tcm11-line: oklch(0.284 0.037 14.3);
  --color-tcm11-acc: #ef4444;
  --color-tcm11-acc: oklch(0.637 0.208 25.3);
  --color-tcm11-acc2: #f43f5e;
  --color-tcm11-acc2: oklch(0.645 0.215 16.4);
  --color-tcm11-on: #ffffff;
  --color-tcm11-on: oklch(1 0 0);
  --color-tcm11-ring: #fca5a5;
  --color-tcm11-ring: oklch(0.808 0.103 19.6);
  --color-tcm11-card: #1c1011;
  --color-tcm11-card: oklch(0.19 0.02 13.7);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-11-wheel');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const stops = [...root.querySelectorAll('[data-stop]')];
  const cur = root.querySelector('[data-current]');
  const live = root.querySelector('[data-live]');
  const n = stops.length, step = 360 / n;
  let rot = 0, active = 0;
  const go = (idx) => {
    idx = ((idx % n) + n) % n;
    let delta = -idx * step - (rot % 360);
    delta = ((delta % 360) + 540) % 360 - 180;
    rot += delta;
    root.style.setProperty('--rot', rot + 'deg');
    stops.forEach((s, k) => s.setAttribute('aria-pressed', String(k === idx)));
    active = idx;
    cur.textContent = stops[idx].textContent;
    live.textContent = stops[idx].textContent + ' selected';
  };
  stops.forEach((s, k) => s.addEventListener('click', () => go(k)));
  root.querySelectorAll('[data-step]').forEach((b) => b.addEventListener('click', () => go(active + Number(b.dataset.step))));
  root.addEventListener('keydown', (e) => {
    const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
    if (!d || e.target.closest('[data-step]') === null && !e.target.closest('[data-stop]')) return;
    e.preventDefault(); go(active + d);
  });
})();
```
