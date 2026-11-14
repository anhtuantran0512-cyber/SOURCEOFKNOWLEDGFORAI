---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-underline-slide-nav-hover-effect/"
title: "Tailwind Underline Slide Nav Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six navigation underline styles — grow from left, expand from centre, an overline that switches origin mid-interaction, a double line, a thick highlight and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Underline Slide Nav Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-underline-slide-nav-hover-effect/

Six navigation underline styles — grow from left, expand from centre, an overline that switches origin mid-interaction, a double line, a thick highlight and a dot indicator. Six navs, one anchor recipe, one changed utility each.
## HTML
```html
<section class="thv-25 w-full min-h-svh bg-thv25-bg font-thv25-sans px-8 py-12 flex flex-col gap-11">
  <p class="text-center text-[0.72rem] tracking-[0.15em] uppercase text-thv25-dim">Underline Slide Nav — 6 Styles</p>

  <nav aria-label="Grow from left" class="flex flex-wrap items-center gap-8">
    <a href="#" aria-current="page" class="relative pb-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc aria-[current=page]:text-white after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 aria-[current=page]:after:scale-x-100 motion-reduce:after:transition-none">Home</a>
    <a href="#" class="relative pb-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">About</a>
    <a href="#" class="relative pb-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Work</a>
    <a href="#" class="relative pb-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv25-dim">Grow from Left</span>
  </nav>

  <nav aria-label="Expand from centre" class="flex flex-wrap items-center gap-8">
    <a href="#" class="relative pb-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-center after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Home</a>
    <a href="#" class="relative pb-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-center after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">About</a>
    <a href="#" class="relative pb-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-center after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Work</a>
    <a href="#" class="relative pb-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-center after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv25-dim">Expand from Centre</span>
  </nav>

  <nav aria-label="Top overline" class="flex flex-wrap items-center gap-8">
    <a href="#" class="relative pt-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-thv25-acc before:origin-right before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 hover:before:origin-left focus-visible:before:scale-x-100 focus-visible:before:origin-left motion-reduce:before:transition-none">Home</a>
    <a href="#" class="relative pt-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-thv25-acc before:origin-right before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 hover:before:origin-left focus-visible:before:scale-x-100 focus-visible:before:origin-left motion-reduce:before:transition-none">About</a>
    <a href="#" class="relative pt-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-thv25-acc before:origin-right before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 hover:before:origin-left focus-visible:before:scale-x-100 focus-visible:before:origin-left motion-reduce:before:transition-none">Work</a>
    <a href="#" class="relative pt-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-thv25-acc before:origin-right before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 hover:before:origin-left focus-visible:before:scale-x-100 focus-visible:before:origin-left motion-reduce:before:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv25-dim">Top Overline</span>
  </nav>

  <nav aria-label="Double line" class="flex flex-wrap items-center gap-8">
    <a href="#" class="relative py-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-thv25-acc before:origin-right before:scale-x-0 before:transition-transform before:duration-350 after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-350 hover:before:scale-x-100 hover:after:scale-x-100 focus-visible:before:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:before:transition-none motion-reduce:after:transition-none">Home</a>
    <a href="#" class="relative py-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-thv25-acc before:origin-right before:scale-x-0 before:transition-transform before:duration-350 after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-350 hover:before:scale-x-100 hover:after:scale-x-100 focus-visible:before:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:before:transition-none motion-reduce:after:transition-none">About</a>
    <a href="#" class="relative py-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-thv25-acc before:origin-right before:scale-x-0 before:transition-transform before:duration-350 after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-350 hover:before:scale-x-100 hover:after:scale-x-100 focus-visible:before:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:before:transition-none motion-reduce:after:transition-none">Work</a>
    <a href="#" class="relative py-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-thv25-acc before:origin-right before:scale-x-0 before:transition-transform before:duration-350 after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv25-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-350 hover:before:scale-x-100 hover:after:scale-x-100 focus-visible:before:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:before:transition-none motion-reduce:after:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv25-dim">Double Line</span>
  </nav>

  <nav aria-label="Thick fill highlight" class="flex flex-wrap items-center gap-8">
    <a href="#" class="relative isolate px-1.5 py-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:-inset-x-1.5 after:-bottom-0.5 after:-z-10 after:h-[34px] after:rounded after:bg-thv25-acc after:origin-bottom after:scale-y-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] hover:after:scale-y-100 focus-visible:after:scale-y-100 motion-reduce:after:transition-none">Home</a>
    <a href="#" class="relative isolate px-1.5 py-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:-inset-x-1.5 after:-bottom-0.5 after:-z-10 after:h-[34px] after:rounded after:bg-thv25-acc after:origin-bottom after:scale-y-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] hover:after:scale-y-100 focus-visible:after:scale-y-100 motion-reduce:after:transition-none">About</a>
    <a href="#" class="relative isolate px-1.5 py-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:-inset-x-1.5 after:-bottom-0.5 after:-z-10 after:h-[34px] after:rounded after:bg-thv25-acc after:origin-bottom after:scale-y-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] hover:after:scale-y-100 focus-visible:after:scale-y-100 motion-reduce:after:transition-none">Work</a>
    <a href="#" class="relative isolate px-1.5 py-1 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:-inset-x-1.5 after:-bottom-0.5 after:-z-10 after:h-[34px] after:rounded after:bg-thv25-acc after:origin-bottom after:scale-y-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.34,1.56,.64,1)] hover:after:scale-y-100 focus-visible:after:scale-y-100 motion-reduce:after:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv25-dim">Thick Fill Highlight</span>
  </nav>

  <nav aria-label="Dot indicator" class="flex flex-wrap items-center gap-8">
    <a href="#" class="relative pb-2 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:bottom-0 after:left-1/2 after:w-[5px] after:h-[5px] after:rounded-full after:bg-thv25-acc after:-translate-x-1/2 after:scale-0 after:transition-transform after:duration-250 after:ease-[cubic-bezier(.34,1.56,.64,1)] hover:after:scale-100 focus-visible:after:scale-100 motion-reduce:after:transition-none">Home</a>
    <a href="#" class="relative pb-2 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:bottom-0 after:left-1/2 after:w-[5px] after:h-[5px] after:rounded-full after:bg-thv25-acc after:-translate-x-1/2 after:scale-0 after:transition-transform after:duration-250 after:ease-[cubic-bezier(.34,1.56,.64,1)] hover:after:scale-100 focus-visible:after:scale-100 motion-reduce:after:transition-none">About</a>
    <a href="#" class="relative pb-2 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:bottom-0 after:left-1/2 after:w-[5px] after:h-[5px] after:rounded-full after:bg-thv25-acc after:-translate-x-1/2 after:scale-0 after:transition-transform after:duration-250 after:ease-[cubic-bezier(.34,1.56,.64,1)] hover:after:scale-100 focus-visible:after:scale-100 motion-reduce:after:transition-none">Work</a>
    <a href="#" class="relative pb-2 text-[0.95rem] font-medium text-thv25-ink no-underline transition-colors duration-250 rounded-xs hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv25-acc after:content-[''] after:absolute after:bottom-0 after:left-1/2 after:w-[5px] after:h-[5px] after:rounded-full after:bg-thv25-acc after:-translate-x-1/2 after:scale-0 after:transition-transform after:duration-250 after:ease-[cubic-bezier(.34,1.56,.64,1)] hover:after:scale-100 focus-visible:after:scale-100 motion-reduce:after:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv25-dim">Dot Indicator</span>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv25-bg: #0b0b0f;
  --color-thv25-bg: oklch(0.13 0.01 285);
  --color-thv25-ink: #cccccc;
  --color-thv25-ink: oklch(0.83 0 0);
  --color-thv25-dim: #8a8a94;
  --color-thv25-dim: oklch(0.64 0.01 285);
  --color-thv25-acc: #7c6af7;
  --color-thv25-acc: oklch(0.62 0.2 285);
  --font-thv25-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-25 {
  width: 100%;
  min-height: 100svh;
}

.thv-25 ::selection {
  background: var(--color-thv25-acc);
  color: #fff;
}
```
