---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-nested-multi-level-dropdown/"
title: "Tailwind Nested Multi-Level Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "Three levels deep, each submenu flying out to the right of its parent — and the demo that makes named groups indispensable."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Nested Multi-Level Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-nested-multi-level-dropdown/

Three levels deep, each submenu flying out to the right of its parent — and the demo that makes named groups indispensable. group/l1, group/l2, group/l3 keep each level's hover from leaking into its children, which is exactly the bug the CSS version fights with > combinators.
## HTML
```html
<section class="tdd-11 w-full min-h-svh grid justify-center content-start bg-linear-[135deg,var(--color-tdd11-bg1),var(--color-tdd11-bg2)] font-tdd11-sans text-tdd11-ink px-5 py-8" aria-label="Nested multi-level dropdown demo">
  <nav class="relative z-10" aria-label="Primary">
    <ul class="flex list-none gap-0.5 rounded-xl border border-tdd11-edge bg-white p-1.5 shadow-[0_4px_20px_oklch(0_0_0/0.07)]">
      <li class="relative">
        <a href="#home" class="flex items-center justify-between gap-2 whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-semibold text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Home</a>
      </li>
      <li class="group/l1 relative after:absolute after:inset-x-0 after:top-full after:h-2 after:content-['']">
        <a href="#products" class="flex items-center justify-between gap-2 whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-semibold text-tdd11-ink no-underline transition-colors duration-150 after:text-[11px] after:text-tdd11-mut after:content-['\2304'] hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Products</a>
        <ul class="pointer-events-none absolute top-[calc(100%+8px)] left-0 z-10 flex min-w-42 -translate-y-1 list-none flex-col gap-px rounded-[10px] border border-tdd11-edge bg-white p-1.5 opacity-0 shadow-[0_8px_32px_oklch(0_0_0/0.12)] transition-[opacity,translate] duration-200 group-hover/l1:pointer-events-auto group-hover/l1:translate-y-0 group-hover/l1:opacity-100 group-focus-within/l1:pointer-events-auto group-focus-within/l1:translate-y-0 group-focus-within/l1:opacity-100">
          <li class="group/l2 relative after:absolute after:inset-y-0 after:left-full after:w-2.5 after:content-['']">
            <a href="#software" class="flex items-center justify-between gap-2 whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 after:ml-auto after:text-sm after:text-tdd11-mut after:content-['\203A'] hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Software</a>
            <ul class="pointer-events-none absolute -top-1.5 left-[calc(100%+10px)] z-20 flex min-w-42 translate-x-1 list-none flex-col gap-px rounded-[10px] border border-tdd11-edge bg-white p-1.5 opacity-0 shadow-[0_8px_32px_oklch(0_0_0/0.14)] transition-[opacity,translate] duration-200 group-hover/l2:pointer-events-auto group-hover/l2:translate-x-0 group-hover/l2:opacity-100 group-focus-within/l2:pointer-events-auto group-focus-within/l2:translate-x-0 group-focus-within/l2:opacity-100">
              <li><a href="#web-app" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Web App</a></li>
              <li><a href="#desktop" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Desktop</a></li>
              <li><a href="#mobile" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Mobile</a></li>
            </ul>
          </li>
          <li class="group/l2 relative after:absolute after:inset-y-0 after:left-full after:w-2.5 after:content-['']">
            <a href="#hardware" class="flex items-center justify-between gap-2 whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 after:ml-auto after:text-sm after:text-tdd11-mut after:content-['\203A'] hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Hardware</a>
            <ul class="pointer-events-none absolute -top-1.5 left-[calc(100%+10px)] z-20 flex min-w-42 translate-x-1 list-none flex-col gap-px rounded-[10px] border border-tdd11-edge bg-white p-1.5 opacity-0 shadow-[0_8px_32px_oklch(0_0_0/0.14)] transition-[opacity,translate] duration-200 group-hover/l2:pointer-events-auto group-hover/l2:translate-x-0 group-hover/l2:opacity-100 group-focus-within/l2:pointer-events-auto group-focus-within/l2:translate-x-0 group-focus-within/l2:opacity-100">
              <li><a href="#devices" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Devices</a></li>
              <li><a href="#accessories" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Accessories</a></li>
            </ul>
          </li>
          <li><a href="#services" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Services</a></li>
        </ul>
      </li>
      <li class="group/l1 relative after:absolute after:inset-x-0 after:top-full after:h-2 after:content-['']">
        <a href="#company" class="flex items-center justify-between gap-2 whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-semibold text-tdd11-ink no-underline transition-colors duration-150 after:text-[11px] after:text-tdd11-mut after:content-['\2304'] hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Company</a>
        <ul class="pointer-events-none absolute top-[calc(100%+8px)] left-0 z-10 flex min-w-42 -translate-y-1 list-none flex-col gap-px rounded-[10px] border border-tdd11-edge bg-white p-1.5 opacity-0 shadow-[0_8px_32px_oklch(0_0_0/0.12)] transition-[opacity,translate] duration-200 group-hover/l1:pointer-events-auto group-hover/l1:translate-y-0 group-hover/l1:opacity-100 group-focus-within/l1:pointer-events-auto group-focus-within/l1:translate-y-0 group-focus-within/l1:opacity-100">
          <li><a href="#about" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">About</a></li>
          <li><a href="#careers" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Careers</a></li>
          <li class="group/l2 relative after:absolute after:inset-y-0 after:left-full after:w-2.5 after:content-['']">
            <a href="#press" class="flex items-center justify-between gap-2 whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 after:ml-auto after:text-sm after:text-tdd11-mut after:content-['\203A'] hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Press</a>
            <ul class="pointer-events-none absolute -top-1.5 left-[calc(100%+10px)] z-20 flex min-w-42 translate-x-1 list-none flex-col gap-px rounded-[10px] border border-tdd11-edge bg-white p-1.5 opacity-0 shadow-[0_8px_32px_oklch(0_0_0/0.14)] transition-[opacity,translate] duration-200 group-hover/l2:pointer-events-auto group-hover/l2:translate-x-0 group-hover/l2:opacity-100 group-focus-within/l2:pointer-events-auto group-focus-within/l2:translate-x-0 group-focus-within/l2:opacity-100">
              <li><a href="#news" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">News</a></li>
              <li><a href="#media-kit" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Media Kit</a></li>
            </ul>
          </li>
        </ul>
      </li>
      <li class="relative"><a href="#contact" class="block whitespace-nowrap rounded-lg px-3.5 py-2.5 text-[13.5px] font-semibold text-tdd11-ink no-underline transition-colors duration-150 hover:bg-tdd11-tint hover:text-tdd11-acc focus-visible:bg-tdd11-tint focus-visible:outline-none">Contact</a></li>
    </ul>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd11-bg1: #eff6ff;
  --color-tdd11-bg1: oklch(0.97 0.02 250);
  --color-tdd11-bg2: #e0e7ff;
  --color-tdd11-bg2: oklch(0.92 0.04 275);
  --color-tdd11-ink: #1e293b;
  --color-tdd11-ink: oklch(0.28 0.03 260);
  --color-tdd11-mut: #64748b;
  --color-tdd11-mut: oklch(0.55 0.03 255);
  --color-tdd11-edge: #e2e8f0;
  --color-tdd11-edge: oklch(0.92 0.01 255);
  --color-tdd11-tint: #eff6ff;
  --color-tdd11-tint: oklch(0.97 0.02 250);
  --color-tdd11-acc: #1d4ed8;
  --color-tdd11-acc: oklch(0.48 0.2 264);
  --font-tdd11-sans: 'Manrope', system-ui, sans-serif;
}

.tdd-11 {
  width: 100%;
  min-height: 100svh;
}

.tdd-11 ::selection {
  background: var(--color-tdd11-acc);
  color: #eff6ff;
}
```
