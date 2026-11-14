---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-auto-fit-blog-archive-grid/"
title: "Tailwind Auto-Fit Blog Archive Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "The self-adjusting archive: one arbitrary track list, no media queries, columns appearing and disappearing as the container resizes."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Auto-Fit Blog Archive Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-auto-fit-blog-archive-grid/

The self-adjusting archive: one arbitrary track list, no media queries, columns appearing and disappearing as the container resizes. The port is a straight one-for-one, and it is the demo that best shows where the line falls &mdash; repeat(auto-fit,minmax(280px,1fr)) stays arbitrary, everything else becomes a utility.
## HTML
```html
<section class="tcg-01 w-full min-h-svh bg-tcg01-bg font-tcg01-sans text-tcg01-ink px-6 py-12" aria-label="Auto-fit blog archive grid demo">

  <header class="max-w-[1100px] mx-auto mb-8">
    <span class="text-[.75rem] font-bold tracking-[0.12em] uppercase text-tcg01-accent">Latest Articles</span>
    <h2 class="mt-1.5 text-[clamp(1.5rem,3vw,2.25rem)] font-extrabold tracking-[-0.02em]">The Auto-Fit Archive</h2>
  </header>

  <div class="max-w-[1100px] mx-auto grid [grid-template-columns:repeat(auto-fit,minmax(280px,1fr))] gap-7">

    <article class="group overflow-hidden rounded-[14px] border border-tcg01-line bg-tcg01-card transition-[translate,box-shadow,border-color] duration-250 hover:-translate-y-1 hover:border-transparent hover:shadow-[0_16px_32px_-16px_oklch(0.2_0.04_260/0.18)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="relative aspect-video overflow-hidden">
        <span class="absolute top-3.5 left-3.5 z-2 px-2.5 py-1.25 rounded-full bg-white/92 text-tcg01-ink text-[.7rem] font-bold tracking-[0.04em]">Engineering</span>
        <div class="w-full h-full bg-linear-[135deg,#3b82f6,#1e3a8a] transition-transform duration-500 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <div class="px-5 pt-4.5 pb-5">
        <h3 class="text-[1.05rem] font-bold leading-[1.35] tracking-[-0.01em] [overflow-wrap:break-word]"><a href="#grids" class="no-underline text-tcg01-ink hover:text-tcg01-accent focus-visible:outline-2 focus-visible:outline-tcg01-accent focus-visible:outline-offset-3">Designing Resilient Grid Systems for the Modern Web</a></h3>
        <p class="mt-2 text-[.875rem] leading-[1.5] text-tcg01-muted text-pretty">How auto-fit and minmax remove the need for breakpoint-driven column math.</p>
        <div class="flex gap-2 mt-3.5 text-[.78rem] text-tcg01-muted"><span>Maya Chen</span><span aria-hidden="true">&bull;</span><span>6 min read</span></div>
      </div>
    </article>

    <article class="group overflow-hidden rounded-[14px] border border-tcg01-line bg-tcg01-card transition-[translate,box-shadow,border-color] duration-250 hover:-translate-y-1 hover:border-transparent hover:shadow-[0_16px_32px_-16px_oklch(0.2_0.04_260/0.18)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="relative aspect-video overflow-hidden">
        <span class="absolute top-3.5 left-3.5 z-2 px-2.5 py-1.25 rounded-full bg-white/92 text-tcg01-ink text-[.7rem] font-bold tracking-[0.04em]">Design</span>
        <div class="w-full h-full bg-linear-[135deg,#f472b6,#7c3aed] transition-transform duration-500 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <div class="px-5 pt-4.5 pb-5">
        <h3 class="text-[1.05rem] font-bold leading-[1.35] tracking-[-0.01em] [overflow-wrap:break-word]"><a href="#type" class="no-underline text-tcg01-ink hover:text-tcg01-accent focus-visible:outline-2 focus-visible:outline-tcg01-accent focus-visible:outline-offset-3">Typography Scales That Do Not Break on Mobile</a></h3>
        <p class="mt-2 text-[.875rem] leading-[1.5] text-tcg01-muted text-pretty">A practical look at clamp(), fluid type, and readable line lengths.</p>
        <div class="flex gap-2 mt-3.5 text-[.78rem] text-tcg01-muted"><span>Sam Osei</span><span aria-hidden="true">&bull;</span><span>4 min read</span></div>
      </div>
    </article>

    <article class="group overflow-hidden rounded-[14px] border border-tcg01-line bg-tcg01-card transition-[translate,box-shadow,border-color] duration-250 hover:-translate-y-1 hover:border-transparent hover:shadow-[0_16px_32px_-16px_oklch(0.2_0.04_260/0.18)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="relative aspect-video overflow-hidden">
        <span class="absolute top-3.5 left-3.5 z-2 px-2.5 py-1.25 rounded-full bg-white/92 text-tcg01-ink text-[.7rem] font-bold tracking-[0.04em]">Product</span>
        <div class="w-full h-full bg-linear-[135deg,#34d399,#065f46] transition-transform duration-500 group-hover:scale-106 motion-reduce:transition-none motion-reduce:group-hover:scale-100" aria-hidden="true"></div>
      </div>
      <div class="px-5 pt-4.5 pb-5">
        <h3 class="text-[1.05rem] font-bold leading-[1.35] tracking-[-0.01em] [overflow-wrap:break-word]"><a href="#components" class="no-underline text-tcg01-ink hover:text-tcg01-accent focus-visible:outline-2 focus-visible:outline-tcg01-accent focus-visible:outline-offset-3">Shipping Faster With Component-Driven Layouts</a></h3>
        <p class="mt-2 text-[.875rem] leading-[1.5] text-tcg01-muted text-pretty">Lessons from rebuilding a design system around composable grid primitives.</p>
        <div class="flex gap-2 mt-3.5 text-[.78rem] text-tcg01-muted"><span>Priya Nair</span><span aria-hidden="true">&bull;</span><span>8 min read</span></div>
      </div>
    </article>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg01-bg: #fafafa;
  --color-tcg01-bg: oklch(0.98 0 0);
  --color-tcg01-card: #ffffff;
  --color-tcg01-card: oklch(1 0 0);
  --color-tcg01-ink: #0f172a;
  --color-tcg01-ink: oklch(0.21 0.04 260);
  --color-tcg01-muted: #64748b;
  --color-tcg01-muted: oklch(0.55 0.03 257);
  --color-tcg01-line: #e2e8f0;
  --color-tcg01-line: oklch(0.92 0.01 255);
  --color-tcg01-accent: #2563eb;
  --color-tcg01-accent: oklch(0.52 0.22 262);
  --font-tcg01-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract. */

.tcg-01 {
  width: 100%;
  min-height: 100svh;
}

.tcg-01 ::selection {
  background: #2563eb;
  color: #fff;
}
```
