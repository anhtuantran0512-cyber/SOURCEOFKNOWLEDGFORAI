---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-clip-path-curtain-reveal-dropdown/"
title: "Tailwind Clip-Path Curtain Reveal Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "A curtain that falls open: the panel is always full height, and a clip-path polygon animates from a zero-height strip at its top edge to the full rectangle."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Clip-Path Curtain Reveal Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-clip-path-curtain-reveal-dropdown/

A curtain that falls open: the panel is always full height, and a clip-path polygon animates from a zero-height strip at its top edge to the full rectangle. Both polygons live on the panel as arbitrary utilities, which is the whole argument for the port — a mismatched pair of point counts is the classic bug in this pattern, and here the pair is one line apart.
## HTML
```html
<section class="tdd-02 w-full min-h-svh grid justify-center content-start bg-linear-[160deg,var(--color-tdd02-bg1),var(--color-tdd02-bg2)] font-tdd02-sans text-tdd02-ink px-5 py-8" aria-label="Clip-path curtain reveal dropdown demo">
  <nav class="relative z-10 flex w-[min(720px,92vw)] items-center gap-8 rounded-xl border-b-2 border-tdd02-edge bg-white px-7 py-3.5 shadow-[0_2px_16px_oklch(0_0_0/0.06)]" aria-label="Primary">
    <a href="#home" class="mr-auto text-lg font-bold tracking-[-0.5px] text-tdd02-acc no-underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd02-acc">Vertex</a>
    <div class="flex gap-1">
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <button type="button" class="cursor-pointer rounded-lg border-0 bg-transparent px-3.5 py-2 font-tdd02-sans text-sm font-medium text-tdd02-ink transition-colors duration-150 group-hover:bg-tdd02-tint group-hover:text-tdd02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd02-acc">Company &#9662;</button>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 min-w-55 -translate-x-1/2 overflow-hidden rounded-xl border border-tdd02-edge bg-white opacity-0 shadow-[0_16px_48px_oklch(0_0_0/0.12)] [clip-path:polygon(0_0,100%_0,100%_0,0_0)] transition-[clip-path,opacity] duration-400 ease-tdd02 group-hover:pointer-events-auto group-hover:opacity-100 group-hover:[clip-path:polygon(0_0,100%_0,100%_100%,0_100%)] group-focus-within:pointer-events-auto group-focus-within:opacity-100 group-focus-within:[clip-path:polygon(0_0,100%_0,100%_100%,0_100%)] motion-reduce:[clip-path:none] motion-reduce:duration-150">
          <div class="grid grid-cols-2 gap-1 p-2">
            <a href="#about" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#127959;</span>About Us</a>
            <a href="#careers" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#128101;</span>Careers</a>
            <a href="#press" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#128240;</span>Press</a>
            <a href="#locations" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#128205;</span>Locations</a>
          </div>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <button type="button" class="cursor-pointer rounded-lg border-0 bg-transparent px-3.5 py-2 font-tdd02-sans text-sm font-medium text-tdd02-ink transition-colors duration-150 group-hover:bg-tdd02-tint group-hover:text-tdd02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd02-acc">Platform &#9662;</button>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 min-w-55 -translate-x-1/2 overflow-hidden rounded-xl border border-tdd02-edge bg-white opacity-0 shadow-[0_16px_48px_oklch(0_0_0/0.12)] [clip-path:polygon(0_0,100%_0,100%_0,0_0)] transition-[clip-path,opacity] duration-400 ease-tdd02 group-hover:pointer-events-auto group-hover:opacity-100 group-hover:[clip-path:polygon(0_0,100%_0,100%_100%,0_100%)] group-focus-within:pointer-events-auto group-focus-within:opacity-100 group-focus-within:[clip-path:polygon(0_0,100%_0,100%_100%,0_100%)] motion-reduce:[clip-path:none] motion-reduce:duration-150">
          <div class="grid grid-cols-2 gap-1 p-2">
            <a href="#analytics" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#9889;</span>Analytics</a>
            <a href="#reporting" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#128202;</span>Reporting</a>
            <a href="#integrations" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#128736;</span>Integrations</a>
            <a href="#security" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#128274;</span>Security</a>
          </div>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <button type="button" class="cursor-pointer rounded-lg border-0 bg-transparent px-3.5 py-2 font-tdd02-sans text-sm font-medium text-tdd02-ink transition-colors duration-150 group-hover:bg-tdd02-tint group-hover:text-tdd02-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd02-acc">Developers &#9662;</button>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 min-w-55 -translate-x-1/2 overflow-hidden rounded-xl border border-tdd02-edge bg-white opacity-0 shadow-[0_16px_48px_oklch(0_0_0/0.12)] [clip-path:polygon(0_0,100%_0,100%_0,0_0)] transition-[clip-path,opacity] duration-400 ease-tdd02 group-hover:pointer-events-auto group-hover:opacity-100 group-hover:[clip-path:polygon(0_0,100%_0,100%_100%,0_100%)] group-focus-within:pointer-events-auto group-focus-within:opacity-100 group-focus-within:[clip-path:polygon(0_0,100%_0,100%_100%,0_100%)] motion-reduce:[clip-path:none] motion-reduce:duration-150">
          <div class="grid grid-cols-2 gap-1 p-2">
            <a href="#api" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#128196;</span>API Docs</a>
            <a href="#sdks" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#129520;</span>SDKs</a>
            <a href="#status" class="flex items-center gap-2.5 rounded-lg px-3 py-2.5 text-[13.5px] font-medium text-tdd02-ink no-underline transition-colors duration-150 hover:bg-tdd02-tint hover:text-tdd02-acc focus-visible:bg-tdd02-tint focus-visible:outline-none"><span class="text-base leading-none" aria-hidden="true">&#127381;</span>Status</a>
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
  --color-tdd02-bg1: #fff7ed;
  --color-tdd02-bg1: oklch(0.97 0.02 70);
  --color-tdd02-bg2: #fef3c7;
  --color-tdd02-bg2: oklch(0.95 0.06 92);
  --color-tdd02-ink: #1c1917;
  --color-tdd02-ink: oklch(0.22 0.01 60);
  --color-tdd02-edge: #e7e5e4;
  --color-tdd02-edge: oklch(0.91 0.005 60);
  --color-tdd02-tint: #fff7ed;
  --color-tdd02-tint: oklch(0.97 0.02 70);
  --color-tdd02-acc: #f97316;
  --color-tdd02-acc: oklch(0.7 0.19 45);
  --font-tdd02-sans: 'DM Sans', system-ui, sans-serif;
  --ease-tdd02: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-02 {
  width: 100%;
  min-height: 100svh;
}

.tdd-02 ::selection {
  background: var(--color-tdd02-acc);
  color: #fff;
}
```
