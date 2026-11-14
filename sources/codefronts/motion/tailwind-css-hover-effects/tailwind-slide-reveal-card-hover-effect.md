---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-slide-reveal-card-hover-effect/"
title: "Tailwind Slide Reveal Card Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four cards that hide content until hover — bottom-up overlay, left-push, curtain wipe and a blurred dissolve."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide Reveal Card Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-slide-reveal-card-hover-effect/

Four cards that hide content until hover — bottom-up overlay, left-push, curtain wipe and a blurred dissolve. Every reveal is a group-hover: transform on a panel clipped by the card's overflow-hidden.
## HTML
```html
<section class="thv-17 w-full min-h-svh grid place-items-center bg-thv17-bg font-thv17-sans px-6 py-14">
  <div class="w-[min(760px,100%)] grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-8">
    <div class="group relative overflow-hidden min-h-[220px] rounded-2xl bg-white/[0.03] border border-white/[0.08]">
      <div class="flex flex-col gap-2.5 p-7">
        <span class="text-2xl text-thv17-amber">♟</span>
        <span class="text-base font-bold text-thv17-text">Strategy Kit</span>
        <span class="text-[0.82rem] leading-relaxed text-thv17-dim">A modern approach to product design.</span>
      </div>
      <div class="absolute inset-0 flex flex-col gap-2.5 p-7 bg-thv17-amber translate-y-full transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:translate-y-0 group-focus-within:translate-y-0 motion-reduce:transition-none">
        <span class="text-base font-bold text-black">Revealed!</span>
        <span class="text-[0.82rem] leading-relaxed text-black/70">A bottom-up slide reveals the hidden details.</span>
        <a href="#" class="mt-1 inline-flex items-center min-h-11 text-[0.85rem] font-semibold text-black no-underline underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black">Explore →</a>
      </div>
    </div>
    <div class="group relative overflow-hidden min-h-[220px] rounded-2xl bg-white/[0.03] border border-white/[0.08]">
      <div class="absolute inset-0 flex w-[200%] transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:-translate-x-1/2 group-focus-within:-translate-x-1/2 motion-reduce:transition-none">
        <div class="basis-1/2 shrink-0 flex flex-col gap-2.5 p-7">
          <span class="text-2xl text-thv17-amber">⬡</span>
          <span class="text-base font-bold text-thv17-text">Design System</span>
          <span class="text-[0.82rem] leading-relaxed text-thv17-dim">Components that scale.</span>
        </div>
        <div class="basis-1/2 shrink-0 flex flex-col gap-2.5 p-7 bg-thv17-orange">
          <span class="text-base font-bold text-white">Left Push</span>
          <span class="text-[0.82rem] leading-relaxed text-white/85">Content slides out, the reveal slides in.</span>
          <a href="#" class="mt-1 inline-flex items-center min-h-11 text-[0.85rem] font-semibold text-white no-underline underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Open →</a>
        </div>
      </div>
    </div>
    <div class="group relative overflow-hidden min-h-[220px] rounded-2xl bg-white/[0.03] border border-white/[0.08]">
      <div class="flex flex-col gap-2.5 p-7">
        <span class="text-2xl text-thv17-amber">◈</span>
        <span class="text-base font-bold text-thv17-text">Brand Guide</span>
        <span class="text-[0.82rem] leading-relaxed text-thv17-dim">Visual language at scale.</span>
      </div>
      <div class="absolute inset-0 z-10 bg-thv17-warm origin-left scale-x-0 transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:scale-x-100 group-focus-within:scale-x-100 motion-reduce:transition-none"></div>
      <div class="absolute inset-0 z-20 flex flex-col gap-2.5 p-7 bg-thv17-warm opacity-0 transition-opacity duration-200 delay-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">
        <span class="text-base font-bold text-black">Curtain!</span>
        <span class="text-[0.82rem] leading-relaxed text-black/70">A wipe reveals the content beneath.</span>
        <a href="#" class="mt-1 inline-flex items-center min-h-11 text-[0.85rem] font-semibold text-black no-underline underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black">View →</a>
      </div>
    </div>
    <div class="group relative overflow-hidden min-h-[220px] rounded-2xl bg-white/[0.03] border border-white/[0.08]">
      <div class="flex flex-col gap-2.5 p-7">
        <span class="text-2xl text-thv17-amber">✦</span>
        <span class="text-base font-bold text-thv17-text">Case Study</span>
        <span class="text-[0.82rem] leading-relaxed text-thv17-dim">Process and outcomes, detailed.</span>
      </div>
      <div class="absolute inset-0 flex flex-col gap-2.5 p-7 bg-thv17-bg/95 backdrop-blur-[4px] opacity-0 translate-y-2 transition-[opacity,transform] duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-opacity">
        <span class="text-base font-bold text-thv17-text">Dissolve</span>
        <span class="text-[0.82rem] leading-relaxed text-thv17-dim">Opacity fade with a translateY settle.</span>
        <a href="#" class="mt-1 inline-flex items-center min-h-11 text-[0.85rem] font-semibold text-thv17-amber no-underline underline-offset-4 hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-thv17-amber">Read →</a>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv17-bg: #0c0700;
  --color-thv17-bg: oklch(0.12 0.02 70);
  --color-thv17-text: #fef3c7;
  --color-thv17-text: oklch(0.95 0.06 95);
  --color-thv17-dim: #a8a29e;
  --color-thv17-dim: oklch(0.72 0.01 60);
  --color-thv17-amber: #f59e0b;
  --color-thv17-amber: oklch(0.77 0.16 70);
  --color-thv17-orange: #f97316;
  --color-thv17-orange: oklch(0.7 0.19 45);
  --color-thv17-warm: #fbbf24;
  --color-thv17-warm: oklch(0.82 0.16 82);
  --font-thv17-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-17 {
  width: 100%;
  min-height: 100svh;
}

.thv-17 ::selection {
  background: var(--color-thv17-orange);
  color: #fff;
}
```
