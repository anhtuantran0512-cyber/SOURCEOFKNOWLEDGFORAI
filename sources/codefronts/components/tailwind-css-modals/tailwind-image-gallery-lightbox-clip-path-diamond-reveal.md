---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-image-gallery-lightbox-clip-path-diamond-reveal/"
title: "Tailwind Image Gallery Lightbox with Clip-Path Diamond Reveal"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A portfolio lightbox that opens through a diamond aperture — four polygon vertices expanding from the centre past the frame's corners."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Gallery Lightbox with Clip-Path Diamond Reveal
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-image-gallery-lightbox-clip-path-diamond-reveal/

A portfolio lightbox that opens through a diamond aperture — four polygon vertices expanding from the centre past the frame's corners. The port states both polygons as arbitrary properties on the stage, adds real arrow-key navigation the original only described, and keeps the counter and caption legible on near-black.
## HTML
```html
<section class="tw-09 w-full min-h-svh grid place-items-center bg-tw09-bg font-tw09-sans px-6 py-10">
  <button type="button" data-tw09-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-lg border border-tw09-brand bg-transparent text-[15px] font-semibold text-tw09-brand cursor-pointer transition-colors duration-200 hover:bg-tw09-brand hover:text-tw09-bg focus-visible:outline-2 focus-visible:outline-tw09-brand focus-visible:outline-offset-2">Open gallery · 12 photos</button>

  <dialog id="tw-09-dlg" aria-labelledby="tw-09-title" class="group w-full max-w-none h-full max-h-none m-0 p-8 border-0 bg-transparent open:grid open:place-items-center open:backdrop:bg-tw09-scrim open:backdrop:backdrop-blur-[10px]">
    <button type="button" data-tw09-close aria-label="Close gallery" class="fixed top-5 right-6 grid place-items-center size-11 rounded-full border border-tw09-edge bg-tw09-glass text-base text-tw09-ink cursor-pointer transition-[background-color,rotate] duration-200 hover:bg-tw09-glass2 hover:rotate-90 focus-visible:outline-2 focus-visible:outline-tw09-brand focus-visible:outline-offset-2 motion-reduce:hover:rotate-0">&#10005;</button>
    <button type="button" data-tw09-prev aria-label="Previous image" class="fixed left-2 sm:left-6 top-1/2 -translate-y-1/2 grid place-items-center size-11 rounded-full border border-tw09-edge bg-tw09-glass text-base text-tw09-ink cursor-pointer transition-colors duration-200 hover:bg-tw09-glass2 focus-visible:outline-2 focus-visible:outline-tw09-brand focus-visible:outline-offset-2">&#9668;</button>
    <button type="button" autofocus data-tw09-next aria-label="Next image" class="fixed right-2 sm:right-6 top-1/2 -translate-y-1/2 grid place-items-center size-11 rounded-full border border-tw09-edge bg-tw09-glass text-base text-tw09-ink cursor-pointer transition-colors duration-200 hover:bg-tw09-glass2 focus-visible:outline-2 focus-visible:outline-tw09-brand focus-visible:outline-offset-2">&#9658;</button>

    <div class="w-[min(820px,100%,calc((100svh-200px)*1.6))] opacity-0 [clip-path:polygon(50%_50%,50%_50%,50%_50%,50%_50%)] transition-[opacity,clip-path] duration-[600ms] ease-[cubic-bezier(.65,0,.35,1)] group-open:opacity-100 group-open:[clip-path:polygon(50%_-50%,150%_50%,50%_150%,-50%_50%)] motion-reduce:transition-opacity motion-reduce:[clip-path:none]">
      <h2 id="tw-09-title" class="mb-3.5 text-center text-xs font-bold uppercase tracking-[0.14em] text-tw09-sub">Portfolio · 2026 selections</h2>

      <div data-tw09-frame class="relative aspect-[16/10] rounded-md overflow-hidden bg-tw09-frame">
        <span data-tw09-counter class="absolute top-3.5 right-3.5 px-3 py-1.5 rounded-full bg-tw09-chip backdrop-blur-[4px] font-tw09-mono text-xs font-bold tracking-wide text-tw09-ink" aria-live="polite">3 / 12</span>
      </div>

      <div class="mt-4 text-center">
        <p class="text-sm leading-relaxed text-tw09-sub"><strong data-tw09-caption class="block mb-0.5 font-semibold text-tw09-ink">Northlight fintech dashboard · Q3 2026</strong>Design system refresh · 200+ components migrated · 4× ship velocity</p>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw09-bg: #0a0a0f;
  --color-tw09-bg: oklch(0.14 0.01 285);
  --color-tw09-frame: #1b1b2e;
  --color-tw09-frame: oklch(0.24 0.03 285);
  --color-tw09-ink: #f5f5fa;
  --color-tw09-ink: oklch(0.97 0.005 285);
  --color-tw09-sub: #a9b3c6;
  --color-tw09-sub: oklch(0.77 0.02 260);
  --color-tw09-edge: #f5f5fa33;
  --color-tw09-edge: oklch(0.97 0.005 285 / 0.2);
  --color-tw09-glass: #ffffff0f;
  --color-tw09-glass: oklch(1 0 0 / 0.06);
  --color-tw09-glass2: #ffffff24;
  --color-tw09-glass2: oklch(1 0 0 / 0.14);
  --color-tw09-chip: #00000080;
  --color-tw09-chip: oklch(0 0 0 / 0.5);
  --color-tw09-brand: #a78bfa;
  --color-tw09-brand: oklch(0.73 0.16 296);
  --color-tw09-scrim: #000000f0;
  --color-tw09-scrim: oklch(0 0 0 / 0.94);
  --font-tw09-sans: 'Outfit', system-ui, sans-serif;
  --font-tw09-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tw-09 {
  width: 100%;
}
/* Placeholder artwork for the frame — swap for a real <img srcset>. */

#tw-09-dlg [data-tw09-frame] {
  background-image: linear-gradient(135deg, oklch(0.62 0.19 285), oklch(0.65 0.22 350), oklch(0.72 0.18 55));
}

#tw-09-dlg::backdrop {
  background: oklch(0 0 0 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s ease, backdrop-filter .3s ease, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tw-09-dlg[open]::backdrop {
    background: oklch(0 0 0 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-09-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-09');
  var dlg = root.querySelector('#tw-09-dlg');
  var counter = root.querySelector('[data-tw09-counter]');
  var caption = root.querySelector('[data-tw09-caption]');
  var SHOTS = [
    'Atlas travel booking · Q1 2026',
    'Harbor payments console · Q2 2026',
    'Northlight fintech dashboard · Q3 2026',
    'Fieldnote research tool · Q3 2026'
  ];
  var i = 2;

  function paint() {
    counter.textContent = (i + 1) + ' / ' + SHOTS.length;
    caption.textContent = SHOTS[i];
  }
  function step(n) { i = (i + n + SHOTS.length) % SHOTS.length; paint(); }

  root.querySelector('[data-tw09-open]').addEventListener('click', function () { dlg.showModal(); paint(); });
  root.querySelector('[data-tw09-close]').addEventListener('click', function () { dlg.close(); });
  root.querySelector('[data-tw09-prev]').addEventListener('click', function () { step(-1); });
  root.querySelector('[data-tw09-next]').addEventListener('click', function () { step(1); });

  dlg.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { e.preventDefault(); step(-1); }
    else if (e.key === 'ArrowRight') { e.preventDefault(); step(1); }
  });
  // Full-bleed dialog: the edge controls are fixed and sit outside the stage's rect,
  // so light-dismiss tests the event target instead of coordinates.
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
})();
```
