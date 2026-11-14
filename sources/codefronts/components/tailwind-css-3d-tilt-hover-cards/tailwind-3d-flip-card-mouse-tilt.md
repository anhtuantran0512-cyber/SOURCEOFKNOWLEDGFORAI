---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-flip-card-mouse-tilt/"
title: "Tailwind 3D Flip Card with Mouse Tilt (Click to Flip)"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "Tilt and flip in one transform: the card follows the cursor, and a click (or Enter/Space) swings it 180° to reveal contact details — and it keeps tilting…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Flip Card with Mouse Tilt (Click to Flip)
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-flip-card-mouse-tilt/

Tilt and flip in one transform: the card follows the cursor, and a click (or Enter/Space) swings it 180° to reveal contact details — and it keeps tilting while flipped. Flip and tilt compose in one rotateY(calc(var(--flip)_+_var(--ry))). The port fixes a real bug: the hidden face is now inert, so its buttons can no longer be tabbed to while invisible.
## HTML
```html
<section class="ttc-12 w-full min-h-svh grid place-items-center bg-ttc12-bg bg-[radial-gradient(80%_90%_at_70%_20%,var(--color-ttc12-lobe),transparent_60%)] px-6 py-14 font-ttc12-sans text-white" aria-label="3D flip card with mouse tilt demo">
  <div class="grid w-full justify-items-center gap-8">
    <div data-ttc12-scene class="w-full max-w-[19.5rem] perspective-[1100px]">
      <div data-carrier class="relative h-60 transform-3d [transform:rotateX(var(--rx,0deg))_rotateY(calc(var(--flip,0deg)_+_var(--ry,0deg)))] transition-transform duration-700 ease-[cubic-bezier(0.3,0.8,0.3,1.1)] data-live:duration-90 data-live:ease-linear motion-reduce:transition-none">
        <article data-face="front" class="absolute inset-0 flex flex-col rounded-[20px] border border-ttc12-acc/35 bg-linear-160 from-ttc12-card1 to-ttc12-card2 p-6 shadow-[0_26px_54px_-26px_oklch(0_0_0/0.8)] backface-hidden">
          <p class="font-ttc12-mono text-[10.5px] font-bold tracking-[0.2em] text-ttc12-acc">FREELANCE · SF</p>
          <h3 class="mt-3 text-[28px] leading-none font-bold tracking-[-0.02em]">Jonah Reyes</h3>
          <p class="mt-1.5 text-sm text-ttc12-mut">Motion &amp; Brand Designer</p>
          <button data-flip type="button" aria-pressed="false" class="mt-auto inline-flex min-h-11 cursor-pointer items-center gap-2 self-start rounded-full bg-ttc12-acc px-5 text-[13px] font-semibold text-ttc12-bg transition-transform hover:scale-105 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">Contact <span aria-hidden="true">↻</span></button>
        </article>
        <article data-face="back" inert class="absolute inset-0 flex flex-col rounded-[20px] border border-ttc12-acc/35 bg-linear-160 from-ttc12-card1 to-ttc12-card2 p-6 shadow-[0_26px_54px_-26px_oklch(0_0_0/0.8)] backface-hidden [transform:rotateY(180deg)]">
          <p class="font-ttc12-mono text-[10.5px] font-bold tracking-[0.2em] text-ttc12-acc">SAY HELLO</p>
          <ul class="mt-2 grid text-[14px]">
            <li><a href="mailto:[email protected]" class="flex min-h-11 items-center gap-3 rounded-lg text-white no-underline hover:text-ttc12-acc focus-visible:outline-2 focus-visible:outline-ttc12-acc"><svg aria-hidden="true" viewBox="0 0 24 24" class="size-4 flex-none text-ttc12-acc" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>[email protected]</a></li>
            <li><a href="tel:+14155550132" class="flex min-h-11 items-center gap-3 rounded-lg text-white no-underline hover:text-ttc12-acc focus-visible:outline-2 focus-visible:outline-ttc12-acc"><svg aria-hidden="true" viewBox="0 0 24 24" class="size-4 flex-none text-ttc12-acc" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>+1 (415) 555-0132</a></li>
          </ul>
          <button data-flip type="button" aria-pressed="true" class="mt-auto inline-flex min-h-11 cursor-pointer items-center gap-2 self-start rounded-full border border-white/25 px-5 text-[13px] font-semibold text-white transition-colors hover:bg-white/10 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white"><span aria-hidden="true">↺</span> Back</button>
        </article>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/12 bg-white/5 px-3.5 py-2 font-ttc12-mono text-[11.5px] text-ttc12-mut">rotateY(calc(var(--flip)_+_var(--ry))) · backface-hidden · inert</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc12-bg: #0e0d15;
  --color-ttc12-bg: oklch(0.15 0.015 270);
  --color-ttc12-lobe: #3b2f14b3;
  --color-ttc12-lobe: oklch(0.25 0.05 80 / 0.7);
  --color-ttc12-card1: #2a2517;
  --color-ttc12-card1: oklch(0.23 0.03 80);
  --color-ttc12-card2: #16151d;
  --color-ttc12-card2: oklch(0.17 0.02 270);
  --color-ttc12-acc: #e8b94a;
  --color-ttc12-acc: oklch(0.8 0.14 80);
  --color-ttc12-mut: #c6c3cf;
  --color-ttc12-mut: oklch(0.82 0.015 280);
  --font-ttc12-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-ttc12-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-12 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc12-scene]').forEach((scene) => {
    if (scene.dataset.wired) return;
    scene.dataset.wired = '1';
    const carrier = scene.querySelector('[data-carrier]');
    const front = carrier.querySelector('[data-face="front"]');
    const back = carrier.querySelector('[data-face="back"]');
    const btns = carrier.querySelectorAll('[data-flip]');
    let flipped = false, swinging = 0;
    const setFlip = (f) => {
      flipped = f;
      carrier.style.setProperty('--flip', f ? '180deg' : '0deg');
      front.inert = f;              // hidden face leaves the tab order AND the a11y tree
      back.inert = !f;
      btns.forEach((b) => b.setAttribute('aria-pressed', String(f)));
      carrier.removeAttribute('data-live'); // fall back to the slow 700ms swing
      clearTimeout(swinging);
      swinging = setTimeout(() => { swinging = 0; }, 700);
      (f ? back : front).querySelector('[data-flip]').focus({ preventScroll: true });
    };
    btns.forEach((b) => b.addEventListener('click', () => setFlip(!flipped)));
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 10;
    scene.addEventListener('pointermove', (e) => {
      if (swinging) return; // let the swing finish clean
      const r = scene.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      const dir = flipped ? -1 : 1; // pointer-left is back-face-right
      carrier.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      carrier.style.setProperty('--ry', (dir * (px - 0.5) * MAX).toFixed(2) + 'deg');
      carrier.setAttribute('data-live', '');
    });
    scene.addEventListener('pointerleave', () => {
      carrier.removeAttribute('data-live');
      carrier.style.setProperty('--rx', '0deg');
      carrier.style.setProperty('--ry', '0deg');
    });
  });
})();
```
