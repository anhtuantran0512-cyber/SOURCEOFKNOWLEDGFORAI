---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-mouse-tracking-liquid-glass-lens-hero/"
title: "Mouse-Tracking Liquid Glass Lens Hero in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A Liquid Glass lens that follows the pointer across a shifting conic-mesh hero, refracting the headline and colours beneath it with an eased spring; on touch…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mouse-Tracking Liquid Glass Lens Hero in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-mouse-tracking-liquid-glass-lens-hero/

A Liquid Glass lens that follows the pointer across a shifting conic-mesh hero, refracting the headline and colours beneath it with an eased spring; on touch it drifts in a slow figure-eight until you drag. Now with real CTAs and a reduced-motion path.
## HTML
```html
<section data-ths31-hero style="--mx:50%;--my:50%" class="ths-31 relative isolate grid w-full min-h-svh cursor-crosshair touch-pan-y content-center overflow-hidden bg-[conic-gradient(from_60deg_at_30%_30%,var(--color-ths31-amber),var(--color-ths31-red),var(--color-ths31-violet),var(--color-ths31-cyan),var(--color-ths31-amber))] bg-size-[200%_200%] px-6 py-16 font-ths31-sans text-white animate-ths31-mesh motion-reduce:animate-none sm:px-12" aria-label="Mouse-tracking liquid glass hero">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(70%_60%_at_20%_60%,rgb(0_0_0/0.28),transparent_70%)]"></div>
  <div class="max-w-3xl">
    <p class="text-[13px] font-semibold tracking-[0.14em] uppercase [text-shadow:0_1px_8px_rgb(0_0_0/0.3)]">Frontend that feels physical</p>
    <h1 class="mt-3 font-ths31-display text-[clamp(64px,14vw,150px)] leading-[0.88] font-extrabold tracking-[-0.045em] [text-shadow:0_4px_24px_rgb(0_0_0/0.28)]">Liquid<br>Glass</h1>
    <p class="mt-5 max-w-[34ch] text-base/relaxed [text-shadow:0_1px_8px_rgb(0_0_0/0.35)]">Move — or tap and drag on touch — the lens refracts everything beneath it.</p>
    <div class="mt-8 flex flex-wrap gap-3">
      <a href="#work" class="inline-flex min-h-12 cursor-pointer items-center rounded-full bg-white px-7 text-[15px] font-semibold text-ths31-ink shadow-[0_12px_30px_-10px_rgb(0_0_0/0.45)] transition hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white motion-reduce:transition-none">See the work</a>
      <a href="#source" class="inline-flex min-h-12 cursor-pointer items-center rounded-full border border-white/60 bg-white/10 px-6 text-[15px] font-semibold text-white backdrop-blur-sm transition hover:bg-white/20 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white">View source</a>
    </div>
  </div>
  <span aria-hidden="true" data-ths31-lens class="pointer-events-none absolute top-(--my) left-(--mx) size-48 -translate-1/2 rounded-full border-2 border-white/70 bg-[radial-gradient(circle_at_35%_30%,rgb(255_255_255/0.32),rgb(255_255_255/0.05)_55%,transparent_72%)] shadow-[inset_0_3px_12px_rgb(255_255_255/0.55),inset_0_-12px_26px_rgb(0_0_0/0.28),0_14px_40px_-8px_rgb(0_0_0/0.55)] backdrop-blur-md backdrop-contrast-110 backdrop-saturate-200 motion-reduce:hidden"></span>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths31-ink: #1c1030;
  --color-ths31-ink: oklch(0.209 0.062 298.2);
  --color-ths31-amber: #f59e0b;
  --color-ths31-amber: oklch(0.769 0.165 70.1);
  --color-ths31-red: #ef4444;
  --color-ths31-red: oklch(0.637 0.208 25.3);
  --color-ths31-violet: #8b5cf6;
  --color-ths31-violet: oklch(0.606 0.219 292.7);
  --color-ths31-cyan: #06b6d4;
  --color-ths31-cyan: oklch(0.715 0.126 215.2);
  --font-ths31-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-ths31-sans: 'Geist', system-ui, sans-serif;
  --animate-ths31-mesh: ths31-mesh 16s ease-in-out infinite;

  @keyframes ths31-mesh {
    50% {
      background-position: 100% 100%;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-31 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('[data-ths31-hero]').forEach((hero) => {
    if (hero.dataset.wired || reduce) return;
    hero.dataset.wired = '1';
    const coarse = matchMedia('(pointer: coarse)').matches;
    let tx = 0, ty = 0, x = 0, y = 0, raf = 0, orbit = 0, t0 = 0;
    const paint = () => { hero.style.setProperty('--mx', x + 'px'); hero.style.setProperty('--my', y + 'px'); };
    const centre = () => { const b = hero.getBoundingClientRect(); tx = b.width / 2; ty = b.height / 2; };
    const loop = () => {
      x += (tx - x) * 0.14; y += (ty - y) * 0.14; paint();
      raf = (Math.abs(tx - x) > 0.5 || Math.abs(ty - y) > 0.5) ? requestAnimationFrame(loop) : 0;
    };
    const kick = () => { if (!raf) raf = requestAnimationFrame(loop); };
    const startOrbit = () => {
      if (orbit) return;
      const step = (t) => {
        if (!t0) t0 = t;
        const s = (t - t0) / 1000, b = hero.getBoundingClientRect();
        x = tx = b.width / 2 + Math.cos(s * 0.7) * b.width * 0.28;
        y = ty = b.height / 2 + Math.sin(s * 1.4) * b.height * 0.22;
        paint(); orbit = requestAnimationFrame(step);
      };
      orbit = requestAnimationFrame(step);
    };
    const stopOrbit = () => { cancelAnimationFrame(orbit); orbit = 0; t0 = 0; };
    hero.addEventListener('pointermove', (e) => {
      if (e.pointerType === 'touch' && !e.isPrimary) return;
      stopOrbit();
      const b = hero.getBoundingClientRect();
      tx = e.clientX - b.left; ty = e.clientY - b.top; kick();
    });
    hero.addEventListener('pointerleave', () => { centre(); kick(); if (coarse) setTimeout(startOrbit, 800); });
    const init = () => {
      const b = hero.getBoundingClientRect();
      if (b.width < 32 || b.height < 32) return requestAnimationFrame(init);
      centre(); x = tx; y = ty; paint();
      if (coarse) startOrbit();
    };
    init();
  });
})();
```
