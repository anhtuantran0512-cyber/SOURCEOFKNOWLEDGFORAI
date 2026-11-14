---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-holographic-card-effect-3d-tilt/"
title: "Tailwind Holographic Card Effect with 3D Tilt"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "Trading-card-grade holo in utilities: a six-stop oklch conic-gradient foil travels opposite the cursor under mix-blend-color-dodge, a specular stripe rakes…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Holographic Card Effect with 3D Tilt
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-holographic-card-effect-3d-tilt/

Trading-card-grade holo in utilities: a six-stop oklch conic-gradient foil travels opposite the cursor under mix-blend-color-dodge, a specular stripe rakes across on mix-blend-overlay, and the card banks a dramatic ±20°. New in the port: touch screens get a slow idle foil sweep via pointer-coarse:animate-ttc04-sweep, so phones see the holo too.
## HTML
```html
<section class="ttc-04 w-full min-h-svh grid place-items-center bg-ttc04-bg bg-[radial-gradient(100%_120%_at_50%_-10%,var(--color-ttc04-lobe),transparent_60%)] px-6 py-14 font-ttc04-sans text-white" aria-label="Holographic 3D tilt card demo">
  <div class="grid w-full justify-items-center gap-8">
    <article data-ttc04-card class="group/card relative aspect-[5/7] w-full max-w-[17rem] overflow-hidden rounded-[18px] border border-white/20 shadow-[0_34px_70px_-28px_oklch(0_0_0/0.9)] [transform:perspective(900px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-transform duration-650 ease-[cubic-bezier(0.2,0.9,0.3,1.2)] data-live:duration-70 data-live:ease-linear motion-reduce:transition-none" aria-label="Nebula Drifter, number 042 of 500, legendary">
      <img class="absolute inset-0 size-full object-cover saturate-115 contrast-105" src="https://picsum.photos/seed/nebula-drifter/540/756" alt="" loading="lazy">
      <div aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[conic-gradient(from_90deg,oklch(0.7_0.2_20),oklch(0.75_0.19_90),oklch(0.72_0.2_160),oklch(0.7_0.2_230),oklch(0.68_0.21_300),oklch(0.7_0.2_20))] [background-size:220%_220%] [background-position:var(--mx,50%)_var(--my,50%)] saturate-140 brightness-85 mix-blend-color-dodge opacity-0 transition-opacity duration-500 group-data-live/card:opacity-85 pointer-coarse:opacity-60 pointer-coarse:animate-ttc04-sweep motion-reduce:hidden"></div>
      <div aria-hidden="true" class="pointer-events-none absolute -inset-[40%] bg-[linear-gradient(115deg,transparent_42%,oklch(1_0_0/0.65)_50%,transparent_58%)] [background-size:250%_250%] [background-position:var(--mx,50%)_var(--my,50%)] mix-blend-overlay opacity-0 transition-opacity duration-500 group-data-live/card:opacity-100 motion-reduce:hidden"></div>
      <div class="absolute inset-x-3.5 top-3.5 flex items-center justify-between font-ttc04-mono text-[10px] font-semibold tracking-[0.14em]">
        <span class="rounded-full bg-black/45 px-2.5 py-1.5 backdrop-blur-sm">042 / 500</span>
        <span class="rounded-full bg-black/45 px-2.5 py-1.5 text-ttc04-gold backdrop-blur-sm">LEGENDARY</span>
      </div>
      <div class="absolute inset-x-3.5 bottom-3.5 rounded-xl border border-white/15 bg-ttc04-plate px-4 py-3 backdrop-blur-md translate-z-[40px]">
        <h3 class="text-lg font-bold tracking-[-0.01em]">Nebula Drifter</h3>
        <p class="mt-0.5 text-xs text-ttc04-mut">Deep Field series · Artist: K. Oduya</p>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full border border-white/12 bg-white/5 px-3.5 py-2 font-ttc04-mono text-[11.5px] text-ttc04-mut">mix-blend-color-dodge · [background-position:var(--mx)] · pointer-coarse:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc04-bg: #0b0911;
  --color-ttc04-bg: oklch(0.12 0.02 290);
  --color-ttc04-lobe: #2a1a3ee6;
  --color-ttc04-lobe: oklch(0.22 0.06 300 / 0.9);
  --color-ttc04-plate: #0c0a18a6;
  --color-ttc04-plate: oklch(0.14 0.03 290 / 0.65);
  --color-ttc04-gold: #eac36a;
  --color-ttc04-gold: oklch(0.83 0.12 85);
  --color-ttc04-mut: #c7c3d4;
  --color-ttc04-mut: oklch(0.82 0.02 290);
  --font-ttc04-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-ttc04-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttc04-sweep: ttc04-sweep 6s ease-in-out infinite alternate;

  @keyframes ttc04-sweep {
    from {
      background-position: 0% 20%;
    }

    to {
      background-position: 100% 80%;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-04 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc04-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 20; // collectibles earn drama
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
      // Foil travels OPPOSITE the pointer, like light raking across real holo foil.
      card.style.setProperty('--mx', ((1 - px) * 100).toFixed(1) + '%');
      card.style.setProperty('--my', ((1 - py) * 100).toFixed(1) + '%');
      card.setAttribute('data-live', '');
    });
    card.addEventListener('pointerleave', () => {
      card.removeAttribute('data-live');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
