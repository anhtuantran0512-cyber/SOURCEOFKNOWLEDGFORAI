---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-blockquotes/responsive-tailwind-center-aligned-quote-banner/"
title: "Responsive Tailwind Center-Aligned Quote Banner"
section: "snippets"
category: "tailwind-css-blockquotes"
category_name: "Tailwind CSS Blockquotes"
description: "A full-bleed keynote quote banner: display serif at clamp(40px,3vw+24px,76px), a gradient-clipped closing phrase, and a rule–name–rule attribution line built…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind Center-Aligned Quote Banner
Source: https://codefronts.com/snippets/tailwind-css-blockquotes/responsive-tailwind-center-aligned-quote-banner/

A full-bleed keynote quote banner: display serif at clamp(40px,3vw+24px,76px), a gradient-clipped closing phrase, and a rule–name–rule attribution line built from a three-column grid. On phones the rules drop away with max-sm: and the attribution stacks, so the name never wraps into a two-line orphan between hairlines.
## HTML
```html
<section class="tbq-04 w-full min-h-svh grid place-items-center overflow-hidden bg-tbq04-bg bg-[radial-gradient(60%_45%_at_50%_42%,var(--color-tbq04-glow),transparent_70%)] px-5 py-16 text-center font-tbq04-sans text-tbq04-ink" aria-label="Center aligned quote banner demo">
  <div class="grid w-full justify-items-center gap-10">
    <figure class="grid w-full max-w-[900px] justify-items-center gap-7">
      <p class="inline-flex items-center gap-2.5 text-xs font-bold tracking-[0.28em] uppercase text-tbq04-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-tbq04-acc shadow-[0_0_12px_var(--color-tbq04-acc)]"></span>From the keynote</p>
      <blockquote>
        <p class="max-w-[20ch] font-tbq04-display text-[clamp(40px,3vw+24px,76px)] leading-[1.02] tracking-[-0.015em] text-balance">Make the easy path and the right path <em class="bg-linear-to-r from-tbq04-acc to-tbq04-acc2 box-decoration-clone bg-clip-text text-transparent">the same path.</em></p>
      </blockquote>
      <figcaption class="grid w-full max-w-[560px] grid-cols-[1fr_auto_1fr] items-center gap-4.5 text-sm text-tbq04-mut max-sm:grid-cols-1 max-sm:gap-1">
        <span aria-hidden="true" class="h-px bg-linear-to-r from-transparent to-tbq04-ink/30 max-sm:hidden"></span>
        <span><strong class="font-semibold text-tbq04-ink">Amara Chen</strong><span class="max-sm:hidden"> — </span><span class="max-sm:block">Head of Platform, Fieldday</span></span>
        <span aria-hidden="true" class="h-px bg-linear-to-l from-transparent to-tbq04-ink/30 max-sm:hidden"></span>
      </figcaption>
    </figure>
    <p aria-hidden="true" class="rounded-full border border-tbq04-ink/15 px-3.5 py-2 font-tbq04-mono text-[11.5px] text-tbq04-mut">grid-cols-[1fr_auto_1fr] · bg-clip-text · clamp() display</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbq04-bg: #0e0e18;
  --color-tbq04-bg: oklch(0.17 0.02 285);
  --color-tbq04-glow: #3d21438c;
  --color-tbq04-glow: oklch(0.3 0.07 320 / 0.55);
  --color-tbq04-ink: #f0f1f9;
  --color-tbq04-ink: oklch(0.96 0.01 280);
  --color-tbq04-mut: #b5b5ca;
  --color-tbq04-mut: oklch(0.78 0.03 285);
  --color-tbq04-acc: #ed9ee5;
  --color-tbq04-acc: oklch(0.8 0.13 330);
  --color-tbq04-acc2: #fdb171;
  --color-tbq04-acc2: oklch(0.82 0.12 60);
  --font-tbq04-display: 'Instrument Serif', Georgia, serif;
  --font-tbq04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tbq04-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tbq-04 {
  width: 100%;
  min-height: 100svh;
}
```
