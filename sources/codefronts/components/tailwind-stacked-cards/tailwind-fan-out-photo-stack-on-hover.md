---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-fan-out-photo-stack-on-hover/"
title: "Tailwind Fan Out Photo Stack on Hover"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A tidy pile that fans into an arc, where the arithmetic replaces the rule."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Fan Out Photo Stack on Hover
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-fan-out-photo-stack-on-hover/

A tidy pile that fans into an arc, where the arithmetic replaces the rule. Every photo carries --n &mdash; its signed position from the centre &mdash; and one shared class list turns that into both the rotation and the arc lift: group-hover:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))]. Five identical class lists, five different destinations, no :nth-child map anywhere.
## HTML
```html
<section class="stk-05 w-full min-h-svh flex flex-col items-center justify-center gap-[34px] px-5 py-15 font-stk05-sans bg-stk05-paper" aria-label="Fan-out photo stack">
  <div class="group relative w-55 h-75">
    <a class="absolute left-1/2 top-0 -ml-[90px] w-45 rounded-[14px] overflow-hidden bg-white p-2 pb-[22px] shadow-[0_16px_34px_-20px_rgba(60,40,20,0.6)] [transform-origin:50%_130%] transition-transform duration-500 ease-stk05 delay-0 group-hover:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] group-focus-within:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] hover:z-5 hover:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! focus-visible:z-5 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk05-focus),0_20px_40px_-18px_rgba(60,40,20,0.7)] focus-visible:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! motion-reduce:duration-200 motion-reduce:group-hover:[transform:translateX(calc(var(--n)*48px))] motion-reduce:group-focus-within:[transform:translateX(calc(var(--n)*48px))]" href="#" style="--n:-2">
      <img class="block w-full aspect-[3/4] object-cover rounded-lg" src="https://picsum.photos/seed/tw-fan-1/300/380" width="300" height="380" alt="Coastline seen from a cliff path">
    </a>
    <a class="absolute left-1/2 top-0 -ml-[90px] w-45 rounded-[14px] overflow-hidden bg-white p-2 pb-[22px] shadow-[0_16px_34px_-20px_rgba(60,40,20,0.6)] [transform-origin:50%_130%] transition-transform duration-500 ease-stk05 delay-[40ms] group-hover:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] group-focus-within:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] hover:z-5 hover:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! focus-visible:z-5 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk05-focus),0_20px_40px_-18px_rgba(60,40,20,0.7)] focus-visible:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! motion-reduce:duration-200 motion-reduce:group-hover:[transform:translateX(calc(var(--n)*48px))] motion-reduce:group-focus-within:[transform:translateX(calc(var(--n)*48px))]" href="#" style="--n:-1">
      <img class="block w-full aspect-[3/4] object-cover rounded-lg" src="https://picsum.photos/seed/tw-fan-2/300/380" width="300" height="380" alt="Narrow street in an old town">
    </a>
    <a class="absolute left-1/2 top-0 -ml-[90px] w-45 rounded-[14px] overflow-hidden bg-white p-2 pb-[22px] shadow-[0_16px_34px_-20px_rgba(60,40,20,0.6)] [transform-origin:50%_130%] transition-transform duration-500 ease-stk05 delay-[80ms] group-hover:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] group-focus-within:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] hover:z-5 hover:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! focus-visible:z-5 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk05-focus),0_20px_40px_-18px_rgba(60,40,20,0.7)] focus-visible:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! motion-reduce:duration-200 motion-reduce:group-hover:[transform:translateX(calc(var(--n)*48px))] motion-reduce:group-focus-within:[transform:translateX(calc(var(--n)*48px))]" href="#" style="--n:0">
      <img class="block w-full aspect-[3/4] object-cover rounded-lg" src="https://picsum.photos/seed/tw-fan-3/300/380" width="300" height="380" alt="Stone hut on a mountain ridge">
    </a>
    <a class="absolute left-1/2 top-0 -ml-[90px] w-45 rounded-[14px] overflow-hidden bg-white p-2 pb-[22px] shadow-[0_16px_34px_-20px_rgba(60,40,20,0.6)] [transform-origin:50%_130%] transition-transform duration-500 ease-stk05 delay-[40ms] group-hover:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] group-focus-within:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] hover:z-5 hover:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! focus-visible:z-5 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk05-focus),0_20px_40px_-18px_rgba(60,40,20,0.7)] focus-visible:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! motion-reduce:duration-200 motion-reduce:group-hover:[transform:translateX(calc(var(--n)*48px))] motion-reduce:group-focus-within:[transform:translateX(calc(var(--n)*48px))]" href="#" style="--n:1">
      <img class="block w-full aspect-[3/4] object-cover rounded-lg" src="https://picsum.photos/seed/tw-fan-4/300/380" width="300" height="380" alt="Harbour at dusk with moored boats">
    </a>
    <a class="absolute left-1/2 top-0 -ml-[90px] w-45 rounded-[14px] overflow-hidden bg-white p-2 pb-[22px] shadow-[0_16px_34px_-20px_rgba(60,40,20,0.6)] [transform-origin:50%_130%] transition-transform duration-500 ease-stk05 delay-0 group-hover:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] group-focus-within:[transform:rotate(calc(var(--n)*15deg))_translateY(calc(var(--n)*var(--n)*-2px))] hover:z-5 hover:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! focus-visible:z-5 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk05-focus),0_20px_40px_-18px_rgba(60,40,20,0.7)] focus-visible:[transform:rotate(calc(var(--n)*15deg))_translateY(-24px)]! motion-reduce:duration-200 motion-reduce:group-hover:[transform:translateX(calc(var(--n)*48px))] motion-reduce:group-focus-within:[transform:translateX(calc(var(--n)*48px))]" href="#" style="--n:2">
      <img class="block w-full aspect-[3/4] object-cover rounded-lg" src="https://picsum.photos/seed/tw-fan-5/300/380" width="300" height="380" alt="Rippled desert dunes at midday">
    </a>
  </div>
  <p class="m-0 font-stk05-mono text-[11px] tracking-[0.14em] uppercase text-stk05-muted">Hover to fan &middot; Tab to spread</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk05-paper: #e9e4db;
  --color-stk05-paper: oklch(0.91 0.012 80);
  --color-stk05-muted: #9a8f80;
  --color-stk05-muted: oklch(0.65 0.02 80);
  --color-stk05-focus: #6a7bf0;
  --color-stk05-focus: oklch(0.60 0.17 265);
  --font-stk05-sans: 'Archivo', system-ui, sans-serif;
  --font-stk05-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk05: cubic-bezier(0.2, 0.85, 0.2, 1);
}
```
