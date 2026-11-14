---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-country-selector-dropdown-with-flags/"
title: "Tailwind Country Selector Dropdown With Flags"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The checkout country picker, ported to variants: the panel carries its closed and open geometry as utilities on one element, the selected row styles itself…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Country Selector Dropdown With Flags
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-country-selector-dropdown-with-flags/

The checkout country picker, ported to variants: the panel carries its closed and open geometry as utilities on one element, the selected row styles itself off aria-selected, and the roving highlight styles itself off data-active. The flags are still gradients &mdash; the one thing that stays in the stylesheet, because a flag is a recipe, not a design token.
## HTML
```html
<section class="tcs-01 w-full min-h-svh grid place-items-center bg-tcs01-bg font-tcs01-sans text-tcs01-ink px-5 py-15" aria-label="Country selector dropdown demo">
  <div class="w-70 max-w-full flex flex-col gap-2.5">
    <span id="tcs01-lbl" class="text-[13px] font-semibold tracking-[0.3px] text-tcs01-mut">Shipping country</span>
    <div data-select class="group relative">
      <button id="tcs01-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs01-list" aria-labelledby="tcs01-lbl tcs01-trigger" class="w-full flex items-center gap-2.75 min-h-12 px-3.75 rounded-tcs01 border border-tcs01-line bg-tcs01-surface text-[15px] text-tcs01-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs01-line2 focus-visible:outline-none focus-visible:border-tcs01-ring focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs01-ring)_28%,transparent)]">
        <span class="tcs01-flag" data-c="us" aria-hidden="true"></span>
        <span data-value class="flex-1 text-left">United States</span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs01-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs01-list" role="listbox" aria-labelledby="tcs01-lbl" tabindex="-1" class="absolute top-[calc(100%+8px)] inset-x-0 z-20 list-none max-h-65 overflow-y-auto p-1.5 rounded-tcs01 border border-tcs01-line bg-tcs01-surface shadow-[0_24px_50px_-12px_oklch(0.12_0.02_275/0.65)] invisible opacity-0 -translate-y-2 scale-98 origin-top [transition:opacity_.22s_ease,translate_.22s_var(--ease-tcs01),scale_.22s_var(--ease-tcs01),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:[transition:opacity_.22s_ease,translate_.22s_var(--ease-tcs01),scale_.22s_var(--ease-tcs01),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs01-o0" role="option" aria-selected="true" data-v="United States" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[9px] text-[15px] text-tcs01-mut2 cursor-pointer transition-colors duration-150 data-active:bg-tcs01-hover aria-selected:text-white"><span class="tcs01-flag" data-c="us" aria-hidden="true"></span>United States<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs01-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs01-o1" role="option" aria-selected="false" data-v="United Kingdom" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[9px] text-[15px] text-tcs01-mut2 cursor-pointer transition-colors duration-150 data-active:bg-tcs01-hover aria-selected:text-white"><span class="tcs01-flag" data-c="uk" aria-hidden="true"></span>United Kingdom<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs01-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs01-o2" role="option" aria-selected="false" data-v="Canada" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[9px] text-[15px] text-tcs01-mut2 cursor-pointer transition-colors duration-150 data-active:bg-tcs01-hover aria-selected:text-white"><span class="tcs01-flag" data-c="ca" aria-hidden="true"></span>Canada<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs01-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs01-o3" role="option" aria-selected="false" data-v="Australia" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[9px] text-[15px] text-tcs01-mut2 cursor-pointer transition-colors duration-150 data-active:bg-tcs01-hover aria-selected:text-white"><span class="tcs01-flag" data-c="au" aria-hidden="true"></span>Australia<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs01-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs01-o4" role="option" aria-selected="false" data-v="Germany" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[9px] text-[15px] text-tcs01-mut2 cursor-pointer transition-colors duration-150 data-active:bg-tcs01-hover aria-selected:text-white"><span class="tcs01-flag" data-c="de" aria-hidden="true"></span>Germany<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs01-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs01-o5" role="option" aria-selected="false" data-v="Japan" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[9px] text-[15px] text-tcs01-mut2 cursor-pointer transition-colors duration-150 data-active:bg-tcs01-hover aria-selected:text-white"><span class="tcs01-flag" data-c="jp" aria-hidden="true"></span>Japan<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs01-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs01-mono text-[11px] text-tcs01-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs01-bg: #0b0e1a;
  --color-tcs01-bg: oklch(0.16 0.03 275);
  --color-tcs01-surface: #171b2e;
  --color-tcs01-surface: oklch(0.23 0.03 275);
  --color-tcs01-line: #2a2f4a;
  --color-tcs01-line: oklch(0.32 0.04 277);
  --color-tcs01-line2: #3a4066;
  --color-tcs01-line2: oklch(0.4 0.05 277);
  --color-tcs01-hover: #232842;
  --color-tcs01-hover: oklch(0.29 0.04 277);
  --color-tcs01-ink: #e6e8f2;
  --color-tcs01-ink: oklch(0.92 0.01 277);
  --color-tcs01-mut: #8b90ad;
  --color-tcs01-mut: oklch(0.64 0.03 277);
  --color-tcs01-mut2: #c9cce0;
  --color-tcs01-mut2: oklch(0.84 0.02 277);
  --color-tcs01-acc: #6366f1;
  --color-tcs01-acc: oklch(0.58 0.2 277);
  --color-tcs01-ring: #818cf8;
  --color-tcs01-ring: oklch(0.68 0.16 277);
  --font-tcs01-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --radius-tcs01: 14px;
  --ease-tcs01: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-01 {
  width: 100%;
  min-height: 100svh;
}
/* Flags stay CSS: six one-off gradient recipes keyed by data-c. They are paint,
   not design-scale values, and each needs pseudo-elements. */

.tcs-01 .tcs01-flag {
  width: 24px;
  height: 16px;
  flex: none;
  border-radius: 3px;
  box-shadow: 0 0 0 1px oklch(1 0 0 / 0.12);
}

.tcs-01 .tcs01-flag[data-c="us"] {
  background: repeating-linear-gradient(#b22234 0 2px, #fff 2px 4px);
  position: relative;
}

.tcs-01 .tcs01-flag[data-c="us"]::before {
  content: "";
  position: absolute;
  inset: 0 60% 46% 0;
  background: #3c3b6e;
  border-radius: 3px 0 0 0;
}

.tcs-01 .tcs01-flag[data-c="uk"] {
  background: #012169;
  position: relative;
  overflow: hidden;
}

.tcs-01 .tcs01-flag[data-c="uk"]::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent 42%, #fff 42% 58%, transparent 58%), linear-gradient(0deg, transparent 38%, #fff 38% 62%, transparent 62%);
}

.tcs-01 .tcs01-flag[data-c="uk"]::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent 45%, #c8102e 45% 55%, transparent 55%), linear-gradient(0deg, transparent 42%, #c8102e 42% 58%, transparent 58%);
}

.tcs-01 .tcs01-flag[data-c="ca"] {
  background: linear-gradient(90deg, #d80621 22%, #fff 22% 78%, #d80621 78%);
  position: relative;
}

.tcs-01 .tcs01-flag[data-c="ca"]::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 5px;
  height: 5px;
  background: #d80621;
  transform: translate(-50%, -50%) rotate(45deg);
}

.tcs-01 .tcs01-flag[data-c="au"] {
  background: #012169;
  position: relative;
}

.tcs-01 .tcs01-flag[data-c="au"]::before {
  content: "";
  position: absolute;
  right: 3px;
  top: 50%;
  width: 3px;
  height: 3px;
  background: #fff;
  border-radius: 50%;
  box-shadow: -4px -3px 0 -1px #fff, 4px 2px 0 -1px #fff;
}

.tcs-01 .tcs01-flag[data-c="de"] {
  background: linear-gradient(#000 0 33%, #dd0000 33% 66%, #ffce00 66%);
}

.tcs-01 .tcs01-flag[data-c="jp"] {
  background: #fff;
  position: relative;
}

.tcs-01 .tcs01-flag[data-c="jp"]::before {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 8px;
  height: 8px;
  background: #bc002d;
  border-radius: 50%;
  transform: translate(-50%, -50%);
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-01 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-01').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-01').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      var o = e.detail.opt;
      root.querySelector('[data-value]').textContent = o.dataset.v;
      root.querySelector('[data-trigger] .tcs01-flag').setAttribute('data-c', o.querySelector('.tcs01-flag').getAttribute('data-c'));
    });
  });
})();
```
