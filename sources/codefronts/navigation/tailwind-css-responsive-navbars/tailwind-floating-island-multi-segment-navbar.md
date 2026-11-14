---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-floating-island-multi-segment-navbar/"
title: "Tailwind Floating Island Multi-Segment Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "Three detached capsules — brand, links, call to action — floating over the page instead of one bar."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Island Multi-Segment Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-floating-island-multi-segment-navbar/

Three detached capsules — brand, links, call to action — floating over the page instead of one bar. Each island carries the same glass recipe as a shared set of utilities, and below md the middle island simply stops existing while its links drop out of the brand capsule.
## HTML
```html
<div class="tnb-16 group w-full min-h-svh bg-linear-[180deg,var(--color-tnb16-page),var(--color-tnb16-page2)] font-tnb16-sans text-tnb16-ink" aria-label="Floating island navbar demo">
  <input type="checkbox" id="tnb16-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <div class="sticky top-0 z-100 flex items-start justify-between gap-4 px-5 py-5 md:px-8">
    <div class="relative flex items-center rounded-full border border-tnb16-edge bg-white/85 backdrop-blur-xl shadow-[0_4px_24px_oklch(0_0_0/0.08),inset_0_1px_0_oklch(1_0_0/0.6)]">
      <a href="#home" class="flex items-center gap-2 px-5 py-2.5 text-base font-extrabold tracking-[-0.02em] text-tnb16-ink no-underline">
        <span class="size-2 rounded-full bg-tnb16-dot shadow-[0_0_0_3px_oklch(0.72_0.17_140/0.2)]" aria-hidden="true"></span>Canopy
      </a>
      <label for="tnb16-menu" class="mr-1.5 flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 rounded-full md:hidden" aria-hidden="true">
        <span class="block h-px w-4.5 rounded-sm bg-tnb16-ink transition-transform duration-300 group-has-checked:translate-y-1.5 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-px w-4.5 rounded-sm bg-tnb16-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-px w-4.5 rounded-sm bg-tnb16-ink transition-transform duration-300 group-has-checked:-translate-y-1.5 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
      <nav class="absolute inset-x-0 top-[calc(100%+10px)] hidden rounded-3xl border border-tnb16-edge bg-white/92 p-2 backdrop-blur-xl shadow-[0_8px_32px_oklch(0_0_0/0.1)] max-md:group-has-checked:grid" aria-label="Mobile">
        <a href="#explore" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-semibold text-tnb16-acc no-underline">Explore</a>
        <a href="#products" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-semibold text-tnb16-mut no-underline transition-colors hover:bg-tnb16-acc/8 hover:text-tnb16-acc">Products</a>
        <a href="#sustainability" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-semibold text-tnb16-mut no-underline transition-colors hover:bg-tnb16-acc/8 hover:text-tnb16-acc">Sustainability</a>
        <a href="#journal" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-semibold text-tnb16-mut no-underline transition-colors hover:bg-tnb16-acc/8 hover:text-tnb16-acc">Journal</a>
        <a href="#about" class="flex min-h-11 items-center rounded-full px-4 text-[15px] font-semibold text-tnb16-mut no-underline transition-colors hover:bg-tnb16-acc/8 hover:text-tnb16-acc">About</a>
        <a href="#start" class="mt-1 flex min-h-11 items-center justify-center rounded-full bg-tnb16-acc text-sm font-bold text-white no-underline">Get started</a>
      </nav>
    </div>
    <nav class="hidden items-center rounded-full border border-tnb16-edge bg-white/85 p-1.5 backdrop-blur-xl shadow-[0_4px_24px_oklch(0_0_0/0.08),inset_0_1px_0_oklch(1_0_0/0.6)] md:flex" aria-label="Primary">
      <ul class="flex list-none items-center gap-0">
        <li><a href="#explore" aria-current="page" class="block rounded-full px-3.5 py-1.5 text-sm font-semibold whitespace-nowrap text-tnb16-acc no-underline aria-[current=page]:bg-tnb16-acc/12">Explore</a></li>
        <li><a href="#products" class="block rounded-full px-3.5 py-1.5 text-sm font-semibold whitespace-nowrap text-tnb16-mut no-underline transition-colors duration-200 hover:bg-tnb16-acc/8 hover:text-tnb16-ink">Products</a></li>
        <li><a href="#sustainability" class="block rounded-full px-3.5 py-1.5 text-sm font-semibold whitespace-nowrap text-tnb16-mut no-underline transition-colors duration-200 hover:bg-tnb16-acc/8 hover:text-tnb16-ink">Sustainability</a></li>
        <li><a href="#journal" class="block rounded-full px-3.5 py-1.5 text-sm font-semibold whitespace-nowrap text-tnb16-mut no-underline transition-colors duration-200 hover:bg-tnb16-acc/8 hover:text-tnb16-ink">Journal</a></li>
        <li><a href="#about" class="block rounded-full px-3.5 py-1.5 text-sm font-semibold whitespace-nowrap text-tnb16-mut no-underline transition-colors duration-200 hover:bg-tnb16-acc/8 hover:text-tnb16-ink">About</a></li>
      </ul>
    </nav>
    <div class="hidden items-center gap-2 rounded-full border border-tnb16-edge bg-white/85 p-1.5 pl-4 backdrop-blur-xl shadow-[0_4px_24px_oklch(0_0_0/0.08),inset_0_1px_0_oklch(1_0_0/0.6)] lg:flex">
      <span class="text-[13px] font-semibold whitespace-nowrap text-tnb16-mut">Join 12k+ members</span>
      <a href="#start" class="rounded-full bg-tnb16-acc px-4 py-2 text-sm font-bold whitespace-nowrap text-white no-underline shadow-[0_2px_8px_oklch(0.55_0.14_140/0.35)] transition-[background,transform] duration-200 hover:scale-97 hover:bg-tnb16-accdark motion-reduce:transition-none motion-reduce:hover:scale-100">Get started</a>
    </div>
  </div>
  <main class="mx-auto max-w-3xl px-5 py-16 md:px-8">
    <h1 class="mb-4 text-4xl font-extrabold tracking-[-0.04em] text-tnb16-ink">Floating Island Navbar</h1>
    <p class="text-lg leading-relaxed text-tnb16-mut">Three capsules, no bar. Each carries its own glass recipe, so any one of them can differ without unpicking a shared rule — and on mobile the brand island absorbs the menu while the others simply stand down.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb16-page: #f4f8ef;
  --color-tnb16-page: oklch(0.97 0.02 130);
  --color-tnb16-page2: #e6f0dc;
  --color-tnb16-page2: oklch(0.94 0.03 130);
  --color-tnb16-ink: #1c2b0e;
  --color-tnb16-ink: oklch(0.27 0.06 130);
  --color-tnb16-mut: #566b45;
  --color-tnb16-mut: oklch(0.48 0.05 130);
  --color-tnb16-edge: #d3e0c6;
  --color-tnb16-edge: oklch(0.89 0.03 130);
  --color-tnb16-acc: #4a8c2a;
  --color-tnb16-acc: oklch(0.55 0.14 140);
  --color-tnb16-accdark: #3a6e20;
  --color-tnb16-accdark: oklch(0.47 0.13 140);
  --color-tnb16-dot: #6abf40;
  --color-tnb16-dot: oklch(0.72 0.17 140);
  --font-tnb16-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tnb-16 {
  width: 100%;
  min-height: 100svh;
}

.tnb-16 ::selection {
  background: var(--color-tnb16-acc);
  color: #fff;
}
```
