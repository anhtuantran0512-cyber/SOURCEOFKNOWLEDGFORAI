---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-scroll-driven-scaling-card-stack/"
title: "Tailwind Scroll-Driven Scaling Card Stack"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "The storytelling hero, written in the markup."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scroll-Driven Scaling Card Stack
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-scroll-driven-scaling-card-stack/

The storytelling hero, written in the markup. Each card is sticky with a stepped offset computed from its own --i, so top-[calc(90px+var(--i)*16px)] replaces four :nth-child rules. The scale-and-darken is an @theme animation — animate-stk01-shrink — driven by the two arbitrary properties Tailwind has no utility for, [animation-timeline:view()] and [animation-range:exit]. The only rules left in a stylesheet are the keyframes themselves.
## HTML
```html
<section class="stk-01 w-full min-h-svh h-svh overflow-y-auto bg-stk01-paper font-stk01-sans px-5 [scroll-behavior:smooth] motion-reduce:[scroll-behavior:auto]" aria-label="Scroll-driven scaling card stack">
  <div class="w-[min(520px,100%)] mx-auto pt-[14vh] pb-[40vh]">
    <p class="sticky top-4 z-10 m-0 text-center font-stk01-mono text-[11px] tracking-[0.16em] uppercase text-stk01-muted mb-[6vh]">Scroll &darr; inside this panel</p>
    <article class="sticky top-[calc(90px+var(--i)*16px)] h-65 mb-15 rounded-[22px] p-[34px] text-white bg-linear-[135deg,var(--color-stk01-a1),var(--color-stk01-a2)] shadow-[0_30px_60px_-34px_rgba(20,24,50,0.7)] animate-stk01-shrink [animation-timeline:view()] [animation-range:exit] motion-reduce:animate-none" style="--i:0">
      <span class="font-stk01-mono text-[13px] font-medium tracking-[0.2em] opacity-70">01</span>
      <h3 class="mt-3.5 mb-2.5 text-3xl font-extrabold tracking-[-0.02em]">Capture</h3>
      <p class="max-w-[34ch] text-base leading-relaxed opacity-90">Every idea starts as a rough note. We pin it before it escapes.</p>
    </article>
    <article class="sticky top-[calc(90px+var(--i)*16px)] h-65 mb-15 rounded-[22px] p-[34px] text-white bg-linear-[135deg,var(--color-stk01-b1),var(--color-stk01-b2)] shadow-[0_30px_60px_-34px_rgba(20,24,50,0.7)] animate-stk01-shrink [animation-timeline:view()] [animation-range:exit] motion-reduce:animate-none" style="--i:1">
      <span class="font-stk01-mono text-[13px] font-medium tracking-[0.2em] opacity-70">02</span>
      <h3 class="mt-3.5 mb-2.5 text-3xl font-extrabold tracking-[-0.02em]">Shape</h3>
      <p class="max-w-[34ch] text-base leading-relaxed opacity-90">Notes compress into a plan &mdash; the earlier one settles quietly behind.</p>
    </article>
    <article class="sticky top-[calc(90px+var(--i)*16px)] h-65 mb-15 rounded-[22px] p-[34px] text-white bg-linear-[135deg,var(--color-stk01-c1),var(--color-stk01-c2)] shadow-[0_30px_60px_-34px_rgba(20,24,50,0.7)] animate-stk01-shrink [animation-timeline:view()] [animation-range:exit] motion-reduce:animate-none" style="--i:2">
      <span class="font-stk01-mono text-[13px] font-medium tracking-[0.2em] opacity-70">03</span>
      <h3 class="mt-3.5 mb-2.5 text-3xl font-extrabold tracking-[-0.02em]">Ship</h3>
      <p class="max-w-[34ch] text-base leading-relaxed opacity-90">The plan surfaces on top, in focus, ready to hand off.</p>
    </article>
    <article class="sticky top-[calc(90px+var(--i)*16px)] h-65 mb-15 rounded-[22px] p-[34px] text-white bg-linear-[135deg,var(--color-stk01-d1),var(--color-stk01-d2)] shadow-[0_30px_60px_-34px_rgba(20,24,50,0.7)] animate-stk01-shrink [animation-timeline:view()] [animation-range:exit] motion-reduce:animate-none" style="--i:3">
      <span class="font-stk01-mono text-[13px] font-medium tracking-[0.2em] opacity-70">04</span>
      <h3 class="mt-3.5 mb-2.5 text-3xl font-extrabold tracking-[-0.02em]">Reflect</h3>
      <p class="max-w-[34ch] text-base leading-relaxed opacity-90">What worked stacks up as depth you can scroll back through.</p>
    </article>
    <div class="pt-[12vh] text-center font-stk01-mono text-sm tracking-[0.14em] uppercase text-stk01-muted">Fin.</div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk01-paper: #eef0f4;
  --color-stk01-paper: oklch(0.945 0.006 265);
  --color-stk01-muted: #8a90a0;
  --color-stk01-muted: oklch(0.64 0.018 265);
  --color-stk01-a1: #6f6bf0;
  --color-stk01-a1: oklch(0.62 0.17 274);
  --color-stk01-a2: #8f5ce8;
  --color-stk01-a2: oklch(0.55 0.16 292);
  --color-stk01-b1: #3ec1d3;
  --color-stk01-b1: oklch(0.66 0.15 200);
  --color-stk01-b2: #4f8ee0;
  --color-stk01-b2: oklch(0.60 0.16 250);
  --color-stk01-c1: #4fd39a;
  --color-stk01-c1: oklch(0.70 0.15 150);
  --color-stk01-c2: #3bb7cf;
  --color-stk01-c2: oklch(0.62 0.15 200);
  --color-stk01-d1: #e9a53f;
  --color-stk01-d1: oklch(0.72 0.16 60);
  --color-stk01-d2: #e0713f;
  --color-stk01-d2: oklch(0.64 0.17 30);
  --font-stk01-sans: 'Archivo', system-ui, sans-serif;
  --font-stk01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-stk01-shrink: stk-01-shrink linear both;
}
/* Keyframes are a rule, not a value: there is no utility form for them, and the
   @theme --animate-* entry above only names this block. */

@keyframes stk-01-shrink {
  to {
    transform: scale(0.9);
    filter: brightness(0.72);
  }
}
```
