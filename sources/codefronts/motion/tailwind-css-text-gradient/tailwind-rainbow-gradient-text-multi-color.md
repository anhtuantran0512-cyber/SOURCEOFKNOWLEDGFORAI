---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-rainbow-gradient-text-multi-color/"
title: "Tailwind Rainbow Gradient Text (Multi-Color)"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "A full-spectrum rainbow from two colour stops."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Rainbow Gradient Text (Multi-Color)
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-rainbow-gradient-text-multi-color/

A full-spectrum rainbow from two colour stops. v4's /longer interpolation modifier tells the gradient to travel the long way round the oklch hue wheel, so from-ttg15-start to-ttg15-start sweeps all 360°. The animated twin loops seamlessly, and the tag cloud gets matching gradient borders.
## HTML
```html
<section class="ttg-15 w-full min-h-svh grid place-items-center bg-ttg15-bg px-5 py-16 font-ttg15-sans text-ttg15-ink" aria-label="Rainbow gradient text demo">
  <div class="grid w-full max-w-3xl justify-items-center text-center">
    <h1 class="w-fit bg-linear-to-r/longer from-ttg15-start to-ttg15-start bg-clip-text pb-[0.06em] text-[clamp(3.25rem,11vw,6.75rem)] leading-none font-extrabold tracking-[-0.045em] text-transparent">Spectacular</h1>
    <p class="mt-1 w-fit bg-linear-to-r/longer from-ttg15-start to-ttg15-start bg-[length:200%_100%] bg-clip-text pb-[0.06em] text-[clamp(2rem,6.5vw,4rem)] leading-none font-extrabold tracking-[-0.04em] text-transparent animate-ttg15-flow motion-reduce:animate-none">Iridescent</p>
    <ul class="mt-10 flex flex-wrap justify-center gap-2.5" aria-label="Topics">
      <li class="rounded-full border-[1.5px] border-transparent px-4 py-1.5 text-sm font-bold [background:linear-gradient(var(--color-ttg15-bg),var(--color-ttg15-bg))_padding-box,linear-gradient(90deg_in_oklch,var(--color-ttg15-h1),var(--color-ttg15-h2))_border-box]">Design</li>
      <li class="rounded-full border-[1.5px] border-transparent px-4 py-1.5 text-sm font-bold [background:linear-gradient(var(--color-ttg15-bg),var(--color-ttg15-bg))_padding-box,linear-gradient(90deg_in_oklch,var(--color-ttg15-h2),var(--color-ttg15-h3))_border-box]">Colour</li>
      <li class="rounded-full border-[1.5px] border-transparent px-4 py-1.5 text-sm font-bold [background:linear-gradient(var(--color-ttg15-bg),var(--color-ttg15-bg))_padding-box,linear-gradient(90deg_in_oklch,var(--color-ttg15-h3),var(--color-ttg15-h4))_border-box]">Motion</li>
      <li class="rounded-full border-[1.5px] border-transparent px-4 py-1.5 text-sm font-bold [background:linear-gradient(var(--color-ttg15-bg),var(--color-ttg15-bg))_padding-box,linear-gradient(90deg_in_oklch,var(--color-ttg15-h4),var(--color-ttg15-h5))_border-box]">Type</li>
      <li class="rounded-full border-[1.5px] border-transparent px-4 py-1.5 text-sm font-bold [background:linear-gradient(var(--color-ttg15-bg),var(--color-ttg15-bg))_padding-box,linear-gradient(90deg_in_oklch,var(--color-ttg15-h5),var(--color-ttg15-h1))_border-box]">Play</li>
    </ul>
    <p class="mt-8 max-w-md text-[14.5px]/[1.7] text-ttg15-mut text-pretty">Two identical stops plus <code class="rounded bg-white/8 px-1.5 py-0.5 font-ttg15-mono text-[12.5px] text-ttg15-ink">/longer</code> make the gradient travel the long way round the oklch hue wheel &mdash; a full, evenly lit spectrum.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg15-bg: #07050c;
  --color-ttg15-bg: oklch(0.13 0.012 295);
  --color-ttg15-ink: #f1eff6;
  --color-ttg15-ink: oklch(0.96 0.008 295);
  --color-ttg15-mut: #a7a3b4;
  --color-ttg15-mut: oklch(0.75 0.018 295);
  --color-ttg15-start: #ff6b6b;
  --color-ttg15-start: oklch(0.75 0.17 25);
  --color-ttg15-h1: #ff6f6a;
  --color-ttg15-h1: oklch(0.72 0.18 25);
  --color-ttg15-h2: #e7b23b;
  --color-ttg15-h2: oklch(0.8 0.15 85);
  --color-ttg15-h3: #3fcf8e;
  --color-ttg15-h3: oklch(0.77 0.16 155);
  --color-ttg15-h4: #4aa3ff;
  --color-ttg15-h4: oklch(0.7 0.16 250);
  --color-ttg15-h5: #c070ff;
  --color-ttg15-h5: oklch(0.7 0.2 310);
  --font-ttg15-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-ttg15-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-ttg15-flow: ttg15-flow 5s linear infinite;

  @keyframes ttg15-flow {
    from {
      background-position: 0% 50%;
    }

    to {
      background-position: 200% 50%;
    }
  }
}

.ttg-15 {
  width: 100%;
  min-height: 100svh;
}
```
