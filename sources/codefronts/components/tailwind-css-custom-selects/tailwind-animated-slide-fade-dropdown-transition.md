---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-animated-slide-fade-dropdown-transition/"
title: "Tailwind Animated Slide Fade Dropdown Transition"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The choreography demo: the panel resolves from blurred-and-small to sharp on a spring, and the rows cascade behind it on a per-index delay &mdash;…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Slide Fade Dropdown Transition
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-animated-slide-fade-dropdown-transition/

The choreography demo: the panel resolves from blurred-and-small to sharp on a spring, and the rows cascade behind it on a per-index delay &mdash; group-data-open:[transition-delay:calc(var(--i)*45ms+60ms)], the per-item index pattern that replaces five :nth-child rules.
## HTML
```html
<section class="tcs-18 w-full min-h-svh grid place-items-center bg-tcs18-bg font-tcs18-sans text-tcs18-ink px-5 py-15" aria-label="Animated slide fade dropdown transition demo">
  <div class="w-70 max-w-full flex flex-col gap-2.5">
    <span id="tcs18-lbl" class="text-[13px] font-semibold text-tcs18-mut">Notification sound</span>
    <div data-select class="group relative">
      <button id="tcs18-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs18-list" aria-labelledby="tcs18-lbl tcs18-trigger" class="w-full flex items-center min-h-12 px-3.75 rounded-[14px] border border-tcs18-line bg-tcs18-surface text-[15px] text-tcs18-ink cursor-pointer transition-[border-color,box-shadow] duration-200 hover:border-tcs18-line2 focus-visible:outline-none focus-visible:border-tcs18-acc focus-visible:shadow-[0_0_0_4px_color-mix(in_oklch,var(--color-tcs18-acc)_20%,transparent)]">
        <span data-name class="flex-1 text-left">Chime</span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs18-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-250 ease-tcs18-spring group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs18-list" role="listbox" aria-labelledby="tcs18-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none p-1.5 rounded-[14px] border border-tcs18-line bg-tcs18-panel shadow-[0_26px_54px_-14px_oklch(0.08_0.02_250/0.72)] origin-top invisible opacity-0 -translate-y-3.5 scale-92 blur-[8px] [transition:opacity_.28s_ease,translate_.4s_var(--ease-tcs18-spring),scale_.4s_var(--ease-tcs18-spring),filter_.28s_ease,visibility_0s_.4s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:blur-none group-data-open:[transition:opacity_.28s_ease,translate_.4s_var(--ease-tcs18-spring),scale_.4s_var(--ease-tcs18-spring),filter_.28s_ease,visibility_0s_0s] motion-reduce:blur-none motion-reduce:scale-100 motion-reduce:translate-y-0 motion-reduce:[transition:opacity_.15s,visibility_0s_.15s]">
        <li id="tcs18-o0" role="option" aria-selected="true" data-v="Chime" style="--i:0" class="group/opt flex items-center min-h-11 px-3.25 rounded-[10px] text-[14.5px] text-tcs18-ink2 cursor-pointer opacity-0 -translate-y-2.5 [transition:background-color_.14s,opacity_.3s_ease,translate_.34s_var(--ease-tcs18-spring)] data-active:bg-tcs18-hover aria-selected:bg-tcs18-sel aria-selected:text-tcs18-acc2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(var(--i)*45ms+60ms)] motion-reduce:opacity-100 motion-reduce:translate-y-0 motion-reduce:transition-none motion-reduce:[transition-delay:0ms]">Chime</li>
        <li id="tcs18-o1" role="option" aria-selected="false" data-v="Pulse" style="--i:1" class="group/opt flex items-center min-h-11 px-3.25 rounded-[10px] text-[14.5px] text-tcs18-ink2 cursor-pointer opacity-0 -translate-y-2.5 [transition:background-color_.14s,opacity_.3s_ease,translate_.34s_var(--ease-tcs18-spring)] data-active:bg-tcs18-hover aria-selected:bg-tcs18-sel aria-selected:text-tcs18-acc2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(var(--i)*45ms+60ms)] motion-reduce:opacity-100 motion-reduce:translate-y-0 motion-reduce:transition-none motion-reduce:[transition-delay:0ms]">Pulse</li>
        <li id="tcs18-o2" role="option" aria-selected="false" data-v="Ripple" style="--i:2" class="group/opt flex items-center min-h-11 px-3.25 rounded-[10px] text-[14.5px] text-tcs18-ink2 cursor-pointer opacity-0 -translate-y-2.5 [transition:background-color_.14s,opacity_.3s_ease,translate_.34s_var(--ease-tcs18-spring)] data-active:bg-tcs18-hover aria-selected:bg-tcs18-sel aria-selected:text-tcs18-acc2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(var(--i)*45ms+60ms)] motion-reduce:opacity-100 motion-reduce:translate-y-0 motion-reduce:transition-none motion-reduce:[transition-delay:0ms]">Ripple</li>
        <li id="tcs18-o3" role="option" aria-selected="false" data-v="Bloom" style="--i:3" class="group/opt flex items-center min-h-11 px-3.25 rounded-[10px] text-[14.5px] text-tcs18-ink2 cursor-pointer opacity-0 -translate-y-2.5 [transition:background-color_.14s,opacity_.3s_ease,translate_.34s_var(--ease-tcs18-spring)] data-active:bg-tcs18-hover aria-selected:bg-tcs18-sel aria-selected:text-tcs18-acc2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(var(--i)*45ms+60ms)] motion-reduce:opacity-100 motion-reduce:translate-y-0 motion-reduce:transition-none motion-reduce:[transition-delay:0ms]">Bloom</li>
        <li id="tcs18-o4" role="option" aria-selected="false" data-v="Silent" style="--i:4" class="group/opt flex items-center min-h-11 px-3.25 rounded-[10px] text-[14.5px] text-tcs18-ink2 cursor-pointer opacity-0 -translate-y-2.5 [transition:background-color_.14s,opacity_.3s_ease,translate_.34s_var(--ease-tcs18-spring)] data-active:bg-tcs18-hover aria-selected:bg-tcs18-sel aria-selected:text-tcs18-acc2 group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:[transition-delay:calc(var(--i)*45ms+60ms)] motion-reduce:opacity-100 motion-reduce:translate-y-0 motion-reduce:transition-none motion-reduce:[transition-delay:0ms]">Silent</li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs18-mono text-[11px] text-tcs18-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs18-bg: #060c18;
  --color-tcs18-bg: oklch(0.16 0.03 255);
  --color-tcs18-surface: #0e1f36;
  --color-tcs18-surface: oklch(0.24 0.05 250);
  --color-tcs18-panel: #0c1c31;
  --color-tcs18-panel: oklch(0.22 0.05 250);
  --color-tcs18-hover: #15304f;
  --color-tcs18-hover: oklch(0.3 0.06 250);
  --color-tcs18-sel: #193758;
  --color-tcs18-sel: oklch(0.33 0.07 250);
  --color-tcs18-line: #1f3a5c;
  --color-tcs18-line: oklch(0.34 0.06 250);
  --color-tcs18-line2: #2d5583;
  --color-tcs18-line2: oklch(0.44 0.08 250);
  --color-tcs18-ink: #dbeafe;
  --color-tcs18-ink: oklch(0.92 0.04 250);
  --color-tcs18-ink2: #cfe0f5;
  --color-tcs18-ink2: oklch(0.88 0.04 250);
  --color-tcs18-mut: #7591b8;
  --color-tcs18-mut: oklch(0.65 0.06 250);
  --color-tcs18-acc: #22d3ee;
  --color-tcs18-acc: oklch(0.79 0.14 202);
  --color-tcs18-acc2: #67e8f9;
  --color-tcs18-acc2: oklch(0.86 0.11 202);
  --font-tcs18-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs18-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-18 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-18 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-18').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-18').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      root.querySelector('[data-name]').textContent = e.detail.opt.dataset.v;
    });
  });
})();
```
