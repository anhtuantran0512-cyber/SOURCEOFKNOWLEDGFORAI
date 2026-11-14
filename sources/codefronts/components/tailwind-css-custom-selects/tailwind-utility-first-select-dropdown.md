---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-utility-first-select-dropdown/"
title: "Tailwind Utility First Select Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The one demo whose CSS original was an imitation of Tailwind &mdash; hand-written shadows emulating ring-2, hex greys standing in for the palette."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Utility First Select Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-utility-first-select-dropdown/

The one demo whose CSS original was an imitation of Tailwind &mdash; hand-written shadows emulating ring-2, hex greys standing in for the palette. Here it is simply the thing itself: ring-3 ring-tcs17-acc/40, shadow-xs, shadow-lg, and a stylesheet that holds nothing but tokens.
## HTML
```html
<section class="tcs-17 w-full min-h-svh grid place-items-center bg-tcs17-bg font-tcs17-sans text-tcs17-ink px-5 py-15" aria-label="Utility-first select dropdown demo">
  <div class="w-72 max-w-full flex flex-col gap-1.5">
    <span id="tcs17-lbl" class="text-sm font-medium text-tcs17-ink2">Team</span>
    <div data-select class="group relative">
      <button id="tcs17-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs17-list" aria-labelledby="tcs17-lbl tcs17-trigger" class="w-full flex items-center min-h-11 px-3.25 rounded-lg border border-tcs17-line2 bg-white text-sm text-tcs17-ink shadow-xs cursor-pointer transition-[box-shadow,border-color] duration-150 hover:border-tcs17-line3 focus-visible:outline-none focus-visible:border-tcs17-acc focus-visible:ring-3 focus-visible:ring-tcs17-acc/40">
        <span data-name class="flex-1 text-left">Engineering</span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tcs17-mut [stroke-width:2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-150 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs17-list" role="listbox" aria-labelledby="tcs17-lbl" tabindex="-1" class="absolute top-[calc(100%+6px)] inset-x-0 z-20 list-none p-1.25 rounded-lg border border-tcs17-line bg-white shadow-lg invisible opacity-0 -translate-y-1.5 [transition:opacity_.15s,translate_.18s_ease,visibility_0s_.18s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.15s,translate_.18s_ease,visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs17-o0" role="option" aria-selected="true" data-v="Engineering" class="group/opt flex items-center min-h-11 px-3 rounded-md text-sm text-tcs17-ink2 cursor-pointer transition-colors duration-100 data-active:bg-tcs17-tint data-active:text-tcs17-acc2 aria-selected:font-medium aria-selected:text-tcs17-acc2">Engineering<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 ml-auto fill-none stroke-tcs17-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-100 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs17-o1" role="option" aria-selected="false" data-v="Design" class="group/opt flex items-center min-h-11 px-3 rounded-md text-sm text-tcs17-ink2 cursor-pointer transition-colors duration-100 data-active:bg-tcs17-tint data-active:text-tcs17-acc2 aria-selected:font-medium aria-selected:text-tcs17-acc2">Design<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 ml-auto fill-none stroke-tcs17-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-100 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs17-o2" role="option" aria-selected="false" data-v="Marketing" class="group/opt flex items-center min-h-11 px-3 rounded-md text-sm text-tcs17-ink2 cursor-pointer transition-colors duration-100 data-active:bg-tcs17-tint data-active:text-tcs17-acc2 aria-selected:font-medium aria-selected:text-tcs17-acc2">Marketing<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 ml-auto fill-none stroke-tcs17-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-100 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs17-o3" role="option" aria-selected="false" data-v="Sales" class="group/opt flex items-center min-h-11 px-3 rounded-md text-sm text-tcs17-ink2 cursor-pointer transition-colors duration-100 data-active:bg-tcs17-tint data-active:text-tcs17-acc2 aria-selected:font-medium aria-selected:text-tcs17-acc2">Sales<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 ml-auto fill-none stroke-tcs17-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-100 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs17-o4" role="option" aria-selected="false" data-v="Support" class="group/opt flex items-center min-h-11 px-3 rounded-md text-sm text-tcs17-ink2 cursor-pointer transition-colors duration-100 data-active:bg-tcs17-tint data-active:text-tcs17-acc2 aria-selected:font-medium aria-selected:text-tcs17-acc2">Support<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 ml-auto fill-none stroke-tcs17-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-100 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 mt-1 font-tcs17-mono text-[11px] text-tcs17-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs17-bg: #f9fafb;
  --color-tcs17-bg: oklch(0.985 0.002 250);
  --color-tcs17-tint: #eef2ff;
  --color-tcs17-tint: oklch(0.96 0.02 277);
  --color-tcs17-line: #e5e7eb;
  --color-tcs17-line: oklch(0.92 0.004 250);
  --color-tcs17-line2: #d1d5db;
  --color-tcs17-line2: oklch(0.87 0.005 250);
  --color-tcs17-line3: #9ca3af;
  --color-tcs17-line3: oklch(0.71 0.01 255);
  --color-tcs17-ink: #111827;
  --color-tcs17-ink: oklch(0.21 0.02 265);
  --color-tcs17-ink2: #374151;
  --color-tcs17-ink2: oklch(0.38 0.02 265);
  --color-tcs17-mut: #6b7280;
  --color-tcs17-mut: oklch(0.55 0.02 260);
  --color-tcs17-acc: #6366f1;
  --color-tcs17-acc: oklch(0.58 0.2 277);
  --color-tcs17-acc2: #4338ca;
  --color-tcs17-acc2: oklch(0.44 0.21 277);
  --font-tcs17-sans: ui-sans-serif, system-ui, sans-serif;
  --font-tcs17-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-17 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-17').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-17').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      root.querySelector('[data-name]').textContent = e.detail.opt.dataset.v;
    });
  });
})();
```
