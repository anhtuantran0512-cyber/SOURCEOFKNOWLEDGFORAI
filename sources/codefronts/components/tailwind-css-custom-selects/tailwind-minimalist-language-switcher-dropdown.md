---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-minimalist-language-switcher-dropdown/"
title: "Tailwind Minimalist Language Switcher Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The quiet one: an icon pill in a light header that opens a 210px list of languages with their endonyms."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Language Switcher Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-minimalist-language-switcher-dropdown/

The quiet one: an icon pill in a light header that opens a 210px list of languages with their endonyms. Almost the entire demo is utilities &mdash; the only stylesheet rule is the CSS globe, and the only new markup idea is lang on each option so a screen reader pronounces Français in French.
## HTML
```html
<section class="tcs-06 w-full min-h-svh bg-tcs06-bg font-tcs06-sans text-tcs06-ink" aria-label="Minimalist language switcher demo">
  <div class="flex items-center justify-between gap-4 px-7 py-4 bg-white border-b border-tcs06-line">
    <span class="text-[17px] font-extrabold tracking-[-0.3px]">codefronts</span>
    <div data-select class="group relative">
      <button id="tcs06-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs06-list" aria-label="Change language" class="flex items-center gap-2 min-h-11 pl-3.25 pr-3.5 rounded-full border border-tcs06-line bg-tcs06-chip text-tcs06-ink2 cursor-pointer transition-[background-color,border-color,box-shadow] duration-200 hover:bg-tcs06-chip2 focus-visible:outline-none focus-visible:border-tcs06-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs06-acc)_20%,transparent)]">
        <span class="tcs06-globe" aria-hidden="true"></span>
        <span data-code class="text-[13px] font-bold tracking-[0.5px]">EN</span>
      </button>
      <ul id="tcs06-list" role="listbox" aria-label="Language" tabindex="-1" class="absolute top-[calc(100%+10px)] right-0 z-20 w-52.5 list-none p-1.5 rounded-[14px] border border-tcs06-line bg-white shadow-[0_22px_44px_-16px_oklch(0.3_0.03_260/0.24)] origin-top-right invisible opacity-0 scale-95 -translate-y-1.5 [transition:opacity_.18s,scale_.22s_var(--ease-tcs06),translate_.22s_var(--ease-tcs06),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:scale-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.18s,scale_.22s_var(--ease-tcs06),translate_.22s_var(--ease-tcs06),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs06-o0" role="option" aria-selected="true" data-v="English" data-code="EN" lang="en" class="group/opt flex items-center gap-2.5 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs06-hover"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm text-tcs06-ink">English</b><small class="text-xs text-tcs06-mut">English</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tcs06-acc [stroke-width:2.6] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs06-o1" role="option" aria-selected="false" data-v="French" data-code="FR" lang="fr" class="group/opt flex items-center gap-2.5 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs06-hover"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm text-tcs06-ink">French</b><small class="text-xs text-tcs06-mut">Français</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tcs06-acc [stroke-width:2.6] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs06-o2" role="option" aria-selected="false" data-v="German" data-code="DE" lang="de" class="group/opt flex items-center gap-2.5 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs06-hover"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm text-tcs06-ink">German</b><small class="text-xs text-tcs06-mut">Deutsch</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tcs06-acc [stroke-width:2.6] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs06-o3" role="option" aria-selected="false" data-v="Spanish" data-code="ES" lang="es" class="group/opt flex items-center gap-2.5 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs06-hover"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm text-tcs06-ink">Spanish</b><small class="text-xs text-tcs06-mut">Español</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tcs06-acc [stroke-width:2.6] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs06-o4" role="option" aria-selected="false" data-v="Japanese" data-code="JA" lang="ja" class="group/opt flex items-center gap-2.5 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs06-hover"><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm text-tcs06-ink">Japanese</b><small class="text-xs text-tcs06-mut">日本語</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tcs06-acc [stroke-width:2.6] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
      </ul>
    </div>
  </div>
  <div class="grid gap-3.5 max-w-140 mx-auto px-6 py-12" aria-hidden="true">
    <div class="h-3 w-[64%] rounded-full bg-tcs06-line"></div>
    <div class="h-3 w-[78%] rounded-full bg-tcs06-line"></div>
    <div class="h-3 w-[48%] rounded-full bg-tcs06-line"></div>
  </div>
  <p data-live aria-live="polite" class="sr-only"></p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs06-bg: #f1f5f9;
  --color-tcs06-bg: oklch(0.96 0.005 250);
  --color-tcs06-chip: #f1f5f9;
  --color-tcs06-chip: oklch(0.96 0.008 250);
  --color-tcs06-chip2: #e8eef5;
  --color-tcs06-chip2: oklch(0.93 0.012 250);
  --color-tcs06-hover: #f1f5f9;
  --color-tcs06-hover: oklch(0.96 0.008 250);
  --color-tcs06-line: #e2e8f0;
  --color-tcs06-line: oklch(0.91 0.01 250);
  --color-tcs06-ink: #0f172a;
  --color-tcs06-ink: oklch(0.22 0.03 265);
  --color-tcs06-ink2: #334155;
  --color-tcs06-ink2: oklch(0.38 0.03 260);
  --color-tcs06-mut: #94a3b8;
  --color-tcs06-mut: oklch(0.7 0.03 255);
  --color-tcs06-acc: #0ea5e9;
  --color-tcs06-acc: oklch(0.68 0.15 231);
  --font-tcs06-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tcs06: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-06 {
  width: 100%;
  min-height: 100svh;
}
/* The globe stays CSS: a circle plus two meridians drawn with pseudo-elements and
   currentColor. Three arbitrary before:/after: utilities would be strictly worse. */

.tcs-06 .tcs06-globe {
  position: relative;
  flex: none;
  width: 17px;
  height: 17px;
  border: 1.7px solid currentColor;
  border-radius: 50%;
}

.tcs-06 .tcs06-globe::before {
  content: "";
  position: absolute;
  inset: -1.7px 4px;
  border: 1.7px solid currentColor;
  border-radius: 50%;
}

.tcs-06 .tcs06-globe::after {
  content: "";
  position: absolute;
  left: 50%;
  top: -1.7px;
  bottom: -1.7px;
  border-left: 1.7px solid currentColor;
  transform: translateX(-50%);
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-06 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-06').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-06').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      root.querySelector('[data-code]').textContent = e.detail.opt.dataset.code;
    });
  });
})();
```
