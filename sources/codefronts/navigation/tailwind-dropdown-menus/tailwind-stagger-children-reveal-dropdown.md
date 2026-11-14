---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-stagger-children-reveal-dropdown/"
title: "Tailwind Stagger Children Reveal Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "Links that cascade in one by one."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stagger Children Reveal Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-stagger-children-reveal-dropdown/

Links that cascade in one by one. The CSS version writes an nth-child rule per item; Tailwind cannot, because variant values must be static classes. The idiomatic answer is the per-item index pattern — each link carries style="--i:2" and one shared utility reads it, so adding a sixth link means copying a line and incrementing a number.
## HTML
```html
<section class="tdd-06 w-full min-h-svh grid justify-center content-start bg-linear-[135deg,var(--color-tdd06-bg1),var(--color-tdd06-bg2)_50%,var(--color-tdd06-bg3)] font-tdd06-sans text-tdd06-ink px-5 py-8" aria-label="Staggered children reveal dropdown demo">
  <nav class="relative z-10 flex items-center gap-1 rounded-2xl border border-tdd06-edge bg-white py-2.5 pr-2.5 pl-5 shadow-[0_4px_20px_oklch(0_0_0/0.06)]" aria-label="Primary">
    <span class="mr-3 text-[17px] font-extrabold tracking-[-0.3px] text-tdd06-acc">&#9670; Flow</span>
    <div class="flex gap-0.5">
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <a href="#products" class="flex items-center gap-1.5 rounded-[10px] px-3.5 py-2 text-sm font-semibold text-tdd06-ink no-underline transition-colors duration-150 group-hover:bg-tdd06-tint group-hover:text-tdd06-acc focus-visible:bg-tdd06-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd06-acc"><span>Products</span><span class="text-xs text-tdd06-mut transition-transform duration-200 group-hover:rotate-180 group-hover:text-tdd06-acc group-focus-within:rotate-180" aria-hidden="true">&#9662;</span></a>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-50 -translate-x-1/2 flex-col gap-0.5 rounded-2xl border border-tdd06-edge bg-white p-2 opacity-0 shadow-[0_12px_40px_oklch(0_0_0/0.1)] transition-opacity duration-200 group-hover:pointer-events-auto group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:opacity-100">
          <a href="#tokens" style="--i:0;--c:#6366f1" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Design Tokens</a>
          <a href="#kit" style="--i:1;--c:#ec4899" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Component Kit</a>
          <a href="#icons" style="--i:2;--c:#f59e0b" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Icon Library</a>
          <a href="#figma" style="--i:3;--c:#10b981" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Figma Plugin</a>
          <a href="#cli" style="--i:4;--c:#3b82f6" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>CLI Tools</a>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <a href="#use-cases" class="flex items-center gap-1.5 rounded-[10px] px-3.5 py-2 text-sm font-semibold text-tdd06-ink no-underline transition-colors duration-150 group-hover:bg-tdd06-tint group-hover:text-tdd06-acc focus-visible:bg-tdd06-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd06-acc"><span>Use Cases</span><span class="text-xs text-tdd06-mut transition-transform duration-200 group-hover:rotate-180 group-hover:text-tdd06-acc group-focus-within:rotate-180" aria-hidden="true">&#9662;</span></a>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-50 -translate-x-1/2 flex-col gap-0.5 rounded-2xl border border-tdd06-edge bg-white p-2 opacity-0 shadow-[0_12px_40px_oklch(0_0_0/0.1)] transition-opacity duration-200 group-hover:pointer-events-auto group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:opacity-100">
          <a href="#startups" style="--i:0;--c:#8b5cf6" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Startups</a>
          <a href="#agencies" style="--i:1;--c:#06b6d4" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Agencies</a>
          <a href="#freelancers" style="--i:2;--c:#f97316" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Freelancers</a>
          <a href="#enterprise" style="--i:3;--c:#14b8a6" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Enterprise</a>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <a href="#company" class="flex items-center gap-1.5 rounded-[10px] px-3.5 py-2 text-sm font-semibold text-tdd06-ink no-underline transition-colors duration-150 group-hover:bg-tdd06-tint group-hover:text-tdd06-acc focus-visible:bg-tdd06-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd06-acc"><span>Company</span><span class="text-xs text-tdd06-mut transition-transform duration-200 group-hover:rotate-180 group-hover:text-tdd06-acc group-focus-within:rotate-180" aria-hidden="true">&#9662;</span></a>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-50 -translate-x-1/2 flex-col gap-0.5 rounded-2xl border border-tdd06-edge bg-white p-2 opacity-0 shadow-[0_12px_40px_oklch(0_0_0/0.1)] transition-opacity duration-200 group-hover:pointer-events-auto group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:opacity-100">
          <a href="#about" style="--i:0;--c:#ef4444" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>About</a>
          <a href="#blog" style="--i:1;--c:#a855f7" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Blog</a>
          <a href="#careers" style="--i:2;--c:#0ea5e9" class="flex items-center gap-2.5 rounded-[10px] px-3 py-2.5 text-[13.5px] font-semibold text-tdd06-ink no-underline opacity-0 -translate-x-2.5 transition-[opacity,translate,background] duration-300 ease-tdd06 hover:bg-tdd06-hover focus-visible:bg-tdd06-hover focus-visible:outline-none group-hover:opacity-100 group-hover:translate-x-0 group-hover:[transition-delay:calc(var(--i)*60ms)] group-focus-within:opacity-100 group-focus-within:translate-x-0 motion-reduce:[transition-delay:0ms]"><i class="size-2 shrink-0 rounded-full bg-[var(--c)]" aria-hidden="true"></i>Careers</a>
        </div>
      </div>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd06-bg1: #f0fdf4;
  --color-tdd06-bg1: oklch(0.98 0.02 150);
  --color-tdd06-bg2: #ecfdf5;
  --color-tdd06-bg2: oklch(0.98 0.02 165);
  --color-tdd06-bg3: #f0f9ff;
  --color-tdd06-bg3: oklch(0.98 0.02 230);
  --color-tdd06-ink: #1e293b;
  --color-tdd06-ink: oklch(0.28 0.03 260);
  --color-tdd06-mut: #94a3b8;
  --color-tdd06-mut: oklch(0.7 0.03 255);
  --color-tdd06-edge: #e2e8f0;
  --color-tdd06-edge: oklch(0.92 0.01 255);
  --color-tdd06-tint: #eef2ff;
  --color-tdd06-tint: oklch(0.96 0.02 275);
  --color-tdd06-hover: #f8fafc;
  --color-tdd06-hover: oklch(0.98 0.005 255);
  --color-tdd06-acc: #6366f1;
  --color-tdd06-acc: oklch(0.59 0.2 278);
  --font-tdd06-sans: 'Nunito', system-ui, sans-serif;
  --ease-tdd06: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-06 {
  width: 100%;
  min-height: 100svh;
}

.tdd-06 ::selection {
  background: var(--color-tdd06-acc);
  color: #fff;
}
```
