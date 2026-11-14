---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-gradient-border-animated-navbar/"
title: "Tailwind Gradient Border Animated Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "A floating glass bar inside a rotating gradient ring."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Border Animated Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-gradient-border-animated-navbar/

A floating glass bar inside a rotating gradient ring. The port fixes the original's real flaw: the CSS version swapped whole background declarations at four keyframe stops, so the gradient jumped. Here an @property-registered angle interpolates, and the ring turns continuously — the one place this collection adds a rule to the stylesheet to get a better result.
## HTML
```html
<div class="tnb-11 group w-full min-h-svh bg-tnb11-page font-tnb11-sans text-tnb11-ink" aria-label="Gradient border animated navbar demo">
  <input type="checkbox" id="tnb11-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <div class="sticky top-0 z-100 px-5 py-5 md:px-8">
    <div class="mx-auto max-w-5xl animate-tnb11-spin rounded-2xl bg-[linear-gradient(var(--tnb11-angle),var(--color-tnb11-g1),var(--color-tnb11-g2),var(--color-tnb11-g3))] p-px motion-reduce:animate-none">
      <nav class="relative flex items-center gap-4 rounded-[15px] bg-tnb11-glass/85 py-2 pr-2 pl-5 backdrop-blur-xl" aria-label="Primary">
      <a href="#home" class="shrink-0 text-xl font-extrabold tracking-[-0.02em] text-tnb11-ink no-underline"><span class="bg-linear-[90deg,var(--color-tnb11-g1),var(--color-tnb11-g2)] bg-clip-text text-transparent">Violet</span>Lab</a>
      <ul class="hidden flex-1 list-none items-center gap-1 md:flex">
        <li><a href="#home" aria-current="page" class="block rounded-[10px] bg-white/7 px-3.5 py-2 text-sm font-semibold text-tnb11-ink no-underline">Home</a></li>
        <li><a href="#products" class="block rounded-[10px] px-3.5 py-2 text-sm font-semibold text-tnb11-mut no-underline transition-colors duration-200 hover:bg-white/7 hover:text-tnb11-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb11-g2">Products</a></li>
        <li><a href="#docs" class="block rounded-[10px] px-3.5 py-2 text-sm font-semibold text-tnb11-mut no-underline transition-colors duration-200 hover:bg-white/7 hover:text-tnb11-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb11-g2">Docs</a></li>
        <li><a href="#pricing" class="block rounded-[10px] px-3.5 py-2 text-sm font-semibold text-tnb11-mut no-underline transition-colors duration-200 hover:bg-white/7 hover:text-tnb11-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb11-g2">Pricing</a></li>
        <li><a href="#blog" class="block rounded-[10px] px-3.5 py-2 text-sm font-semibold text-tnb11-mut no-underline transition-colors duration-200 hover:bg-white/7 hover:text-tnb11-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb11-g2">Blog</a></li>
      </ul>
      <a href="#start" class="hidden shrink-0 rounded-[10px] bg-linear-[135deg,var(--color-tnb11-g1),var(--color-tnb11-g2)] px-5 py-2.5 text-sm font-bold text-white no-underline shadow-[0_4px_20px_oklch(0.5_0.25_300/0.4)] transition-[opacity,translate,box-shadow] duration-200 hover:-translate-y-px hover:opacity-85 hover:shadow-[0_8px_28px_oklch(0.5_0.25_300/0.55)] md:block motion-reduce:transition-none motion-reduce:hover:translate-y-0">Get started</a>
      <label for="tnb11-menu" class="ml-auto flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 md:hidden" aria-hidden="true">
        <span class="block h-px w-5 rounded-sm bg-tnb11-ink transition-transform duration-300 group-has-checked:translate-y-1.5 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-px w-5 rounded-sm bg-tnb11-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-px w-5 rounded-sm bg-tnb11-ink transition-transform duration-300 group-has-checked:-translate-y-1.5 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </nav>
    </div>
    <div class="mx-auto mt-2 hidden max-w-5xl rounded-2xl border border-tnb11-g2/25 bg-tnb11-glass/95 p-2 backdrop-blur-xl max-md:group-has-checked:grid">
      <a href="#home" class="flex min-h-11 items-center rounded-[10px] px-3 text-[15px] font-semibold text-tnb11-ink no-underline">Home</a>
      <a href="#products" class="flex min-h-11 items-center rounded-[10px] px-3 text-[15px] font-semibold text-tnb11-mut no-underline transition-colors hover:bg-tnb11-g2/15 hover:text-tnb11-ink">Products</a>
      <a href="#docs" class="flex min-h-11 items-center rounded-[10px] px-3 text-[15px] font-semibold text-tnb11-mut no-underline transition-colors hover:bg-tnb11-g2/15 hover:text-tnb11-ink">Docs</a>
      <a href="#pricing" class="flex min-h-11 items-center rounded-[10px] px-3 text-[15px] font-semibold text-tnb11-mut no-underline transition-colors hover:bg-tnb11-g2/15 hover:text-tnb11-ink">Pricing</a>
      <a href="#start" class="mt-1 flex min-h-11 items-center justify-center rounded-[10px] bg-linear-[135deg,var(--color-tnb11-g1),var(--color-tnb11-g2)] text-sm font-bold text-white no-underline">Get started</a>
    </div>
  </div>
  <main class="mx-auto max-w-3xl px-5 py-16 md:px-8">
    <h1 class="mb-4 bg-linear-[90deg,var(--color-tnb11-g1),var(--color-tnb11-g2),var(--color-tnb11-g3)] bg-clip-text text-4xl font-extrabold tracking-[-0.03em] text-transparent">Gradient Border Navbar</h1>
    <p class="text-lg leading-relaxed text-tnb11-mut">The ring turns smoothly because <code class="rounded bg-white/7 px-1.5 py-0.5 text-[0.9em]">--tnb11-angle</code> is registered with <code class="rounded bg-white/7 px-1.5 py-0.5 text-[0.9em]">@property</code>. The CSS original swapped four whole gradient declarations and visibly jumped between them.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb11-page: #0a0016;
  --color-tnb11-page: oklch(0.13 0.05 300);
  --color-tnb11-glass: #14082a;
  --color-tnb11-glass: oklch(0.19 0.06 300);
  --color-tnb11-ink: #f5f0ff;
  --color-tnb11-ink: oklch(0.96 0.02 300);
  --color-tnb11-mut: #a99bc4;
  --color-tnb11-mut: oklch(0.72 0.05 300);
  --color-tnb11-g1: #c026d3;
  --color-tnb11-g1: oklch(0.6 0.26 325);
  --color-tnb11-g2: #7c3aed;
  --color-tnb11-g2: oklch(0.53 0.26 295);
  --color-tnb11-g3: #2563eb;
  --color-tnb11-g3: oklch(0.52 0.22 262);
  --font-tnb11-sans: 'Raleway', system-ui, sans-serif;
  --animate-tnb11-spin: tnb11-spin 6s linear infinite;
}
/* An angle must be a REGISTERED custom property to interpolate; this is the one
   rule that buys the smooth rotation the CSS original could not get. */

@property --tnb11-angle {
  syntax: '<angle>';
  initial-value: 135deg;
  inherits: false;
}

@keyframes tnb11-spin {
  to {
    --tnb11-angle: 495deg;
  }
}

.tnb-11 {
  width: 100%;
  min-height: 100svh;
}

.tnb-11 ::selection {
  background: var(--color-tnb11-g2);
  color: #fff;
}
```
