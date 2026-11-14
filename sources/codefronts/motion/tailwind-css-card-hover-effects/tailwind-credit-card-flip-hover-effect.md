---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-credit-card-flip-hover-effect/"
title: "Tailwind Credit Card Flip with Magnetic Strip & CVV"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "The fintech variant of the flip: a platinum card front with number, holder and expiry, turning to a back face with magnetic strip and CVV."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Credit Card Flip with Magnetic Strip & CVV
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-credit-card-flip-hover-effect/

The fintech variant of the flip: a platinum card front with number, holder and expiry, turning to a back face with magnetic strip and CVV. Geometry identical to demo 04 &mdash; the interesting difference is layout, and how a full-bleed strip is done with negative margin utilities.
## HTML
```html
<section class="tch-19 w-full min-h-svh grid place-items-center bg-tch19-bg font-tch19-sans p-8 [perspective:1500px]">
  <div tabindex="0" class="group w-[330px] h-[440px] cursor-pointer outline-none rounded-[20px] focus-visible:outline-3 focus-visible:outline-tch19-acc focus-visible:outline-offset-4">
    <div class="relative size-full transform-3d transition-transform duration-700 ease-[cubic-bezier(0.4,0.2,0.2,1)] group-hover:rotate-y-180 group-focus-within:rotate-y-180 motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0 motion-reduce:group-focus-within:rotate-y-0">
      <div class="absolute inset-0 rounded-[20px] overflow-hidden backface-hidden p-10 flex flex-col justify-between shadow-[0_20px_45px_rgb(0_0_0/0.45)] bg-[linear-gradient(160deg,#12806a,#064237)] text-tch19-front-ink motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-0">
        <div class="flex justify-between items-center">
          <div class="grid place-items-center size-11 rounded-xl bg-tch19-front-ink text-tch19-front-deep font-extrabold text-xl">◈</div>
          <span class="font-tch19-mono text-[0.75rem] tracking-[0.2em]">PLATINUM</span>
        </div>
        <div class="font-tch19-mono text-[1.4rem] tracking-[0.16em] tabular-nums">4921 ·· 7755 ·· 0042</div>
        <div class="flex justify-between items-end text-[0.78rem]">
          <span class="font-semibold tracking-[0.08em] uppercase">A. Marlowe</span><span class="tabular-nums">12/29</span>
        </div>
      </div>
      <div class="absolute inset-0 rounded-[20px] overflow-hidden backface-hidden rotate-y-180 p-10 flex flex-col justify-between shadow-[0_20px_45px_rgb(0_0_0/0.45)] bg-[linear-gradient(160deg,#1a1f29,#0c0f14)] text-tch19-back-ink pointer-events-none group-hover:pointer-events-auto group-focus-within:pointer-events-auto motion-reduce:rotate-y-0 motion-reduce:opacity-0 motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-100">
        <div class="h-[46px] -mx-10 bg-black"></div>
        <h2 class="font-extrabold text-[1.6rem] leading-[1.1]">Flip to<br>the back</h2>
        <p class="text-[0.85rem] leading-[1.6] text-tch19-back-mut">Same card, two faces. A full 180° rotation reveals account details on the reverse.</p>
        <span class="self-end font-tch19-mono font-medium tracking-[0.2em] px-3.5 py-1.5 rounded-md bg-tch19-back-chip text-tch19-back-deep tabular-nums">··· 309</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch19-bg: #0e1116;
  --color-tch19-bg: oklch(0.15 0.01 250);
  --color-tch19-front-ink: #eafff7;
  --color-tch19-front-ink: oklch(0.97 0.02 165);
  --color-tch19-front-deep: #064237;
  --color-tch19-front-deep: oklch(0.32 0.07 168);
  --color-tch19-back-ink: #dfe4ec;
  --color-tch19-back-ink: oklch(0.9 0.01 255);
  --color-tch19-back-mut: #9aa3b2;
  --color-tch19-back-mut: oklch(0.69 0.02 255);
  --color-tch19-back-chip: #e8ecf3;
  --color-tch19-back-chip: oklch(0.93 0.008 255);
  --color-tch19-back-deep: #0c0f14;
  --color-tch19-back-deep: oklch(0.13 0.01 250);
  --color-tch19-acc: #12806a;
  --color-tch19-acc: oklch(0.52 0.1 168);
  --font-tch19-sans: 'Libre Franklin', system-ui, sans-serif;
  --font-tch19-mono: 'IBM Plex Mono', ui-monospace, monospace;
}

.tch-19 {
  width: 100%;
  min-height: 100svh;
}
```
