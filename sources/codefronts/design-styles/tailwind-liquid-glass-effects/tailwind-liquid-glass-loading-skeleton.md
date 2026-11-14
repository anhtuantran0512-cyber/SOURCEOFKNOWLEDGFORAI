---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-loading-skeleton/"
title: "Tailwind Liquid Glass Loading Skeleton"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A profile-card skeleton where the placeholders are glass rather than grey."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Loading Skeleton
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-loading-skeleton/

A profile-card skeleton where the placeholders are glass rather than grey. One card-wide shimmer sweeps across all of them &mdash; a single animated layer instead of one per block, which is both cheaper and the more convincing illusion of light gliding over a surface.
## HTML
```html
<section class="lgt-19 grid w-full min-h-svh place-items-center p-15 font-lgt19-sans bg-[image:url('https://picsum.photos/seed/lgskel/1100/800')] bg-cover bg-center bg-fixed" aria-label="Tailwind liquid glass loading skeleton">
  <div aria-busy="true" class="relative isolate w-[min(360px,92vw)] overflow-hidden rounded-[24px] border border-white/24 bg-white/9 p-6.5 backdrop-blur-[20px] backdrop-saturate-160 shadow-[inset_0_1px_0_rgba(255,255,255,.35),0_30px_60px_-30px_rgba(0,0,0,.6)] after:pointer-events-none after:absolute after:inset-0 after:z-2 after:animate-lgt19-sweep after:[background:linear-gradient(105deg,transparent_30%,rgba(255,255,255,.28)_48%,transparent_66%)] motion-reduce:after:animate-none motion-reduce:after:opacity-15">
    <span class="sr-only">Loading profile&hellip;</span>

    <div class="mb-5.5 flex items-center gap-4">
      <div class="size-15 flex-none rounded-full border border-white/15 bg-white/16"></div>
      <div class="flex flex-1 flex-col gap-2.25">
        <div class="h-4 w-[65%] rounded-lg border border-white/15 bg-white/16"></div>
        <div class="h-3 w-2/5 rounded-lg border border-white/15 bg-white/16"></div>
      </div>
    </div>

    <div class="mb-3 h-3 w-full rounded-md border border-white/15 bg-white/16"></div>
    <div class="mb-3 h-3 w-full rounded-md border border-white/15 bg-white/16"></div>
    <div class="mb-3 h-3 w-[55%] rounded-md border border-white/15 bg-white/16"></div>

    <div class="mt-4.5 flex items-center justify-between">
      <div class="h-7 w-21 rounded-full border border-white/15 bg-white/16"></div>
      <div class="h-10 w-27.5 rounded-xl border border-white/15 bg-white/16"></div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-lgt19-sans: 'Manrope', system-ui, sans-serif;
  --animate-lgt19-sweep: lgt-19-sweep 1.6s ease-in-out infinite;
}
/* The hold from 60% to 100% is what makes the sweep breathe instead of strobe. */

@keyframes lgt-19-sweep {
  0% {
    transform: translateX(-100%);
  }

  60%,
    100% {
    transform: translateX(100%);
  }
}
```
