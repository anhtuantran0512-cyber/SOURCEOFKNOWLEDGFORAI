---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/magnetic-cross/"
title: "Magnetic Cursor Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "The award-site magnetic button: inside a 170px field the button leans toward the cursor and the × leans further, a parallax that makes the glyph feel attracted."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Cursor Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/magnetic-cross/

The award-site magnetic button: inside a 170px field the button leans toward the cursor and the × leans further, a parallax that makes the glyph feel attracted. The script writes four custom properties; Tailwind reads them with translate-x-(--tcb14-mx). On leave, group-data-releasing/zone: swaps in an elastic overshoot curve. Because translate and scale are separate properties, active:scale-92 presses without cancelling the pull.
## HTML
```html
<section class="tcb-14 w-full min-h-svh grid place-items-center bg-tcb14-bg bg-[radial-gradient(110%_120%_at_50%_0%,var(--color-tcb14-glow),transparent_60%)] px-6 py-12 font-tcb14-sans" aria-label="Magnetic close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div id="tcb-14-zone" class="group/zone grid size-[170px] place-items-center rounded-full border border-dashed border-tcb14-acc/20 [--tcb14-gx:0px] [--tcb14-gy:0px] [--tcb14-mx:0px] [--tcb14-my:0px]">
      <button type="button" aria-label="Close" class="grid size-16 translate-x-(--tcb14-mx) translate-y-(--tcb14-my) cursor-pointer place-items-center rounded-full border-[1.5px] border-tcb14-acc/40 bg-tcb14-btn shadow-[0_16px_36px_-18px_rgb(0_0_0/0.8)] transition-[translate,scale,border-color] duration-80 ease-linear group-data-releasing/zone:duration-500 group-data-releasing/zone:ease-[cubic-bezier(.34,1.8,.44,1)] hover:border-tcb14-acc focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb14-acc active:scale-92">
        <span aria-hidden="true" class="relative size-5 translate-x-(--tcb14-gx) translate-y-(--tcb14-gy) transition-[translate] duration-80 ease-linear group-data-releasing/zone:duration-500 group-data-releasing/zone:ease-[cubic-bezier(.34,1.8,.44,1)] before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-tcb14-acc after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-tcb14-acc"></span>
      </button>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb14-mono text-[11.5px] text-tcb14-mut ring-1 ring-white/12">translate-x-(--tcb14-mx) · group-data-releasing/zone: · active:scale-92</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb14-bg: #0e1714;
  --color-tcb14-bg: oklch(0.16 0.02 170);
  --color-tcb14-glow: #173427e6;
  --color-tcb14-glow: oklch(0.24 0.04 160 / 0.9);
  --color-tcb14-btn: #131f1b;
  --color-tcb14-btn: oklch(0.2 0.03 165);
  --color-tcb14-acc: #4fd68a;
  --color-tcb14-acc: oklch(0.78 0.17 150);
  --color-tcb14-mut: #9fb8ad;
  --color-tcb14-mut: oklch(0.76 0.03 165);
  --font-tcb14-sans: 'Geist', system-ui, sans-serif;
  --font-tcb14-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-14 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const zone = document.getElementById('tcb-14-zone');
  if (!zone || zone.dataset.wired) return;
  zone.dataset.wired = '1';
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 14;
  const clamp = (v) => Math.max(-MAX, Math.min(MAX, v));
  const set = (mx, my, gx, gy) => {
    zone.style.setProperty('--tcb14-mx', mx + 'px');
    zone.style.setProperty('--tcb14-my', my + 'px');
    zone.style.setProperty('--tcb14-gx', gx + 'px');
    zone.style.setProperty('--tcb14-gy', gy + 'px');
  };
  zone.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse') return;
    zone.removeAttribute('data-releasing');
    const r = zone.getBoundingClientRect();
    const dx = e.clientX - (r.left + r.width / 2);
    const dy = e.clientY - (r.top + r.height / 2);
    set(clamp(dx * 0.3), clamp(dy * 0.3), clamp(dx * 0.45), clamp(dy * 0.45));
  });
  zone.addEventListener('pointerleave', () => {
    zone.setAttribute('data-releasing', '');
    set(0, 0, 0, 0);
  });
})();
```
