---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-modals/tailwind-tabbed-settings-modal-zero-js-radio-tabs/"
title: "Tailwind Tabbed Settings Modal with Zero-JS Radio Tabs"
section: "components"
category: "tailwind-css-modals"
category_name: "Tailwind CSS Modals"
description: "A preferences dialog with a vertical nav and three panels, switched entirely by radios: no tab controller, no aria-selected bookkeeping."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tabbed Settings Modal with Zero-JS Radio Tabs
Source: https://codefronts.com/components/tailwind-css-modals/tailwind-tabbed-settings-modal-zero-js-radio-tabs/

A preferences dialog with a vertical nav and three panels, switched entirely by radios: no tab controller, no aria-selected bookkeeping. group-has-[#tm-17-appear:checked]: selects both the active nav item and its panel, from the class list of each.
## HTML
```html
<section class="tm-17 w-full min-h-svh grid place-items-center bg-tm17-bg font-tm17-sans px-6 py-10">
  <button type="button" data-tm17-open class="inline-flex items-center gap-2.5 min-h-11 px-6 rounded-xl text-sm font-semibold text-tm17-ink bg-tm17-btn border border-tm17-edge cursor-pointer transition-colors duration-200 hover:bg-tm17-btnhover hover:border-tm17-acc focus-visible:outline-2 focus-visible:outline-tm17-acc focus-visible:outline-offset-2"><span aria-hidden="true">⚙</span> Settings</button>

  <dialog id="tm-17-dlg" aria-labelledby="tm-17-title" class="m-auto w-[min(620px,94vw)] max-h-[90dvh] overflow-hidden p-0 border-0 rounded-[18px] text-tm17-ink bg-tm17-card shadow-[0_40px_90px_-30px_#000,0_0_0_1px_var(--color-tm17-edge)] opacity-0 scale-[0.97] transition-[opacity,translate,scale,overlay,display] duration-[260ms] transition-discrete open:opacity-100 open:scale-100 open:starting:opacity-0 open:starting:scale-[0.97] open:backdrop:bg-tm17-scrim open:backdrop:backdrop-blur-[5px] motion-reduce:transition-none">
    <div data-tm17-card class="group relative grid grid-cols-[190px_1fr] min-h-[420px] max-[540px]:grid-cols-1">
      <input type="radio" name="tm-17-tab" id="tm-17-account" checked class="peer/account sr-only">
      <input type="radio" name="tm-17-tab" id="tm-17-appear" class="peer/appear sr-only">
      <input type="radio" name="tm-17-tab" id="tm-17-notif" class="peer/notif sr-only">

      <button type="button" data-tm17-close aria-label="Close settings" class="absolute top-2.5 right-3 z-[3] grid place-items-center size-11 rounded-lg border-0 bg-transparent text-tm17-mut text-[22px] leading-none cursor-pointer transition-colors duration-200 hover:bg-tm17-btnhover hover:text-white focus-visible:outline-2 focus-visible:outline-tm17-acc focus-visible:outline-offset-2">&times;</button>

      <nav aria-label="Settings sections" class="flex flex-col gap-1 px-3.5 py-6 bg-tm17-nav border-r border-tm17-edge max-[540px]:flex-row max-[540px]:overflow-auto max-[540px]:border-r-0 max-[540px]:border-b max-[540px]:py-3">
        <h2 id="tm-17-title" class="px-3 mb-3.5 text-[13px] uppercase tracking-[0.16em] text-tm17-faint max-[540px]:hidden">Settings</h2>
        <label for="tm-17-account" class="flex items-center gap-2.5 min-h-11 px-3 rounded-[9px] text-sm font-semibold text-tm17-mut cursor-pointer whitespace-nowrap transition-colors duration-200 hover:bg-tm17-btn hover:text-tm17-hi group-has-[#tm-17-account:checked]:bg-tm17-acctint group-has-[#tm-17-account:checked]:text-white group-has-[#tm-17-account:focus-visible]:outline-2 group-has-[#tm-17-account:focus-visible]:outline-tm17-acc group-has-[#tm-17-account:focus-visible]:-outline-offset-2"><span aria-hidden="true">👤</span> Account</label>
        <label for="tm-17-appear" class="flex items-center gap-2.5 min-h-11 px-3 rounded-[9px] text-sm font-semibold text-tm17-mut cursor-pointer whitespace-nowrap transition-colors duration-200 hover:bg-tm17-btn hover:text-tm17-hi group-has-[#tm-17-appear:checked]:bg-tm17-acctint group-has-[#tm-17-appear:checked]:text-white group-has-[#tm-17-appear:focus-visible]:outline-2 group-has-[#tm-17-appear:focus-visible]:outline-tm17-acc group-has-[#tm-17-appear:focus-visible]:-outline-offset-2"><span aria-hidden="true">🎨</span> Appearance</label>
        <label for="tm-17-notif" class="flex items-center gap-2.5 min-h-11 px-3 rounded-[9px] text-sm font-semibold text-tm17-mut cursor-pointer whitespace-nowrap transition-colors duration-200 hover:bg-tm17-btn hover:text-tm17-hi group-has-[#tm-17-notif:checked]:bg-tm17-acctint group-has-[#tm-17-notif:checked]:text-white group-has-[#tm-17-notif:focus-visible]:outline-2 group-has-[#tm-17-notif:focus-visible]:outline-tm17-acc group-has-[#tm-17-notif:focus-visible]:-outline-offset-2"><span aria-hidden="true">🔔</span> Notifications</label>
      </nav>

      <div class="overflow-auto px-7 py-7">
        <section class="hidden group-has-[#tm-17-account:checked]:block animate-tm17-fade motion-reduce:animate-none">
          <h3 class="mb-5 text-lg font-bold text-tm17-hi">Account</h3>
          <div class="flex flex-col gap-1.5 mb-4">
            <label for="tm-17-dn" class="text-[12.5px] font-semibold text-tm17-mut">Display name</label>
            <input id="tm-17-dn" type="text" value="Alex Rivera" class="w-full min-h-11 px-3.5 rounded-[10px] border border-tm17-edge bg-tm17-well text-sm text-tm17-hi transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm17-acc focus:shadow-[0_0_0_3px_var(--color-tm17-ring)]">
          </div>
          <div class="flex flex-col gap-1.5 mb-4">
            <label for="tm-17-em" class="text-[12.5px] font-semibold text-tm17-mut">Email</label>
            <input id="tm-17-em" type="email" value="[email protected]" class="w-full min-h-11 px-3.5 rounded-[10px] border border-tm17-edge bg-tm17-well text-sm text-tm17-hi transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm17-acc focus:shadow-[0_0_0_3px_var(--color-tm17-ring)]">
          </div>
          <div class="flex flex-col gap-1.5">
            <label for="tm-17-tz" class="text-[12.5px] font-semibold text-tm17-mut">Time zone</label>
            <select id="tm-17-tz" class="w-full min-h-11 px-3 rounded-[10px] border border-tm17-edge bg-tm17-well text-sm text-tm17-hi cursor-pointer transition-[border-color,box-shadow] duration-200 focus:outline-none focus:border-tm17-acc focus:shadow-[0_0_0_3px_var(--color-tm17-ring)]">
              <option>GMT−05:00 · New York</option><option>GMT+00:00 · London</option><option>GMT+05:30 · Mumbai</option>
            </select>
          </div>
        </section>

        <section class="hidden group-has-[#tm-17-appear:checked]:block animate-tm17-fade motion-reduce:animate-none">
          <h3 class="mb-5 text-lg font-bold text-tm17-hi">Appearance</h3>
          <p class="mb-3 text-[12.5px] font-semibold text-tm17-mut">Theme</p>
          <div class="flex gap-3 mb-6">
            <label class="relative flex-1 flex flex-col items-center gap-2 px-2 py-3.5 rounded-xl border border-tm17-edge bg-tm17-well text-[13px] font-semibold text-tm17-mut cursor-pointer transition-colors duration-200 has-checked:border-tm17-acc has-checked:text-white has-checked:bg-tm17-acctint has-focus-visible:outline-2 has-focus-visible:outline-tm17-acc has-focus-visible:outline-offset-2"><input type="radio" name="tm-17-th" checked class="sr-only"><span class="w-full h-8 rounded-lg border border-tm17-swedge bg-[#15131f]"></span>Dark</label>
            <label class="relative flex-1 flex flex-col items-center gap-2 px-2 py-3.5 rounded-xl border border-tm17-edge bg-tm17-well text-[13px] font-semibold text-tm17-mut cursor-pointer transition-colors duration-200 has-checked:border-tm17-acc has-checked:text-white has-checked:bg-tm17-acctint has-focus-visible:outline-2 has-focus-visible:outline-tm17-acc has-focus-visible:outline-offset-2"><input type="radio" name="tm-17-th" class="sr-only"><span class="w-full h-8 rounded-lg border border-tm17-swedge bg-[#e8e6f0]"></span>Light</label>
            <label class="relative flex-1 flex flex-col items-center gap-2 px-2 py-3.5 rounded-xl border border-tm17-edge bg-tm17-well text-[13px] font-semibold text-tm17-mut cursor-pointer transition-colors duration-200 has-checked:border-tm17-acc has-checked:text-white has-checked:bg-tm17-acctint has-focus-visible:outline-2 has-focus-visible:outline-tm17-acc has-focus-visible:outline-offset-2"><input type="radio" name="tm-17-th" class="sr-only"><span class="w-full h-8 rounded-lg border border-tm17-swedge bg-[linear-gradient(90deg,#15131f_50%,#e8e6f0_50%)]"></span>System</label>
          </div>
          <label class="flex items-center justify-between gap-4 py-3.5 border-t border-tm17-edgesoft cursor-pointer">
            <span class="text-sm text-tm17-ink">Reduce motion</span>
            <input type="checkbox" class="shrink-0 relative w-11 h-6 appearance-none rounded-full bg-tm17-off cursor-pointer transition-colors duration-200 checked:bg-tm17-acc before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:size-[18px] before:rounded-full before:bg-tm17-knob before:transition-transform before:duration-200 checked:before:translate-x-5 checked:before:bg-white focus-visible:outline-2 focus-visible:outline-tm17-acc focus-visible:outline-offset-2 motion-reduce:before:transition-none">
          </label>
          <label class="flex items-center justify-between gap-4 py-3.5 border-t border-tm17-edgesoft cursor-pointer">
            <span class="text-sm text-tm17-ink">Compact density</span>
            <input type="checkbox" checked class="shrink-0 relative w-11 h-6 appearance-none rounded-full bg-tm17-off cursor-pointer transition-colors duration-200 checked:bg-tm17-acc before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:size-[18px] before:rounded-full before:bg-tm17-knob before:transition-transform before:duration-200 checked:before:translate-x-5 checked:before:bg-white focus-visible:outline-2 focus-visible:outline-tm17-acc focus-visible:outline-offset-2 motion-reduce:before:transition-none">
          </label>
        </section>

        <section class="hidden group-has-[#tm-17-notif:checked]:block animate-tm17-fade motion-reduce:animate-none">
          <h3 class="mb-5 text-lg font-bold text-tm17-hi">Notifications</h3>
          <label class="flex items-center justify-between gap-4 py-3.5 border-t border-tm17-edgesoft cursor-pointer">
            <span class="flex flex-col gap-0.5"><b class="text-sm font-semibold text-tm17-ink">Product updates</b><small class="text-xs text-tm17-faint">New features &amp; releases</small></span>
            <input type="checkbox" checked class="shrink-0 relative w-11 h-6 appearance-none rounded-full bg-tm17-off cursor-pointer transition-colors duration-200 checked:bg-tm17-acc before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:size-[18px] before:rounded-full before:bg-tm17-knob before:transition-transform before:duration-200 checked:before:translate-x-5 checked:before:bg-white focus-visible:outline-2 focus-visible:outline-tm17-acc focus-visible:outline-offset-2 motion-reduce:before:transition-none">
          </label>
          <label class="flex items-center justify-between gap-4 py-3.5 border-t border-tm17-edgesoft cursor-pointer">
            <span class="flex flex-col gap-0.5"><b class="text-sm font-semibold text-tm17-ink">Mentions &amp; replies</b><small class="text-xs text-tm17-faint">When someone tags you</small></span>
            <input type="checkbox" checked class="shrink-0 relative w-11 h-6 appearance-none rounded-full bg-tm17-off cursor-pointer transition-colors duration-200 checked:bg-tm17-acc before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:size-[18px] before:rounded-full before:bg-tm17-knob before:transition-transform before:duration-200 checked:before:translate-x-5 checked:before:bg-white focus-visible:outline-2 focus-visible:outline-tm17-acc focus-visible:outline-offset-2 motion-reduce:before:transition-none">
          </label>
          <label class="flex items-center justify-between gap-4 py-3.5 border-t border-tm17-edgesoft cursor-pointer">
            <span class="flex flex-col gap-0.5"><b class="text-sm font-semibold text-tm17-ink">Weekly digest</b><small class="text-xs text-tm17-faint">A Monday summary email</small></span>
            <input type="checkbox" class="shrink-0 relative w-11 h-6 appearance-none rounded-full bg-tm17-off cursor-pointer transition-colors duration-200 checked:bg-tm17-acc before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:size-[18px] before:rounded-full before:bg-tm17-knob before:transition-transform before:duration-200 checked:before:translate-x-5 checked:before:bg-white focus-visible:outline-2 focus-visible:outline-tm17-acc focus-visible:outline-offset-2 motion-reduce:before:transition-none">
          </label>
          <label class="flex items-center justify-between gap-4 py-3.5 border-t border-tm17-edgesoft cursor-pointer">
            <span class="flex flex-col gap-0.5"><b class="text-sm font-semibold text-tm17-ink">Marketing</b><small class="text-xs text-tm17-faint">Occasional offers</small></span>
            <input type="checkbox" class="shrink-0 relative w-11 h-6 appearance-none rounded-full bg-tm17-off cursor-pointer transition-colors duration-200 checked:bg-tm17-acc before:content-[''] before:absolute before:top-[3px] before:left-[3px] before:size-[18px] before:rounded-full before:bg-tm17-knob before:transition-transform before:duration-200 checked:before:translate-x-5 checked:before:bg-white focus-visible:outline-2 focus-visible:outline-tm17-acc focus-visible:outline-offset-2 motion-reduce:before:transition-none">
          </label>
        </section>
      </div>
    </div>
  </dialog>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tm17-bg: #08070b;
  --color-tm17-bg: oklch(0.14 0.012 290);
  --color-tm17-card: #14121e;
  --color-tm17-card: oklch(0.2 0.02 290);
  --color-tm17-nav: #100e1a;
  --color-tm17-nav: oklch(0.18 0.02 290);
  --color-tm17-well: #0d0b16;
  --color-tm17-well: oklch(0.16 0.018 290);
  --color-tm17-btn: #191627;
  --color-tm17-btn: oklch(0.22 0.025 290);
  --color-tm17-btnhover: #221d33;
  --color-tm17-btnhover: oklch(0.26 0.032 290);
  --color-tm17-edge: #2c2842;
  --color-tm17-edge: oklch(0.3 0.03 290);
  --color-tm17-edgesoft: #211d33;
  --color-tm17-edgesoft: oklch(0.25 0.025 290);
  --color-tm17-swedge: #3a3556;
  --color-tm17-swedge: oklch(0.36 0.04 290);
  --color-tm17-off: #2c2842;
  --color-tm17-off: oklch(0.3 0.03 290);
  --color-tm17-knob: #9a94b8;
  --color-tm17-knob: oklch(0.68 0.03 290);
  --color-tm17-hi: #f2eefb;
  --color-tm17-hi: oklch(0.95 0.01 290);
  --color-tm17-ink: #ddd9ec;
  --color-tm17-ink: oklch(0.89 0.018 290);
  --color-tm17-mut: #aba5c6;
  --color-tm17-mut: oklch(0.74 0.03 290);
  --color-tm17-faint: #8d87ab;
  --color-tm17-faint: oklch(0.63 0.035 290);
  --color-tm17-acc: #a78bfa;
  --color-tm17-acc: oklch(0.74 0.15 292);
  --color-tm17-acctint: #34285c;
  --color-tm17-acctint: oklch(0.34 0.09 292);
  --color-tm17-ring: #a78bfa3d;
  --color-tm17-ring: oklch(0.74 0.15 292 / 0.24);
  --color-tm17-scrim: #060509a3;
  --color-tm17-scrim: oklch(0.12 0.01 290 / 0.64);
  --font-tm17-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tm17-fade: tm17-fade .25s ease;
}

.tm-17 {
  width: 100%;
}

@keyframes tm17-fade {
  from {
    opacity: 0;
    transform: translateY(6px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

#tm-17-dlg::backdrop {
  background: oklch(0.12 0.01 290 / 0);
  backdrop-filter: blur(0px);
  transition: background .3s, backdrop-filter .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}

@starting-style {
  #tm-17-dlg[open]::backdrop {
    background: oklch(0.12 0.01 290 / 0);
    backdrop-filter: blur(0px);
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.tm-17');
  var dlg = root.querySelector('#tm-17-dlg');
  var card = root.querySelector('[data-tm17-card]');
  root.querySelector('[data-tm17-open]').addEventListener('click', function () { dlg.showModal(); });
  root.querySelector('[data-tm17-close]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) {
    var r = card.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dlg.close();
  });
})();
```
