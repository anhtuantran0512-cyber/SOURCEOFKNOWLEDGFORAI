---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-cyberpunk-neon-glow-3d-tilt-card/"
title: "Tailwind Cyberpunk Neon Glow 3D Tilt Card"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "An event-promo card whose neon reacts physically: the magenta and cyan glows are offset FROM the tilt, so the side the card banks away from throws a longer…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cyberpunk Neon Glow 3D Tilt Card
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-cyberpunk-neon-glow-3d-tilt-card/

An event-promo card whose neon reacts physically: the magenta and cyan glows are offset FROM the tilt, so the side the card banks away from throws a longer glow — like a sign swinging in front of a wall. One arbitrary [box-shadow:var(--gx)_var(--gy)_…] carries both throws; scanlines and a soft, non-strobing tube flicker finish the Night City read.
## HTML
```html
<section class="ttc-09 w-full min-h-svh grid place-items-center bg-ttc09-bg bg-[radial-gradient(100%_100%_at_50%_120%,var(--color-ttc09-lobe),transparent_60%)] px-8 py-16 font-ttc09-sans text-white" aria-label="Cyberpunk neon glow tilt card demo">
  <div class="grid w-full justify-items-center gap-10">
    <article data-ttc09-card class="relative w-full max-w-[19rem] overflow-hidden rounded-[14px] border-[1.5px] border-ttc09-pink bg-linear-165 from-ttc09-card1 to-ttc09-card2 p-7 [box-shadow:var(--gx,0px)_var(--gy,10px)_34px_-6px_var(--color-ttc09-pinkglow),calc(var(--gx,0px)*-1)_calc(var(--gy,10px)*-1)_34px_-6px_var(--color-ttc09-cyanglow)] [transform:perspective(1000px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-[transform,box-shadow] duration-550 ease-[cubic-bezier(0.2,0.9,0.3,1.15)] data-live:duration-80 data-live:ease-linear animate-ttc09-flicker motion-reduce:animate-none motion-reduce:transition-none">
      <div aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[repeating-linear-gradient(0deg,oklch(1_0_0/0.055)_0_1px,transparent_1px_3px)] animate-ttc09-drift motion-reduce:animate-none"></div>
      <p class="relative font-ttc09-mono text-[11px] font-bold tracking-[0.22em] text-ttc09-cyan">LIVE // 10.31</p>
      <h3 class="relative mt-3.5 text-[46px] leading-[0.92] font-bold tracking-[0.02em] uppercase [text-shadow:0_0_18px_var(--color-ttc09-pinkglow)]">Neon<br>District</h3>
      <dl class="relative mt-5 grid grid-cols-2 gap-3 border-t border-white/12 pt-4 text-[13px]">
        <div><dt class="font-ttc09-mono text-[10px] tracking-[0.16em] text-ttc09-mut">VENUE</dt><dd class="mt-1 font-semibold">Sector 7 Warehouse</dd></div>
        <div><dt class="font-ttc09-mono text-[10px] tracking-[0.16em] text-ttc09-mut">DOORS</dt><dd class="mt-1 font-semibold tabular-nums">23:00</dd></div>
      </dl>
      <a href="#" class="relative mt-6 flex min-h-12 items-center justify-center rounded-lg border-[1.5px] border-ttc09-pink font-ttc09-mono text-xs font-bold tracking-[0.16em] text-ttc09-pink no-underline transition-colors hover:bg-ttc09-pink hover:text-ttc09-bg focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-ttc09-cyan">CLAIM ACCESS</a>
    </article>
    <p aria-hidden="true" class="rounded-full border border-white/12 bg-white/5 px-3.5 py-2 font-ttc09-mono text-[11.5px] text-ttc09-mut">[box-shadow:var(--gx)_var(--gy)…] · steps(1) flicker</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc09-bg: #0b0810;
  --color-ttc09-bg: oklch(0.11 0.015 300);
  --color-ttc09-lobe: #3a1333b3;
  --color-ttc09-lobe: oklch(0.2 0.07 330 / 0.7);
  --color-ttc09-card1: #1c1320;
  --color-ttc09-card1: oklch(0.17 0.03 320);
  --color-ttc09-card2: #110d16;
  --color-ttc09-card2: oklch(0.13 0.02 300);
  --color-ttc09-pink: #ff3ea5;
  --color-ttc09-pink: oklch(0.68 0.26 350);
  --color-ttc09-pinkglow: #ff3ea58c;
  --color-ttc09-pinkglow: oklch(0.68 0.26 350 / 0.55);
  --color-ttc09-cyan: #37d6f0;
  --color-ttc09-cyan: oklch(0.8 0.14 205);
  --color-ttc09-cyanglow: #37d6f073;
  --color-ttc09-cyanglow: oklch(0.8 0.14 205 / 0.45);
  --color-ttc09-mut: #c2b7c6;
  --color-ttc09-mut: oklch(0.8 0.02 320);
  --font-ttc09-sans: 'Chakra Petch', system-ui, sans-serif;
  --font-ttc09-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttc09-flicker: ttc09-flicker 5s steps(1) infinite;
  --animate-ttc09-drift: ttc09-drift 9s linear infinite;

  @keyframes ttc09-flicker {
    0%,
        100% {
      border-color: var(--color-ttc09-pink);
    }

    7% {
      border-color: color-mix(in oklab, var(--color-ttc09-pink) 60%, transparent);
    }

    9% {
      border-color: var(--color-ttc09-pink);
    }

    54% {
      border-color: color-mix(in oklab, var(--color-ttc09-pink) 75%, transparent);
    }

    57% {
      border-color: var(--color-ttc09-pink);
    }
  }

  @keyframes ttc09-drift {
    to {
      translate: 0 3px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-09 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc09-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 12, GLOW = 1.6; // px of shadow throw per degree of tilt
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const rx = (0.5 - (e.clientY - r.top) / r.height) * MAX;
      const ry = ((e.clientX - r.left) / r.width - 0.5) * MAX;
      card.style.setProperty('--rx', rx.toFixed(2) + 'deg');
      card.style.setProperty('--ry', ry.toFixed(2) + 'deg');
      // Glow throws OPPOSITE the bank: a sign swinging in front of a wall.
      card.style.setProperty('--gx', (-ry * GLOW).toFixed(1) + 'px');
      card.style.setProperty('--gy', (rx * GLOW).toFixed(1) + 'px');
      card.setAttribute('data-live', '');
    });
    card.addEventListener('pointerleave', () => {
      card.removeAttribute('data-live');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
      card.style.setProperty('--gx', '0px');
      card.style.setProperty('--gy', '10px');
    });
  });
})();
```
