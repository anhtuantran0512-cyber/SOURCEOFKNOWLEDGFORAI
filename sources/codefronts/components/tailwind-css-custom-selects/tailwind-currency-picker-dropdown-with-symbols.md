---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-currency-picker-dropdown-with-symbols/"
title: "Tailwind Currency Picker Dropdown With Symbols"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "A fintech currency select whose gradient border is a before: utility, not a stylesheet rule: the conic ring, the mask pair and the hover fade all live in the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Currency Picker Dropdown With Symbols
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-currency-picker-dropdown-with-symbols/

A fintech currency select whose gradient border is a before: utility, not a stylesheet rule: the conic ring, the mask pair and the hover fade all live in the trigger's class list. Options are a three-column grid so $, € and C$ stay aligned, and the panel unfolds with an animated clip-path inset.
## HTML
```html
<section class="tcs-02 w-full min-h-svh grid place-items-center bg-tcs02-bg font-tcs02-sans text-tcs02-ink px-5 py-15" aria-label="Currency picker dropdown demo">
  <div class="w-75 max-w-full flex flex-col gap-2.5">
    <span id="tcs02-lbl" class="text-[13px] font-semibold tracking-[0.3px] text-tcs02-mut">Pay in currency</span>
    <div data-select class="group relative">
      <button id="tcs02-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs02-list" aria-labelledby="tcs02-lbl tcs02-trigger" class="relative w-full flex items-center gap-3.25 min-h-13 px-4 rounded-2xl bg-tcs02-surface text-tcs02-ink cursor-pointer overflow-hidden focus-visible:outline-none before:content-[''] before:absolute before:inset-0 before:rounded-2xl before:p-[1.5px] before:bg-[conic-gradient(from_210deg,var(--color-tcs02-acc),var(--color-tcs02-acc2),var(--color-tcs02-acc),oklch(0.45_0.1_160),var(--color-tcs02-acc))] before:[mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask-composite:exclude] before:opacity-80 before:transition-opacity before:duration-250 hover:before:opacity-100 focus-visible:before:opacity-100 focus-visible:before:shadow-[0_0_22px_-4px_var(--color-tcs02-acc)]">
        <span data-badge class="grid place-items-center w-8.5 h-8.5 rounded-[10px] bg-linear-[140deg,var(--color-tcs02-acc),var(--color-tcs02-acc2)] text-tcs02-bg font-extrabold text-[17px]">$</span>
        <span class="flex-1 flex flex-col text-left leading-[1.25]"><b data-code class="text-[15px] tracking-[0.5px]">USD</b><small data-name class="text-[11.5px] text-tcs02-mut">US Dollar</small></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs02-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-250 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs02-list" role="listbox" aria-labelledby="tcs02-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none max-h-70 overflow-y-auto p-1.75 rounded-2xl border border-tcs02-line bg-tcs02-surface shadow-[0_26px_54px_-14px_oklch(0.1_0.03_165/0.7)] invisible opacity-0 [clip-path:inset(0_0_100%_0)] [transition:clip-path_.28s_var(--ease-tcs02),opacity_.2s,visibility_0s_.28s] group-data-open:visible group-data-open:opacity-100 group-data-open:[clip-path:inset(0_0_0_0)] group-data-open:[transition:clip-path_.28s_var(--ease-tcs02),opacity_.2s,visibility_0s_0s] motion-reduce:[clip-path:none] motion-reduce:transition-none">
        <li id="tcs02-o0" role="option" aria-selected="true" data-v="USD" data-sym="$" data-name="US Dollar" class="group/opt grid grid-cols-[34px_52px_1fr] items-center gap-3 min-h-11 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs02-hover"><span class="grid place-items-center w-8.5 h-8.5 rounded-[9px] bg-tcs02-symbg text-tcs02-lime font-extrabold text-base transition-colors duration-150 group-aria-selected/opt:bg-linear-[140deg,var(--color-tcs02-acc),var(--color-tcs02-acc2)] group-aria-selected/opt:text-tcs02-bg">$</span><span class="font-tcs02-mono text-[13.5px] font-bold tracking-[0.5px] text-tcs02-ink">USD</span><span class="text-[13px] text-tcs02-mut">US Dollar</span></li>
        <li id="tcs02-o1" role="option" aria-selected="false" data-v="EUR" data-sym="€" data-name="Euro" class="group/opt grid grid-cols-[34px_52px_1fr] items-center gap-3 min-h-11 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs02-hover"><span class="grid place-items-center w-8.5 h-8.5 rounded-[9px] bg-tcs02-symbg text-tcs02-lime font-extrabold text-base transition-colors duration-150 group-aria-selected/opt:bg-linear-[140deg,var(--color-tcs02-acc),var(--color-tcs02-acc2)] group-aria-selected/opt:text-tcs02-bg">€</span><span class="font-tcs02-mono text-[13.5px] font-bold tracking-[0.5px] text-tcs02-ink">EUR</span><span class="text-[13px] text-tcs02-mut">Euro</span></li>
        <li id="tcs02-o2" role="option" aria-selected="false" data-v="GBP" data-sym="£" data-name="British Pound" class="group/opt grid grid-cols-[34px_52px_1fr] items-center gap-3 min-h-11 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs02-hover"><span class="grid place-items-center w-8.5 h-8.5 rounded-[9px] bg-tcs02-symbg text-tcs02-lime font-extrabold text-base transition-colors duration-150 group-aria-selected/opt:bg-linear-[140deg,var(--color-tcs02-acc),var(--color-tcs02-acc2)] group-aria-selected/opt:text-tcs02-bg">£</span><span class="font-tcs02-mono text-[13.5px] font-bold tracking-[0.5px] text-tcs02-ink">GBP</span><span class="text-[13px] text-tcs02-mut">British Pound</span></li>
        <li id="tcs02-o3" role="option" aria-selected="false" data-v="JPY" data-sym="¥" data-name="Japanese Yen" class="group/opt grid grid-cols-[34px_52px_1fr] items-center gap-3 min-h-11 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs02-hover"><span class="grid place-items-center w-8.5 h-8.5 rounded-[9px] bg-tcs02-symbg text-tcs02-lime font-extrabold text-base transition-colors duration-150 group-aria-selected/opt:bg-linear-[140deg,var(--color-tcs02-acc),var(--color-tcs02-acc2)] group-aria-selected/opt:text-tcs02-bg">¥</span><span class="font-tcs02-mono text-[13.5px] font-bold tracking-[0.5px] text-tcs02-ink">JPY</span><span class="text-[13px] text-tcs02-mut">Japanese Yen</span></li>
        <li id="tcs02-o4" role="option" aria-selected="false" data-v="CAD" data-sym="C$" data-name="Canadian Dollar" class="group/opt grid grid-cols-[34px_52px_1fr] items-center gap-3 min-h-11 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs02-hover"><span class="grid place-items-center w-8.5 h-8.5 rounded-[9px] bg-tcs02-symbg text-tcs02-lime font-extrabold text-base transition-colors duration-150 group-aria-selected/opt:bg-linear-[140deg,var(--color-tcs02-acc),var(--color-tcs02-acc2)] group-aria-selected/opt:text-tcs02-bg">C$</span><span class="font-tcs02-mono text-[13.5px] font-bold tracking-[0.5px] text-tcs02-ink">CAD</span><span class="text-[13px] text-tcs02-mut">Canadian Dollar</span></li>
        <li id="tcs02-o5" role="option" aria-selected="false" data-v="AUD" data-sym="A$" data-name="Australian Dollar" class="group/opt grid grid-cols-[34px_52px_1fr] items-center gap-3 min-h-11 px-3 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs02-hover"><span class="grid place-items-center w-8.5 h-8.5 rounded-[9px] bg-tcs02-symbg text-tcs02-lime font-extrabold text-base transition-colors duration-150 group-aria-selected/opt:bg-linear-[140deg,var(--color-tcs02-acc),var(--color-tcs02-acc2)] group-aria-selected/opt:text-tcs02-bg">A$</span><span class="font-tcs02-mono text-[13.5px] font-bold tracking-[0.5px] text-tcs02-ink">AUD</span><span class="text-[13px] text-tcs02-mut">Australian Dollar</span></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs02-mono text-[11px] text-tcs02-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs02-bg: #04120c;
  --color-tcs02-bg: oklch(0.16 0.03 165);
  --color-tcs02-surface: #0a1f16;
  --color-tcs02-surface: oklch(0.23 0.04 165);
  --color-tcs02-line: #163a2a;
  --color-tcs02-line: oklch(0.32 0.05 163);
  --color-tcs02-hover: #123227;
  --color-tcs02-hover: oklch(0.29 0.05 164);
  --color-tcs02-symbg: #0f2c20;
  --color-tcs02-symbg: oklch(0.27 0.05 165);
  --color-tcs02-ink: #eafff5;
  --color-tcs02-ink: oklch(0.96 0.03 165);
  --color-tcs02-mut: #7fae9b;
  --color-tcs02-mut: oklch(0.7 0.05 163);
  --color-tcs02-lime: #4ade80;
  --color-tcs02-lime: oklch(0.82 0.19 148);
  --color-tcs02-acc: #10b981;
  --color-tcs02-acc: oklch(0.7 0.16 163);
  --color-tcs02-acc2: #0891b2;
  --color-tcs02-acc2: oklch(0.62 0.12 216);
  --font-tcs02-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs02: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-02 {
  width: 100%;
  min-height: 100svh;
}
/* The only shim utilities cannot express: Safari still needs the -webkit- pair for the
   gradient-border mask on the trigger. Everything else is a before: utility. */

.tcs-02 [data-trigger]::before {
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-02 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-02').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-02').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset;
      root.querySelector('[data-badge]').textContent = d.sym;
      root.querySelector('[data-code]').textContent = d.v;
      root.querySelector('[data-name]').textContent = d.name;
    });
  });
})();
```
