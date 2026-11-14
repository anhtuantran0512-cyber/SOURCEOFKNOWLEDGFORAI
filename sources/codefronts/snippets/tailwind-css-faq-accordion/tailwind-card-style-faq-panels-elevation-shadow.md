---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-card-style-faq-panels-elevation-shadow/"
title: "Tailwind Card-Style FAQ Panels with a Layered Shadow Elevation System"
section: "snippets"
category: "tailwind-css-faq-accordion"
category_name: "Tailwind CSS FAQ Accordion"
description: "Separated FAQ cards with a real elevation system: three levels (resting, hover, open) built from layered shadows that mimic how light actually falls — a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Card-Style FAQ Panels with a Layered Shadow Elevation System
Source: https://codefronts.com/snippets/tailwind-css-faq-accordion/tailwind-card-style-faq-panels-elevation-shadow/

Separated FAQ cards with a real elevation system: three levels (resting, hover, open) built from layered shadows that mimic how light actually falls — a tight dark contact layer plus a wide soft ambient one — instead of the single fuzzy grey blob of tutorial CSS. Cards lift 2px on hover and rise to full elevation when open, with the shadow tinted in the page's own hue rather than black.
## HTML
```html
<section class="tfa-17 w-full min-h-svh grid place-items-center bg-tfa17-bg font-tfa17-sans text-tfa17-ink px-5 py-12">
  <div class="w-[min(640px,100%)]">
    <header>
      <h1 class="text-[clamp(26px,4.6vw,38px)] font-extrabold tracking-[-0.025em]">Warranty &amp; repairs</h1>
      <p class="mt-3 max-w-[52ch] text-[14.5px] leading-relaxed text-tfa17-mut">Three elevations: resting, hover-lift, open. Every shadow is two layers — contact plus ambient — in the page's own hue.</p>
    </header>

    <div data-panel class="mt-7 flex flex-col gap-4">
      <details class="group rounded-[18px] border border-tfa17-edge bg-white shadow-[0_1px_2px_oklch(0.35_0.04_265/0.1),0_4px_12px_oklch(0.35_0.04_265/0.07)] [&:not([open]):hover]:shadow-[0_2px_3px_oklch(0.35_0.04_265/0.12),0_8px_20px_oklch(0.35_0.04_265/0.1)] [&:not([open]):hover]:-translate-y-0.5 open:shadow-[0_2px_4px_oklch(0.35_0.04_265/0.12),0_12px_32px_oklch(0.35_0.04_265/0.14),0_24px_60px_oklch(0.35_0.04_265/0.1)] open:-translate-y-0.5 open:border-transparent transition-[box-shadow,translate,border-color] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none" open>
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-[18px] text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa17-acc focus-visible:rounded-[18px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa17-acc [&::-webkit-details-marker]:hidden">What does the warranty cover?
          <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-[10px] bg-tfa17-tint text-tfa17-acc transition-[rotate,background-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:bg-tfa17-tinthover group-open:rotate-180 motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[58ch] px-5 pb-[19px] text-[14px] leading-[1.7] text-tfa17-mut">Two years, parts and labour, covering manufacturing defects and battery health below 80%. Accidental damage is a separate care plan — but out-of-warranty repairs are flat-rate and published, never “send it in for a quote”.</p>
      </details>
      <details class="group rounded-[18px] border border-tfa17-edge bg-white shadow-[0_1px_2px_oklch(0.35_0.04_265/0.1),0_4px_12px_oklch(0.35_0.04_265/0.07)] [&:not([open]):hover]:shadow-[0_2px_3px_oklch(0.35_0.04_265/0.12),0_8px_20px_oklch(0.35_0.04_265/0.1)] [&:not([open]):hover]:-translate-y-0.5 open:shadow-[0_2px_4px_oklch(0.35_0.04_265/0.12),0_12px_32px_oklch(0.35_0.04_265/0.14),0_24px_60px_oklch(0.35_0.04_265/0.1)] open:-translate-y-0.5 open:border-transparent transition-[box-shadow,translate,border-color] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-[18px] text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa17-acc focus-visible:rounded-[18px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa17-acc [&::-webkit-details-marker]:hidden">How do I start a repair?
          <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-[10px] bg-tfa17-tint text-tfa17-acc transition-[rotate,background-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:bg-tfa17-tinthover group-open:rotate-180 motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[58ch] px-5 pb-[19px] text-[14px] leading-[1.7] text-tfa17-mut">Run the diagnostic in the app, which pre-fills the repair ticket with logs. A prepaid label arrives by email; most repairs turn around in five business days door to door, with a loaner option on the care plan.</p>
      </details>
      <details class="group rounded-[18px] border border-tfa17-edge bg-white shadow-[0_1px_2px_oklch(0.35_0.04_265/0.1),0_4px_12px_oklch(0.35_0.04_265/0.07)] [&:not([open]):hover]:shadow-[0_2px_3px_oklch(0.35_0.04_265/0.12),0_8px_20px_oklch(0.35_0.04_265/0.1)] [&:not([open]):hover]:-translate-y-0.5 open:shadow-[0_2px_4px_oklch(0.35_0.04_265/0.12),0_12px_32px_oklch(0.35_0.04_265/0.14),0_24px_60px_oklch(0.35_0.04_265/0.1)] open:-translate-y-0.5 open:border-transparent transition-[box-shadow,translate,border-color] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-[18px] text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa17-acc focus-visible:rounded-[18px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa17-acc [&::-webkit-details-marker]:hidden">Can I repair it myself?
          <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-[10px] bg-tfa17-tint text-tfa17-acc transition-[rotate,background-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:bg-tfa17-tinthover group-open:rotate-180 motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[58ch] px-5 pb-[19px] text-[14px] leading-[1.7] text-tfa17-mut">Yes — self-repair kits with genuine parts, tools and guides cover the battery, screen and buttons. DIY repairs with our parts do not void the warranty; third-party parts void only the affected subsystem.</p>
      </details>
      <details class="group rounded-[18px] border border-tfa17-edge bg-white shadow-[0_1px_2px_oklch(0.35_0.04_265/0.1),0_4px_12px_oklch(0.35_0.04_265/0.07)] [&:not([open]):hover]:shadow-[0_2px_3px_oklch(0.35_0.04_265/0.12),0_8px_20px_oklch(0.35_0.04_265/0.1)] [&:not([open]):hover]:-translate-y-0.5 open:shadow-[0_2px_4px_oklch(0.35_0.04_265/0.12),0_12px_32px_oklch(0.35_0.04_265/0.14),0_24px_60px_oklch(0.35_0.04_265/0.1)] open:-translate-y-0.5 open:border-transparent transition-[box-shadow,translate,border-color] duration-350 ease-[cubic-bezier(0.4,0,0.2,1)] motion-reduce:transition-none">
        <summary class="flex min-h-11 cursor-pointer list-none items-center justify-between gap-4 px-5 py-[18px] text-[15.5px] font-semibold tracking-[-0.01em] transition-colors duration-200 hover:text-tfa17-acc focus-visible:rounded-[18px] focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tfa17-acc [&::-webkit-details-marker]:hidden">Is water damage covered?
          <span aria-hidden="true" class="grid size-7 shrink-0 place-items-center rounded-[10px] bg-tfa17-tint text-tfa17-acc transition-[rotate,background-color] duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:bg-tfa17-tinthover group-open:rotate-180 motion-reduce:transition-colors"><svg viewBox="0 0 16 16" width="13" height="13"><path d="M3 6l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </summary>
        <p class="max-w-[58ch] px-5 pb-[19px] text-[14px] leading-[1.7] text-tfa17-mut">IP67 failures within rating are warranty repairs — a pressure test tells us quickly. Beyond-rating exposure (diving, jacuzzi chemistry) falls to the care plan accidental tier at the flat rate.</p>
      </details>
    </div>

    <p class="mt-6 text-[12.5px] text-tfa17-mut">Shadow recipe: tight contact layer plus wide ambient layer, tinted in the page hue. Never plain black.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfa17-bg: #f0f0f7;
  --color-tfa17-bg: oklch(0.95 0.012 265);
  --color-tfa17-ink: #2a2733;
  --color-tfa17-ink: oklch(0.24 0.03 268);
  --color-tfa17-mut: #5d596b;
  --color-tfa17-mut: oklch(0.47 0.022 265);
  --color-tfa17-edge: #e3e1ec;
  --color-tfa17-edge: oklch(0.91 0.012 265);
  --color-tfa17-tint: #ebe8fa;
  --color-tfa17-tint: oklch(0.93 0.03 268);
  --color-tfa17-tinthover: #ded8f7;
  --color-tfa17-tinthover: oklch(0.89 0.05 268);
  --color-tfa17-acc: #5238c8;
  --color-tfa17-acc: oklch(0.45 0.2 268);
  --font-tfa17-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tfa-17 {
  width: 100%;
  min-height: 100svh;
}

.tfa-17 [data-panel] {
  interpolate-size: allow-keywords;
}

@supports (interpolate-size: allow-keywords) {
  .tfa-17 details::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1), opacity .3s, content-visibility .38s allow-discrete;
  }

  .tfa-17 details[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tfa-17 details::details-content {
    transition-duration: 1ms;
  }
}
```
