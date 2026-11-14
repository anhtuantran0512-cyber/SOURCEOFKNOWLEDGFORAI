---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-pop-out-character-card-cursor-tracking-eyes/"
title: "Tailwind 3D Pop-Out Character Card with Cursor-Tracking Eyes"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "The scroll-stopping agency trick: a mascot whose head rises OUTSIDE the card, floating at translate-z-[45px] and lifting to 70px on hover while the card…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Pop-Out Character Card with Cursor-Tracking Eyes
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-pop-out-character-card-cursor-tracking-eyes/

The scroll-stopping agency trick: a mascot whose head rises OUTSIDE the card, floating at translate-z-[45px] and lifting to 70px on hover while the card tilts beneath it. The port gives the character a personality upgrade — pupils that follow the cursor and an idle blink — using the same custom-property bridge that drives the tilt.
## HTML
```html
<section class="ttc-05 w-full min-h-svh grid place-items-center bg-ttc05-bg bg-[radial-gradient(80%_90%_at_80%_10%,var(--color-ttc05-lobe1),transparent_60%),radial-gradient(70%_80%_at_10%_90%,var(--color-ttc05-lobe2),transparent_60%)] px-6 pt-28 pb-14 font-ttc05-sans text-white" aria-label="3D pop-out character card demo">
  <div class="grid w-full justify-items-center gap-8">
    <article data-ttc05-card class="group/card relative h-64 w-full max-w-[18rem] overflow-visible rounded-[24px] transform-3d [transform:perspective(1000px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-transform duration-600 ease-[cubic-bezier(0.2,0.9,0.3,1.15)] data-live:duration-80 data-live:ease-linear motion-reduce:transition-none" aria-label="Blobby, studio mascot">
      <div aria-hidden="true" class="absolute inset-0 overflow-hidden rounded-[24px] border border-white/12 bg-linear-170 from-ttc05-face1 to-ttc05-face2 shadow-[0_30px_60px_-26px_oklch(0_0_0/0.8)] after:absolute after:inset-0 after:bg-[radial-gradient(120%_60%_at_50%_0%,var(--color-ttc05-shine),transparent_60%)] after:content-['']"></div>
      <div aria-hidden="true" class="absolute -top-[76px] left-1/2 h-[170px] w-[150px] -translate-x-1/2 translate-z-[45px] bg-[radial-gradient(60%_55%_at_50%_32%,var(--color-ttc05-skin2)_0_58%,transparent_59%),radial-gradient(75%_48%_at_50%_78%,var(--color-ttc05-skin)_0_60%,transparent_61%)] drop-shadow-[0_22px_18px_oklch(0_0_0/0.5)] transition-[translate,scale] duration-600 ease-[cubic-bezier(0.2,0.9,0.3,1.3)] group-data-live/card:translate-z-[70px] group-data-live/card:scale-106 motion-reduce:transition-none">
        <span class="absolute top-[40px] left-[48px] grid h-6 w-[18px] origin-center place-items-center rounded-full bg-white animate-ttc05-blink motion-reduce:animate-none"><span class="size-2.5 rounded-full bg-ttc05-ink [translate:var(--ex,0px)_var(--ey,0px)] transition-[translate] duration-150"></span></span>
        <span class="absolute top-[40px] right-[48px] grid h-6 w-[18px] origin-center place-items-center rounded-full bg-white animate-ttc05-blink motion-reduce:animate-none"><span class="size-2.5 rounded-full bg-ttc05-ink [translate:var(--ex,0px)_var(--ey,0px)] transition-[translate] duration-150"></span></span>
        <span class="absolute top-[74px] left-1/2 h-2.5 w-7 -translate-x-1/2 rounded-b-full bg-ttc05-ink"></span>
      </div>
      <div class="absolute inset-x-5 bottom-5 translate-z-[30px]">
        <h3 class="text-[26px] leading-none font-bold">Blobby</h3>
        <p class="mt-1.5 text-[13px] text-ttc05-mut">Chief Vibe Officer · est. 2019</p>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full border border-white/12 bg-white/5 px-3.5 py-2 font-ttc05-mono text-[11.5px] text-ttc05-mut">overflow-visible · translate-z-[70px] · [translate:var(--ex)]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc05-bg: #0c1618;
  --color-ttc05-bg: oklch(0.16 0.02 200);
  --color-ttc05-lobe1: #1f4a26b3;
  --color-ttc05-lobe1: oklch(0.3 0.09 145 / 0.7);
  --color-ttc05-lobe2: #1c2f4ab3;
  --color-ttc05-lobe2: oklch(0.28 0.07 250 / 0.7);
  --color-ttc05-face1: #1e3a26;
  --color-ttc05-face1: oklch(0.28 0.06 150);
  --color-ttc05-face2: #13232a;
  --color-ttc05-face2: oklch(0.2 0.04 200);
  --color-ttc05-shine: #3d7a4a59;
  --color-ttc05-shine: oklch(0.5 0.12 150 / 0.35);
  --color-ttc05-skin: #4cc062;
  --color-ttc05-skin: oklch(0.72 0.19 145);
  --color-ttc05-skin2: #6fd682;
  --color-ttc05-skin2: oklch(0.8 0.17 145);
  --color-ttc05-ink: #0f1c1f;
  --color-ttc05-ink: oklch(0.2 0.02 200);
  --color-ttc05-mut: #c1d0cc;
  --color-ttc05-mut: oklch(0.84 0.02 180);
  --font-ttc05-sans: 'Fredoka', system-ui, sans-serif;
  --font-ttc05-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttc05-blink: ttc05-blink 5s ease-in-out infinite;

  @keyframes ttc05-blink {
    0%,
        95%,
        100% {
      scale: 1 1;
    }

    97.5% {
      scale: 1 0.1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-05 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc05-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 13, EYE = 3.5; // EYE: pupil travel in px
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ex', ((px - 0.5) * 2 * EYE).toFixed(2) + 'px');
      card.style.setProperty('--ey', ((py - 0.5) * 2 * EYE).toFixed(2) + 'px');
      card.setAttribute('data-live', ''); // lifts the mascot to translate-z-[70px]
    });
    card.addEventListener('pointerleave', () => {
      card.removeAttribute('data-live');
      ['--rx', '--ry'].forEach((p) => card.style.setProperty(p, '0deg'));
      ['--ex', '--ey'].forEach((p) => card.style.setProperty(p, '0px'));
    });
  });
})();
```
