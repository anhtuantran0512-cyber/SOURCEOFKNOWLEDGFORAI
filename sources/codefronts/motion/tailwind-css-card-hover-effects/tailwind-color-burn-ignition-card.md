---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-color-burn-ignition-card/"
title: "Tailwind Color-Burn Ignition Card with Grayscale-to-Fire Hover"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A BBQ card that sits grey and dim until hover, then ignites: the grayscale filter releases, a color-burn fire layer rises from below, and screen-blended…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Color-Burn Ignition Card with Grayscale-to-Fire Hover
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-color-burn-ignition-card/

A BBQ card that sits grey and dim until hover, then ignites: the grayscale filter releases, a color-burn fire layer rises from below, and screen-blended embers fade in. Three stacked state changes on one trigger, all utilities.
## HTML
```html
<section class="tch-30 w-full min-h-svh grid place-items-center bg-tch30-bg font-tch30-sans p-8">
  <article tabindex="0" class="group relative w-[330px] h-[440px] rounded-[14px] overflow-hidden cursor-pointer outline-none bg-tch30-card grayscale-80 brightness-75 transition-[filter,box-shadow] duration-600 hover:grayscale-0 hover:brightness-100 hover:shadow-[0_0_60px_rgb(255_90_20/0.4)] focus-visible:grayscale-0 focus-visible:brightness-100 focus-visible:outline-3 focus-visible:outline-tch30-flame focus-visible:outline-offset-4 motion-reduce:transition-none">
    <div class="absolute inset-0 bg-[linear-gradient(160deg,#4a4a52,#1c1c20)]"></div>
    <div class="absolute inset-0 z-1 pointer-events-none opacity-0 translate-y-1/5 mix-blend-color-burn transition-[opacity,translate] duration-600 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 bg-[radial-gradient(circle_at_50%_100%,#ff7a18,#ff2d00_40%,#8a0e00_70%,transparent_90%)]"></div>
    <div class="absolute inset-0 z-2 pointer-events-none opacity-0 mix-blend-screen transition-opacity duration-600 delay-100 group-hover:opacity-70 group-focus-visible:opacity-70 bg-[radial-gradient(#ffcf6b_1px,transparent_1.5px),radial-gradient(#ff8a3c_1px,transparent_1.5px)] bg-[length:60px_60px,90px_90px] bg-[position:0_0,30px_40px]"></div>
    <div class="relative z-3 h-full p-[2.4rem] flex flex-col justify-between text-tch30-ink">
      <span class="text-[0.72rem] tracking-[0.25em] uppercase text-tch30-tag">BBQ · Texas Style</span>
      <h2 class="font-tch30-display font-extrabold text-[3.6rem] leading-[0.82] uppercase">Low &amp;<br>Slow</h2>
      <p class="text-[0.86rem] leading-[1.6] text-tch30-body">Sixteen hours over post oak. Hover to bring the coals back to life.</p>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch30-bg: #100804;
  --color-tch30-bg: oklch(0.14 0.02 45);
  --color-tch30-card: #1a1a1a;
  --color-tch30-card: oklch(0.2 0 0);
  --color-tch30-ink: #f3ece4;
  --color-tch30-ink: oklch(0.94 0.01 70);
  --color-tch30-body: #d8cabc;
  --color-tch30-body: oklch(0.84 0.02 70);
  --color-tch30-tag: #ffb27a;
  --color-tch30-tag: oklch(0.82 0.11 55);
  --color-tch30-flame: #ff5a14;
  --color-tch30-flame: oklch(0.68 0.2 42);
  --font-tch30-sans: 'Barlow', system-ui, sans-serif;
  --font-tch30-display: 'Big Shoulders Display', system-ui, sans-serif;
}

.tch-30 {
  width: 100%;
  min-height: 100svh;
}
```
