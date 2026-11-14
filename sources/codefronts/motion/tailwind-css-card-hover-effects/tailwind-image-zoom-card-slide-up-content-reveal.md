---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-image-zoom-card-slide-up-content-reveal/"
title: "Tailwind Image Zoom Card with Slide-Up Content Reveal"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "The dependable shop-grid workhorse: the image scales inside a clipped frame while a frosted detail sheet slides up from a peeking strip."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Zoom Card with Slide-Up Content Reveal
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-image-zoom-card-slide-up-content-reveal/

The dependable shop-grid workhorse: the image scales inside a clipped frame while a frosted detail sheet slides up from a peeking strip. This is the port where Tailwind is simply better &mdash; group-hover: and group-focus-within: replace four descendant selectors, and keyboard parity costs one extra variant instead of a new rule.
## HTML
```html
<section class="tch-03 w-full min-h-svh grid place-items-center bg-tch03-bg font-tch03-sans p-8">
  <article class="group relative w-[330px] h-[440px] rounded-[18px] overflow-hidden bg-white cursor-pointer shadow-[0_14px_36px_rgb(60_50_40/0.12)]">
    <div class="absolute inset-0 overflow-hidden">
      <div class="absolute inset-0 scale-100 transition-transform duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:scale-112 group-focus-within:scale-112 motion-reduce:transition-none bg-[radial-gradient(circle_at_35%_30%,#ffe2c2_0_30%,transparent_31%),linear-gradient(150deg,#e8956b,#b6452f_70%)] after:content-[''] after:absolute after:left-1/2 after:top-[42%] after:size-[150px] after:-translate-x-1/2 after:-translate-y-1/2 after:rounded-[50%_50%_48%_52%/60%_58%_42%_40%] after:bg-[linear-gradient(160deg,#6b3526,#3a1a12)] after:shadow-[0_20px_40px_rgb(0_0_0/0.25)]"></div>
    </div>
    <span class="absolute top-5 left-5 z-3 bg-tch03-ink text-white text-[0.68rem] font-bold tracking-[0.12em] uppercase px-3 py-1.5 rounded-full">New In</span>
    <div class="absolute inset-x-0 bottom-0 z-4 p-[1.4rem_1.5rem_1.6rem] bg-white/95 backdrop-blur-[6px] translate-y-[calc(100%-84px)] transition-transform duration-550 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:translate-y-0 group-focus-within:translate-y-0 motion-reduce:transition-none">
      <div class="flex justify-between items-baseline">
        <div>
          <h2 class="font-tch03-display font-semibold text-2xl text-tch03-ink">Terra Vase</h2>
          <p class="text-[0.8rem] text-tch03-mut mt-0.5">Hand-thrown stoneware</p>
        </div>
        <span class="font-bold text-xl text-tch03-acc">$68</span>
      </div>
      <p class="text-[0.84rem] leading-[1.55] text-tch03-body mt-3.5 mb-4">Matte terracotta with a subtle asymmetric lip. Each piece is wheel-thrown and one of a kind.</p>
      <a href="#" class="flex items-center justify-center min-h-11 rounded-[10px] bg-tch03-ink text-white no-underline font-semibold text-[0.88rem] transition-colors duration-200 hover:bg-tch03-acc focus-visible:outline-2 focus-visible:outline-tch03-acc focus-visible:outline-offset-2">View Product</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch03-bg: #f4f1ec;
  --color-tch03-bg: oklch(0.96 0.006 75);
  --color-tch03-ink: #2a2018;
  --color-tch03-ink: oklch(0.25 0.02 55);
  --color-tch03-body: #6a5e52;
  --color-tch03-body: oklch(0.5 0.02 65);
  --color-tch03-mut: #8a7d70;
  --color-tch03-mut: oklch(0.6 0.02 65);
  --color-tch03-acc: #b6452f;
  --color-tch03-acc: oklch(0.51 0.15 32);
  --font-tch03-sans: 'Manrope', system-ui, sans-serif;
  --font-tch03-display: 'Fraunces', Georgia, serif;
}

.tch-03 {
  width: 100%;
  min-height: 100svh;
}
```
