---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-quick-view-modal-morphing-button-elastic/"
title: "Tailwind Product Quick View Modal with Elastic Button Morph"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A browse-mode product preview that expands from a button-sized pill into a full card — scale, translate and border-radius animating together on an elastic…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Product Quick View Modal with Elastic Button Morph
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-quick-view-modal-morphing-button-elastic/

A browse-mode product preview that expands from a button-sized pill into a full card — scale, translate and border-radius animating together on an elastic curve. The port states all three on the dialog as open:starting: values, so the morph's start shape lives beside its end shape.
## HTML
```html
<section class="tw-11 w-full min-h-svh grid place-items-center bg-tw11-bg font-tw11-sans px-6 py-10">
  <button type="button" data-tw11-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-lg border border-tw11-ink bg-transparent text-[15px] font-semibold text-tw11-ink cursor-pointer transition-colors duration-200 hover:bg-tw11-ink hover:text-tw11-card focus-visible:outline-2 focus-visible:outline-tw11-ink focus-visible:outline-offset-2">Quick view</button>

  <dialog id="tw-11-dlg" aria-labelledby="tw-11-title" class="m-auto w-[min(720px,94vw)] p-0 border-0 overflow-hidden text-left text-tw11-ink bg-tw11-card shadow-[0_40px_60px_-20px_#1e293b59] will-change-transform opacity-0 scale-[0.08] translate-y-[200px] rounded-full transition-[opacity,scale,translate,border-radius,overlay,display] duration-[650ms] ease-[cubic-bezier(.68,-0.55,.32,1.55)] transition-discrete open:opacity-100 open:scale-100 open:translate-y-0 open:rounded-2xl open:starting:opacity-0 open:starting:scale-[0.08] open:starting:translate-y-[200px] open:starting:rounded-full open:backdrop:bg-tw11-scrim open:backdrop:backdrop-blur-[4px] motion-reduce:transition-[opacity] motion-reduce:duration-200 motion-reduce:scale-100 motion-reduce:translate-y-0 motion-reduce:rounded-2xl">
    <button type="button" autofocus data-tw11-close aria-label="Close quick view" class="absolute top-3.5 right-3.5 z-10 grid place-items-center size-11 rounded-lg border-0 bg-tw11-glass backdrop-blur-[4px] text-[15px] text-tw11-sub cursor-pointer transition-colors duration-200 hover:bg-white hover:text-tw11-ink focus-visible:outline-2 focus-visible:outline-tw11-ink focus-visible:outline-offset-2">&#10005;</button>

    <div class="grid grid-cols-[1.1fr_1fr] max-[560px]:grid-cols-1">
      <div data-tw11-gallery class="p-6">
        <div data-tw11-hero class="grid place-items-center aspect-square rounded-xl text-[88px]" aria-hidden="true">&#128092;</div>
        <div role="radiogroup" aria-label="Colour" class="flex justify-center gap-2 mt-3.5">
          <button type="button" role="radio" aria-checked="true" aria-label="Slate" class="grid place-items-center size-11 rounded-full cursor-pointer bg-transparent border-0 focus-visible:outline-2 focus-visible:outline-tw11-ink focus-visible:outline-offset-2"><span class="block size-6 rounded-full bg-tw11-swslate ring-1 ring-tw11-line transition-[scale,box-shadow] duration-200 [button[aria-checked=true]_&amp;]:scale-110 [button[aria-checked=true]_&amp;]:ring-2 [button[aria-checked=true]_&amp;]:ring-tw11-ink"></span></button>
          <button type="button" role="radio" aria-checked="false" aria-label="Coral" class="grid place-items-center size-11 rounded-full cursor-pointer bg-transparent border-0 focus-visible:outline-2 focus-visible:outline-tw11-ink focus-visible:outline-offset-2"><span class="block size-6 rounded-full bg-tw11-swcoral ring-1 ring-tw11-line transition-[scale,box-shadow] duration-200 [button[aria-checked=true]_&amp;]:scale-110 [button[aria-checked=true]_&amp;]:ring-2 [button[aria-checked=true]_&amp;]:ring-tw11-ink"></span></button>
          <button type="button" role="radio" aria-checked="false" aria-label="Olive" class="grid place-items-center size-11 rounded-full cursor-pointer bg-transparent border-0 focus-visible:outline-2 focus-visible:outline-tw11-ink focus-visible:outline-offset-2"><span class="block size-6 rounded-full bg-tw11-swolive ring-1 ring-tw11-line transition-[scale,box-shadow] duration-200 [button[aria-checked=true]_&amp;]:scale-110 [button[aria-checked=true]_&amp;]:ring-2 [button[aria-checked=true]_&amp;]:ring-tw11-ink"></span></button>
          <button type="button" role="radio" aria-checked="false" aria-label="Mustard" class="grid place-items-center size-11 rounded-full cursor-pointer bg-transparent border-0 focus-visible:outline-2 focus-visible:outline-tw11-ink focus-visible:outline-offset-2"><span class="block size-6 rounded-full bg-tw11-swmustard ring-1 ring-tw11-line transition-[scale,box-shadow] duration-200 [button[aria-checked=true]_&amp;]:scale-110 [button[aria-checked=true]_&amp;]:ring-2 [button[aria-checked=true]_&amp;]:ring-tw11-ink"></span></button>
        </div>
      </div>

      <div class="flex flex-col px-[26px] pt-7 pb-6">
        <p class="mb-1.5 text-xs font-bold uppercase tracking-[0.08em] text-tw11-sub">Terra Studio</p>
        <h2 id="tw-11-title" class="mb-2.5 font-tw11-display text-2xl font-extrabold tracking-[-0.015em] leading-tight">Everyday Crossbody</h2>
        <p class="flex items-baseline gap-2.5 mb-3">
          <span class="text-[1.35rem] font-extrabold text-tw11-brand tabular-nums">$128</span>
          <span class="text-sm text-tw11-sub line-through tabular-nums">$168</span>
        </p>
        <p class="mb-4 text-sm leading-relaxed text-tw11-sub text-pretty">Vegetable-tanned leather · Recycled brass hardware · Fits a 13-inch laptop.</p>

        <div role="radiogroup" aria-label="Size" class="flex gap-2 mb-4">
          <button type="button" role="radio" aria-checked="false" class="min-w-11 min-h-11 px-3.5 rounded-lg border border-tw11-line bg-white text-sm font-bold text-tw11-ink cursor-pointer transition-colors duration-200 hover:border-tw11-ink aria-[checked=true]:bg-tw11-ink aria-[checked=true]:text-tw11-card aria-[checked=true]:border-tw11-ink focus-visible:outline-2 focus-visible:outline-tw11-ink focus-visible:outline-offset-2">S</button>
          <button type="button" role="radio" aria-checked="true" class="min-w-11 min-h-11 px-3.5 rounded-lg border border-tw11-line bg-white text-sm font-bold text-tw11-ink cursor-pointer transition-colors duration-200 hover:border-tw11-ink aria-[checked=true]:bg-tw11-ink aria-[checked=true]:text-tw11-card aria-[checked=true]:border-tw11-ink focus-visible:outline-2 focus-visible:outline-tw11-ink focus-visible:outline-offset-2">M</button>
          <button type="button" role="radio" aria-checked="false" class="min-w-11 min-h-11 px-3.5 rounded-lg border border-tw11-line bg-white text-sm font-bold text-tw11-ink cursor-pointer transition-colors duration-200 hover:border-tw11-ink aria-[checked=true]:bg-tw11-ink aria-[checked=true]:text-tw11-card aria-[checked=true]:border-tw11-ink focus-visible:outline-2 focus-visible:outline-tw11-ink focus-visible:outline-offset-2">L</button>
        </div>

        <button type="button" data-tw11-close class="mt-auto min-h-11 px-5 rounded-[9px] border-0 bg-tw11-brand text-[15px] font-bold text-white tabular-nums shadow-[0_8px_18px_-6px_var(--color-tw11-glow)] cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw11-branddark hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw11-brand focus-visible:outline-offset-[3px] motion-reduce:hover:translate-y-0">Add to cart · $128</button>
        <a href="#" class="mt-2.5 text-center text-[13px] text-tw11-sub no-underline hover:text-tw11-ink hover:underline">View full details &rarr;</a>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw11-bg: #fdf7f4;
  --color-tw11-bg: oklch(0.97 0.012 40);
  --color-tw11-card: #fafaf7;
  --color-tw11-card: oklch(0.98 0.004 95);
  --color-tw11-ink: #1e293b;
  --color-tw11-ink: oklch(0.3 0.03 258);
  --color-tw11-sub: #55657c;
  --color-tw11-sub: oklch(0.5 0.03 255);
  --color-tw11-line: #e5e0d5;
  --color-tw11-line: oklch(0.9 0.015 85);
  --color-tw11-brand: #e05252;
  --color-tw11-brand: oklch(0.62 0.17 22);
  --color-tw11-branddark: #c23e3e;
  --color-tw11-branddark: oklch(0.55 0.17 22);
  --color-tw11-glow: #ff6b6b80;
  --color-tw11-glow: oklch(0.7 0.17 22 / 0.5);
  --color-tw11-glass: #ffffffb3;
  --color-tw11-glass: oklch(1 0 0 / 0.7);
  --color-tw11-swslate: #1e293b;
  --color-tw11-swslate: oklch(0.3 0.03 258);
  --color-tw11-swcoral: #ff6b6b;
  --color-tw11-swcoral: oklch(0.7 0.17 22);
  --color-tw11-swolive: #84cc16;
  --color-tw11-swolive: oklch(0.77 0.19 128);
  --color-tw11-swmustard: #eab308;
  --color-tw11-swmustard: oklch(0.79 0.16 86);
  --color-tw11-scrim: #1e293b80;
  --color-tw11-scrim: oklch(0.3 0.03 258 / 0.5);
  --font-tw11-sans: 'Outfit', system-ui, sans-serif;
  --font-tw11-display: 'Playfair Display', Georgia, serif;
}

.tw-11 {
  width: 100%;
}
/* Placeholder gallery surfaces — swap for real product photography. */

.tw-11 [data-tw11-gallery] {
  background-image: linear-gradient(180deg, oklch(0.95 0.03 85), oklch(0.92 0.04 80));
}

.tw-11 [data-tw11-hero] {
  background-image: linear-gradient(135deg, oklch(0.93 0.04 350), oklch(0.88 0.06 280));
}

#tw-11-dlg::backdrop {
  background: oklch(0.3 0.03 258 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s ease, backdrop-filter .3s ease, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tw-11-dlg[open]::backdrop {
    background: oklch(0.3 0.03 258 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-11-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-11');
  var dlg = root.querySelector('#tw-11-dlg');
  root.querySelector('[data-tw11-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelectorAll('[data-tw11-close]').forEach(function (b) {
    b.addEventListener('click', function () { dlg.close(); });
  });
  // Radio groups: one checked per group, state written to ARIA so styling follows semantics.
  root.querySelectorAll('[role=radiogroup]').forEach(function (group) {
    group.addEventListener('click', function (e) {
      var btn = e.target.closest('[role=radio]');
      if (!btn) return;
      group.querySelectorAll('[role=radio]').forEach(function (r) { r.setAttribute('aria-checked', String(r === btn)); });
    });
  });
  dlg.addEventListener('click', function (e) {
    var r = dlg.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
