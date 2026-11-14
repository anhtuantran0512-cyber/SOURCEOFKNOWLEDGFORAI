---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-curtain-reveal-card-hover-effect/"
title: "Tailwind Curtain Reveal Card (Parting Velvet Halves)"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "Two striped velvet halves part on hover to unveil the stage behind, gold seam and all."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Curtain Reveal Card (Parting Velvet Halves)
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-curtain-reveal-card-hover-effect/

Two striped velvet halves part on hover to unveil the stage behind, gold seam and all. Nothing here needs custom CSS: the drapes are bg-[repeating-linear-gradient(…)], the part is two group-hover: translates, and the theatrical easing is one arbitrary curve.
## HTML
```html
<section class="tch-11 w-full min-h-svh grid place-items-center bg-tch11-bg font-tch11-sans p-8">
  <article tabindex="0" class="group relative w-[340px] h-[460px] rounded-md overflow-hidden cursor-pointer outline-none shadow-[0_20px_50px_rgb(0_0_0/0.5)] focus-visible:outline-3 focus-visible:outline-tch11-gold focus-visible:outline-offset-4">
    <div class="absolute inset-0 flex flex-col justify-center items-center text-center p-10 text-tch11-ink bg-[linear-gradient(rgb(20_8_12/0.55),rgb(20_8_12/0.75)),radial-gradient(circle_at_50%_35%,#5a2030,#1a0d12_70%)]">
      <span class="font-tch11-display italic text-base tracking-[0.2em] text-tch11-gold">— ACT III —</span>
      <h2 class="font-tch11-display font-extrabold text-[2.6rem] leading-[1.05] my-3">The Velvet<br>Hour</h2>
      <p class="text-[1.15rem] leading-[1.5] text-tch11-body">An evening of chamber music and candlelight. Doors open at eight.</p>
    </div>
    <div class="absolute inset-y-0 left-0 w-1/2 z-2 pointer-events-none origin-left bg-[repeating-linear-gradient(90deg,#7a1f2b_0_10px,#5e1620_10px_20px)] shadow-[inset_0_0_40px_rgb(0_0_0/0.4)] transition-transform duration-700 ease-[cubic-bezier(0.77,0,0.18,1)] group-hover:-translate-x-full group-focus-visible:-translate-x-full motion-reduce:transition-opacity motion-reduce:group-hover:translate-x-0 motion-reduce:group-hover:opacity-0 after:content-[''] after:absolute after:inset-0 after:bg-linear-to-r after:from-transparent after:to-black/25"></div>
    <div class="absolute inset-y-0 right-0 w-1/2 z-2 pointer-events-none origin-right bg-[repeating-linear-gradient(90deg,#7a1f2b_0_10px,#5e1620_10px_20px)] shadow-[inset_0_0_40px_rgb(0_0_0/0.4)] transition-transform duration-700 ease-[cubic-bezier(0.77,0,0.18,1)] group-hover:translate-x-full group-focus-visible:translate-x-full motion-reduce:transition-opacity motion-reduce:group-hover:translate-x-0 motion-reduce:group-hover:opacity-0 after:content-[''] after:absolute after:inset-0 after:bg-linear-to-l after:from-transparent after:to-black/25"></div>
    <div class="absolute inset-y-0 left-1/2 w-0.5 z-3 pointer-events-none -translate-x-1/2 opacity-80 bg-linear-to-b from-tch11-gold to-tch11-gold2 transition-opacity duration-400 group-hover:opacity-0 group-focus-visible:opacity-0"></div>
    <span class="absolute inset-x-0 bottom-6 z-4 text-center pointer-events-none font-tch11-display italic text-tch11-ink text-[1.1rem] tracking-[0.1em] transition-opacity duration-300 group-hover:opacity-0 group-focus-visible:opacity-0">Hover to part the curtain</span>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch11-bg: #1a0d12;
  --color-tch11-bg: oklch(0.19 0.04 15);
  --color-tch11-ink: #f3e3d3;
  --color-tch11-ink: oklch(0.93 0.03 65);
  --color-tch11-body: #cbb8a6;
  --color-tch11-body: oklch(0.79 0.03 65);
  --color-tch11-gold: #d4a373;
  --color-tch11-gold: oklch(0.75 0.08 65);
  --color-tch11-gold2: #8a5a2b;
  --color-tch11-gold2: oklch(0.52 0.09 65);
  --font-tch11-sans: 'Cormorant Garamond', Georgia, serif;
  --font-tch11-display: 'Playfair Display', Georgia, serif;
}

.tch-11 {
  width: 100%;
  min-height: 100svh;
}
```
