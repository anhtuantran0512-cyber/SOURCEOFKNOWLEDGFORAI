---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/brutalist-sidebar-navigation-tailwind-css/"
title: "Brutalist Sidebar Navigation in Tailwind CSS"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "Structure as decoration: a black slab with a 4px red rule, condensed 900-weight uppercase links prefixed by monospace //, and a hover that slams to full…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Sidebar Navigation in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-side-menus/brutalist-sidebar-navigation-tailwind-css/

Structure as decoration: a black slab with a 4px red rule, condensed 900-weight uppercase links prefixed by monospace //, and a hover that slams to full yellow with black ink. The active row fills solid red and grows an arrow via aria-[current=page]:after:content-['→']. Zero gradients, zero radii — and every state is now visible to keyboard users, not just the mouse.
## HTML
```html
<section class="tsm-12 flex w-full min-h-svh border-[3px] border-tsm12-ink bg-tsm12-paper font-tsm12-head text-tsm12-ink" aria-label="Brutalist sidebar navigation demo">
  <nav aria-label="Main" class="flex w-52 shrink-0 flex-col border-r-4 border-tsm12-acc bg-tsm12-ink text-tsm12-paper">
    <div class="border-b-[3px] border-tsm12-acc px-4 py-[18px]">
      <p class="mb-1 font-tsm12-mono text-[10px] tracking-[0.2em] text-tsm12-navmut">EST. 2024</p>
      <p class="text-[28px] leading-none font-black tracking-[-0.02em] uppercase">Brutal</p>
      <p class="mt-1.5 inline-block bg-tsm12-acc px-1.5 py-px text-[11px] font-extrabold tracking-[0.1em] text-white uppercase">Studio</p>
    </div>
    <ul class="flex-1">
      <li><a href="#" class="group/l relative flex min-h-12 items-center border-b border-tsm12-line px-4 text-lg font-extrabold tracking-[0.04em] text-tsm12-navmut uppercase transition-colors duration-100 before:mr-2 before:font-tsm12-mono before:text-xs before:text-tsm12-navmut/60 before:content-['//'] hover:bg-tsm12-yel hover:text-black hover:before:text-black/60 focus-visible:bg-tsm12-yel focus-visible:text-black focus-visible:outline-none aria-[current=page]:border-tsm12-acc aria-[current=page]:bg-tsm12-acc aria-[current=page]:text-tsm12-paper aria-[current=page]:before:text-white/60 aria-[current=page]:after:ml-auto aria-[current=page]:after:font-tsm12-mono aria-[current=page]:after:text-base aria-[current=page]:after:content-['→'] motion-reduce:transition-none" aria-current="page">Home</a></li>
      <li><a href="#" class="group/l relative flex min-h-12 items-center border-b border-tsm12-line px-4 text-lg font-extrabold tracking-[0.04em] text-tsm12-navmut uppercase transition-colors duration-100 before:mr-2 before:font-tsm12-mono before:text-xs before:text-tsm12-navmut/60 before:content-['//'] hover:bg-tsm12-yel hover:text-black hover:before:text-black/60 focus-visible:bg-tsm12-yel focus-visible:text-black focus-visible:outline-none aria-[current=page]:border-tsm12-acc aria-[current=page]:bg-tsm12-acc aria-[current=page]:text-tsm12-paper aria-[current=page]:before:text-white/60 aria-[current=page]:after:ml-auto aria-[current=page]:after:font-tsm12-mono aria-[current=page]:after:text-base aria-[current=page]:after:content-['→'] motion-reduce:transition-none">Work<span class="ml-auto pl-2 font-tsm12-mono text-[11px] font-normal text-tsm12-yel group-hover/l:text-black">12</span></a></li>
      <li><a href="#" class="group/l relative flex min-h-12 items-center border-b border-tsm12-line px-4 text-lg font-extrabold tracking-[0.04em] text-tsm12-navmut uppercase transition-colors duration-100 before:mr-2 before:font-tsm12-mono before:text-xs before:text-tsm12-navmut/60 before:content-['//'] hover:bg-tsm12-yel hover:text-black hover:before:text-black/60 focus-visible:bg-tsm12-yel focus-visible:text-black focus-visible:outline-none aria-[current=page]:border-tsm12-acc aria-[current=page]:bg-tsm12-acc aria-[current=page]:text-tsm12-paper aria-[current=page]:before:text-white/60 aria-[current=page]:after:ml-auto aria-[current=page]:after:font-tsm12-mono aria-[current=page]:after:text-base aria-[current=page]:after:content-['→'] motion-reduce:transition-none">Studio</a></li>
      <li><a href="#" class="group/l relative flex min-h-12 items-center border-b border-tsm12-line px-4 text-lg font-extrabold tracking-[0.04em] text-tsm12-navmut uppercase transition-colors duration-100 before:mr-2 before:font-tsm12-mono before:text-xs before:text-tsm12-navmut/60 before:content-['//'] hover:bg-tsm12-yel hover:text-black hover:before:text-black/60 focus-visible:bg-tsm12-yel focus-visible:text-black focus-visible:outline-none aria-[current=page]:border-tsm12-acc aria-[current=page]:bg-tsm12-acc aria-[current=page]:text-tsm12-paper aria-[current=page]:before:text-white/60 aria-[current=page]:after:ml-auto aria-[current=page]:after:font-tsm12-mono aria-[current=page]:after:text-base aria-[current=page]:after:content-['→'] motion-reduce:transition-none">Journal<span class="ml-auto pl-2 font-tsm12-mono text-[11px] font-normal text-tsm12-yel group-hover/l:text-black">05</span></a></li>
      <li><a href="#" class="group/l relative flex min-h-12 items-center border-b border-tsm12-line px-4 text-lg font-extrabold tracking-[0.04em] text-tsm12-navmut uppercase transition-colors duration-100 before:mr-2 before:font-tsm12-mono before:text-xs before:text-tsm12-navmut/60 before:content-['//'] hover:bg-tsm12-yel hover:text-black hover:before:text-black/60 focus-visible:bg-tsm12-yel focus-visible:text-black focus-visible:outline-none aria-[current=page]:border-tsm12-acc aria-[current=page]:bg-tsm12-acc aria-[current=page]:text-tsm12-paper aria-[current=page]:before:text-white/60 aria-[current=page]:after:ml-auto aria-[current=page]:after:font-tsm12-mono aria-[current=page]:after:text-base aria-[current=page]:after:content-['→'] motion-reduce:transition-none">Contact</a></li>
    </ul>
    <div class="border-t-[3px] border-tsm12-acc px-4 py-3">
      <p class="mb-1 font-tsm12-mono text-[10px] tracking-[0.15em] text-tsm12-navmut">// USER</p>
      <p class="text-sm font-extrabold tracking-[0.05em] uppercase">J. Haas</p>
    </div>
  </nav>
  <div class="min-w-0 flex-1">
    <div class="flex items-baseline gap-3 border-b-[3px] border-tsm12-ink px-6 py-4">
      <span class="font-tsm12-mono text-xs text-tsm12-acc">[01]</span>
      <h1 class="text-[clamp(28px,4vw,40px)] leading-none font-black tracking-[-0.01em] uppercase">Homepage</h1>
    </div>
    <div class="p-6">
      <p class="mb-6 max-w-sm text-base leading-snug font-semibold text-tsm12-mut text-pretty">Raw borders, zero gradients, high-contrast type — and a thick red rule as the only decoration. Hover or Tab the menu.</p>
      <div class="grid max-w-md grid-cols-2 border-[3px] border-tsm12-ink">
        <div class="border-tsm12-ink p-4 odd:border-r-2 nth-[-n+2]:border-b-2"><p class="text-[clamp(26px,4vw,36px)] leading-none font-black tracking-[-0.03em]">24</p><p class="mt-1.5 font-tsm12-mono text-[11px] tracking-[0.1em] text-tsm12-mut uppercase">Projects</p></div>
        <div class="border-tsm12-ink p-4 odd:border-r-2 nth-[-n+2]:border-b-2"><p class="text-[clamp(26px,4vw,36px)] leading-none font-black tracking-[-0.03em]">08</p><p class="mt-1.5 font-tsm12-mono text-[11px] tracking-[0.1em] text-tsm12-mut uppercase">Clients</p></div>
        <div class="border-tsm12-ink p-4 odd:border-r-2 nth-[-n+2]:border-b-2"><p class="text-[clamp(26px,4vw,36px)] leading-none font-black tracking-[-0.03em]">6yr</p><p class="mt-1.5 font-tsm12-mono text-[11px] tracking-[0.1em] text-tsm12-mut uppercase">Experience</p></div>
        <div class="border-tsm12-ink p-4 odd:border-r-2 nth-[-n+2]:border-b-2"><p class="text-[clamp(26px,4vw,36px)] leading-none font-black tracking-[-0.03em]">100%</p><p class="mt-1.5 font-tsm12-mono text-[11px] tracking-[0.1em] text-tsm12-mut uppercase">Remote</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm12-paper: #f5f0e8;
  --color-tsm12-paper: oklch(0.957 0.012 79.8);
  --color-tsm12-ink: #0a0a0a;
  --color-tsm12-ink: oklch(0.145 0 0);
  --color-tsm12-acc: #e63329;
  --color-tsm12-acc: oklch(0.604 0.216 28.7);
  --color-tsm12-yel: #f7e733;
  --color-tsm12-yel: oklch(0.913 0.181 104);
  --color-tsm12-line: #262626;
  --color-tsm12-line: oklch(0.269 0 0);
  --color-tsm12-navmut: #a8a8a8;
  --color-tsm12-navmut: oklch(0.732 0 0);
  --color-tsm12-mut: #3d3d3d;
  --color-tsm12-mut: oklch(0.36 0 0);
  --font-tsm12-head: 'Barlow Condensed', 'Arial Narrow', system-ui, sans-serif;
  --font-tsm12-mono: 'Space Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-12 {
  width: 100%;
  min-height: 100svh;
}
```
