---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-tilt-3d-perspective-hover/"
title: "Tailwind Image Tilt 3D Perspective Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "The pointer-tracked tilt, with the split the port makes possible: JavaScript writes four numbers into custom properties, and every piece of geometry stays in…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Tilt 3D Perspective Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-tilt-3d-perspective-hover/

The pointer-tracked tilt, with the split the port makes possible: JavaScript writes four numbers into custom properties, and every piece of geometry stays in the markup. [transform:perspective(800px)_rotateX(var(--rx))_rotateY(var(--ry))_scale3d(var(--s),var(--s),var(--s))] is one utility reading live values &mdash; the script never touches a class or a style string.
## HTML
```html
<section class="tih-12 w-full min-h-svh grid place-items-center bg-tih12-bg font-tih12-sans px-6 py-10 [perspective:1200px]" aria-label="3D tilt perspective hover demo">
  <div class="grid w-full max-w-195 gap-5 grid-cols-1 sm:grid-cols-3">
    <article style="--rx:0deg; --ry:0deg; --s:1; --mx:50%; --my:50%" class="group rounded-2xl overflow-hidden transform-3d will-change-transform [transform:perspective(800px)_rotateX(var(--rx))_rotateY(var(--ry))_scale3d(var(--s),var(--s),var(--s))] transition-[transform,box-shadow] duration-500 ease-tih12 data-tilting:transition-none hover:shadow-[0_30px_80px_oklch(0_0_0/0.6)] motion-reduce:[transform:none] motion-reduce:transition-none">
      <div class="relative aspect-[3/4] grid place-items-center overflow-hidden bg-[image:url('https://picsum.photos/seed/tih12-mystic/600/800'),linear-gradient(135deg,oklch(0.17_0.07_285),oklch(0.28_0.13_290),oklch(0.55_0.24_295))] bg-cover bg-center bg-no-repeat">
        <div class="absolute inset-0 pointer-events-none opacity-0 transition-opacity duration-300 group-hover:opacity-100 bg-radial-[circle_at_var(--mx)_var(--my),oklch(1_0_0/0.12),transparent_60%] motion-reduce:hidden"></div>
      </div>
      <div class="p-3.5 bg-[oklch(1_0_0/0.03)] backdrop-blur-[2px]">
        <h3 class="text-[13px] font-bold text-tih12-text"><a href="#mystic" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih12-acc focus-visible:outline-offset-3">Mystic Artifacts</a></h3>
        <p class="mt-0.75 text-[11px] text-tih12-muted">Interactive 3D collection</p>
      </div>
    </article>
    <article style="--rx:0deg; --ry:0deg; --s:1; --mx:50%; --my:50%" class="group rounded-2xl overflow-hidden transform-3d will-change-transform [transform:perspective(800px)_rotateX(var(--rx))_rotateY(var(--ry))_scale3d(var(--s),var(--s),var(--s))] transition-[transform,box-shadow] duration-500 ease-tih12 data-tilting:transition-none hover:shadow-[0_30px_80px_oklch(0_0_0/0.6)] motion-reduce:[transform:none] motion-reduce:transition-none">
      <div class="relative aspect-[3/4] grid place-items-center overflow-hidden bg-[image:url('https://picsum.photos/seed/tih12-botanical/600/800'),linear-gradient(135deg,oklch(0.2_0.05_165),oklch(0.35_0.09_163),oklch(0.7_0.15_163))] bg-cover bg-center bg-no-repeat">
        <div class="absolute inset-0 pointer-events-none opacity-0 transition-opacity duration-300 group-hover:opacity-100 bg-radial-[circle_at_var(--mx)_var(--my),oklch(1_0_0/0.12),transparent_60%] motion-reduce:hidden"></div>
      </div>
      <div class="p-3.5 bg-[oklch(1_0_0/0.03)] backdrop-blur-[2px]">
        <h3 class="text-[13px] font-bold text-tih12-text"><a href="#botanical" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih12-acc focus-visible:outline-offset-3">Botanical Studies</a></h3>
        <p class="mt-0.75 text-[11px] text-tih12-muted">Flora &amp; fauna series</p>
      </div>
    </article>
    <article style="--rx:0deg; --ry:0deg; --s:1; --mx:50%; --my:50%" class="group rounded-2xl overflow-hidden transform-3d will-change-transform [transform:perspective(800px)_rotateX(var(--rx))_rotateY(var(--ry))_scale3d(var(--s),var(--s),var(--s))] transition-[transform,box-shadow] duration-500 ease-tih12 data-tilting:transition-none hover:shadow-[0_30px_80px_oklch(0_0_0/0.6)] motion-reduce:[transform:none] motion-reduce:transition-none">
      <div class="relative aspect-[3/4] grid place-items-center overflow-hidden bg-[image:url('https://picsum.photos/seed/tih12-ocean/600/800'),linear-gradient(135deg,oklch(0.18_0.08_265),oklch(0.33_0.14_262),oklch(0.62_0.19_260))] bg-cover bg-center bg-no-repeat">
        <div class="absolute inset-0 pointer-events-none opacity-0 transition-opacity duration-300 group-hover:opacity-100 bg-radial-[circle_at_var(--mx)_var(--my),oklch(1_0_0/0.12),transparent_60%] motion-reduce:hidden"></div>
      </div>
      <div class="p-3.5 bg-[oklch(1_0_0/0.03)] backdrop-blur-[2px]">
        <h3 class="text-[13px] font-bold text-tih12-text"><a href="#ocean" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih12-acc focus-visible:outline-offset-3">Ocean Depths</a></h3>
        <p class="mt-0.75 text-[11px] text-tih12-muted">Underwater photography</p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih12-bg: #060a12;
  --color-tih12-bg: oklch(0.11 0.015 265);
  --color-tih12-text: #f1f5f9;
  --color-tih12-text: oklch(0.96 0.005 250);
  --color-tih12-muted: #64748b;
  --color-tih12-muted: oklch(0.58 0.035 255);
  --color-tih12-acc: #38bdf8;
  --color-tih12-acc: oklch(0.75 0.13 230);
  --font-tih12-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih12: cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-12 {
  width: 100%;
  min-height: 100svh;
}

.tih-12 ::selection {
  background: oklch(0.75 0.13 230);
  color: #000;
}
```

## JavaScript
```js
(function () {
  var INTENSITY = 18;
  document.querySelectorAll('.tih-12 article').forEach(function (card) {
    if (card.dataset.bound) return; card.dataset.bound = '1';
    var pending = null, frame = 0;
    function apply() {
      frame = 0;
      if (!pending) return;
      var r = card.getBoundingClientRect(),
          x = (pending.clientX - r.left) / r.width,
          y = (pending.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((y - 0.5) * -INTENSITY).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((x - 0.5) * INTENSITY).toFixed(2) + 'deg');
      card.style.setProperty('--s', '1.02');
      card.style.setProperty('--mx', (x * 100).toFixed(1) + '%');
      card.style.setProperty('--my', (y * 100).toFixed(1) + '%');
    }
    card.addEventListener('pointermove', function (e) {
      card.setAttribute('data-tilting', '');
      pending = e;
      if (!frame) frame = requestAnimationFrame(apply);
    });
    card.addEventListener('pointerleave', function () {
      card.removeAttribute('data-tilting');
      pending = null;
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
      card.style.setProperty('--s', '1');
    });
  });
})();
```
