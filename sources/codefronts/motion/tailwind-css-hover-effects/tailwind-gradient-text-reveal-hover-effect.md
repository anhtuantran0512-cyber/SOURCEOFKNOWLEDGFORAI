---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-gradient-text-reveal-hover-effect/"
title: "Tailwind Gradient Text Reveal Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six ways to paint a gradient onto letterforms on hover — position wipe, radial burst, rainbow shift, shimmer keyframe, duotone hue swap and a diagonal sweep."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Text Reveal Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-gradient-text-reveal-hover-effect/

Six ways to paint a gradient onto letterforms on hover — position wipe, radial burst, rainbow shift, shimmer keyframe, duotone hue swap and a diagonal sweep. bg-clip-text and text-transparent are first-class utilities, which makes this the port that shrinks the most.
## HTML
```html
<section class="thv-04 w-full min-h-svh grid place-items-center bg-thv04-bg font-thv04-sans px-6 py-14">
  <div class="w-[min(900px,100%)] grid grid-cols-[repeat(auto-fit,minmax(230px,1fr))] gap-8">
    <div class="flex flex-col items-center gap-5 px-6 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-black tracking-[0.06em] text-thv04-text bg-clip-text bg-[linear-gradient(90deg,#7c3aed,#06b6d4,#10b981)] [background-size:200%_auto] [background-position:right_center] rounded-xs transition-[background-position,color] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:text-transparent hover:[background-position:left_center] focus-visible:text-transparent focus-visible:[background-position:left_center] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv04-ring motion-reduce:transition-none">AURORA</span>
      <span class="text-[10px] tracking-[0.15em] uppercase text-thv04-dim text-center">gradient position wipe</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-6 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-black tracking-[0.06em] text-thv04-text bg-clip-text bg-[radial-gradient(circle_at_50%_50%,#f59e0b,#ef4444,#7c3aed)] [background-size:0%_0%] [background-position:center] bg-no-repeat rounded-xs transition-[background-size,color] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:text-transparent hover:[background-size:200%_200%] focus-visible:text-transparent focus-visible:[background-size:200%_200%] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv04-ring motion-reduce:transition-none">RADIAL</span>
      <span class="text-[10px] tracking-[0.15em] uppercase text-thv04-dim text-center">radial-gradient burst</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-6 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-black tracking-[0.06em] text-thv04-text bg-clip-text bg-[linear-gradient(90deg,#f43f5e,#f59e0b,#10b981,#06b6d4,#6d28d9,#f43f5e)] [background-size:400%_auto] [background-position:0%_center] rounded-xs transition-[background-position,color] duration-600 hover:text-transparent hover:[background-position:100%_center] focus-visible:text-transparent focus-visible:[background-position:100%_center] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv04-ring motion-reduce:transition-none">SPECTRUM</span>
      <span class="text-[10px] tracking-[0.15em] uppercase text-thv04-dim text-center">rainbow hue-shift</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-6 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-black tracking-[0.06em] text-thv04-text bg-clip-text bg-[linear-gradient(105deg,#c4b5fd_0%,#fff_40%,#7c3aed_55%,#c4b5fd_100%)] [background-size:200%_auto] rounded-xs transition-colors duration-300 hover:text-transparent hover:animate-thv04-shimmer focus-visible:text-transparent focus-visible:animate-thv04-shimmer focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv04-ring motion-reduce:hover:animate-none motion-reduce:hover:[background-position:50%_center]">SHIMMER</span>
      <span class="text-[10px] tracking-[0.15em] uppercase text-thv04-dim text-center">shimmer keyframe</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-6 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-black tracking-[0.06em] text-thv04-text bg-clip-text bg-[linear-gradient(135deg,#f43f5e,#f97316)] rounded-xs transition-[color,filter] duration-400 hover:text-transparent hover:[filter:hue-rotate(120deg)_saturate(1.4)] focus-visible:text-transparent focus-visible:[filter:hue-rotate(120deg)_saturate(1.4)] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv04-ring motion-reduce:transition-none">DUOTONE</span>
      <span class="text-[10px] tracking-[0.15em] uppercase text-thv04-dim text-center">dual-tone color swap</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-6 py-12 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-black tracking-[0.06em] text-thv04-text bg-clip-text bg-[linear-gradient(135deg,#06b6d4_0%,#a21caf_50%,#06b6d4_100%)] [background-size:200%_200%] [background-position:bottom_right] rounded-xs transition-[background-position,color] duration-600 ease-[cubic-bezier(.4,0,.2,1)] hover:text-transparent hover:[background-position:top_left] focus-visible:text-transparent focus-visible:[background-position:top_left] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv04-ring motion-reduce:transition-none">PRISM</span>
      <span class="text-[10px] tracking-[0.15em] uppercase text-thv04-dim text-center">diagonal sweep</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv04-bg: #06040f;
  --color-thv04-bg: oklch(0.11 0.02 285);
  --color-thv04-text: #d4d4f7;
  --color-thv04-text: oklch(0.87 0.05 290);
  --color-thv04-dim: #555555;
  --color-thv04-dim: oklch(0.46 0 0);
  --color-thv04-ring: #8b5cf6;
  --color-thv04-ring: oklch(0.63 0.21 295);
  --font-thv04-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-thv04-shimmer: thv04-shimmer .8s linear infinite;
}

.thv-04 {
  width: 100%;
  min-height: 100svh;
}

.thv-04 ::selection {
  background: var(--color-thv04-ring);
  color: #fff;
}

@keyframes thv04-shimmer {
  0% {
    background-position: -100% center;
  }

  100% {
    background-position: 200% center;
  }
}
```
