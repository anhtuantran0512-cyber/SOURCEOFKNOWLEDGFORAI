---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-3d-press-effect-button/"
title: "Tailwind 3D Press Effect Button with Keycap Depth"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "A keycap that physically sinks into its own platform."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Press Effect Button with Keycap Depth
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-3d-press-effect-button/

A keycap that physically sinks into its own platform. Two properties do all the work, and as utilities the resting and pressed states sit side by side: shadow-[0_6px_0_…] becomes active:shadow-[0_2px_0_…] while the face drops active:translate-y-1.
## HTML
```html
<section class="tab-05 w-full min-h-svh grid place-items-center bg-tab05-bg font-tab05-sans px-6 py-10">
  <div class="flex flex-col items-center gap-10">
    <p class="text-[0.78rem] tracking-[0.12em] uppercase text-tab05-mut m-0">Click or tap the buttons</p>
    <div class="flex flex-wrap justify-center gap-5">
      <button type="button" class="min-h-11 px-9 text-base font-bold tracking-[0.03em] text-white bg-tab05-indigo rounded-[10px] cursor-pointer select-none transition-[translate,box-shadow] duration-[80ms] shadow-[0_6px_0_var(--color-tab05-indigo-deep),0_8px_12px_oklch(0_0_0/0.18)] hover:brightness-105 active:translate-y-1 active:shadow-[0_2px_0_var(--color-tab05-indigo-deep),0_4px_6px_oklch(0_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab05-indigo motion-reduce:transition-none">Purchase Now</button>
      <button type="button" class="min-h-11 px-9 text-base font-bold tracking-[0.03em] text-white bg-tab05-emerald rounded-[10px] cursor-pointer select-none transition-[translate,box-shadow] duration-[80ms] shadow-[0_6px_0_var(--color-tab05-emerald-deep),0_8px_12px_oklch(0_0_0/0.18)] hover:brightness-105 active:translate-y-1 active:shadow-[0_2px_0_var(--color-tab05-emerald-deep),0_4px_6px_oklch(0_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab05-emerald motion-reduce:transition-none">Download App</button>
      <button type="button" class="min-h-11 px-9 text-base font-bold tracking-[0.03em] text-white bg-tab05-rose rounded-[10px] cursor-pointer select-none transition-[translate,box-shadow] duration-[80ms] shadow-[0_6px_0_var(--color-tab05-rose-deep),0_8px_12px_oklch(0_0_0/0.18)] hover:brightness-105 active:translate-y-1 active:shadow-[0_2px_0_var(--color-tab05-rose-deep),0_4px_6px_oklch(0_0_0/0.12)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab05-rose motion-reduce:transition-none">Delete File</button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab05-bg: #f8fafc;
  --color-tab05-bg: oklch(0.98 0.004 250);
  --color-tab05-mut: #64748b;
  --color-tab05-mut: oklch(0.55 0.03 255);
  --color-tab05-indigo: #6366f1;
  --color-tab05-indigo: oklch(0.58 0.21 277);
  --color-tab05-indigo-deep: #3730a3;
  --color-tab05-indigo-deep: oklch(0.38 0.17 277);
  --color-tab05-emerald: #10b981;
  --color-tab05-emerald: oklch(0.7 0.15 163);
  --color-tab05-emerald-deep: #065f46;
  --color-tab05-emerald-deep: oklch(0.42 0.09 163);
  --color-tab05-rose: #f43f5e;
  --color-tab05-rose: oklch(0.63 0.22 15);
  --color-tab05-rose-deep: #9f1239;
  --color-tab05-rose-deep: oklch(0.42 0.16 15);
  --font-tab05-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tab-05 {
  width: 100%;
  min-height: 100svh;
}

.tab-05 ::selection {
  background: var(--color-tab05-indigo);
  color: #fff;
}
```
