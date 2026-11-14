---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-magazine-overlay-slide-card/"
title: "Tailwind Magazine Overlay Slide Card (Full-Face Panel Takeover)"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A magazine card where a full-bleed red panel slides up and takes over the entire face, swapping a quiet cover for full issue details."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Magazine Overlay Slide Card (Full-Face Panel Takeover)
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-magazine-overlay-slide-card/

A magazine card where a full-bleed red panel slides up and takes over the entire face, swapping a quiet cover for full issue details. Unlike the partial sheets in demos 03 and 18, this panel covers everything &mdash; which makes the easing choice the whole design.
## HTML
```html
<section class="tch-25 w-full min-h-svh grid place-items-center bg-tch25-bg font-tch25-sans p-8">
  <article class="group relative w-[330px] h-[440px] rounded-sm overflow-hidden cursor-pointer bg-tch25-ink shadow-[0_18px_40px_rgb(0_0_0/0.2)]">
    <div class="absolute inset-0 flex flex-col justify-end p-9 text-white bg-[linear-gradient(rgb(0_0_0/0.2),rgb(0_0_0/0.45)),linear-gradient(135deg,#6b7c8c,#2f3a44)]">
      <span class="text-[0.7rem] tracking-[0.25em] uppercase opacity-85">Editorial</span>
      <h2 class="font-tch25-display font-black text-[2.4rem] leading-none mt-1.5">Issue<br>No. 27</h2>
    </div>
    <div class="absolute inset-0 z-2 p-9 flex flex-col justify-between text-white bg-tch25-panel translate-y-[101%] transition-transform duration-550 ease-[cubic-bezier(0.76,0,0.24,1)] group-hover:translate-y-0 group-focus-within:translate-y-0 motion-reduce:transition-none">
      <span class="font-tch25-display italic text-base">№ 27 — Spring</span>
      <h3 class="font-tch25-display font-black text-[2.6rem] leading-[0.95]">The Red<br>Issue</h3>
      <p class="text-[0.88rem] leading-[1.6] text-white/92">Forty pages on color, courage, and the people painting cities awake.</p>
      <a href="#" class="flex items-center min-h-11 text-[0.78rem] tracking-[0.18em] uppercase text-white no-underline border-t border-white/40 pt-4 transition-colors duration-200 hover:text-tch25-bg focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Read the issue →</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch25-bg: #f2f0eb;
  --color-tch25-bg: oklch(0.96 0.005 85);
  --color-tch25-ink: #1a1a1a;
  --color-tch25-ink: oklch(0.2 0 0);
  --color-tch25-panel: #e23744;
  --color-tch25-panel: oklch(0.6 0.2 22);
  --font-tch25-sans: 'Work Sans', system-ui, sans-serif;
  --font-tch25-display: 'Bodoni Moda', Georgia, serif;
}

.tch-25 {
  width: 100%;
  min-height: 100svh;
}
```
