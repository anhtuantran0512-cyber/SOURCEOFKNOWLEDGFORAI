---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-filter-sort-drawer-bottom-sheet/"
title: "Tailwind Filter & Sort Drawer that Becomes a Bottom Sheet"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "One dialog, two shapes: a right-docked full-height panel on desktop, a rounded bottom sheet under 520px — same markup, same transition contract, different axis."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Filter & Sort Drawer that Becomes a Bottom Sheet
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-filter-sort-drawer-bottom-sheet/

One dialog, two shapes: a right-docked full-height panel on desktop, a rounded bottom sheet under 520px — same markup, same transition contract, different axis. The responsive half of the port is max-[520px]: stacked in front of the open: and open:starting: variants.
## HTML
```html
<section class="tm-15 w-full min-h-svh grid place-items-center bg-tm15-bg font-tm15-sans px-6 py-10">
  <button type="button" data-tm15-open class="inline-flex items-center gap-2.5 min-h-11 px-6 rounded-xl text-sm font-semibold text-tm15-ink bg-tm15-btn border border-tm15-edge cursor-pointer transition-colors duration-200 hover:bg-tm15-btnhover hover:border-tm15-acc focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2"><span aria-hidden="true">⚙</span> Filter &amp; sort</button>

  <dialog id="tm-15-dlg" aria-labelledby="tm-15-title" class="ml-auto mr-0 my-0 h-full max-h-dvh w-[min(380px,100vw)] p-0 border-0 rounded-none text-tm15-ink bg-tm15-card shadow-[-30px_0_80px_-20px_#000] translate-x-full transition-[translate,overlay,display] duration-[340ms] ease-[cubic-bezier(0.4,0,0.2,1)] transition-discrete open:translate-x-0 open:starting:translate-x-full open:backdrop:bg-tm15-scrim max-[520px]:mt-auto max-[520px]:mb-0 max-[520px]:mx-auto max-[520px]:h-auto max-[520px]:max-h-[86dvh] max-[520px]:w-screen max-[520px]:rounded-t-[20px] max-[520px]:translate-x-0 max-[520px]:translate-y-full max-[520px]:open:translate-y-0 max-[520px]:open:starting:translate-y-full motion-reduce:transition-none">
    <form method="dialog" data-tm15-card class="flex flex-col h-full max-[520px]:h-auto">
      <header class="flex items-center justify-between px-5 py-4 border-b border-tm15-edge">
        <h2 id="tm-15-title" class="text-[17px] font-bold text-tm15-hi">Filter &amp; sort</h2>
        <button type="button" data-tm15-close aria-label="Close panel" class="grid place-items-center size-11 rounded-lg border-0 bg-transparent text-tm15-mut text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-tm15-well hover:text-white focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2">&times;</button>
      </header>

      <div class="flex-1 overflow-auto px-5 py-2">
        <fieldset class="border-0 p-0 py-4 border-b border-tm15-edgesoft">
          <legend class="mb-3 text-xs uppercase tracking-[0.14em] text-tm15-mut">Sort by</legend>
          <label class="flex items-center gap-3 min-h-11 text-sm text-tm15-ink cursor-pointer"><input type="radio" name="tm-15-sort" checked class="size-[18px] accent-tm15-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2"> Featured</label>
          <label class="flex items-center gap-3 min-h-11 text-sm text-tm15-ink cursor-pointer"><input type="radio" name="tm-15-sort" class="size-[18px] accent-tm15-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2"> Price: low to high</label>
          <label class="flex items-center gap-3 min-h-11 text-sm text-tm15-ink cursor-pointer"><input type="radio" name="tm-15-sort" class="size-[18px] accent-tm15-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2"> Price: high to low</label>
          <label class="flex items-center gap-3 min-h-11 text-sm text-tm15-ink cursor-pointer"><input type="radio" name="tm-15-sort" class="size-[18px] accent-tm15-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2"> Newest</label>
        </fieldset>

        <fieldset class="border-0 p-0 py-4 border-b border-tm15-edgesoft">
          <legend class="mb-3 text-xs uppercase tracking-[0.14em] text-tm15-mut">Category</legend>
          <label class="flex items-center gap-3 min-h-11 text-sm text-tm15-ink cursor-pointer"><input type="checkbox" data-tm15-cat checked class="size-[18px] accent-tm15-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2"> Outerwear <span class="ml-auto text-xs text-tm15-faint">(128)</span></label>
          <label class="flex items-center gap-3 min-h-11 text-sm text-tm15-ink cursor-pointer"><input type="checkbox" data-tm15-cat class="size-[18px] accent-tm15-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2"> Knitwear <span class="ml-auto text-xs text-tm15-faint">(64)</span></label>
          <label class="flex items-center gap-3 min-h-11 text-sm text-tm15-ink cursor-pointer"><input type="checkbox" data-tm15-cat checked class="size-[18px] accent-tm15-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2"> Accessories <span class="ml-auto text-xs text-tm15-faint">(42)</span></label>
          <label class="flex items-center gap-3 min-h-11 text-sm text-tm15-ink cursor-pointer"><input type="checkbox" data-tm15-cat class="size-[18px] accent-tm15-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-2"> Footwear <span class="ml-auto text-xs text-tm15-faint">(31)</span></label>
        </fieldset>

        <fieldset class="border-0 p-0 py-4 border-b border-tm15-edgesoft">
          <legend class="mb-3 text-xs uppercase tracking-[0.14em] text-tm15-mut">Max price &mdash; <output data-tm15-out class="font-bold normal-case tracking-normal text-tm15-acc">$220</output></legend>
          <input type="range" data-tm15-price min="20" max="400" step="10" value="220" aria-label="Maximum price" class="w-full accent-tm15-acc cursor-pointer focus-visible:outline-2 focus-visible:outline-tm15-acc focus-visible:outline-offset-4 focus-visible:rounded">
        </fieldset>

        <fieldset class="border-0 p-0 py-4">
          <legend class="mb-3 text-xs uppercase tracking-[0.14em] text-tm15-mut">Colour</legend>
          <div class="flex flex-wrap gap-2.5">
            <label class="relative size-11 rounded-[10px] cursor-pointer bg-[#3a4a3f] shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_1px_var(--color-tm15-edge)] has-checked:shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_2px_var(--color-tm15-acc)] has-focus-visible:outline-2 has-focus-visible:outline-tm15-acc has-focus-visible:outline-offset-[3px]"><input type="checkbox" aria-label="Forest" class="absolute inset-0 opacity-0 cursor-pointer"></label>
            <label class="relative size-11 rounded-[10px] cursor-pointer bg-[#5a3f2f] shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_1px_var(--color-tm15-edge)] has-checked:shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_2px_var(--color-tm15-acc)] has-focus-visible:outline-2 has-focus-visible:outline-tm15-acc has-focus-visible:outline-offset-[3px]"><input type="checkbox" aria-label="Rust" class="absolute inset-0 opacity-0 cursor-pointer"></label>
            <label class="relative size-11 rounded-[10px] cursor-pointer bg-[#2c3440] shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_1px_var(--color-tm15-edge)] has-checked:shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_2px_var(--color-tm15-acc)] has-focus-visible:outline-2 has-focus-visible:outline-tm15-acc has-focus-visible:outline-offset-[3px]"><input type="checkbox" aria-label="Slate" class="absolute inset-0 opacity-0 cursor-pointer"></label>
            <label class="relative size-11 rounded-[10px] cursor-pointer bg-[#c9b58a] shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_1px_var(--color-tm15-edge)] has-checked:shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_2px_var(--color-tm15-acc)] has-focus-visible:outline-2 has-focus-visible:outline-tm15-acc has-focus-visible:outline-offset-[3px]"><input type="checkbox" aria-label="Sand" class="absolute inset-0 opacity-0 cursor-pointer"></label>
            <label class="relative size-11 rounded-[10px] cursor-pointer bg-[#7a2f3a] shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_1px_var(--color-tm15-edge)] has-checked:shadow-[inset_0_0_0_2px_var(--color-tm15-card),0_0_0_2px_var(--color-tm15-acc)] has-focus-visible:outline-2 has-focus-visible:outline-tm15-acc has-focus-visible:outline-offset-[3px]"><input type="checkbox" aria-label="Wine" class="absolute inset-0 opacity-0 cursor-pointer"></label>
          </div>
        </fieldset>
      </div>

      <footer class="flex gap-3 px-5 py-4 border-t border-tm15-edge bg-tm15-foot">
        <button type="button" data-tm15-clear class="min-h-12 px-5 rounded-xl border border-tm15-edge bg-tm15-btn text-sm font-semibold text-tm15-ink cursor-pointer transition-colors duration-200 hover:bg-tm15-btnhover focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Clear all</button>
        <button type="button" data-tm15-apply class="flex-1 min-h-12 rounded-xl border-0 bg-tm15-acc text-[14.5px] font-bold text-tm15-onacc cursor-pointer transition-[filter,translate] duration-200 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Show <span data-tm15-n aria-live="polite">170</span> results</button>
      </footer>
    </form>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm15-bg: #07090a;
  --color-tm15-bg: oklch(0.15 0.01 200);
  --color-tm15-card: #131a1d;
  --color-tm15-card: oklch(0.21 0.015 200);
  --color-tm15-foot: #0f1618;
  --color-tm15-foot: oklch(0.18 0.012 200);
  --color-tm15-well: #1a2529;
  --color-tm15-well: oklch(0.24 0.018 200);
  --color-tm15-btn: #131c1f;
  --color-tm15-btn: oklch(0.21 0.015 200);
  --color-tm15-btnhover: #1b2529;
  --color-tm15-btnhover: oklch(0.25 0.02 200);
  --color-tm15-edge: #2a373b;
  --color-tm15-edge: oklch(0.31 0.018 200);
  --color-tm15-edgesoft: #1c262a;
  --color-tm15-edgesoft: oklch(0.24 0.015 200);
  --color-tm15-hi: #f0f6f7;
  --color-tm15-hi: oklch(0.96 0.006 200);
  --color-tm15-ink: #d3dddf;
  --color-tm15-ink: oklch(0.88 0.012 200);
  --color-tm15-mut: #9aa9ad;
  --color-tm15-mut: oklch(0.73 0.018 200);
  --color-tm15-faint: #7c8b8f;
  --color-tm15-faint: oklch(0.62 0.018 200);
  --color-tm15-acc: #4cc7d6;
  --color-tm15-acc: oklch(0.77 0.12 200);
  --color-tm15-onacc: #04161a;
  --color-tm15-onacc: oklch(0.18 0.03 200);
  --color-tm15-scrim: #0407088c;
  --color-tm15-scrim: oklch(0.12 0.008 200 / 0.55);
  --font-tm15-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tm-15 {
  width: 100%;
}

#tm-15-dlg::backdrop {
  background: oklch(0.12 0.008 200 / 0);
  transition: background .34s, overlay .34s allow-discrete, display .34s allow-discrete;
}

@starting-style {
  #tm-15-dlg[open]::backdrop {
    background: oklch(0.12 0.008 200 / 0);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-15');
  var dlg = root.querySelector('#tm-15-dlg');
  var out = root.querySelector('[data-tm15-out]');
  var price = root.querySelector('[data-tm15-price]');
  var n = root.querySelector('[data-tm15-n]');

  function recount() {                       // toy live count so the demo feels real
    var cats = root.querySelectorAll('[data-tm15-cat]:checked').length;
    n.textContent = Math.max(0, cats * 42 + Math.round((price.value - 20) / 380 * 40));
  }

  root.querySelector('[data-tm15-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tm15-close]').addEventListener('click', function () { dlg.close(); });
  root.querySelector('[data-tm15-apply]').addEventListener('click', function () { dlg.close(); });
  price.addEventListener('input', function () { out.textContent = '$' + price.value; recount(); });
  root.querySelectorAll('[data-tm15-cat]').forEach(function (c) { c.addEventListener('change', recount); });
  root.querySelector('[data-tm15-clear]').addEventListener('click', function () {
    root.querySelectorAll('input[type=checkbox]').forEach(function (c) { c.checked = false; });
    root.querySelector('input[type=radio]').checked = true;
    price.value = 220; out.textContent = '$220'; recount();
  });
  recount();
})();
```
