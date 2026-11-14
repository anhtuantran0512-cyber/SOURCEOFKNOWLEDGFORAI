---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-shimmer-shine-button-hover-effect/"
title: "Tailwind Shimmer Shine Button Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Five reflective button surfaces — diagonal gloss, radial spotlight, frosted double edge, holographic foil and a full shimmer wash."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shimmer Shine Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-shimmer-shine-button-hover-effect/

Five reflective button surfaces — diagonal gloss, radial spotlight, frosted double edge, holographic foil and a full shimmer wash. Each is a gradient on a pseudo-element swept across the face and clipped by overflow-hidden.
## HTML
```html
<section class="thv-09 w-full min-h-svh grid place-items-center bg-thv09-bg font-thv09-sans px-6 py-14">
  <div class="w-[min(680px,100%)] flex flex-col gap-5">
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden shrink-0 min-h-11 px-9 py-3 rounded-lg border-0 bg-thv09-indigo text-[0.95rem] font-semibold tracking-[0.05em] text-white cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv09-indigo before:content-[''] before:absolute before:top-0 before:-left-[75%] before:w-[75%] before:h-full before:pointer-events-none before:[background:linear-gradient(105deg,transparent_0%,rgba(255,255,255,.7)_50%,transparent_100%)] before:transition-[left] before:duration-700 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:left-[125%] focus-visible:before:left-[125%] motion-reduce:before:transition-none">Diagonal Gloss</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv09-dim">translateX streak</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden shrink-0 min-h-11 px-9 py-3 rounded-lg border-0 bg-thv09-violet text-[0.95rem] font-semibold tracking-[0.05em] text-white cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv09-violet before:content-[''] before:absolute before:inset-0 before:opacity-0 before:pointer-events-none before:[background:radial-gradient(circle_at_50%_50%,rgba(255,255,255,.5)_0%,transparent_65%)] before:transition-opacity before:duration-400 hover:before:opacity-100 focus-visible:before:opacity-100">Radial Spotlight</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv09-dim">radial-gradient reveal</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden shrink-0 min-h-11 px-9 py-3 rounded-lg border-2 border-thv09-blue bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv09-blue cursor-pointer transition-shadow duration-400 hover:shadow-[0_0_24px_rgba(59,130,246,.35)] focus-visible:shadow-[0_0_24px_rgba(59,130,246,.35)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv09-blue before:content-[''] before:absolute before:top-0 before:left-0 before:w-[60%] before:h-full before:-translate-x-full before:pointer-events-none before:[background:linear-gradient(90deg,rgba(59,130,246,.55),transparent)] before:transition-transform before:duration-500 after:content-[''] after:absolute after:top-0 after:right-0 after:w-[60%] after:h-full after:translate-x-full after:pointer-events-none after:[background:linear-gradient(270deg,rgba(59,130,246,.55),transparent)] after:transition-transform after:duration-500 hover:before:translate-x-0 hover:after:translate-x-0 focus-visible:before:translate-x-0 focus-visible:after:translate-x-0 motion-reduce:before:transition-none motion-reduce:after:transition-none">Frosted Edge</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv09-dim">edge-shimmer effect</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="shrink-0 min-h-11 px-9 py-3 rounded-lg border-0 text-[0.95rem] font-semibold tracking-[0.05em] text-white cursor-pointer bg-[conic-gradient(from_0deg,#6366f1,#8b5cf6,#ec4899,#f59e0b,#10b981,#06b6d4,#6366f1)] [background-size:200%_200%] [background-position:0%_50%] transition-[background-position,filter] duration-600 hover:[background-position:100%_50%] hover:[filter:brightness(1.2)_saturate(1.3)] focus-visible:[background-position:100%_50%] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white motion-reduce:transition-none">Holographic Foil</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv09-dim">conic-gradient holo</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden shrink-0 min-h-11 px-9 py-3 rounded-lg border-0 bg-[linear-gradient(135deg,var(--color-thv09-sky),var(--color-thv09-indigo))] text-[0.95rem] font-semibold tracking-[0.05em] text-white cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv09-sky before:content-[''] before:absolute before:top-0 before:-left-full before:w-full before:h-full before:pointer-events-none before:[background:linear-gradient(90deg,transparent_0%,rgba(255,255,255,.6)_50%,transparent_100%)] hover:before:animate-thv09-wash focus-visible:before:animate-thv09-wash motion-reduce:hover:before:animate-none">Shimmer Wash</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv09-dim">full-button wave</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv09-bg: #07070f;
  --color-thv09-bg: oklch(0.12 0.02 285);
  --color-thv09-dim: #4b5563;
  --color-thv09-dim: oklch(0.47 0.02 265);
  --color-thv09-indigo: #6366f1;
  --color-thv09-indigo: oklch(0.6 0.2 277);
  --color-thv09-violet: #8b5cf6;
  --color-thv09-violet: oklch(0.63 0.21 295);
  --color-thv09-blue: #3b82f6;
  --color-thv09-blue: oklch(0.64 0.19 258);
  --color-thv09-sky: #0ea5e9;
  --color-thv09-sky: oklch(0.7 0.15 233);
  --font-thv09-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-thv09-wash: thv09-wash .9s ease-in-out forwards;
}

.thv-09 {
  width: 100%;
  min-height: 100svh;
}

.thv-09 ::selection {
  background: var(--color-thv09-indigo);
  color: #fff;
}

@keyframes thv09-wash {
  0% {
    left: -100%;
  }

  100% {
    left: 100%;
  }
}
```
