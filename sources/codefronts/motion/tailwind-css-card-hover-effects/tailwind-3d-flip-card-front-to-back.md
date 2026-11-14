---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-3d-flip-card-front-to-back/"
title: "Tailwind 3D Flip Card (Front to Back) with backface-visibility"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A team-profile card that turns a full 180° to swap a photo-and-name front for a bio-and-links back."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Flip Card (Front to Back) with backface-visibility
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-3d-flip-card-front-to-back/

A team-profile card that turns a full 180° to swap a photo-and-name front for a bio-and-links back. v4 is the first version where this port is genuinely tidy: transform-3d, rotate-y-180 and backface-hidden are all real utilities, so only perspective stays arbitrary.
## HTML
```html
<section class="tch-04 w-full min-h-svh grid place-items-center bg-tch04-bg bg-[radial-gradient(circle_at_70%_20%,#f6f4ee,#dcd9cf)] font-tch04-sans p-8 [perspective:1600px]">
  <div class="group w-[320px] h-[430px] cursor-pointer">
    <div class="relative size-full transform-3d transition-transform duration-700 ease-[cubic-bezier(0.4,0.15,0.2,1)] group-hover:rotate-y-180 group-focus-within:rotate-y-180 motion-reduce:transition-none motion-reduce:group-hover:rotate-y-0 motion-reduce:group-focus-within:rotate-y-0">
      <div class="absolute inset-0 rounded-3xl overflow-hidden backface-hidden shadow-[0_20px_45px_rgb(60_55_40/0.2)] bg-[linear-gradient(165deg,var(--color-tch04-front-a),var(--color-tch04-front-b))] flex flex-col justify-end p-[2.2rem] text-tch04-front-ink motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-0 motion-reduce:group-focus-within:opacity-0 before:content-[''] before:absolute before:-top-[10%] before:left-1/2 before:size-[200px] before:-translate-x-1/2 before:rounded-full before:bg-[radial-gradient(circle_at_40%_35%,#d8f5ee,#6cc4b4)] before:shadow-[0_20px_50px_rgb(0_0_0/0.2)]">
        <span class="relative text-[0.7rem] tracking-[0.22em] uppercase text-tch04-front-mut">Lead Designer</span>
        <h2 class="relative font-tch04-display font-extrabold text-[2.2rem] leading-none mt-1">Mara<br>Okonkwo</h2>
        <span class="relative mt-4 text-[0.74rem] text-tch04-front-mut">↻ hover or focus to flip</span>
      </div>
      <div class="absolute inset-0 rounded-3xl overflow-hidden backface-hidden rotate-y-180 shadow-[0_20px_45px_rgb(60_55_40/0.2)] bg-[linear-gradient(165deg,#1c1b1a,#0f0e0d)] p-[2.2rem] flex flex-col justify-between text-tch04-back-ink pointer-events-none group-hover:pointer-events-auto group-focus-within:pointer-events-auto motion-reduce:rotate-y-0 motion-reduce:opacity-0 motion-reduce:transition-opacity motion-reduce:duration-300 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-within:opacity-100">
        <div>
          <span class="text-[0.7rem] tracking-[0.22em] uppercase text-tch04-acc">Lead Designer</span>
          <h3 class="font-tch04-display font-extrabold text-[1.7rem] leading-[1.05] mt-1 mb-3.5">Mara Okonkwo</h3>
          <p class="text-[0.85rem] leading-[1.6] text-tch04-back-mut">Twelve years shaping product systems for fintech and health. Obsessed with motion, type, and the space between clicks.</p>
        </div>
        <div class="flex gap-2.5">
          <a href="#" class="flex-1 flex items-center justify-center min-h-11 rounded-[10px] border border-white/20 text-[0.78rem] font-medium text-tch04-back-ink no-underline transition-colors duration-300 hover:bg-tch04-acc/20 focus-visible:outline-2 focus-visible:outline-tch04-acc focus-visible:outline-offset-2">Email</a>
          <a href="#" class="flex-1 flex items-center justify-center min-h-11 rounded-[10px] border border-white/20 text-[0.78rem] font-medium text-tch04-back-ink no-underline transition-colors duration-300 hover:bg-tch04-acc/20 focus-visible:outline-2 focus-visible:outline-tch04-acc focus-visible:outline-offset-2">Dribbble</a>
          <a href="#" class="flex-1 flex items-center justify-center min-h-11 rounded-[10px] border border-white/20 text-[0.78rem] font-medium text-tch04-back-ink no-underline transition-colors duration-300 hover:bg-tch04-acc/20 focus-visible:outline-2 focus-visible:outline-tch04-acc focus-visible:outline-offset-2">LinkedIn</a>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch04-bg: #eceae3;
  --color-tch04-bg: oklch(0.93 0.008 95);
  --color-tch04-front-a: #2f9e8f;
  --color-tch04-front-a: oklch(0.63 0.1 178);
  --color-tch04-front-b: #145c52;
  --color-tch04-front-b: oklch(0.42 0.08 178);
  --color-tch04-front-ink: #f2fbf9;
  --color-tch04-front-ink: oklch(0.98 0.01 178);
  --color-tch04-front-mut: #aef0e3;
  --color-tch04-front-mut: oklch(0.91 0.07 172);
  --color-tch04-back-ink: #ece9e2;
  --color-tch04-back-ink: oklch(0.93 0.008 85);
  --color-tch04-back-mut: #b3afa6;
  --color-tch04-back-mut: oklch(0.73 0.01 85);
  --color-tch04-acc: #5fd3c0;
  --color-tch04-acc: oklch(0.81 0.1 175);
  --font-tch04-sans: 'DM Sans', system-ui, sans-serif;
  --font-tch04-display: 'Bricolage Grotesque', system-ui, sans-serif;
}

.tch-04 {
  width: 100%;
  min-height: 100svh;
}
```
