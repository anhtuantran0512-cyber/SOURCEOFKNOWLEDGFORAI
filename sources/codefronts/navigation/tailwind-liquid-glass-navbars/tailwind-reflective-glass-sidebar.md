---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-reflective-glass-sidebar/"
title: "Tailwind Reflective Glass Sidebar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "A vertical glass sidebar that samples the colour of whatever panel is in view: scroll, and its tint, top glow and active accent shift as though the glass…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Reflective Glass Sidebar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-reflective-glass-sidebar/

A vertical glass sidebar that samples the colour of whatever panel is in view: scroll, and its tint, top glow and active accent shift as though the glass were picking up the light of the room behind it. The port keeps the reflected colour as a registered custom property, which is the one thing that makes the cross-fade smooth instead of a snap.
## HTML
```html
<section class="nbtw-18 relative flex w-full min-h-svh overflow-hidden font-nb18-sans bg-[#0a0c14]" aria-label="Reflective glass sidebar demo">
  <nav class="relative z-[5] flex flex-col items-center gap-2.5 w-[74px] py-4.5 overflow-hidden text-white bg-[color-mix(in_oklab,var(--nb18-reflect)_16%,rgba(255,255,255,.06))] border-e border-e-[color-mix(in_oklab,var(--nb18-reflect)_40%,rgba(255,255,255,.14))] shadow-[inset_0_1px_0_rgba(255,255,255,.3)] backdrop-blur-[24px] backdrop-saturate-[1.8] transition-[background-color,border-color] duration-500 motion-reduce:transition-none" id="nbtw-18-side" aria-label="Primary">
    <span class="absolute inset-x-0 top-0 h-30 pointer-events-none opacity-60 bg-[radial-gradient(60px_120px_at_50%_0,color-mix(in_oklab,var(--nb18-reflect)_80%,transparent),transparent_70%)] transition-[background] duration-500 motion-reduce:transition-none" aria-hidden="true"></span>
    <span class="relative z-[1] mb-2 text-[22px] text-[color-mix(in_oklab,var(--nb18-reflect)_60%,white)] transition-colors duration-500" aria-hidden="true">◈</span>
    <a class="relative z-[1] grid place-items-center size-[46px] rounded-[14px] no-underline text-white/80 text-[19px] transition-[background-color,color] duration-300 hover:bg-white/[0.12] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:text-white aria-[current=page]:bg-[color-mix(in_oklab,var(--nb18-reflect)_55%,transparent)] aria-[current=page]:shadow-[0_0_18px_-2px_color-mix(in_oklab,var(--nb18-reflect)_70%,transparent)]" href="#nbtw-18" aria-current="page" aria-label="Home">⌂</a>
    <a class="relative z-[1] grid place-items-center size-[46px] rounded-[14px] no-underline text-white/80 text-[19px] transition-[background-color,color] duration-300 hover:bg-white/[0.12] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-18" aria-label="Discover">◎</a>
    <a class="relative z-[1] grid place-items-center size-[46px] rounded-[14px] no-underline text-white/80 text-[19px] transition-[background-color,color] duration-300 hover:bg-white/[0.12] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-18" aria-label="Media">▤</a>
    <a class="relative z-[1] grid place-items-center size-[46px] rounded-[14px] no-underline text-white/80 text-[19px] transition-[background-color,color] duration-300 hover:bg-white/[0.12] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-18" aria-label="Settings">⚙</a>
  </nav>
  <div class="flex-1 h-svh overflow-y-auto snap-y snap-mandatory" id="nbtw-18-scroll">
    <div class="h-svh min-h-130 snap-start grid place-items-center bg-[radial-gradient(circle_at_50%_40%,color-mix(in_oklab,#5b8cff_55%,#0a0c14),#0a0c14_75%)]" data-color="#5b8cff"><h3 class="text-white text-[32px] font-extrabold tracking-[-0.02em] [text-shadow:0_2px_20px_rgba(0,0,0,.4)]">Ocean</h3></div>
    <div class="h-svh min-h-130 snap-start grid place-items-center bg-[radial-gradient(circle_at_50%_40%,color-mix(in_oklab,#ff5ea8_55%,#0a0c14),#0a0c14_75%)]" data-color="#ff5ea8"><h3 class="text-white text-[32px] font-extrabold tracking-[-0.02em] [text-shadow:0_2px_20px_rgba(0,0,0,.4)]">Bloom</h3></div>
    <div class="h-svh min-h-130 snap-start grid place-items-center bg-[radial-gradient(circle_at_50%_40%,color-mix(in_oklab,#38e8c6_55%,#0a0c14),#0a0c14_75%)]" data-color="#38e8c6"><h3 class="text-white text-[32px] font-extrabold tracking-[-0.02em] [text-shadow:0_2px_20px_rgba(0,0,0,.4)]">Mint</h3></div>
    <div class="h-svh min-h-130 snap-start grid place-items-center bg-[radial-gradient(circle_at_50%_40%,color-mix(in_oklab,#ffb03a_55%,#0a0c14),#0a0c14_75%)]" data-color="#ffb03a"><h3 class="text-white text-[32px] font-extrabold tracking-[-0.02em] [text-shadow:0_2px_20px_rgba(0,0,0,.4)]">Amber</h3></div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb18-sans: system-ui, 'Segoe UI', sans-serif;
}
/* The load-bearing rule of this demo. An unregistered custom property holding
   a colour is an untyped string: a new value swaps instantly and no transition
   can catch it. Registered as <color>, the browser interpolates. */

@property --nb18-reflect {
  syntax: '<color>';
  inherits: true;
  initial-value: #5b8cff;
}
```

## JavaScript
```js
(() => {
  const side = document.querySelector('#nbtw-18-side');
  const scroll = document.querySelector('#nbtw-18-scroll');
  if (!side || !scroll) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) side.style.setProperty('--nb18-reflect', e.target.dataset.color);
    });
  }, { root: scroll, threshold: 0.6 });
  scroll.querySelectorAll('[data-color]').forEach((p) => io.observe(p));
})();
```
