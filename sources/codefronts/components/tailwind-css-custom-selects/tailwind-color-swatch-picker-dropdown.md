---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-color-swatch-picker-dropdown/"
title: "Tailwind Color Swatch Picker Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "Any hex, no new classes: the swatch is bg-[var(--c)] and each row sets --c, so a palette of six or six hundred costs one class list."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Color Swatch Picker Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-color-swatch-picker-dropdown/

Any hex, no new classes: the swatch is bg-[var(--c)] and each row sets --c, so a palette of six or six hundred costs one class list. The trigger's swatch adds a glow of its own colour &mdash; two stacked shadows, one variable.
## HTML
```html
<section class="tcs-16 w-full min-h-svh grid place-items-center bg-tcs16-bg font-tcs16-sans text-tcs16-ink px-5 py-15" aria-label="Color swatch picker dropdown demo">
  <div class="w-75 max-w-full flex flex-col gap-2.5">
    <span id="tcs16-lbl" class="text-[13px] font-semibold text-tcs16-mut">Label color</span>
    <div data-select class="group relative">
      <button id="tcs16-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs16-list" aria-labelledby="tcs16-lbl tcs16-trigger" class="w-full flex items-center gap-3 min-h-12 px-3.75 rounded-[14px] border border-tcs16-line bg-tcs16-surface text-tcs16-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs16-line2 focus-visible:outline-none focus-visible:border-tcs16-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs16-acc)_22%,transparent)]">
        <span data-sw style="--c:#6366F1" class="w-6 h-6 flex-none rounded-full bg-[var(--c)] shadow-[inset_0_0_0_1px_oklch(1_0_0/0.22),0_0_14px_-1px_var(--c)] transition-[box-shadow] duration-250 motion-reduce:transition-none" aria-hidden="true"></span>
        <span class="flex-1 flex flex-col text-left leading-[1.3]"><b data-name class="text-[14.5px]">Indigo</b><small data-hex class="font-tcs16-mono text-[11.5px] text-tcs16-mut">#6366F1</small></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs16-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs16-list" role="listbox" aria-labelledby="tcs16-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none max-h-70 overflow-y-auto p-1.5 rounded-[14px] border border-tcs16-line bg-tcs16-panel shadow-[0_26px_54px_-14px_oklch(0.08_0.02_290/0.72)] invisible opacity-0 -translate-y-2.5 [transition:opacity_.2s,translate_.22s_var(--ease-tcs16),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.2s,translate_.22s_var(--ease-tcs16),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs16-o0" role="option" aria-selected="true" data-v="Indigo" data-hex="#6366F1" style="--c:#6366F1" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs16-hover aria-selected:bg-tcs16-sel"><span class="w-6 h-6 flex-none rounded-full bg-[var(--c)] shadow-[inset_0_0_0_1px_oklch(1_0_0/0.22)]" aria-hidden="true"></span><span class="flex-1 text-sm">Indigo</span><span class="font-tcs16-mono text-[11.5px] text-tcs16-mut">#6366F1</span></li>
        <li id="tcs16-o1" role="option" aria-selected="false" data-v="Rose" data-hex="#F43F5E" style="--c:#F43F5E" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs16-hover aria-selected:bg-tcs16-sel"><span class="w-6 h-6 flex-none rounded-full bg-[var(--c)] shadow-[inset_0_0_0_1px_oklch(1_0_0/0.22)]" aria-hidden="true"></span><span class="flex-1 text-sm">Rose</span><span class="font-tcs16-mono text-[11.5px] text-tcs16-mut">#F43F5E</span></li>
        <li id="tcs16-o2" role="option" aria-selected="false" data-v="Emerald" data-hex="#10B981" style="--c:#10B981" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs16-hover aria-selected:bg-tcs16-sel"><span class="w-6 h-6 flex-none rounded-full bg-[var(--c)] shadow-[inset_0_0_0_1px_oklch(1_0_0/0.22)]" aria-hidden="true"></span><span class="flex-1 text-sm">Emerald</span><span class="font-tcs16-mono text-[11.5px] text-tcs16-mut">#10B981</span></li>
        <li id="tcs16-o3" role="option" aria-selected="false" data-v="Amber" data-hex="#F59E0B" style="--c:#F59E0B" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs16-hover aria-selected:bg-tcs16-sel"><span class="w-6 h-6 flex-none rounded-full bg-[var(--c)] shadow-[inset_0_0_0_1px_oklch(1_0_0/0.22)]" aria-hidden="true"></span><span class="flex-1 text-sm">Amber</span><span class="font-tcs16-mono text-[11.5px] text-tcs16-mut">#F59E0B</span></li>
        <li id="tcs16-o4" role="option" aria-selected="false" data-v="Sky" data-hex="#0EA5E9" style="--c:#0EA5E9" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs16-hover aria-selected:bg-tcs16-sel"><span class="w-6 h-6 flex-none rounded-full bg-[var(--c)] shadow-[inset_0_0_0_1px_oklch(1_0_0/0.22)]" aria-hidden="true"></span><span class="flex-1 text-sm">Sky</span><span class="font-tcs16-mono text-[11.5px] text-tcs16-mut">#0EA5E9</span></li>
        <li id="tcs16-o5" role="option" aria-selected="false" data-v="Fuchsia" data-hex="#D946EF" style="--c:#D946EF" class="group/opt flex items-center gap-3 min-h-11 px-3 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs16-hover aria-selected:bg-tcs16-sel"><span class="w-6 h-6 flex-none rounded-full bg-[var(--c)] shadow-[inset_0_0_0_1px_oklch(1_0_0/0.22)]" aria-hidden="true"></span><span class="flex-1 text-sm">Fuchsia</span><span class="font-tcs16-mono text-[11.5px] text-tcs16-mut">#D946EF</span></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs16-mono text-[11px] text-tcs16-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs16-bg: #0a0912;
  --color-tcs16-bg: oklch(0.15 0.02 295);
  --color-tcs16-surface: #171528;
  --color-tcs16-surface: oklch(0.23 0.03 295);
  --color-tcs16-panel: #131126;
  --color-tcs16-panel: oklch(0.2 0.03 295);
  --color-tcs16-hover: #1e1b38;
  --color-tcs16-hover: oklch(0.26 0.04 295);
  --color-tcs16-sel: #221e40;
  --color-tcs16-sel: oklch(0.29 0.045 295);
  --color-tcs16-line: #2a2842;
  --color-tcs16-line: oklch(0.31 0.03 295);
  --color-tcs16-line2: #3a3860;
  --color-tcs16-line2: oklch(0.39 0.05 295);
  --color-tcs16-ink: #e8e7f3;
  --color-tcs16-ink: oklch(0.92 0.01 295);
  --color-tcs16-mut: #8b89a8;
  --color-tcs16-mut: oklch(0.65 0.03 295);
  --color-tcs16-acc: #6366f1;
  --color-tcs16-acc: oklch(0.58 0.2 277);
  --font-tcs16-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs16: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-16 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-16 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-16').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-16').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset;
      root.querySelector('[data-sw]').style.setProperty('--c', d.hex);
      root.querySelector('[data-name]').textContent = d.v;
      root.querySelector('[data-hex]').textContent = d.hex;
    });
  });
})();
```
