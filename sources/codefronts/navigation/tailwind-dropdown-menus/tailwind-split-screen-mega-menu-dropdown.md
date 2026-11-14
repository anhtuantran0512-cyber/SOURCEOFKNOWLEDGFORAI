---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-split-screen-mega-menu-dropdown/"
title: "Tailwind Split-Screen Mega Menu Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "The retail mega menu: a billboard column on the left, categorised links on the right, one grid-cols-[1.2fr_1fr] holding the split. It is the demo where…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split-Screen Mega Menu Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-split-screen-mega-menu-dropdown/

The retail mega menu: a billboard column on the left, categorised links on the right, one grid-cols-[1.2fr_1fr] holding the split. It is the demo where Tailwind's ratio tracks and per-instance overrides shine — the second panel restyles its whole billboard with a single gradient utility, no modifier class.
## HTML
```html
<section class="tdd-13 w-full min-h-svh bg-tdd13-bg font-tdd13-sans text-tdd13-ink px-5 py-8" aria-label="Split-screen mega menu dropdown demo">
  <nav class="relative z-10 mx-auto flex w-[min(720px,100%)] items-center gap-1 rounded-t-xl border-b border-tdd13-edge bg-white px-5 shadow-[0_2px_12px_oklch(0_0_0/0.05)]" aria-label="Primary">
    <a href="#home" class="mr-6 py-4 font-tdd13-serif text-xl font-bold tracking-[-0.3px] text-tdd13-ink no-underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd13-ink">Meridian</a>
    <div class="ml-auto flex items-center">
      <div class="group relative">
        <a href="#collections" class="block px-3.5 py-4.5 text-[13.5px] font-medium tracking-[0.03em] text-tdd13-mut no-underline transition-colors duration-150 group-hover:text-tdd13-ink focus-visible:text-tdd13-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd13-ink">Collections &#9662;</a>
        <div class="pointer-events-none absolute top-full left-1/2 grid w-[min(580px,90vw)] -translate-x-1/2 -translate-y-2.5 grid-cols-[1.2fr_1fr] overflow-hidden rounded-b-2xl border border-t-0 border-tdd13-edge bg-white opacity-0 shadow-[0_24px_60px_oklch(0_0_0/0.13)] transition-[opacity,translate] duration-320 ease-tdd13 group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 max-sm:grid-cols-1 motion-reduce:duration-150">
          <div class="flex min-h-55 flex-col gap-2 bg-linear-[145deg,var(--color-tdd13-slate1),var(--color-tdd13-slate2)_50%,var(--color-tdd13-slate3)] px-6 py-7">
            <p class="text-[10px] font-semibold uppercase tracking-[0.12em] text-white/50">Season Highlight</p>
            <p class="font-tdd13-serif text-xl font-bold leading-tight text-white">Summer Capsule 2025</p>
            <p class="mt-1 flex-1 text-[12.5px] leading-relaxed text-white/70 text-pretty">Refined essentials for the modern wardrobe.</p>
            <a href="#explore" class="mt-2 text-[12.5px] font-semibold tracking-[0.03em] text-white/85 no-underline transition-colors duration-150 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Explore Now &#8594;</a>
          </div>
          <div class="grid grid-cols-2 gap-6 px-5 py-6">
            <div class="flex flex-col gap-1">
              <p class="mb-1.5 border-b border-tdd13-edge pb-1.5 text-[10px] font-bold uppercase tracking-[0.1em] text-tdd13-mut">Women</p>
              <a href="#rtw" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Ready to Wear</a>
              <a href="#accessories" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Accessories</a>
              <a href="#footwear" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Footwear</a>
            </div>
            <div class="flex flex-col gap-1">
              <p class="mb-1.5 border-b border-tdd13-edge pb-1.5 text-[10px] font-bold uppercase tracking-[0.1em] text-tdd13-mut">Men</p>
              <a href="#tailoring" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Tailoring</a>
              <a href="#casual" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Casual</a>
              <a href="#sport" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Sport</a>
            </div>
          </div>
        </div>
      </div>
      <div class="group relative">
        <a href="#stories" class="block px-3.5 py-4.5 text-[13.5px] font-medium tracking-[0.03em] text-tdd13-mut no-underline transition-colors duration-150 group-hover:text-tdd13-ink focus-visible:text-tdd13-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd13-ink">Stories &#9662;</a>
        <div class="pointer-events-none absolute top-full left-1/2 grid w-[min(580px,90vw)] -translate-x-1/2 -translate-y-2.5 grid-cols-[1.2fr_1fr] overflow-hidden rounded-b-2xl border border-t-0 border-tdd13-edge bg-white opacity-0 shadow-[0_24px_60px_oklch(0_0_0/0.13)] transition-[opacity,translate] duration-320 ease-tdd13 group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 max-sm:grid-cols-1 motion-reduce:duration-150">
          <div class="flex min-h-55 flex-col gap-2 bg-linear-[145deg,var(--color-tdd13-green1),var(--color-tdd13-green2)_50%,var(--color-tdd13-green3)] px-6 py-7">
            <p class="text-[10px] font-semibold uppercase tracking-[0.12em] text-white/50">From the Journal</p>
            <p class="font-tdd13-serif text-xl font-bold leading-tight text-white">The Art of Slow Fashion</p>
            <p class="mt-1 flex-1 text-[12.5px] leading-relaxed text-white/70 text-pretty">Conscious design for the discerning eye.</p>
            <a href="#read" class="mt-2 text-[12.5px] font-semibold tracking-[0.03em] text-white/85 no-underline transition-colors duration-150 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Read Story &#8594;</a>
          </div>
          <div class="grid grid-cols-2 gap-6 px-5 py-6">
            <div class="flex flex-col gap-1">
              <p class="mb-1.5 border-b border-tdd13-edge pb-1.5 text-[10px] font-bold uppercase tracking-[0.1em] text-tdd13-mut">Editorials</p>
              <a href="#photography" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Photography</a>
              <a href="#film" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Film</a>
              <a href="#interviews" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Interviews</a>
            </div>
            <div class="flex flex-col gap-1">
              <p class="mb-1.5 border-b border-tdd13-edge pb-1.5 text-[10px] font-bold uppercase tracking-[0.1em] text-tdd13-mut">Craft</p>
              <a href="#materials" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Materials</a>
              <a href="#atelier" class="block py-1 text-[13px] font-medium text-tdd13-ink no-underline transition-colors duration-150 hover:text-tdd13-acc focus-visible:text-tdd13-acc focus-visible:outline-none">Atelier</a>
            </div>
          </div>
        </div>
      </div>
      <a href="#world" class="block px-3.5 py-4.5 text-[13.5px] font-medium tracking-[0.03em] text-tdd13-mut no-underline transition-colors duration-150 hover:text-tdd13-ink focus-visible:text-tdd13-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd13-ink">World</a>
      <a href="#services" class="block px-3.5 py-4.5 text-[13.5px] font-medium tracking-[0.03em] text-tdd13-mut no-underline transition-colors duration-150 hover:text-tdd13-ink focus-visible:text-tdd13-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd13-ink">Services</a>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd13-bg: #f8f7f4;
  --color-tdd13-bg: oklch(0.97 0.005 95);
  --color-tdd13-ink: #1e293b;
  --color-tdd13-ink: oklch(0.28 0.03 260);
  --color-tdd13-mut: #64748b;
  --color-tdd13-mut: oklch(0.55 0.03 255);
  --color-tdd13-edge: #e2e8f0;
  --color-tdd13-edge: oklch(0.92 0.01 255);
  --color-tdd13-acc: #0ea5e9;
  --color-tdd13-acc: oklch(0.68 0.15 233);
  --color-tdd13-slate1: #1e293b;
  --color-tdd13-slate1: oklch(0.28 0.03 260);
  --color-tdd13-slate2: #334155;
  --color-tdd13-slate2: oklch(0.37 0.03 258);
  --color-tdd13-slate3: #475569;
  --color-tdd13-slate3: oklch(0.45 0.03 257);
  --color-tdd13-green1: #065f46;
  --color-tdd13-green1: oklch(0.42 0.1 165);
  --color-tdd13-green2: #047857;
  --color-tdd13-green2: oklch(0.49 0.12 165);
  --color-tdd13-green3: #10b981;
  --color-tdd13-green3: oklch(0.7 0.16 163);
  --font-tdd13-sans: 'Inter', system-ui, sans-serif;
  --font-tdd13-serif: 'Playfair Display', Georgia, serif;
  --ease-tdd13: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-13 {
  width: 100%;
  min-height: 100svh;
}

.tdd-13 ::selection {
  background: var(--color-tdd13-ink);
  color: #f8fafc;
}
```
