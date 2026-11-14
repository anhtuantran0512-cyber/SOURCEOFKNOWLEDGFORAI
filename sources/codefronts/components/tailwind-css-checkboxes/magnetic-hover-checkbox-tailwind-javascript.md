---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/magnetic-hover-checkbox-tailwind-javascript/"
title: "Magnetic Hover Checkbox in Tailwind CSS + JavaScript"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "The box leans toward your pointer as it crosses the row and springs back when you leave."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Hover Checkbox in Tailwind CSS + JavaScript
Source: https://codefronts.com/components/tailwind-css-checkboxes/magnetic-hover-checkbox-tailwind-javascript/

The box leans toward your pointer as it crosses the row and springs back when you leave. The script writes only two custom properties, which v4 reads with translate-x-(--tcb26-dx); the label now follows at half strength for a layered parallax, and updates are batched per frame.
## HTML
```html
<section class="tcb-26 w-full min-h-svh grid place-items-center bg-tcb26-bg px-5 py-14 font-tcb26-sans text-tcb26-ink selection:bg-tcb26-acc selection:text-white" data-tcb26 aria-label="Magnetic checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb26-line bg-white px-4 py-2">
    <label class="group flex min-h-15 cursor-pointer items-center gap-4 rounded-xl px-2.5 transition-colors [--tcb26-dx:0px] [--tcb26-dy:0px] hover:bg-tcb26-hover" data-magnet><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[26px] flex-none translate-x-(--tcb26-dx) translate-y-(--tcb26-dy) place-items-center rounded-lg border-2 border-tcb26-box bg-white text-white transition-[translate,background-color,border-color] duration-300 ease-[cubic-bezier(.3,1.2,.4,1)] peer-checked:border-tcb26-acc peer-checked:bg-tcb26-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb26-acc motion-reduce:translate-0"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="translate-x-[calc(var(--tcb26-dx)/2)] translate-y-[calc(var(--tcb26-dy)/2)] text-[15px] transition-[translate] duration-300 ease-[cubic-bezier(.3,1.2,.4,1)] motion-reduce:translate-0">Snap to grid</span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-4 rounded-xl px-2.5 transition-colors [--tcb26-dx:0px] [--tcb26-dy:0px] hover:bg-tcb26-hover" data-magnet><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[26px] flex-none translate-x-(--tcb26-dx) translate-y-(--tcb26-dy) place-items-center rounded-lg border-2 border-tcb26-box bg-white text-white transition-[translate,background-color,border-color] duration-300 ease-[cubic-bezier(.3,1.2,.4,1)] peer-checked:border-tcb26-acc peer-checked:bg-tcb26-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb26-acc motion-reduce:translate-0"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="translate-x-[calc(var(--tcb26-dx)/2)] translate-y-[calc(var(--tcb26-dy)/2)] text-[15px] transition-[translate] duration-300 ease-[cubic-bezier(.3,1.2,.4,1)] motion-reduce:translate-0">Magnetic guides</span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-4 rounded-xl px-2.5 transition-colors [--tcb26-dx:0px] [--tcb26-dy:0px] hover:bg-tcb26-hover" data-magnet><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[26px] flex-none translate-x-(--tcb26-dx) translate-y-(--tcb26-dy) place-items-center rounded-lg border-2 border-tcb26-box bg-white text-white transition-[translate,background-color,border-color] duration-300 ease-[cubic-bezier(.3,1.2,.4,1)] peer-checked:border-tcb26-acc peer-checked:bg-tcb26-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb26-acc motion-reduce:translate-0"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="translate-x-[calc(var(--tcb26-dx)/2)] translate-y-[calc(var(--tcb26-dy)/2)] text-[15px] transition-[translate] duration-300 ease-[cubic-bezier(.3,1.2,.4,1)] motion-reduce:translate-0">Auto-align nodes</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb26-bg: #f3f3fa;
  --color-tcb26-bg: oklch(0.965 0.008 280);
  --color-tcb26-ink: #2d2a3d;
  --color-tcb26-ink: oklch(0.29 0.03 285);
  --color-tcb26-line: #e6e5f2;
  --color-tcb26-line: oklch(0.925 0.012 285);
  --color-tcb26-hover: #f7f7fc;
  --color-tcb26-hover: oklch(0.978 0.006 285);
  --color-tcb26-box: #9c99b8;
  --color-tcb26-box: oklch(0.7 0.04 285);
  --color-tcb26-acc: #5b4bd6;
  --color-tcb26-acc: oklch(0.52 0.19 280);
  --font-tcb26-sans: 'Sora', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-26 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  if (matchMedia('(hover: none)').matches || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 6;
  document.querySelectorAll('[data-tcb26]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    root.querySelectorAll('[data-magnet]').forEach((row) => {
      const box = row.querySelector('[aria-hidden]');
      let raf = 0, x = 0, y = 0;
      const write = () => {
        raf = 0;
        row.style.setProperty('--tcb26-dx', x.toFixed(1) + 'px');
        row.style.setProperty('--tcb26-dy', y.toFixed(1) + 'px');
      };
      row.addEventListener('pointermove', (e) => {
        const r = box.getBoundingClientRect();
        x = Math.max(-MAX, Math.min(MAX, (e.clientX - (r.left + r.width / 2)) / 3));
        y = Math.max(-MAX, Math.min(MAX, (e.clientY - (r.top + r.height / 2)) / 3));
        if (!raf) raf = requestAnimationFrame(write);
      });
      row.addEventListener('pointerleave', () => { x = 0; y = 0; if (!raf) raf = requestAnimationFrame(write); });
    });
  });
})();
```
