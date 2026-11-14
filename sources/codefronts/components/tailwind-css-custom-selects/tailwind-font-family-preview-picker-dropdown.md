---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-font-family-preview-picker-dropdown/"
title: "Tailwind Font Family Preview Picker Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "Each row renders its own name in its own face, and picking one repaints the trigger and the sample sentence through a single custom property &mdash; read by…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Font Family Preview Picker Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-font-family-preview-picker-dropdown/

Each row renders its own name in its own face, and picking one repaints the trigger and the sample sentence through a single custom property &mdash; read by font-[family-name:var(--tcs14-ff,system-ui)], the arbitrary utility most people do not know exists.
## HTML
```html
<section class="tcs-14 w-full min-h-svh grid place-items-center bg-tcs14-bg font-tcs14-sans text-tcs14-ink px-5 py-15" aria-label="Font family preview picker demo">
  <div class="w-85 max-w-full flex flex-col gap-2.5">
    <span id="tcs14-lbl" class="text-[13px] font-semibold text-tcs14-mut">Editor font</span>
    <div data-select class="group relative">
      <button id="tcs14-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs14-list" aria-labelledby="tcs14-lbl tcs14-trigger" class="w-full flex items-center gap-2.75 min-h-12 px-3.75 rounded-[14px] border border-tcs14-line bg-tcs14-surface text-tcs14-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs14-line2 focus-visible:outline-none focus-visible:border-tcs14-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs14-acc)_22%,transparent)]">
        <span data-name class="flex-1 text-left text-base font-[family-name:var(--tcs14-ff,system-ui)]">Inter</span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs14-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs14-list" role="listbox" aria-labelledby="tcs14-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none max-h-70 overflow-y-auto p-1.5 rounded-[14px] border border-tcs14-line bg-tcs14-panel shadow-[0_26px_54px_-14px_oklch(0.1_0.02_265/0.7)] invisible opacity-0 -translate-y-2.5 [transition:opacity_.2s,translate_.22s_var(--ease-tcs14),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.2s,translate_.22s_var(--ease-tcs14),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs14-o0" role="option" aria-selected="true" data-v="Inter" data-ff="system-ui,'Segoe UI',sans-serif" style="font-family:system-ui,'Segoe UI',sans-serif" class="group/opt flex items-center justify-between gap-3 min-h-12 px-3.25 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs14-hover aria-selected:bg-tcs14-sel"><span class="text-base">Inter</span><span class="px-2.25 py-0.75 rounded-full font-tcs14-sans text-[10.5px] font-bold tracking-[0.3px] bg-[color-mix(in_oklch,var(--color-tcs14-sans)_18%,transparent)] text-tcs14-sans">Sans</span></li>
        <li id="tcs14-o1" role="option" aria-selected="false" data-v="Georgia" data-ff="Georgia,'Times New Roman',serif" style="font-family:Georgia,'Times New Roman',serif" class="group/opt flex items-center justify-between gap-3 min-h-12 px-3.25 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs14-hover aria-selected:bg-tcs14-sel"><span class="text-base">Georgia</span><span class="px-2.25 py-0.75 rounded-full font-tcs14-sans text-[10.5px] font-bold tracking-[0.3px] bg-[color-mix(in_oklch,var(--color-tcs14-serif)_18%,transparent)] text-tcs14-serif">Serif</span></li>
        <li id="tcs14-o2" role="option" aria-selected="false" data-v="Courier New" data-ff="'Courier New',ui-monospace,monospace" style="font-family:'Courier New',ui-monospace,monospace" class="group/opt flex items-center justify-between gap-3 min-h-12 px-3.25 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs14-hover aria-selected:bg-tcs14-sel"><span class="text-base">Courier New</span><span class="px-2.25 py-0.75 rounded-full font-tcs14-sans text-[10.5px] font-bold tracking-[0.3px] bg-[color-mix(in_oklch,var(--color-tcs14-mono)_18%,transparent)] text-tcs14-mono">Mono</span></li>
        <li id="tcs14-o3" role="option" aria-selected="false" data-v="Trebuchet MS" data-ff="'Trebuchet MS',sans-serif" style="font-family:'Trebuchet MS',sans-serif" class="group/opt flex items-center justify-between gap-3 min-h-12 px-3.25 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs14-hover aria-selected:bg-tcs14-sel"><span class="text-base">Trebuchet MS</span><span class="px-2.25 py-0.75 rounded-full font-tcs14-sans text-[10.5px] font-bold tracking-[0.3px] bg-[color-mix(in_oklch,var(--color-tcs14-sans)_18%,transparent)] text-tcs14-sans">Sans</span></li>
        <li id="tcs14-o4" role="option" aria-selected="false" data-v="Palatino" data-ff="'Palatino Linotype','Book Antiqua',serif" style="font-family:'Palatino Linotype','Book Antiqua',serif" class="group/opt flex items-center justify-between gap-3 min-h-12 px-3.25 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs14-hover aria-selected:bg-tcs14-sel"><span class="text-base">Palatino</span><span class="px-2.25 py-0.75 rounded-full font-tcs14-sans text-[10.5px] font-bold tracking-[0.3px] bg-[color-mix(in_oklch,var(--color-tcs14-serif)_18%,transparent)] text-tcs14-serif">Serif</span></li>
        <li id="tcs14-o5" role="option" aria-selected="false" data-v="Lucida Console" data-ff="'Lucida Console',monospace" style="font-family:'Lucida Console',monospace" class="group/opt flex items-center justify-between gap-3 min-h-12 px-3.25 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs14-hover aria-selected:bg-tcs14-sel"><span class="text-base">Lucida Console</span><span class="px-2.25 py-0.75 rounded-full font-tcs14-sans text-[10.5px] font-bold tracking-[0.3px] bg-[color-mix(in_oklch,var(--color-tcs14-mono)_18%,transparent)] text-tcs14-mono">Mono</span></li>
      </ul>
    </div>
    <p data-sample class="mt-3.5 px-4 py-3.5 rounded-xl border border-tcs14-line bg-tcs14-sample text-[17px] leading-[1.5] text-tcs14-ink2 font-[family-name:var(--tcs14-ff,system-ui)]">The quick brown fox jumps over the lazy dog.</p>
    <p data-live aria-live="polite" class="min-h-4 font-tcs14-mono text-[11px] text-tcs14-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs14-bg: #0f172a;
  --color-tcs14-bg: oklch(0.2 0.03 265);
  --color-tcs14-surface: #1a2236;
  --color-tcs14-surface: oklch(0.26 0.03 265);
  --color-tcs14-panel: #161d30;
  --color-tcs14-panel: oklch(0.24 0.03 265);
  --color-tcs14-sample: #131a2b;
  --color-tcs14-sample: oklch(0.22 0.03 265);
  --color-tcs14-hover: #212b44;
  --color-tcs14-hover: oklch(0.3 0.03 265);
  --color-tcs14-sel: #25314e;
  --color-tcs14-sel: oklch(0.33 0.04 265);
  --color-tcs14-line: #2b3650;
  --color-tcs14-line: oklch(0.33 0.03 265);
  --color-tcs14-line2: #3a4869;
  --color-tcs14-line2: oklch(0.42 0.04 265);
  --color-tcs14-ink: #e5e9f3;
  --color-tcs14-ink: oklch(0.92 0.01 265);
  --color-tcs14-ink2: #cbd5e1;
  --color-tcs14-ink2: oklch(0.85 0.02 260);
  --color-tcs14-mut: #8592ad;
  --color-tcs14-mut: oklch(0.65 0.03 265);
  --color-tcs14-acc: #3b82f6;
  --color-tcs14-acc: oklch(0.62 0.19 258);
  --color-tcs14-sans: #93c5fd;
  --color-tcs14-sans: oklch(0.8 0.1 250);
  --color-tcs14-serif: #d8b4fe;
  --color-tcs14-serif: oklch(0.8 0.11 305);
  --color-tcs14-mono: #6ee7b7;
  --color-tcs14-mono: oklch(0.83 0.13 165);
  --font-tcs14-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs14: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-14 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-14 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-14').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-14').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset;
      root.style.setProperty('--tcs14-ff', d.ff);
      root.querySelector('[data-name]').textContent = d.v;
    });
  });
})();
```
