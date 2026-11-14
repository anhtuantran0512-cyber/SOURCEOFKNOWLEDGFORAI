---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-master-toggle-indeterminate-tri-state/"
title: "Tailwind Master Toggle with Indeterminate Tri-State"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "What demo 13 could not do: a master switch that actually SETS the group, with a real third state."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Master Toggle with Indeterminate Tri-State
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-master-toggle-indeterminate-tri-state/

What demo 13 could not do: a master switch that actually SETS the group, with a real third state. When some children are on, the master goes indeterminate &mdash; a dash, not a thumb &mdash; using the native pseudo-class and aria-checked="mixed".
## HTML
```html
<section class="ttg-33 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg33-bg font-ttg33-sans" aria-label="Master toggle with indeterminate state">
  <div id="ttg-33-group" class="w-[min(390px,100%)] rounded-[20px] bg-white overflow-hidden border border-ttg33-hair shadow-[0_24px_50px_-34px_oklch(0.4_0.04_265/0.6)]">
    <label class="flex items-center gap-5 min-h-16 px-5 py-4 cursor-pointer bg-ttg33-headbg border-b border-ttg33-hair">
      <span class="flex-1 flex flex-col gap-0.5">
        <b class="text-[15.5px] font-bold text-ttg33-ink">All notifications</b>
        <small id="ttg-33-summary" class="text-[12px] text-ttg33-mute">2 of 3 enabled</small>
      </span>
      <input type="checkbox" id="ttg-33-master" role="switch" aria-checked="mixed" aria-label="All notifications" class="appearance-none shrink-0 w-13 h-7.5 rounded-full bg-ttg33-trackoff relative cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-6.5 before:h-6.5 before:rounded-full before:bg-white before:shadow-[0_2px_5px_oklch(0.3_0.03_265/0.35)] before:transition-transform before:duration-250 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] after:content-[''] after:absolute after:top-1/2 after:left-1/2 after:-mt-[1.5px] after:-ml-[7px] after:w-3.5 after:h-[3px] after:rounded-full after:bg-white after:opacity-0 after:transition-opacity after:duration-200 checked:bg-ttg33-on checked:before:translate-x-[22px] indeterminate:bg-ttg33-mixed indeterminate:before:translate-x-[11px] indeterminate:after:opacity-100 focus-visible:outline-3 focus-visible:outline-ttg33-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
    </label>
    <label class="flex items-center gap-5 min-h-15 px-5 py-3.5 cursor-pointer transition-colors duration-200 hover:bg-ttg33-tint has-checked:[&_.ttg33-t]:text-ttg33-ink">
      <span class="flex-1 flex flex-col gap-0.5">
        <b class="ttg33-t text-[14.5px] font-semibold text-ttg33-dim transition-colors duration-200">Direct messages</b>
        <small class="text-[12px] text-ttg33-mute">Push and email</small>
      </span>
      <input type="checkbox" role="switch" checked data-child aria-label="Direct messages" class="appearance-none shrink-0 w-11 h-6.5 rounded-full bg-ttg33-trackoff relative cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-[22px] before:h-[22px] before:rounded-full before:bg-white before:shadow-[0_2px_5px_oklch(0.3_0.03_265/0.3)] before:transition-transform before:duration-250 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg33-on checked:before:translate-x-[18px] focus-visible:outline-3 focus-visible:outline-ttg33-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
    </label>
    <label class="flex items-center gap-5 min-h-15 px-5 py-3.5 cursor-pointer border-t border-ttg33-hair transition-colors duration-200 hover:bg-ttg33-tint has-checked:[&_.ttg33-t]:text-ttg33-ink">
      <span class="flex-1 flex flex-col gap-0.5">
        <b class="ttg33-t text-[14.5px] font-semibold text-ttg33-dim transition-colors duration-200">Mentions</b>
        <small class="text-[12px] text-ttg33-mute">Only when someone @s you</small>
      </span>
      <input type="checkbox" role="switch" checked data-child aria-label="Mentions" class="appearance-none shrink-0 w-11 h-6.5 rounded-full bg-ttg33-trackoff relative cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-[22px] before:h-[22px] before:rounded-full before:bg-white before:shadow-[0_2px_5px_oklch(0.3_0.03_265/0.3)] before:transition-transform before:duration-250 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg33-on checked:before:translate-x-[18px] focus-visible:outline-3 focus-visible:outline-ttg33-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
    </label>
    <label class="flex items-center gap-5 min-h-15 px-5 py-3.5 cursor-pointer border-t border-ttg33-hair transition-colors duration-200 hover:bg-ttg33-tint has-checked:[&_.ttg33-t]:text-ttg33-ink">
      <span class="flex-1 flex flex-col gap-0.5">
        <b class="ttg33-t text-[14.5px] font-semibold text-ttg33-dim transition-colors duration-200">Product news</b>
        <small class="text-[12px] text-ttg33-mute">Monthly, at most</small>
      </span>
      <input type="checkbox" role="switch" data-child aria-label="Product news" class="appearance-none shrink-0 w-11 h-6.5 rounded-full bg-ttg33-trackoff relative cursor-pointer transition-colors duration-250 before:content-[''] before:absolute before:top-0.5 before:left-0.5 before:w-[22px] before:h-[22px] before:rounded-full before:bg-white before:shadow-[0_2px_5px_oklch(0.3_0.03_265/0.3)] before:transition-transform before:duration-250 before:ease-[cubic-bezier(0.25,0.9,0.3,1.1)] checked:bg-ttg33-on checked:before:translate-x-[18px] focus-visible:outline-3 focus-visible:outline-ttg33-focus focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:before:transition-none">
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg33-bg: #edeef4;
  --color-ttg33-bg: oklch(0.95 0.006 265);
  --color-ttg33-headbg: #f7f8fc;
  --color-ttg33-headbg: oklch(0.98 0.004 265);
  --color-ttg33-hair: #e8eaf1;
  --color-ttg33-hair: oklch(0.93 0.006 265);
  --color-ttg33-tint: #f8f9fc;
  --color-ttg33-tint: oklch(0.98 0.004 265);
  --color-ttg33-ink: #1f2532;
  --color-ttg33-ink: oklch(0.26 0.015 265);
  --color-ttg33-dim: #737b8d;
  --color-ttg33-dim: oklch(0.58 0.018 265);
  --color-ttg33-mute: #8f97a7;
  --color-ttg33-mute: oklch(0.65 0.015 265);
  --color-ttg33-trackoff: #dfe2ea;
  --color-ttg33-trackoff: oklch(0.9 0.008 265);
  --color-ttg33-on: #2f9e63;
  --color-ttg33-on: oklch(0.63 0.16 155);
  --color-ttg33-mixed: #4f74e8;
  --color-ttg33-mixed: oklch(0.58 0.17 265);
  --color-ttg33-focus: #3f63e0;
  --color-ttg33-focus: oklch(0.55 0.19 265);
  --font-ttg33-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-33 {
  width: 100%;
  min-height: 100svh;
}

.ttg-33 input[type="checkbox"] {
  -webkit-appearance: none;
}
/* The mixed dash sits on the thumb, so it needs the thumb's colour, not the track's. */

.ttg-33 #ttg-33-master:indeterminate::after {
  opacity: 1;
  background-color: var(--color-ttg33-mixed);
}
```

## JavaScript
```js
(() => {
  const group = document.querySelector('#ttg-33-group');
  const master = document.querySelector('#ttg-33-master');
  const summary = document.querySelector('#ttg-33-summary');
  if (!group || !master || !summary) return;
  const kids = () => [...group.querySelectorAll('input[data-child]')];

  const sync = () => {
    const all = kids();
    const on = all.filter((k) => k.checked).length;
    master.checked = on === all.length;
    master.indeterminate = on > 0 && on < all.length;
    // :indeterminate is invisible to assistive tech — mirror it.
    master.setAttribute('aria-checked', master.indeterminate ? 'mixed' : String(master.checked));
    summary.textContent = on + ' of ' + all.length + ' enabled';
  };

  master.addEventListener('change', () => {
    kids().forEach((k) => { k.checked = master.checked; });
    sync();
  });
  group.addEventListener('change', (e) => { if (e.target.matches('input[data-child]')) sync(); });
  sync();
})();
```
