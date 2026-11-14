---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-3d-tilt-card-radio-selector/"
title: "Tailwind 3D Tilt Card Radio Selector"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "Premium selectable cards that tilt toward the cursor like they're on gimbals, with a glare sheen sweeping across as they rotate."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt Card Radio Selector
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-3d-tilt-card-radio-selector/

Premium selectable cards that tilt toward the cursor like they're on gimbals, with a glare sheen sweeping across as they rotate. perspective-[900px] on the row, transform-3d on the card, and an arbitrary [transform:rotateX(var(--rx))…] that a small controller feeds. The checked card locks in an accent edge-light and a check badge.
## HTML
```html
<section class="trb-12 w-full min-h-svh grid place-items-center bg-trb12-bg bg-[linear-gradient(160deg,var(--color-trb12-top),transparent_60%)] px-6 py-14 font-trb12-sans text-trb12-ink" aria-label="3D tilt card option selector demo">
  <fieldset data-trb12-group>
    <legend class="text-center text-[26px] font-bold tracking-[-0.02em]">Render tier</legend>
    <div class="mt-8 flex flex-wrap justify-center gap-5 perspective-[900px]">
      <label class="group relative cursor-pointer">
        <input type="radio" name="trb-12" value="swift" class="sr-only">
        <span data-trb12-card class="relative grid w-48 gap-1.5 overflow-hidden rounded-2xl border-[1.5px] border-white/10 bg-[linear-gradient(165deg,#1c2130,#141826)] px-5 py-6 transform-3d [transform:rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-[transform,border-color,box-shadow] duration-200 ease-out before:pointer-events-none before:absolute before:inset-0 before:translate-x-[var(--gx,0px)] before:bg-[linear-gradient(115deg,transparent_30%,rgb(255_255_255/0.16)_48%,transparent_62%)] before:opacity-(--go) before:transition-opacity before:duration-300 before:content-[''] [--go:0] group-has-checked:border-trb12-acc group-has-checked:shadow-trb12-edge group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-trb12-acc">
          <span aria-hidden="true" class="absolute top-4 right-4 grid size-6 scale-0 place-items-center rounded-full bg-trb12-acc text-trb12-bg transition-transform duration-300 ease-trb12-spring group-has-checked:scale-100"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7"/></svg></span>
          <span class="mb-1.5 text-xl font-bold tracking-[-0.01em] text-white">Swift</span>
          <span class="font-trb12-mono text-[13px] text-trb12-mut">8 GB VRAM</span>
          <span class="font-trb12-mono text-[13px] text-trb12-mut">1080p · 60 fps</span>
          <span class="mt-3 text-base font-bold text-trb12-acc">$0.14<small class="text-xs font-medium text-trb12-mut">/hr</small></span>
        </span>
      </label>
      <label class="group relative cursor-pointer">
        <input type="radio" name="trb-12" value="surge" class="sr-only" checked>
        <span data-trb12-card class="relative grid w-48 gap-1.5 overflow-hidden rounded-2xl border-[1.5px] border-white/10 bg-[linear-gradient(165deg,#1c2130,#141826)] px-5 py-6 transform-3d [transform:rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-[transform,border-color,box-shadow] duration-200 ease-out before:pointer-events-none before:absolute before:inset-0 before:translate-x-[var(--gx,0px)] before:bg-[linear-gradient(115deg,transparent_30%,rgb(255_255_255/0.16)_48%,transparent_62%)] before:opacity-(--go) before:transition-opacity before:duration-300 before:content-[''] [--go:0] group-has-checked:border-trb12-acc group-has-checked:shadow-trb12-edge group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-trb12-acc">
          <span aria-hidden="true" class="absolute top-4 right-4 grid size-6 scale-0 place-items-center rounded-full bg-trb12-acc text-trb12-bg transition-transform duration-300 ease-trb12-spring group-has-checked:scale-100"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7"/></svg></span>
          <span class="mb-1.5 text-xl font-bold tracking-[-0.01em] text-white">Surge</span>
          <span class="font-trb12-mono text-[13px] text-trb12-mut">24 GB VRAM</span>
          <span class="font-trb12-mono text-[13px] text-trb12-mut">1440p · 144 fps</span>
          <span class="mt-3 text-base font-bold text-trb12-acc">$0.38<small class="text-xs font-medium text-trb12-mut">/hr</small></span>
        </span>
      </label>
      <label class="group relative cursor-pointer">
        <input type="radio" name="trb-12" value="titan" class="sr-only">
        <span data-trb12-card class="relative grid w-48 gap-1.5 overflow-hidden rounded-2xl border-[1.5px] border-white/10 bg-[linear-gradient(165deg,#1c2130,#141826)] px-5 py-6 transform-3d [transform:rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-[transform,border-color,box-shadow] duration-200 ease-out before:pointer-events-none before:absolute before:inset-0 before:translate-x-[var(--gx,0px)] before:bg-[linear-gradient(115deg,transparent_30%,rgb(255_255_255/0.16)_48%,transparent_62%)] before:opacity-(--go) before:transition-opacity before:duration-300 before:content-[''] [--go:0] group-has-checked:border-trb12-acc group-has-checked:shadow-trb12-edge group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-trb12-acc">
          <span aria-hidden="true" class="absolute top-4 right-4 grid size-6 scale-0 place-items-center rounded-full bg-trb12-acc text-trb12-bg transition-transform duration-300 ease-trb12-spring group-has-checked:scale-100"><svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7"/></svg></span>
          <span class="mb-1.5 text-xl font-bold tracking-[-0.01em] text-white">Titan</span>
          <span class="font-trb12-mono text-[13px] text-trb12-mut">80 GB VRAM</span>
          <span class="font-trb12-mono text-[13px] text-trb12-mut">4K · 240 fps</span>
          <span class="mt-3 text-base font-bold text-trb12-acc">$1.20<small class="text-xs font-medium text-trb12-mut">/hr</small></span>
        </span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb12-bg: #0a0c12;
  --color-trb12-bg: oklch(0.15 0.01 265);
  --color-trb12-top: #151928;
  --color-trb12-top: oklch(0.21 0.03 270);
  --color-trb12-ink: #eef1fa;
  --color-trb12-ink: oklch(0.96 0.01 270);
  --color-trb12-mut: #9ba3bf;
  --color-trb12-mut: oklch(0.72 0.03 270);
  --color-trb12-acc: #2fd0c8;
  --color-trb12-acc: oklch(0.78 0.13 185);
  --shadow-trb12-edge: 0 0 0 1px oklch(0.78 0.13 185 / 0.6), 0 24px 48px -20px oklch(0.78 0.13 185 / 0.45);
  --ease-trb12-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb12-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-trb12-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-12 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const init = () => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches || !matchMedia('(pointer: fine)').matches) return;
    const MAX_TILT = 10, GLARE_SWEEP = 90;
    document.querySelectorAll('[data-trb12-group]').forEach((group) => {
      if (group.dataset.wired) return;
      group.dataset.wired = '1';
      group.querySelectorAll('[data-trb12-card]').forEach((card) => {
        const opt = card.closest('label');
        const set = (k, v) => card.style.setProperty(k, v);
        opt.addEventListener('pointermove', (e) => {
          const r = card.getBoundingClientRect();
          const px = (e.clientX - r.left) / r.width - 0.5, py = (e.clientY - r.top) / r.height - 0.5;
          set('--ry', (px * MAX_TILT * 2).toFixed(2) + 'deg');
          set('--rx', (-py * MAX_TILT * 2).toFixed(2) + 'deg');
          set('--gx', (px * GLARE_SWEEP).toFixed(1) + 'px');
          set('--go', '1');
        }, { passive: true });
        opt.addEventListener('pointerleave', () => { set('--rx', '0deg'); set('--ry', '0deg'); set('--gx', '0px'); set('--go', '0'); });
      });
    });
  };
  document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', init) : init();
})();
```
