---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-shining-light-glare-image-hover/"
title: "Tailwind Shining Light Glare Image Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "A bright band swept across the artwork by a single pseudo-element &mdash; and in utilities the entire sweep is an after: chain on the frame:…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shining Light Glare Image Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-shining-light-glare-image-hover/

A bright band swept across the artwork by a single pseudo-element &mdash; and in utilities the entire sweep is an after: chain on the frame: after:[translate:-200%] group-hover:after:[translate:300%]. No extra markup, no separate rule block, and the two ends of the travel sit next to each other.
## HTML
```html
<section class="tih-13 w-full min-h-svh grid place-items-center bg-tih13-bg font-tih13-sans px-6 py-10" aria-label="Shining light glare image hover demo">
  <div class="grid w-full max-w-195 gap-4 grid-cols-1 sm:grid-cols-3">
    <article class="group relative overflow-hidden rounded-[14px] border border-[oklch(1_0_0/0.06)] transition-[border-color,box-shadow] duration-600 ease-tih13 hover:border-[oklch(0.84_0.16_85/0.3)] hover:shadow-[0_8px_40px_oklch(0.84_0.16_85/0.12)] motion-reduce:transition-none">
      <div class="relative aspect-[4/3] grid place-items-center overflow-hidden bg-[image:url('https://picsum.photos/seed/tih13-gold/800/600'),linear-gradient(135deg,oklch(0.18_0.03_60),oklch(0.32_0.08_55),oklch(0.55_0.13_65),oklch(0.84_0.16_85))] bg-cover bg-center bg-no-repeat after:content-[''] after:absolute after:-inset-1/2 after:w-2/5 after:h-[200%] after:bg-linear-[105deg,transparent_40%,oklch(1_0_0/0.08)_45%,oklch(1_0_0/0.22)_50%,oklch(1_0_0/0.08)_55%,transparent_60%] after:skew-x-[-10deg] after:[translate:-200%] after:transition-[translate] after:duration-600 after:ease-tih13 group-hover:after:[translate:300%] motion-reduce:after:hidden">
      </div>
      <div class="px-4 py-3.5 bg-[oklch(0_0_0/0.4)]">
        <p class="mb-1.25 text-[9px] font-bold tracking-[0.12em] uppercase text-tih13-acc">Premium</p>
        <h3 class="text-sm font-bold text-tih13-text">Gold Tier Membership</h3>
        <p class="mt-0.5 text-[11px] tracking-[-1px] text-tih13-acc" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</p>
        <p class="mt-1.5 text-base font-extrabold text-tih13-acc tabular-nums">$49 / mo</p>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[14px] border border-[oklch(1_0_0/0.06)] transition-[border-color,box-shadow] duration-600 ease-tih13 hover:border-[oklch(0.84_0.16_85/0.3)] hover:shadow-[0_8px_40px_oklch(0.84_0.16_85/0.12)] motion-reduce:transition-none">
      <div class="relative aspect-[4/3] grid place-items-center overflow-hidden bg-[image:url('https://picsum.photos/seed/tih13-platinum/800/600'),linear-gradient(135deg,oklch(0.15_0_0),oklch(0.25_0_0),oklch(0.4_0_0),oklch(0.72_0_0))] bg-cover bg-center bg-no-repeat after:content-[''] after:absolute after:-inset-1/2 after:w-2/5 after:h-[200%] after:bg-linear-[105deg,transparent_40%,oklch(1_0_0/0.08)_45%,oklch(1_0_0/0.22)_50%,oklch(1_0_0/0.08)_55%,transparent_60%] after:skew-x-[-10deg] after:[translate:-200%] after:transition-[translate] after:duration-600 after:ease-tih13 group-hover:after:[translate:300%] motion-reduce:after:hidden">
      </div>
      <div class="px-4 py-3.5 bg-[oklch(0_0_0/0.4)]">
        <p class="mb-1.25 text-[9px] font-bold tracking-[0.12em] uppercase text-tih13-acc">Exclusive</p>
        <h3 class="text-sm font-bold text-tih13-text">Platinum Credit Card</h3>
        <p class="mt-0.5 text-[11px] tracking-[-1px] text-tih13-acc" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</p>
        <p class="mt-1.5 text-base font-extrabold text-tih13-acc tabular-nums">0% APR 18mo</p>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[14px] border border-[oklch(1_0_0/0.06)] transition-[border-color,box-shadow] duration-600 ease-tih13 hover:border-[oklch(0.84_0.16_85/0.3)] hover:shadow-[0_8px_40px_oklch(0.84_0.16_85/0.12)] motion-reduce:transition-none">
      <div class="relative aspect-[4/3] grid place-items-center overflow-hidden bg-[image:url('https://picsum.photos/seed/tih13-diamond/800/600'),linear-gradient(135deg,oklch(0.17_0.07_310),oklch(0.35_0.18_295),oklch(0.55_0.24_295),oklch(0.83_0.1_295))] bg-cover bg-center bg-no-repeat after:content-[''] after:absolute after:-inset-1/2 after:w-2/5 after:h-[200%] after:bg-linear-[105deg,transparent_40%,oklch(1_0_0/0.08)_45%,oklch(1_0_0/0.22)_50%,oklch(1_0_0/0.08)_55%,transparent_60%] after:skew-x-[-10deg] after:[translate:-200%] after:transition-[translate] after:duration-600 after:ease-tih13 group-hover:after:[translate:300%] motion-reduce:after:hidden">
      </div>
      <div class="px-4 py-3.5 bg-[oklch(0_0_0/0.4)]">
        <p class="mb-1.25 text-[9px] font-bold tracking-[0.12em] uppercase text-tih13-acc">Diamond</p>
        <h3 class="text-sm font-bold text-tih13-text">Crystal Pro Bundle</h3>
        <p class="mt-0.5 text-[11px] tracking-[-1px] text-tih13-acc" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</p>
        <p class="mt-1.5 text-base font-extrabold text-tih13-acc tabular-nums">$299 / yr</p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih13-bg: #0a0906;
  --color-tih13-bg: oklch(0.12 0.008 85);
  --color-tih13-text: #f1f5f9;
  --color-tih13-text: oklch(0.96 0.005 250);
  --color-tih13-muted: #78716c;
  --color-tih13-muted: oklch(0.6 0.01 60);
  --color-tih13-acc: #fbbf24;
  --color-tih13-acc: oklch(0.84 0.16 85);
  --font-tih13-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih13: cubic-bezier(0.4, 0, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-13 {
  width: 100%;
  min-height: 100svh;
}

.tih-13 ::selection {
  background: oklch(0.84 0.16 85);
  color: #000;
}
```
