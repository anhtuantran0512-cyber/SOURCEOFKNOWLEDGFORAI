---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-holographic-foil-sticker-button/"
title: "Tailwind Holographic Foil Sticker Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A die-cut vinyl sticker whose holographic laminate shifts with the pointer: the rainbow sweep, the specular conic and a 3D tilt all read from pointer…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Holographic Foil Sticker Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-holographic-foil-sticker-button/

A die-cut vinyl sticker whose holographic laminate shifts with the pointer: the rainbow sweep, the specular conic and a 3D tilt all read from pointer variables, and the corner peels up as you approach. The effect collectors call "cracked ice".
## HTML
```html
<div class="tb-29 w-full min-h-svh grid place-items-center font-tb29-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-29__sticker group relative overflow-hidden isolate cursor-pointer p-2 border-[0.32rem] border-tb29-cut rounded-[1.35rem] bg-tb29-plate text-tb29-ink drop-shadow-[0_16px_26px_#0000008c] [transform:perspective(700px)_rotate3d(var(--ty),var(--tx),0,var(--tilt))] transition-[transform,filter] duration-[350ms] ease-tb29-out touch-manipulation [-webkit-tap-highlight-color:transparent] active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb29-focus motion-reduce:transition-none motion-reduce:[transform:none]">
    <span aria-hidden="true" class="tb-29__holo absolute inset-0 z-20 pointer-events-none opacity-55 transition-opacity duration-[350ms] group-hover:opacity-95 group-focus-visible:opacity-95 motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="tb-29__peel absolute z-30 -top-px -right-px size-6.5 pointer-events-none scale-0 origin-top-right [clip-path:polygon(100%_0,100%_100%,0_0)] bg-[linear-gradient(225deg,#ffffff,#cfd2dc_55%,#9aa0b0)] drop-shadow-[-2px_3px_3px_#00000066] transition-transform duration-[400ms] ease-tb29-out group-hover:scale-100 group-focus-visible:scale-100 motion-reduce:transition-none"></span>
    <span class="relative z-10 grid gap-0.5 justify-items-start min-h-12 px-6 py-2.5 rounded-[0.85rem] bg-[linear-gradient(180deg,var(--color-tb29-plate-lift),var(--color-tb29-plate))]">
      <span class="text-[1.0625rem] font-extrabold tracking-[-0.02em]">Limited drop</span>
      <span class="text-[0.6875rem] font-bold tracking-[0.18em] uppercase tabular-nums text-tb29-muted">01 / 250</span>
    </span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb29-bg: #0a0a0f;
  --color-tb29-bg: oklch(0.12 0.01 285);
  --color-tb29-cut: #fbfbfd;
  --color-tb29-plate: #111119;
  --color-tb29-plate: oklch(0.18 0.012 285);
  --color-tb29-plate-lift: #1a1a24;
  --color-tb29-plate-lift: oklch(0.22 0.012 285);
  --color-tb29-ink: #f6f6fb;
  --color-tb29-muted: #a9a9be;
  --color-tb29-muted: oklch(0.73 0.02 285);
  --color-tb29-focus: #4facfe;
  --color-tb29-focus: oklch(0.72 0.14 235);
  --font-tb29-sans: "Archivo", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb29-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-29 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(40rem 24rem at 50% 45%, #1b1b28, transparent 72%), var(--color-tb29-bg);
}
/* Pointer defaults — the sticker is correct before and without JS. */

.tb-29__sticker {
  --mx: 50%;
  --my: 50%;
  --tx: 0;
  --ty: 0;
  --tilt: 0deg;
  --tb-29-tilt-max: 8;
}
/* THE LAMINATE: a repeating rainbow multiplied by a pointer-anchored specular
   conic, blended into the plate. Two layers whose positions both read --mx/--my. */

.tb-29__holo {
  mix-blend-mode: color-dodge;
  background-image: repeating-linear-gradient(102deg, #ff5f6d 0 12%, #ffc371 18%, #47e5bc 30%, #4facfe 42%, #b06ab3 54%, #ff5f6d 66%), conic-gradient(from 210deg at var(--mx) var(--my), rgba(255,255,255,.55), transparent 28%, rgba(255,255,255,.4) 62%, transparent 88%);
  background-size: 340% 340%, 100% 100%;
  background-position: var(--mx) var(--my), 0 0;
}

@media (prefers-color-scheme: light) {
  .tb-29:not([data-theme="dark"]) {
    --color-tb29-bg: oklch(0.93 0.004 285);
  }
}

.tb-29[data-theme="light"] {
  --color-tb29-bg: oklch(0.93 0.004 285);
}

@media (forced-colors: active) {
  .tb-29__sticker {
    background: ButtonFace;
    border-color: ButtonText;
    filter: none;
    transform: none;
  }

  .tb-29__holo,
    .tb-29__peel {
    display: none;
  }

  .tb-29__sticker > span:last-child {
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const btn = document.querySelector('.tb-29__sticker');
  if (!btn) return;
  const max = Number(getComputedStyle(btn).getPropertyValue('--tb-29-tilt-max')) || 8;
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
    btn.style.setProperty('--mx', '50%');
    btn.style.setProperty('--my', '50%');
  });
})();
```
