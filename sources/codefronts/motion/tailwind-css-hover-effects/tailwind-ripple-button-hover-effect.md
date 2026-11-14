---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-ripple-button-hover-effect/"
title: "Tailwind Ripple Button Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Five impact effects — centre ripple, staggered double ring, contained wave, outline-offset ping and a box-shadow glow ring."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Ripple Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-ripple-button-hover-effect/

Five impact effects — centre ripple, staggered double ring, contained wave, outline-offset ping and a box-shadow glow ring. Ripples are one-shot forwards animations minted as --animate-* tokens; the ping and glow need no animation at all.
## HTML
```html
<section class="thv-12 w-full min-h-svh grid place-items-center bg-thv12-bg font-thv12-sans px-6 py-14">
  <div class="w-[min(680px,100%)] flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative shrink-0 min-h-11 px-9 py-3 rounded-lg border-0 bg-thv12-pink text-[0.95rem] font-semibold tracking-[0.05em] text-white cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv12-pink after:content-[''] after:absolute after:top-1/2 after:left-1/2 after:w-full after:h-full after:rounded-full after:bg-white/40 after:-translate-x-1/2 after:-translate-y-1/2 after:scale-0 after:pointer-events-none hover:after:animate-thv12-ripple focus-visible:after:animate-thv12-ripple motion-reduce:hover:after:animate-none">Center Ripple</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv12-dim">scale + opacity keyframe</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative shrink-0 min-h-11 px-9 py-3 rounded-lg border-0 bg-thv12-rose text-[0.95rem] font-semibold tracking-[0.05em] text-white cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv12-rose before:content-[''] before:absolute before:top-1/2 before:left-1/2 before:w-full before:h-full before:rounded-full before:bg-white/30 before:-translate-x-1/2 before:-translate-y-1/2 before:scale-0 before:pointer-events-none after:content-[''] after:absolute after:top-1/2 after:left-1/2 after:w-full after:h-full after:rounded-full after:bg-white/20 after:-translate-x-1/2 after:-translate-y-1/2 after:scale-0 after:pointer-events-none hover:before:animate-thv12-ripple hover:after:animate-thv12-ripple-late focus-visible:before:animate-thv12-ripple focus-visible:after:animate-thv12-ripple-late motion-reduce:hover:before:animate-none motion-reduce:hover:after:animate-none">Double Ring</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv12-dim">staggered dual ripple</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden shrink-0 min-h-11 px-9 py-3 rounded-lg border-2 border-thv12-magenta bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv12-magenta cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv12-magenta before:content-[''] before:absolute before:top-1/2 before:left-1/2 before:w-0 before:h-0 before:rounded-full before:bg-thv12-magenta/25 before:-translate-x-1/2 before:-translate-y-1/2 before:pointer-events-none hover:before:animate-thv12-wave focus-visible:before:animate-thv12-wave motion-reduce:hover:before:animate-none">Contained Wave</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv12-dim">overflow-clipped wave</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="shrink-0 min-h-11 px-9 py-3 rounded-lg border-0 bg-thv12-purple text-[0.95rem] font-semibold tracking-[0.05em] text-white cursor-pointer outline-2 outline-thv12-purple outline-offset-0 transition-[outline-offset,outline-color] duration-400 hover:outline-offset-[10px] hover:outline-transparent focus-visible:outline-offset-[10px] motion-reduce:transition-none">Border Pulse</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv12-dim">outline-offset ping</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-6 px-9 py-6 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="shrink-0 min-h-11 px-9 py-3 rounded-lg border-2 border-thv12-pink bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv12-pink cursor-pointer shadow-[0_0_0_0_rgba(236,72,153,.4)] transition-[box-shadow,color,background-color] duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:bg-thv12-pink hover:shadow-[0_0_0_12px_rgba(236,72,153,0)] focus-visible:text-white focus-visible:bg-thv12-pink focus-visible:shadow-[0_0_0_12px_rgba(236,72,153,0)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv12-pink motion-reduce:transition-none">Glow Ring</button>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv12-dim">box-shadow expand</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv12-bg: #0f0008;
  --color-thv12-bg: oklch(0.12 0.04 350);
  --color-thv12-dim: #6b7280;
  --color-thv12-dim: oklch(0.55 0.02 265);
  --color-thv12-pink: #ec4899;
  --color-thv12-pink: oklch(0.65 0.23 355);
  --color-thv12-rose: #f43f5e;
  --color-thv12-rose: oklch(0.65 0.23 16);
  --color-thv12-magenta: #db2777;
  --color-thv12-magenta: oklch(0.58 0.23 355);
  --color-thv12-purple: #a855f7;
  --color-thv12-purple: oklch(0.65 0.25 303);
  --font-thv12-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-thv12-ripple: thv12-ripple .6s ease-out forwards;
  --animate-thv12-ripple-late: thv12-ripple .7s ease-out .25s forwards;
  --animate-thv12-wave: thv12-wave .6s ease-out forwards;
}

.thv-12 {
  width: 100%;
  min-height: 100svh;
}

.thv-12 ::selection {
  background: var(--color-thv12-magenta);
  color: #fff;
}

@keyframes thv12-ripple {
  0% {
    scale: 0;
    opacity: .7;
  }

  100% {
    scale: 3.5;
    opacity: 0;
  }
}

@keyframes thv12-wave {
  0% {
    width: 0;
    height: 0;
    opacity: .8;
  }

  100% {
    width: 300px;
    height: 300px;
    opacity: 0;
  }
}
```
