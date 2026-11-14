---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-sidebar-navigation/"
title: "Tailwind Liquid Glass Sidebar Navigation"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A collapsible dashboard shell that re-tints and re-sizes itself from two checkboxes and zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Sidebar Navigation
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-sidebar-navigation/

A collapsible dashboard shell that re-tints and re-sizes itself from two checkboxes and zero JavaScript. This is the demo where v4's token model pays off hardest: has-[#lgt-15-theme:checked]: re-points the palette variables, and every bg-lgt15-surface in the markup changes meaning at once.
## HTML
```html
<section class="lgt-15 relative flex w-full min-h-svh overflow-hidden bg-lgt15-bg font-lgt15-sans" aria-label="Tailwind liquid glass sidebar navigation">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0">
    <span class="absolute -top-10 left-30 size-70 animate-lgt15-float rounded-full bg-lgt15-blob1 opacity-70 blur-[40px] motion-reduce:animate-none"></span>
    <span class="absolute -bottom-8 left-10 size-60 animate-lgt15-float rounded-full bg-lgt15-blob2 opacity-70 blur-[40px] [animation-delay:-4s] motion-reduce:animate-none"></span>
    <span class="absolute top-2/5 -right-10 size-75 animate-lgt15-float rounded-full bg-lgt15-blob3 opacity-70 blur-[40px] [animation-delay:-8s] motion-reduce:animate-none"></span>
  </div>

  <input type="checkbox" id="lgt-15-collapse" class="sr-only">
  <input type="checkbox" id="lgt-15-theme" class="sr-only">

  <aside class="relative z-2 m-4 flex w-(--w) flex-none flex-col gap-2 rounded-[22px] border border-lgt15-rim bg-lgt15-surface p-3.5 pt-4.5 backdrop-blur-[24px] backdrop-saturate-180 shadow-[inset_0_1px_0_var(--color-lgt15-rim),0_30px_60px_-30px_rgba(0,0,0,.4)] transition-[width] duration-350 ease-out motion-reduce:transition-none">
    <div class="flex items-center gap-3 px-2.5 pt-2 pb-3.5 text-lgt15-fg">
      <span class="flex-none text-[22px] text-lgt15-active">&#9670;</span>
      <span class="lgt-15-label overflow-hidden text-[19px] font-bold whitespace-nowrap transition-opacity duration-200">Nimbus</span>
    </div>

    <nav class="flex flex-1 flex-col gap-1" aria-label="Dashboard">
      <a href="#lgt-15" aria-current="page" class="flex items-center gap-3.5 rounded-[12px] px-3 py-2.75 text-sm font-semibold text-lgt15-muted no-underline transition-colors duration-200 hover:bg-lgt15-fg/10 hover:text-lgt15-fg focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-lgt15-active aria-[current=page]:bg-lgt15-active aria-[current=page]:text-white aria-[current=page]:shadow-[inset_0_1px_0_rgba(255,255,255,.4)]"><span class="w-5 flex-none text-center text-[17px]">&#9636;</span><span class="lgt-15-label overflow-hidden whitespace-nowrap transition-opacity duration-200">Overview</span></a>
      <a href="#lgt-15" class="flex items-center gap-3.5 rounded-[12px] px-3 py-2.75 text-sm font-semibold text-lgt15-muted no-underline transition-colors duration-200 hover:bg-lgt15-fg/10 hover:text-lgt15-fg focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-lgt15-active"><span class="w-5 flex-none text-center text-[17px]">&#9707;</span><span class="lgt-15-label overflow-hidden whitespace-nowrap transition-opacity duration-200">Projects</span></a>
      <a href="#lgt-15" class="flex items-center gap-3.5 rounded-[12px] px-3 py-2.75 text-sm font-semibold text-lgt15-muted no-underline transition-colors duration-200 hover:bg-lgt15-fg/10 hover:text-lgt15-fg focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-lgt15-active"><span class="w-5 flex-none text-center text-[17px]">&#9776;</span><span class="lgt-15-label overflow-hidden whitespace-nowrap transition-opacity duration-200">Tasks</span></a>
      <a href="#lgt-15" class="flex items-center gap-3.5 rounded-[12px] px-3 py-2.75 text-sm font-semibold text-lgt15-muted no-underline transition-colors duration-200 hover:bg-lgt15-fg/10 hover:text-lgt15-fg focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-lgt15-active"><span class="w-5 flex-none text-center text-[17px]">&#9677;</span><span class="lgt-15-label overflow-hidden whitespace-nowrap transition-opacity duration-200">Reports</span></a>
    </nav>

    <div class="flex flex-col gap-1 border-t border-lgt15-rim pt-2.5">
      <label for="lgt-15-theme" class="flex cursor-pointer items-center gap-3.5 rounded-[12px] px-3 py-2.75 text-sm font-semibold text-lgt15-muted transition-colors duration-200 hover:bg-lgt15-fg/10 hover:text-lgt15-fg"><span class="w-5 flex-none text-center text-[17px]">&#9680;</span><span class="lgt-15-label overflow-hidden whitespace-nowrap transition-opacity duration-200">Dark mode</span></label>
      <label for="lgt-15-collapse" class="flex cursor-pointer items-center gap-3.5 rounded-[12px] px-3 py-2.75 text-sm font-semibold text-lgt15-muted transition-colors duration-200 hover:bg-lgt15-fg/10 hover:text-lgt15-fg"><span class="w-5 flex-none text-center text-[17px]">&#8660;</span><span class="lgt-15-label overflow-hidden whitespace-nowrap transition-opacity duration-200">Collapse</span></label>
    </div>
  </aside>

  <div class="relative z-2 flex-1 px-10 py-15 text-lgt15-fg">
    <h3 class="mb-2.5 text-3xl font-extrabold">Dashboard</h3>
    <p class="max-w-[44ch] text-base leading-relaxed text-lgt15-muted">Toggle dark mode or collapse &mdash; the shell re-points its theme variables through CSS <code>:has()</code>, so every utility changes meaning at once. No JavaScript.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt15-bg: #dfe6f5;
  --color-lgt15-surface: rgb(255 255 255 / 0.55);
  --color-lgt15-fg: #1a1730;
  --color-lgt15-muted: rgb(26 23 48 / 0.66);
  --color-lgt15-rim: rgb(255 255 255 / 0.8);
  --color-lgt15-active: #7c5cf0;
  --color-lgt15-active: oklch(0.66 0.18 285);
  --color-lgt15-blob1: oklch(0.7 0.2 300);
  --color-lgt15-blob2: oklch(0.72 0.18 200);
  --color-lgt15-blob3: oklch(0.72 0.17 40);
  --font-lgt15-sans: 'Manrope', system-ui, sans-serif;
  --animate-lgt15-float: lgt-15-float 14s ease-in-out infinite;
}

.lgt-15 {
  --w: 230px;
}
/* A descendant checkbox restyling its ancestor: the whole shell, in two rules. */

.lgt-15:has(#lgt-15-theme:checked) {
  --color-lgt15-bg: #0e0b1a;
  --color-lgt15-surface: rgb(255 255 255 / 0.10);
  --color-lgt15-fg: #f2f0fa;
  --color-lgt15-muted: rgb(255 255 255 / 0.7);
  --color-lgt15-rim: rgb(255 255 255 / 0.3);
}

.lgt-15:has(#lgt-15-collapse:checked) {
  --w: 78px;
}

.lgt-15:has(#lgt-15-collapse:checked) .lgt-15-label {
  opacity: 0;
}

@keyframes lgt-15-float {
  0%,
    100% {
    transform: translate(0, 0);
  }

  50% {
    transform: translate(24px, -20px);
  }
}
```
