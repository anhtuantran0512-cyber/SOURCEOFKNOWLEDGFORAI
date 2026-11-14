---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-glass-bento-grid-layout/"
title: "Tailwind Glass Bento Grid Layout"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "A liquid-glass bento over a slowly drifting conic mesh, where each tile sets its own refraction with an inline --edge &mdash; 0 for flat frosted panels, 1…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glass Bento Grid Layout
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-glass-bento-grid-layout/

A liquid-glass bento over a slowly drifting conic mesh, where each tile sets its own refraction with an inline --edge &mdash; 0 for flat frosted panels, 1 for a pronounced lensed rim. The animation lives in @theme as --animate-tcg15-bg, which is how v4 mints an animate-* utility from a keyframe.
## HTML
```html
<section class="tcg-15 w-full min-h-svh p-5.5 font-tcg15-sans bg-[conic-gradient(from_20deg_at_40%_30%,#7c3aed,#2563eb,#0891b2,#7c3aed)] bg-[length:200%_200%] animate-tcg15-bg motion-reduce:animate-none" aria-label="Liquid glass bento grid demo">
  <div class="max-w-[640px] mx-auto grid grid-cols-4 max-[520px]:grid-cols-2 [grid-auto-rows:96px] gap-3">

    <a href="#system" style="--edge:1" class="relative isolate col-span-2 row-span-2 flex flex-col justify-end p-4 rounded-[20px] overflow-hidden no-underline text-white bg-[color-mix(in_oklab,white_12%,transparent)] border border-white/32 backdrop-blur-[18px] backdrop-saturate-180 shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_20px_44px_-28px_oklch(0_0_0/0.6)] transition-transform duration-300 hover:-translate-y-[3px] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:absolute after:inset-0 after:rounded-[20px] after:pointer-events-none after:opacity-[var(--edge,0)] after:shadow-[inset_0_0_calc(var(--edge,0)*26px)_calc(var(--edge,0)*6px)_oklch(1_0_0/0.35)]">
      <span class="mb-auto text-[11px] font-extrabold tracking-[0.1em] uppercase opacity-80">Featured</span>
      <h3 class="mt-2 text-2xl font-extrabold leading-[1.2]">Design system v3</h3>
      <p class="mt-1.5 text-[12.5px] text-white/82 text-pretty">72 components shipped this quarter with full Liquid Glass theming.</p>
    </a>

    <a href="#refraction" style="--edge:.6" class="relative isolate col-span-2 row-span-2 flex flex-col justify-end p-4 rounded-[20px] overflow-hidden no-underline text-white bg-[color-mix(in_oklab,white_12%,transparent)] border border-white/32 backdrop-blur-[18px] backdrop-saturate-180 shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_20px_44px_-28px_oklch(0_0_0/0.6)] transition-transform duration-300 hover:-translate-y-[3px] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:absolute after:inset-0 after:rounded-[20px] after:pointer-events-none after:opacity-[var(--edge,0)] after:shadow-[inset_0_0_calc(var(--edge,0)*26px)_calc(var(--edge,0)*6px)_oklch(1_0_0/0.35)]">
      <span class="mb-auto text-[11px] font-extrabold tracking-[0.1em] uppercase opacity-80">Guide</span>
      <h3 class="mt-2 text-lg font-extrabold leading-[1.2]">Refraction 101</h3>
    </a>

    <a href="#demos" style="--edge:0" class="relative isolate flex flex-col justify-end p-4 rounded-[20px] overflow-hidden no-underline text-white bg-[color-mix(in_oklab,white_12%,transparent)] border border-white/32 backdrop-blur-[18px] backdrop-saturate-180 shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_20px_44px_-28px_oklch(0_0_0/0.6)] transition-transform duration-300 hover:-translate-y-[3px] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="text-4xl font-black leading-none tabular-nums">21</span>
      <p class="mt-1.5 text-[12.5px] text-white/82">Demos</p>
    </a>

    <a href="#cls" style="--edge:0" class="relative isolate flex flex-col justify-end p-4 rounded-[20px] overflow-hidden no-underline text-white bg-[color-mix(in_oklab,white_12%,transparent)] border border-white/32 backdrop-blur-[18px] backdrop-saturate-180 shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_20px_44px_-28px_oklch(0_0_0/0.6)] transition-transform duration-300 hover:-translate-y-[3px] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="text-4xl font-black leading-none tabular-nums">0</span>
      <p class="mt-1.5 text-[12.5px] text-white/82">CLS score</p>
    </a>

    <a href="#perf" style="--edge:.4" class="relative isolate col-span-2 flex flex-col justify-end p-4 rounded-[20px] overflow-hidden no-underline text-white bg-[color-mix(in_oklab,white_12%,transparent)] border border-white/32 backdrop-blur-[18px] backdrop-saturate-180 shadow-[inset_0_1px_0_oklch(1_0_0/0.45),0_20px_44px_-28px_oklch(0_0_0/0.6)] transition-transform duration-300 hover:-translate-y-[3px] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0 after:absolute after:inset-0 after:rounded-[20px] after:pointer-events-none after:opacity-[var(--edge,0)] after:shadow-[inset_0_0_calc(var(--edge,0)*26px)_calc(var(--edge,0)*6px)_oklch(1_0_0/0.35)]">
      <span class="mb-auto text-[11px] font-extrabold tracking-[0.1em] uppercase opacity-80">Perf</span>
      <h3 class="mt-2 text-lg font-extrabold leading-[1.2]">60fps, GPU-composited</h3>
    </a>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-tcg15-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tcg15-bg: tcg15-bg 24s ease-in-out infinite;
}
/* Keyframes cannot be a utility, so the body stays here; the @theme entry above
   is what mints the animate-tcg15-bg utility that references it. */

@keyframes tcg15-bg {
  50% {
    background-position: 100% 100%;
  }
}
/* Root rule: the full-bleed contract. */

.tcg-15 {
  width: 100%;
  min-height: 100svh;
}

.tcg-15 ::selection {
  background: #fff;
  color: #2563eb;
}
```
