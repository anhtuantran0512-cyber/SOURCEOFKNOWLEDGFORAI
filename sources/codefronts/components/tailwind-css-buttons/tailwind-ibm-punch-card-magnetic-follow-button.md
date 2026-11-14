---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-ibm-punch-card-magnetic-follow-button/"
title: "Tailwind IBM Punch Card Magnetic Follow Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "An 80-column punch card that tilts toward your cursor in real 3D and drifts a few pixels with it: rows of rectangular holes cut by a mask grid, a clipped…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind IBM Punch Card Magnetic Follow Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-ibm-punch-card-magnetic-follow-button/

An 80-column punch card that tilts toward your cursor in real 3D and drifts a few pixels with it: rows of rectangular holes cut by a mask grid, a clipped corner, faded index printing, and a sheen that tracks the light across the card stock.
## HTML
```html
<div class="tb-50 w-full min-h-svh grid place-items-center font-tb50-mono p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-50__card group relative cursor-pointer grid gap-2 content-between w-[min(100%,26rem)] min-h-38 px-4.5 pt-3.5 pb-4 border-0 rounded-[0.15rem] text-left text-[0.8125rem] text-tb50-ink [clip-path:polygon(0_0,calc(100%-1.1rem)_0,100%_1.1rem,100%_100%,0_100%)] drop-shadow-[0_14px_22px_#0000008c] [transform:perspective(760px)_rotate3d(var(--ty),var(--tx),0,var(--tilt))_translate3d(calc(var(--tx)*6px),calc(var(--ty)*-6px),0)] transition-[transform,filter] duration-[400ms] ease-tb50-out touch-manipulation [-webkit-tap-highlight-color:transparent] hover:drop-shadow-[0_22px_30px_#00000099] active:drop-shadow-[0_6px_12px_#0000008c] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb50-accent disabled:cursor-not-allowed disabled:grayscale-[0.6] disabled:opacity-75 motion-reduce:transition-none motion-reduce:[transform:none]">
    <span aria-hidden="true" class="tb-50__sheen absolute inset-0 pointer-events-none opacity-65 transition-opacity duration-[350ms] group-hover:opacity-100 motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="tb-50__holes absolute inset-0 pointer-events-none"></span>
    <span class="relative z-30 flex justify-between gap-4 text-[0.6875rem] tracking-[0.14em] tabular-nums text-tb50-print">
      <span class="font-semibold">0042</span>
      <span>001 · 080</span>
    </span>
    <span class="relative z-30 text-[1.0625rem] font-semibold tracking-[0.06em]">RUN JOB — COMPILE</span>
    <span class="relative z-30 text-[0.625rem] tracking-[0.16em] uppercase text-tb50-accent">IBM 5081 · FORTRAN IV</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb50-bg: #15171a;
  --color-tb50-bg: oklch(0.19 0.008 250);
  --color-tb50-card: #efe6cd;
  --color-tb50-card: oklch(0.92 0.03 88);
  --color-tb50-card-lo: #ddd2b4;
  --color-tb50-card-lo: oklch(0.86 0.035 86);
  --color-tb50-ink: #2b2a22;
  --color-tb50-ink: oklch(0.27 0.015 95);
  --color-tb50-print: #4d7a70;
  --color-tb50-print: oklch(0.52 0.06 175);
  --color-tb50-accent: #9c4526;
  --color-tb50-accent: oklch(0.47 0.13 40);
  --font-tb50-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  --ease-tb50-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-50 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(32rem 20rem at 50% 40%, #1f2226, transparent 74%), var(--color-tb50-bg);
}
/* Pointer defaults: the card is correct before and without JS. */

.tb-50__card {
  --tx: 0;
  --ty: 0;
  --tilt: 0deg;
  --mx: 50%;
  --my: 50%;
  --tb-50-tilt-max: 9;
  background-color: var(--color-tb50-card);
  background-image: repeating-linear-gradient(0deg, rgba(109,143,134,.14) 0 1px, transparent 1px 1.05rem), linear-gradient(168deg, var(--color-tb50-card), var(--color-tb50-card-lo));
}

.tb-50__sheen {
  background: radial-gradient(12rem 8rem at var(--mx) var(--my), rgba(255,255,255,.5), transparent 66%);
}
/* THE PUNCHES: a column rhythm INTERSECTED with two row bands, so holes exist
   only where both agree. Real holes — the page shows through them. */

@supports ((mask-composite: intersect) or (-webkit-mask-composite: source-in)) {
  .tb-50__holes {
    background: linear-gradient(180deg, rgba(0,0,0,.55), rgba(0,0,0,.4));
    -webkit-mask: repeating-linear-gradient(90deg, #000 0 .3rem, transparent .3rem .62rem) 0 0/100% 100%, repeating-linear-gradient(180deg, transparent 0 3.2rem, #000 3.2rem 3.75rem, transparent 3.75rem 4.9rem, #000 4.9rem 5.45rem, transparent 5.45rem 100%) 0 0/100% 100%;
    mask: repeating-linear-gradient(90deg, #000 0 .3rem, transparent .3rem .62rem) 0 0/100% 100%, repeating-linear-gradient(180deg, transparent 0 3.2rem, #000 3.2rem 3.75rem, transparent 3.75rem 4.9rem, #000 4.9rem 5.45rem, transparent 5.45rem 100%) 0 0/100% 100%;
    -webkit-mask-composite: source-in;
    mask-composite: intersect;
  }
}

@media (prefers-color-scheme: light) {
  .tb-50:not([data-theme="dark"]) {
    --color-tb50-bg: oklch(0.23 0.008 250);
  }
}

.tb-50[data-theme="light"] {
  --color-tb50-bg: oklch(0.23 0.008 250);
}

@media (forced-colors: active) {
  .tb-50__card {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    filter: none;
    transform: none;
    clip-path: none;
  }

  .tb-50__holes,
    .tb-50__sheen {
    display: none;
  }

  .tb-50__card span {
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.tb-50__card');
  if (!btn) return;
  const max = Number(getComputedStyle(btn).getPropertyValue('--tb-50-tilt-max')) || 9;
  let box = null;
  btn.addEventListener('pointerenter', () => { box = btn.getBoundingClientRect(); });
  btn.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    box = box || btn.getBoundingClientRect();
    const nx = (e.clientX - box.left) / box.width;
    const ny = (e.clientY - box.top) / box.height;
    btn.style.setProperty('--mx', (nx * 100).toFixed(1) + '%');
    btn.style.setProperty('--my', (ny * 100).toFixed(1) + '%');
    btn.style.setProperty('--tx', (nx - 0.5).toFixed(3));
    btn.style.setProperty('--ty', (0.5 - ny).toFixed(3));
    btn.style.setProperty('--tilt', (Math.hypot(nx - 0.5, ny - 0.5) * 2 * max).toFixed(2) + 'deg');
  });
  btn.addEventListener('pointerleave', () => {
    box = null;
    btn.style.setProperty('--tilt', '0deg');
    btn.style.setProperty('--tx', '0');
    btn.style.setProperty('--ty', '0');
    btn.style.setProperty('--mx', '50%');
    btn.style.setProperty('--my', '50%');
  });
})();
```
