---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-button-group-component-segmented/"
title: "Tailwind Button Group Component (Segmented Radio-Like)"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A segmented control on real radio inputs, so arrow-key navigation, roving focus and form serialisation come from the platform."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Button Group Component (Segmented Radio-Like)
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-button-group-component-segmented/

A segmented control on real radio inputs, so arrow-key navigation, roving focus and form serialisation come from the platform. The sliding thumb tracks the checked segment, and the port makes the label's own inversion a has-checked: variant — the state is read where it is rendered, not from four rules at the bottom of a stylesheet.
## HTML
```html
<div class="tb-08 w-full min-h-svh grid place-items-center bg-tb08-bg font-tb08-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <div role="group" aria-label="Chart range" class="tb-08__group relative flex w-[min(100%,25rem)] p-[0.3rem] rounded-[1rem] bg-tb08-track shadow-[inset_0_1px_2px_var(--color-tb08-inset)] active:[&_.tb-08\_\_thumb]:scale-[0.97]">
    <span aria-hidden="true" class="tb-08__thumb absolute z-0 top-[0.3rem] left-[0.3rem] bottom-[0.3rem] w-[calc((100%-0.6rem)/4)] rounded-[0.7rem] bg-tb08-thumb shadow-[0_1px_2px_var(--color-tb08-shadow-1),0_6px_14px_-8px_var(--color-tb08-shadow-2)] transition-[translate,scale] duration-500 ease-tb08-spring motion-reduce:transition-none"></span>
    <label class="relative z-10 flex-1 cursor-pointer grid place-items-center min-h-11 px-2 rounded-[0.7rem] text-sm font-semibold tracking-[-0.005em] text-tb08-muted transition-colors duration-200 [-webkit-tap-highlight-color:transparent] hover:text-tb08-ink-soft has-checked:text-tb08-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tb08-accent motion-reduce:transition-none"><input type="radio" name="tb-08-range" value="day" class="sr-only"><span>Day</span></label>
    <label class="relative z-10 flex-1 cursor-pointer grid place-items-center min-h-11 px-2 rounded-[0.7rem] text-sm font-semibold tracking-[-0.005em] text-tb08-muted transition-colors duration-200 [-webkit-tap-highlight-color:transparent] hover:text-tb08-ink-soft has-checked:text-tb08-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tb08-accent motion-reduce:transition-none"><input type="radio" name="tb-08-range" value="week" checked class="sr-only"><span>Week</span></label>
    <label class="relative z-10 flex-1 cursor-pointer grid place-items-center min-h-11 px-2 rounded-[0.7rem] text-sm font-semibold tracking-[-0.005em] text-tb08-muted transition-colors duration-200 [-webkit-tap-highlight-color:transparent] hover:text-tb08-ink-soft has-checked:text-tb08-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tb08-accent motion-reduce:transition-none"><input type="radio" name="tb-08-range" value="month" class="sr-only"><span>Month</span></label>
    <label class="relative z-10 flex-1 cursor-pointer grid place-items-center min-h-11 px-2 rounded-[0.7rem] text-sm font-semibold tracking-[-0.005em] text-tb08-muted transition-colors duration-200 [-webkit-tap-highlight-color:transparent] hover:text-tb08-ink-soft has-checked:text-tb08-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tb08-accent motion-reduce:transition-none"><input type="radio" name="tb-08-range" value="year" class="sr-only"><span>Year</span></label>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb08-bg: #f1f2f4;
  --color-tb08-bg: oklch(0.958 0.004 265);
  --color-tb08-track: #e6e7ea;
  --color-tb08-track: oklch(0.925 0.005 265);
  --color-tb08-thumb: #ffffff;
  --color-tb08-ink: #0d0d12;
  --color-tb08-ink: oklch(0.15 0.008 280);
  --color-tb08-ink-soft: #3a3a45;
  --color-tb08-ink-soft: oklch(0.34 0.01 280);
  --color-tb08-muted: #55555f;
  --color-tb08-muted: oklch(0.45 0.012 280);
  --color-tb08-accent: #5b21b6;
  --color-tb08-accent: oklch(0.44 0.2 296);
  --color-tb08-inset: #0d0d121f;
  --color-tb08-inset: oklch(0.15 0.008 280 / 0.12);
  --color-tb08-shadow-1: #0d0d122e;
  --color-tb08-shadow-1: oklch(0.15 0.008 280 / 0.18);
  --color-tb08-shadow-2: #0d0d1266;
  --color-tb08-shadow-2: oklch(0.15 0.008 280 / 0.4);
  --font-tb08-sans: "Manrope", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb08-spring: cubic-bezier(0.16, 1, 0.3, 1);
}

@supports (transition-timing-function: linear(0, 1)) {
  @theme {
    --ease-tb08-spring: linear(0, 0.42 8%, 0.79 17%, 1.02 24%, 1.09 29%, 1.06 36%, 1 48%, 1);
  }
}

.tb-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
/* Positional sibling state: which of four is checked. No Tailwind variant expresses this. */

.tb-08__group:has(label:nth-of-type(2) input:checked) .tb-08__thumb {
  translate: 100% 0;
}

.tb-08__group:has(label:nth-of-type(3) input:checked) .tb-08__thumb {
  translate: 200% 0;
}

.tb-08__group:has(label:nth-of-type(4) input:checked) .tb-08__thumb {
  translate: 300% 0;
}

@supports not selector(:has(*)) {
  .tb-08__thumb {
    display: none;
  }

  .tb-08 input:checked ~ span {
    color: var(--color-tb08-ink);
    text-decoration: underline;
    text-underline-offset: 0.4em;
  }
}

@media (prefers-color-scheme: dark) {
  .tb-08:not([data-theme="light"]) {
    --color-tb08-bg: oklch(0.12 0.006 280);
    --color-tb08-track: oklch(0.2 0.008 280);
    --color-tb08-thumb: oklch(0.32 0.012 280);
    --color-tb08-ink: oklch(0.97 0.003 280);
    --color-tb08-ink-soft: oklch(0.85 0.006 280);
    --color-tb08-muted: oklch(0.68 0.01 280);
    --color-tb08-accent: oklch(0.78 0.13 296);
  }
}

.tb-08[data-theme="dark"] {
  --color-tb08-bg: oklch(0.12 0.006 280);
  --color-tb08-track: oklch(0.2 0.008 280);
  --color-tb08-thumb: oklch(0.32 0.012 280);
  --color-tb08-ink: oklch(0.97 0.003 280);
  --color-tb08-muted: oklch(0.68 0.01 280);
}

@media (forced-colors: active) {
  .tb-08__group {
    border: 1px solid ButtonText;
  }

  .tb-08__thumb {
    background: Highlight;
  }

  .tb-08 label:has(input:checked) {
    color: HighlightText;
  }
}
```
