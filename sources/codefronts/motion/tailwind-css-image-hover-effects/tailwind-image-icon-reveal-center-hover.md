---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-icon-reveal-center-hover/"
title: "Tailwind Image Icon Reveal Center Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "The artwork darkens and an action button pops in at the centre, spinning up from scale-50 -rotate-20 to rest."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Icon Reveal Center Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-icon-reveal-center-hover/

The artwork darkens and an action button pops in at the centre, spinning up from scale-50 -rotate-20 to rest. In v4 those are two individual properties, which quietly removes the CSS version's biggest footgun: transform function order no longer matters, because there is no shorthand to order.
## HTML
```html
<section class="tih-19 w-full min-h-svh grid place-items-center bg-tih19-bg font-tih19-sans px-6 py-10" aria-label="Centre icon reveal hover demo">
  <div class="grid w-full max-w-195 gap-3 grid-cols-2 sm:grid-cols-3">
    <article class="group relative overflow-hidden rounded-[10px] aspect-[4/3]">
      <div class="absolute inset-0 bg-[image:url('https://picsum.photos/seed/tih19-reel/800/600'),linear-gradient(135deg,oklch(0.17_0.07_285),oklch(0.31_0.14_280),oklch(0.45_0.19_275))] bg-cover bg-center bg-no-repeat transition-[filter,scale] duration-380 ease-tih19 group-hover:brightness-40 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="absolute inset-0 grid place-items-center opacity-0 scale-50 -rotate-20 transition-[opacity,scale,rotate] duration-380 ease-tih19 group-hover:opacity-100 group-hover:scale-100 group-hover:rotate-0 focus-within:opacity-100 focus-within:scale-100 focus-within:rotate-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:scale-100 motion-reduce:rotate-0">
        <button type="button" class="grid place-items-center w-13 h-13 rounded-full text-[22px] text-white bg-[oklch(1_0_0/0.12)] border-2 border-[oklch(1_0_0/0.25)] backdrop-blur-md cursor-pointer transition-[background,scale] duration-200 hover:bg-[oklch(1_0_0/0.22)] hover:scale-110 focus-visible:outline-2 focus-visible:outline-tih19-acc focus-visible:outline-offset-2 motion-reduce:transition-none" aria-label="Play Intro Reel 2026">&#9654;</button>
      </div>
      <div class="absolute inset-x-0 bottom-0 flex items-center justify-between px-2.5 py-2 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <span class="text-[11px] font-bold text-tih19-text">Intro Reel 2026</span>
        <span class="text-[10px] text-tih19-muted tabular-nums">4.2k views</span>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[10px] aspect-[4/3]">
      <div class="absolute inset-0 bg-[image:url('https://picsum.photos/seed/tih19-jungle/800/600'),linear-gradient(135deg,oklch(0.2_0.04_190),oklch(0.42_0.09_165),oklch(0.6_0.13_163))] bg-cover bg-center bg-no-repeat transition-[filter,scale] duration-380 ease-tih19 group-hover:brightness-40 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="absolute inset-0 grid place-items-center opacity-0 scale-50 -rotate-20 transition-[opacity,scale,rotate] duration-380 ease-tih19 group-hover:opacity-100 group-hover:scale-100 group-hover:rotate-0 focus-within:opacity-100 focus-within:scale-100 focus-within:rotate-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:scale-100 motion-reduce:rotate-0">
        <button type="button" class="grid place-items-center w-13 h-13 rounded-full text-[22px] text-white bg-[oklch(1_0_0/0.12)] border-2 border-[oklch(1_0_0/0.25)] backdrop-blur-md cursor-pointer transition-[background,scale] duration-200 hover:bg-[oklch(1_0_0/0.22)] hover:scale-110 focus-visible:outline-2 focus-visible:outline-tih19-acc focus-visible:outline-offset-2 motion-reduce:transition-none" aria-label="Zoom Jungle Macro">&#128269;</button>
      </div>
      <div class="absolute inset-x-0 bottom-0 flex items-center justify-between px-2.5 py-2 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <span class="text-[11px] font-bold text-tih19-text">Jungle Macro</span>
        <span class="text-[10px] text-tih19-muted tabular-nums">1.8k views</span>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[10px] aspect-[4/3]">
      <div class="absolute inset-0 bg-[image:url('https://picsum.photos/seed/tih19-prism/800/600'),linear-gradient(135deg,oklch(0.25_0.13_305),oklch(0.45_0.22_300),oklch(0.63_0.21_300))] bg-cover bg-center bg-no-repeat transition-[filter,scale] duration-380 ease-tih19 group-hover:brightness-40 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="absolute inset-0 grid place-items-center opacity-0 scale-50 -rotate-20 transition-[opacity,scale,rotate] duration-380 ease-tih19 group-hover:opacity-100 group-hover:scale-100 group-hover:rotate-0 focus-within:opacity-100 focus-within:scale-100 focus-within:rotate-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:scale-100 motion-reduce:rotate-0">
        <button type="button" class="grid place-items-center w-13 h-13 rounded-full text-[22px] text-white bg-[oklch(1_0_0/0.12)] border-2 border-[oklch(1_0_0/0.25)] backdrop-blur-md cursor-pointer transition-[background,scale] duration-200 hover:bg-[oklch(1_0_0/0.22)] hover:scale-110 focus-visible:outline-2 focus-visible:outline-tih19-acc focus-visible:outline-offset-2 motion-reduce:transition-none" aria-label="Open Prism Study">&#128279;</button>
      </div>
      <div class="absolute inset-x-0 bottom-0 flex items-center justify-between px-2.5 py-2 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <span class="text-[11px] font-bold text-tih19-text">Prism Study</span>
        <span class="text-[10px] text-tih19-muted tabular-nums">9.1k views</span>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[10px] aspect-[4/3]">
      <div class="absolute inset-0 bg-[image:url('https://picsum.photos/seed/tih19-golden/800/600'),linear-gradient(135deg,oklch(0.18_0.03_60),oklch(0.45_0.11_60),oklch(0.65_0.14_65))] bg-cover bg-center bg-no-repeat transition-[filter,scale] duration-380 ease-tih19 group-hover:brightness-40 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="absolute inset-0 grid place-items-center opacity-0 scale-50 -rotate-20 transition-[opacity,scale,rotate] duration-380 ease-tih19 group-hover:opacity-100 group-hover:scale-100 group-hover:rotate-0 focus-within:opacity-100 focus-within:scale-100 focus-within:rotate-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:scale-100 motion-reduce:rotate-0">
        <button type="button" class="grid place-items-center w-13 h-13 rounded-full text-[22px] text-white bg-[oklch(1_0_0/0.12)] border-2 border-[oklch(1_0_0/0.25)] backdrop-blur-md cursor-pointer transition-[background,scale] duration-200 hover:bg-[oklch(1_0_0/0.22)] hover:scale-110 focus-visible:outline-2 focus-visible:outline-tih19-acc focus-visible:outline-offset-2 motion-reduce:transition-none" aria-label="Play Golden Hour BTS">&#9654;</button>
      </div>
      <div class="absolute inset-x-0 bottom-0 flex items-center justify-between px-2.5 py-2 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <span class="text-[11px] font-bold text-tih19-text">Golden Hour BTS</span>
        <span class="text-[10px] text-tih19-muted tabular-nums">3.3k views</span>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[10px] aspect-[4/3]">
      <div class="absolute inset-0 bg-[image:url('https://picsum.photos/seed/tih19-blue/800/600'),linear-gradient(135deg,oklch(0.17_0.08_265),oklch(0.33_0.14_262),oklch(0.55_0.2_260))] bg-cover bg-center bg-no-repeat transition-[filter,scale] duration-380 ease-tih19 group-hover:brightness-40 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="absolute inset-0 grid place-items-center opacity-0 scale-50 -rotate-20 transition-[opacity,scale,rotate] duration-380 ease-tih19 group-hover:opacity-100 group-hover:scale-100 group-hover:rotate-0 focus-within:opacity-100 focus-within:scale-100 focus-within:rotate-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:scale-100 motion-reduce:rotate-0">
        <button type="button" class="grid place-items-center w-13 h-13 rounded-full text-[22px] text-white bg-[oklch(1_0_0/0.12)] border-2 border-[oklch(1_0_0/0.25)] backdrop-blur-md cursor-pointer transition-[background,scale] duration-200 hover:bg-[oklch(1_0_0/0.22)] hover:scale-110 focus-visible:outline-2 focus-visible:outline-tih19-acc focus-visible:outline-offset-2 motion-reduce:transition-none" aria-label="Zoom Deep Blue Series">&#128269;</button>
      </div>
      <div class="absolute inset-x-0 bottom-0 flex items-center justify-between px-2.5 py-2 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <span class="text-[11px] font-bold text-tih19-text">Deep Blue Series</span>
        <span class="text-[10px] text-tih19-muted tabular-nums">7.6k views</span>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[10px] aspect-[4/3]">
      <div class="absolute inset-0 bg-[image:url('https://picsum.photos/seed/tih19-bloom/800/600'),linear-gradient(135deg,oklch(0.16_0.06_350),oklch(0.4_0.18_5),oklch(0.6_0.22_15))] bg-cover bg-center bg-no-repeat transition-[filter,scale] duration-380 ease-tih19 group-hover:brightness-40 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="absolute inset-0 grid place-items-center opacity-0 scale-50 -rotate-20 transition-[opacity,scale,rotate] duration-380 ease-tih19 group-hover:opacity-100 group-hover:scale-100 group-hover:rotate-0 focus-within:opacity-100 focus-within:scale-100 focus-within:rotate-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:scale-100 motion-reduce:rotate-0">
        <button type="button" class="grid place-items-center w-13 h-13 rounded-full text-[22px] text-white bg-[oklch(1_0_0/0.12)] border-2 border-[oklch(1_0_0/0.25)] backdrop-blur-md cursor-pointer transition-[background,scale] duration-200 hover:bg-[oklch(1_0_0/0.22)] hover:scale-110 focus-visible:outline-2 focus-visible:outline-tih19-acc focus-visible:outline-offset-2 motion-reduce:transition-none" aria-label="Open Bloom Editorial">&#128279;</button>
      </div>
      <div class="absolute inset-x-0 bottom-0 flex items-center justify-between px-2.5 py-2 bg-linear-[to_top,oklch(0_0_0/0.8),transparent]">
        <span class="text-[11px] font-bold text-tih19-text">Bloom Editorial</span>
        <span class="text-[10px] text-tih19-muted tabular-nums">2.9k views</span>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih19-bg: #07070e;
  --color-tih19-bg: oklch(0.11 0.012 285);
  --color-tih19-text: #f1f5f9;
  --color-tih19-text: oklch(0.96 0.005 250);
  --color-tih19-muted: #475569;
  --color-tih19-muted: oklch(0.68 0.02 255);
  --color-tih19-acc: #818cf8;
  --color-tih19-acc: oklch(0.7 0.15 275);
  --font-tih19-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih19: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-19 {
  width: 100%;
  min-height: 100svh;
}

.tih-19 ::selection {
  background: oklch(0.7 0.15 275);
  color: #fff;
}
```
