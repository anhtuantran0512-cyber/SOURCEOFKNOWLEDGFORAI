---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-animated-underline-tabs-navbar/"
title: "Tailwind Animated Underline Tabs Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "Docs-style tabs where the underline is an after: strip that scales from 0 to 0.6 on hover and to 1 on the current tab. All three states are utilities on the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Underline Tabs Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-animated-underline-tabs-navbar/

Docs-style tabs where the underline is an after: strip that scales from 0 to 0.6 on hover and to 1 on the current tab. All three states are utilities on the link, and the active one reads aria-current="page" — so the indicator and the screen-reader announcement come from the same attribute.
## HTML
```html
<div class="tnb-04 group w-full min-h-svh bg-tnb04-page font-tnb04-sans text-tnb04-ink" aria-label="Animated underline tabs navbar demo">
  <input type="checkbox" id="tnb04-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="sticky top-0 z-100 border-b border-tnb04-track bg-tnb04-page">
    <div class="flex h-15 items-center gap-6 px-5 md:px-10">
      <a href="#home" class="shrink-0 text-xl font-extrabold tracking-[-0.04em] text-tnb04-ink no-underline">Stack<span class="text-tnb04-acc">.</span></a>
      <div class="ml-auto hidden items-center gap-3 sm:flex">
        <a href="#signin" class="text-sm font-semibold text-tnb04-mut no-underline transition-colors hover:text-tnb04-ink">Sign in</a>
        <a href="#build" class="rounded-md bg-tnb04-ink px-4 py-2 text-sm font-bold tracking-[-0.01em] text-white no-underline transition-[background,translate] duration-200 hover:-translate-y-px hover:bg-tnb04-acc motion-reduce:transition-none motion-reduce:hover:translate-y-0">Start building</a>
      </div>
      <label for="tnb04-menu" class="ml-auto flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 sm:hidden" aria-hidden="true">
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb04-ink transition-transform duration-300 group-has-checked:translate-y-2 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb04-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb04-ink transition-transform duration-300 group-has-checked:-translate-y-2 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </div>
    <nav class="hidden h-12 items-end overflow-x-auto px-5 [scrollbar-width:none] sm:flex md:px-10" aria-label="Sections">
      <a href="#overview" aria-current="page" class="relative inline-flex h-full shrink-0 items-center gap-1.5 px-5 text-sm font-semibold whitespace-nowrap text-tnb04-mut no-underline transition-colors duration-200 after:absolute after:inset-x-5 after:bottom-0 after:h-[2.5px] after:origin-center after:scale-x-0 after:rounded-t-sm after:bg-tnb04-acc after:transition-transform after:duration-250 hover:text-tnb04-ink hover:after:scale-x-60 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tnb04-acc aria-[current=page]:text-tnb04-acc aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none">Overview</a>
      <a href="#components" class="relative inline-flex h-full shrink-0 items-center gap-1.5 px-5 text-sm font-semibold whitespace-nowrap text-tnb04-mut no-underline transition-colors duration-200 after:absolute after:inset-x-5 after:bottom-0 after:h-[2.5px] after:origin-center after:scale-x-0 after:rounded-t-sm after:bg-tnb04-acc after:transition-transform after:duration-250 hover:text-tnb04-ink hover:after:scale-x-60 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tnb04-acc motion-reduce:after:transition-none">Components <span class="min-w-5 rounded-full bg-tnb04-track px-1.5 text-center text-[11px] font-bold text-tnb04-mut">48</span></a>
      <a href="#templates" class="relative inline-flex h-full shrink-0 items-center gap-1.5 px-5 text-sm font-semibold whitespace-nowrap text-tnb04-mut no-underline transition-colors duration-200 after:absolute after:inset-x-5 after:bottom-0 after:h-[2.5px] after:origin-center after:scale-x-0 after:rounded-t-sm after:bg-tnb04-acc after:transition-transform after:duration-250 hover:text-tnb04-ink hover:after:scale-x-60 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tnb04-acc motion-reduce:after:transition-none">Templates <span class="min-w-5 rounded-full bg-tnb04-track px-1.5 text-center text-[11px] font-bold text-tnb04-mut">12</span></a>
      <a href="#docs" class="relative inline-flex h-full shrink-0 items-center gap-1.5 px-5 text-sm font-semibold whitespace-nowrap text-tnb04-mut no-underline transition-colors duration-200 after:absolute after:inset-x-5 after:bottom-0 after:h-[2.5px] after:origin-center after:scale-x-0 after:rounded-t-sm after:bg-tnb04-acc after:transition-transform after:duration-250 hover:text-tnb04-ink hover:after:scale-x-60 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tnb04-acc motion-reduce:after:transition-none">Documentation</a>
      <a href="#changelog" class="relative inline-flex h-full shrink-0 items-center gap-1.5 px-5 text-sm font-semibold whitespace-nowrap text-tnb04-mut no-underline transition-colors duration-200 after:absolute after:inset-x-5 after:bottom-0 after:h-[2.5px] after:origin-center after:scale-x-0 after:rounded-t-sm after:bg-tnb04-acc after:transition-transform after:duration-250 hover:text-tnb04-ink hover:after:scale-x-60 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tnb04-acc motion-reduce:after:transition-none">Changelog <span class="min-w-5 rounded-full bg-tnb04-track px-1.5 text-center text-[11px] font-bold text-tnb04-mut">3</span></a>
      <a href="#community" class="relative inline-flex h-full shrink-0 items-center gap-1.5 px-5 text-sm font-semibold whitespace-nowrap text-tnb04-mut no-underline transition-colors duration-200 after:absolute after:inset-x-5 after:bottom-0 after:h-[2.5px] after:origin-center after:scale-x-0 after:rounded-t-sm after:bg-tnb04-acc after:transition-transform after:duration-250 hover:text-tnb04-ink hover:after:scale-x-60 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tnb04-acc motion-reduce:after:transition-none">Community</a>
      <a href="#showcase" class="relative inline-flex h-full shrink-0 items-center gap-1.5 px-5 text-sm font-semibold whitespace-nowrap text-tnb04-mut no-underline transition-colors duration-200 after:absolute after:inset-x-5 after:bottom-0 after:h-[2.5px] after:origin-center after:scale-x-0 after:rounded-t-sm after:bg-tnb04-acc after:transition-transform after:duration-250 hover:text-tnb04-ink hover:after:scale-x-60 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tnb04-acc motion-reduce:after:transition-none">Showcase</a>
    </nav>
    <div class="hidden border-t border-tnb04-track px-5 py-2 max-sm:group-has-checked:grid">
      <a href="#overview" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-semibold text-tnb04-acc no-underline">Overview</a>
      <a href="#components" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-semibold text-tnb04-ink no-underline transition-colors hover:bg-tnb04-tint hover:text-tnb04-acc">Components</a>
      <a href="#templates" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-semibold text-tnb04-ink no-underline transition-colors hover:bg-tnb04-tint hover:text-tnb04-acc">Templates</a>
      <a href="#docs" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-semibold text-tnb04-ink no-underline transition-colors hover:bg-tnb04-tint hover:text-tnb04-acc">Documentation</a>
      <a href="#changelog" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-semibold text-tnb04-ink no-underline transition-colors hover:bg-tnb04-tint hover:text-tnb04-acc">Changelog</a>
      <a href="#build" class="mt-2 flex min-h-11 items-center justify-center rounded-md bg-tnb04-ink text-sm font-bold text-white no-underline">Start building</a>
    </div>
  </header>
  <main class="mx-auto max-w-3xl px-5 py-16 md:px-10">
    <h1 class="mb-4 text-4xl font-extrabold tracking-[-0.04em] text-tnb04-ink">Animated Underline <span class="text-tnb04-acc">Tabs</span></h1>
    <p class="text-lg leading-relaxed text-tnb04-mut">Hover any tab for the 60% tease; the current tab holds 100%. Both are <code class="rounded bg-tnb04-tint px-1.5 py-0.5 text-[0.9em] text-tnb04-acc">after:scale-x-*</code> values on the link — and the active state is <code class="rounded bg-tnb04-tint px-1.5 py-0.5 text-[0.9em] text-tnb04-acc">aria-current</code>, not a class.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb04-page: #ffffff;
  --color-tnb04-page: oklch(1 0 0);
  --color-tnb04-ink: #1c1c1c;
  --color-tnb04-ink: oklch(0.24 0 0);
  --color-tnb04-mut: #6f6f6f;
  --color-tnb04-mut: oklch(0.54 0 0);
  --color-tnb04-track: #f0ebe3;
  --color-tnb04-track: oklch(0.94 0.01 80);
  --color-tnb04-tint: #ffe8df;
  --color-tnb04-tint: oklch(0.94 0.03 40);
  --color-tnb04-acc: #ff6b35;
  --color-tnb04-acc: oklch(0.68 0.2 40);
  --font-tnb04-sans: 'Manrope', system-ui, sans-serif;
}

.tnb-04 {
  width: 100%;
  min-height: 100svh;
}

.tnb-04 ::selection {
  background: var(--color-tnb04-acc);
  color: #fff;
}
/* Scrollbar hiding needs a vendor pseudo-element: no variant form exists. */

.tnb-04 nav::-webkit-scrollbar {
  display: none;
}
```
