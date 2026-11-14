---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-3d-perspective-flip-dropdown/"
title: "Tailwind 3D Perspective Flip Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "A panel that folds open from its top edge like a hinged lid."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Perspective Flip Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-3d-perspective-flip-dropdown/

A panel that folds open from its top edge like a hinged lid. v4 finally ships the 3D primitives as first-class utilities — perspective-[800px], transform-3d, rotate-x-90, origin-top — so the entire effect is markup, and the stylesheet holds nothing but tokens.
## HTML
```html
<section class="tdd-03 w-full min-h-svh grid justify-center content-start bg-linear-[135deg,var(--color-tdd03-bg1),var(--color-tdd03-bg2)] font-tdd03-sans px-5 py-8" aria-label="3D perspective flip dropdown demo">
  <nav class="relative z-10 flex items-center gap-10 rounded-2xl bg-tdd03-ink px-8 py-4 shadow-[0_8px_32px_oklch(0.22_0.04_265/0.25)]" aria-label="Primary">
    <span class="mr-auto text-lg font-bold tracking-[3px] text-white">NOVA</span>
    <div class="flex gap-1">
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <a href="#work" class="block rounded-lg px-4 py-2 text-sm font-semibold tracking-[0.5px] text-white/75 no-underline transition-colors duration-150 group-hover:bg-white/10 group-hover:text-white focus-visible:bg-white/10 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd03-acc">Work</a>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 -translate-x-1/2 perspective-[800px] transform-3d group-hover:pointer-events-auto group-focus-within:pointer-events-auto">
          <div class="flex min-w-45 -rotate-x-90 origin-top flex-col gap-0.5 rounded-xl border border-tdd03-edge bg-white p-1.5 opacity-0 shadow-[0_20px_60px_oklch(0.22_0.04_265/0.2)] transition-[transform,opacity] duration-400 ease-tdd03 group-hover:rotate-x-0 group-hover:opacity-100 group-focus-within:rotate-x-0 group-focus-within:opacity-100 motion-reduce:rotate-x-0 motion-reduce:duration-150">
            <a href="#case-studies" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">Case Studies</a>
            <a href="#branding" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">Branding</a>
            <a href="#motion" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">Motion</a>
            <a href="#web-design" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">Web Design</a>
          </div>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <a href="#services" class="block rounded-lg px-4 py-2 text-sm font-semibold tracking-[0.5px] text-white/75 no-underline transition-colors duration-150 group-hover:bg-white/10 group-hover:text-white focus-visible:bg-white/10 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd03-acc">Services</a>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 -translate-x-1/2 perspective-[800px] transform-3d group-hover:pointer-events-auto group-focus-within:pointer-events-auto">
          <div class="flex min-w-45 -rotate-x-90 origin-top flex-col gap-0.5 rounded-xl border border-tdd03-edge bg-white p-1.5 opacity-0 shadow-[0_20px_60px_oklch(0.22_0.04_265/0.2)] transition-[transform,opacity] duration-400 ease-tdd03 group-hover:rotate-x-0 group-hover:opacity-100 group-focus-within:rotate-x-0 group-focus-within:opacity-100 motion-reduce:rotate-x-0 motion-reduce:duration-150">
            <a href="#strategy" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">Strategy</a>
            <a href="#design" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">Design</a>
            <a href="#development" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">Development</a>
          </div>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <a href="#studio" class="block rounded-lg px-4 py-2 text-sm font-semibold tracking-[0.5px] text-white/75 no-underline transition-colors duration-150 group-hover:bg-white/10 group-hover:text-white focus-visible:bg-white/10 focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd03-acc">Studio</a>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 -translate-x-1/2 perspective-[800px] transform-3d group-hover:pointer-events-auto group-focus-within:pointer-events-auto">
          <div class="flex min-w-45 -rotate-x-90 origin-top flex-col gap-0.5 rounded-xl border border-tdd03-edge bg-white p-1.5 opacity-0 shadow-[0_20px_60px_oklch(0.22_0.04_265/0.2)] transition-[transform,opacity] duration-400 ease-tdd03 group-hover:rotate-x-0 group-hover:opacity-100 group-focus-within:rotate-x-0 group-focus-within:opacity-100 motion-reduce:rotate-x-0 motion-reduce:duration-150">
            <a href="#about" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">About</a>
            <a href="#team" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">Team</a>
            <a href="#culture" class="block rounded-lg px-3.5 py-2.5 text-sm font-medium text-tdd03-ink no-underline transition-colors duration-150 hover:bg-tdd03-tint hover:text-tdd03-acc focus-visible:bg-tdd03-tint focus-visible:outline-none">Culture</a>
          </div>
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
  --color-tdd03-bg1: #f1f5f9;
  --color-tdd03-bg1: oklch(0.97 0.005 250);
  --color-tdd03-bg2: #e0e7ff;
  --color-tdd03-bg2: oklch(0.92 0.04 275);
  --color-tdd03-ink: #0f172a;
  --color-tdd03-ink: oklch(0.21 0.04 265);
  --color-tdd03-edge: #e2e8f0;
  --color-tdd03-edge: oklch(0.92 0.01 255);
  --color-tdd03-tint: #eef2ff;
  --color-tdd03-tint: oklch(0.96 0.02 275);
  --color-tdd03-acc: #6366f1;
  --color-tdd03-acc: oklch(0.59 0.2 278);
  --font-tdd03-sans: 'Syne', system-ui, sans-serif;
  --ease-tdd03: cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tdd-03 {
  width: 100%;
  min-height: 100svh;
}

.tdd-03 ::selection {
  background: var(--color-tdd03-ink);
  color: #e2e8f0;
}
```
