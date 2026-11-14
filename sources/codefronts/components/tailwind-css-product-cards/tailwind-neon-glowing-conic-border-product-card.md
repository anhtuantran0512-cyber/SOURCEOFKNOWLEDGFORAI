---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-neon-glowing-conic-border-product-card/"
title: "Tailwind Neon Glowing Conic-Border Product Card"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "A dark card wrapped in a conic-gradient border that ignites and spins on hover, with a blurred copy of itself throwing the glow."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Glowing Conic-Border Product Card
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-neon-glowing-conic-border-product-card/

A dark card wrapped in a conic-gradient border that ignites and spins on hover, with a blurred copy of itself throwing the glow. The rotation needs a registered @property --angle and a @keyframes — both stylesheet rules — but the animation itself becomes a real utility, because --animate-tpc09-spin in @theme mints animate-tpc09-spin.
## HTML
```html
<section class="tpc-09 w-full min-h-svh grid place-items-center font-tpc09-sans px-5 py-14 bg-[radial-gradient(120%_120%_at_50%_20%,oklch(0.16_0.02_300),oklch(0.09_0.01_300))]" aria-label="Neon glowing border product card demo">
  <article class="group relative isolate w-80 max-w-full p-0.5 rounded-[20px]">
    <span aria-hidden="true" class="absolute inset-0 -z-10 rounded-[20px] opacity-50 bg-[conic-gradient(from_var(--angle),var(--color-tpc09-c1),var(--color-tpc09-c2),var(--color-tpc09-c3),var(--color-tpc09-c1))] animate-tpc09-spin [animation-play-state:paused] transition-opacity duration-400 group-hover:opacity-100 group-hover:[animation-play-state:running] motion-reduce:animate-none"></span>
    <span aria-hidden="true" class="absolute inset-0 -z-10 rounded-[20px] opacity-25 blur-[18px] bg-[conic-gradient(from_var(--angle),var(--color-tpc09-c1),var(--color-tpc09-c2),var(--color-tpc09-c3),var(--color-tpc09-c1))] animate-tpc09-spin [animation-play-state:paused] transition-opacity duration-400 group-hover:opacity-70 group-hover:[animation-play-state:running] motion-reduce:animate-none"></span>
    <div class="rounded-[18px] overflow-hidden bg-tpc09-face">
      <div role="img" aria-label="Product photo: Flux automatic watch" class="aspect-[16/11] bg-linear-[135deg,var(--color-tpc09-ph),var(--color-tpc09-ph2)] bg-[url('https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&h=550&fit=crop&q=70')] bg-cover bg-center"></div>
      <div class="px-5.5 pt-5 pb-5.5">
        <p class="font-tpc09-mono text-[11px] tracking-[0.2em] uppercase text-tpc09-c2">Flux</p>
        <h3 class="mt-1.5 text-[18px] font-semibold text-tpc09-ink text-pretty">Flux Automatic Watch</h3>
        <div class="mt-4.5 flex items-center justify-between gap-3">
          <p class="text-[22px] font-extrabold text-tpc09-hi tabular-nums">$460</p>
          <button type="button" class="min-h-11 h-11 px-5.5 rounded-xl border-0 bg-linear-[120deg,var(--color-tpc09-c1),var(--color-tpc09-c2)] text-tpc09-onacc text-sm font-bold cursor-pointer transition-[filter,scale] duration-200 hover:brightness-110 active:scale-97 focus-visible:outline-3 focus-visible:outline-tpc09-c1 focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
        </div>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc09-face: #0b0a11;
  --color-tpc09-face: oklch(0.13 0.012 300);
  --color-tpc09-ph: #171522;
  --color-tpc09-ph: oklch(0.19 0.018 300);
  --color-tpc09-ph2: #0f0e18;
  --color-tpc09-ph2: oklch(0.15 0.015 300);
  --color-tpc09-ink: #f1eefb;
  --color-tpc09-ink: oklch(0.95 0.01 300);
  --color-tpc09-hi: #ffffff;
  --color-tpc09-hi: oklch(1 0 0);
  --color-tpc09-onacc: #0a0713;
  --color-tpc09-onacc: oklch(0.13 0.02 300);
  --color-tpc09-c1: #6fd8ee;
  --color-tpc09-c1: oklch(0.82 0.16 200);
  --color-tpc09-c2: #e055b0;
  --color-tpc09-c2: oklch(0.72 0.24 330);
  --color-tpc09-c3: #f2c94c;
  --color-tpc09-c3: oklch(0.85 0.18 90);
  --font-tpc09-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpc09-mono: 'JetBrains Mono', ui-monospace, monospace;
  /* An @theme --animate-* entry mints a real utility: animate-tpc09-spin. */
  --animate-tpc09-spin: tpc-09-spin 6s linear infinite;
}
/* The registered angle: unregistered, --angle is a string and will not
   interpolate, so the border would jump rather than sweep. */

@property --angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@keyframes tpc-09-spin {
  to {
    --angle: 360deg;
  }
}

.tpc-09 {
  width: 100%;
  min-height: 100svh;
}

.tpc-09 ::selection {
  background: var(--color-tpc09-c2);
  color: #fff;
}
```
