---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-split-two-tone-navbar/"
title: "Tailwind Split Two-Tone Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "Editorial contrast: a dark brand-and-nav bar and a yellow action block meeting on a 24px diagonal."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split Two-Tone Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-split-two-tone-navbar/

Editorial contrast: a dark brand-and-nav bar and a yellow action block meeting on a 24px diagonal. The cut is a single arbitrary [clip-path:polygon(…)] utility on the yellow panel, which overlaps the dark bar by 24px so the angle always has dark behind it.
## HTML
```html
<div class="tnb-09 group w-full min-h-svh bg-tnb09-page font-tnb09-sans text-tnb09-ink" aria-label="Split two-tone navbar demo">
  <input type="checkbox" id="tnb09-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="sticky top-0 z-100 md:grid md:h-17 md:grid-cols-[auto_1fr_auto]">
    <div class="flex h-15 items-center bg-tnb09-dark px-5 md:h-full md:px-10">
      <a href="#studio" class="text-xl font-bold tracking-[-0.02em] whitespace-nowrap text-tnb09-paper no-underline">Geo<span class="text-tnb09-yellow">metric</span></a>
      <label for="tnb09-menu" class="ml-auto flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb09-paper transition-transform duration-300 group-has-checked:translate-y-2 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb09-paper transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb09-paper transition-transform duration-300 group-has-checked:-translate-y-2 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </div>
    <nav class="hidden items-center justify-center bg-tnb09-dark md:flex" aria-label="Primary">
      <ul class="flex list-none items-center gap-0">
        <li><a href="#studio" aria-current="page" class="block rounded-md px-4.5 py-2 text-sm font-semibold text-tnb09-yellow no-underline">Studio</a></li>
        <li><a href="#work" class="block rounded-md px-4.5 py-2 text-sm font-medium text-tnb09-paper/60 no-underline transition-colors duration-200 hover:bg-white/8 hover:text-tnb09-paper focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb09-yellow">Work</a></li>
        <li><a href="#process" class="block rounded-md px-4.5 py-2 text-sm font-medium text-tnb09-paper/60 no-underline transition-colors duration-200 hover:bg-white/8 hover:text-tnb09-paper focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb09-yellow">Process</a></li>
        <li><a href="#journal" class="block rounded-md px-4.5 py-2 text-sm font-medium text-tnb09-paper/60 no-underline transition-colors duration-200 hover:bg-white/8 hover:text-tnb09-paper focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb09-yellow">Journal</a></li>
      </ul>
    </nav>
    <div class="hidden items-center gap-3 bg-tnb09-yellow pr-8 pl-10 md:flex md:-ml-6 md:[clip-path:polygon(24px_0,100%_0,100%_100%,0_100%)]">
      <a href="#login" class="rounded-md border-[1.5px] border-tnb09-dark/20 bg-tnb09-dark/10 px-4.5 py-2 text-sm font-bold whitespace-nowrap text-tnb09-dark no-underline transition-colors duration-200 hover:bg-tnb09-dark/18">Log in</a>
      <a href="#start" class="rounded-md bg-tnb09-dark px-4.5 py-2 text-sm font-bold whitespace-nowrap text-tnb09-paper no-underline transition-[background,translate] duration-200 hover:-translate-y-px hover:bg-tnb09-dark2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">Start project</a>
    </div>
    <div class="hidden border-b-[3px] border-tnb09-yellow bg-tnb09-dark px-5 pt-2 pb-4 max-md:group-has-checked:grid">
      <a href="#studio" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-semibold text-tnb09-yellow no-underline">Studio</a>
      <a href="#work" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-medium text-tnb09-paper/70 no-underline transition-colors hover:bg-tnb09-yellow/10 hover:text-tnb09-yellow">Work</a>
      <a href="#process" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-medium text-tnb09-paper/70 no-underline transition-colors hover:bg-tnb09-yellow/10 hover:text-tnb09-yellow">Process</a>
      <a href="#journal" class="flex min-h-11 items-center rounded-md px-2 text-[15px] font-medium text-tnb09-paper/70 no-underline transition-colors hover:bg-tnb09-yellow/10 hover:text-tnb09-yellow">Journal</a>
      <a href="#start" class="mt-2 flex min-h-11 items-center justify-center rounded-md bg-tnb09-yellow text-sm font-bold text-tnb09-dark no-underline">Start project</a>
    </div>
  </header>
  <main class="mx-auto max-w-3xl px-5 py-16 md:px-8">
    <h1 class="mb-4 text-4xl font-bold tracking-[-0.03em] text-tnb09-ink">Split Two-Tone Navbar</h1>
    <p class="text-lg leading-relaxed text-tnb09-mut">The diagonal is two complementary <code class="rounded bg-tnb09-yellow/25 px-1.5 py-0.5 text-[0.9em]">clip-path</code> polygons, each stated on the panel it cuts. Below <code class="rounded bg-tnb09-yellow/25 px-1.5 py-0.5 text-[0.9em]">md</code> both are dropped and the yellow survives as a 3px rule.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb09-page: #ffffff;
  --color-tnb09-page: oklch(1 0 0);
  --color-tnb09-dark: #1a1a2e;
  --color-tnb09-dark: oklch(0.24 0.04 280);
  --color-tnb09-dark2: #2a2a4e;
  --color-tnb09-dark2: oklch(0.32 0.06 280);
  --color-tnb09-yellow: #f7c948;
  --color-tnb09-yellow: oklch(0.85 0.15 90);
  --color-tnb09-paper: #f0eeff;
  --color-tnb09-paper: oklch(0.95 0.02 290);
  --color-tnb09-ink: #1a1a2e;
  --color-tnb09-ink: oklch(0.24 0.04 280);
  --color-tnb09-mut: #6b7280;
  --color-tnb09-mut: oklch(0.55 0.02 265);
  --font-tnb09-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tnb-09 {
  width: 100%;
  min-height: 100svh;
}

.tnb-09 ::selection {
  background: var(--color-tnb09-yellow);
  color: #1a1a2e;
}
```
