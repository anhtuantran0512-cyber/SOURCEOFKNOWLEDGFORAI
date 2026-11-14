---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-3d-tilt-parallax-card-hover-effect/"
title: "Tailwind 3D Tilt & Parallax Card with Depth Layers"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A featured-work card that rotates toward the cursor in real 3D while background, badge, title and copy ride separate Z planes and drift at different rates."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt & Parallax Card with Depth Layers
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-3d-tilt-parallax-card-hover-effect/

A featured-work card that rotates toward the cursor in real 3D while background, badge, title and copy ride separate Z planes and drift at different rates. The port's interesting cost: perspective, transform-style and translateZ have no utilities and stay arbitrary properties &mdash; but the whole child-layer contract collapses into one *: variant on the card.
## HTML
```html
<section class="tch-01 w-full min-h-svh grid place-items-center bg-tch01-bg bg-[radial-gradient(circle_at_30%_20%,var(--color-tch01-glow),var(--color-tch01-bg)_65%)] font-tch01-sans p-8 [perspective:1300px]">
  <article data-tch01="root" tabindex="0" class="group relative w-[340px] h-[460px] rounded-[26px] bg-tch01-card border border-white/10 shadow-[0_30px_60px_rgb(0_0_0/0.5)] cursor-pointer [transform-style:preserve-3d] transition-transform duration-150 ease-out outline-none focus-visible:outline-3 focus-visible:outline-tch01-acc focus-visible:outline-offset-4 *:absolute *:transition-transform *:duration-150 *:ease-out *:will-change-transform motion-reduce:transition-none motion-reduce:*:transition-none">
    <div data-depth="10" class="inset-0 rounded-[26px] overflow-hidden bg-[radial-gradient(circle_at_30%_25%,#ff7a59_0_18%,transparent_19%),radial-gradient(circle_at_75%_70%,#5b8cff_0_24%,transparent_25%),linear-gradient(160deg,#2a2f63,#11132c)] after:content-[''] after:absolute after:inset-0 after:bg-[radial-gradient(circle_at_50%_40%,transparent,rgb(9_10_24/0.6))]"></div>
    <span data-depth="34" class="top-8 left-8 z-5 text-[0.7rem] tracking-[0.22em] uppercase text-tch01-tag">Featured Work</span>
    <div data-depth="46" class="top-8 right-8 z-5 grid place-items-center size-[46px] rounded-[14px] bg-white/12 border border-white/25 text-white font-bold backdrop-blur-[4px]">◈</div>
    <h2 data-depth="60" class="left-8 bottom-[5.4rem] z-5 font-tch01-display font-black text-[3rem] leading-[0.9] text-white">Aether<br>Studio</h2>
    <p data-depth="40" class="left-8 right-8 bottom-8 z-5 text-[0.85rem] leading-[1.55] text-tch01-body">An award-winning interactive site. Background, type, and badge each ride their own depth plane.</p>
    <div data-tch01="glare" class="inset-0 z-6 rounded-[26px] pointer-events-none opacity-0 transition-opacity duration-300 group-hover:opacity-100 bg-[radial-gradient(circle_at_var(--tch01-gx,50%)_var(--tch01-gy,50%),rgb(255_255_255/0.22),transparent_45%)]"></div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch01-bg: #090a18;
  --color-tch01-bg: oklch(0.13 0.03 275);
  --color-tch01-glow: #1f2347;
  --color-tch01-glow: oklch(0.26 0.06 275);
  --color-tch01-card: #0e1024;
  --color-tch01-card: oklch(0.16 0.04 275);
  --color-tch01-tag: #ffd6c4;
  --color-tch01-tag: oklch(0.89 0.05 45);
  --color-tch01-body: #c4c8e6;
  --color-tch01-body: oklch(0.82 0.04 280);
  --color-tch01-acc: #ff7a59;
  --color-tch01-acc: oklch(0.72 0.17 40);
  --font-tch01-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tch01-display: 'Fraunces', Georgia, serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build compiles. */

.tch-01 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tch-01');
  if (!root) return;
  const card = root.querySelector('[data-tch01="root"]');
  if (!card) return;
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const layers = card.querySelectorAll('[data-depth]');
  let frame = 0;
  card.addEventListener('mousemove', (e) => {
    if (frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width;
      const py = (e.clientY - r.top) / r.height;
      card.style.transform = 'rotateY(' + ((px - 0.5) * 18) + 'deg) rotateX(' + ((0.5 - py) * 18) + 'deg)';
      layers.forEach((l) => {
        const d = parseFloat(l.dataset.depth);
        l.style.transform = 'translateZ(' + (d) + 'px) translate(' + ((0.5 - px) * d * 0.6) + 'px, ' + ((0.5 - py) * d * 0.6) + 'px)';
      });
      card.style.setProperty('--tch01-gx', '' + (px * 100) + '%');
      card.style.setProperty('--tch01-gy', '' + (py * 100) + '%');
    });
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'rotateY(0deg) rotateX(0deg)';
    layers.forEach((l) => {
      l.style.transform = 'translateZ(' + (parseFloat(l.dataset.depth)) + 'px)';
    });
  });
})();
```
