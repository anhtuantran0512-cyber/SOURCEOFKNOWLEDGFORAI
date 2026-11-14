---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-centered-logo-navbar/"
title: "Tailwind Centered Logo Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "The fashion-house header: a serif logotype dead centre, uppercase link groups balanced either side."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Centered Logo Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-centered-logo-navbar/

The fashion-house header: a serif logotype dead centre, uppercase link groups balanced either side. grid-cols-[1fr_auto_1fr] is the entire layout, and the mobile state is the same grid collapsed to two cells — not the second bar the CSS original had to maintain.
## HTML
```html
<div class="tnb-12 group w-full min-h-svh bg-tnb12-page font-tnb12-sans text-tnb12-ink" aria-label="Centered logo navbar demo">
  <input type="checkbox" id="tnb12-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="sticky top-0 z-100 border-b border-tnb12-edge bg-tnb12-page">
    <div class="flex h-15 items-center px-5 md:grid md:h-18 md:grid-cols-[1fr_auto_1fr] md:px-10">
      <nav class="hidden justify-self-end md:block" aria-label="Collections">
        <ul class="flex list-none items-center gap-0">
          <li><a href="#collections" aria-current="page" class="block rounded px-4 py-2 text-xs font-medium tracking-[0.12em] whitespace-nowrap text-tnb12-ink uppercase no-underline">Collections</a></li>
          <li><a href="#lookbook" class="block rounded px-4 py-2 text-xs font-medium tracking-[0.12em] whitespace-nowrap text-tnb12-mut uppercase no-underline transition-colors duration-200 hover:text-tnb12-ink">Lookbook</a></li>
          <li><a href="#stores" class="block rounded px-4 py-2 text-xs font-medium tracking-[0.12em] whitespace-nowrap text-tnb12-mut uppercase no-underline transition-colors duration-200 hover:text-tnb12-ink">Stores</a></li>
        </ul>
      </nav>
      <a href="#home" class="block text-center no-underline md:px-6">
        <span class="block font-tnb12-display text-xl font-semibold tracking-[0.08em] whitespace-nowrap text-tnb12-ink md:text-2xl">AURORE</span>
        <span class="hidden text-[10px] font-medium tracking-[0.2em] text-tnb12-acc uppercase md:block">Paris &mdash; since 1924</span>
      </a>
      <nav class="hidden justify-self-start md:block" aria-label="Secondary">
        <ul class="flex list-none items-center justify-start gap-0">
          <li><a href="#about" class="block rounded px-4 py-2 text-xs font-medium tracking-[0.12em] whitespace-nowrap text-tnb12-mut uppercase no-underline transition-colors duration-200 hover:text-tnb12-ink">About</a></li>
          <li><a href="#atelier" class="block rounded px-4 py-2 text-xs font-medium tracking-[0.12em] whitespace-nowrap text-tnb12-mut uppercase no-underline transition-colors duration-200 hover:text-tnb12-ink">Atelier</a></li>
          <li><a href="#reserve" class="ml-2 block rounded border border-tnb12-acc px-3.5 py-1.5 text-xs font-medium tracking-[0.12em] whitespace-nowrap text-tnb12-acc uppercase no-underline transition-colors duration-200 hover:bg-tnb12-acc hover:text-tnb12-page">Reserve</a></li>
        </ul>
      </nav>
      <label for="tnb12-menu" class="ml-auto flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-px w-5 rounded-sm bg-tnb12-ink transition-transform duration-300 group-has-checked:translate-y-1.5 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-px w-5 rounded-sm bg-tnb12-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-px w-5 rounded-sm bg-tnb12-ink transition-transform duration-300 group-has-checked:-translate-y-1.5 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </div>
    <nav class="hidden divide-y divide-tnb12-edge border-t border-tnb12-edge px-5 pb-3 max-md:group-has-checked:grid" aria-label="Mobile">
      <a href="#collections" class="flex min-h-11 items-center text-xs font-medium tracking-[0.12em] text-tnb12-ink uppercase no-underline">Collections</a>
      <a href="#lookbook" class="flex min-h-11 items-center text-xs font-medium tracking-[0.12em] text-tnb12-mut uppercase no-underline transition-colors hover:text-tnb12-ink">Lookbook</a>
      <a href="#stores" class="flex min-h-11 items-center text-xs font-medium tracking-[0.12em] text-tnb12-mut uppercase no-underline transition-colors hover:text-tnb12-ink">Stores</a>
      <a href="#about" class="flex min-h-11 items-center text-xs font-medium tracking-[0.12em] text-tnb12-mut uppercase no-underline transition-colors hover:text-tnb12-ink">About</a>
      <a href="#atelier" class="flex min-h-11 items-center text-xs font-medium tracking-[0.12em] text-tnb12-mut uppercase no-underline transition-colors hover:text-tnb12-ink">Atelier</a>
      <a href="#reserve" class="flex min-h-11 items-center text-xs font-medium tracking-[0.12em] text-tnb12-acc uppercase no-underline">Reserve</a>
    </nav>
  </header>
  <main class="mx-auto max-w-2xl px-6 py-16 text-center">
    <h1 class="mb-4 font-tnb12-display text-4xl font-semibold tracking-[0.05em] text-tnb12-ink md:text-5xl">Centered Logo Navbar</h1>
    <p class="text-lg leading-loose text-tnb12-mut">Three grid tracks — <code class="rounded bg-tnb12-acc/12 px-1.5 py-0.5 text-[0.9em]">1fr auto 1fr</code> — hold the wordmark in the middle while the link groups fill the sides. Below <code class="rounded bg-tnb12-acc/12 px-1.5 py-0.5 text-[0.9em]">md</code> the same header keeps the wordmark and folds the links into a hairline list.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb12-page: #faf8f5;
  --color-tnb12-page: oklch(0.98 0.006 85);
  --color-tnb12-ink: #1a1612;
  --color-tnb12-ink: oklch(0.22 0.01 60);
  --color-tnb12-mut: #857a6b;
  --color-tnb12-mut: oklch(0.58 0.02 75);
  --color-tnb12-edge: #e8e0d4;
  --color-tnb12-edge: oklch(0.91 0.015 85);
  --color-tnb12-acc: #a5853f;
  --color-tnb12-acc: oklch(0.63 0.09 85);
  --font-tnb12-sans: 'Jost', system-ui, sans-serif;
  --font-tnb12-display: 'Cormorant Garamond', Georgia, serif;
}

.tnb-12 {
  width: 100%;
  min-height: 100svh;
}

.tnb-12 ::selection {
  background: var(--color-tnb12-acc);
  color: #faf8f5;
}
```
