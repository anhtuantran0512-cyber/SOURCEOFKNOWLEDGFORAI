---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-product-quick-view-modal-has-checked-chips/"
title: "Tailwind Product Quick-View Modal with has-checked Variant Chips"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A two-column quick view — gallery, rating, colour and size chips, quantity stepper, Add to bag — that a shopper can evaluate without leaving the grid."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Product Quick-View Modal with has-checked Variant Chips
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-product-quick-view-modal-has-checked-chips/

A two-column quick view — gallery, rating, colour and size chips, quantity stepper, Add to bag — that a shopper can evaluate without leaving the grid. Variant selection stays zero-JS: has-checked: on each label reads the radio inside it, so the chip styles itself.
## HTML
```html
<section class="tm-05 w-full min-h-svh grid place-items-center bg-tm05-bg font-tm05-sans px-6 py-10">
  <div class="flex flex-col items-center gap-2.5">
    <button type="button" data-tm05-open class="inline-flex items-center justify-center min-h-11 px-6 rounded-xl text-[15px] font-semibold text-tm05-ink bg-tm05-btn border border-tm05-btnedge cursor-pointer transition-colors duration-200 hover:bg-tm05-btnhover hover:border-tm05-acc focus-visible:outline-2 focus-visible:outline-tm05-acc focus-visible:outline-offset-2">Quick view</button>
    <span class="font-tm05-mono text-xs tracking-[0.14em] text-tm05-faint">(product-grid trigger)</span>
  </div>

  <dialog id="tm-05-dlg" aria-labelledby="tm-05-title" class="m-auto w-[min(720px,94vw)] max-h-[90dvh] overflow-auto p-0 border-0 rounded-[20px] text-tm05-ink bg-tm05-card shadow-[0_40px_90px_-30px_#000,0_0_0_1px_var(--color-tm05-edge)] opacity-0 scale-[0.97] transition-[opacity,translate,scale,overlay,display] duration-[280ms] transition-discrete open:opacity-100 open:scale-100 open:starting:opacity-0 open:starting:scale-[0.97] open:backdrop:bg-tm05-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <div data-tm05-card class="@container/card relative grid grid-cols-2 @max-md/card:grid-cols-1">
      <button type="button" data-tm05-close aria-label="Close" class="absolute top-3 right-3 z-[3] grid place-items-center size-9 rounded-lg border-0 bg-tm05-xbg text-tm05-ink text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-tm05-well hover:text-white focus-visible:outline-2 focus-visible:outline-tm05-acc focus-visible:outline-offset-2">&times;</button>

      <div class="p-4.5 bg-tm05-media">
        <div class="relative w-full h-full min-h-[280px] @max-md/card:min-h-[200px] rounded-[14px] border border-tm05-edge bg-[repeating-linear-gradient(135deg,var(--color-tm05-stripeA)_0_12px,var(--color-tm05-stripeB)_12px_24px)] after:content-['product_shot'] after:absolute after:inset-0 after:grid after:place-items-center after:font-tm05-mono after:text-xs after:tracking-[0.2em] after:uppercase after:text-tm05-faint"></div>
      </div>

      <div class="px-7 pt-7 pb-6">
        <p class="mb-2 text-[11px] tracking-[0.2em] text-tm05-acc">FIELD &amp; FORGE</p>
        <h2 id="tm-05-title" class="mb-2.5 text-2xl font-bold tracking-[-0.01em] text-tm05-hi">Merino Trail Overshirt</h2>
        <div class="mb-4 text-[12.5px] text-tm05-mut" aria-label="Rated 4.5 of 5"><span class="tracking-[1px] text-tm05-acc">★★★★</span><span class="tracking-[1px] text-tm05-acc opacity-50">★</span> <b class="text-tm05-ink">4.5</b> &middot; 218 reviews</div>
        <div class="mb-5 text-[26px] font-extrabold text-white">$148<small class="ml-1.5 text-xs font-medium text-tm05-mut">USD</small></div>

        <fieldset class="flex flex-wrap gap-2.5 mb-4 border-0 p-0">
          <legend class="basis-full mb-2.5 text-[11px] uppercase tracking-[0.16em] text-tm05-mut">Colour</legend>
          <label class="relative size-9 rounded-full cursor-pointer bg-[#3a4a3f] shadow-[inset_0_0_0_2px_var(--color-tm05-card),0_0_0_1px_var(--color-tm05-edge)] has-checked:shadow-[inset_0_0_0_2px_var(--color-tm05-card),0_0_0_2px_var(--color-tm05-acc)] has-focus-visible:outline-2 has-focus-visible:outline-tm05-acc has-focus-visible:outline-offset-[3px]"><input type="radio" name="tm-05-c" aria-label="Forest" checked class="absolute inset-0 opacity-0 cursor-pointer"></label>
          <label class="relative size-9 rounded-full cursor-pointer bg-[#5a3f2f] shadow-[inset_0_0_0_2px_var(--color-tm05-card),0_0_0_1px_var(--color-tm05-edge)] has-checked:shadow-[inset_0_0_0_2px_var(--color-tm05-card),0_0_0_2px_var(--color-tm05-acc)] has-focus-visible:outline-2 has-focus-visible:outline-tm05-acc has-focus-visible:outline-offset-[3px]"><input type="radio" name="tm-05-c" aria-label="Rust" class="absolute inset-0 opacity-0 cursor-pointer"></label>
          <label class="relative size-9 rounded-full cursor-pointer bg-[#2c3440] shadow-[inset_0_0_0_2px_var(--color-tm05-card),0_0_0_1px_var(--color-tm05-edge)] has-checked:shadow-[inset_0_0_0_2px_var(--color-tm05-card),0_0_0_2px_var(--color-tm05-acc)] has-focus-visible:outline-2 has-focus-visible:outline-tm05-acc has-focus-visible:outline-offset-[3px]"><input type="radio" name="tm-05-c" aria-label="Slate" class="absolute inset-0 opacity-0 cursor-pointer"></label>
        </fieldset>

        <fieldset class="flex flex-wrap gap-2.5 mb-5 border-0 p-0">
          <legend class="basis-full mb-2.5 text-[11px] uppercase tracking-[0.16em] text-tm05-mut">Size</legend>
          <label class="relative grid place-items-center min-w-11 min-h-11 px-3 rounded-[9px] cursor-pointer text-sm font-semibold text-tm05-mut border border-tm05-edge bg-tm05-well transition-colors duration-150 has-checked:border-tm05-acc has-checked:bg-tm05-acctint has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tm05-acc has-focus-visible:outline-offset-2">S<input type="radio" name="tm-05-s" aria-label="Small" class="sr-only"></label>
          <label class="relative grid place-items-center min-w-11 min-h-11 px-3 rounded-[9px] cursor-pointer text-sm font-semibold text-tm05-mut border border-tm05-edge bg-tm05-well transition-colors duration-150 has-checked:border-tm05-acc has-checked:bg-tm05-acctint has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tm05-acc has-focus-visible:outline-offset-2">M<input type="radio" name="tm-05-s" aria-label="Medium" checked class="sr-only"></label>
          <label class="relative grid place-items-center min-w-11 min-h-11 px-3 rounded-[9px] cursor-pointer text-sm font-semibold text-tm05-mut border border-tm05-edge bg-tm05-well transition-colors duration-150 has-checked:border-tm05-acc has-checked:bg-tm05-acctint has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tm05-acc has-focus-visible:outline-offset-2">L<input type="radio" name="tm-05-s" aria-label="Large" class="sr-only"></label>
          <label class="relative grid place-items-center min-w-11 min-h-11 px-3 rounded-[9px] cursor-pointer text-sm font-semibold text-tm05-mut border border-tm05-edge bg-tm05-well transition-colors duration-150 has-checked:border-tm05-acc has-checked:bg-tm05-acctint has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-tm05-acc has-focus-visible:outline-offset-2">XL<input type="radio" name="tm-05-s" aria-label="Extra large" class="sr-only"></label>
        </fieldset>

        <div class="flex gap-3 mt-2">
          <div class="flex items-center rounded-xl border border-tm05-edge overflow-hidden">
            <button type="button" data-tm05-step="-1" aria-label="Decrease quantity" class="w-11 h-12 border-0 bg-tm05-well text-tm05-ink text-xl cursor-pointer transition-colors duration-150 hover:bg-tm05-btnhover focus-visible:outline-2 focus-visible:outline-tm05-acc focus-visible:-outline-offset-2">&minus;</button>
            <span id="tm-05-n" aria-live="polite" class="min-w-11 text-center text-base font-semibold text-white">1</span>
            <button type="button" data-tm05-step="1" aria-label="Increase quantity" class="w-11 h-12 border-0 bg-tm05-well text-tm05-ink text-xl cursor-pointer transition-colors duration-150 hover:bg-tm05-btnhover focus-visible:outline-2 focus-visible:outline-tm05-acc focus-visible:-outline-offset-2">+</button>
          </div>
          <button type="button" data-tm05-add class="flex-1 min-h-12 rounded-xl border-0 bg-tm05-acc text-[15px] font-bold text-tm05-onacc cursor-pointer transition-[filter,translate] duration-200 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Add to bag</button>
        </div>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm05-bg: #080a09;
  --color-tm05-bg: oklch(0.15 0.012 150);
  --color-tm05-card: #141a17;
  --color-tm05-card: oklch(0.21 0.015 150);
  --color-tm05-media: #0c110e;
  --color-tm05-media: oklch(0.17 0.012 150);
  --color-tm05-well: #0f1512;
  --color-tm05-well: oklch(0.19 0.012 150);
  --color-tm05-btn: #14201a;
  --color-tm05-btn: oklch(0.22 0.03 150);
  --color-tm05-btnedge: #2c4a3a;
  --color-tm05-btnedge: oklch(0.34 0.06 150);
  --color-tm05-btnhover: #1a2a22;
  --color-tm05-btnhover: oklch(0.26 0.04 150);
  --color-tm05-xbg: #0a0e0cb3;
  --color-tm05-xbg: oklch(0.17 0.012 150 / 0.7);
  --color-tm05-edge: #2c3a32;
  --color-tm05-edge: oklch(0.31 0.02 150);
  --color-tm05-stripeA: #18211c;
  --color-tm05-stripeA: oklch(0.23 0.018 150);
  --color-tm05-stripeB: #141b17;
  --color-tm05-stripeB: oklch(0.21 0.015 150);
  --color-tm05-hi: #f0f7f3;
  --color-tm05-hi: oklch(0.96 0.01 150);
  --color-tm05-ink: #d7e4dc;
  --color-tm05-ink: oklch(0.89 0.015 150);
  --color-tm05-mut: #9db0a5;
  --color-tm05-mut: oklch(0.74 0.02 150);
  --color-tm05-faint: #6d7f75;
  --color-tm05-faint: oklch(0.58 0.02 150);
  --color-tm05-acc: #5fd39b;
  --color-tm05-acc: oklch(0.78 0.15 155);
  --color-tm05-acctint: #1c3a2c;
  --color-tm05-acctint: oklch(0.3 0.06 155);
  --color-tm05-onacc: #04140b;
  --color-tm05-onacc: oklch(0.18 0.04 155);
  --color-tm05-scrim: #04070699;
  --color-tm05-scrim: oklch(0.12 0.008 150 / 0.6);
  --font-tm05-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tm05-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tm-05 {
  width: 100%;
}

#tm-05-dlg::backdrop {
  background: oklch(0.12 0.008 150 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-05-dlg[open]::backdrop {
    background: oklch(0.12 0.008 150 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-05');
  var dlg = root.querySelector('#tm-05-dlg');
  var card = root.querySelector('[data-tm05-card]');
  var n = root.querySelector('#tm-05-n');
  root.querySelector('[data-tm05-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tm05-close]').addEventListener('click', function () { dlg.close(); });
  root.querySelectorAll('[data-tm05-step]').forEach(function (b) {
    b.addEventListener('click', function () {
      n.textContent = Math.max(1, parseInt(n.textContent, 10) + parseInt(b.dataset.tm05Step, 10));
    });
  });
  var add = root.querySelector('[data-tm05-add]');
  add.addEventListener('click', function () {
    add.textContent = 'Added ✓';
    setTimeout(function () { add.textContent = 'Add to bag'; }, 1400);
  });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
