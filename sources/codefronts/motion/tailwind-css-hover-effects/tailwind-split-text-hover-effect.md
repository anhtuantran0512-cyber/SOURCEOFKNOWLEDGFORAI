---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-split-text-hover-effect/"
title: "Tailwind Split Text Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four hovers that cut a word in half and push the pieces apart — top/bottom, left/right, a diagonal polygon and a split-plus-fade."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split Text Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-split-text-hover-effect/

Four hovers that cut a word in half and push the pieces apart — top/bottom, left/right, a diagonal polygon and a split-plus-fade. Two clipped copies of the text live in before: and after:; the base element goes transparent so nothing shows through the seam.
## HTML
```html
<section class="thv-05 w-full min-h-svh grid place-items-center bg-thv05-bg font-thv05-sans px-6 py-14">
  <div class="w-[min(820px,100%)] grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-10">
    <div class="flex flex-col items-center gap-6 px-8 py-14 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" data-text="DIVIDE" class="relative inline-block overflow-hidden text-[clamp(2rem,6vw,3rem)] font-black tracking-[0.1em] text-transparent rounded-xs focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv05-cyan before:content-[attr(data-text)] before:absolute before:inset-0 before:text-thv05-cyan before:[clip-path:inset(0_0_50%_0)] before:transition-transform before:duration-450 before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[attr(data-text)] after:absolute after:inset-0 after:text-thv05-cyan after:[clip-path:inset(50%_0_0_0)] after:transition-transform after:duration-450 after:ease-[cubic-bezier(.4,0,.2,1)] hover:before:-translate-y-[0.55em] hover:after:translate-y-[0.55em] focus-visible:before:-translate-y-[0.55em] focus-visible:after:translate-y-[0.55em] motion-reduce:before:transition-none motion-reduce:after:transition-none">DIVIDE</span>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv05-dim">top / bottom split</span>
    </div>
    <div class="flex flex-col items-center gap-6 px-8 py-14 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" data-text="SCHISM" class="relative inline-block overflow-hidden text-[clamp(2rem,6vw,3rem)] font-black tracking-[0.1em] text-transparent rounded-xs focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv05-rose before:content-[attr(data-text)] before:absolute before:inset-0 before:text-thv05-rose before:[clip-path:inset(0_50%_0_0)] before:transition-transform before:duration-450 before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[attr(data-text)] after:absolute after:inset-0 after:text-thv05-amber after:[clip-path:inset(0_0_0_50%)] after:transition-transform after:duration-450 after:ease-[cubic-bezier(.4,0,.2,1)] hover:before:-translate-x-[0.4em] hover:after:translate-x-[0.4em] focus-visible:before:-translate-x-[0.4em] focus-visible:after:translate-x-[0.4em] motion-reduce:before:transition-none motion-reduce:after:transition-none">SCHISM</span>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv05-dim">left / right push</span>
    </div>
    <div class="flex flex-col items-center gap-6 px-8 py-14 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" data-text="SLASH" class="relative inline-block text-[clamp(2rem,6vw,3rem)] font-black tracking-[0.1em] text-transparent rounded-xs focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv05-violet before:content-[attr(data-text)] before:absolute before:inset-0 before:text-thv05-violet before:[clip-path:polygon(0_0,100%_0,60%_100%,0_100%)] before:transition-transform before:duration-450 before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[attr(data-text)] after:absolute after:inset-0 after:text-thv05-cyan after:[clip-path:polygon(60%_0,100%_0,100%_100%,0_100%)] after:transition-transform after:duration-450 after:ease-[cubic-bezier(.4,0,.2,1)] hover:before:-translate-x-[0.3em] hover:before:-translate-y-[0.3em] hover:after:translate-x-[0.3em] hover:after:translate-y-[0.3em] focus-visible:before:-translate-x-[0.3em] focus-visible:before:-translate-y-[0.3em] focus-visible:after:translate-x-[0.3em] focus-visible:after:translate-y-[0.3em] motion-reduce:before:transition-none motion-reduce:after:transition-none">SLASH</span>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv05-dim">diagonal polygon</span>
    </div>
    <div class="flex flex-col items-center gap-6 px-8 py-14 rounded-2xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" data-text="RIFT" class="relative inline-block text-[clamp(2rem,6vw,3rem)] font-black tracking-[0.1em] text-transparent rounded-xs focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv05-amber before:content-[attr(data-text)] before:absolute before:inset-0 before:text-thv05-amber before:[clip-path:inset(0_0_50%_0)] before:transition-[transform,opacity] before:duration-450 before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[attr(data-text)] after:absolute after:inset-0 after:text-thv05-rose after:[clip-path:inset(50%_0_0_0)] after:transition-[transform,opacity] after:duration-450 after:ease-[cubic-bezier(.4,0,.2,1)] hover:before:-translate-y-[0.6em] hover:before:-rotate-3 hover:before:opacity-0 hover:after:translate-y-[0.6em] hover:after:rotate-3 hover:after:opacity-0 focus-visible:before:-translate-y-[0.6em] focus-visible:before:opacity-0 focus-visible:after:translate-y-[0.6em] focus-visible:after:opacity-0 motion-reduce:before:transition-none motion-reduce:after:transition-none">RIFT</span>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv05-dim">split + fade</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv05-bg: #020917;
  --color-thv05-bg: oklch(0.13 0.03 260);
  --color-thv05-dim: #475569;
  --color-thv05-dim: oklch(0.45 0.03 257);
  --color-thv05-cyan: #06b6d4;
  --color-thv05-cyan: oklch(0.71 0.14 208);
  --color-thv05-rose: #f43f5e;
  --color-thv05-rose: oklch(0.65 0.23 16);
  --color-thv05-violet: #8b5cf6;
  --color-thv05-violet: oklch(0.63 0.21 295);
  --color-thv05-amber: #f59e0b;
  --color-thv05-amber: oklch(0.77 0.16 70);
  --font-thv05-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-05 {
  width: 100%;
  min-height: 100svh;
}

.thv-05 ::selection {
  background: var(--color-thv05-cyan);
  color: #fff;
}
```
