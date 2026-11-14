---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-flip-cards/tailwind-auto-height-flip-card-grid-stacking-cross-fade/"
title: "Tailwind Auto-Height Flip Card with CSS Grid Stacking & Cross-Fade"
section: "components"
category: "tailwind-css-flip-cards"
category_name: "Tailwind CSS Flip Cards"
description: "The CMS-safe variant: no pixel heights anywhere."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Auto-Height Flip Card with CSS Grid Stacking & Cross-Fade
Source: https://codefronts.com/components/tailwind-css-flip-cards/tailwind-auto-height-flip-card-grid-stacking-cross-fade/

The CMS-safe variant: no pixel heights anywhere. Both faces live in the same grid cell via col-start-1 row-start-1, so the taller one sets the card's height and content of any length fits. The trade is real &mdash; this is a cross-fade with a rotation flourish, not a true 3D turn &mdash; and the port fixes the technique's accessibility hole by toggling aria-hidden on the face that is not showing.
## HTML
```html
<section class="tfc-17 w-full min-h-svh grid place-items-center content-center gap-6 bg-tfc17-bg font-tfc17-sans px-5 py-10 text-tfc17-ink">
  <div class="text-center">
    <h2 class="text-base font-bold text-white">Auto-height flip cards</h2>
    <p class="mt-1 text-[11px] text-tfc17-muted">No fixed heights &mdash; each card grows to its tallest face</p>
    <code class="mt-2 inline-block rounded border border-tfc17-violet/25 bg-tfc17-violet/15 px-2 py-0.5 font-tfc17-mono text-[11px] text-tfc17-violet">grid + col-start-1 row-start-1</code>
  </div>

  <div class="flex flex-wrap justify-center gap-5">

    <div class="group relative grid w-[280px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc17-violet has-[:focus-visible]:outline-offset-4">
      <input id="tfc-17-a" type="checkbox" class="peer sr-only">
      <label for="tfc-17-a" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show the extended detail for card A</span></label>
      <div class="col-start-1 row-start-1 rounded-2xl border border-tfc17-violet/20 bg-linear-145 from-tfc17-a1 to-tfc17-a2 p-6 transition-[opacity,transform] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:opacity-0 group-hover:[transform:rotateY(90deg)] group-has-checked:opacity-0 group-has-checked:[transform:rotateY(90deg)] group-has-[:focus-visible]:opacity-0 group-has-[:focus-visible]:[transform:rotateY(90deg)] motion-reduce:transition-none">
        <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc17-violet">Dynamic card A</p>
        <h3 class="mb-2 text-lg font-extrabold text-white">Short front</h3>
        <p class="text-[13px] leading-[1.6] text-tfc17-muted">This front face has minimal content. The back has much more, and the card simply grows.</p>
        <p class="mt-3.5 text-[10px] tracking-[0.08em] text-tfc17-dim">Hover, tap or press Space to expand &rarr;</p>
      </div>
      <div aria-hidden="true" class="col-start-1 row-start-1 rounded-2xl border border-tfc17-sky/20 bg-linear-145 from-tfc17-b1 to-tfc17-b2 p-6 opacity-0 [transform:rotateY(-90deg)] transition-[opacity,transform] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:opacity-100 group-hover:[transform:rotateY(0deg)] group-has-checked:opacity-100 group-has-checked:[transform:rotateY(0deg)] group-has-[:focus-visible]:opacity-100 group-has-[:focus-visible]:[transform:rotateY(0deg)] motion-reduce:transition-none">
        <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc17-sky">Full detail &middot; back</p>
        <h3 class="mb-2.5 text-base font-extrabold text-white">Extended back content</h3>
        <p class="text-[13px] leading-[1.7] text-tfc17-ink/70">The grid technique means this face can hold as much content as it needs and the card height adapts &mdash; no hardcoded pixels anywhere.</p>
        <ul class="mt-2.5 flex flex-col gap-1.5 text-xs text-tfc17-ink/65">
          <li class="flex items-start gap-2 before:mt-1.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc17-sky">Both faces share one grid cell</li>
          <li class="flex items-start gap-2 before:mt-1.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc17-sky">Opacity plus rotateY sells the turn</li>
          <li class="flex items-start gap-2 before:mt-1.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc17-sky">The taller face sets the height</li>
          <li class="flex items-start gap-2 before:mt-1.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc17-sky">Zero JavaScript</li>
        </ul>
      </div>
    </div>

    <div class="group relative grid w-[280px] rounded-2xl has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tfc17-pink has-[:focus-visible]:outline-offset-4">
      <input id="tfc-17-b" type="checkbox" class="peer sr-only">
      <label for="tfc-17-b" class="absolute inset-0 z-20 cursor-pointer rounded-2xl"><span class="sr-only">Show the summary for card B</span></label>
      <div class="col-start-1 row-start-1 rounded-2xl border border-tfc17-pink/20 bg-linear-145 from-tfc17-c1 to-tfc17-c2 p-6 transition-[opacity,transform] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:opacity-0 group-hover:[transform:rotateY(90deg)] group-has-checked:opacity-0 group-has-checked:[transform:rotateY(90deg)] group-has-[:focus-visible]:opacity-0 group-has-[:focus-visible]:[transform:rotateY(90deg)] motion-reduce:transition-none">
        <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc17-pink">Dynamic card B</p>
        <h3 class="mb-2 text-lg font-extrabold text-white">Longer front content</h3>
        <p class="text-[13px] leading-[1.6] text-tfc17-muted">This card carries far more on the front &mdash; a paragraph, a list, and a closing note &mdash; and still no height is declared anywhere.</p>
        <ul class="mt-3 flex flex-col gap-1.5 text-xs text-tfc17-ink/65">
          <li class="flex items-start gap-2 before:mt-1.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc17-pink">Point one with some detail</li>
          <li class="flex items-start gap-2 before:mt-1.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc17-pink">Point two with some detail</li>
          <li class="flex items-start gap-2 before:mt-1.5 before:size-1.5 before:shrink-0 before:rounded-full before:bg-tfc17-pink">Point three with some detail</li>
        </ul>
        <p class="mt-3.5 text-[10px] tracking-[0.08em] text-tfc17-dim">Hover, tap or press Space for the summary &rarr;</p>
      </div>
      <div aria-hidden="true" class="col-start-1 row-start-1 rounded-2xl border border-tfc17-green/20 bg-linear-145 from-tfc17-d1 to-tfc17-d2 p-6 opacity-0 [transform:rotateY(-90deg)] transition-[opacity,transform] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover:opacity-100 group-hover:[transform:rotateY(0deg)] group-has-checked:opacity-100 group-has-checked:[transform:rotateY(0deg)] group-has-[:focus-visible]:opacity-100 group-has-[:focus-visible]:[transform:rotateY(0deg)] motion-reduce:transition-none">
        <p class="mb-2.5 text-[9px] font-bold uppercase tracking-[0.15em] text-tfc17-green">TL;DR &middot; back</p>
        <h3 class="mb-2.5 text-base font-extrabold text-white">Short summary</h3>
        <p class="text-[13px] leading-[1.7] text-tfc17-ink/70">Each face owns its natural height. No JS, no fixed pixels, no clipped content.</p>
      </div>
    </div>

  </div>

  <p class="max-w-[580px] rounded-xl border border-tfc17-violet/15 bg-tfc17-violet/6 px-5 py-4 text-center text-xs leading-[1.7] text-tfc17-muted text-pretty">Both faces sit on <code class="rounded bg-tfc17-violet/12 px-1 font-tfc17-mono text-tfc17-violet">col-start-1 row-start-1</code>, so they overlap in one grid cell and the tallest one sets the card height. Opacity fades while <code class="rounded bg-tfc17-violet/12 px-1 font-tfc17-mono text-tfc17-violet">rotateY(&plusmn;90deg)</code> adds depth &mdash; an auto-height flip with no JavaScript.</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfc17-bg: #08060e;
  --color-tfc17-bg: oklch(0.13 0.02 295);
  --color-tfc17-a1: #130e28;
  --color-tfc17-a1: oklch(0.19 0.05 295);
  --color-tfc17-a2: #0a0718;
  --color-tfc17-a2: oklch(0.14 0.035 295);
  --color-tfc17-b1: #0e1a28;
  --color-tfc17-b1: oklch(0.2 0.04 245);
  --color-tfc17-b2: #080f18;
  --color-tfc17-b2: oklch(0.15 0.025 245);
  --color-tfc17-c1: #1a0e18;
  --color-tfc17-c1: oklch(0.19 0.04 330);
  --color-tfc17-c2: #0f0810;
  --color-tfc17-c2: oklch(0.14 0.03 330);
  --color-tfc17-d1: #0a1a0e;
  --color-tfc17-d1: oklch(0.19 0.045 150);
  --color-tfc17-d2: #060e08;
  --color-tfc17-d2: oklch(0.13 0.025 150);
  --color-tfc17-violet: #8b5cf6;
  --color-tfc17-violet: oklch(0.63 0.2 295);
  --color-tfc17-sky: #38bdf8;
  --color-tfc17-sky: oklch(0.76 0.13 230);
  --color-tfc17-pink: #f472b6;
  --color-tfc17-pink: oklch(0.73 0.17 350);
  --color-tfc17-green: #4ade80;
  --color-tfc17-green: oklch(0.8 0.17 152);
  --color-tfc17-ink: #faf5ff;
  --color-tfc17-ink: oklch(0.98 0.015 300);
  --color-tfc17-muted: #b3a8c2;
  --color-tfc17-muted: oklch(0.76 0.035 300);
  --color-tfc17-dim: #87809a;
  --color-tfc17-dim: oklch(0.62 0.03 300);
  --font-tfc17-sans: 'Sora', system-ui, sans-serif;
  --font-tfc17-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tfc-17 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfc-17 * {
    transition-duration: 1ms !important;
  }
}
```
