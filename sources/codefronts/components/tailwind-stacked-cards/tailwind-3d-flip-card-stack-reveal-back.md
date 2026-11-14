---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-3d-flip-card-stack-reveal-back/"
title: "Tailwind 3D Flip Card Stack Reveal Back"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A pricing card that turns 180&deg; to show what is behind it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Flip Card Stack Reveal Back
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-3d-flip-card-stack-reveal-back/

A pricing card that turns 180&deg; to show what is behind it. This is the port where v4's own 3D utilities finally cover the ground: transform-3d, backface-hidden, rotate-y-180 and perspective-distant are all real classes, so the flip needs no arbitrary properties at all. The reduced-motion path is the substantive part &mdash; it replaces the turn with a cross-fade rather than a slower turn.
## HTML
```html
<section class="stk-23 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk23-sans bg-stk23-bg" aria-label="3D flip card stack">
  <div class="relative w-[min(280px,90vw)] h-60 [perspective:1200px]">
    <div class="absolute inset-0 rounded-[20px] border border-stk23-line bg-stk23-under shadow-[0_18px_34px_-22px_rgba(0,0,0,0.8)] [transform:translate(calc(var(--i)*10px),calc(var(--i)*10px))_scale(calc(1-var(--i)*0.04))]" style="--i:2" aria-hidden="true"></div>
    <div class="absolute inset-0 rounded-[20px] border border-stk23-line bg-stk23-under shadow-[0_18px_34px_-22px_rgba(0,0,0,0.8)] [transform:translate(calc(var(--i)*10px),calc(var(--i)*10px))_scale(calc(1-var(--i)*0.04))]" style="--i:1" aria-hidden="true"></div>
    <div class="group absolute inset-0 z-5 rounded-[20px] outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk23-accent)]" tabindex="0">
      <div class="relative size-full transform-3d transition-transform duration-600 ease-stk23 group-hover:rotate-y-180 group-focus-visible:rotate-y-180 motion-reduce:transition-none motion-reduce:rotate-y-0!">
        <div class="absolute inset-0 flex flex-col justify-center rounded-[20px] p-6.5 text-white backface-hidden bg-linear-[155deg,var(--color-stk23-f1),var(--color-stk23-f2)] shadow-[0_24px_48px_-26px_rgba(0,0,0,0.85)] transition-opacity duration-300 motion-reduce:group-hover:opacity-0 motion-reduce:group-focus-visible:opacity-0">
          <p class="m-0 font-stk23-mono text-xs font-medium tracking-[0.16em] uppercase text-stk23-accent">Pro plan</p>
          <h3 class="my-1.5 text-[44px] font-black leading-none tracking-[-0.03em]">$24<small class="text-base font-semibold text-stk23-muted">/mo</small></h3>
          <p class="m-0 text-sm text-stk23-body">Hover or focus to see what&rsquo;s inside &rarr;</p>
        </div>
        <div class="absolute inset-0 flex flex-col justify-center gap-3.5 rounded-[20px] p-6.5 text-white backface-hidden rotate-y-180 bg-linear-[155deg,var(--color-stk23-accent),var(--color-stk23-deep)] shadow-[0_24px_48px_-26px_rgba(0,0,0,0.85)] opacity-100 transition-opacity duration-300 motion-reduce:rotate-y-0! motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100">
          <ul class="flex list-none flex-col gap-2.25">
            <li class="relative pl-5.5 text-sm font-semibold before:absolute before:left-0 before:font-black before:content-['&#x2713;']">Unlimited projects</li>
            <li class="relative pl-5.5 text-sm font-semibold before:absolute before:left-0 before:font-black before:content-['&#x2713;']">Priority support</li>
            <li class="relative pl-5.5 text-sm font-semibold before:absolute before:left-0 before:font-black before:content-['&#x2713;']">SSO &amp; audit log</li>
          </ul>
          <button class="rounded-[11px] border-0 bg-white px-4 py-2.75 text-sm font-extrabold text-stk23-deep cursor-pointer transition-transform duration-150 hover:scale-[1.02] active:scale-95 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2" type="button">Start trial</button>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk23-bg: #0f1119;
  --color-stk23-bg: oklch(0.18 0.014 275);
  --color-stk23-under: #1c1f2b;
  --color-stk23-under: oklch(0.25 0.016 275);
  --color-stk23-line: #2b2f3d;
  --color-stk23-line: oklch(0.32 0.018 275);
  --color-stk23-f1: #242838;
  --color-stk23-f1: oklch(0.28 0.022 275);
  --color-stk23-f2: #181b28;
  --color-stk23-f2: oklch(0.23 0.020 275);
  --color-stk23-muted: #9aa0b4;
  --color-stk23-muted: oklch(0.70 0.018 275);
  --color-stk23-body: #c3c7de;
  --color-stk23-body: oklch(0.83 0.020 275);
  --color-stk23-accent: #7b8fe8;
  --color-stk23-accent: oklch(0.66 0.16 265);
  --color-stk23-deep: #5c4dc4;
  --color-stk23-deep: oklch(0.50 0.16 285);
  --font-stk23-sans: 'Archivo', system-ui, sans-serif;
  --font-stk23-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk23: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
