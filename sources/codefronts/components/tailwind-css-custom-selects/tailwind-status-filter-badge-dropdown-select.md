---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-status-filter-badge-dropdown-select/"
title: "Tailwind Status Filter Badge Dropdown Select"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "A tracker-style status filter where the field becomes the badge you chose."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Status Filter Badge Dropdown Select
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-status-filter-badge-dropdown-select/

A tracker-style status filter where the field becomes the badge you chose. One pill class list serves all five statuses: it reads --s-bg and --s-fg, and a five-line attribute block binds the pair &mdash; the port's answer to when is a value a token and when is it data?
## HTML
```html
<section class="tcs-10 w-full min-h-svh grid place-items-center bg-tcs10-bg font-tcs10-sans text-tcs10-ink px-5 py-15" aria-label="Status filter badge dropdown demo">
  <div class="w-72.5 max-w-full flex flex-col gap-2.5">
    <span id="tcs10-lbl" class="text-[13px] font-semibold text-tcs10-mut">Task status</span>
    <div data-select class="group relative">
      <button id="tcs10-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs10-list" aria-labelledby="tcs10-lbl tcs10-trigger" class="w-full flex items-center gap-2.75 min-h-12 px-3.5 rounded-[14px] border border-tcs10-line bg-tcs10-surface text-tcs10-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs10-line2 focus-visible:outline-none focus-visible:border-tcs10-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs10-acc)_22%,transparent)]">
        <span data-pill data-s="progress" class="inline-flex items-center gap-1.75 px-3.25 py-1.25 rounded-full text-[13px] font-semibold bg-[var(--s-bg)] text-[var(--s-fg)] border border-[color-mix(in_oklch,var(--s-fg)_25%,transparent)]"><span class="w-1.75 h-1.75 rounded-full bg-[var(--s-fg)] shadow-[0_0_8px_-1px_var(--s-fg)]" aria-hidden="true"></span><span data-pill-label>In Progress</span></span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 ml-auto fill-none stroke-tcs10-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs10-list" role="listbox" aria-labelledby="tcs10-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none p-1.5 rounded-[14px] border border-tcs10-line bg-tcs10-panel shadow-[0_26px_54px_-14px_oklch(0.1_0.02_275/0.7)] invisible opacity-0 -translate-y-2.5 [transition:opacity_.2s,translate_.22s_var(--ease-tcs10),visibility_0s_.22s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition:opacity_.2s,translate_.22s_var(--ease-tcs10),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs10-o0" role="option" aria-selected="true" data-v="In Progress" data-s="progress" class="flex items-center min-h-11 px-2.5 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs10-hover aria-selected:bg-tcs10-sel"><span data-s="progress" class="inline-flex items-center gap-1.75 px-3.25 py-1.25 rounded-full text-[13px] font-semibold bg-[var(--s-bg)] text-[var(--s-fg)] border border-[color-mix(in_oklch,var(--s-fg)_25%,transparent)]"><span class="w-1.75 h-1.75 rounded-full bg-[var(--s-fg)] shadow-[0_0_8px_-1px_var(--s-fg)]" aria-hidden="true"></span>In Progress</span></li>
        <li id="tcs10-o1" role="option" aria-selected="false" data-v="In Review" data-s="review" class="flex items-center min-h-11 px-2.5 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs10-hover aria-selected:bg-tcs10-sel"><span data-s="review" class="inline-flex items-center gap-1.75 px-3.25 py-1.25 rounded-full text-[13px] font-semibold bg-[var(--s-bg)] text-[var(--s-fg)] border border-[color-mix(in_oklch,var(--s-fg)_25%,transparent)]"><span class="w-1.75 h-1.75 rounded-full bg-[var(--s-fg)] shadow-[0_0_8px_-1px_var(--s-fg)]" aria-hidden="true"></span>In Review</span></li>
        <li id="tcs10-o2" role="option" aria-selected="false" data-v="Completed" data-s="done" class="flex items-center min-h-11 px-2.5 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs10-hover aria-selected:bg-tcs10-sel"><span data-s="done" class="inline-flex items-center gap-1.75 px-3.25 py-1.25 rounded-full text-[13px] font-semibold bg-[var(--s-bg)] text-[var(--s-fg)] border border-[color-mix(in_oklch,var(--s-fg)_25%,transparent)]"><span class="w-1.75 h-1.75 rounded-full bg-[var(--s-fg)] shadow-[0_0_8px_-1px_var(--s-fg)]" aria-hidden="true"></span>Completed</span></li>
        <li id="tcs10-o3" role="option" aria-selected="false" data-v="Blocked" data-s="blocked" class="flex items-center min-h-11 px-2.5 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs10-hover aria-selected:bg-tcs10-sel"><span data-s="blocked" class="inline-flex items-center gap-1.75 px-3.25 py-1.25 rounded-full text-[13px] font-semibold bg-[var(--s-bg)] text-[var(--s-fg)] border border-[color-mix(in_oklch,var(--s-fg)_25%,transparent)]"><span class="w-1.75 h-1.75 rounded-full bg-[var(--s-fg)] shadow-[0_0_8px_-1px_var(--s-fg)]" aria-hidden="true"></span>Blocked</span></li>
        <li id="tcs10-o4" role="option" aria-selected="false" data-v="Backlog" data-s="backlog" class="flex items-center min-h-11 px-2.5 rounded-[10px] cursor-pointer transition-colors duration-150 data-active:bg-tcs10-hover aria-selected:bg-tcs10-sel"><span data-s="backlog" class="inline-flex items-center gap-1.75 px-3.25 py-1.25 rounded-full text-[13px] font-semibold bg-[var(--s-bg)] text-[var(--s-fg)] border border-[color-mix(in_oklch,var(--s-fg)_25%,transparent)]"><span class="w-1.75 h-1.75 rounded-full bg-[var(--s-fg)] shadow-[0_0_8px_-1px_var(--s-fg)]" aria-hidden="true"></span>Backlog</span></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs10-mono text-[11px] text-tcs10-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs10-bg: #0b0d16;
  --color-tcs10-bg: oklch(0.16 0.02 275);
  --color-tcs10-surface: #171a2a;
  --color-tcs10-surface: oklch(0.23 0.02 275);
  --color-tcs10-panel: #161927;
  --color-tcs10-panel: oklch(0.22 0.02 275);
  --color-tcs10-hover: #20263a;
  --color-tcs10-hover: oklch(0.27 0.02 275);
  --color-tcs10-sel: #232a40;
  --color-tcs10-sel: oklch(0.29 0.025 275);
  --color-tcs10-line: #282d42;
  --color-tcs10-line: oklch(0.3 0.02 275);
  --color-tcs10-line2: #39405e;
  --color-tcs10-line2: oklch(0.38 0.03 275);
  --color-tcs10-ink: #e6e8f2;
  --color-tcs10-ink: oklch(0.92 0.01 275);
  --color-tcs10-mut: #868ca6;
  --color-tcs10-mut: oklch(0.64 0.02 275);
  --color-tcs10-acc: #6366f1;
  --color-tcs10-acc: oklch(0.58 0.2 277);
  --font-tcs10-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs10: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-10 {
  width: 100%;
  min-height: 100svh;
}
/* One status vocabulary, five rows: each data-s binds the pair the pill utilities read.
   Not @theme entries — they are looked up by attribute at runtime, and minting ten
   utilities nobody writes would be pure output weight. */

.tcs-10 [data-s="progress"] {
  --s-bg: oklch(0.72 0.16 75 / 0.14);
  --s-fg: oklch(0.82 0.16 82);
}

.tcs-10 [data-s="review"] {
  --s-bg: oklch(0.58 0.2 277 / 0.14);
  --s-fg: oklch(0.78 0.11 275);
}

.tcs-10 [data-s="done"] {
  --s-bg: oklch(0.7 0.16 163 / 0.14);
  --s-fg: oklch(0.78 0.15 163);
}

.tcs-10 [data-s="blocked"] {
  --s-bg: oklch(0.65 0.22 15 / 0.14);
  --s-fg: oklch(0.72 0.17 15);
}

.tcs-10 [data-s="backlog"] {
  --s-bg: oklch(0.7 0.03 255 / 0.13);
  --s-fg: oklch(0.85 0.02 255);
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-10 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-10').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-10').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      var d = e.detail.opt.dataset;
      root.querySelector('[data-pill]').setAttribute('data-s', d.s);
      root.querySelector('[data-pill-label]').textContent = d.v;
    });
  });
})();
```
