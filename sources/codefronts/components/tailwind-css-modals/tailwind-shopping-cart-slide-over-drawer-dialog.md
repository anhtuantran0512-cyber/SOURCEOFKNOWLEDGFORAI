---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-shopping-cart-slide-over-drawer-dialog/"
title: "Tailwind Shopping Cart Slide-Over Drawer with Dialog"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A right-edge mini-cart that slides in over an inert page: line items, a free-shipping progress bar, a live subtotal and a checkout CTA."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shopping Cart Slide-Over Drawer with Dialog
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-shopping-cart-slide-over-drawer-dialog/

A right-edge mini-cart that slides in over an inert page: line items, a free-shipping progress bar, a live subtotal and a checkout CTA. The slide is translate-x-full &rarr; open:translate-x-0 with open:starting:translate-x-full — in and out, with no JS timers and no transition-end listeners.
## HTML
```html
<section class="tm-06 w-full min-h-svh grid place-items-center bg-tm06-bg font-tm06-sans px-6 py-10">
  <button type="button" data-tm06-open class="inline-flex items-center gap-2.5 min-h-11 px-5 rounded-xl text-sm font-semibold text-tm06-ink bg-tm06-btn border border-tm06-edge cursor-pointer transition-colors duration-200 hover:bg-tm06-btnhover hover:border-tm06-acc focus-visible:outline-2 focus-visible:outline-tm06-acc focus-visible:outline-offset-2">
    <span aria-hidden="true">🛍</span> Your bag <span class="grid place-items-center min-w-[22px] h-[22px] px-1.5 rounded-full bg-tm06-acc text-xs font-bold text-tm06-onacc">2</span>
  </button>

  <dialog id="tm-06-dlg" aria-labelledby="tm-06-title" class="ml-auto mr-0 my-0 h-full max-h-dvh w-[min(400px,100vw)] p-0 border-0 rounded-none text-tm06-ink bg-tm06-card shadow-[-30px_0_80px_-20px_#000] translate-x-full transition-[translate,overlay,display] duration-[340ms] ease-[cubic-bezier(0.4,0,0.2,1)] transition-discrete open:translate-x-0 open:starting:translate-x-full open:backdrop:bg-tm06-scrim motion-reduce:transition-none">
    <div data-tm06-card class="flex flex-col h-full">
      <header class="flex items-center justify-between px-5 pt-5 pb-4 border-b border-tm06-edge">
        <h2 id="tm-06-title" class="text-lg font-bold text-tm06-hi">Your bag</h2>
        <button type="button" data-tm06-close aria-label="Close bag" class="grid place-items-center size-9 rounded-lg border-0 bg-transparent text-tm06-mut text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-tm06-well hover:text-white focus-visible:outline-2 focus-visible:outline-tm06-acc focus-visible:outline-offset-2">&times;</button>
      </header>

      <div class="px-5 py-4 border-b border-tm06-edge">
        <p class="mb-2.5 text-[13px] text-tm06-mut"><b data-tm06-left class="font-semibold text-tm06-acc">$52</b> away from free shipping</p>
        <div data-tm06-bar role="progressbar" aria-valuemin="0" aria-valuemax="200" aria-valuenow="148" aria-label="Progress to free shipping" class="h-1.5 rounded-full bg-tm06-well overflow-hidden">
          <i data-tm06-fill style="width:74%" class="block h-full rounded-full bg-tm06-acc transition-[width] duration-300 motion-reduce:transition-none"></i>
        </div>
      </div>

      <ul class="flex-1 overflow-auto list-none m-0 px-5 py-2">
        <li data-tm06-item class="grid grid-cols-[56px_1fr_auto] items-center gap-3.5 py-4 border-b border-tm06-edge">
          <div class="relative w-14 h-16 rounded-[9px] border border-tm06-edge bg-[repeating-linear-gradient(135deg,var(--color-tm06-stripeA)_0_8px,var(--color-tm06-stripeB)_8px_16px)] after:content-['shot'] after:absolute after:inset-0 after:grid after:place-items-center after:font-tm06-mono after:text-[9px] after:tracking-[0.1em] after:text-tm06-faint"></div>
          <div>
            <p class="text-sm font-semibold text-tm06-hi">Merino Overshirt</p>
            <p class="mt-0.5 mb-2 text-xs text-tm06-mut">Forest &middot; M</p>
            <div class="inline-flex items-center rounded-lg border border-tm06-edge overflow-hidden">
              <button type="button" data-tm06-step="-1" aria-label="Decrease quantity" class="w-11 h-11 border-0 bg-tm06-well text-tm06-ink text-base cursor-pointer transition-colors duration-150 hover:bg-tm06-btnhover focus-visible:outline-2 focus-visible:outline-tm06-acc focus-visible:-outline-offset-2">&minus;</button>
              <span data-tm06-qty aria-live="polite" class="min-w-9 text-center text-[13px] font-semibold text-white">1</span>
              <button type="button" data-tm06-step="1" aria-label="Increase quantity" class="w-11 h-11 border-0 bg-tm06-well text-tm06-ink text-base cursor-pointer transition-colors duration-150 hover:bg-tm06-btnhover focus-visible:outline-2 focus-visible:outline-tm06-acc focus-visible:-outline-offset-2">+</button>
            </div>
          </div>
          <p data-tm06-line data-price="98" class="text-sm font-bold text-tm06-hi">$98</p>
        </li>
        <li data-tm06-item class="grid grid-cols-[56px_1fr_auto] items-center gap-3.5 py-4 border-b border-tm06-edge">
          <div class="relative w-14 h-16 rounded-[9px] border border-tm06-edge bg-[repeating-linear-gradient(135deg,var(--color-tm06-stripeA)_0_8px,var(--color-tm06-stripeB)_8px_16px)] after:content-['shot'] after:absolute after:inset-0 after:grid after:place-items-center after:font-tm06-mono after:text-[9px] after:tracking-[0.1em] after:text-tm06-faint"></div>
          <div>
            <p class="text-sm font-semibold text-tm06-hi">Canvas Field Cap</p>
            <p class="mt-0.5 mb-2 text-xs text-tm06-mut">Rust &middot; OS</p>
            <div class="inline-flex items-center rounded-lg border border-tm06-edge overflow-hidden">
              <button type="button" data-tm06-step="-1" aria-label="Decrease quantity" class="w-11 h-11 border-0 bg-tm06-well text-tm06-ink text-base cursor-pointer transition-colors duration-150 hover:bg-tm06-btnhover focus-visible:outline-2 focus-visible:outline-tm06-acc focus-visible:-outline-offset-2">&minus;</button>
              <span data-tm06-qty aria-live="polite" class="min-w-9 text-center text-[13px] font-semibold text-white">1</span>
              <button type="button" data-tm06-step="1" aria-label="Increase quantity" class="w-11 h-11 border-0 bg-tm06-well text-tm06-ink text-base cursor-pointer transition-colors duration-150 hover:bg-tm06-btnhover focus-visible:outline-2 focus-visible:outline-tm06-acc focus-visible:-outline-offset-2">+</button>
            </div>
          </div>
          <p data-tm06-line data-price="50" class="text-sm font-bold text-tm06-hi">$50</p>
        </li>
      </ul>

      <footer class="px-5 pt-4 pb-5 border-t border-tm06-edge bg-tm06-foot">
        <div class="flex items-baseline justify-between mb-3.5">
          <span class="text-sm text-tm06-mut">Subtotal</span>
          <b data-tm06-total aria-live="polite" class="text-[22px] text-white">$148</b>
        </div>
        <button type="button" class="w-full min-h-12 rounded-xl border-0 bg-tm06-acc text-[15px] font-bold text-tm06-onacc cursor-pointer transition-[filter,translate] duration-200 hover:brightness-110 active:translate-y-px focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:active:translate-y-0">Checkout</button>
        <p class="mt-3 text-center text-[11.5px] text-tm06-faint">Shipping &amp; taxes calculated at checkout</p>
      </footer>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm06-bg: #0a0706;
  --color-tm06-bg: oklch(0.15 0.015 30);
  --color-tm06-card: #191210;
  --color-tm06-card: oklch(0.21 0.018 30);
  --color-tm06-foot: #140d0b;
  --color-tm06-foot: oklch(0.18 0.015 30);
  --color-tm06-well: #1a1310;
  --color-tm06-well: oklch(0.2 0.018 30);
  --color-tm06-btn: #1a1310;
  --color-tm06-btn: oklch(0.2 0.018 30);
  --color-tm06-btnhover: #241a16;
  --color-tm06-btnhover: oklch(0.25 0.025 30);
  --color-tm06-edge: #33251f;
  --color-tm06-edge: oklch(0.3 0.025 30);
  --color-tm06-stripeA: #241a15;
  --color-tm06-stripeA: oklch(0.24 0.02 30);
  --color-tm06-stripeB: #1c130f;
  --color-tm06-stripeB: oklch(0.21 0.018 30);
  --color-tm06-hi: #f7ede9;
  --color-tm06-hi: oklch(0.95 0.012 30);
  --color-tm06-ink: #e5d5cf;
  --color-tm06-ink: oklch(0.89 0.018 30);
  --color-tm06-mut: #b09a92;
  --color-tm06-mut: oklch(0.73 0.025 30);
  --color-tm06-faint: #8a746b;
  --color-tm06-faint: oklch(0.6 0.025 30);
  --color-tm06-acc: #f08a63;
  --color-tm06-acc: oklch(0.74 0.15 40);
  --color-tm06-onacc: #180a07;
  --color-tm06-onacc: oklch(0.2 0.04 40);
  --color-tm06-scrim: #0604038c;
  --color-tm06-scrim: oklch(0.12 0.01 30 / 0.55);
  --font-tm06-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tm06-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tm-06 {
  width: 100%;
}

#tm-06-dlg::backdrop {
  background: oklch(0.12 0.01 30 / 0);
  transition: background .34s, overlay .34s allow-discrete, display .34s allow-discrete;
}

@starting-style {
  #tm-06-dlg[open]::backdrop {
    background: oklch(0.12 0.01 30 / 0);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-06');
  var dlg = root.querySelector('#tm-06-dlg');
  var card = root.querySelector('[data-tm06-card]');
  var THRESHOLD = 200;
  root.querySelector('[data-tm06-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tm06-close]').addEventListener('click', function () { dlg.close(); });

  function recalc() {
    var sum = 0;
    root.querySelectorAll('[data-tm06-item]').forEach(function (li) {
      var q = parseInt(li.querySelector('[data-tm06-qty]').textContent, 10);
      var line = li.querySelector('[data-tm06-line]');
      var base = parseInt(line.dataset.price, 10);
      line.textContent = '$' + base * q;
      sum += base * q;
    });
    root.querySelector('[data-tm06-total]').textContent = '$' + sum;
    root.querySelector('[data-tm06-fill]').style.width = Math.min(100, sum / THRESHOLD * 100) + '%';
    root.querySelector('[data-tm06-left]').textContent = '$' + Math.max(0, THRESHOLD - sum);
    root.querySelector('[data-tm06-bar]').setAttribute('aria-valuenow', sum);
  }

  root.querySelectorAll('[data-tm06-step]').forEach(function (b) {
    b.addEventListener('click', function () {
      var span = b.parentNode.querySelector('[data-tm06-qty]');
      span.textContent = Math.max(1, parseInt(span.textContent, 10) + parseInt(b.dataset.tm06Step, 10));
      recalc();
    });
  });

  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
