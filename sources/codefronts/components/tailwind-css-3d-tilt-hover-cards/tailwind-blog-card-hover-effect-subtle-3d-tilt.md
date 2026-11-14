---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-blog-card-hover-effect-subtle-3d-tilt/"
title: "Tailwind Blog Card Hover Effect with Subtle 3D Tilt"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "An editorial card that respects reading: tilt capped at ±4.5° so the headline never smears, a cover that eases to scale-104, and an author row that slides…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Blog Card Hover Effect with Subtle 3D Tilt
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-blog-card-hover-effect-subtle-3d-tilt/

An editorial card that respects reading: tilt capped at ±4.5° so the headline never smears, a cover that eases to scale-104, and an author row that slides open with the grid-rows-[0fr] → grid-rows-[1fr] trick. The port fixes the original's biggest miss: the reveal now also opens on keyboard focus (group-focus-visible/link:) and is always open on touch.
## HTML
```html
<section class="ttc-08 w-full min-h-svh grid place-items-center bg-ttc08-bg bg-linear-to-b from-ttc08-bg to-ttc08-bg2 px-6 py-14 font-ttc08-serif text-ttc08-ink" aria-label="Blog article card with subtle 3D tilt demo">
  <div class="grid w-full justify-items-center gap-8">
    <a href="#" class="group/link block w-full max-w-[21rem] rounded-[20px] no-underline text-inherit focus-visible:outline-3 focus-visible:outline-offset-5 focus-visible:outline-ttc08-acc">
      <article data-ttc08-card class="group/card overflow-hidden rounded-[18px] border border-ttc08-line bg-ttc08-card shadow-[0_16px_40px_-28px_var(--color-ttc08-shadow)] [transform:perspective(1300px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-[transform,box-shadow] duration-550 ease-[cubic-bezier(0.2,0.9,0.3,1.05)] data-live:duration-90 data-live:ease-linear data-live:shadow-[0_26px_54px_-26px_var(--color-ttc08-shadow)] motion-reduce:transition-none">
        <div aria-hidden="true" class="aspect-video overflow-hidden bg-ttc08-cover">
          <img class="size-full object-cover transition-[scale] duration-550 ease-[cubic-bezier(0.2,0.9,0.3,1.05)] group-data-live/card:scale-104 motion-reduce:transition-none" src="https://picsum.photos/seed/tokens-grammar/640/360" alt="" loading="lazy">
        </div>
        <div class="px-6 pt-5 pb-5">
          <p class="font-ttc08-sans text-[11px] font-bold tracking-[0.14em] uppercase text-ttc08-acc">Design Systems</p>
          <h3 class="mt-2 text-[22px] leading-[1.22] font-medium tracking-[-0.01em] text-pretty">Why Your Tokens Need a Grammar, Not a Dictionary</h3>
          <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-300 ease-out group-data-live/card:grid-rows-[1fr] group-focus-visible/link:grid-rows-[1fr] pointer-coarse:grid-rows-[1fr] motion-reduce:grid-rows-[1fr] motion-reduce:transition-none">
            <div class="min-h-0 overflow-hidden">
              <div class="flex items-center gap-2.5 pt-4 font-ttc08-sans text-[12.5px] text-ttc08-mut">
                <img class="size-7 rounded-full object-cover" src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=96&auto=format&fit=crop" alt="" width="28" height="28" loading="lazy">
                <span class="font-semibold text-ttc08-ink">Priya Sharma</span><span aria-hidden="true">·</span><span>7 min read</span>
              </div>
            </div>
          </div>
        </div>
      </article>
    </a>
    <p aria-hidden="true" class="rounded-full border border-ttc08-line bg-white/60 px-3.5 py-2 font-ttc08-mono text-[11.5px] text-ttc08-mut">grid-rows-[0fr] → [1fr] · group-focus-visible/link: · pointer-coarse:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc08-bg: #f8f5ef;
  --color-ttc08-bg: oklch(0.97 0.008 85);
  --color-ttc08-bg2: #efe9df;
  --color-ttc08-bg2: oklch(0.935 0.014 75);
  --color-ttc08-card: #fdfcf9;
  --color-ttc08-card: oklch(0.99 0.004 85);
  --color-ttc08-cover: #b98e62;
  --color-ttc08-cover: oklch(0.67 0.08 60);
  --color-ttc08-line: #e3dccf;
  --color-ttc08-line: oklch(0.89 0.015 80);
  --color-ttc08-ink: #2c241c;
  --color-ttc08-ink: oklch(0.26 0.02 60);
  --color-ttc08-mut: #6a5e52;
  --color-ttc08-mut: oklch(0.48 0.025 60);
  --color-ttc08-acc: #a8562c;
  --color-ttc08-acc: oklch(0.53 0.13 48);
  --color-ttc08-shadow: #6b543899;
  --color-ttc08-shadow: oklch(0.42 0.05 70 / 0.6);
  --font-ttc08-serif: 'Newsreader', Georgia, serif;
  --font-ttc08-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttc08-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-08 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc08-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 4.5; // legibility cap: headlines shimmer past ~5 degrees
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
      card.setAttribute('data-live', ''); // also opens the 0fr -> 1fr author row
    });
    card.addEventListener('pointerleave', () => {
      card.removeAttribute('data-live');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
