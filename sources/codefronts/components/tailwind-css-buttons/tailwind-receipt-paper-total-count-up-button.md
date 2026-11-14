---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-receipt-paper-total-count-up-button/"
title: "Tailwind Receipt Paper Total Count-Up Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A thermal receipt whose total counts up from zero when you press it — the number is animated by CSS, using a registered integer fed into counter-reset and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Receipt Paper Total Count-Up Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-receipt-paper-total-count-up-button/

A thermal receipt whose total counts up from zero when you press it — the number is animated by CSS, using a registered integer fed into counter-reset and printed through content. Zigzag torn edge, faded thermal ink, monospaced columns.
## HTML
```html
<div class="tb-49 w-full min-h-svh grid place-items-center font-tb49-mono p-[clamp(1.5rem,6vw,4rem)]">
  <label class="tb-49__slip group relative cursor-pointer grid gap-1.5 w-[min(100%,17rem)] px-4.5 pt-5 pb-6.5 text-[0.8125rem] leading-relaxed tabular-nums text-tb49-ink drop-shadow-[0_12px_18px_#00000080] transition-[translate,filter] duration-300 ease-tb49-out [-webkit-tap-highlight-color:transparent] hover:-translate-y-0.5 hover:drop-shadow-[0_18px_24px_#0000008c] has-focus-visible:-translate-y-0.5 has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tb49-accent active:translate-y-px motion-reduce:transition-none">
    <input type="checkbox" aria-label="Total the order" class="sr-only">
    <span class="text-center font-bold tracking-[0.18em] uppercase text-xs">Corner Roastery</span>
    <span class="flex justify-between gap-4 text-tb49-muted"><span>Filter, 12oz</span><span>18.00</span></span>
    <span class="flex justify-between gap-4 text-tb49-muted"><span>Beans, 250g</span><span>22.60</span></span>
    <span class="flex justify-between gap-4 text-tb49-muted"><span>Service</span><span>8.00</span></span>
    <span aria-hidden="true" class="block h-0 my-1.5 border-t border-dashed border-tb49-rule group-has-checked:border-solid"></span>
    <span class="flex items-baseline justify-between gap-4">
      <span class="font-bold tracking-[0.12em] uppercase text-xs">Total</span>
      <span class="relative text-2xl font-bold tracking-[-0.02em] text-tb49-accent">
        <span aria-hidden="true" class="tb-49__total hidden group-has-checked:animate-tb49-count"></span>
        <span class="tb-49__fallback inline">$48.60</span>
      </span>
    </span>
    <span class="text-center text-[0.6875rem] tracking-[0.06em] text-tb49-muted">Tap to tally · thank you</span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@property --tb-49-n {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

@theme {
  --color-tb49-bg: #26262a;
  --color-tb49-bg: oklch(0.28 0.006 285);
  --color-tb49-paper: #f7f4ec;
  --color-tb49-paper: oklch(0.97 0.012 90);
  --color-tb49-paper-lo: #e7e2d5;
  --color-tb49-paper-lo: oklch(0.91 0.014 88);
  --color-tb49-ink: #2c2a26;
  --color-tb49-ink: oklch(0.27 0.012 85);
  --color-tb49-muted: #5f5a50;
  --color-tb49-muted: oklch(0.46 0.014 85);
  --color-tb49-rule: #2c2a2659;
  --color-tb49-rule: oklch(0.27 0.012 85 / 0.35);
  --color-tb49-accent: #1f6f5c;
  --color-tb49-accent: oklch(0.45 0.1 168);
  --font-tb49-mono: "Courier Prime", ui-monospace, "Courier New", Courier, monospace;
  --ease-tb49-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb49-count: tb-49-count 1.5s cubic-bezier(0.2, 0.9, 0.2, 1) forwards;
}

@keyframes tb-49-count {
  from {
    --tb-49-n: 0;
  }

  to {
    --tb-49-n: 4860;
  }
}

.tb-49 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(30rem 20rem at 50% 34%, rgba(255,255,255,.05), transparent 72%), var(--color-tb49-bg);
}
/* THERMAL STOCK + ZIGZAG TEAR: a .4rem strip of downward teeth at the bottom,
   unioned with a base covering the rest. */

.tb-49__slip {
  background-color: var(--color-tb49-paper);
  background-image: radial-gradient(.05rem .05rem at 30% 40%, rgba(90,84,70,.14) 99%, transparent), linear-gradient(180deg, var(--color-tb49-paper), var(--color-tb49-paper-lo));
  background-size: 5px 5px, 100% 100%;
  -webkit-mask: conic-gradient(from 135deg at 50% 0, #000 90deg, transparent 0) 0 100%/.76rem .4rem repeat-x, linear-gradient(#000, #000) 0 0/100% calc(100% - .38rem) no-repeat;
  mask: conic-gradient(from 135deg at 50% 0, #000 90deg, transparent 0) 0 100%/.76rem .4rem repeat-x, linear-gradient(#000, #000) 0 0/100% calc(100% - .38rem) no-repeat;
}
/* THE COUNT-UP ENGINE. Registration + counter split + generated content: none of
   this has a utility form, and the real-text fallback below is why it is safe. */

@supports (counter-reset: x var(--tb-49-n)) {
  .tb-49__total {
    display: inline;
    counter-reset: tb-49-a calc(var(--tb-49-n) / 100) tb-49-b calc(var(--tb-49-n) - (var(--tb-49-n) / 100) * 100);
  }

  .tb-49__total::after {
    content: "$" counter(tb-49-a) "." counter(tb-49-b, decimal-leading-zero);
  }

  .tb-49__fallback {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tb-49__total {
    animation: none !important;
    --tb-49-n: 4860;
  }
}

@media (prefers-color-scheme: light) {
  .tb-49:not([data-theme="dark"]) {
    --color-tb49-bg: oklch(0.33 0.006 285);
  }
}

.tb-49[data-theme="light"] {
  --color-tb49-bg: oklch(0.33 0.006 285);
}

@media (forced-colors: active) {
  .tb-49__slip {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
    mask: none;
    -webkit-mask: none;
    filter: none;
  }

  .tb-49__slip span {
    color: CanvasText;
  }
}
```
