---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-holographic-foil-shimmer-card/"
title: "Tailwind Holographic Foil Shimmer Card with mix-blend-mode"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A collectible trading card with a colour-dodge foil sweep, sparkle grain and a light 3D tilt."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Holographic Foil Shimmer Card with mix-blend-mode
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-holographic-foil-shimmer-card/

A collectible trading card with a colour-dodge foil sweep, sparkle grain and a light 3D tilt. mix-blend-mode is a first-class utility here (mix-blend-color-dodge), so the port's only stylesheet residue is the sweep keyframes &mdash; exposed back as animate-tch10-sweep.
## HTML
```html
<section class="tch-10 w-full min-h-svh grid place-items-center bg-tch10-bg font-tch10-sans p-8 [perspective:1200px]">
  <article tabindex="0" class="group relative w-[320px] h-[450px] rounded-[18px] overflow-hidden cursor-pointer outline-none transform-3d bg-[linear-gradient(135deg,#14142a,#0c0c1a)] border border-white/8 shadow-[0_12px_30px_rgb(0_0_0/0.5)] transition-[rotate,box-shadow] duration-400 hover:rotate-x-6 hover:-rotate-y-6 hover:shadow-[0_30px_60px_rgb(120_80_255/0.3)] focus-visible:rotate-x-6 focus-visible:-rotate-y-6 focus-visible:outline-3 focus-visible:outline-tch10-cyan focus-visible:outline-offset-4 motion-reduce:transition-none motion-reduce:hover:rotate-x-0 motion-reduce:hover:rotate-y-0">
    <div class="absolute inset-0 opacity-0 mix-blend-color-dodge transition-opacity duration-400 bg-[length:250%_250%] bg-[0%_0%] bg-[linear-gradient(115deg,transparent_20%,rgb(255_0_200/0.35)_35%,rgb(0_255_220/0.35)_45%,rgb(255_230_0/0.35)_55%,transparent_70%)] group-hover:opacity-100 group-hover:animate-tch10-sweep group-focus-visible:opacity-100 motion-reduce:group-hover:animate-none"></div>
    <div class="absolute inset-0 opacity-0 mix-blend-overlay transition-opacity duration-400 bg-[radial-gradient(rgb(255_255_255/0.4)_0.5px,transparent_0.6px)] bg-[length:7px_7px] group-hover:opacity-50 group-focus-visible:opacity-50"></div>
    <div class="relative z-3 h-full p-[2.2rem] flex flex-col justify-between text-tch10-ink [transform:translateZ(40px)]">
      <span class="font-tch10-display text-[0.7rem] tracking-[0.3em] text-tch10-cyan">// MYTHIC · 001/250</span>
      <div class="mx-auto size-[90px] rounded-full blur-[0.5px] bg-[conic-gradient(#ff00c8,#00ffdc,#ffe600,#ff00c8)] shadow-[0_0_30px_rgb(120_80_255/0.5)]"></div>
      <div>
        <h2 class="font-tch10-display font-extrabold text-[1.7rem] text-center tracking-[0.05em]">Prism Warden</h2>
        <p class="text-[0.95rem] leading-[1.4] text-tch10-body text-center mt-1.5">A foil-stamped collector card that catches light across the full spectrum.</p>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@keyframes tch10-sweep {
  0% {
    background-position: 0% 0%;
  }

  100% {
    background-position: 200% 200%;
  }
}

@theme {
  --color-tch10-bg: #0a0a12;
  --color-tch10-bg: oklch(0.11 0.015 285);
  --color-tch10-ink: #e6e9ff;
  --color-tch10-ink: oklch(0.93 0.02 275);
  --color-tch10-body: #aaaabb;
  --color-tch10-body: oklch(0.74 0.015 285);
  --color-tch10-cyan: #66ccff;
  --color-tch10-cyan: oklch(0.8 0.12 230);
  --font-tch10-sans: 'Rajdhani', system-ui, sans-serif;
  --font-tch10-display: 'Orbitron', system-ui, sans-serif;
  --animate-tch10-sweep: tch10-sweep 2.5s linear infinite;
}

.tch-10 {
  width: 100%;
  min-height: 100svh;
}
```
