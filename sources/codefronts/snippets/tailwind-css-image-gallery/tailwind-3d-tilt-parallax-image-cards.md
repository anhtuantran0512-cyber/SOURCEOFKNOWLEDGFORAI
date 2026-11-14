---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-3d-tilt-parallax-image-cards/"
title: "Tailwind 3D Tilt Parallax Image Cards with Pointer-Driven Variables"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "Photo cards that tilt in 3D toward the cursor with a moving specular glare and a caption floating above the image."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt Parallax Image Cards with Pointer-Driven Variables
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-3d-tilt-parallax-image-cards/

Photo cards that tilt in 3D toward the cursor with a moving specular glare and a caption floating above the image. JavaScript writes four numbers; every visual consequence is a Tailwind utility reading them — the cleanest possible division between behaviour and appearance.
## HTML
```html
<section class="tgl-16 w-full min-h-svh grid place-items-center px-5 py-10 font-tgl16-sans [perspective:1000px] bg-[radial-gradient(120%_120%_at_50%_15%,oklch(0.2_0.04_290),oklch(0.09_0.02_280))]" id="tgl-16" aria-label="3D tilt parallax cards">
  <div class="flex flex-wrap justify-center gap-7 w-[min(940px,100%)]">
    <article data-tilt tabindex="0" class="group relative w-[260px] rounded-[20px] overflow-hidden cursor-pointer bg-tgl16-well [--rx:0deg] [--ry:0deg] [--mx:50%] [--my:50%] [transform:rotateX(var(--rx))_rotateY(var(--ry))] transform-3d transition-[transform,box-shadow] duration-[400ms] shadow-[0_30px_60px_-30px_rgba(0,0,0,0.8)] after:content-[''] after:absolute after:inset-0 after:z-[3] after:pointer-events-none after:opacity-0 after:transition-opacity after:duration-300 after:mix-blend-screen after:bg-[radial-gradient(300px_300px_at_var(--mx)_var(--my),rgba(255,255,255,0.28),transparent_60%)] hover:after:opacity-100 focus-visible:outline-3 focus-visible:outline-tgl16-acc focus-visible:outline-offset-[3px] motion-reduce:[transform:none] motion-reduce:transition-none motion-reduce:after:hidden">
      <div class="overflow-hidden"><img src="https://images.unsplash.com/photo-1516031190212-da133013de50?q=80&w=500&h=620&auto=format&fit=crop" alt="Aurora over mountains" loading="lazy" decoding="async" class="block w-full [aspect-ratio:5/6] object-cover"></div>
      <figcaption class="absolute inset-x-0 bottom-0 z-[2] px-5 py-5 [transform:translateZ(50px)] bg-[linear-gradient(0deg,rgba(8,6,15,0.9),transparent)] motion-reduce:[transform:none]">
        <span class="font-tgl16-mono text-[11px] tracking-[0.2em] uppercase text-tgl16-acc">Iceland</span>
        <h3 class="mt-1 text-[19px] font-bold text-white">Northern Skies</h3>
      </figcaption>
    </article>
    <article data-tilt tabindex="0" class="group relative w-[260px] rounded-[20px] overflow-hidden cursor-pointer bg-tgl16-well [--rx:0deg] [--ry:0deg] [--mx:50%] [--my:50%] [transform:rotateX(var(--rx))_rotateY(var(--ry))] transform-3d transition-[transform,box-shadow] duration-[400ms] shadow-[0_30px_60px_-30px_rgba(0,0,0,0.8)] after:content-[''] after:absolute after:inset-0 after:z-[3] after:pointer-events-none after:opacity-0 after:transition-opacity after:duration-300 after:mix-blend-screen after:bg-[radial-gradient(300px_300px_at_var(--mx)_var(--my),rgba(255,255,255,0.28),transparent_60%)] hover:after:opacity-100 focus-visible:outline-3 focus-visible:outline-tgl16-acc focus-visible:outline-offset-[3px] motion-reduce:[transform:none] motion-reduce:transition-none motion-reduce:after:hidden">
      <div class="overflow-hidden"><img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=500&h=620&auto=format&fit=crop" alt="Canyon at sunset" loading="lazy" decoding="async" class="block w-full [aspect-ratio:5/6] object-cover"></div>
      <figcaption class="absolute inset-x-0 bottom-0 z-[2] px-5 py-5 [transform:translateZ(50px)] bg-[linear-gradient(0deg,rgba(8,6,15,0.9),transparent)] motion-reduce:[transform:none]">
        <span class="font-tgl16-mono text-[11px] tracking-[0.2em] uppercase text-tgl16-acc">Utah</span>
        <h3 class="mt-1 text-[19px] font-bold text-white">Red Horizon</h3>
      </figcaption>
    </article>
    <article data-tilt tabindex="0" class="group relative w-[260px] rounded-[20px] overflow-hidden cursor-pointer bg-tgl16-well [--rx:0deg] [--ry:0deg] [--mx:50%] [--my:50%] [transform:rotateX(var(--rx))_rotateY(var(--ry))] transform-3d transition-[transform,box-shadow] duration-[400ms] shadow-[0_30px_60px_-30px_rgba(0,0,0,0.8)] after:content-[''] after:absolute after:inset-0 after:z-[3] after:pointer-events-none after:opacity-0 after:transition-opacity after:duration-300 after:mix-blend-screen after:bg-[radial-gradient(300px_300px_at_var(--mx)_var(--my),rgba(255,255,255,0.28),transparent_60%)] hover:after:opacity-100 focus-visible:outline-3 focus-visible:outline-tgl16-acc focus-visible:outline-offset-[3px] motion-reduce:[transform:none] motion-reduce:transition-none motion-reduce:after:hidden">
      <div class="overflow-hidden"><img src="https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?q=80&w=500&h=620&auto=format&fit=crop" alt="Foggy forest at dawn" loading="lazy" decoding="async" class="block w-full [aspect-ratio:5/6] object-cover"></div>
      <figcaption class="absolute inset-x-0 bottom-0 z-[2] px-5 py-5 [transform:translateZ(50px)] bg-[linear-gradient(0deg,rgba(8,6,15,0.9),transparent)] motion-reduce:[transform:none]">
        <span class="font-tgl16-mono text-[11px] tracking-[0.2em] uppercase text-tgl16-acc">Oregon</span>
        <h3 class="mt-1 text-[19px] font-bold text-white">Deep Green</h3>
      </figcaption>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* @property registration has no utility form — typed variables are what make the
   settle-back on pointer-leave interpolate instead of snapping. */

@property --rx {
  syntax: '<angle>';
  inherits: true;
  initial-value: 0deg;
}

@property --ry {
  syntax: '<angle>';
  inherits: true;
  initial-value: 0deg;
}

@theme {
  --color-tgl16-well: #12101d;
  --color-tgl16-well: oklch(0.19 0.02 285);
  --color-tgl16-acc: #b9a7f7;
  --color-tgl16-acc: oklch(0.78 0.13 290);
  --font-tgl16-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tgl16-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.tgl-16 {
  width: 100%;
  min-height: 100svh;
}

.tgl-16 ::selection {
  background: var(--color-tgl16-acc);
  color: #0a0616;
}
```

## JavaScript
```js
(function () {
  var root = document.getElementById('tgl-16');
  if (!root) return;
  if (matchMedia('(hover:none)').matches || matchMedia('(prefers-reduced-motion:reduce)').matches) return;

  var MAX = 12; // max tilt in degrees

  root.querySelectorAll('[data-tilt]').forEach(function (card) {
    card.addEventListener('pointermove', function (e) {
      var r = card.getBoundingClientRect();
      var px = (e.clientX - r.left) / r.width;
      var py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--ry', ((px - 0.5) * 2 * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--rx', ((0.5 - py) * 2 * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
      card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
    });
    card.addEventListener('pointerleave', function () {
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
