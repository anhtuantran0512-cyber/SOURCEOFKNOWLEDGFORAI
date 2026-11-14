---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-on-hover-animation/"
title: "Tailwind Gradient Text on Hover Animation"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "Hover any link or card and the gradient wipes across the letters from left to right."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Text on Hover Animation
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-on-hover-animation/

Hover any link or card and the gradient wipes across the letters from left to right. It's two background layers clipped to the text &mdash; a solid ink layer underneath and a gradient layer whose width animates from 0% to 100%. Unlike the original's instant swap, this is a real, interruptible transition.
## HTML
```html
<section class="ttg-05 w-full min-h-svh grid place-items-center bg-ttg05-bg px-5 py-14 font-ttg05-sans text-ttg05-ink" aria-label="Gradient text on hover demo">
  <div class="w-full max-w-2xl rounded-3xl border border-white/8 bg-ttg05-card p-8 shadow-[0_30px_60px_-30px_rgb(0_0_0/0.7)] max-sm:p-6">
    <p class="font-ttg05-mono text-[11px] tracking-[0.16em] text-ttg05-mut uppercase">Hover or tab through the links</p>
    <nav class="mt-4 flex flex-wrap gap-1" aria-label="Demo">
      <a href="#" class="inline-flex min-h-11 items-center rounded-lg bg-[linear-gradient(90deg,var(--color-ttg05-a),var(--color-ttg05-b)),linear-gradient(var(--color-ttg05-solid),var(--color-ttg05-solid))] bg-[length:0%_100%,100%_100%] bg-no-repeat bg-clip-text px-3.5 text-base font-semibold text-transparent transition-[background-size] duration-500 ease-out hover:bg-[length:100%_100%,100%_100%] focus-visible:bg-[length:100%_100%,100%_100%] focus-visible:outline-2 focus-visible:outline-ttg05-a motion-reduce:transition-none">Home</a>
      <a href="#" class="inline-flex min-h-11 items-center rounded-lg bg-[linear-gradient(90deg,var(--color-ttg05-a),var(--color-ttg05-b)),linear-gradient(var(--color-ttg05-solid),var(--color-ttg05-solid))] bg-[length:0%_100%,100%_100%] bg-no-repeat bg-clip-text px-3.5 text-base font-semibold text-transparent transition-[background-size] duration-500 ease-out hover:bg-[length:100%_100%,100%_100%] focus-visible:bg-[length:100%_100%,100%_100%] focus-visible:outline-2 focus-visible:outline-ttg05-a motion-reduce:transition-none">Features</a>
      <a href="#" class="inline-flex min-h-11 items-center rounded-lg bg-[linear-gradient(90deg,var(--color-ttg05-a),var(--color-ttg05-b)),linear-gradient(var(--color-ttg05-solid),var(--color-ttg05-solid))] bg-[length:0%_100%,100%_100%] bg-no-repeat bg-clip-text px-3.5 text-base font-semibold text-transparent transition-[background-size] duration-500 ease-out hover:bg-[length:100%_100%,100%_100%] focus-visible:bg-[length:100%_100%,100%_100%] focus-visible:outline-2 focus-visible:outline-ttg05-a motion-reduce:transition-none">Pricing</a>
      <a href="#" class="inline-flex min-h-11 items-center rounded-lg bg-[linear-gradient(90deg,var(--color-ttg05-a),var(--color-ttg05-b)),linear-gradient(var(--color-ttg05-solid),var(--color-ttg05-solid))] bg-[length:0%_100%,100%_100%] bg-no-repeat bg-clip-text px-3.5 text-base font-semibold text-transparent transition-[background-size] duration-500 ease-out hover:bg-[length:100%_100%,100%_100%] focus-visible:bg-[length:100%_100%,100%_100%] focus-visible:outline-2 focus-visible:outline-ttg05-a motion-reduce:transition-none">Changelog</a>
      <a href="#" class="inline-flex min-h-11 items-center rounded-lg bg-[linear-gradient(90deg,var(--color-ttg05-a),var(--color-ttg05-b)),linear-gradient(var(--color-ttg05-solid),var(--color-ttg05-solid))] bg-[length:0%_100%,100%_100%] bg-no-repeat bg-clip-text px-3.5 text-base font-semibold text-transparent transition-[background-size] duration-500 ease-out hover:bg-[length:100%_100%,100%_100%] focus-visible:bg-[length:100%_100%,100%_100%] focus-visible:outline-2 focus-visible:outline-ttg05-a motion-reduce:transition-none">Contact</a>
    </nav>
    <div class="my-7 h-px bg-white/8"></div>
    <div class="grid gap-3.5 sm:grid-cols-3">
      <a href="#" class="group rounded-2xl border border-white/8 bg-white/[0.025] p-5 transition hover:-translate-y-0.5 hover:border-ttg05-a/40 hover:bg-white/[0.045] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg05-a motion-reduce:transition-none">
        <h3 class="flex items-center justify-between text-[15.5px] font-bold"><span class="bg-[linear-gradient(90deg,var(--color-ttg05-a),var(--color-ttg05-b)),linear-gradient(var(--color-ttg05-ink),var(--color-ttg05-ink))] bg-[length:0%_100%,100%_100%] bg-no-repeat bg-clip-text text-transparent transition-[background-size] duration-500 group-hover:bg-[length:100%_100%,100%_100%] group-focus-visible:bg-[length:100%_100%,100%_100%] motion-reduce:transition-none">Analytics</span><span aria-hidden="true" class="text-ttg05-mut transition group-hover:translate-x-0.5 group-hover:text-ttg05-b">&rarr;</span></h3>
        <p class="mt-2 text-[13.5px]/[1.6] text-ttg05-mut">Real-time dashboards for every metric your team cares about.</p>
      </a>
      <a href="#" class="group rounded-2xl border border-white/8 bg-white/[0.025] p-5 transition hover:-translate-y-0.5 hover:border-ttg05-a/40 hover:bg-white/[0.045] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg05-a motion-reduce:transition-none">
        <h3 class="flex items-center justify-between text-[15.5px] font-bold"><span class="bg-[linear-gradient(90deg,var(--color-ttg05-a),var(--color-ttg05-b)),linear-gradient(var(--color-ttg05-ink),var(--color-ttg05-ink))] bg-[length:0%_100%,100%_100%] bg-no-repeat bg-clip-text text-transparent transition-[background-size] duration-500 group-hover:bg-[length:100%_100%,100%_100%] group-focus-visible:bg-[length:100%_100%,100%_100%] motion-reduce:transition-none">Integrations</span><span aria-hidden="true" class="text-ttg05-mut transition group-hover:translate-x-0.5 group-hover:text-ttg05-b">&rarr;</span></h3>
        <p class="mt-2 text-[13.5px]/[1.6] text-ttg05-mut">Connect to 200+ tools with one-click OAuth flows.</p>
      </a>
      <a href="#" class="group rounded-2xl border border-white/8 bg-white/[0.025] p-5 transition hover:-translate-y-0.5 hover:border-ttg05-a/40 hover:bg-white/[0.045] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg05-a motion-reduce:transition-none">
        <h3 class="flex items-center justify-between text-[15.5px] font-bold"><span class="bg-[linear-gradient(90deg,var(--color-ttg05-a),var(--color-ttg05-b)),linear-gradient(var(--color-ttg05-ink),var(--color-ttg05-ink))] bg-[length:0%_100%,100%_100%] bg-no-repeat bg-clip-text text-transparent transition-[background-size] duration-500 group-hover:bg-[length:100%_100%,100%_100%] group-focus-visible:bg-[length:100%_100%,100%_100%] motion-reduce:transition-none">Collaboration</span><span aria-hidden="true" class="text-ttg05-mut transition group-hover:translate-x-0.5 group-hover:text-ttg05-b">&rarr;</span></h3>
        <p class="mt-2 text-[13.5px]/[1.6] text-ttg05-mut">Shared workspaces with granular permission controls.</p>
      </a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg05-bg: #0c0c11;
  --color-ttg05-bg: oklch(0.16 0.008 285);
  --color-ttg05-card: #16161e;
  --color-ttg05-card: oklch(0.2 0.012 285);
  --color-ttg05-ink: #eceef3;
  --color-ttg05-ink: oklch(0.95 0.006 270);
  --color-ttg05-solid: #b3b9c6;
  --color-ttg05-solid: oklch(0.79 0.018 265);
  --color-ttg05-mut: #9ba1af;
  --color-ttg05-mut: oklch(0.72 0.018 270);
  --color-ttg05-a: #9b5cf6;
  --color-ttg05-a: oklch(0.64 0.22 295);
  --color-ttg05-b: #f2509a;
  --color-ttg05-b: oklch(0.68 0.21 355);
  --font-ttg05-sans: 'Geist', system-ui, sans-serif;
  --font-ttg05-mono: 'Geist Mono', ui-monospace, monospace;
}

.ttg-05 {
  width: 100%;
  min-height: 100svh;
}
```
