---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-minimalist-elevation-dynamic-shadow-card/"
title: "Tailwind Minimalist Elevation Card with Layered Dynamic Shadows"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "The restrained one: nearly flat at rest, then an 8px lift and a four-layer shadow that reads as light blocked at four distances."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Elevation Card with Layered Dynamic Shadows
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-minimalist-elevation-dynamic-shadow-card/

The restrained one: nearly flat at rest, then an 8px lift and a four-layer shadow that reads as light blocked at four distances. The port's lesson is where shadows belong &mdash; two multi-layer stacks used by one element each go in @theme as --shadow-* entries, which is what turns them into shadow-tch06-rest and shadow-tch06-lift.
## HTML
```html
<section class="tch-06 w-full min-h-svh grid place-items-center bg-tch06-bg font-tch06-sans p-8">
  <article class="group relative w-[340px] min-h-[420px] p-[2.2rem] rounded-2xl bg-white border border-tch06-edge text-tch06-ink flex flex-col cursor-pointer shadow-tch06-rest transition-[translate,box-shadow,border-color] duration-350 ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:-translate-y-2 hover:border-tch06-edge2 hover:shadow-tch06-lift focus-within:-translate-y-2 focus-within:shadow-tch06-lift motion-reduce:transition-none motion-reduce:hover:translate-y-0">
    <div class="grid place-items-center size-13 rounded-[13px] bg-linear-to-br from-tch06-acc to-tch06-acc2 text-white text-2xl shadow-[0_6px_14px_var(--color-tch06-acc2)]/30">⌘</div>
    <span class="mt-6 text-[0.72rem] tracking-[0.14em] uppercase text-tch06-mut">Documentation</span>
    <h2 class="font-tch06-display font-medium text-[1.9rem] leading-[1.15] mt-1.5">Quickstart<br>in 5 minutes</h2>
    <p class="text-[0.9rem] leading-[1.65] text-tch06-body mt-3.5">Install the SDK, authenticate, and ship your first request. The card lifts gently off the page as you focus it.</p>
    <a href="#" class="mt-auto inline-flex items-center gap-1.5 min-h-11 text-[0.88rem] font-semibold text-tch06-acc2 no-underline rounded-md focus-visible:outline-2 focus-visible:outline-tch06-acc2 focus-visible:outline-offset-2">Read the guide <span class="transition-transform duration-350 group-hover:translate-x-1 motion-reduce:transition-none" aria-hidden="true">→</span></a>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch06-bg: #f7f8fa;
  --color-tch06-bg: oklch(0.98 0.003 255);
  --color-tch06-edge: #e7e9ee;
  --color-tch06-edge: oklch(0.93 0.005 255);
  --color-tch06-edge2: #dfe2e8;
  --color-tch06-edge2: oklch(0.9 0.006 255);
  --color-tch06-ink: #1c2230;
  --color-tch06-ink: oklch(0.25 0.02 255);
  --color-tch06-body: #5c6678;
  --color-tch06-body: oklch(0.49 0.02 255);
  --color-tch06-mut: #8a94a6;
  --color-tch06-mut: oklch(0.65 0.02 255);
  --color-tch06-acc: #3b82f6;
  --color-tch06-acc: oklch(0.62 0.19 259);
  --color-tch06-acc2: #2563eb;
  --color-tch06-acc2: oklch(0.54 0.22 262);
  --font-tch06-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tch06-display: 'Newsreader', Georgia, serif;
  --shadow-tch06-rest: 0 1px 2px oklch(0.25 0.03 255 / 0.04), 0 2px 4px oklch(0.25 0.03 255 / 0.03);
  --shadow-tch06-lift: 0 2px 4px oklch(0.25 0.03 255 / 0.04), 0 6px 12px oklch(0.25 0.03 255 / 0.06), 0 14px 28px oklch(0.25 0.03 255 / 0.08), 0 28px 56px oklch(0.25 0.03 255 / 0.1);
}

.tch-06 {
  width: 100%;
  min-height: 100svh;
}
```
