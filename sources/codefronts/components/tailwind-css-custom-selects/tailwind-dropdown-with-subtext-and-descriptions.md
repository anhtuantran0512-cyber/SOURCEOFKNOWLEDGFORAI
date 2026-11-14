---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-dropdown-with-subtext-and-descriptions/"
title: "Tailwind Dropdown With Subtext And Descriptions"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The role picker: gradient icon tile, bold title, description line."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dropdown With Subtext And Descriptions
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-dropdown-with-subtext-and-descriptions/

The role picker: gradient icon tile, bold title, description line. The port's detail worth stealing is the active row's inset ring &mdash; data-active:shadow-[inset_0_0_0_1px_...] &mdash; which reads as a crisp outline on a dark panel without the 1px jump a border would cause.
## HTML
```html
<section class="tcs-13 w-full min-h-svh grid place-items-center bg-tcs13-bg font-tcs13-sans text-tcs13-ink px-5 py-15" aria-label="Dropdown with subtext and descriptions demo">
  <div class="w-85 max-w-full flex flex-col gap-2.5">
    <span id="tcs13-lbl" class="text-[13px] font-semibold text-tcs13-mut">Access role</span>
    <div data-select class="group relative">
      <button id="tcs13-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs13-list" aria-labelledby="tcs13-lbl tcs13-trigger" class="w-full flex items-center gap-3.25 min-h-16 px-3.75 rounded-[15px] border border-tcs13-line bg-tcs13-surface text-tcs13-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs13-line3 focus-visible:outline-none focus-visible:border-tcs13-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs13-acc)_24%,transparent)]">
        <span data-tile class="grid place-items-center w-10 h-10 flex-none rounded-xl bg-[linear-gradient(140deg,oklch(0.62_0.2_293),oklch(0.58_0.2_277))]" aria-hidden="true"><svg viewBox="0 0 24 24" class="w-5 h-5 fill-none stroke-white [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M12 2l7 4v6c0 5-3.5 8-7 10-3.5-2-7-5-7-10V6z"/></svg></span>
        <span class="flex-1 flex flex-col text-left leading-[1.3]"><b data-name class="text-[14.5px]">Administrator</b><small data-desc class="text-[11.5px] text-tcs13-mut">Full access to all settings</small></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs13-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs13-list" role="listbox" aria-labelledby="tcs13-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none max-h-75 overflow-y-auto p-1.5 rounded-[15px] border border-tcs13-line bg-tcs13-panel shadow-[0_28px_56px_-14px_oklch(0.1_0.03_295/0.72)] invisible opacity-0 -translate-y-2.5 [transition:opacity_.2s,translate_.22s_var(--ease-tcs13),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.2s,translate_.22s_var(--ease-tcs13),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs13-o0" role="option" aria-selected="true" data-v="Administrator" data-desc="Full access to all settings and billing" data-grad="oklch(0.62 0.2 293),oklch(0.58 0.2 277)" data-icon="a" class="group/opt flex items-center gap-3.25 min-h-15 px-2.75 rounded-xl cursor-pointer transition-[background-color,box-shadow] duration-150 data-active:bg-tcs13-hover data-active:shadow-[inset_0_0_0_1px_var(--color-tcs13-line2)]"><span class="grid place-items-center w-10 h-10 flex-none rounded-xl bg-[linear-gradient(140deg,oklch(0.62_0.2_293),oklch(0.58_0.2_277))]" aria-hidden="true"><svg viewBox="0 0 24 24" class="w-5 h-5 fill-none stroke-white [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M12 2l7 4v6c0 5-3.5 8-7 10-3.5-2-7-5-7-10V6z"/></svg></span><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm">Administrator</b><small class="text-[11.5px] text-tcs13-mut text-pretty">Full access to all settings and billing</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 flex-none fill-none stroke-tcs13-acc2 [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs13-o1" role="option" aria-selected="false" data-v="Editor" data-desc="Create and edit content, no billing" data-grad="oklch(0.72 0.13 205),oklch(0.62 0.18 255)" data-icon="b" class="group/opt flex items-center gap-3.25 min-h-15 px-2.75 rounded-xl cursor-pointer transition-[background-color,box-shadow] duration-150 data-active:bg-tcs13-hover data-active:shadow-[inset_0_0_0_1px_var(--color-tcs13-line2)]"><span class="grid place-items-center w-10 h-10 flex-none rounded-xl bg-[linear-gradient(140deg,oklch(0.72_0.13_205),oklch(0.62_0.18_255))]" aria-hidden="true"><svg viewBox="0 0 24 24" class="w-5 h-5 fill-none stroke-white [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M4 20l4-1 10-10-3-3L5 16z"/></svg></span><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm">Editor</b><small class="text-[11.5px] text-tcs13-mut text-pretty">Create and edit content, no billing</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 flex-none fill-none stroke-tcs13-acc2 [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs13-o2" role="option" aria-selected="false" data-v="Viewer" data-desc="Read-only access to shared items" data-grad="oklch(0.7 0.16 163),oklch(0.6 0.14 163)" data-icon="c" class="group/opt flex items-center gap-3.25 min-h-15 px-2.75 rounded-xl cursor-pointer transition-[background-color,box-shadow] duration-150 data-active:bg-tcs13-hover data-active:shadow-[inset_0_0_0_1px_var(--color-tcs13-line2)]"><span class="grid place-items-center w-10 h-10 flex-none rounded-xl bg-[linear-gradient(140deg,oklch(0.7_0.16_163),oklch(0.6_0.14_163))]" aria-hidden="true"><svg viewBox="0 0 24 24" class="w-5 h-5 fill-none stroke-white [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg></span><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm">Viewer</b><small class="text-[11.5px] text-tcs13-mut text-pretty">Read-only access to shared items</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 flex-none fill-none stroke-tcs13-acc2 [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs13-o3" role="option" aria-selected="false" data-v="Guest" data-desc="Limited, time-boxed access" data-grad="oklch(0.78 0.16 70),oklch(0.65 0.22 25)" data-icon="d" class="group/opt flex items-center gap-3.25 min-h-15 px-2.75 rounded-xl cursor-pointer transition-[background-color,box-shadow] duration-150 data-active:bg-tcs13-hover data-active:shadow-[inset_0_0_0_1px_var(--color-tcs13-line2)]"><span class="grid place-items-center w-10 h-10 flex-none rounded-xl bg-[linear-gradient(140deg,oklch(0.78_0.16_70),oklch(0.65_0.22_25))]" aria-hidden="true"><svg viewBox="0 0 24 24" class="w-5 h-5 fill-none stroke-white [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg></span><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm">Guest</b><small class="text-[11.5px] text-tcs13-mut text-pretty">Limited, time-boxed access</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 flex-none fill-none stroke-tcs13-acc2 [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs13-mono text-[11px] text-tcs13-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs13-bg: #0d0a1c;
  --color-tcs13-bg: oklch(0.16 0.03 295);
  --color-tcs13-surface: #191333;
  --color-tcs13-surface: oklch(0.23 0.05 295);
  --color-tcs13-panel: #15102e;
  --color-tcs13-panel: oklch(0.21 0.05 295);
  --color-tcs13-hover: #221a45;
  --color-tcs13-hover: oklch(0.27 0.06 295);
  --color-tcs13-line: #2f2757;
  --color-tcs13-line: oklch(0.33 0.06 295);
  --color-tcs13-line2: #352b60;
  --color-tcs13-line2: oklch(0.36 0.07 295);
  --color-tcs13-line3: #443b73;
  --color-tcs13-line3: oklch(0.42 0.08 295);
  --color-tcs13-ink: #ece8fb;
  --color-tcs13-ink: oklch(0.93 0.02 295);
  --color-tcs13-mut: #9990c1;
  --color-tcs13-mut: oklch(0.68 0.06 295);
  --color-tcs13-acc: #8b5cf6;
  --color-tcs13-acc: oklch(0.62 0.2 293);
  --color-tcs13-acc2: #a78bfa;
  --color-tcs13-acc2: oklch(0.72 0.15 293);
  --font-tcs13-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs13-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs13: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-13 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-13 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-13').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-13').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      var o = e.detail.opt, tile = root.querySelector('[data-tile]');
      tile.style.backgroundImage = 'linear-gradient(140deg,' + o.dataset.grad + ')';
      tile.innerHTML = o.querySelector('span').innerHTML;
      root.querySelector('[data-name]').textContent = o.dataset.v;
      root.querySelector('[data-desc]').textContent = o.dataset.desc;
    });
  });
})();
```
