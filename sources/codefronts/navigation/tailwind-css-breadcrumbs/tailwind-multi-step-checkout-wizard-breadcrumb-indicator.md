---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-multi-step-checkout-wizard-breadcrumb-indicator/"
title: "Tailwind Multi-Step Checkout & Wizard Breadcrumb Indicator"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Breadcrumbs as a checkout progress bar: auto-numbered circular badges, connector lines that fill for completed steps, and three states read straight off a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Step Checkout & Wizard Breadcrumb Indicator
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-multi-step-checkout-wizard-breadcrumb-indicator/

Breadcrumbs as a checkout progress bar: auto-numbered circular badges, connector lines that fill for completed steps, and three states read straight off a data-state attribute with data-[state=done]: variants. The numbering stays a CSS counter &mdash; the one thing utilities genuinely cannot do.
## HTML
```html
<section class="tbc-27 w-full min-h-svh grid place-items-center bg-tbc27-bg font-tbc27-sans px-7 py-9">
  <nav aria-label="Checkout progress" class="w-[min(560px,100%)]">
    <ol class="flex list-none m-0 p-0 [counter-reset:tbc27step]">
      <li data-state="done" class="group relative flex-1 flex flex-col items-center gap-2.5 text-center before:content-[''] before:absolute before:top-4 before:-left-1/2 before:w-full before:h-0.75 before:z-0 before:bg-tbc27-done first:before:hidden">
        <span aria-hidden="true" class="relative z-1 grid place-items-center w-8.5 h-8.5 rounded-full text-sm font-bold [counter-increment:tbc27step] bg-tbc27-done border-2 border-tbc27-done text-white before:content-['\2713']"></span>
        <span class="text-[13px]/[1.2] font-semibold text-tbc27-label">Cart</span>
        <span class="sr-only">completed</span>
      </li>
      <li data-state="done" class="group relative flex-1 flex flex-col items-center gap-2.5 text-center before:content-[''] before:absolute before:top-4 before:-left-1/2 before:w-full before:h-0.75 before:z-0 before:bg-tbc27-done">
        <span aria-hidden="true" class="relative z-1 grid place-items-center w-8.5 h-8.5 rounded-full text-sm font-bold [counter-increment:tbc27step] bg-tbc27-done border-2 border-tbc27-done text-white before:content-['\2713']"></span>
        <span class="text-[13px]/[1.2] font-semibold text-tbc27-label">Shipping</span>
        <span class="sr-only">completed</span>
      </li>
      <li data-state="current" aria-current="step" class="group relative flex-1 flex flex-col items-center gap-2.5 text-center before:content-[''] before:absolute before:top-4 before:-left-1/2 before:w-full before:h-0.75 before:z-0 before:bg-tbc27-done">
        <span aria-hidden="true" class="relative z-1 grid place-items-center w-8.5 h-8.5 rounded-full text-sm font-bold [counter-increment:tbc27step] bg-white border-2 border-tbc27-acc text-tbc27-acc shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tbc27-acc)_20%,transparent)] before:content-[counter(tbc27step)]"></span>
        <span class="text-[13px]/[1.2] font-bold text-tbc27-strong">Payment</span>
      </li>
      <li data-state="upcoming" class="group relative flex-1 flex flex-col items-center gap-2.5 text-center before:content-[''] before:absolute before:top-4 before:-left-1/2 before:w-full before:h-0.75 before:z-0 before:bg-tbc27-mut">
        <span aria-hidden="true" class="relative z-1 grid place-items-center w-8.5 h-8.5 rounded-full text-sm font-bold [counter-increment:tbc27step] bg-white border-2 border-tbc27-mut text-tbc27-mutink before:content-[counter(tbc27step)]"></span>
        <span class="text-[13px]/[1.2] font-semibold text-tbc27-mutink">Review</span>
      </li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc27-bg: #fbfbfd;
  --color-tbc27-bg: oklch(0.98 0.004 250);
  --color-tbc27-acc: #4a68d4;
  --color-tbc27-acc: oklch(0.55 0.16 265);
  --color-tbc27-done: #2f8f6b;
  --color-tbc27-done: oklch(0.55 0.13 160);
  --color-tbc27-mut: #d2d5dd;
  --color-tbc27-mut: oklch(0.85 0.01 250);
  --color-tbc27-mutink: #7d818c;
  --color-tbc27-mutink: oklch(0.56 0.01 250);
  --color-tbc27-label: #61656f;
  --color-tbc27-label: oklch(0.46 0.02 250);
  --color-tbc27-strong: #32353d;
  --color-tbc27-strong: oklch(0.28 0.02 250);
  --font-tbc27-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-27 {
  width: 100%;
  min-height: 100svh;
}
/* counter() inside content has no utility form — the numeral itself is the one part
   of this pattern that must stay in CSS. */

.tbc-27 li span[aria-hidden]::before {
  line-height: 1;
}
```
