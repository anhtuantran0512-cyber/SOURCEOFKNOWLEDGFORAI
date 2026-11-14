---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-magnetic-liquid-button-hover-effect/"
title: "Tailwind Magnetic Liquid Button Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four tactile button hovers — liquid fill, blob morph, surface-tension droplet and rubber squash-and-stretch."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Magnetic Liquid Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-magnetic-liquid-button-hover-effect/

Four tactile button hovers — liquid fill, blob morph, surface-tension droplet and rubber squash-and-stretch. Fill layers are before: pseudo-elements scaled from zero; the label rides above on relative z-10.
## HTML
```html
<section class="thv-07 w-full min-h-svh grid place-items-center bg-thv07-bg font-thv07-sans px-6 py-14">
  <div class="w-[min(760px,100%)] grid grid-cols-[repeat(auto-fit,minmax(240px,1fr))] gap-10">
    <div class="flex flex-col items-center gap-5 px-8 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden isolate min-h-11 px-9 py-3.5 rounded-lg border-2 border-thv07-green bg-transparent text-base font-semibold tracking-[0.06em] text-thv07-green cursor-pointer transition-colors duration-350 before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv07-green before:origin-bottom before:scale-y-0 before:transition-transform before:duration-350 before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:before:scale-y-100 focus-visible:text-white focus-visible:before:scale-y-100 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv07-green motion-reduce:before:transition-none"><span class="relative z-10">Liquid Fill</span></button>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv07-dim">scale-Y fill</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-8 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden isolate min-h-11 px-9 py-3.5 rounded-lg border-2 border-thv07-teal bg-transparent text-base font-semibold tracking-[0.06em] text-thv07-teal cursor-pointer transition-[color,border-radius] duration-500 ease-[cubic-bezier(.4,0,.2,1)] before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv07-teal before:rounded-lg before:scale-0 before:transition-[transform,border-radius] before:duration-350 before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:rounded-[60%_40%_70%_30%/40%_70%_30%_60%] hover:before:scale-100 hover:before:rounded-[60%_40%_70%_30%/40%_70%_30%_60%] focus-visible:text-white focus-visible:before:scale-100 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv07-teal motion-reduce:transition-none motion-reduce:before:transition-none"><span class="relative z-10">Blob Morph</span></button>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv07-dim">border-radius keyframe</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-8 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden isolate min-h-11 px-9 py-3.5 rounded-lg border-2 border-thv07-emerald bg-transparent text-base font-semibold tracking-[0.06em] text-thv07-emerald cursor-pointer transition-colors duration-350 after:content-[''] after:absolute after:top-1/2 after:left-1/2 after:-z-10 after:w-[200%] after:h-[200%] after:rounded-full after:bg-thv07-emerald after:-translate-x-1/2 after:-translate-y-1/2 after:scale-0 after:transition-transform after:duration-500 after:ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:after:scale-100 focus-visible:text-white focus-visible:after:scale-100 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv07-emerald motion-reduce:after:transition-none"><span class="relative z-10">Surface Tension</span></button>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv07-dim">centred droplet expand</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-8 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden isolate min-h-11 px-9 py-3.5 rounded-lg border-2 border-thv07-mint bg-transparent text-base font-semibold tracking-[0.06em] text-thv07-mint cursor-pointer transition-[transform,color] duration-200 ease-[cubic-bezier(.4,0,.2,1)] before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv07-mint before:origin-bottom before:scale-y-0 before:transition-transform before:duration-350 hover:text-black hover:scale-x-[1.06] hover:scale-y-[0.93] hover:before:scale-y-100 focus-visible:text-black focus-visible:before:scale-y-100 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv07-mint active:scale-x-[0.97] active:scale-y-[1.04] motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:before:transition-none"><span class="relative z-10">Rubber Stretch</span></button>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv07-dim">squash-and-stretch</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv07-bg: #030d09;
  --color-thv07-bg: oklch(0.13 0.02 165);
  --color-thv07-dim: #4b6157;
  --color-thv07-dim: oklch(0.45 0.02 165);
  --color-thv07-green: #10b981;
  --color-thv07-green: oklch(0.7 0.15 163);
  --color-thv07-teal: #0d9488;
  --color-thv07-teal: oklch(0.6 0.12 180);
  --color-thv07-emerald: #059669;
  --color-thv07-emerald: oklch(0.6 0.13 163);
  --color-thv07-mint: #6ee7b7;
  --color-thv07-mint: oklch(0.86 0.13 165);
  --font-thv07-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-07 {
  width: 100%;
  min-height: 100svh;
}

.thv-07 ::selection {
  background: var(--color-thv07-green);
  color: #fff;
}
```
