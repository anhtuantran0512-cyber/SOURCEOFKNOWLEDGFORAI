---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-3d-perspective-tilt-card-stack/"
title: "Tailwind 3D Perspective Tilt Card Stack"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "The holographic deck: five parallax planes, an iridescent conic sweep, a cursor-tracked specular glare and a mask-composite border, tilting toward the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Perspective Tilt Card Stack
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-3d-perspective-tilt-card-stack/

The holographic deck: five parallax planes, an iridescent conic sweep, a cursor-tracked specular glare and a mask-composite border, tilting toward the pointer in real time. This is the demo where the port costs the most &mdash; @property, @keyframes and the mask trick all stay in CSS &mdash; and the payoff is that every translateZ plane is now readable on the element it belongs to instead of five rules away.
## HTML
```html
<section class="stk-06 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk06-sans bg-stk06-bg [background-image:radial-gradient(circle_at_20%_30%,color-mix(in_oklch,var(--color-stk06-a)_22%,transparent),transparent_60%),radial-gradient(circle_at_80%_70%,color-mix(in_oklch,var(--color-stk06-b)_22%,transparent),transparent_60%)]" aria-label="Holographic 3D perspective tilt card stack">
  <div class="relative w-[min(340px,100%)] h-115 [perspective:1200px] [perspective-origin:center_40%] has-focus-visible:outline-3 has-focus-visible:outline-stk06-a has-focus-visible:outline-offset-[12px] has-focus-visible:rounded-[26px]">
    <div class="group relative size-full cursor-grab [transform-style:preserve-3d] [transform:rotateX(var(--stk-06-tilt-x))_rotateY(var(--stk-06-tilt-y))] transition-[--stk-06-tilt-x,--stk-06-tilt-y] duration-400 ease-stk06 focus-visible:outline-none focus-visible:[--stk-06-tilt-x:10deg] focus-visible:[--stk-06-tilt-y:-12deg] motion-reduce:transition-none" id="stk-06-deck" tabindex="0" role="button" aria-label="Interactive holographic card deck. Move the pointer to tilt it.">
      <div class="absolute inset-0 rounded-[22px] bg-linear-[160deg,var(--color-stk06-card),var(--color-stk06-deep)] border border-stk06-edge shadow-[0_30px_60px_-30px_rgba(0,0,0,0.9)] brightness-50 [transform:translateZ(-100px)_translateY(20px)_scale(0.92)]" aria-hidden="true">
        <span class="absolute top-5 right-[22px] font-stk06-mono text-sm font-bold tracking-[0.05em] text-stk06-num">03</span>
      </div>
      <div class="absolute inset-0 rounded-[22px] bg-linear-[160deg,var(--color-stk06-card),var(--color-stk06-deep)] border border-stk06-edge shadow-[0_30px_60px_-30px_rgba(0,0,0,0.9)] brightness-75 [transform:translateZ(-50px)_translateY(10px)_scale(0.96)]" aria-hidden="true">
        <span class="absolute top-5 right-[22px] font-stk06-mono text-sm font-bold tracking-[0.05em] text-stk06-num">02</span>
      </div>
      <div class="absolute inset-0 overflow-hidden rounded-[22px] border border-stk06-edge shadow-[0_30px_60px_-30px_rgba(0,0,0,0.9)] [transform:translateZ(0)] [background-image:linear-gradient(155deg,color-mix(in_oklch,var(--color-stk06-a)_12%,var(--color-stk06-card))_0%,var(--color-stk06-deep)_100%)]">
        <div class="absolute inset-0 rounded-[inherit] pointer-events-none opacity-85 blur-[20px] [transform:translateZ(4px)] [background-image:radial-gradient(circle_at_30%_30%,color-mix(in_oklch,var(--color-stk06-a)_35%,transparent),transparent_50%),radial-gradient(circle_at_70%_70%,color-mix(in_oklch,var(--color-stk06-b)_35%,transparent),transparent_50%)]" aria-hidden="true"></div>
        <div class="absolute inset-0 rounded-[inherit] pointer-events-none opacity-[0.32] mix-blend-color-dodge animate-stk06-spin motion-reduce:animate-none [transform:translateZ(6px)] [background-image:conic-gradient(from_var(--stk-06-holo)_at_var(--stk-06-mx)_var(--stk-06-my),color-mix(in_oklch,var(--color-stk06-a)_70%,transparent),color-mix(in_oklch,var(--color-stk06-b)_70%,transparent),color-mix(in_oklch,var(--color-stk06-c)_70%,transparent),color-mix(in_oklch,var(--color-stk06-a)_70%,transparent))]" aria-hidden="true"></div>
        <div class="absolute inset-0 flex h-full flex-col justify-end gap-2 px-[30px] py-8 text-white [transform:translateZ(30px)]">
          <p class="m-0 font-stk06-mono text-[11px] font-bold tracking-[0.22em] uppercase text-stk06-a">Holographic &middot; 01</p>
          <h3 class="m-0 text-[32px] font-extrabold leading-[1.05] tracking-[-0.03em] text-white">Depth Pass</h3>
          <p class="m-0 max-w-[26ch] text-sm leading-snug text-stk06-body">Move your pointer to tilt the deck. Layered parallax, iridescent sweep, real specular glare.</p>
        </div>
        <div class="absolute inset-0 rounded-[inherit] pointer-events-none opacity-0 mix-blend-overlay transition-opacity duration-300 group-hover:opacity-100 group-focus-visible:opacity-100 [transform:translateZ(35px)] [background-image:radial-gradient(200px_circle_at_var(--stk-06-mx)_var(--stk-06-my),rgba(255,255,255,0.35),transparent_55%)]" aria-hidden="true"></div>
        <div class="stk-06__rim absolute inset-0 rounded-[inherit] pointer-events-none p-0.5 opacity-70 transition-opacity duration-300 group-hover:opacity-100 group-focus-visible:opacity-100 [transform:translateZ(38px)] [background-image:conic-gradient(from_var(--stk-06-holo),var(--color-stk06-a),var(--color-stk06-b),var(--color-stk06-c),var(--color-stk06-a))] [mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] [mask-composite:exclude]" aria-hidden="true"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Registered so they can INTERPOLATE. An unregistered custom property is an
   untyped token: the tilt would snap back instead of easing, and the holo
   angle could not be animated by keyframes at all. No utility form exists. */

@property --stk-06-tilt-x {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: true;
}

@property --stk-06-tilt-y {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: true;
}

@property --stk-06-mx {
  syntax: '<percentage>';
  initial-value: 50%;
  inherits: true;
}

@property --stk-06-my {
  syntax: '<percentage>';
  initial-value: 50%;
  inherits: true;
}

@property --stk-06-holo {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@theme {
  --color-stk06-bg: #04050a;
  --color-stk06-bg: oklch(0.10 0.015 275);
  --color-stk06-card: #1a1c2e;
  --color-stk06-card: oklch(0.24 0.03 285);
  --color-stk06-deep: #0f1120;
  --color-stk06-deep: oklch(0.18 0.028 285);
  --color-stk06-edge: #2a2d48;
  --color-stk06-edge: oklch(0.32 0.035 285);
  --color-stk06-num: #6a72a8;
  --color-stk06-num: oklch(0.55 0.06 285);
  --color-stk06-body: #c3c7de;
  --color-stk06-body: oklch(0.83 0.02 285);
  --color-stk06-a: #c77ce8;
  --color-stk06-a: oklch(0.72 0.18 320);
  --color-stk06-b: #3fa6e0;
  --color-stk06-b: oklch(0.68 0.20 200);
  --color-stk06-c: #e8ab48;
  --color-stk06-c: oklch(0.75 0.19 60);
  --font-stk06-sans: 'Archivo', system-ui, sans-serif;
  --font-stk06-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk06: cubic-bezier(0.22, 1, 0.36, 1);
  --animate-stk06-spin: stk-06-spin 8s linear infinite;
}

@keyframes stk-06-spin {
  from {
    --stk-06-holo: 0deg;
  }

  to {
    --stk-06-holo: 360deg;
  }
}
/* Older Safari spells mask-composite differently, and one class list cannot
   carry two declarations of the same property. */

.stk-06__rim {
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.stk-06');
  if (!root) return;
  const deck = root.querySelector('#stk-06-deck');
  const MAX_DEG = 14;

  /* Touch devices fire synthetic mousemove events; without this guard the card
     jitters under a phantom pointer. Reduced motion opts out entirely. */
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  let raf = 0;
  const set = (rx, ry, mx, my) => {
    deck.style.setProperty('--stk-06-tilt-x', rx + 'deg');
    deck.style.setProperty('--stk-06-tilt-y', ry + 'deg');
    deck.style.setProperty('--stk-06-mx', mx + '%');
    deck.style.setProperty('--stk-06-my', my + '%');
  };

  deck.addEventListener('pointermove', (e) => {
    if (raf) cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      const r = deck.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width;
      const py = (e.clientY - r.top) / r.height;
      set(((0.5 - py) * 2 * MAX_DEG).toFixed(2), ((px - 0.5) * 2 * MAX_DEG).toFixed(2), (px * 100).toFixed(1), (py * 100).toFixed(1));
    });
  });

  deck.addEventListener('pointerleave', () => {
    if (raf) cancelAnimationFrame(raf);
    set(0, 0, 50, 50);
  });
})();
```
