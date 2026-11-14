---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-asymmetric-typography-hero-section/"
title: "Asymmetric Typography Hero Section in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "Construction-site asymmetric typography — three headline lines stepping across a broken grid, a hi-vis outlined word, a giant italic ampersand and an…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Asymmetric Typography Hero Section in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-asymmetric-typography-hero-section/

Construction-site asymmetric typography — three headline lines stepping across a broken grid, a hi-vis outlined word, a giant italic ampersand and an animated caution-tape stripe. Safety yellow on concrete grey, hard black rules. Collapses to a clean stack on phones.
## HTML
```html
<section class="ths-12 grid w-full min-h-svh overflow-hidden bg-ths12-bg bg-[radial-gradient(rgb(0_0_0/0.06)_1px,transparent_1px)] bg-size-[14px_14px] p-5 font-ths12-sans text-ths12-ink sm:p-10" aria-label="Asymmetric typography hero">
  <div class="grid w-full content-between gap-6 md:grid-cols-[1fr_1fr_0.6fr]">
    <div class="flex items-center justify-between md:col-span-3">
      <span class="bg-ths12-hivis px-2.5 py-1 font-ths12-mono text-[11px] font-bold tracking-[0.2em]">/ ZONE 4</span>
      <span class="font-ths12-mono text-[11px] font-bold tracking-[0.2em]">BUILD #2.418 · GREEN</span>
    </div>
    <h1 class="font-ths12-sans leading-[0.85] font-black tracking-[-0.04em] uppercase [font-stretch:115%] md:col-span-3">
      <span class="block text-[clamp(56px,12vw,150px)]">Under</span>
      <span class="block text-[clamp(34px,7vw,92px)] text-ths12-hivis [font-stretch:100%] [-webkit-text-stroke:2px_var(--color-ths12-ink)] md:ml-[clamp(24px,8vw,150px)]">construction.</span>
      <span class="block text-[clamp(34px,7vw,92px)] [font-stretch:100%] md:ml-[clamp(48px,18vw,320px)]">Always.</span>
    </h1>
    <p class="max-w-sm self-end border-l-4 border-ths12-hivis pl-4 text-[15px] leading-relaxed text-ths12-body md:col-span-2">Software you ship is software that's still being built. We make CI fast enough to do it on the dev's terms — not the build's.</p>
    <span aria-hidden="true" class="hidden self-end justify-self-end font-ths12-serif text-[clamp(80px,14vw,170px)] leading-none font-extrabold italic md:block">&amp;</span>
    <a href="#start" class="inline-flex min-h-12 items-center justify-self-start bg-ths12-ink px-7 font-ths12-mono text-sm font-extrabold tracking-[0.16em] text-ths12-hivis transition hover:bg-ths12-hivis hover:text-ths12-ink hover:shadow-[0_0_0_2px_var(--color-ths12-ink)] focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-ths12-ink motion-reduce:transition-none">DEPLOY →</a>
    <span aria-hidden="true" class="h-4 animate-ths12-tape self-center bg-[repeating-linear-gradient(45deg,var(--color-ths12-ink)_0_12px,var(--color-ths12-hivis)_12px_24px)] bg-size-[34px_34px] motion-reduce:animate-none md:col-span-2"></span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths12-bg: #c8c4be;
  --color-ths12-bg: oklch(0.822 0.009 78.3);
  --color-ths12-ink: #0a0a0a;
  --color-ths12-ink: oklch(0.145 0 0);
  --color-ths12-body: #1f1f1f;
  --color-ths12-body: oklch(0.239 0 0);
  --color-ths12-hivis: #f5d028;
  --color-ths12-hivis: oklch(0.864 0.169 95.2);
  --font-ths12-sans: 'Archivo', system-ui, sans-serif;
  --font-ths12-serif: 'Playfair Display', Georgia, serif;
  --font-ths12-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths12-tape: ths12-tape 1.2s linear infinite;

  @keyframes ths12-tape {
    to {
      background-position: 34px 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-12 {
  width: 100%;
  min-height: 100svh;
}
```
