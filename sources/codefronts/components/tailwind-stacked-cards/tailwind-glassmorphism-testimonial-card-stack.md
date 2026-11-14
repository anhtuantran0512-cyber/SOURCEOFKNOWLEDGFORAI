---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-glassmorphism-testimonial-card-stack/"
title: "Tailwind Glassmorphism Testimonial Card Stack"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A frosted pile over a slowly drifting gradient."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Testimonial Card Stack
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-glassmorphism-testimonial-card-stack/

A frosted pile over a slowly drifting gradient. backdrop-blur-[16px] backdrop-saturate-150 is one of the few places Tailwind's utility is genuinely nicer than the property &mdash; the -webkit- prefix ships automatically. The resting scatter rides each card as --x/--y/--r, and the spread is a group-hover: / group-focus-within: pair of arbitrary transforms, so the whole choreography sits on the three cards instead of in six selectors.
## HTML
```html
<section class="stk-03 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk03-sans bg-linear-[125deg,var(--color-stk03-g1),var(--color-stk03-g2),var(--color-stk03-g3)] bg-[size:220%_220%] animate-stk03-flow motion-reduce:animate-none" aria-label="Glassmorphic testimonial stack">
  <div class="group relative w-[min(360px,100%)] h-75">
    <figure class="absolute inset-0 z-3 flex flex-col justify-between p-[26px_24px] rounded-[22px] bg-white/16 backdrop-blur-[16px] backdrop-saturate-150 ring-1 ring-inset ring-white/40 shadow-[0_20px_45px_-22px_rgba(20,10,50,0.5)] text-white [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-[transform,box-shadow] duration-500 ease-stk03 group-hover:[transform:translate(0,-14px)_rotate(0deg)] group-focus-within:[transform:translate(0,-14px)_rotate(0deg)] group-hover:shadow-[0_34px_60px_-26px_rgba(20,10,50,0.7)] motion-reduce:duration-200" style="--x:0px;--y:0px;--r:0deg">
      <blockquote class="m-0 text-[17px] font-semibold leading-snug [text-shadow:0_1px_12px_rgba(30,10,60,0.35)]">&ldquo;This shipped our redesign a full sprint early. The polish is unreal.&rdquo;</blockquote>
      <figcaption class="flex items-center gap-3 text-[13px]">
        <span class="grid place-items-center size-9.5 shrink-0 rounded-full bg-stk03-av1 text-[13px] font-bold text-white ring-1 ring-inset ring-white/50">MK</span>
        <span><b class="block font-bold">Maya K.</b><a class="text-white/85 underline decoration-white/40 decoration-1 underline-offset-2 text-xs hover:text-white hover:decoration-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 rounded-xs" href="#">Head of Design, Northwind</a></span>
      </figcaption>
    </figure>
    <figure class="absolute inset-0 z-2 flex flex-col justify-between p-[26px_24px] rounded-[22px] bg-white/16 backdrop-blur-[16px] backdrop-saturate-150 ring-1 ring-inset ring-white/40 shadow-[0_20px_45px_-22px_rgba(20,10,50,0.5)] text-white [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-transform duration-500 ease-stk03 group-hover:[transform:translate(46px,30px)_rotate(7deg)] group-focus-within:[transform:translate(46px,30px)_rotate(7deg)] motion-reduce:duration-200" style="--x:22px;--y:14px;--r:4deg">
      <blockquote class="m-0 text-[17px] font-semibold leading-snug [text-shadow:0_1px_12px_rgba(30,10,60,0.35)]">&ldquo;Dependency-free and gorgeous. Our Lighthouse score didn&rsquo;t budge.&rdquo;</blockquote>
      <figcaption class="flex items-center gap-3 text-[13px]">
        <span class="grid place-items-center size-9.5 shrink-0 rounded-full bg-stk03-av2 text-[13px] font-bold text-white ring-1 ring-inset ring-white/50">JL</span>
        <span><b class="block font-bold">Jon L.</b><a class="text-white/85 underline decoration-white/40 decoration-1 underline-offset-2 text-xs hover:text-white hover:decoration-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 rounded-xs" href="#">Staff Engineer, Fathom</a></span>
      </figcaption>
    </figure>
    <figure class="absolute inset-0 z-1 flex flex-col justify-between p-[26px_24px] rounded-[22px] bg-white/16 backdrop-blur-[16px] backdrop-saturate-150 ring-1 ring-inset ring-white/40 shadow-[0_20px_45px_-22px_rgba(20,10,50,0.5)] text-white [transform:translate(var(--x),var(--y))_rotate(var(--r))] transition-transform duration-500 ease-stk03 group-hover:[transform:translate(-44px,44px)_rotate(-8deg)] group-focus-within:[transform:translate(-44px,44px)_rotate(-8deg)] motion-reduce:duration-200" style="--x:-20px;--y:26px;--r:-5deg">
      <blockquote class="m-0 text-[17px] font-semibold leading-snug [text-shadow:0_1px_12px_rgba(30,10,60,0.35)]">&ldquo;Clients think we hired a motion studio. It&rsquo;s one stylesheet.&rdquo;</blockquote>
      <figcaption class="flex items-center gap-3 text-[13px]">
        <span class="grid place-items-center size-9.5 shrink-0 rounded-full bg-stk03-av3 text-[13px] font-bold text-white ring-1 ring-inset ring-white/50">RA</span>
        <span><b class="block font-bold">Reese A.</b><a class="text-white/85 underline decoration-white/40 decoration-1 underline-offset-2 text-xs hover:text-white hover:decoration-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 rounded-xs" href="#">Founder, Studio Arc</a></span>
      </figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk03-g1: #a259d9;
  --color-stk03-g1: oklch(0.60 0.20 300);
  --color-stk03-g2: #34a8e0;
  --color-stk03-g2: oklch(0.68 0.19 210);
  --color-stk03-g3: #f0894a;
  --color-stk03-g3: oklch(0.72 0.18 30);
  --color-stk03-av1: #ef7a63;
  --color-stk03-av1: oklch(0.70 0.18 20);
  --color-stk03-av2: #3fa9dc;
  --color-stk03-av2: oklch(0.70 0.16 200);
  --color-stk03-av3: #4cc48a;
  --color-stk03-av3: oklch(0.72 0.16 140);
  --font-stk03-sans: 'Archivo', system-ui, sans-serif;
  --ease-stk03: cubic-bezier(0.2, 0.8, 0.2, 1);
  --animate-stk03-flow: stk-03-flow 16s ease-in-out infinite;
}
/* The gradient drift: keyframes have no utility form. Everything else in this
   demo — including the -webkit-backdrop-filter twin — the compiler emits. */

@keyframes stk-03-flow {
  0%,
    100% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }
}
```
