---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-add-to-cart-modal-liquid-morph-metaball/"
title: "Tailwind Add to Cart Confirmation with SVG Liquid Morph Entrance"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "An e-commerce confirmation that blobs into existence: an SVG goo filter plus a 0.6&rarr;1 spring, with the filter dropped the instant the card settles so…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Add to Cart Confirmation with SVG Liquid Morph Entrance
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-add-to-cart-modal-liquid-morph-metaball/

An e-commerce confirmation that blobs into existence: an SVG goo filter plus a 0.6&rarr;1 spring, with the filter dropped the instant the card settles so text renders crisp. The port carries the filter as [filter:url(#tw-10-goo)] and switches it off with open:[filter:none], keeping the whole effect in the class list.
## HTML
```html
<section class="tw-10 w-full min-h-svh grid place-items-center bg-tw10-bg font-tw10-sans px-6 py-10">
  <svg width="0" height="0" class="absolute" aria-hidden="true">
    <defs>
      <filter id="tw-10-goo">
        <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur"/>
        <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="goo"/>
        <feComposite in="SourceGraphic" in2="goo" operator="atop"/>
      </filter>
    </defs>
  </svg>

  <button type="button" data-tw10-open class="inline-flex items-center justify-center min-h-11 px-7 rounded-[9px] border-0 bg-tw10-brand text-[15px] font-bold text-white shadow-[0_10px_22px_-6px_var(--color-tw10-glow)] cursor-pointer transition-[background-color,translate] duration-200 hover:bg-tw10-branddark hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tw10-brand focus-visible:outline-offset-2 motion-reduce:hover:translate-y-0">Add to cart · $89</button>

  <dialog id="tw-10-dlg" aria-labelledby="tw-10-title" class="m-auto w-[min(460px,94vw)] p-0 border-0 rounded-2xl text-left text-tw10-ink bg-tw10-card shadow-[0_40px_60px_-20px_#1e293b59] opacity-0 scale-[0.6] [filter:url(#tw-10-goo)] transition-[opacity,scale,filter,overlay,display] duration-500 ease-[cubic-bezier(.34,1.56,.64,1)] [transition-delay:0ms,0ms,500ms] transition-discrete open:opacity-100 open:scale-100 open:[filter:none] open:starting:opacity-0 open:starting:scale-[0.6] open:backdrop:bg-tw10-scrim open:backdrop:backdrop-blur-[6px] motion-reduce:transition-[opacity] motion-reduce:duration-150 motion-reduce:scale-100 motion-reduce:[filter:none]">
    <div class="relative px-7 pt-7 pb-6">
      <button type="button" data-tw10-close aria-label="Close dialog" class="absolute top-3.5 right-3.5 grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tw10-sub text-[15px] cursor-pointer transition-colors duration-200 hover:bg-tw10-well2 hover:text-tw10-ink focus-visible:outline-2 focus-visible:outline-tw10-brand focus-visible:outline-offset-2">&#10005;</button>

      <p class="inline-flex items-center gap-2 mb-3 py-1 pl-1.5 pr-3 rounded-full bg-tw10-goodtint text-xs font-bold uppercase tracking-wide text-tw10-good">
        <span aria-hidden="true" class="grid place-items-center size-5 rounded-full bg-tw10-good text-[11px] text-white">&#10003;</span>Added to cart
      </p>
      <h2 id="tw-10-title" class="mb-[18px] text-[1.35rem] font-extrabold tracking-[-0.015em] leading-tight">You're all set</h2>

      <div class="flex items-center gap-3.5 mb-3.5 p-3.5 rounded-xl border border-tw10-line bg-tw10-well">
        <span aria-hidden="true" data-tw10-thumb class="shrink-0 grid place-items-center size-18 rounded-[9px] text-[32px]">&#128095;</span>
        <div class="flex-1 min-w-0">
          <p class="mb-0.5 text-sm font-bold">Terra Runner · Slate / Coral</p>
          <p class="mb-0.5 text-xs text-tw10-sub">Size 10 · Qty 1</p>
          <p class="text-[15px] font-extrabold text-tw10-brand tabular-nums">$89.00</p>
        </div>
      </div>

      <div class="mb-4 px-4 py-3.5 rounded-[9px] border border-tw10-line">
        <div class="flex justify-between items-center text-sm"><span>Cart subtotal (2 items)</span><strong class="font-extrabold tabular-nums">$168.00</strong></div>
        <div class="flex justify-between items-center mt-2 pt-2 border-t border-tw10-line text-sm font-semibold text-tw10-good"><span>Free shipping unlocked</span><span aria-hidden="true">&#127881;</span></div>
      </div>

      <p aria-live="polite" class="sr-only">Terra Runner added to cart. Cart subtotal is $168.00 for 2 items.</p>

      <div class="grid grid-cols-2 gap-2.5">
        <button type="button" data-tw10-close class="min-h-11 rounded-[9px] border-0 bg-tw10-well2 text-sm font-bold text-tw10-ink cursor-pointer transition-[background-color,translate] duration-150 hover:bg-tw10-well3 active:translate-y-px focus-visible:outline-2 focus-visible:outline-tw10-ink focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Continue shopping</button>
        <button type="button" autofocus data-tw10-close class="min-h-11 rounded-[9px] border-0 bg-tw10-brand text-sm font-bold text-white cursor-pointer transition-[background-color,translate] duration-150 hover:bg-tw10-branddark active:translate-y-px focus-visible:outline-2 focus-visible:outline-tw10-brand focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">View cart &rarr;</button>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tw10-bg: #fdf7f4;
  --color-tw10-bg: oklch(0.97 0.012 40);
  --color-tw10-card: #ffffff;
  --color-tw10-card: oklch(1 0 0);
  --color-tw10-well: #fafbfc;
  --color-tw10-well: oklch(0.98 0.003 255);
  --color-tw10-well2: #f1f5f9;
  --color-tw10-well2: oklch(0.96 0.006 250);
  --color-tw10-well3: #e2e8f0;
  --color-tw10-well3: oklch(0.92 0.01 250);
  --color-tw10-ink: #1e293b;
  --color-tw10-ink: oklch(0.3 0.03 258);
  --color-tw10-sub: #55657c;
  --color-tw10-sub: oklch(0.5 0.03 255);
  --color-tw10-line: #eef1f5;
  --color-tw10-line: oklch(0.95 0.005 255);
  --color-tw10-brand: #e05252;
  --color-tw10-brand: oklch(0.62 0.17 22);
  --color-tw10-branddark: #c23e3e;
  --color-tw10-branddark: oklch(0.55 0.17 22);
  --color-tw10-glow: #ff6b6b80;
  --color-tw10-glow: oklch(0.7 0.17 22 / 0.5);
  --color-tw10-good: #047857;
  --color-tw10-good: oklch(0.52 0.12 164);
  --color-tw10-goodtint: #0596691f;
  --color-tw10-goodtint: oklch(0.63 0.14 163 / 0.12);
  --color-tw10-scrim: #1e293b80;
  --color-tw10-scrim: oklch(0.3 0.03 258 / 0.5);
  --font-tw10-sans: 'Outfit', system-ui, sans-serif;
}

.tw-10 {
  width: 100%;
}
/* Placeholder product swatch — swap for a real <img>. */

.tw-10 [data-tw10-thumb] {
  background-image: linear-gradient(135deg, oklch(0.93 0.04 350), oklch(0.95 0.06 90));
}

#tw-10-dlg::backdrop {
  background: oklch(0.3 0.03 258 / 0);
  backdrop-filter: blur(0px);
  transition: background .25s ease, backdrop-filter .25s ease, overlay .25s allow-discrete, display .25s allow-discrete;
}

@starting-style {
  #tw-10-dlg[open]::backdrop {
    background: oklch(0.3 0.03 258 / 0);
    backdrop-filter: blur(0px);
  }
}

@media (prefers-reduced-motion: reduce) {
  #tw-10-dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tw-10');
  var dlg = root.querySelector('#tw-10-dlg');
  var card = dlg.firstElementChild;
  root.querySelector('[data-tw10-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelectorAll('[data-tw10-close]').forEach(function (b) {
    b.addEventListener('click', function () { dlg.close(); });
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
