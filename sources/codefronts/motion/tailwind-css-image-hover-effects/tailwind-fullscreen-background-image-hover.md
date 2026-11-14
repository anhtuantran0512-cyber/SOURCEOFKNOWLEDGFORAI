---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-fullscreen-background-image-hover/"
title: "Tailwind Fullscreen Background Image Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "A nav where hovering an item swaps the whole viewport background &mdash; and the port replaces six class toggles with one attribute."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Fullscreen Background Image Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-fullscreen-background-image-hover/

A nav where hovering an item swaps the whole viewport background &mdash; and the port replaces six class toggles with one attribute. The stage carries data-active="3"; each panel reads it through group-data-[active=3]:opacity-100. The script sets one value and never touches a class list.
## HTML
```html
<section class="tih-17 group w-full min-h-svh relative overflow-hidden bg-tih17-bg font-tih17-sans" data-active="0" aria-label="Fullscreen background swap on hover demo">
  <div class="absolute inset-0 pointer-events-none" aria-hidden="true">
    <div class="absolute inset-0 opacity-0 scale-104 bg-linear-[135deg,oklch(0.1_0_0),oklch(0.17_0_0)] transition-[opacity,scale] duration-600 ease-tih17 group-data-[active=0]:opacity-100 group-data-[active=0]:scale-100 motion-reduce:duration-0"></div>
    <div class="absolute inset-0 opacity-0 scale-104 bg-[image:url('https://picsum.photos/seed/tih17-universe/1600/900'),linear-gradient(135deg,oklch(0.17_0.07_285),oklch(0.34_0.12_285),oklch(0.28_0.06_290))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-600 ease-tih17 group-data-[active=1]:opacity-100 group-data-[active=1]:scale-100 motion-reduce:duration-0"></div>
    <div class="absolute inset-0 opacity-0 scale-104 bg-[image:url('https://picsum.photos/seed/tih17-canopy/1600/900'),linear-gradient(135deg,oklch(0.2_0.04_190),oklch(0.42_0.09_165),oklch(0.6_0.13_163))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-600 ease-tih17 group-data-[active=2]:opacity-100 group-data-[active=2]:scale-100 motion-reduce:duration-0"></div>
    <div class="absolute inset-0 opacity-0 scale-104 bg-[image:url('https://picsum.photos/seed/tih17-dunes/1600/900'),linear-gradient(135deg,oklch(0.18_0.03_60),oklch(0.32_0.08_55),oklch(0.48_0.11_60))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-600 ease-tih17 group-data-[active=3]:opacity-100 group-data-[active=3]:scale-100 motion-reduce:duration-0"></div>
    <div class="absolute inset-0 opacity-0 scale-104 bg-[image:url('https://picsum.photos/seed/tih17-violet/1600/900'),linear-gradient(135deg,oklch(0.17_0.07_310),oklch(0.35_0.18_298),oklch(0.55_0.24_295))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-600 ease-tih17 group-data-[active=4]:opacity-100 group-data-[active=4]:scale-100 motion-reduce:duration-0"></div>
    <div class="absolute inset-0 opacity-0 scale-104 bg-[image:url('https://picsum.photos/seed/tih17-ocean/1600/900'),linear-gradient(135deg,oklch(0.17_0.08_265),oklch(0.33_0.14_262),oklch(0.5_0.2_260))] bg-cover bg-center bg-no-repeat transition-[opacity,scale] duration-600 ease-tih17 group-data-[active=5]:opacity-100 group-data-[active=5]:scale-100 motion-reduce:duration-0"></div>
  </div>
  <nav class="relative z-2 flex flex-col justify-center min-h-svh p-10" aria-label="Background preview">
    <p class="mb-5 text-[10px] font-bold tracking-[0.14em] uppercase text-tih17-muted">Navigate &middot; hover or focus to preview</p>
    <ul class="list-none flex flex-col gap-1">
      <li><a href="#deep-universe" data-target="1" class="group/link flex items-center gap-3 min-h-11 px-3 py-2.5 rounded-lg no-underline transition-colors duration-200 hover:bg-[oklch(1_0_0/0.06)] focus-visible:bg-[oklch(1_0_0/0.06)] focus-visible:outline-2 focus-visible:outline-tih17-acc focus-visible:outline-offset-2">
        <span class="w-5.5 shrink-0 text-[11px] font-semibold text-tih17-muted tabular-nums">01</span>
        <span class="text-sm" aria-hidden="true">&#127756;</span>
        <span class="text-xl font-extrabold tracking-[-0.02em] text-[oklch(1_0_0/0.25)] transition-[color,translate] duration-600 ease-tih17 group-hover/link:text-tih17-text group-hover/link:translate-x-1.5 group-focus-visible/link:text-tih17-text motion-reduce:transition-none">Deep Universe</span>
        <span class="ml-auto text-base text-tih17-acc opacity-0 -translate-x-2 transition-[opacity,translate] duration-200 group-hover/link:opacity-100 group-hover/link:translate-x-0 group-focus-visible/link:opacity-100 group-focus-visible/link:translate-x-0" aria-hidden="true">&rarr;</span>
      </a></li>
      <li><a href="#wild-canopy" data-target="2" class="group/link flex items-center gap-3 min-h-11 px-3 py-2.5 rounded-lg no-underline transition-colors duration-200 hover:bg-[oklch(1_0_0/0.06)] focus-visible:bg-[oklch(1_0_0/0.06)] focus-visible:outline-2 focus-visible:outline-tih17-acc focus-visible:outline-offset-2">
        <span class="w-5.5 shrink-0 text-[11px] font-semibold text-tih17-muted tabular-nums">02</span>
        <span class="text-sm" aria-hidden="true">&#127807;</span>
        <span class="text-xl font-extrabold tracking-[-0.02em] text-[oklch(1_0_0/0.25)] transition-[color,translate] duration-600 ease-tih17 group-hover/link:text-tih17-text group-hover/link:translate-x-1.5 group-focus-visible/link:text-tih17-text motion-reduce:transition-none">Wild Canopy</span>
        <span class="ml-auto text-base text-tih17-acc opacity-0 -translate-x-2 transition-[opacity,translate] duration-200 group-hover/link:opacity-100 group-hover/link:translate-x-0 group-focus-visible/link:opacity-100 group-focus-visible/link:translate-x-0" aria-hidden="true">&rarr;</span>
      </a></li>
      <li><a href="#desert-dunes" data-target="3" class="group/link flex items-center gap-3 min-h-11 px-3 py-2.5 rounded-lg no-underline transition-colors duration-200 hover:bg-[oklch(1_0_0/0.06)] focus-visible:bg-[oklch(1_0_0/0.06)] focus-visible:outline-2 focus-visible:outline-tih17-acc focus-visible:outline-offset-2">
        <span class="w-5.5 shrink-0 text-[11px] font-semibold text-tih17-muted tabular-nums">03</span>
        <span class="text-sm" aria-hidden="true">&#127964;</span>
        <span class="text-xl font-extrabold tracking-[-0.02em] text-[oklch(1_0_0/0.25)] transition-[color,translate] duration-600 ease-tih17 group-hover/link:text-tih17-text group-hover/link:translate-x-1.5 group-focus-visible/link:text-tih17-text motion-reduce:transition-none">Desert Dunes</span>
        <span class="ml-auto text-base text-tih17-acc opacity-0 -translate-x-2 transition-[opacity,translate] duration-200 group-hover/link:opacity-100 group-hover/link:translate-x-0 group-focus-visible/link:opacity-100 group-focus-visible/link:translate-x-0" aria-hidden="true">&rarr;</span>
      </a></li>
      <li><a href="#violet-dreams" data-target="4" class="group/link flex items-center gap-3 min-h-11 px-3 py-2.5 rounded-lg no-underline transition-colors duration-200 hover:bg-[oklch(1_0_0/0.06)] focus-visible:bg-[oklch(1_0_0/0.06)] focus-visible:outline-2 focus-visible:outline-tih17-acc focus-visible:outline-offset-2">
        <span class="w-5.5 shrink-0 text-[11px] font-semibold text-tih17-muted tabular-nums">04</span>
        <span class="text-sm" aria-hidden="true">&#128302;</span>
        <span class="text-xl font-extrabold tracking-[-0.02em] text-[oklch(1_0_0/0.25)] transition-[color,translate] duration-600 ease-tih17 group-hover/link:text-tih17-text group-hover/link:translate-x-1.5 group-focus-visible/link:text-tih17-text motion-reduce:transition-none">Violet Dreams</span>
        <span class="ml-auto text-base text-tih17-acc opacity-0 -translate-x-2 transition-[opacity,translate] duration-200 group-hover/link:opacity-100 group-hover/link:translate-x-0 group-focus-visible/link:opacity-100 group-focus-visible/link:translate-x-0" aria-hidden="true">&rarr;</span>
      </a></li>
      <li><a href="#ocean-horizon" data-target="5" class="group/link flex items-center gap-3 min-h-11 px-3 py-2.5 rounded-lg no-underline transition-colors duration-200 hover:bg-[oklch(1_0_0/0.06)] focus-visible:bg-[oklch(1_0_0/0.06)] focus-visible:outline-2 focus-visible:outline-tih17-acc focus-visible:outline-offset-2">
        <span class="w-5.5 shrink-0 text-[11px] font-semibold text-tih17-muted tabular-nums">05</span>
        <span class="text-sm" aria-hidden="true">&#127754;</span>
        <span class="text-xl font-extrabold tracking-[-0.02em] text-[oklch(1_0_0/0.25)] transition-[color,translate] duration-600 ease-tih17 group-hover/link:text-tih17-text group-hover/link:translate-x-1.5 group-focus-visible/link:text-tih17-text motion-reduce:transition-none">Ocean Horizon</span>
        <span class="ml-auto text-base text-tih17-acc opacity-0 -translate-x-2 transition-[opacity,translate] duration-200 group-hover/link:opacity-100 group-hover/link:translate-x-0 group-focus-visible/link:opacity-100 group-focus-visible/link:translate-x-0" aria-hidden="true">&rarr;</span>
      </a></li>
    </ul>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih17-bg: #06060a;
  --color-tih17-bg: oklch(0.1 0.008 285);
  --color-tih17-text: #f1f5f9;
  --color-tih17-text: oklch(0.96 0.005 250);
  --color-tih17-muted: #64748b;
  --color-tih17-muted: oklch(0.58 0.035 255);
  --color-tih17-acc: #f472b6;
  --color-tih17-acc: oklch(0.72 0.16 350);
  --font-tih17-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih17: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-17 {
  width: 100%;
  min-height: 100svh;
}

.tih-17 ::selection {
  background: oklch(0.72 0.16 350);
  color: #000;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tih-17').forEach(function (stage) {
    if (stage.dataset.bound) return; stage.dataset.bound = '1';
    function set(v) { stage.setAttribute('data-active', String(v)); }
    stage.querySelectorAll('a[data-target]').forEach(function (link) {
      link.addEventListener('pointerenter', function () { set(link.dataset.target); });
      link.addEventListener('pointerleave', function () { set(0); });
      link.addEventListener('focus', function () { set(link.dataset.target); });
      link.addEventListener('blur', function () { set(0); });
      link.addEventListener('click', function (e) { e.preventDefault(); });
    });
    document.addEventListener('touchstart', function (e) {
      if (!stage.contains(e.target)) set(0);
    }, { passive: true });
  });
})();
```
