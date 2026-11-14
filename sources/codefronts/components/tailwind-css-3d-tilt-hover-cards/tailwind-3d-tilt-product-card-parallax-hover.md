---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-tilt-product-card-parallax-hover/"
title: "Tailwind 3D Tilt Product Card with Parallax Hover Effect"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "The D2C product spotlight in utilities: the sneaker floats at translate-z-[50px], the Add-to-Cart button rides higher at translate-z-[60px], and a radial…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt Product Card with Parallax Hover Effect
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-tilt-product-card-parallax-hover/

The D2C product spotlight in utilities: the sneaker floats at translate-z-[50px], the Add-to-Cart button rides higher at translate-z-[60px], and a radial glare chases the cursor. The whole depth stack is declared on the elements that own it, and the port adds a working colourway picker — three real radios that re-hue the product with has-[[value=volt]:checked]:[--hue:110deg], no extra JS.
## HTML
```html
<section class="ttc-01 w-full min-h-svh grid place-items-center bg-ttc01-bg bg-[radial-gradient(80%_90%_at_15%_10%,var(--color-ttc01-lobe1),transparent_60%),radial-gradient(70%_80%_at_90%_95%,var(--color-ttc01-lobe2),transparent_60%)] px-6 py-14 font-ttc01-sans text-ttc01-ink" aria-label="3D tilt product card demo">
  <div class="grid w-full justify-items-center gap-8">
    <article data-ttc01-card class="group/card relative w-full max-w-[19.5rem] rounded-[24px] border border-white/10 bg-linear-160 from-ttc01-card1 to-ttc01-card2 px-6 pt-6 pb-6 shadow-[0_30px_60px_-30px_oklch(0_0_0/0.8)] transform-3d [transform:perspective(1100px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-transform duration-600 ease-[cubic-bezier(0.2,0.9,0.3,1.15)] data-live:duration-80 data-live:ease-linear motion-reduce:transition-none has-[[value=volt]:checked]:[--hue:110deg] has-[[value=tide]:checked]:[--hue:190deg]">
      <div class="flex items-center justify-between translate-z-[35px]">
        <span class="rounded-full border border-ttc01-acc/50 px-2.5 py-1.5 text-[10px] leading-none font-bold tracking-[0.14em] text-ttc01-acc">NEW DROP</span>
        <span class="text-xs font-medium text-ttc01-mut">Free returns</span>
      </div>
      <div class="relative mx-auto mt-5 mb-4 aspect-[4/3] w-[94%] -rotate-6 translate-z-[50px] transition-[translate,rotate] duration-600 ease-[cubic-bezier(0.2,0.9,0.3,1.15)] group-data-live/card:-rotate-9 group-data-live/card:translate-z-[64px] motion-reduce:transition-none">
        <div aria-hidden="true" class="absolute inset-[10%] rounded-full bg-ttc01-acc/40 blur-2xl"></div>
        <img class="relative size-full rounded-2xl object-cover [filter:hue-rotate(var(--hue,0deg))_drop-shadow(0_24px_22px_oklch(0_0_0/0.55))] transition-[filter] duration-500" src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=640&auto=format&fit=crop" alt="Aurora Runner sneaker, side view" width="320" height="240" loading="lazy">
      </div>
      <h3 class="text-[22px] leading-tight font-bold tracking-[-0.02em] translate-z-[25px]">Aurora Runner</h3>
      <div class="mt-1 flex items-center justify-between gap-3 translate-z-[25px]">
        <p class="text-sm text-ttc01-mut">Limited colourway · <strong class="font-semibold text-ttc01-ink tabular-nums">$189</strong></p>
        <fieldset class="flex items-center">
          <legend class="sr-only">Colourway</legend>
          <label class="grid size-11 cursor-pointer place-items-center"><input type="radio" name="ttc01-colour" value="ember" checked aria-label="Ember" class="size-5 cursor-pointer appearance-none rounded-full bg-ttc01-ember ring-2 ring-transparent ring-offset-2 ring-offset-ttc01-card2 transition checked:ring-ttc01-ink focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ttc01-acc"></label>
          <label class="grid size-11 cursor-pointer place-items-center"><input type="radio" name="ttc01-colour" value="volt" aria-label="Volt" class="size-5 cursor-pointer appearance-none rounded-full bg-ttc01-volt ring-2 ring-transparent ring-offset-2 ring-offset-ttc01-card2 transition checked:ring-ttc01-ink focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ttc01-acc"></label>
          <label class="grid size-11 cursor-pointer place-items-center"><input type="radio" name="ttc01-colour" value="tide" aria-label="Tide" class="size-5 cursor-pointer appearance-none rounded-full bg-ttc01-tide ring-2 ring-transparent ring-offset-2 ring-offset-ttc01-card2 transition checked:ring-ttc01-ink focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ttc01-acc"></label>
        </fieldset>
      </div>
      <button type="button" class="mt-4 h-12 w-full cursor-pointer rounded-xl bg-linear-120 from-ttc01-acc to-ttc01-acc2 text-sm font-semibold text-ttc01-bg shadow-[0_14px_26px_-12px_var(--color-ttc01-acc2)] translate-z-[60px] transition-[filter] hover:brightness-110 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-ttc01-ink">Add to Cart</button>
      <div aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-[inherit] bg-[radial-gradient(260px_circle_at_var(--mx,50%)_var(--my,50%),oklch(1_0_0/0.2),transparent_65%)] opacity-0 translate-z-[70px] transition-opacity duration-400 group-data-live/card:opacity-100"></div>
    </article>
    <p aria-hidden="true" class="rounded-full border border-white/10 bg-white/5 px-3.5 py-2 font-ttc01-mono text-[11.5px] text-ttc01-mut">transform-3d · translate-z-[60px] · has-[:checked]:[--hue]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc01-bg: #0f0d18;
  --color-ttc01-bg: oklch(0.15 0.02 280);
  --color-ttc01-lobe1: #2e2244e6;
  --color-ttc01-lobe1: oklch(0.28 0.06 290 / 0.9);
  --color-ttc01-lobe2: #3a1d14cc;
  --color-ttc01-lobe2: oklch(0.25 0.07 40 / 0.8);
  --color-ttc01-card1: #25212f;
  --color-ttc01-card1: oklch(0.24 0.03 285);
  --color-ttc01-card2: #1a1722;
  --color-ttc01-card2: oklch(0.18 0.025 280);
  --color-ttc01-ink: #eef0f7;
  --color-ttc01-ink: oklch(0.95 0.01 260);
  --color-ttc01-mut: #b3b1c0;
  --color-ttc01-mut: oklch(0.76 0.02 270);
  --color-ttc01-acc: #f58d57;
  --color-ttc01-acc: oklch(0.74 0.15 45);
  --color-ttc01-acc2: #ea5d3d;
  --color-ttc01-acc2: oklch(0.66 0.18 32);
  --color-ttc01-ember: #e2403a;
  --color-ttc01-ember: oklch(0.62 0.2 27);
  --color-ttc01-volt: #9bc53d;
  --color-ttc01-volt: oklch(0.76 0.17 125);
  --color-ttc01-tide: #2fa6c9;
  --color-ttc01-tide: oklch(0.67 0.12 225);
  --font-ttc01-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-ttc01-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-01 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc01-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    // Touch + motion guards: everyone else gets the fully styled static card.
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 14; // degrees of tilt at the card's edge
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
      card.removeAttribute('data-live'); // re-arms the slow spring transition
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
