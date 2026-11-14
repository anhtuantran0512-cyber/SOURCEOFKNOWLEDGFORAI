---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-file-type-media-uploader-dropdown/"
title: "Tailwind File Type Media Uploader Dropdown"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "A format picker dressed as a drop zone: border-2 border-dashed on the trigger, extension badges that tint themselves from one per-row variable, and size…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind File Type Media Uploader Dropdown
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-file-type-media-uploader-dropdown/

A format picker dressed as a drop zone: border-2 border-dashed on the trigger, extension badges that tint themselves from one per-row variable, and size limits as subtext. Five formats, five --x values, and exactly one badge class list.
## HTML
```html
<section class="tcs-15 w-full min-h-svh grid place-items-center bg-tcs15-bg font-tcs15-sans text-tcs15-ink px-5 py-15" aria-label="File type uploader dropdown demo">
  <div class="w-80 max-w-full flex flex-col gap-2.5">
    <span id="tcs15-lbl" class="text-[13px] font-semibold text-tcs15-mut">Accepted file type</span>
    <div data-select class="group relative">
      <button id="tcs15-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs15-list" aria-labelledby="tcs15-lbl tcs15-trigger" class="w-full flex items-center gap-3.25 min-h-16 px-4 rounded-[15px] border-2 border-dashed border-tcs15-line bg-tcs15-surface text-tcs15-ink cursor-pointer transition-[border-color,background-color,box-shadow] duration-200 hover:border-tcs15-line2 hover:bg-tcs15-surface2 focus-visible:outline-none focus-visible:border-tcs15-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs15-acc)_20%,transparent)]">
        <span class="grid place-items-center w-9 h-9 flex-none rounded-[10px] bg-[color-mix(in_oklch,var(--color-tcs15-acc)_14%,transparent)]" aria-hidden="true"><svg viewBox="0 0 24 24" class="w-4.75 h-4.75 fill-none stroke-tcs15-acc2 [stroke-width:1.9] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/></svg></span>
        <span class="flex-1 flex flex-col text-left leading-[1.3]"><b data-name class="text-[14.5px]">PDF documents</b><small data-size class="text-[11.5px] text-tcs15-mut">up to 25 MB</small></span>
        <span data-ext style="--x:oklch(0.65 0.22 25)" class="px-2.25 py-1.25 rounded-lg font-tcs15-mono text-[10.5px] font-extrabold tracking-[0.5px] bg-[color-mix(in_oklch,var(--x)_16%,transparent)] text-[var(--x)]">PDF</span>
      </button>
      <ul id="tcs15-list" role="listbox" aria-labelledby="tcs15-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none p-1.5 rounded-[15px] border border-tcs15-line bg-tcs15-panel shadow-[0_26px_54px_-14px_oklch(0.1_0.03_175/0.7)] invisible opacity-0 -translate-y-2.5 [transition:opacity_.2s,translate_.22s_var(--ease-tcs15),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.2s,translate_.22s_var(--ease-tcs15),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs15-o0" role="option" aria-selected="true" data-v="PDF documents" data-x="pdf" data-size="up to 25 MB" data-color="oklch(0.65 0.22 25)" style="--x:oklch(0.65 0.22 25)" class="group/opt flex items-center gap-3.25 min-h-13 px-2.75 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs15-hover aria-selected:bg-tcs15-sel"><span class="px-2.25 py-1.25 rounded-lg font-tcs15-mono text-[10.5px] font-extrabold tracking-[0.5px] bg-[color-mix(in_oklch,var(--x)_16%,transparent)] text-[var(--x)]">PDF</span><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm">PDF documents</b><small class="text-[11.5px] text-tcs15-mut">up to 25 MB</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 fill-none stroke-tcs15-acc2 [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs15-o1" role="option" aria-selected="false" data-v="CSV spreadsheets" data-x="csv" data-size="up to 10 MB" data-color="oklch(0.72 0.18 145)" style="--x:oklch(0.72 0.18 145)" class="group/opt flex items-center gap-3.25 min-h-13 px-2.75 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs15-hover aria-selected:bg-tcs15-sel"><span class="px-2.25 py-1.25 rounded-lg font-tcs15-mono text-[10.5px] font-extrabold tracking-[0.5px] bg-[color-mix(in_oklch,var(--x)_16%,transparent)] text-[var(--x)]">CSV</span><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm">CSV spreadsheets</b><small class="text-[11.5px] text-tcs15-mut">up to 10 MB</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 fill-none stroke-tcs15-acc2 [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs15-o2" role="option" aria-selected="false" data-v="PNG images" data-x="png" data-size="up to 5 MB" data-color="oklch(0.62 0.19 258)" style="--x:oklch(0.62 0.19 258)" class="group/opt flex items-center gap-3.25 min-h-13 px-2.75 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs15-hover aria-selected:bg-tcs15-sel"><span class="px-2.25 py-1.25 rounded-lg font-tcs15-mono text-[10.5px] font-extrabold tracking-[0.5px] bg-[color-mix(in_oklch,var(--x)_16%,transparent)] text-[var(--x)]">PNG</span><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm">PNG images</b><small class="text-[11.5px] text-tcs15-mut">up to 5 MB</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 fill-none stroke-tcs15-acc2 [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs15-o3" role="option" aria-selected="false" data-v="MP4 video" data-x="mp4" data-size="up to 200 MB" data-color="oklch(0.63 0.23 303)" style="--x:oklch(0.63 0.23 303)" class="group/opt flex items-center gap-3.25 min-h-13 px-2.75 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs15-hover aria-selected:bg-tcs15-sel"><span class="px-2.25 py-1.25 rounded-lg font-tcs15-mono text-[10.5px] font-extrabold tracking-[0.5px] bg-[color-mix(in_oklch,var(--x)_16%,transparent)] text-[var(--x)]">MP4</span><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm">MP4 video</b><small class="text-[11.5px] text-tcs15-mut">up to 200 MB</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 fill-none stroke-tcs15-acc2 [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs15-o4" role="option" aria-selected="false" data-v="ZIP archives" data-x="zip" data-size="up to 100 MB" data-color="oklch(0.78 0.16 70)" style="--x:oklch(0.78 0.16 70)" class="group/opt flex items-center gap-3.25 min-h-13 px-2.75 rounded-[11px] cursor-pointer transition-colors duration-150 data-active:bg-tcs15-hover aria-selected:bg-tcs15-sel"><span class="px-2.25 py-1.25 rounded-lg font-tcs15-mono text-[10.5px] font-extrabold tracking-[0.5px] bg-[color-mix(in_oklch,var(--x)_16%,transparent)] text-[var(--x)]">ZIP</span><span class="flex flex-1 flex-col leading-[1.3]"><b class="text-sm">ZIP archives</b><small class="text-[11.5px] text-tcs15-mut">up to 100 MB</small></span><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 fill-none stroke-tcs15-acc2 [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs15-mono text-[11px] text-tcs15-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs15-bg: #04140f;
  --color-tcs15-bg: oklch(0.17 0.03 175);
  --color-tcs15-surface: #0b201d;
  --color-tcs15-surface: oklch(0.22 0.03 175);
  --color-tcs15-surface2: #0d2622;
  --color-tcs15-surface2: oklch(0.25 0.035 175);
  --color-tcs15-panel: #0a1c1a;
  --color-tcs15-panel: oklch(0.21 0.03 175);
  --color-tcs15-hover: #10312c;
  --color-tcs15-hover: oklch(0.28 0.04 175);
  --color-tcs15-sel: #123933;
  --color-tcs15-sel: oklch(0.31 0.045 175);
  --color-tcs15-line: #1d453e;
  --color-tcs15-line: oklch(0.34 0.04 175);
  --color-tcs15-line2: #2b6157;
  --color-tcs15-line2: oklch(0.44 0.05 175);
  --color-tcs15-ink: #dcf5f0;
  --color-tcs15-ink: oklch(0.93 0.03 175);
  --color-tcs15-mut: #5f8f88;
  --color-tcs15-mut: oklch(0.63 0.04 175);
  --color-tcs15-acc: #14b8a6;
  --color-tcs15-acc: oklch(0.7 0.13 180);
  --color-tcs15-acc2: #2dd4bf;
  --color-tcs15-acc2: oklch(0.79 0.13 180);
  --font-tcs15-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs15-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs15: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-15 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-15 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-15').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-15').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset, ext = root.querySelector('[data-ext]');
      ext.style.setProperty('--x', d.color);
      ext.textContent = d.x.toUpperCase();
      root.querySelector('[data-name]').textContent = d.v;
      root.querySelector('[data-size]').textContent = d.size;
    });
  });
})();
```
