---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-inline-word-swap-hover-effect/"
title: "Tailwind Inline Word Swap Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six ways to replace a word on hover — slide up, clip reveal, cross-fade, scale-in, blur swap and a flip-down."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Inline Word Swap Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-inline-word-swap-hover-effect/

Six ways to replace a word on hover — slide up, clip reveal, cross-fade, scale-in, blur swap and a flip-down. Two absolutely stacked spans, one leaving and one arriving, with the incoming word marked aria-hidden.
## HTML
```html
<section class="thv-28 w-full min-h-svh bg-thv28-bg font-thv28-sans px-8 py-12 flex flex-col items-start gap-8 max-w-[640px] mx-auto">
  <p class="self-center text-[0.72rem] tracking-[0.15em] uppercase text-thv28-dim">Inline Word Swap — 6 Styles</p>

  <div class="flex items-center gap-6">
    <a href="#" aria-label="Design Systems" class="group relative inline-block overflow-hidden min-w-[8ch] h-[1.2em] text-[1.6rem] font-bold leading-[1.2] no-underline align-bottom rounded-xs focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv28-acc">
      <span class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-ink transition-transform duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-hover:-translate-y-full group-focus-visible:-translate-y-full motion-reduce:transition-none">Design</span>
      <span aria-hidden="true" class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-acc translate-y-full transition-transform duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-hover:translate-y-0 group-focus-visible:translate-y-0 motion-reduce:transition-none">Systems</span>
    </a>
    <span class="min-w-[90px] text-[0.68rem] tracking-[0.1em] uppercase text-thv28-dim">Slide Up</span>
  </div>

  <div class="flex items-center gap-6">
    <a href="#" aria-label="Make it Work" class="group relative inline-block overflow-hidden min-w-[8ch] h-[1.2em] text-[1.6rem] font-bold leading-[1.2] no-underline align-bottom rounded-xs focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv28-acc">
      <span class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-ink [clip-path:inset(0_0_0_0)] transition-[clip-path] duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-hover:[clip-path:inset(0_0_0_100%)] group-focus-visible:[clip-path:inset(0_0_0_100%)] motion-reduce:transition-none">Make it</span>
      <span aria-hidden="true" class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-acc [clip-path:inset(0_100%_0_0)] transition-[clip-path] duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-hover:[clip-path:inset(0_0_0_0)] group-focus-visible:[clip-path:inset(0_0_0_0)] motion-reduce:transition-none">Work</span>
    </a>
    <span class="min-w-[90px] text-[0.68rem] tracking-[0.1em] uppercase text-thv28-dim">Clip Reveal</span>
  </div>

  <div class="flex items-center gap-6">
    <a href="#" aria-label="Start Now" class="group relative inline-block overflow-hidden min-w-[8ch] h-[1.2em] text-[1.6rem] font-bold leading-[1.2] no-underline align-bottom rounded-xs focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv28-acc">
      <span class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-ink transition-opacity duration-250 group-hover:opacity-0 group-focus-visible:opacity-0">Start</span>
      <span aria-hidden="true" class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-acc opacity-0 transition-opacity duration-250 delay-100 group-hover:opacity-100 group-focus-visible:opacity-100">Now</span>
    </a>
    <span class="min-w-[90px] text-[0.68rem] tracking-[0.1em] uppercase text-thv28-dim">Fade Cross</span>
  </div>

  <div class="flex items-center gap-6">
    <a href="#" aria-label="Build Fast" class="group relative inline-block overflow-hidden min-w-[8ch] h-[1.2em] text-[1.6rem] font-bold leading-[1.2] no-underline align-bottom rounded-xs focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv28-acc">
      <span class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-ink transition-[opacity,transform] duration-250 group-hover:opacity-0 group-hover:scale-125 group-focus-visible:opacity-0 motion-reduce:transition-opacity">Build</span>
      <span aria-hidden="true" class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-acc opacity-0 scale-[.6] transition-[opacity,transform] duration-300 delay-[50ms] ease-[cubic-bezier(.34,1.56,.64,1)] group-hover:opacity-100 group-hover:scale-100 group-focus-visible:opacity-100 group-focus-visible:scale-100 motion-reduce:transition-opacity">Fast</span>
    </a>
    <span class="min-w-[90px] text-[0.68rem] tracking-[0.1em] uppercase text-thv28-dim">Scale In</span>
  </div>

  <div class="flex items-center gap-6">
    <a href="#" aria-label="Ship it" class="group relative inline-block overflow-hidden min-w-[8ch] h-[1.2em] text-[1.6rem] font-bold leading-[1.2] no-underline align-bottom rounded-xs focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv28-acc">
      <span class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-ink transition-[filter,opacity] duration-300 group-hover:blur-[8px] group-hover:opacity-0 group-focus-visible:opacity-0">Ship</span>
      <span aria-hidden="true" class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-acc blur-[8px] opacity-0 transition-[filter,opacity] duration-300 delay-[50ms] group-hover:blur-0 group-hover:opacity-100 group-focus-visible:blur-0 group-focus-visible:opacity-100">it</span>
    </a>
    <span class="min-w-[90px] text-[0.68rem] tracking-[0.1em] uppercase text-thv28-dim">Blur Swap</span>
  </div>

  <div class="flex items-center gap-6">
    <a href="#" aria-label="Create Iterate" class="group relative inline-block overflow-hidden min-w-[8ch] h-[1.2em] perspective-[300px] text-[1.6rem] font-bold leading-[1.2] no-underline align-bottom rounded-xs focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv28-acc">
      <span class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-ink origin-bottom transition-[transform,opacity] duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-hover:rotate-x-90 group-hover:opacity-0 group-focus-visible:rotate-x-90 group-focus-visible:opacity-0 motion-reduce:transition-opacity">Create</span>
      <span aria-hidden="true" class="absolute inset-x-0 top-0 block whitespace-nowrap text-thv28-acc origin-top rotate-x-[-90deg] opacity-0 transition-[transform,opacity] duration-350 delay-[50ms] ease-[cubic-bezier(.4,0,.2,1)] group-hover:rotate-x-0 group-hover:opacity-100 group-focus-visible:rotate-x-0 group-focus-visible:opacity-100 motion-reduce:transition-opacity">Iterate</span>
    </a>
    <span class="min-w-[90px] text-[0.68rem] tracking-[0.1em] uppercase text-thv28-dim">Flip Down</span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv28-bg: #0b0b0e;
  --color-thv28-bg: oklch(0.12 0.01 285);
  --color-thv28-ink: #d5d5da;
  --color-thv28-ink: oklch(0.86 0.01 285);
  --color-thv28-dim: #8a8a96;
  --color-thv28-dim: oklch(0.64 0.01 285);
  --color-thv28-acc: #7c6af7;
  --color-thv28-acc: oklch(0.62 0.2 285);
  --font-thv28-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-28 {
  width: 100%;
  min-height: 100svh;
}

.thv-28 ::selection {
  background: var(--color-thv28-acc);
  color: #fff;
}
```
