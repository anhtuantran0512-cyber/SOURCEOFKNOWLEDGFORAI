---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-glassmorphism-card-hover-effect/"
title: "Tailwind Glassmorphism Card Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four frosted panels — clarity increase, edge glow, depth stack and a specular sweep — over a blurred orb field."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Card Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-glassmorphism-card-hover-effect/

Four frosted panels — clarity increase, edge glow, depth stack and a specular sweep — over a blurred orb field. backdrop-blur-* is a core utility, so the whole glass recipe is four tokens: translucent background, blur, hairline border, shadow.
## HTML
```html
<section class="thv-15 relative overflow-hidden w-full min-h-svh grid place-items-center bg-thv15-bg font-thv15-sans px-6 py-14">
  <div aria-hidden="true" class="absolute inset-0 pointer-events-none">
    <span class="absolute -top-24 -left-24 w-[400px] h-[400px] rounded-full bg-thv15-purple opacity-45 blur-[80px]"></span>
    <span class="absolute -bottom-20 -right-16 w-[350px] h-[350px] rounded-full bg-thv15-pink opacity-45 blur-[80px]"></span>
    <span class="absolute top-[30%] left-[40%] w-[280px] h-[280px] rounded-full bg-thv15-cyan opacity-45 blur-[80px]"></span>
  </div>
  <div class="relative z-10 w-[min(760px,100%)] grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-7">
    <button type="button" class="flex flex-col gap-3.5 p-8 text-left rounded-3xl bg-white/6 backdrop-blur-md border border-white/12 cursor-pointer transition-[background-color,backdrop-filter,border-color,transform] duration-400 hover:bg-white/14 hover:backdrop-blur-xl hover:border-white/25 hover:-translate-y-1 focus-visible:bg-white/14 focus-visible:-translate-y-1 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white/70 motion-reduce:transition-colors motion-reduce:hover:translate-y-0">
      <span class="text-2xl text-thv15-text">✦</span>
      <span class="text-base font-bold text-thv15-text">Frosted Clarity</span>
      <span class="text-sm leading-relaxed text-thv15-dim">Blur depth increases on hover, making the panel appear to thicken.</span>
    </button>
    <button type="button" class="flex flex-col gap-3.5 p-8 text-left rounded-3xl bg-white/6 backdrop-blur-md border border-white/12 cursor-pointer transition-[background-color,border-color,box-shadow] duration-400 hover:bg-thv15-purple/10 hover:border-thv15-purple/60 hover:shadow-[0_0_0_1px_rgba(124,58,237,.3),0_0_24px_rgba(124,58,237,.4),inset_0_0_24px_rgba(124,58,237,.05)] focus-visible:border-thv15-purple/60 focus-visible:shadow-[0_0_24px_rgba(124,58,237,.4)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv15-purple motion-reduce:transition-none">
      <span class="text-2xl text-thv15-text">◉</span>
      <span class="text-base font-bold text-thv15-text">Edge Glow</span>
      <span class="text-sm leading-relaxed text-thv15-dim">Border lights up with accent colour and a matching halo.</span>
    </button>
    <button type="button" class="flex flex-col gap-3.5 p-8 text-left rounded-3xl bg-white/6 backdrop-blur-md border border-white/12 shadow-[0_4px_20px_rgba(0,0,0,.2)] cursor-pointer transition-[transform,box-shadow,background-color,border-color] duration-400 hover:-translate-y-2 hover:bg-white/10 hover:border-white/20 hover:shadow-[0_2px_8px_rgba(0,0,0,.2),0_16px_40px_rgba(0,0,0,.4),0_32px_60px_rgba(0,0,0,.2)] focus-visible:-translate-y-2 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white/70 motion-reduce:transition-colors motion-reduce:hover:translate-y-0">
      <span class="text-2xl text-thv15-text">⬡</span>
      <span class="text-base font-bold text-thv15-text">Depth Stack</span>
      <span class="text-sm leading-relaxed text-thv15-dim">Layered shadows separate on hover, revealing depth.</span>
    </button>
    <button type="button" class="relative overflow-hidden flex flex-col gap-3.5 p-8 text-left rounded-3xl bg-white/6 backdrop-blur-md border border-white/12 cursor-pointer transition-[background-color,border-color] duration-400 hover:bg-white/10 hover:border-white/20 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white/70 before:content-[''] before:absolute before:-top-1/2 before:-left-[60%] before:w-[40%] before:h-[200%] before:-skew-x-[20deg] before:pointer-events-none before:[background:linear-gradient(105deg,transparent,rgba(255,255,255,.12),transparent)] before:transition-[left] before:duration-500 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:left-[120%] focus-visible:before:left-[120%] motion-reduce:before:transition-none">
      <span class="text-2xl text-thv15-text">◈</span>
      <span class="text-base font-bold text-thv15-text">Reflection</span>
      <span class="text-sm leading-relaxed text-thv15-dim">A specular highlight sweeps across the glass surface.</span>
    </button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv15-bg: #080514;
  --color-thv15-bg: oklch(0.12 0.03 290);
  --color-thv15-text: #e2d9f3;
  --color-thv15-text: oklch(0.9 0.04 295);
  --color-thv15-dim: #b3aec4;
  --color-thv15-dim: oklch(0.75 0.02 295);
  --color-thv15-purple: #7c3aed;
  --color-thv15-purple: oklch(0.54 0.25 295);
  --color-thv15-pink: #ec4899;
  --color-thv15-pink: oklch(0.65 0.23 355);
  --color-thv15-cyan: #06b6d4;
  --color-thv15-cyan: oklch(0.71 0.14 208);
  --font-thv15-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-15 {
  width: 100%;
  min-height: 100svh;
}

.thv-15 ::selection {
  background: var(--color-thv15-purple);
  color: #fff;
}
```
