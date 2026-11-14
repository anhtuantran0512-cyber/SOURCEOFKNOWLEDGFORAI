---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-floating-label-select-dropdown-field/"
title: "Tailwind Floating Label Select Dropdown Field"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The floating label, and the port deletes its state machine."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Label Select Dropdown Field
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-floating-label-select-dropdown-field/

The floating label, and the port deletes its state machine. The label floats when the field is focused, when the panel is open, or when a value exists &mdash; group-focus-within:, group-data-open: and group-has-[[aria-selected=true]]:. The has-value class and the two focus listeners are simply gone.
## HTML
```html
<section class="tcs-19 w-full min-h-svh grid place-items-center bg-tcs19-bg font-tcs19-sans text-tcs19-ink px-6 py-15" aria-label="Floating label select field demo">
  <div class="w-90 max-w-full">
    <div data-select class="group relative">
      <span id="tcs19-lab" class="absolute left-3.75 top-1/2 z-1 -translate-y-1/2 origin-left px-1.25 text-[15px] text-tcs19-mut bg-transparent pointer-events-none [transition:translate_.2s_var(--ease-tcs19),scale_.2s_var(--ease-tcs19),color_.2s,background-color_.2s] group-focus-within:-translate-y-[30px] group-focus-within:scale-82 group-focus-within:bg-tcs19-surface group-focus-within:text-tcs19-acc group-data-open:-translate-y-[30px] group-data-open:scale-82 group-data-open:bg-tcs19-surface group-data-open:text-tcs19-acc group-has-[[aria-selected=true]]:-translate-y-[30px] group-has-[[aria-selected=true]]:scale-82 group-has-[[aria-selected=true]]:bg-tcs19-surface motion-reduce:transition-none">Country of residence</span>
      <button id="tcs19-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs19-list" aria-labelledby="tcs19-lab tcs19-trigger" class="w-full flex items-center min-h-14 px-3.75 rounded-xl border-[1.5px] border-tcs19-line bg-tcs19-surface text-[15px] text-tcs19-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs19-line2 focus-visible:outline-none focus-visible:border-tcs19-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs19-acc)_16%,transparent)]">
        <span data-name class="flex-1 text-left"></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs19-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs19-list" role="listbox" aria-labelledby="tcs19-lab" tabindex="-1" class="absolute top-[calc(100%+8px)] inset-x-0 z-20 list-none p-1.5 rounded-xl border border-tcs19-line bg-tcs19-surface shadow-[0_26px_54px_-14px_oklch(0.08_0.02_215/0.7)] invisible opacity-0 -translate-y-2 [transition:opacity_.18s,translate_.2s_var(--ease-tcs19),visibility_0s_.2s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.18s,translate_.2s_var(--ease-tcs19),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs19-o0" role="option" aria-selected="false" data-v="United States" class="group/opt flex items-center min-h-11 px-3.25 rounded-[9px] text-[14.5px] text-tcs19-ink2 cursor-pointer transition-colors duration-150 data-active:bg-tcs19-hover aria-selected:bg-tcs19-sel aria-selected:text-tcs19-acc">United States</li>
        <li id="tcs19-o1" role="option" aria-selected="false" data-v="United Kingdom" class="group/opt flex items-center min-h-11 px-3.25 rounded-[9px] text-[14.5px] text-tcs19-ink2 cursor-pointer transition-colors duration-150 data-active:bg-tcs19-hover aria-selected:bg-tcs19-sel aria-selected:text-tcs19-acc">United Kingdom</li>
        <li id="tcs19-o2" role="option" aria-selected="false" data-v="Canada" class="group/opt flex items-center min-h-11 px-3.25 rounded-[9px] text-[14.5px] text-tcs19-ink2 cursor-pointer transition-colors duration-150 data-active:bg-tcs19-hover aria-selected:bg-tcs19-sel aria-selected:text-tcs19-acc">Canada</li>
        <li id="tcs19-o3" role="option" aria-selected="false" data-v="Australia" class="group/opt flex items-center min-h-11 px-3.25 rounded-[9px] text-[14.5px] text-tcs19-ink2 cursor-pointer transition-colors duration-150 data-active:bg-tcs19-hover aria-selected:bg-tcs19-sel aria-selected:text-tcs19-acc">Australia</li>
        <li id="tcs19-o4" role="option" aria-selected="false" data-v="Netherlands" class="group/opt flex items-center min-h-11 px-3.25 rounded-[9px] text-[14.5px] text-tcs19-ink2 cursor-pointer transition-colors duration-150 data-active:bg-tcs19-hover aria-selected:bg-tcs19-sel aria-selected:text-tcs19-acc">Netherlands</li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 mt-2 font-tcs19-mono text-[11px] text-tcs19-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs19-bg: #0a0f18;
  --color-tcs19-bg: oklch(0.16 0.02 250);
  --color-tcs19-surface: #101826;
  --color-tcs19-surface: oklch(0.21 0.02 250);
  --color-tcs19-hover: #182234;
  --color-tcs19-hover: oklch(0.26 0.02 250);
  --color-tcs19-sel: #193530;
  --color-tcs19-sel: oklch(0.29 0.05 175);
  --color-tcs19-line: #2a3446;
  --color-tcs19-line: oklch(0.31 0.02 250);
  --color-tcs19-line2: #3a4761;
  --color-tcs19-line2: oklch(0.39 0.03 250);
  --color-tcs19-ink: #e6ecf5;
  --color-tcs19-ink: oklch(0.93 0.01 250);
  --color-tcs19-ink2: #cdd6e5;
  --color-tcs19-ink2: oklch(0.86 0.015 250);
  --color-tcs19-mut: #8090a6;
  --color-tcs19-mut: oklch(0.65 0.025 250);
  --color-tcs19-acc: #2dd4bf;
  --color-tcs19-acc: oklch(0.79 0.13 180);
  --font-tcs19-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs19-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs19: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-19 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-19 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-19').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-19').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      root.querySelector('[data-name]').textContent = e.detail.opt.dataset.v;
    });
  });
})();
```
