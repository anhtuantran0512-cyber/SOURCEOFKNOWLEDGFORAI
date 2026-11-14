---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-scattered-photo-collage-target-spotlight/"
title: "Tailwind Scattered Photo Collage with :target Spotlight"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A casual collage strewn across a board at random angles; click any photograph and it springs to the centre, straightens and rises above the pile."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scattered Photo Collage with :target Spotlight
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-scattered-photo-collage-target-spotlight/

A casual collage strewn across a board at random angles; click any photograph and it springs to the centre, straightens and rises above the pile. Deep-linkable, keyboard-operable and script-free — and the port is where Tailwind's ! important modifier earns its place.
## HTML
```html
<section class="tgl-22 relative w-full min-h-svh flex flex-col items-center justify-center gap-4 bg-tgl22-bg font-tgl22-sans px-5 py-10" id="tgl-22" aria-label="Scattered photos collage">
  <a href="#tgl-22" aria-label="Reset collage" class="absolute inset-0 z-0"></a>
  <div class="relative z-[1] w-[min(820px,100%)] [aspect-ratio:16/10]">
    <a id="tgl-22-1" href="#tgl-22-1" style="--rot:-8deg;top:8%;left:10%" class="absolute w-[26%] p-2 rounded-sm overflow-hidden bg-tgl22-print no-underline origin-center [transform:rotate(var(--rot))] shadow-[0_12px_28px_-12px_rgba(0,0,0,0.7)] transition-transform duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:z-[6] hover:[transform:rotate(var(--rot))_scale(1.04)] target:top-1/2! target:left-1/2! target:z-[10] target:[transform:translate(-50%,-50%)_rotate(0deg)_scale(1.5)] focus-visible:outline-3 focus-visible:outline-tgl22-acc focus-visible:outline-offset-[3px] motion-reduce:transition-none max-[560px]:w-[38%]"><img src="https://images.unsplash.com/photo-1501554728187-ce583db33af7?q=80&w=400&h=300&auto=format&fit=crop" alt="Harbour town from the ferry" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover bg-tgl22-well"></a>
    <a id="tgl-22-2" href="#tgl-22-2" style="--rot:6deg;top:14%;left:38%" class="absolute w-[26%] p-2 rounded-sm overflow-hidden bg-tgl22-print no-underline origin-center [transform:rotate(var(--rot))] shadow-[0_12px_28px_-12px_rgba(0,0,0,0.7)] transition-transform duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:z-[6] hover:[transform:rotate(var(--rot))_scale(1.04)] target:top-1/2! target:left-1/2! target:z-[10] target:[transform:translate(-50%,-50%)_rotate(0deg)_scale(1.5)] focus-visible:outline-3 focus-visible:outline-tgl22-acc focus-visible:outline-offset-[3px] motion-reduce:transition-none max-[560px]:w-[38%]"><img src="https://images.unsplash.com/photo-1589003077984-894e133dabab?q=80&w=400&h=300&auto=format&fit=crop" alt="Friends around a table" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover bg-tgl22-well"></a>
    <a id="tgl-22-3" href="#tgl-22-3" style="--rot:-5deg;top:10%;left:64%" class="absolute w-[26%] p-2 rounded-sm overflow-hidden bg-tgl22-print no-underline origin-center [transform:rotate(var(--rot))] shadow-[0_12px_28px_-12px_rgba(0,0,0,0.7)] transition-transform duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:z-[6] hover:[transform:rotate(var(--rot))_scale(1.04)] target:top-1/2! target:left-1/2! target:z-[10] target:[transform:translate(-50%,-50%)_rotate(0deg)_scale(1.5)] focus-visible:outline-3 focus-visible:outline-tgl22-acc focus-visible:outline-offset-[3px] motion-reduce:transition-none max-[560px]:w-[38%]"><img src="https://images.unsplash.com/photo-1522312346375-d1a52e2b99b3?q=80&w=400&h=300&auto=format&fit=crop" alt="City street in the evening" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover bg-tgl22-well"></a>
    <a id="tgl-22-4" href="#tgl-22-4" style="--rot:9deg;top:46%;left:18%" class="absolute w-[26%] p-2 rounded-sm overflow-hidden bg-tgl22-print no-underline origin-center [transform:rotate(var(--rot))] shadow-[0_12px_28px_-12px_rgba(0,0,0,0.7)] transition-transform duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:z-[6] hover:[transform:rotate(var(--rot))_scale(1.04)] target:top-1/2! target:left-1/2! target:z-[10] target:[transform:translate(-50%,-50%)_rotate(0deg)_scale(1.5)] focus-visible:outline-3 focus-visible:outline-tgl22-acc focus-visible:outline-offset-[3px] motion-reduce:transition-none max-[560px]:w-[38%]"><img src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=400&h=300&auto=format&fit=crop" alt="Trail through tall grass" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover bg-tgl22-well"></a>
    <a id="tgl-22-5" href="#tgl-22-5" style="--rot:-7deg;top:50%;left:48%" class="absolute w-[26%] p-2 rounded-sm overflow-hidden bg-tgl22-print no-underline origin-center [transform:rotate(var(--rot))] shadow-[0_12px_28px_-12px_rgba(0,0,0,0.7)] transition-transform duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:z-[6] hover:[transform:rotate(var(--rot))_scale(1.04)] target:top-1/2! target:left-1/2! target:z-[10] target:[transform:translate(-50%,-50%)_rotate(0deg)_scale(1.5)] focus-visible:outline-3 focus-visible:outline-tgl22-acc focus-visible:outline-offset-[3px] motion-reduce:transition-none max-[560px]:w-[38%]"><img src="https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?q=80&w=400&h=300&auto=format&fit=crop" alt="Dinner spread on a long table" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover bg-tgl22-well"></a>
    <a id="tgl-22-6" href="#tgl-22-6" style="--rot:4deg;top:44%;left:70%" class="absolute w-[26%] p-2 rounded-sm overflow-hidden bg-tgl22-print no-underline origin-center [transform:rotate(var(--rot))] shadow-[0_12px_28px_-12px_rgba(0,0,0,0.7)] transition-transform duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:z-[6] hover:[transform:rotate(var(--rot))_scale(1.04)] target:top-1/2! target:left-1/2! target:z-[10] target:[transform:translate(-50%,-50%)_rotate(0deg)_scale(1.5)] focus-visible:outline-3 focus-visible:outline-tgl22-acc focus-visible:outline-offset-[3px] motion-reduce:transition-none max-[560px]:w-[38%]"><img src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=400&h=300&auto=format&fit=crop" alt="Beach umbrellas at midday" loading="lazy" decoding="async" class="block w-full [aspect-ratio:4/3] object-cover bg-tgl22-well"></a>
  </div>
  <p class="relative z-[1] m-0 font-tgl22-mono text-[11px] tracking-[0.14em] uppercase text-tgl22-mut">click a photo to bring it forward &middot; click the background to reset</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl22-bg: #1c1a17;
  --color-tgl22-bg: oklch(0.21 0.008 70);
  --color-tgl22-print: #fffdf8;
  --color-tgl22-print: oklch(0.99 0.006 90);
  --color-tgl22-well: #e0dacd;
  --color-tgl22-well: oklch(0.89 0.014 85);
  --color-tgl22-mut: #a79c8c;
  --color-tgl22-mut: oklch(0.7 0.02 80);
  --color-tgl22-acc: #5f8fdc;
  --color-tgl22-acc: oklch(0.66 0.14 250);
  --font-tgl22-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tgl22-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.tgl-22 {
  width: 100%;
  min-height: 100svh;
}

.tgl-22 ::selection {
  background: var(--color-tgl22-acc);
  color: #fff;
}
```
