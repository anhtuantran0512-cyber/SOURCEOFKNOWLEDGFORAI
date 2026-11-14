---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-3d-tilt-card-hover-effect/"
title: "Tailwind 3D Tilt Card Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four perspective cards — fixed diagonal tilt, opposite-axis tilt, a float lift with shadow depth, and translateZ parallax layers."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt Card Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-3d-tilt-card-hover-effect/

Four perspective cards — fixed diagonal tilt, opposite-axis tilt, a float lift with shadow depth, and translateZ parallax layers. v4 ships perspective-*, transform-3d, rotate-x-* and translate-z-*, so this port needs almost no arbitrary values.
## HTML
```html
<section class="thv-13 w-full min-h-svh grid place-items-center bg-thv13-bg font-thv13-sans px-6 py-14">
  <div class="w-[min(800px,100%)] grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-10">
    <div class="perspective-[800px]">
      <button type="button" class="block w-full min-h-[220px] text-left rounded-2xl bg-white/[0.04] border border-white/10 transform-3d cursor-pointer transition-[transform,box-shadow] duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:rotate-x-[8deg] hover:rotate-y-[-8deg] hover:shadow-[8px_12px_40px_rgba(14,165,233,.3)] focus-visible:rotate-x-[8deg] focus-visible:rotate-y-[-8deg] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv13-blue motion-reduce:transition-none motion-reduce:hover:rotate-x-0 motion-reduce:hover:rotate-y-0 motion-reduce:hover:border-thv13-blue">
        <span class="flex flex-col gap-3 p-8">
          <span class="text-3xl text-thv13-blue">◈</span>
          <span class="text-lg font-bold text-thv13-text">Static Tilt</span>
          <span class="text-sm leading-relaxed text-thv13-dim">Perspective rotateX + rotateY on hover.</span>
        </span>
      </button>
    </div>
    <div class="perspective-[800px]">
      <button type="button" class="block w-full min-h-[220px] text-left rounded-2xl bg-white/[0.04] border border-thv13-indigo/30 transform-3d cursor-pointer transition-[transform,box-shadow,border-color] duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:rotate-x-[-6deg] hover:rotate-y-[10deg] hover:border-thv13-indigo/60 hover:shadow-[-10px_8px_40px_rgba(99,102,241,.3)] focus-visible:rotate-x-[-6deg] focus-visible:rotate-y-[10deg] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv13-indigo motion-reduce:transition-none motion-reduce:hover:rotate-x-0 motion-reduce:hover:rotate-y-0">
        <span class="flex flex-col gap-3 p-8">
          <span class="text-3xl text-thv13-indigo">⬡</span>
          <span class="text-lg font-bold text-thv13-text">Axis Flip</span>
          <span class="text-sm leading-relaxed text-thv13-dim">Opposite-axis lean with a matching cast shadow.</span>
        </span>
      </button>
    </div>
    <div>
      <button type="button" class="block w-full min-h-[220px] text-left rounded-2xl bg-white/[0.04] border border-thv13-teal/30 shadow-[0_4px_20px_rgba(0,0,0,.4)] cursor-pointer transition-[transform,box-shadow] duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:-translate-y-[14px] hover:shadow-[0_28px_60px_rgba(0,0,0,.5),0_0_30px_rgba(20,184,166,.2)] focus-visible:-translate-y-[14px] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv13-teal motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <span class="flex flex-col gap-3 p-8">
          <span class="text-3xl text-thv13-teal">▲</span>
          <span class="text-lg font-bold text-thv13-text">Float Lift</span>
          <span class="text-sm leading-relaxed text-thv13-dim">translateY plus a longer cast shadow.</span>
        </span>
      </button>
    </div>
    <div class="perspective-[800px]">
      <button type="button" class="group relative block w-full min-h-[220px] text-left rounded-2xl bg-white/[0.04] border border-thv13-sky/30 transform-3d cursor-pointer transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:rotate-x-[6deg] hover:rotate-y-[-6deg] focus-visible:rotate-x-[6deg] focus-visible:rotate-y-[-6deg] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv13-sky motion-reduce:transition-none motion-reduce:hover:rotate-x-0 motion-reduce:hover:rotate-y-0">
        <span class="absolute inset-0 rounded-2xl bg-[linear-gradient(135deg,rgba(14,165,233,.1),rgba(56,189,248,.05))]"></span>
        <span class="absolute inset-0 flex items-start p-8 transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:translate-z-[20px] group-hover:-translate-y-1.5 group-focus-visible:translate-z-[20px]"><span class="text-4xl text-thv13-sky">◉</span></span>
        <span class="absolute inset-0 flex flex-col justify-end gap-2 p-7 transition-transform duration-400 ease-[cubic-bezier(.4,0,.2,1)] group-hover:translate-z-[35px] group-hover:-translate-y-1 group-focus-visible:translate-z-[35px]">
          <span class="text-lg font-bold text-thv13-text">Parallax</span>
          <span class="text-sm leading-relaxed text-thv13-dim">translateZ layered depth.</span>
        </span>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv13-bg: #020810;
  --color-thv13-bg: oklch(0.12 0.02 250);
  --color-thv13-text: #bae6fd;
  --color-thv13-text: oklch(0.89 0.07 225);
  --color-thv13-dim: #64748b;
  --color-thv13-dim: oklch(0.55 0.03 257);
  --color-thv13-blue: #0ea5e9;
  --color-thv13-blue: oklch(0.7 0.15 233);
  --color-thv13-sky: #38bdf8;
  --color-thv13-sky: oklch(0.76 0.13 226);
  --color-thv13-indigo: #6366f1;
  --color-thv13-indigo: oklch(0.6 0.2 277);
  --color-thv13-teal: #14b8a6;
  --color-thv13-teal: oklch(0.72 0.13 180);
  --font-thv13-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-13 {
  width: 100%;
  min-height: 100svh;
}

.thv-13 ::selection {
  background: var(--color-thv13-blue);
  color: #fff;
}
```
