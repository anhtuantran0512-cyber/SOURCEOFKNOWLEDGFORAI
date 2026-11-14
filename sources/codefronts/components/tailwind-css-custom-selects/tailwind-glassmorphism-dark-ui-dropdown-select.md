---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-custom-selects/tailwind-glassmorphism-dark-ui-dropdown-select/"
title: "Tailwind Glassmorphism Dark UI Dropdown Select"
section: "components"
category: "tailwind-css-custom-selects"
category_name: "Tailwind CSS Custom Selects"
description: "The showpiece: a frosted select floating over an aurora that drifts behind it."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Dark UI Dropdown Select
Source: https://codefronts.com/components/tailwind-css-custom-selects/tailwind-glassmorphism-dark-ui-dropdown-select/

The showpiece: a frosted select floating over an aurora that drifts behind it. --animate-tcs20-drift in @theme mints animate-tcs20-drift, the three-blob backdrop is a single arbitrary bg-[radial-gradient(...),...], and the only CSS left is the keyframes and Safari's mask shim.
## HTML
```html
<section class="tcs-20 relative w-full min-h-svh grid place-items-center overflow-hidden bg-tcs20-bg font-tcs20-sans text-tcs20-ink px-5 py-15" aria-label="Glassmorphism dark UI dropdown demo">
  <div aria-hidden="true" class="absolute -inset-[20%] z-0 blur-[20px] animate-tcs20-drift motion-reduce:animate-none bg-[radial-gradient(40%_40%_at_25%_30%,oklch(0.6_0.24_303/0.55),transparent_70%),radial-gradient(45%_45%_at_75%_65%,oklch(0.75_0.14_230/0.5),transparent_70%),radial-gradient(35%_35%_at_60%_20%,oklch(0.65_0.22_352/0.4),transparent_70%)]"></div>
  <div class="relative z-1 w-80 max-w-full flex flex-col gap-3">
    <span id="tcs20-lbl" class="text-[13px] font-semibold text-tcs20-mut">Deployment region</span>
    <div data-select class="group relative">
      <button id="tcs20-trigger" data-trigger type="button" aria-haspopup="listbox" aria-expanded="false" aria-controls="tcs20-list" aria-labelledby="tcs20-lbl tcs20-trigger" class="relative w-full flex items-center gap-2.75 min-h-13 px-4 rounded-[15px] border-0 bg-[oklch(0.2_0.03_300/0.45)] backdrop-blur-[18px] text-tcs20-ink cursor-pointer shadow-[inset_0_1px_0_oklch(1_0_0/0.14),0_10px_30px_-12px_oklch(0.05_0_0/0.6)] transition-[box-shadow] duration-200 focus-visible:outline-none focus-visible:shadow-[inset_0_1px_0_oklch(1_0_0/0.2),0_0_0_4px_color-mix(in_oklch,var(--color-tcs20-acc)_30%,transparent)] before:content-[''] before:absolute before:inset-0 before:rounded-[15px] before:p-px before:pointer-events-none before:bg-[linear-gradient(140deg,oklch(1_0_0/0.5),oklch(1_0_0/0.05)_40%,transparent)] before:[mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask-composite:exclude]">
        <span class="w-2.25 h-2.25 flex-none rounded-full bg-tcs20-live shadow-[0_0_10px_-1px_var(--color-tcs20-live)]" aria-hidden="true"></span>
        <span data-name class="flex-1 text-left text-[15px]">US East (N. Virginia)</span>
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.5 h-4.5 fill-none stroke-tcs20-mut [stroke-width:2.2] [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-data-open:rotate-180 motion-reduce:transition-none"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <ul id="tcs20-list" role="listbox" aria-labelledby="tcs20-lbl" tabindex="-1" class="absolute top-[calc(100%+9px)] inset-x-0 z-20 list-none p-1.5 rounded-[15px] border border-[oklch(1_0_0/0.12)] bg-[oklch(0.18_0.03_300/0.62)] backdrop-blur-[18px] shadow-[inset_0_1px_0_oklch(1_0_0/0.1),0_28px_56px_-16px_oklch(0.05_0_0/0.7)] origin-top invisible opacity-0 -translate-y-2.5 scale-98 [transition:opacity_.22s,translate_.28s_var(--ease-tcs20),scale_.28s_var(--ease-tcs20),visibility_0s_.28s] group-data-open:visible group-data-open:opacity-100 group-data-open:translate-y-0 group-data-open:scale-100 group-data-open:[transition:opacity_.22s,translate_.28s_var(--ease-tcs20),scale_.28s_var(--ease-tcs20),visibility_0s_0s] motion-reduce:transition-none">
        <li id="tcs20-o0" role="option" aria-selected="true" data-v="US East (N. Virginia)" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[10px] text-[14.5px] text-tcs20-ink2 cursor-pointer transition-colors duration-150 data-active:bg-[oklch(1_0_0/0.08)] aria-selected:bg-[oklch(1_0_0/0.06)]"><span class="w-1.75 h-1.75 flex-none rounded-full bg-[oklch(1_0_0/0.35)] transition-[background-color,box-shadow] duration-150 group-aria-selected/opt:bg-tcs20-live group-aria-selected/opt:shadow-[0_0_8px_-1px_var(--color-tcs20-live)]" aria-hidden="true"></span>US East (N. Virginia)<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs20-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs20-o1" role="option" aria-selected="false" data-v="US West (Oregon)" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[10px] text-[14.5px] text-tcs20-ink2 cursor-pointer transition-colors duration-150 data-active:bg-[oklch(1_0_0/0.08)] aria-selected:bg-[oklch(1_0_0/0.06)]"><span class="w-1.75 h-1.75 flex-none rounded-full bg-[oklch(1_0_0/0.35)] transition-[background-color,box-shadow] duration-150 group-aria-selected/opt:bg-tcs20-live group-aria-selected/opt:shadow-[0_0_8px_-1px_var(--color-tcs20-live)]" aria-hidden="true"></span>US West (Oregon)<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs20-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs20-o2" role="option" aria-selected="false" data-v="EU (Frankfurt)" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[10px] text-[14.5px] text-tcs20-ink2 cursor-pointer transition-colors duration-150 data-active:bg-[oklch(1_0_0/0.08)] aria-selected:bg-[oklch(1_0_0/0.06)]"><span class="w-1.75 h-1.75 flex-none rounded-full bg-[oklch(1_0_0/0.35)] transition-[background-color,box-shadow] duration-150 group-aria-selected/opt:bg-tcs20-live group-aria-selected/opt:shadow-[0_0_8px_-1px_var(--color-tcs20-live)]" aria-hidden="true"></span>EU (Frankfurt)<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs20-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs20-o3" role="option" aria-selected="false" data-v="Asia Pacific (Tokyo)" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[10px] text-[14.5px] text-tcs20-ink2 cursor-pointer transition-colors duration-150 data-active:bg-[oklch(1_0_0/0.08)] aria-selected:bg-[oklch(1_0_0/0.06)]"><span class="w-1.75 h-1.75 flex-none rounded-full bg-[oklch(1_0_0/0.35)] transition-[background-color,box-shadow] duration-150 group-aria-selected/opt:bg-tcs20-live group-aria-selected/opt:shadow-[0_0_8px_-1px_var(--color-tcs20-live)]" aria-hidden="true"></span>Asia Pacific (Tokyo)<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs20-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
        <li id="tcs20-o4" role="option" aria-selected="false" data-v="South America (São Paulo)" class="group/opt flex items-center gap-2.75 min-h-11 px-3 rounded-[10px] text-[14.5px] text-tcs20-ink2 cursor-pointer transition-colors duration-150 data-active:bg-[oklch(1_0_0/0.08)] aria-selected:bg-[oklch(1_0_0/0.06)]"><span class="w-1.75 h-1.75 flex-none rounded-full bg-[oklch(1_0_0/0.35)] transition-[background-color,box-shadow] duration-150 group-aria-selected/opt:bg-tcs20-live group-aria-selected/opt:shadow-[0_0_8px_-1px_var(--color-tcs20-live)]" aria-hidden="true"></span>South America (São Paulo)<svg viewBox="0 0 24 24" aria-hidden="true" class="w-4.25 h-4.25 ml-auto fill-none stroke-tcs20-acc [stroke-width:2.4] [stroke-linecap:round] [stroke-linejoin:round] opacity-0 transition-opacity duration-150 group-aria-selected/opt:opacity-100"><path d="M5 12l5 5L20 7"/></svg></li>
      </ul>
    </div>
    <p data-live aria-live="polite" class="min-h-4 font-tcs20-mono text-[11px] text-tcs20-mut"></p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcs20-bg: #0a0714;
  --color-tcs20-bg: oklch(0.14 0.03 300);
  --color-tcs20-ink: #f2ecfb;
  --color-tcs20-ink: oklch(0.95 0.02 300);
  --color-tcs20-ink2: #e9e1f7;
  --color-tcs20-ink2: oklch(0.91 0.03 300);
  --color-tcs20-mut: #b9abd0;
  --color-tcs20-mut: oklch(0.75 0.05 300);
  --color-tcs20-acc: #c084fc;
  --color-tcs20-acc: oklch(0.75 0.18 303);
  --color-tcs20-live: #4ade80;
  --color-tcs20-live: oklch(0.82 0.19 148);
  --font-tcs20-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcs20-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tcs20: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tcs20-drift: tcs20-drift 16s ease-in-out infinite alternate;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tcs-20 {
  width: 100%;
  min-height: 100svh;
}
/* @keyframes have no utility form, and the -webkit- mask pair for the glass edge has no
   variant. Everything else in this demo — blur, translucency, inner highlight — is a utility. */

@keyframes tcs20-drift {
  0% {
    transform: translate(-4%, -3%) scale(1);
  }

  50% {
    transform: translate(5%, 4%) scale(1.12);
  }

  100% {
    transform: translate(-3%, 5%) scale(1.05);
  }
}

.tcs-20 [data-trigger]::before {
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tcs-20 [data-select]').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var trig = root.querySelector('[data-trigger]');
    var list = root.querySelector('[role="listbox"]');
    var opts = Array.prototype.slice.call(root.querySelectorAll('[role="option"]'));
    var live = root.closest('.tcs-20').querySelector('[data-live]');
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
  document.querySelectorAll('.tcs-20').forEach(function (root) {
    root.addEventListener('tcs:pick', function (e) {
      root.querySelector('[data-name]').textContent = e.detail.opt.dataset.v;
    });
  });
})();
```
