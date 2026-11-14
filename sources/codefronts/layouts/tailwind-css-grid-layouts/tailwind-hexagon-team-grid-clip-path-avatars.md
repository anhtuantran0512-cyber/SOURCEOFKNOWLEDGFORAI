---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-hexagon-team-grid-clip-path-avatars/"
title: "Tailwind Hexagon Team Grid with clip-path Avatars"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A team page as an interlocking honeycomb: ten hexagonal portraits that nest peak-into-notch, each revealing a name and role on hover or keyboard focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hexagon Team Grid with clip-path Avatars
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-hexagon-team-grid-clip-path-avatars/

A team page as an interlocking honeycomb: ten hexagonal portraits that nest peak-into-notch, each revealing a name and role on hover or keyboard focus. The photo is clipped by the same polygon as the cell, so the comb stays a comb.
## HTML
```html
<section class="tgx-14 w-full min-h-svh bg-tgx14-bg font-tgx14-sans px-6 py-10 grid place-items-center gap-6">
  <header class="flex flex-col gap-1.5 text-center">
    <p class="text-[0.66rem] tracking-[0.2em] uppercase text-tgx14-honey">Hexlab · Studio</p>
    <h2 class="text-[1.5rem] font-semibold text-white tracking-[-0.015em]">Ten people, one comb</h2>
    <p class="text-[0.8rem] text-tgx14-dim max-w-[44ch]">Hover or tab through the team — each cell reveals a name and a role without moving its neighbours.</p>
  </header>
  <ul class="list-none flex flex-col items-start">
    <li class="flex gap-0">
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Ada N.</strong><span class="text-[0.62rem] text-tgx14-honey">Design lead</span></span>
      </a>
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Tomás R.</strong><span class="text-[0.62rem] text-tgx14-honey">Engineering</span></span>
      </a>
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Ines K.</strong><span class="text-[0.62rem] text-tgx14-honey">Research</span></span>
      </a>
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Sam B.</strong><span class="text-[0.62rem] text-tgx14-honey">Platform</span></span>
      </a>
    </li>
    <li class="flex gap-0 mt-[calc(var(--hex)*-0.3)] ml-[calc(var(--hex)/2)]">
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Noor A.</strong><span class="text-[0.62rem] text-tgx14-honey">Accessibility</span></span>
      </a>
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Jonas P.</strong><span class="text-[0.62rem] text-tgx14-honey">Performance</span></span>
      </a>
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Mei L.</strong><span class="text-[0.62rem] text-tgx14-honey">Brand</span></span>
      </a>
    </li>
    <li class="flex gap-0 mt-[calc(var(--hex)*-0.3)]">
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Ruth O.</strong><span class="text-[0.62rem] text-tgx14-honey">Content</span></span>
      </a>
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Dev S.</strong><span class="text-[0.62rem] text-tgx14-honey">Data</span></span>
      </a>
      <a href="#0" class="group relative block w-[var(--hex)] aspect-[1/1.1547] no-underline [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)] bg-tgx14-cell transition duration-200 hover:scale-105 focus-visible:scale-105 focus-visible:outline-none motion-reduce:transition-none motion-reduce:hover:scale-100">
        <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=260&h=300&q=80&auto=format&fit=crop" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover [clip-path:polygon(50%_0,100%_25%,100%_75%,50%_100%,0_75%,0_25%)]">
        <span class="absolute inset-0 grid content-end gap-0.5 px-3 pb-4 bg-[linear-gradient(180deg,transparent_45%,oklch(0.18_0.03_65/0.9))] opacity-0 transition-opacity duration-200 group-hover:opacity-100 group-focus-visible:opacity-100 motion-reduce:transition-none"><strong class="text-[0.76rem] font-semibold text-white leading-tight">Clara V.</strong><span class="text-[0.62rem] text-tgx14-honey">Ops</span></span>
      </a>
    </li>
  </ul>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx14-bg: #241a0f;
  --color-tgx14-bg: oklch(0.21 0.03 65);
  --color-tgx14-cell: #4a3a1c;
  --color-tgx14-cell: oklch(0.34 0.06 75);
  --color-tgx14-honey: #f0bd52;
  --color-tgx14-honey: oklch(0.82 0.15 80);
  --color-tgx14-dim: #cbbda6;
  --color-tgx14-dim: oklch(0.81 0.03 80);
  --font-tgx14-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-14 {
  width: 100%;
  min-height: 100svh;
  --hex: 104px;
  background-image: radial-gradient(100% 120% at 50% 0%, oklch(0.28 0.05 70 / 0.9), transparent 60%);
}
```
