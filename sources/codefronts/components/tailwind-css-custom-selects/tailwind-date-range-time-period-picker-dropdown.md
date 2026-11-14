---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-date-range-time-period-picker-dropdown/"
title: "Tailwind Date Range Time Period Picker Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The dashboard period picker: four presets that each show their resolved dates, computed from new Date() at load, plus a separated Custom Range row whose…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Date Range Time Period Picker Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-date-range-time-period-picker-dropdown/

The dashboard period picker: four presets that each show their resolved dates, computed from new Date() at load, plus a separated Custom Range row whose chevron nudges right under the keyboard cursor &mdash; group-data-active/opt:translate-x-0.5, a micro-interaction that costs one utility.
## HTML
```html
<section class="tcs-11 w-full min-h-svh grid place-items-center bg-tcs11-bg font-tcs11-sans text-tcs11-ink px-5 py-15" aria-label="Date range period picker demo">
  <div class="w-80 max-w-full flex flex-col gap-2.5">
    <span id="tcs11-lbl" class="text-[13px] font-semibold text-tcs11-mut">Date range</span>
    <div data-select class="group relative">
      <button id="tcs11-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs11-list" aria-labelledby="tcs11-lbl tcs11-trigger" class="w-full flex items-center gap-3 min-h-14 px-4 rounded-[15px] border border-tcs11-line bg-tcs11-surface text-tcs11-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs11-line2 focus-visible:outline-none focus-visible:border-tcs11-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs11-acc)_22%,transparent)]">
        <span class="tcs11-cal" aria-hidden="true"></span>
        <span class="flex-1 flex flex-col text-left leading-[1.3]"><b data-name class="text-[15px]">Last 7 Days</b><small data-span class="font-tcs11-mono text-[11.5px] text-tcs11-mut"></small></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs11-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs11-list" role="listbox" aria-labelledby="tcs11-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none p-1.5 rounded-[15px] border border-tcs11-line bg-tcs11-panel shadow-[0_26px_54px_-14px_oklch(0.1_0.03_340/0.72)] invisible opacity-0 -translate-y-2.5 [transition:opacity_.2s,translate_.22s_var(--ease-tcs11),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.2s,translate_.22s_var(--ease-tcs11),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs11-o0" role="option" aria-selected="true" data-v="Last 7 Days" data-k="7d" class="group/opt flex items-center gap-3 min-h-12.5 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs11-hover aria-selected:bg-tcs11-sel"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-[14.5px]">Last 7 Days</b><small data-sp class="font-tcs11-mono text-[11.5px] text-tcs11-mut"></small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 fill-none stroke-tcs11-acc [stroke-width:2.5] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs11-o1" role="option" aria-selected="false" data-v="Last 30 Days" data-k="30d" class="group/opt flex items-center gap-3 min-h-12.5 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs11-hover aria-selected:bg-tcs11-sel"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-[14.5px]">Last 30 Days</b><small data-sp class="font-tcs11-mono text-[11.5px] text-tcs11-mut"></small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 fill-none stroke-tcs11-acc [stroke-width:2.5] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs11-o2" role="option" aria-selected="false" data-v="Month to Date" data-k="mtd" class="group/opt flex items-center gap-3 min-h-12.5 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs11-hover aria-selected:bg-tcs11-sel"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-[14.5px]">Month to Date</b><small data-sp class="font-tcs11-mono text-[11.5px] text-tcs11-mut"></small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 fill-none stroke-tcs11-acc [stroke-width:2.5] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs11-o3" role="option" aria-selected="false" data-v="Year to Date" data-k="ytd" class="group/opt flex items-center gap-3 min-h-12.5 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs11-hover aria-selected:bg-tcs11-sel"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-[14.5px]">Year to Date</b><small data-sp class="font-tcs11-mono text-[11.5px] text-tcs11-mut"></small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 fill-none stroke-tcs11-acc [stroke-width:2.5] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li class="h-px mx-2 my-1.5 bg-tcs11-line" role="presentation"></li>
        <li id="tcs11-o4" role="option" aria-selected="false" data-v="Custom Range" data-k="custom" class="group/opt flex items-center gap-3 min-h-12.5 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs11-hover aria-selected:bg-tcs11-sel"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-[14.5px]">Custom Range</b><small class="text-[11.5px] text-tcs11-mut">Pick specific dates</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tcs11-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-transform duration-150 group-data-active/opt:translate-x-0.5"><path d="M9 6l6 6-6 6"/></svg></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs11-mono text-[11px] text-tcs11-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs11-bg: #12091a;
  --color-tcs11-bg: oklch(0.17 0.04 330);
  --color-tcs11-surface: #241430;
  --color-tcs11-surface: oklch(0.25 0.06 330);
  --color-tcs11-panel: #1e1029;
  --color-tcs11-panel: oklch(0.22 0.06 330);
  --color-tcs11-hover: #321c42;
  --color-tcs11-hover: oklch(0.29 0.07 330);
  --color-tcs11-sel: #3a2049;
  --color-tcs11-sel: oklch(0.32 0.08 330);
  --color-tcs11-line: #3d2450;
  --color-tcs11-line: oklch(0.34 0.08 330);
  --color-tcs11-line2: #5a3572;
  --color-tcs11-line2: oklch(0.44 0.11 330);
  --color-tcs11-ink: #f3e6f0;
  --color-tcs11-ink: oklch(0.94 0.02 340);
  --color-tcs11-mut: #b38cab;
  --color-tcs11-mut: oklch(0.72 0.06 340);
  --color-tcs11-acc: #f472b6;
  --color-tcs11-acc: oklch(0.74 0.17 349);
  --font-tcs11-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs11-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs11: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-11 {
  width: 100%;
  min-height: 100svh;
}
/* The calendar glyph stays CSS: a bordered box plus a binding bar and two rings,
   drawn with pseudo-elements. */

.tcs-11 .tcs11-cal {
  position: relative;
  flex: none;
  width: 20px;
  height: 19px;
  margin-top: 2px;
  border: 2px solid var(--color-tcs11-acc);
  border-radius: 5px;
}

.tcs-11 .tcs11-cal::before {
  content: "";
  position: absolute;
  inset: 0 -2px auto -2px;
  top: -2px;
  height: 5px;
  background: var(--color-tcs11-acc);
  border-radius: 4px 4px 0 0;
}

.tcs-11 .tcs11-cal::after {
  content: "";
  position: absolute;
  left: 3px;
  top: -5px;
  width: 3px;
  height: 5px;
  background: var(--color-tcs11-acc);
  border-radius: 2px;
  box-shadow: 8px 0 0 0 var(--color-tcs11-acc);
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-11 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-11').querySelector('[data-live]');
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
  var FMT = { month: 'short', day: 'numeric' };
  function span(key) {
    var end = new Date(), start = new Date();
    if (key === '7d') start.setDate(end.getDate() - 6);
    else if (key === '30d') start.setDate(end.getDate() - 29);
    else if (key === 'mtd') start = new Date(end.getFullYear(), end.getMonth(), 1);
    else if (key === 'ytd') start = new Date(end.getFullYear(), 0, 1);
    else return 'Pick specific dates';
    return start.toLocaleDateString(undefined, FMT) + ' – ' + end.toLocaleDateString(undefined, FMT);
  }
  document.querySelectorAll('.tcs-11').forEach(function (root) {
    root.querySelectorAll('[role="option"][data-k]').forEach(function (o) {
      var sp = o.querySelector('[data-sp]');
      if (sp) sp.textContent = span(o.dataset.k);
    });
    var sel = root.querySelector('[role="option"][aria-selected="true"]');
    root.querySelector('[data-span]').textContent = span(sel ? sel.dataset.k : '7d');
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset;
      root.querySelector('[data-name]').textContent = d.v;
      root.querySelector('[data-span]').textContent = span(d.k);
    });
  });
})();
```
