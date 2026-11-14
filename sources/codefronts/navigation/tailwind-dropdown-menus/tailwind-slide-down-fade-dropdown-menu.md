---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-slide-down-fade-dropdown-menu/"
title: "Tailwind Slide-Down Fade Dropdown Menu"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "The default dropdown, and the one worth porting first: hover a nav item and its panel grows down while the content fades in a beat later."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide-Down Fade Dropdown Menu
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-slide-down-fade-dropdown-menu/

The default dropdown, and the one worth porting first: hover a nav item and its panel grows down while the content fades in a beat later. In utilities the two-speed reveal is a single transition-[max-height,opacity,translate] plus one arbitrary transition-delay, and the hover bridge that keeps the menu alive across the gap is an after: strip on the group itself.
## HTML
```html
<section class="tdd-01 w-full min-h-svh grid place-items-center bg-linear-[135deg,var(--color-tdd01-bg1),var(--color-tdd01-bg2)] font-tdd01-sans text-tdd01-ink px-5 py-10" aria-label="Slide-down fade dropdown demo">
  <nav class="relative z-10 flex items-center gap-1 rounded-2xl border border-tdd01-edge bg-white px-3 py-2 shadow-[0_2px_12px_oklch(0_0_0/0.06)]" aria-label="Primary">
    <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2 after:content-['']">
      <a href="#products" class="flex items-center gap-1.5 whitespace-nowrap rounded-lg px-3.5 py-2 text-sm font-medium text-tdd01-ink no-underline transition-colors duration-200 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd01-acc">Products <span class="mt-px inline-block text-xs leading-none text-tdd01-mut transition-transform duration-250 group-hover:rotate-180 group-hover:text-tdd01-acc group-focus-within:rotate-180 motion-reduce:transition-none">&#9662;</span></a>
      <ul class="pointer-events-none absolute top-[calc(100%+8px)] left-1/2 min-w-50 max-h-0 -translate-x-1/2 -translate-y-1.5 list-none overflow-hidden rounded-xl border border-tdd01-edge bg-white p-1.5 opacity-0 shadow-[0_10px_40px_oklch(0.55_0.2_280/0.15)] transition-[max-height,opacity,translate] duration-350 ease-out group-hover:pointer-events-auto group-hover:max-h-80 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-75 group-focus-within:pointer-events-auto group-focus-within:max-h-80 group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:transition-none">
        <li><a href="#design-system" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>Design System</a></li>
        <li><a href="#components" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>Component Library</a></li>
        <li><a href="#icons" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>Icon Pack</a></li>
        <li><a href="#templates" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>Templates</a></li>
      </ul>
    </div>
    <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2 after:content-['']">
      <a href="#solutions" class="flex items-center gap-1.5 whitespace-nowrap rounded-lg px-3.5 py-2 text-sm font-medium text-tdd01-ink no-underline transition-colors duration-200 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd01-acc">Solutions <span class="mt-px inline-block text-xs leading-none text-tdd01-mut transition-transform duration-250 group-hover:rotate-180 group-hover:text-tdd01-acc group-focus-within:rotate-180 motion-reduce:transition-none">&#9662;</span></a>
      <ul class="pointer-events-none absolute top-[calc(100%+8px)] left-1/2 min-w-50 max-h-0 -translate-x-1/2 -translate-y-1.5 list-none overflow-hidden rounded-xl border border-tdd01-edge bg-white p-1.5 opacity-0 shadow-[0_10px_40px_oklch(0.55_0.2_280/0.15)] transition-[max-height,opacity,translate] duration-350 ease-out group-hover:pointer-events-auto group-hover:max-h-80 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-75 group-focus-within:pointer-events-auto group-focus-within:max-h-80 group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:transition-none">
        <li><a href="#startups" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>For Startups</a></li>
        <li><a href="#enterprise" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>For Enterprise</a></li>
        <li><a href="#agencies" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>For Agencies</a></li>
      </ul>
    </div>
    <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2 after:content-['']">
      <a href="#resources" class="flex items-center gap-1.5 whitespace-nowrap rounded-lg px-3.5 py-2 text-sm font-medium text-tdd01-ink no-underline transition-colors duration-200 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd01-acc">Resources <span class="mt-px inline-block text-xs leading-none text-tdd01-mut transition-transform duration-250 group-hover:rotate-180 group-hover:text-tdd01-acc group-focus-within:rotate-180 motion-reduce:transition-none">&#9662;</span></a>
      <ul class="pointer-events-none absolute top-[calc(100%+8px)] left-1/2 min-w-50 max-h-0 -translate-x-1/2 -translate-y-1.5 list-none overflow-hidden rounded-xl border border-tdd01-edge bg-white p-1.5 opacity-0 shadow-[0_10px_40px_oklch(0.55_0.2_280/0.15)] transition-[max-height,opacity,translate] duration-350 ease-out group-hover:pointer-events-auto group-hover:max-h-80 group-hover:translate-y-0 group-hover:opacity-100 group-hover:delay-75 group-focus-within:pointer-events-auto group-focus-within:max-h-80 group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:transition-none">
        <li><a href="#docs" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>Documentation</a></li>
        <li><a href="#blog" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>Blog</a></li>
        <li><a href="#community" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>Community</a></li>
        <li><a href="#changelog" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd01-ink no-underline transition-colors duration-150 hover:bg-tdd01-tint hover:text-tdd01-acc focus-visible:bg-tdd01-tint focus-visible:outline-none"><i class="size-1.5 rounded-[1px] rotate-45 bg-tdd01-acc/60" aria-hidden="true"></i>Changelog</a></li>
      </ul>
    </div>
    <a href="#start" class="ml-2 rounded-lg bg-tdd01-acc px-4.5 py-2 text-sm font-semibold text-white no-underline transition-[background,translate] duration-200 hover:bg-tdd01-accdark hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd01-accdark motion-reduce:transition-none">Get Started</a>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd01-bg1: #f0f4ff;
  --color-tdd01-bg1: oklch(0.96 0.02 265);
  --color-tdd01-bg2: #faf5ff;
  --color-tdd01-bg2: oklch(0.97 0.02 305);
  --color-tdd01-ink: #111827;
  --color-tdd01-ink: oklch(0.21 0.02 265);
  --color-tdd01-mut: #6b7280;
  --color-tdd01-mut: oklch(0.55 0.02 265);
  --color-tdd01-edge: #e5e7eb;
  --color-tdd01-edge: oklch(0.91 0.005 265);
  --color-tdd01-tint: #f5f3ff;
  --color-tdd01-tint: oklch(0.97 0.02 295);
  --color-tdd01-acc: #6366f1;
  --color-tdd01-acc: oklch(0.59 0.2 278);
  --color-tdd01-accdark: #4f46e5;
  --color-tdd01-accdark: oklch(0.53 0.22 278);
  --font-tdd01-sans: 'Inter', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build compiles. */

.tdd-01 {
  width: 100%;
  min-height: 100svh;
}

.tdd-01 ::selection {
  background: var(--color-tdd01-acc);
  color: #fff;
}
```
