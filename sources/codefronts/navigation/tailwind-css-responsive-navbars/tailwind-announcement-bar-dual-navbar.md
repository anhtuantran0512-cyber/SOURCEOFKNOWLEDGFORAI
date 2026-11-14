---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-announcement-bar-dual-navbar/"
title: "Tailwind Announcement Bar Dual Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "The e-commerce header stack: promo strip, utility row, main nav."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Announcement Bar Dual Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-announcement-bar-dual-navbar/

The e-commerce header stack: promo strip, utility row, main nav. The port upgrades the dismiss from an instant display:none to an animated collapse — grid-rows-[1fr] to grid-rows-[0fr], the modern height-transition idiom — and remembers the dismissal in localStorage.
## HTML
```html
<div class="tnb-19 group w-full min-h-svh bg-tnb19-page font-tnb19-sans text-tnb19-ink" aria-label="Announcement bar dual navbar demo">
  <input type="checkbox" id="tnb19-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="sticky top-0 z-100">
    <div id="tnb19-promo" class="grid grid-rows-[1fr] bg-tnb19-promo transition-[grid-template-rows] duration-300 data-dismissed:grid-rows-[0fr] motion-reduce:transition-none">
      <div class="relative flex items-center justify-center gap-3 overflow-hidden px-10 py-2 text-[13px] font-medium text-white">
        <span aria-hidden="true">&#127881;</span>
        <p>Summer sale &mdash; up to 40% off everything. <a href="#shop" class="font-bold text-white underline underline-offset-2 hover:opacity-80">Shop now &rarr;</a></p>
        <button type="button" id="tnb19-dismiss" aria-label="Dismiss announcement" class="absolute top-1/2 right-3 grid size-6 -translate-y-1/2 cursor-pointer place-items-center rounded-full border-0 bg-white/20 text-sm text-white transition-colors hover:bg-white/35">&times;</button>
      </div>
    </div>
    <div class="flex items-center justify-between border-b border-tnb19-edge bg-tnb19-util px-8 py-1 text-xs font-medium text-tnb19-mut max-md:hidden">
      <div class="flex gap-5">
        <span class="flex items-center gap-1"><span aria-hidden="true">&#128205;</span>Free shipping over $50</span>
        <span class="flex items-center gap-1"><span aria-hidden="true">&#128274;</span>Secure checkout</span>
      </div>
      <div class="flex items-center gap-5">
        <a href="#help" class="text-tnb19-mut no-underline transition-colors hover:text-tnb19-ink">Help</a>
        <a href="#track" class="text-tnb19-mut no-underline transition-colors hover:text-tnb19-ink">Track order</a>
        <a href="#lang" class="text-tnb19-mut no-underline transition-colors hover:text-tnb19-ink">English &#9662;</a>
      </div>
    </div>
    <nav class="flex h-16 items-center gap-6 border-b border-tnb19-edge bg-white px-5 md:px-8" aria-label="Primary">
      <a href="#home" class="shrink-0 text-xl font-extrabold tracking-[-0.03em] text-tnb19-ink no-underline">Stock<span class="text-tnb19-acc">pile</span></a>
      <ul class="hidden flex-1 list-none items-center gap-0 md:flex">
        <li><a href="#home" aria-current="page" class="block rounded-md px-3.5 py-2 text-sm font-semibold text-tnb19-acc no-underline">Home</a></li>
        <li><a href="#new" class="block rounded-md px-3.5 py-2 text-sm font-medium text-tnb19-mut no-underline transition-colors duration-150 hover:bg-tnb19-hover hover:text-tnb19-ink">New arrivals</a></li>
        <li><a href="#collections" class="block rounded-md px-3.5 py-2 text-sm font-medium text-tnb19-mut no-underline transition-colors duration-150 hover:bg-tnb19-hover hover:text-tnb19-ink">Collections</a></li>
        <li><a href="#sale" class="block rounded-md px-3.5 py-2 text-sm font-medium text-tnb19-mut no-underline transition-colors duration-150 hover:bg-tnb19-hover hover:text-tnb19-ink">Sale</a></li>
        <li><a href="#about" class="block rounded-md px-3.5 py-2 text-sm font-medium text-tnb19-mut no-underline transition-colors duration-150 hover:bg-tnb19-hover hover:text-tnb19-ink">About</a></li>
      </ul>
      <div class="ml-auto hidden items-center gap-3 md:flex">
        <a href="#cart" class="relative flex items-center gap-1.5 rounded-lg px-3 py-2 text-sm font-semibold text-tnb19-mut no-underline transition-colors hover:bg-tnb19-hover hover:text-tnb19-ink"><span aria-hidden="true">&#128722;</span>Cart<span class="absolute top-0.5 right-0.5 grid size-4 place-items-center rounded-full bg-tnb19-acc text-[10px] font-extrabold text-white ring-2 ring-white">3</span></a>
        <a href="#signin" class="rounded-lg bg-tnb19-acc px-4 py-2 text-sm font-bold text-white no-underline transition-[background,translate] duration-200 hover:-translate-y-px hover:bg-tnb19-accdark motion-reduce:transition-none motion-reduce:hover:translate-y-0">Sign in</a>
      </div>
      <label for="tnb19-menu" class="ml-auto flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb19-ink transition-transform duration-300 group-has-checked:translate-y-2 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb19-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb19-ink transition-transform duration-300 group-has-checked:-translate-y-2 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </nav>
    <div class="hidden border-b border-tnb19-edge bg-white px-5 py-2 max-md:group-has-checked:grid">
      <a href="#home" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-semibold text-tnb19-acc no-underline">Home</a>
      <a href="#new" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-medium text-tnb19-mut no-underline transition-colors hover:bg-tnb19-hover hover:text-tnb19-ink">New arrivals</a>
      <a href="#collections" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-medium text-tnb19-mut no-underline transition-colors hover:bg-tnb19-hover hover:text-tnb19-ink">Collections</a>
      <a href="#sale" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-medium text-tnb19-mut no-underline transition-colors hover:bg-tnb19-hover hover:text-tnb19-ink">Sale</a>
      <a href="#cart" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-medium text-tnb19-mut no-underline">Cart (3)</a>
      <a href="#signin" class="mt-2 flex min-h-11 items-center justify-center rounded-lg bg-tnb19-acc text-sm font-bold text-white no-underline">Sign in</a>
    </div>
  </header>
  <main class="mx-auto max-w-3xl px-5 py-12 md:px-8">
    <h1 class="mb-4 text-4xl font-extrabold tracking-[-0.03em] text-tnb19-ink">Announcement + Dual Navbar</h1>
    <p class="text-lg leading-relaxed text-tnb19-mut">Dismiss the promo: it collapses rather than vanishing, because the strip is a one-row grid animating <code class="rounded bg-tnb19-hover px-1.5 py-0.5 text-[0.9em]">grid-rows-[1fr]</code> to <code class="rounded bg-tnb19-hover px-1.5 py-0.5 text-[0.9em]">grid-rows-[0fr]</code>. Reload — it stays dismissed.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb19-page: #fbfbfc;
  --color-tnb19-page: oklch(0.99 0.002 280);
  --color-tnb19-ink: #141418;
  --color-tnb19-ink: oklch(0.2 0.005 280);
  --color-tnb19-mut: #6b7280;
  --color-tnb19-mut: oklch(0.55 0.02 265);
  --color-tnb19-edge: #ededf0;
  --color-tnb19-edge: oklch(0.94 0.003 280);
  --color-tnb19-util: #f9f9fa;
  --color-tnb19-util: oklch(0.98 0.002 280);
  --color-tnb19-hover: #f4f4f8;
  --color-tnb19-hover: oklch(0.96 0.004 280);
  --color-tnb19-promo: #6d28d9;
  --color-tnb19-promo: oklch(0.48 0.24 293);
  --color-tnb19-acc: #7c3aed;
  --color-tnb19-acc: oklch(0.53 0.26 295);
  --color-tnb19-accdark: #6d28d9;
  --color-tnb19-accdark: oklch(0.48 0.24 293);
  --font-tnb19-sans: 'Rubik', system-ui, sans-serif;
}

.tnb-19 {
  width: 100%;
  min-height: 100svh;
}

.tnb-19 ::selection {
  background: var(--color-tnb19-acc);
  color: #fff;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tnb-19').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var promo = root.querySelector('#tnb19-promo');
    var btn = root.querySelector('#tnb19-dismiss');
    if (!promo || !btn) return;
    var KEY = 'tnb19-promo-dismissed';

    try {
      if (localStorage.getItem(KEY) === '1') {
        promo.style.transition = 'none';
        promo.toggleAttribute('data-dismissed', true);
        requestAnimationFrame(function () { promo.style.transition = ''; });
      }
    } catch (e) { /* storage blocked: show the promo */ }

    btn.addEventListener('click', function () {
      promo.toggleAttribute('data-dismissed', true);
      btn.setAttribute('aria-expanded', 'false');
      try { localStorage.setItem(KEY, '1'); } catch (e) {}
    });
  });
})();
```
