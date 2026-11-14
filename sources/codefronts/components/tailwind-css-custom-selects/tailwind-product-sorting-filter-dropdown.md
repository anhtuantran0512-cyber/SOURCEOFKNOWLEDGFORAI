---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-product-sorting-filter-dropdown/"
title: "Tailwind Product Sorting Filter Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The storefront sort control, light and pink: a single highlight bar tracks the pointer and the keyboard cursor by translating --n row heights, and the icons…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Product Sorting Filter Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-product-sorting-filter-dropdown/

The storefront sort control, light and pink: a single highlight bar tracks the pointer and the keyboard cursor by translating --n row heights, and the icons carry the sort direction so intent is visible before you read the label.
## HTML
```html
<section class="tcs-12 w-full min-h-svh grid place-items-center bg-tcs12-bg font-tcs12-sans text-tcs12-ink px-5 py-15" aria-label="Product sorting filter dropdown demo">
  <div class="w-105 max-w-full flex flex-col gap-2.5">
    <div class="flex items-center justify-between gap-4 px-4.5 py-3.5 rounded-2xl border border-tcs12-line bg-white shadow-[0_12px_30px_-14px_color-mix(in_oklch,var(--color-tcs12-acc)_35%,transparent)]">
      <span class="text-[13.5px] font-semibold text-tcs12-mut">248 products</span>
      <div data-select class="group relative flex items-center gap-2">
        <span id="tcs12-lbl" class="text-[13.5px] font-semibold text-tcs12-mut">Sort:</span>
        <button id="tcs12-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs12-list" aria-labelledby="tcs12-lbl tcs12-trigger" class="flex items-center gap-2 min-h-11 px-3.25 rounded-[11px] border border-tcs12-line2 bg-tcs12-chip text-sm font-semibold text-tcs12-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs12-line3 focus-visible:outline-none focus-visible:border-tcs12-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs12-acc)_16%,transparent)]">
          <span data-name>Featured</span>
          <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tcs12-mut2 [stroke-width:2.3] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
        </button>
        <ul id="tcs12-list" role="listbox" aria-labelledby="tcs12-lbl" tabindex="-1" style="--n:0" class="absolute top-[calc(100%+9px)] right-0 z-20 w-57.5 list-none p-1.5 rounded-[14px] border border-tcs12-line bg-white shadow-[0_24px_48px_-16px_color-mix(in_oklch,var(--color-tcs12-acc)_40%,transparent)] origin-top-right invisible opacity-0 -translate-y-2 scale-98 [transition:opacity_.2s,translate_.22s_var(--ease-tcs12),scale_.22s_var(--ease-tcs12),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:[transition:opacity_.2s,translate_.22s_var(--ease-tcs12),scale_.22s_var(--ease-tcs12),visibility_0s_0s] motion-reduce:transition-none">
          <span aria-hidden="true" class="absolute left-1.5 right-1.5 top-1.5 h-11 rounded-[10px] pointer-events-none opacity-0 bg-linear-[90deg,color-mix(in_oklch,var(--color-tcs12-acc)_12%,transparent),color-mix(in_oklch,var(--color-tcs12-acc2)_10%,transparent)] shadow-[inset_0_0_0_1px_color-mix(in_oklch,var(--color-tcs12-acc)_25%,transparent)] [translate:0_calc(var(--n)*44px)] [transition:translate_.28s_var(--ease-tcs12-spring),opacity_.2s] group-data-open:opacity-100 motion-reduce:transition-none"></span>
          <li id="tcs12-o0" role="option" aria-selected="true" data-v="Featured" class="group/opt relative z-1 flex items-center gap-2.5 h-11 px-2.75 rounded-[10px] text-[13.5px] font-semibold text-tcs12-ink cursor-pointer aria-selected:text-tcs12-acc"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-current [stroke-width:2] [stroke-linecap:round] [stroke-linejoin:round] opacity-70 group-aria-selected/opt:opacity-100"><path d="M12 3l2.5 6H21l-5 4 2 7-6-4-6 4 2-7-5-4h6.5z"/></svg>Featured</li>
          <li id="tcs12-o1" role="option" aria-selected="false" data-v="Price: Low to High" class="group/opt relative z-1 flex items-center gap-2.5 h-11 px-2.75 rounded-[10px] text-[13.5px] font-semibold text-tcs12-ink cursor-pointer aria-selected:text-tcs12-acc"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-current [stroke-width:2] [stroke-linecap:round] [stroke-linejoin:round] opacity-70 group-aria-selected/opt:opacity-100"><path d="M12 5v14M6 13l6 6 6-6"/></svg>Price: Low to High</li>
          <li id="tcs12-o2" role="option" aria-selected="false" data-v="Price: High to Low" class="group/opt relative z-1 flex items-center gap-2.5 h-11 px-2.75 rounded-[10px] text-[13.5px] font-semibold text-tcs12-ink cursor-pointer aria-selected:text-tcs12-acc"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-current [stroke-width:2] [stroke-linecap:round] [stroke-linejoin:round] opacity-70 group-aria-selected/opt:opacity-100"><path d="M12 19V5M6 11l6-6 6 6"/></svg>Price: High to Low</li>
          <li id="tcs12-o3" role="option" aria-selected="false" data-v="Newest Arrivals" class="group/opt relative z-1 flex items-center gap-2.5 h-11 px-2.75 rounded-[10px] text-[13.5px] font-semibold text-tcs12-ink cursor-pointer aria-selected:text-tcs12-acc"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-current [stroke-width:2] [stroke-linecap:round] [stroke-linejoin:round] opacity-70 group-aria-selected/opt:opacity-100"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg>Newest Arrivals</li>
          <li id="tcs12-o4" role="option" aria-selected="false" data-v="Top Rated" class="group/opt relative z-1 flex items-center gap-2.5 h-11 px-2.75 rounded-[10px] text-[13.5px] font-semibold text-tcs12-ink cursor-pointer aria-selected:text-tcs12-acc"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-current [stroke-width:2] [stroke-linecap:round] [stroke-linejoin:round] opacity-70 group-aria-selected/opt:opacity-100"><path d="M12 3l2.5 6H21l-5 4 2 7-6-4-6 4 2-7-5-4h6.5z"/></svg>Top Rated</li>
        </ul>
      </div>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs12-mono text-[11px] text-tcs12-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs12-bg: #fdf2f8;
  --color-tcs12-bg: oklch(0.97 0.015 340);
  --color-tcs12-chip: #fdf2f8;
  --color-tcs12-chip: oklch(0.97 0.02 340);
  --color-tcs12-line: #f3e0ee;
  --color-tcs12-line: oklch(0.93 0.025 340);
  --color-tcs12-line2: #f7d6ea;
  --color-tcs12-line2: oklch(0.9 0.04 340);
  --color-tcs12-line3: #f0abcc;
  --color-tcs12-line3: oklch(0.8 0.09 345);
  --color-tcs12-ink: #374151;
  --color-tcs12-ink: oklch(0.38 0.02 265);
  --color-tcs12-mut: #9ca3af;
  --color-tcs12-mut: oklch(0.7 0.02 265);
  --color-tcs12-mut2: #c77ba0;
  --color-tcs12-mut2: oklch(0.68 0.1 345);
  --color-tcs12-acc: #ec4899;
  --color-tcs12-acc: oklch(0.65 0.2 352);
  --color-tcs12-acc2: #a855f7;
  --color-tcs12-acc2: oklch(0.63 0.23 303);
  --font-tcs12-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs12-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs12: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-tcs12-spring: cubic-bezier(0.34, 1.4, 0.64, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-12 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-12 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-12').querySelector('[data-live]');
    var i = opts.findIndex(function (o) { return o.getAttribute('aria-selected') === 'true'; });
    if (i < 0) i = 0;
    var typed = '', timer;
    function keepInView(el) {
      var top = el.offsetTop, bottom = top + el.offsetHeight;
      if (top < list.scrollTop) list.scrollTop = top;
      else if (bottom > list.scrollTop + list.clientHeight) list.scrollTop = bottom - list.clientHeight;
    }
    function mark(n) {
      i = n;
      opts.forEach(function (o, k) { o.toggleAttribute('data-active', k === n); });
      if (opts[n].id) trig.setAttribute('aria-activedescendant', opts[n].id);
      keepInView(opts[n]);
    }
    function set(open) {
      root.toggleAttribute('data-open', open);
      trig.setAttribute('aria-expanded', String(open));
      if (open) mark(i);
      else {
        opts.forEach(function (o) { o.removeAttribute('data-active'); });
        trig.removeAttribute('aria-activedescendant');
      }
    }
    function pick(n) {
      opts.forEach(function (o) { o.setAttribute('aria-selected', 'false'); });
      opts[n].setAttribute('aria-selected', 'true');
      i = n;
      root.dispatchEvent(new CustomEvent('tcs:pick', { bubbles: true, detail: { opt: opts[n], index: n } }));
      if (live) live.textContent = (opts[n].dataset.v || opts[n].textContent).trim() + ' selected';
      set(false);
      trig.focus();
    }
    trig.addEventListener('click', function () { set(!root.hasAttribute('data-open')); });
    opts.forEach(function (o, k) {
      o.addEventListener('click', function () { pick(k); });
      o.addEventListener('mousemove', function () { if (i !== k && root.hasAttribute('data-open')) mark(k); });
    });
    root.addEventListener('keydown', function (e) {
      var open = root.hasAttribute('data-open');
      if (!open) {
        if (e.key === 'ArrowDown' || e.key === 'ArrowUp' || e.key === 'Enter' || e.key === ' ') { e.preventDefault(); set(true); }
        return;
      }
      if (e.key === 'ArrowDown') { e.preventDefault(); mark((i + 1) % opts.length); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); mark((i - 1 + opts.length) % opts.length); }
      else if (e.key === 'Home') { e.preventDefault(); mark(0); }
      else if (e.key === 'End') { e.preventDefault(); mark(opts.length - 1); }
      else if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(i); }
      else if (e.key === 'Escape' || e.key === 'Tab') { set(false); if (e.key === 'Escape') { e.preventDefault(); trig.focus(); } }
      else if (e.key.length === 1 && e.key.trim()) {
        clearTimeout(timer);
        typed += e.key.toLowerCase();
        timer = setTimeout(function () { typed = ''; }, 600);
        var hit = opts.findIndex(function (o) { return (o.dataset.v || o.textContent).trim().toLowerCase().indexOf(typed) === 0; });
        if (hit >= 0) mark(hit);
      }
    });
    document.addEventListener('pointerdown', function (e) { if (!root.contains(e.target)) set(false); });
  });
})();
(function () {
  document.querySelectorAll('.tcs-12').forEach(function (root) {
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    function to(n) { list.style.setProperty('--n', String(n)); }
    function selected() {
      var n = opts.findIndex(function (o) { return o.getAttribute('aria-selected') === 'true'; });
      return n < 0 ? 0 : n;
    }
    opts.forEach(function (o, k) { o.addEventListener('mousemove', function () { to(k); }); });
    list.addEventListener('mouseleave', function () { to(selected()); });
    root.addEventListener('keydown', function () { requestAnimationFrame(function () {
      var a = opts.findIndex(function (o) { return o.hasAttribute('data-active'); });
      to(a < 0 ? selected() : a);
    }); });
    root.querySelector('[data-trigger]').addEventListener('click', function () { requestAnimationFrame(function () { to(selected()); }); });
    root.addEventListener('tcs:pick', function (e) {
      root.querySelector('[data-name]').textContent = e.detail.opt.dataset.v;
      to(selected());
    });
    to(selected());
  });
})();
```
