---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-dark-mode-theme-selector-dropdown/"
title: "Tailwind Dark Mode Theme Selector Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "Light / Dark / System, and the port makes an argument: @theme is a build-time mint, so a theme the user switches at runtime belongs in a plain [data-theme]…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Theme Selector Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-dark-mode-theme-selector-dropdown/

Light / Dark / System, and the port makes an argument: @theme is a build-time mint, so a theme the user switches at runtime belongs in a plain [data-theme] block read through bg-[var(--tcs08-surf)]. One attribute repaints the whole stage &mdash; including color-scheme, so native controls follow.
## HTML
```html
<section class="tcs-08 w-full min-h-svh grid place-items-center px-5 py-15 font-tcs08-sans bg-[var(--tcs08-bg)] text-[var(--tcs08-txt)] [transition:background-color_.3s,color_.3s] motion-reduce:transition-none" data-theme="dark" aria-label="Dark mode theme selector demo">
  <div class="w-70 max-w-full flex flex-col gap-2.5">
    <span id="tcs08-lbl" class="text-[13px] font-semibold text-[var(--tcs08-mut)]">Appearance</span>
    <div data-select class="group relative">
      <button id="tcs08-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs08-list" aria-labelledby="tcs08-lbl tcs08-trigger" class="w-full flex items-center gap-2.75 min-h-12 px-3.75 rounded-[14px] border border-[var(--tcs08-line)] bg-[var(--tcs08-surf)] text-[15px] text-[var(--tcs08-txt)] cursor-pointer [transition:border-color_.2s,box-shadow_.2s,background-color_.3s] hover:border-[var(--tcs08-acc)] focus-visible:outline-none focus-visible:border-[var(--tcs08-acc)] focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--tcs08-acc)_22%,transparent)]">
        <span data-ic class="tcs08-ic" data-i="moon" aria-hidden="true"></span>
        <span data-name class="flex-1 text-left">Dark</span>
        <span class="w-5.5 h-5.5 rounded-md bg-[var(--tcs08-prev)] shadow-[inset_0_0_0_1px_var(--tcs08-line)]" aria-hidden="true"></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-[var(--tcs08-mut)] [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs08-list" role="listbox" aria-labelledby="tcs08-lbl" tabindex="-1" class="absolute top-[calc(100%+8px)] inset-x-0 z-20 list-none p-1.5 rounded-[14px] border border-[var(--tcs08-line)] bg-[var(--tcs08-surf)] shadow-[0_24px_50px_-14px_oklch(0.1_0_0/0.5)] origin-top invisible opacity-0 -translate-y-2 scale-98 [transition:opacity_.2s,translate_.22s_var(--ease-tcs08),scale_.22s_var(--ease-tcs08),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:[transition:opacity_.2s,translate_.22s_var(--ease-tcs08),scale_.22s_var(--ease-tcs08),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs08-o0" role="option" aria-selected="false" data-v="Light" data-theme="light" data-ic="sun" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-[15px] cursor-pointer transition-colors duration-150 data-active:bg-[color-mix(in_oklch,var(--tcs08-acc)_12%,transparent)]"><span class="tcs08-ic" data-i="sun" aria-hidden="true"></span>Light<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-[var(--tcs08-acc)] [stroke-width:2.5] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs08-o1" role="option" aria-selected="true" data-v="Dark" data-theme="dark" data-ic="moon" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-[15px] cursor-pointer transition-colors duration-150 data-active:bg-[color-mix(in_oklch,var(--tcs08-acc)_12%,transparent)]"><span class="tcs08-ic" data-i="moon" aria-hidden="true"></span>Dark<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-[var(--tcs08-acc)] [stroke-width:2.5] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs08-o2" role="option" aria-selected="false" data-v="System" data-theme="system" data-ic="sys" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] text-[15px] cursor-pointer transition-colors duration-150 data-active:bg-[color-mix(in_oklch,var(--tcs08-acc)_12%,transparent)]"><span class="tcs08-ic" data-i="sys" aria-hidden="true"></span>System<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-[var(--tcs08-acc)] [stroke-width:2.5] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs08-mono text-[11px] text-[var(--tcs08-mut)]"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-tcs08-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs08-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs08: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-08 {
  width: 100%;
  min-height: 100svh;
}
/* Runtime theme sets, deliberately NOT @theme entries: these are re-bound at runtime by
   a data-theme attribute, and @theme resolves at build time. The markup reads them with
   arbitrary values — bg-[var(--tcs08-surf)] — so one attribute repaints every element. */

.tcs-08[data-theme="dark"] {
  --tcs08-bg: oklch(0.17 0.01 265);
  --tcs08-surf: oklch(0.23 0.01 265);
  --tcs08-line: oklch(0.31 0.01 265);
  --tcs08-txt: oklch(0.93 0.005 265);
  --tcs08-mut: oklch(0.65 0.015 265);
  --tcs08-acc: oklch(0.75 0.13 230);
  --tcs08-prev: oklch(0.17 0.01 265);
  color-scheme: dark;
}

.tcs-08[data-theme="light"] {
  --tcs08-bg: oklch(0.95 0.005 260);
  --tcs08-surf: oklch(1 0 0);
  --tcs08-line: oklch(0.91 0.008 260);
  --tcs08-txt: oklch(0.24 0.02 265);
  --tcs08-mut: oklch(0.55 0.02 260);
  --tcs08-acc: oklch(0.56 0.15 235);
  --tcs08-prev: oklch(1 0 0);
  color-scheme: light;
}

.tcs-08[data-theme="system"] {
  --tcs08-bg: oklch(0.18 0.015 275);
  --tcs08-surf: oklch(0.23 0.015 275);
  --tcs08-line: oklch(0.31 0.015 275);
  --tcs08-txt: oklch(0.93 0.005 275);
  --tcs08-mut: oklch(0.65 0.015 275);
  --tcs08-acc: oklch(0.7 0.14 280);
  --tcs08-prev: linear-gradient(120deg, oklch(0.17 0.01 265) 50%, oklch(0.95 0.005 260) 50%);
  color-scheme: light dark;
}
/* The three icons stay CSS: conic-gradient sun rays behind a radial mask, an inset-shadow
   crescent and a monitor outline — pseudo-element artwork, not design-scale values. */

.tcs-08 .tcs08-ic {
  position: relative;
  display: inline-block;
  flex: none;
  width: 19px;
  height: 19px;
  color: var(--tcs08-acc);
}

.tcs-08 .tcs08-ic[data-i="sun"] {
  border-radius: 50%;
  box-shadow: inset 0 0 0 2px currentColor;
}

.tcs-08 .tcs08-ic[data-i="sun"]::before {
  content: "";
  position: absolute;
  inset: -4px;
  background: conic-gradient(currentColor 0 8%, transparent 8% 25%, currentColor 25% 33%, transparent 33% 50%, currentColor 50% 58%, transparent 58% 75%, currentColor 75% 83%, transparent 83%);
  -webkit-mask: radial-gradient(circle, transparent 55%, #000 56% 70%, transparent 71%);
  mask: radial-gradient(circle, transparent 55%, #000 56% 70%, transparent 71%);
}

.tcs-08 .tcs08-ic[data-i="moon"] {
  border-radius: 50%;
  box-shadow: inset -5px 0 0 0 currentColor;
}

.tcs-08 .tcs08-ic[data-i="sys"] {
  height: 15px;
  margin-top: 2px;
  border: 2px solid currentColor;
  border-radius: 4px;
}

.tcs-08 .tcs08-ic[data-i="sys"]::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: -6px;
  width: 9px;
  height: 2px;
  background: currentColor;
  transform: translateX(-50%);
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-08 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-08').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-08').forEach(function (root) {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset;
      root.setAttribute('data-theme', d.theme);
      root.querySelector('[data-ic]').setAttribute('data-i', d.ic);
      root.querySelector('[data-name]').textContent = d.v;
    });
    mq.addEventListener('change', function () {
      if (root.getAttribute('data-theme') === 'system') root.setAttribute('data-theme', 'system');
    });
  });
})();
```
