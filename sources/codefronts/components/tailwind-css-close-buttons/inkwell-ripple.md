---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/inkwell-ripple/"
title: "Material Ripple Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "The Material ink ripple without a library: the script records the press point as --tcb18-rx/--tcb18-ry, the after: pseudo-element is positioned there with…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Ripple Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/inkwell-ripple/

The Material ink ripple without a library: the script records the press point as --tcb18-rx/--tcb18-ry, the after: pseudo-element is positioned there with after:left-(--tcb18-rx), and data-rippling:after:animate-tcb18-ink blooms it. Keyboard presses ripple from the centre, so the feedback is identical for every input.
## HTML
```html
<section class="tcb-18 w-full min-h-svh grid place-items-center bg-tcb18-bg px-6 py-12 font-tcb18-sans" aria-label="Material ripple close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="flex w-full max-w-[22rem] items-center gap-4 rounded-3xl bg-white px-5 py-4 shadow-[0_2px_6px_-2px_var(--color-tcb18-shadow)]">
      <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-full bg-tcb18-tonal font-semibold text-tcb18-acc">M</span>
      <div class="min-w-0 flex-1">
        <div class="text-[15px] font-medium text-tcb18-text">Backup complete</div>
        <div class="text-[13px] text-tcb18-mut">Tap the × anywhere</div>
      </div>
      <button id="tcb-18-btn" type="button" aria-label="Dismiss backup notification" class="relative grid size-12 flex-none cursor-pointer place-items-center overflow-hidden rounded-full bg-white shadow-[0_3px_10px_-2px_var(--color-tcb18-shadow),0_12px_28px_-14px_var(--color-tcb18-shadow)] transition-shadow duration-200 [--tcb18-rx:50%] [--tcb18-ry:50%] after:pointer-events-none after:absolute after:top-(--tcb18-ry) after:left-(--tcb18-rx) after:-ms-7 after:-mt-7 after:size-14 after:rounded-full after:bg-tcb18-ink after:opacity-0 hover:shadow-[0_5px_14px_-2px_var(--color-tcb18-shadow),0_16px_34px_-14px_var(--color-tcb18-shadow)] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb18-acc data-rippling:after:animate-tcb18-ink motion-reduce:data-rippling:after:animate-none">
        <span aria-hidden="true" class="relative size-4.5 before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-4.5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-tcb18-text after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-4.5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-tcb18-text"></span>
      </button>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb18-mono text-[11.5px] text-tcb18-mut ring-1 ring-black/8">after:left-(--tcb18-rx) · data-rippling:after:animate-tcb18-ink</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb18-bg: #efedf8;
  --color-tcb18-bg: oklch(0.95 0.01 285);
  --color-tcb18-tonal: #e6defa;
  --color-tcb18-tonal: oklch(0.92 0.04 290);
  --color-tcb18-text: #3d3a4d;
  --color-tcb18-text: oklch(0.35 0.03 285);
  --color-tcb18-mut: #5e5a70;
  --color-tcb18-mut: oklch(0.47 0.03 285);
  --color-tcb18-acc: #6446d6;
  --color-tcb18-acc: oklch(0.52 0.2 285);
  --color-tcb18-ink: #7a55e059;
  --color-tcb18-ink: oklch(0.55 0.2 285 / 0.35);
  --color-tcb18-shadow: #4d466b73;
  --color-tcb18-shadow: oklch(0.4 0.06 285 / 0.45);
  --font-tcb18-sans: 'Roboto Flex', system-ui, sans-serif;
  --font-tcb18-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tcb18-ink: tcb18-ink 0.45s cubic-bezier(0.2,0.6,0.4,1) forwards;

  @keyframes tcb18-ink {
    0% {
      transform: scale(0);
      opacity: 1;
    }

    100% {
      transform: scale(2.5);
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-18 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const btn = document.getElementById('tcb-18-btn');
  if (!btn || btn.dataset.wired) return;
  btn.dataset.wired = '1';
  const ripple = (x, y) => {
    if (x != null) {
      const r = btn.getBoundingClientRect();
      btn.style.setProperty('--tcb18-rx', (x - r.left) + 'px');
      btn.style.setProperty('--tcb18-ry', (y - r.top) + 'px');
    } else {
      btn.style.setProperty('--tcb18-rx', '50%');
      btn.style.setProperty('--tcb18-ry', '50%');
    }
    btn.removeAttribute('data-rippling');
    requestAnimationFrame(() => requestAnimationFrame(() => btn.setAttribute('data-rippling', '')));
  };
  btn.addEventListener('pointerdown', (e) => ripple(e.clientX, e.clientY));
  btn.addEventListener('keydown', (e) => { if ((e.key === 'Enter' || e.key === ' ') && !e.repeat) ripple(); });
})();
```
