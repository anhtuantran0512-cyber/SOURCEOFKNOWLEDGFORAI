---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/pure-tailwind-css-illustrated-empty-state/"
title: "Pure Tailwind CSS Illustrated Empty State (No Images)"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A recipe app's empty cookbook, illustrated entirely in utilities: a terracotta pot with handles, a tilted lid, a shadowed plate and three wisps of steam…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure Tailwind CSS Illustrated Empty State (No Images)
Source: https://codefronts.com/snippets/tailwind-css-empty-states/pure-tailwind-css-illustrated-empty-state/

A recipe app's empty cookbook, illustrated entirely in utilities: a terracotta pot with handles, a tilted lid, a shadowed plate and three wisps of steam rising on a loop — no SVG, no images, no JavaScript. Every shape is a positioned <span> with percentage geometry, so the drawing scales with its container.
## HTML
```html
<div class="tes-18 w-full min-h-svh bg-tes18-paper font-tes18-sans text-tes18-ink antialiased">
  <header class="flex flex-wrap items-center gap-x-8 gap-y-2 border-b border-tes18-line px-[clamp(1rem,4vw,3rem)] py-4">
    <span class="font-tes18-serif text-[1.6rem] leading-none">Copperpot</span>
    <nav aria-label="Cookbook" class="order-3 flex w-full gap-5 overflow-x-auto text-sm text-tes18-mut sm:order-none sm:w-auto sm:flex-1">
      <a href="#" class="border-b-2 border-transparent py-2 hover:border-tes18-clay hover:text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Discover</a><a href="#" class="border-b-2 border-transparent py-2 hover:border-tes18-clay hover:text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Weeknight</a><a href="#" class="border-b-2 border-transparent py-2 hover:border-tes18-clay hover:text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Baking</a><a href="#" aria-current="page" class="border-b-2 border-tes18-ink py-2 text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Saved</a>
    </nav>
    <span aria-hidden="true" class="ml-auto grid size-9 place-items-center rounded-full bg-tes18-olive text-xs font-semibold text-tes18-card">RS</span>
  </header>
  <main class="mx-auto grid w-full max-w-6xl items-start gap-[clamp(1.25rem,3vw,2.5rem)] px-[clamp(1rem,4vw,3rem)] py-[clamp(1.5rem,4vw,3rem)] md:grid-cols-[13rem_minmax(0,1fr)]">
    <aside class="hidden content-start gap-2 md:grid">
      <p class="font-tes18-serif text-lg italic text-tes18-mut">Collections</p>
      <ul class="grid gap-0.5 text-sm"><li><a href="#" class="block rounded-lg px-2.5 py-2 text-tes18-mut hover:bg-tes18-sunk hover:text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Sunday roasts</a></li><li><a href="#" class="block rounded-lg px-2.5 py-2 text-tes18-mut hover:bg-tes18-sunk hover:text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Twenty minutes</a></li><li><a href="#" class="block rounded-lg px-2.5 py-2 text-tes18-mut hover:bg-tes18-sunk hover:text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Bread and doughs</a></li><li><a href="#" class="block rounded-lg px-2.5 py-2 text-tes18-mut hover:bg-tes18-sunk hover:text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Preserving</a></li></ul>
      <p class="mt-3 font-tes18-serif text-lg italic text-tes18-mut">Shopping</p>
      <ul class="grid gap-0.5 text-sm"><li><a href="#" class="block rounded-lg px-2.5 py-2 text-tes18-mut hover:bg-tes18-sunk hover:text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">This week</a></li><li><a href="#" class="block rounded-lg px-2.5 py-2 text-tes18-mut hover:bg-tes18-sunk hover:text-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Pantry staples</a></li></ul>
    </aside>
    <section class="grid justify-items-center gap-3 rounded-[28px] border border-tes18-line bg-tes18-card bg-[radial-gradient(color-mix(in_oklab,var(--color-tes18-line2)_45%,transparent)_0.8px,transparent_0.8px)] bg-size-[15px_15px] px-[clamp(1.25rem,3vw,2.5rem)] py-[clamp(2rem,5vw,3.5rem)] text-center shadow-[0_40px_70px_-60px_oklch(0.25_0.02_55/0.6)]">
      <div aria-hidden="true" class="relative mb-4 aspect-[1.35] w-[min(17rem,80%)]">
        <span class="absolute right-[4%] bottom-[3%] left-[4%] h-[16%] rounded-[50%] bg-tes18-sunk shadow-[inset_0_-6px_0_var(--color-tes18-line)]"></span>
        <span class="absolute bottom-[56%] left-[37%] h-[22%] w-[3.5%] origin-bottom animate-tes18-steam rounded-full bg-tes18-line2/70 motion-reduce:animate-none"></span>
        <span class="absolute bottom-[58%] left-[48.5%] h-[28%] w-[3.5%] origin-bottom animate-tes18-steam rounded-full bg-tes18-line2/70 [animation-delay:.6s] motion-reduce:animate-none"></span>
        <span class="absolute bottom-[56%] left-[60%] h-[20%] w-[3.5%] origin-bottom animate-tes18-steam rounded-full bg-tes18-line2/70 [animation-delay:1.2s] motion-reduce:animate-none"></span>
        <span class="absolute bottom-[34%] left-[14%] h-[11%] w-[14%] rounded-l-full border-[6px] border-r-0 border-tes18-clay2"></span>
        <span class="absolute right-[14%] bottom-[34%] h-[11%] w-[14%] rounded-r-full border-[6px] border-l-0 border-tes18-clay2"></span>
        <span class="absolute bottom-[12%] left-1/2 h-[42%] w-[58%] -translate-x-1/2 rounded-t-[10px] rounded-b-[45%_55%] bg-tes18-clay shadow-[inset_-14px_-10px_0_var(--color-tes18-clay2)]"></span>
        <span class="absolute bottom-[28%] left-[30%] h-[7%] w-[22%] rounded-full bg-tes18-cream/60"></span>
        <span class="absolute bottom-[51%] left-1/2 h-[7%] w-[64%] -translate-x-1/2 rounded-full bg-tes18-clay2"></span>
        <span class="absolute bottom-[57%] left-[30%] h-[7%] w-[42%] origin-left -rotate-[9deg] rounded-t-full bg-tes18-olive shadow-[inset_0_-4px_0_oklch(0.4_0.05_118)] before:absolute before:-top-[70%] before:left-1/2 before:size-[34%] before:max-h-4 before:max-w-4 before:-translate-x-1/2 before:rounded-full before:bg-tes18-olive"></span>
        <span class="absolute top-[12%] right-[10%] size-2 rounded-full bg-tes18-clay/60"></span>
        <span class="absolute top-[30%] left-[8%] size-1.5 rounded-full bg-tes18-olive/60"></span>
        <span class="absolute top-[6%] left-[24%] size-1 rounded-full bg-tes18-clay/50"></span>
      </div>
      <h1 class="font-tes18-serif text-[clamp(1.9rem,4vw,2.6rem)] leading-tight tracking-tight text-balance">Nothing saved to your cookbook</h1>
      <p class="max-w-[46ch] text-[15px]/7 text-tes18-mut text-pretty">Save a recipe and it lands here with its ingredients scaled to your household, ready for the week’s shopping list.</p>
      <div class="mt-3 flex flex-wrap justify-center gap-2.5">
        <a href="#" class="inline-flex min-h-11 items-center rounded-full bg-tes18-ink px-6 text-sm font-medium text-tes18-card transition hover:bg-tes18-clay focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Browse this week’s picks</a>
        <a href="#" class="inline-flex min-h-11 items-center rounded-full border border-tes18-line2 px-5 text-sm transition hover:border-tes18-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes18-clay">Import from a link</a>
      </div>
    </section>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes18-paper: #f7f2e9;
  --color-tes18-paper: oklch(0.962 0.015 85);
  --color-tes18-card: #fffdf8;
  --color-tes18-card: oklch(0.991 0.007 85);
  --color-tes18-sunk: #efe7d9;
  --color-tes18-sunk: oklch(0.925 0.022 82);
  --color-tes18-line: #e3d9c7;
  --color-tes18-line: oklch(0.885 0.026 82);
  --color-tes18-line2: #cec1a9;
  --color-tes18-line2: oklch(0.805 0.036 80);
  --color-tes18-ink: #221d16;
  --color-tes18-ink: oklch(0.225 0.018 55);
  --color-tes18-mut: #635a4c;
  --color-tes18-mut: oklch(0.46 0.022 62);
  --color-tes18-clay: #b8673a;
  --color-tes18-clay: oklch(0.6 0.12 47);
  --color-tes18-clay2: #9a4f27;
  --color-tes18-clay2: oklch(0.52 0.12 45);
  --color-tes18-olive: #6a7748;
  --color-tes18-olive: oklch(0.54 0.065 118);
  --color-tes18-cream: #f3e4c9;
  --color-tes18-cream: oklch(0.915 0.045 85);
  --font-tes18-sans: 'Geist', system-ui, sans-serif;
  --font-tes18-serif: 'Instrument Serif', Georgia, serif;
  --animate-tes18-steam: tes18-steam 2.4s ease-in-out infinite;

  @keyframes tes18-steam {
    0% {
      opacity: 0;
      translate: 0 10%;
      scale: 1 0.6;
    }

    40% {
      opacity: 1;
    }

    100% {
      opacity: 0;
      translate: 0 -30%;
      scale: 1 1.1;
    }
  }
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-18 {
  width: 100%;
  min-height: 100svh;
}

.tes-18 [hidden] {
  display: none !important;
}
```
