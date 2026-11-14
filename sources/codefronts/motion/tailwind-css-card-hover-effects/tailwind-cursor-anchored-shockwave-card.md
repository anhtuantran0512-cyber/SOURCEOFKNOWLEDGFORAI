---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-cursor-anchored-shockwave-card/"
title: "Tailwind Cursor-Anchored Shockwave Ripple Card"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "Two concentric rings fire outward from the exact point the cursor enters the card, the second trailing the first by 120ms."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cursor-Anchored Shockwave Ripple Card
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-cursor-anchored-shockwave-card/

Two concentric rings fire outward from the exact point the cursor enters the card, the second trailing the first by 120ms. The anchoring is the whole trick: a pointerenter handler writes the entry point into two custom properties, and the rings' origin reads them.
## HTML
```html
<section class="tch-29 w-full min-h-svh grid place-items-center bg-tch29-bg font-tch29-sans p-8">
  <article data-tch29="root" class="group relative w-[340px] h-[440px] rounded-[18px] overflow-hidden cursor-pointer bg-[radial-gradient(circle_at_50%_40%,#0e2236,#060d16)] border border-tch29-ring-a/20
    before:content-[''] before:absolute before:z-1 before:size-2.5 before:rounded-full before:pointer-events-none before:top-[var(--tch29-y,50%)] before:left-[var(--tch29-x,50%)] before:-translate-x-1/2 before:-translate-y-1/2 before:scale-0 before:border-2 before:border-tch29-ring-a/70 before:shadow-[0_0_30px_var(--color-tch29-ring-a)] group-hover:before:animate-tch29-ring-a motion-reduce:group-hover:before:animate-none
    after:content-[''] after:absolute after:z-1 after:size-2.5 after:rounded-full after:pointer-events-none after:top-[var(--tch29-y,50%)] after:left-[var(--tch29-x,50%)] after:-translate-x-1/2 after:-translate-y-1/2 after:scale-0 after:border after:border-tch29-ring-b/60 group-hover:after:animate-tch29-ring-b motion-reduce:group-hover:after:animate-none">
    <div class="relative z-2 h-full p-[2.4rem] flex flex-col justify-between text-tch29-ink">
      <span class="font-tch29-display text-[0.72rem] tracking-[0.24em] uppercase text-tch29-ring-a">// Energy Core</span>
      <h2 class="font-tch29-display font-bold text-[2.6rem] leading-[0.95]">Pulse<br>Reactor</h2>
      <p class="text-[0.86rem] leading-[1.6] text-tch29-body">Every interaction sends a wave outward. Hover anywhere — the ripple starts where you enter.</p>
      <a href="#" class="self-start inline-flex items-center min-h-11 px-6 rounded-lg font-tch29-display text-[0.85rem] tracking-[0.06em] no-underline bg-tch29-ring-a/12 border border-tch29-ring-a/40 text-tch29-ring-a transition-colors duration-200 hover:bg-tch29-ring-a/22 focus-visible:outline-2 focus-visible:outline-tch29-ring-a focus-visible:outline-offset-2">Discharge ⚡</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@keyframes tch29-ring {
  0% {
    transform: translate(-50%,-50%) scale(0);
    opacity: 0.9;
  }

  100% {
    transform: translate(-50%,-50%) scale(60);
    opacity: 0;
  }
}

@theme {
  --color-tch29-bg: #07101a;
  --color-tch29-bg: oklch(0.15 0.02 245);
  --color-tch29-ink: #dceaf7;
  --color-tch29-ink: oklch(0.92 0.02 240);
  --color-tch29-body: #8fa6bb;
  --color-tch29-body: oklch(0.7 0.03 240);
  --color-tch29-ring-a: #50c8ff;
  --color-tch29-ring-a: oklch(0.79 0.13 235);
  --color-tch29-ring-b: #a05aff;
  --color-tch29-ring-b: oklch(0.6 0.23 295);
  --font-tch29-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tch29-display: 'Chakra Petch', system-ui, sans-serif;
  --animate-tch29-ring-a: tch29-ring 0.9s cubic-bezier(0.2,0.6,0.3,1) forwards;
  --animate-tch29-ring-b: tch29-ring 1.1s cubic-bezier(0.2,0.6,0.3,1) 0.12s forwards;
}

.tch-29 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tch-29');
  if (!root) return;
  const card = root.querySelector('[data-tch29="root"]');
  if (!card) return;
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  card.addEventListener('pointerenter', (e) => {
    const r = card.getBoundingClientRect();
    card.style.setProperty('--tch29-x', '' + (e.clientX - r.left) + 'px');
    card.style.setProperty('--tch29-y', '' + (e.clientY - r.top) + 'px');
  });
})();
```
