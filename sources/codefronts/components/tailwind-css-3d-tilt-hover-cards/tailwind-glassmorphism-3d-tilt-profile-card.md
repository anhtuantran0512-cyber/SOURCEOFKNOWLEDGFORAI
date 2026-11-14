---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-glassmorphism-3d-tilt-profile-card/"
title: "Tailwind Glassmorphism 3D Tilt Profile Card"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "A frosted-glass team card for agency About pages: real backdrop-blur-[20px] over an oklch aurora, a gradient hairline drawn with the padding-box/border-box…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism 3D Tilt Profile Card
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-glassmorphism-3d-tilt-profile-card/

A frosted-glass team card for agency About pages: real backdrop-blur-[20px] over an oklch aurora, a gradient hairline drawn with the padding-box/border-box trick, a spinning conic avatar ring animated through @property, and three depth planes that separate as the card tilts ±10°. Tailwind writes the -webkit-backdrop-filter prefix for you.
## HTML
```html
<section class="ttc-02 w-full min-h-svh grid place-items-center bg-ttc02-bg bg-[radial-gradient(70%_90%_at_20%_15%,var(--color-ttc02-lobe1),transparent_55%),radial-gradient(80%_90%_at_85%_90%,var(--color-ttc02-lobe2),transparent_55%)] px-6 py-14 font-ttc02-sans text-white" aria-label="Glassmorphism 3D tilt profile card demo">
  <div class="grid w-full justify-items-center gap-8">
    <article data-ttc02-card class="group/card relative w-full max-w-[20rem] rounded-[26px] border border-transparent px-7 pt-9 pb-7 text-center [background:linear-gradient(oklch(1_0_0/0.08),oklch(1_0_0/0.04))_padding-box,linear-gradient(150deg,oklch(1_0_0/0.45),oklch(1_0_0/0.06)_40%,oklch(1_0_0/0.28))_border-box] backdrop-blur-[20px] shadow-[0_30px_70px_-30px_oklch(0_0_0/0.7)] transform-3d [transform:perspective(1100px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-transform duration-600 ease-[cubic-bezier(0.2,0.9,0.3,1.1)] data-live:duration-80 data-live:ease-linear motion-reduce:transition-none">
      <div class="mx-auto size-24 rounded-full p-[3px] bg-[conic-gradient(from_var(--ttc02-ang),var(--color-ttc02-a),var(--color-ttc02-b),var(--color-ttc02-a))] animate-ttc02-spin translate-z-[45px] motion-reduce:animate-none">
        <img class="size-full rounded-full border-3 border-ttc02-bg object-cover" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=200&auto=format&fit=crop" alt="" width="96" height="96" loading="lazy">
      </div>
      <h3 class="mt-5 text-[22px] font-bold tracking-[-0.02em] translate-z-[28px]">Maya Chen</h3>
      <p class="mt-1 text-xs font-semibold tracking-[0.16em] uppercase text-ttc02-role translate-z-[28px]">Design Director</p>
      <p class="mt-4 text-[14px] leading-[1.6] text-ttc02-mut text-pretty translate-z-[18px]">Leads brand systems and motion for product teams across three time zones.</p>
      <p class="mt-4 inline-flex items-center gap-2 rounded-full bg-white/8 px-3 py-1.5 text-xs font-medium text-ttc02-mut translate-z-[22px]"><span aria-hidden="true" class="size-2 rounded-full bg-ttc02-ok shadow-[0_0_0_3px_oklch(0.78_0.16_155/0.25)]"></span>Open to new projects</p>
      <nav aria-label="Maya Chen's links" class="mt-5 flex justify-center gap-2.5 translate-z-[55px]">
        <a href="#" class="inline-flex min-h-11 items-center rounded-full border border-white/20 bg-white/10 px-5 text-[13px] font-semibold text-white no-underline transition-colors hover:bg-white/22 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Portfolio</a>
        <a href="#" class="inline-flex min-h-11 items-center rounded-full border border-white/20 bg-white/10 px-5 text-[13px] font-semibold text-white no-underline transition-colors hover:bg-white/22 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">LinkedIn</a>
      </nav>
      <div aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-[inherit] bg-[radial-gradient(300px_circle_at_var(--mx,50%)_var(--my,50%),oklch(1_0_0/0.16),transparent_60%)] opacity-0 transition-opacity duration-400 group-data-live/card:opacity-100"></div>
    </article>
    <p aria-hidden="true" class="rounded-full border border-white/15 bg-white/5 px-3.5 py-2 font-ttc02-mono text-[11.5px] text-ttc02-mut">backdrop-blur-[20px] · padding-box/border-box · @property ring</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc02-bg: #110f1b;
  --color-ttc02-bg: oklch(0.16 0.02 280);
  --color-ttc02-lobe1: #5b2f78cc;
  --color-ttc02-lobe1: oklch(0.4 0.13 310 / 0.8);
  --color-ttc02-lobe2: #17617acc;
  --color-ttc02-lobe2: oklch(0.45 0.12 210 / 0.8);
  --color-ttc02-a: #2fc0d9;
  --color-ttc02-a: oklch(0.74 0.13 210);
  --color-ttc02-b: #b46be0;
  --color-ttc02-b: oklch(0.66 0.18 310);
  --color-ttc02-role: #a6e6f2;
  --color-ttc02-role: oklch(0.88 0.07 210);
  --color-ttc02-mut: #d6d3e2;
  --color-ttc02-mut: oklch(0.87 0.02 285);
  --color-ttc02-ok: #4fd08b;
  --color-ttc02-ok: oklch(0.78 0.16 155);
  --font-ttc02-sans: 'Manrope', system-ui, sans-serif;
  --font-ttc02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttc02-spin: ttc02-spin 7s linear infinite;

  @keyframes ttc02-spin {
    to {
      --ttc02-ang: 360deg;
    }
  }
}
/* The ring angle must be a typed property to animate inside conic-gradient() — an at-rule, so it stays CSS. */

@property --ttc02-ang {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-02 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc02-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 10; // glass reads best under 12 degrees
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
      card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
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
