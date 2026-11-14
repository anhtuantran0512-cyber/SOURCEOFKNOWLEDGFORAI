---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-hamburger-menus/simple-3-line-tailwind-hamburger-icon-hover-effect/"
title: "Simple 3-Line Tailwind Hamburger Icon Hover Effect"
section: "navigation"
category: "tailwind-hamburger-menus"
category_name: "Tailwind Hamburger Menus"
description: "Five hover treatments for the resting burger &mdash; the micro-interaction users see a hundred times before they ever click."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Simple 3-Line Tailwind Hamburger Icon Hover Effect
Source: https://codefronts.com/navigation/tailwind-hamburger-menus/simple-3-line-tailwind-hamburger-icon-hover-effect/

Five hover treatments for the resting burger &mdash; the micro-interaction users see a hundred times before they ever click. The port's real contribution is enforcement: every group-hover: has a group-focus-visible: twin typed immediately after it, so the keyboard gap that hover-only effects always ship is impossible to miss here.
## HTML
```html
<section class="thb-19 w-full min-h-svh bg-thb19-bg font-thb19-sans text-thb19-ink px-5 py-9" aria-label="Hamburger icon hover effects demo">
  <div class="p-6 rounded-[20px] border border-thb19-edge bg-thb19-bg">
    <header class="flex items-baseline justify-between gap-3 flex-wrap mb-5">
      <h2 class="text-base font-semibold tracking-[-0.01em]">Hover states</h2>
      <span class="text-[11.5px] text-thb19-mut">hover or Tab through &mdash; resting-state micro-interactions</span>
    </header>
    <div class="grid grid-cols-[repeat(auto-fit,minmax(min(118px,100%),1fr))] gap-3.25">
      <figure class="flex flex-col items-center gap-2.75">
        <button type="button" aria-label="Slide-through hover demo" class="group w-full aspect-[1.15] grid place-items-center overflow-hidden rounded-[15px] border border-thb19-edge bg-thb19-card text-thb19-ink cursor-pointer shadow-[0_10px_24px_-20px_oklch(0.3_0.03_255/0.7)] transition-[border-color,translate] duration-250 hover:-translate-y-0.5 hover:border-[color-mix(in_oklch,var(--color-thb19-acc)_45%,var(--color-thb19-edge))] focus-visible:outline-2 focus-visible:outline-thb19-acc focus-visible:outline-offset-2">
          <span class="relative block w-7 h-5 overflow-hidden" aria-hidden="true">
            <i class="absolute left-0 top-0 w-7 h-[2.5px] rounded-sm bg-current after:content-[''] after:absolute after:inset-0 after:rounded-sm after:bg-inherit after:-translate-x-[34px] transition-[translate] duration-350 ease-thb19cut group-hover:translate-x-[34px] group-focus-visible:translate-x-[34px] motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[8.75px] w-7 h-[2.5px] rounded-sm bg-current after:content-[''] after:absolute after:inset-0 after:rounded-sm after:bg-inherit after:-translate-x-[34px] transition-[translate] duration-350 ease-thb19cut delay-[45ms] group-hover:translate-x-[34px] group-focus-visible:translate-x-[34px] motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[17.5px] w-7 h-[2.5px] rounded-sm bg-current after:content-[''] after:absolute after:inset-0 after:rounded-sm after:bg-inherit after:-translate-x-[34px] transition-[translate] duration-350 ease-thb19cut delay-[90ms] group-hover:translate-x-[34px] group-focus-visible:translate-x-[34px] motion-reduce:transition-none"></i>
          </span>
        </button>
        <figcaption class="grid justify-items-center gap-1 text-center"><b class="text-[12.5px] font-semibold">Slide-through</b><code class="font-thb19-mono text-[10px] text-thb19-mut">mask + after: twin</code></figcaption>
      </figure>
      <figure class="flex flex-col items-center gap-2.75">
        <button type="button" aria-label="Stretch hover demo" class="group w-full aspect-[1.15] grid place-items-center rounded-[15px] border border-thb19-edge bg-thb19-card text-thb19-ink cursor-pointer shadow-[0_10px_24px_-20px_oklch(0.3_0.03_255/0.7)] transition-[border-color,translate] duration-250 hover:-translate-y-0.5 hover:border-[color-mix(in_oklch,var(--color-thb19-acc)_45%,var(--color-thb19-edge))] focus-visible:outline-2 focus-visible:outline-thb19-acc focus-visible:outline-offset-2">
          <span class="relative block w-7 h-5" aria-hidden="true">
            <i class="absolute left-0 top-0 w-7 h-[2.5px] rounded-sm bg-current"></i>
            <i class="absolute left-0 top-[8.75px] w-[17px] h-[2.5px] rounded-sm bg-current transition-[width] duration-300 ease-thb19 group-hover:w-7 group-focus-visible:w-7 motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[17.5px] w-7 h-[2.5px] rounded-sm bg-current"></i>
          </span>
        </button>
        <figcaption class="grid justify-items-center gap-1 text-center"><b class="text-[12.5px] font-semibold">Stretch</b><code class="font-thb19-mono text-[10px] text-thb19-mut">middle 17px &rarr; 28px</code></figcaption>
      </figure>
      <figure class="flex flex-col items-center gap-2.75">
        <button type="button" aria-label="Wave hover demo" class="group w-full aspect-[1.15] grid place-items-center rounded-[15px] border border-thb19-edge bg-thb19-card text-thb19-ink cursor-pointer shadow-[0_10px_24px_-20px_oklch(0.3_0.03_255/0.7)] transition-[border-color,translate] duration-250 hover:-translate-y-0.5 hover:border-[color-mix(in_oklch,var(--color-thb19-acc)_45%,var(--color-thb19-edge))] focus-visible:outline-2 focus-visible:outline-thb19-acc focus-visible:outline-offset-2">
          <span class="relative block w-7 h-5" aria-hidden="true">
            <i class="absolute left-0 top-0 w-7 h-[2.5px] rounded-sm bg-current transition-[translate] duration-300 ease-thb19bounce group-hover:translate-y-[3px] group-focus-visible:translate-y-[3px] motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[8.75px] w-7 h-[2.5px] rounded-sm bg-current transition-[translate] duration-300 ease-thb19bounce delay-[50ms] group-hover:translate-y-[3px] group-focus-visible:translate-y-[3px] motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[17.5px] w-7 h-[2.5px] rounded-sm bg-current transition-[translate] duration-300 ease-thb19bounce delay-[100ms] group-hover:translate-y-[3px] group-focus-visible:translate-y-[3px] motion-reduce:transition-none"></i>
          </span>
        </button>
        <figcaption class="grid justify-items-center gap-1 text-center"><b class="text-[12.5px] font-semibold">Wave</b><code class="font-thb19-mono text-[10px] text-thb19-mut">staggered dip + bounce</code></figcaption>
      </figure>
      <figure class="flex flex-col items-center gap-2.75">
        <button type="button" aria-label="Spread hover demo" class="group w-full aspect-[1.15] grid place-items-center rounded-[15px] border border-thb19-edge bg-thb19-card text-thb19-ink cursor-pointer shadow-[0_10px_24px_-20px_oklch(0.3_0.03_255/0.7)] transition-[border-color,translate] duration-250 hover:-translate-y-0.5 hover:border-[color-mix(in_oklch,var(--color-thb19-acc)_45%,var(--color-thb19-edge))] focus-visible:outline-2 focus-visible:outline-thb19-acc focus-visible:outline-offset-2">
          <span class="relative block w-7 h-5" aria-hidden="true">
            <i class="absolute left-0 top-0 w-7 h-[2.5px] rounded-sm bg-current transition-[translate] duration-300 ease-thb19 group-hover:-translate-y-[3px] group-focus-visible:-translate-y-[3px] motion-reduce:transition-none"></i>
            <i class="absolute left-0 top-[8.75px] w-7 h-[2.5px] rounded-sm bg-current"></i>
            <i class="absolute left-0 top-[17.5px] w-7 h-[2.5px] rounded-sm bg-current transition-[translate] duration-300 ease-thb19 group-hover:translate-y-[3px] group-focus-visible:translate-y-[3px] motion-reduce:transition-none"></i>
          </span>
        </button>
        <figcaption class="grid justify-items-center gap-1 text-center"><b class="text-[12.5px] font-semibold">Spread</b><code class="font-thb19-mono text-[10px] text-thb19-mut">outer lines &plusmn;3px</code></figcaption>
      </figure>
      <figure class="flex flex-col items-center gap-2.75">
        <button type="button" aria-label="Tilt hover demo" class="group w-full aspect-[1.15] grid place-items-center rounded-[15px] border border-thb19-edge bg-thb19-card text-thb19-ink cursor-pointer shadow-[0_10px_24px_-20px_oklch(0.3_0.03_255/0.7)] transition-[border-color,translate] duration-250 hover:-translate-y-0.5 hover:border-[color-mix(in_oklch,var(--color-thb19-acc)_45%,var(--color-thb19-edge))] focus-visible:outline-2 focus-visible:outline-thb19-acc focus-visible:outline-offset-2">
          <span class="relative block w-7 h-5 transition-[rotate] duration-450 ease-thb19bounce group-hover:rotate-90 group-focus-visible:rotate-90 motion-reduce:transition-none" aria-hidden="true">
            <i class="absolute left-0 top-0 w-7 h-[2.5px] rounded-sm bg-current"></i>
            <i class="absolute left-0 top-[8.75px] w-7 h-[2.5px] rounded-sm bg-current"></i>
            <i class="absolute left-0 top-[17.5px] w-7 h-[2.5px] rounded-sm bg-current"></i>
          </span>
        </button>
        <figcaption class="grid justify-items-center gap-1 text-center"><b class="text-[12.5px] font-semibold">Tilt</b><code class="font-thb19-mono text-[10px] text-thb19-mut">rotate 90&deg; overshoot</code></figcaption>
      </figure>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thb19-bg: #f4f5f8;
  --color-thb19-bg: oklch(0.965 0.005 250);
  --color-thb19-card: #ffffff;
  --color-thb19-card: oklch(1 0 0);
  --color-thb19-edge: #e1e3ea;
  --color-thb19-edge: oklch(0.89 0.008 250);
  --color-thb19-ink: #32354a;
  --color-thb19-ink: oklch(0.24 0.015 255);
  --color-thb19-mut: #73778a;
  --color-thb19-mut: oklch(0.54 0.012 255);
  --color-thb19-acc: #d4485a;
  --color-thb19-acc: oklch(0.6 0.17 20);
  --font-thb19-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thb19-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-thb19: cubic-bezier(0.2, 0.7, 0.2, 1);
  --ease-thb19cut: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-thb19bounce: cubic-bezier(0.3, 1.6, 0.4, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.thb-19 {
  width: 100%;
  min-height: 100svh;
}
```
