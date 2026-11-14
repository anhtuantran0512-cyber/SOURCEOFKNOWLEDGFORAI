---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-book-cover-open-card/"
title: "Tailwind Book Cover Open Card with Hinged 3D Rotation"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A hard cover that swings open on a left hinge to reveal the first page inside."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Book Cover Open Card with Hinged 3D Rotation
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-book-cover-open-card/

A hard cover that swings open on a left hinge to reveal the first page inside. The hinge is the whole demo: origin-left plus a 145° rotateY, with a shadow that flips sides as the cover passes vertical.
## HTML
```html
<section class="tch-32 w-full min-h-svh grid place-items-center bg-tch32-bg bg-[radial-gradient(circle_at_50%_40%,#3a2e22,#1a130d)] font-tch32-sans p-8 [perspective:1600px]">
  <article tabindex="0" class="group relative w-[300px] h-[420px] cursor-pointer outline-none transform-3d">
    <div class="absolute inset-0 rounded-[4px_8px_8px_4px] bg-tch32-page p-[2.4rem_2rem_2.4rem_2.6rem] flex flex-col text-tch32-pink shadow-[inset_18px_0_30px_-18px_rgb(0_0_0/0.4)]">
      <span class="font-tch32-display text-[0.8rem] tracking-[0.2em] uppercase text-tch32-gilt mb-4">Chapter One</span>
      <h2 class="font-tch32-display text-[1.9rem] leading-[1.15] mb-4">The House<br>on Linden Row</h2>
      <p class="text-base leading-[1.65] italic text-tch32-pmut">"I had not meant to stay the winter. But the house, you understand, had other plans..."</p>
      <span class="mt-auto text-center text-[0.85rem] text-tch32-gilt">— 1 —</span>
    </div>
    <div class="absolute inset-0 z-2 rounded-[4px_8px_8px_4px] transform-3d origin-left shadow-[6px_6px_24px_rgb(0_0_0/0.5)] transition-[transform,box-shadow] duration-900 ease-[cubic-bezier(0.65,0,0.35,1)] group-hover:rotate-y-[-145deg] group-hover:shadow-[-10px_6px_30px_rgb(0_0_0/0.4)] group-focus-visible:rotate-y-[-145deg] motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:rotate-y-0 motion-reduce:group-hover:opacity-0">
      <div class="absolute inset-0 rounded-[4px_8px_8px_4px] backface-hidden border-l-6 border-l-tch32-spine bg-[linear-gradient(160deg,#6b2737,#401520)] p-[2.6rem_2rem] flex flex-col justify-between text-tch32-cink">
        <span class="font-tch32-display text-[0.72rem] tracking-[0.25em] uppercase text-tch32-gilt">Harrow &amp; Quill</span>
        <div>
          <h1 class="font-tch32-display text-[2.6rem] leading-[1.05]">The House<br>on Linden<br>Row</h1>
          <div class="w-[50px] h-0.5 bg-tch32-gilt my-3"></div>
          <span class="italic text-[1.05rem] text-tch32-cmut">by E. Marlowe</span>
        </div>
      </div>
      <div class="absolute inset-0 rounded-[4px_8px_8px_4px] backface-hidden rotate-y-180 bg-tch32-cback shadow-[inset_0_0_40px_rgb(0_0_0/0.4)]"></div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch32-bg: #2a2018;
  --color-tch32-bg: oklch(0.28 0.02 65);
  --color-tch32-page: #f5efe0;
  --color-tch32-page: oklch(0.95 0.02 85);
  --color-tch32-pink: #3a2e1f;
  --color-tch32-pink: oklch(0.3 0.02 70);
  --color-tch32-pmut: #5a4a36;
  --color-tch32-pmut: oklch(0.42 0.03 70);
  --color-tch32-gilt: #9a7b4f;
  --color-tch32-gilt: oklch(0.58 0.06 70);
  --color-tch32-cink: #e8d8b8;
  --color-tch32-cink: oklch(0.89 0.04 80);
  --color-tch32-cmut: #d8c3a0;
  --color-tch32-cmut: oklch(0.83 0.05 80);
  --color-tch32-cback: #5a1f2c;
  --color-tch32-cback: oklch(0.34 0.1 15);
  --color-tch32-spine: #2e0f17;
  --color-tch32-spine: oklch(0.22 0.07 15);
  --font-tch32-sans: 'EB Garamond', Georgia, serif;
  --font-tch32-display: 'Marcellus', Georgia, serif;
}

.tch-32 {
  width: 100%;
  min-height: 100svh;
}
```
