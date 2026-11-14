---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-highlight-fill-nav-hover-effect/"
title: "Tailwind Highlight Fill Nav Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six nav fills — pill, block, gradient, a slashed clip-path, a radial spotlight and a difference-blend invert."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Highlight Fill Nav Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-highlight-fill-nav-hover-effect/

Six nav fills — pill, block, gradient, a slashed clip-path, a radial spotlight and a difference-blend invert. Each is a before: layer behind the label; the invert variant is the one that needs a stacking context to behave.
## HTML
```html
<section class="thv-26 w-full min-h-svh bg-thv26-bg font-thv26-sans px-8 py-12 flex flex-col gap-10">
  <p class="text-center text-[0.72rem] tracking-[0.15em] uppercase text-thv26-dim">Highlight Fill Nav — 6 Styles</p>

  <nav aria-label="Pill fill" class="flex flex-wrap items-center gap-6">
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded-full transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded-full before:bg-thv26-acc before:opacity-0 before:scale-x-[.1] before:scale-y-[.4] before:transition-[transform,opacity] before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:opacity-100 hover:before:scale-100 focus-visible:before:opacity-100 focus-visible:before:scale-100 motion-reduce:before:transition-opacity">Explore</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded-full transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded-full before:bg-thv26-acc before:opacity-0 before:scale-x-[.1] before:scale-y-[.4] before:transition-[transform,opacity] before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:opacity-100 hover:before:scale-100 focus-visible:before:opacity-100 focus-visible:before:scale-100 motion-reduce:before:transition-opacity">Gallery</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded-full transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded-full before:bg-thv26-acc before:opacity-0 before:scale-x-[.1] before:scale-y-[.4] before:transition-[transform,opacity] before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:opacity-100 hover:before:scale-100 focus-visible:before:opacity-100 focus-visible:before:scale-100 motion-reduce:before:transition-opacity">Studio</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded-full transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded-full before:bg-thv26-acc before:opacity-0 before:scale-x-[.1] before:scale-y-[.4] before:transition-[transform,opacity] before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:opacity-100 hover:before:scale-100 focus-visible:before:opacity-100 focus-visible:before:scale-100 motion-reduce:before:transition-opacity">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv26-dim">Pill Fill</span>
  </nav>

  <nav aria-label="Block fill" class="flex flex-wrap items-center gap-6">
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:bg-thv26-acc before:origin-bottom before:scale-y-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-y-100 focus-visible:before:scale-y-100 motion-reduce:before:transition-none">Explore</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:bg-thv26-acc before:origin-bottom before:scale-y-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-y-100 focus-visible:before:scale-y-100 motion-reduce:before:transition-none">Gallery</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:bg-thv26-acc before:origin-bottom before:scale-y-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-y-100 focus-visible:before:scale-y-100 motion-reduce:before:transition-none">Studio</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:bg-thv26-acc before:origin-bottom before:scale-y-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-y-100 focus-visible:before:scale-y-100 motion-reduce:before:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv26-dim">Block Fill</span>
  </nav>

  <nav aria-label="Gradient fill" class="flex flex-wrap items-center gap-6">
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:opacity-90 before:bg-[linear-gradient(135deg,#7c6af7,#f764a8)] before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Explore</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:opacity-90 before:bg-[linear-gradient(135deg,#7c6af7,#f764a8)] before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Gallery</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:opacity-90 before:bg-[linear-gradient(135deg,#7c6af7,#f764a8)] before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Studio</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline rounded transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:opacity-90 before:bg-[linear-gradient(135deg,#7c6af7,#f764a8)] before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv26-dim">Gradient Fill</span>
  </nav>

  <nav aria-label="Slash clip" class="flex flex-wrap items-center gap-6">
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline transition-colors duration-250 hover:text-[#111111] focus-visible:text-[#111111] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-gold before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv26-gold before:[clip-path:polygon(8%_0%,100%_0%,92%_100%,0%_100%)] before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Explore</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline transition-colors duration-250 hover:text-[#111111] focus-visible:text-[#111111] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-gold before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv26-gold before:[clip-path:polygon(8%_0%,100%_0%,92%_100%,0%_100%)] before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Gallery</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline transition-colors duration-250 hover:text-[#111111] focus-visible:text-[#111111] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-gold before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv26-gold before:[clip-path:polygon(8%_0%,100%_0%,92%_100%,0%_100%)] before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Studio</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline transition-colors duration-250 hover:text-[#111111] focus-visible:text-[#111111] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-gold before:content-[''] before:absolute before:inset-0 before:-z-10 before:bg-thv26-gold before:[clip-path:polygon(8%_0%,100%_0%,92%_100%,0%_100%)] before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv26-dim">Slash Clip</span>
  </nav>

  <nav aria-label="Radial spotlight" class="flex flex-wrap items-center gap-6">
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:opacity-0 before:scale-0 before:bg-[radial-gradient(ellipse_at_center,rgba(124,106,247,.7)_0%,transparent_72%)] before:transition-[transform,opacity] before:duration-300 hover:before:opacity-100 hover:before:scale-[2] focus-visible:before:opacity-100 focus-visible:before:scale-[2] motion-reduce:before:transition-opacity">Explore</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:opacity-0 before:scale-0 before:bg-[radial-gradient(ellipse_at_center,rgba(124,106,247,.7)_0%,transparent_72%)] before:transition-[transform,opacity] before:duration-300 hover:before:opacity-100 hover:before:scale-[2] focus-visible:before:opacity-100 focus-visible:before:scale-[2] motion-reduce:before:transition-opacity">Gallery</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:opacity-0 before:scale-0 before:bg-[radial-gradient(ellipse_at_center,rgba(124,106,247,.7)_0%,transparent_72%)] before:transition-[transform,opacity] before:duration-300 hover:before:opacity-100 hover:before:scale-[2] focus-visible:before:opacity-100 focus-visible:before:scale-[2] motion-reduce:before:transition-opacity">Studio</a>
    <a href="#" class="relative isolate px-3 py-1.5 text-[0.95rem] font-medium text-thv26-ink no-underline transition-colors duration-250 hover:text-white focus-visible:text-white focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv26-acc before:content-[''] before:absolute before:inset-0 before:-z-10 before:opacity-0 before:scale-0 before:bg-[radial-gradient(ellipse_at_center,rgba(124,106,247,.7)_0%,transparent_72%)] before:transition-[transform,opacity] before:duration-300 hover:before:opacity-100 hover:before:scale-[2] focus-visible:before:opacity-100 focus-visible:before:scale-[2] motion-reduce:before:transition-opacity">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv26-dim">Radial Spotlight</span>
  </nav>

  <nav aria-label="Invert blend" class="isolate flex flex-wrap items-center gap-6">
    <a href="#" class="relative px-3 py-1.5 text-[0.95rem] font-medium text-white no-underline rounded mix-blend-difference focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:bg-white before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Explore</a>
    <a href="#" class="relative px-3 py-1.5 text-[0.95rem] font-medium text-white no-underline rounded mix-blend-difference focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:bg-white before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Gallery</a>
    <a href="#" class="relative px-3 py-1.5 text-[0.95rem] font-medium text-white no-underline rounded mix-blend-difference focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:bg-white before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Studio</a>
    <a href="#" class="relative px-3 py-1.5 text-[0.95rem] font-medium text-white no-underline rounded mix-blend-difference focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-white before:content-[''] before:absolute before:inset-0 before:-z-10 before:rounded before:bg-white before:origin-left before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 focus-visible:before:scale-x-100 motion-reduce:before:transition-none">Contact</a>
    <span class="ml-auto text-[0.68rem] tracking-[0.1em] uppercase text-thv26-dim">Invert Blend</span>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv26-bg: #0a0a10;
  --color-thv26-bg: oklch(0.12 0.01 285);
  --color-thv26-ink: #c4c4cc;
  --color-thv26-ink: oklch(0.81 0.01 285);
  --color-thv26-dim: #8a8a96;
  --color-thv26-dim: oklch(0.64 0.01 285);
  --color-thv26-acc: #5b4fcf;
  --color-thv26-acc: oklch(0.5 0.2 285);
  --color-thv26-gold: #e8c840;
  --color-thv26-gold: oklch(0.84 0.15 95);
  --font-thv26-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-26 {
  width: 100%;
  min-height: 100svh;
}

.thv-26 ::selection {
  background: var(--color-thv26-acc);
  color: #fff;
}
```
