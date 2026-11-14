---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-glassmorphism-frosted-navbar/"
title: "Tailwind Glassmorphism Frosted Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "The frosted sticky bar, and the first thing worth porting: backdrop-blur-xl backdrop-saturate-150 over a bg-white/8 fill, sticky at the top, with a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Frosted Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-glassmorphism-frosted-navbar/

The frosted sticky bar, and the first thing worth porting: backdrop-blur-xl backdrop-saturate-150 over a bg-white/8 fill, sticky at the top, with a checkbox-driven mobile menu. The CSS original needs a second hand-built mobile bar; here the same bar carries both layouts, because the breakpoint is a prefix on the element that changes.
## HTML
```html
<div class="tnb-01 group w-full min-h-svh bg-linear-[160deg,var(--color-tnb01-bg1),var(--color-tnb01-bg2)] font-tnb01-sans text-tnb01-ink" aria-label="Glassmorphism frosted navbar demo">
  <input type="checkbox" id="tnb01-menu" class="sr-only peer" aria-label="Toggle navigation menu">
  <header class="sticky top-0 z-100 border-b border-white/15 bg-white/8 backdrop-blur-xl backdrop-saturate-150">
    <nav class="mx-auto flex h-16 max-w-7xl items-center justify-between gap-4 px-5 md:px-8" aria-label="Primary">
      <a href="#home" class="flex shrink-0 items-center gap-2.5 text-lg font-extrabold tracking-[-0.02em] text-tnb01-ink no-underline">
        <span class="grid size-8 place-items-center rounded-lg bg-linear-[135deg,var(--color-tnb01-acc),var(--color-tnb01-acc2)] text-base text-white" aria-hidden="true">&#10022;</span>Prisma
      </a>
      <ul class="hidden list-none items-center gap-1 md:flex">
        <li><a href="#home" aria-current="page" class="relative rounded-lg bg-tnb01-acc/15 px-3.5 py-2 text-sm font-medium text-tnb01-acc no-underline transition-colors duration-200 after:absolute after:-bottom-0.5 after:left-1/2 after:size-1 after:-translate-x-1/2 after:rounded-full after:bg-tnb01-acc after:content-[''] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb01-acc">Home</a></li>
        <li><a href="#products" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tnb01-ink/75 no-underline transition-colors duration-200 hover:bg-tnb01-acc/15 hover:text-tnb01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb01-acc">Products</a></li>
        <li><a href="#pricing" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tnb01-ink/75 no-underline transition-colors duration-200 hover:bg-tnb01-acc/15 hover:text-tnb01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb01-acc">Pricing</a></li>
        <li><a href="#blog" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tnb01-ink/75 no-underline transition-colors duration-200 hover:bg-tnb01-acc/15 hover:text-tnb01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb01-acc">Blog</a></li>
        <li><a href="#about" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tnb01-ink/75 no-underline transition-colors duration-200 hover:bg-tnb01-acc/15 hover:text-tnb01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb01-acc">About</a></li>
      </ul>
      <div class="hidden shrink-0 items-center gap-3 md:flex">
        <a href="#signin" class="rounded-lg border border-white/15 px-4 py-2 text-sm font-semibold text-tnb01-ink no-underline transition-colors duration-200 hover:bg-tnb01-acc/15 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnb01-acc">Sign in</a>
        <a href="#start" class="rounded-lg bg-linear-[135deg,var(--color-tnb01-acc),var(--color-tnb01-acc2)] px-4 py-2 text-sm font-semibold text-white no-underline transition-[opacity,translate] duration-200 hover:-translate-y-px hover:opacity-85 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none motion-reduce:hover:translate-y-0">Get started</a>
      </div>
      <label for="tnb01-menu" class="flex size-11 cursor-pointer flex-col items-center justify-center gap-1.5 rounded-lg md:hidden" aria-hidden="true">
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb01-ink transition-transform duration-300 group-has-checked:translate-y-2 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb01-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
        <span class="block h-0.5 w-5.5 rounded-sm bg-tnb01-ink transition-transform duration-300 group-has-checked:-translate-y-2 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
      </label>
    </nav>
    <div class="hidden border-t border-white/10 bg-tnb01-bg2/95 px-5 py-4 backdrop-blur-xl max-md:group-has-checked:grid">
      <a href="#home" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb01-acc no-underline">Home</a>
      <a href="#products" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb01-ink/80 no-underline transition-colors hover:bg-tnb01-acc/15 hover:text-tnb01-acc">Products</a>
      <a href="#pricing" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb01-ink/80 no-underline transition-colors hover:bg-tnb01-acc/15 hover:text-tnb01-acc">Pricing</a>
      <a href="#blog" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb01-ink/80 no-underline transition-colors hover:bg-tnb01-acc/15 hover:text-tnb01-acc">Blog</a>
      <a href="#about" class="flex min-h-11 items-center rounded-lg px-3 text-[15px] font-medium text-tnb01-ink/80 no-underline transition-colors hover:bg-tnb01-acc/15 hover:text-tnb01-acc">About</a>
      <div class="mt-3 flex gap-3 border-t border-white/10 pt-4">
        <a href="#signin" class="flex min-h-11 flex-1 items-center justify-center rounded-lg border border-white/15 text-sm font-semibold text-tnb01-ink no-underline">Sign in</a>
        <a href="#start" class="flex min-h-11 flex-1 items-center justify-center rounded-lg bg-linear-[135deg,var(--color-tnb01-acc),var(--color-tnb01-acc2)] text-sm font-semibold text-white no-underline">Get started</a>
      </div>
    </div>
  </header>
  <main class="mx-auto max-w-3xl px-5 py-16 md:px-8">
    <h1 class="mb-4 bg-linear-[135deg,var(--color-tnb01-acc),var(--color-tnb01-acc2)] bg-clip-text text-4xl font-extrabold tracking-[-0.03em] text-transparent md:text-5xl">Glassmorphism Navbar</h1>
    <p class="text-lg leading-relaxed text-tnb01-ink/65">Narrow the window past <code class="rounded bg-white/10 px-1.5 py-0.5 text-[0.9em]">md</code> and the same bar becomes the hamburger layout — one navbar, two class lists. Scroll: the bar stays, and <code class="rounded bg-white/10 px-1.5 py-0.5 text-[0.9em]">backdrop-blur-xl</code> blurs the gradient behind it.</p>
    <div class="mt-10 grid gap-4 sm:grid-cols-3">
      <div class="rounded-2xl border border-white/10 bg-white/5 p-5 text-sm text-tnb01-ink/70">Translucent fill first — blur over opaque paint is a no-op.</div>
      <div class="rounded-2xl border border-white/10 bg-white/5 p-5 text-sm text-tnb01-ink/70">State lives on the element: <code>group-has-checked:</code>, not a sibling chain.</div>
      <div class="rounded-2xl border border-white/10 bg-white/5 p-5 text-sm text-tnb01-ink/70">44px rows on mobile, declared as <code>min-h-11</code>.</div>
    </div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb01-bg1: #14102b;
  --color-tnb01-bg1: oklch(0.22 0.06 285);
  --color-tnb01-bg2: #241a4d;
  --color-tnb01-bg2: oklch(0.3 0.09 288);
  --color-tnb01-ink: #f0eeff;
  --color-tnb01-ink: oklch(0.95 0.02 290);
  --color-tnb01-acc: #a78bfa;
  --color-tnb01-acc: oklch(0.74 0.15 295);
  --color-tnb01-acc2: #60a5fa;
  --color-tnb01-acc2: oklch(0.73 0.14 255);
  --font-tnb01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build compiles. */

.tnb-01 {
  width: 100%;
  min-height: 100svh;
}

.tnb-01 ::selection {
  background: var(--color-tnb01-acc);
  color: #14102b;
}
```
