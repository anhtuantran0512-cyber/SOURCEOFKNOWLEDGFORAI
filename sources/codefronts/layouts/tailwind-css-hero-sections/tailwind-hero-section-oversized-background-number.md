---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-oversized-background-number/"
title: "Tailwind CSS Hero Section with Oversized Background Number"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A vintage wine-label poster — a colossal 1924 drawn as a fading gold-to-burgundy outline behind italic serif copy, with a ruled tasting strip and a ghost CTA."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Hero Section with Oversized Background Number
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-oversized-background-number/

A vintage wine-label poster — a colossal 1924 drawn as a fading gold-to-burgundy outline behind italic serif copy, with a ruled tasting strip and a ghost CTA. Cream paper, gold-leaf accents, a century of quiet.
## HTML
```html
<section class="ths-13 relative isolate grid w-full min-h-svh place-items-center overflow-hidden bg-ths13-bg bg-[radial-gradient(70%_60%_at_50%_45%,var(--color-ths13-glow),transparent_75%)] px-5 py-16 font-ths13-serif text-ths13-ink sm:px-14" aria-label="Hero with oversized background number">
  <div aria-hidden="true" class="pointer-events-none absolute top-1/2 left-1/2 -z-10 -translate-1/2 bg-linear-to-b from-ths13-wine/15 to-transparent to-80% bg-clip-text text-[clamp(220px,40vw,520px)] leading-none font-black tracking-[-0.03em] text-transparent select-none [-webkit-text-stroke:1.5px_rgb(156_122_42/0.45)]">1924</div>
  <div class="max-w-[38rem] text-center">
    <span class="font-ths13-body text-lg tracking-[0.08em] text-ths13-gold italic">— Estate · Vinifera ·</span>
    <h1 class="mt-4 text-[clamp(40px,6.4vw,70px)] leading-[1.03] font-semibold text-balance">A century of <em class="text-ths13-wine">quiet wines.</em></h1>
    <p class="mx-auto mt-5 max-w-[28rem] font-ths13-body text-xl/relaxed text-ths13-mut italic">Six grapes. Four hectares. One family that still skips the marketing and lets the vintage speak.</p>
    <a href="#cellar" class="mt-8 inline-flex min-h-12 items-center border-[1.5px] border-ths13-wine px-8 font-ths13-mono text-xs font-bold tracking-[0.16em] text-ths13-wine uppercase transition hover:bg-ths13-wine hover:text-ths13-bg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths13-wine motion-reduce:transition-none">Visit the cellar</a>
    <dl class="mx-auto mt-10 grid max-w-md grid-cols-3 divide-x divide-ths13-gold/50 border-y border-ths13-gold/50 py-4 font-ths13-mono text-[11px] tracking-[0.12em] text-ths13-mut uppercase">
      <div><dt>Founded</dt><dd class="mt-1 font-ths13-serif text-lg tracking-normal text-ths13-ink normal-case">1924</dd></div>
      <div><dt>Region</dt><dd class="mt-1 font-ths13-serif text-lg tracking-normal text-ths13-ink normal-case">Douro</dd></div>
      <div><dt>Grapes</dt><dd class="mt-1 font-ths13-serif text-lg tracking-normal text-ths13-ink normal-case">Six</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths13-bg: #f5ebd4;
  --color-ths13-bg: oklch(0.942 0.032 87.3);
  --color-ths13-glow: #fbf5e6;
  --color-ths13-glow: oklch(0.971 0.021 88.7);
  --color-ths13-ink: #2a0a18;
  --color-ths13-ink: oklch(0.205 0.056 356);
  --color-ths13-mut: #5a3848;
  --color-ths13-mut: oklch(0.387 0.054 350.2);
  --color-ths13-wine: #6b1230;
  --color-ths13-wine: oklch(0.351 0.123 6.7);
  --color-ths13-gold: #9c7a2a;
  --color-ths13-gold: oklch(0.598 0.105 85.1);
  --font-ths13-serif: 'Playfair Display', Georgia, serif;
  --font-ths13-body: 'Cormorant Garamond', Georgia, serif;
  --font-ths13-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-13 {
  width: 100%;
  min-height: 100svh;
}
```
