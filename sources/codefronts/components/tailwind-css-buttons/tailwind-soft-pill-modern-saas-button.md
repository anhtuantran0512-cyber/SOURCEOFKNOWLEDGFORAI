---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-soft-pill-modern-saas-button/"
title: "Tailwind Soft Pill Modern SaaS Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "The button a 2027 SaaS product ships: a soft pill with a true 1px gradient stroke drawn by mask-composite, an inner top-light, a spring lift, a shortcut chip…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Soft Pill Modern SaaS Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-soft-pill-modern-saas-button/

The button a 2027 SaaS product ships: a soft pill with a true 1px gradient stroke drawn by mask-composite, an inner top-light, a spring lift, a shortcut chip that dims as the arrow slides, and a focus ring that respects the radius exactly.
## HTML
```html
<div class="tb-32 w-full min-h-svh grid place-items-center font-tb32-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-32__btn group relative cursor-pointer grid grid-flow-col items-center gap-3 min-h-13 pl-6 pr-3 border-0 rounded-full text-[0.9375rem] font-semibold tracking-[-0.012em] text-tb32-ink bg-[linear-gradient(180deg,var(--color-tb32-surface),var(--color-tb32-surface-lo))] shadow-[inset_0_1px_0_#ffffffd9,0_1px_2px_var(--color-tb32-shadow-1),0_10px_24px_-14px_var(--color-tb32-shadow-2)] transition-[translate,box-shadow,color] duration-500 ease-tb32-spring before:content-[''] before:absolute before:inset-0 before:rounded-[inherit] before:p-px before:pointer-events-none before:bg-[linear-gradient(160deg,var(--color-tb32-stroke-a),var(--color-tb32-stroke-b))] before:[mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask-composite:exclude] before:transition-[background] before:duration-300 hover:-translate-y-[3px] hover:shadow-[inset_0_1px_0_#ffffffe6,0_2px_4px_var(--color-tb32-shadow-1),0_18px_34px_-16px_var(--color-tb32-accent-glow)] hover:before:bg-[linear-gradient(160deg,var(--color-tb32-accent-soft),var(--color-tb32-stroke-b))] active:translate-y-px active:shadow-[inset_0_1px_3px_var(--color-tb32-shadow-2)] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb32-accent disabled:cursor-not-allowed disabled:text-tb32-muted disabled:opacity-60 disabled:translate-y-0 supports-not-[mask-composite:exclude]:border supports-not-[mask-composite:exclude]:border-tb32-stroke-b supports-not-[mask-composite:exclude]:before:hidden motion-reduce:transition-none motion-reduce:hover:translate-y-0">
    <span>Create workspace</span>
    <kbd class="font-tb32-sans text-[0.6875rem] font-bold tracking-[0.04em] text-tb32-muted px-2 py-1 rounded-[0.45rem] bg-tb32-chip shadow-[inset_0_0_0_1px_var(--color-tb32-chip-line)] transition-[opacity,translate] duration-400 ease-tb32-out group-hover:opacity-45 group-hover:-translate-x-0.5 motion-reduce:transition-none">⌘ K</kbd>
    <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-[1.05rem] mr-1.5 text-tb32-accent transition-transform duration-[450ms] ease-tb32-out group-hover:translate-x-1 motion-reduce:transition-none"><path d="M5 12h13"/><path d="M12.5 6 18.5 12l-6 6"/></svg>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb32-bg: #f7f8fa;
  --color-tb32-bg: oklch(0.975 0.004 265);
  --color-tb32-surface: #ffffff;
  --color-tb32-surface-lo: #f2f4f8;
  --color-tb32-surface-lo: oklch(0.96 0.005 265);
  --color-tb32-ink: #101114;
  --color-tb32-ink: oklch(0.17 0.008 265);
  --color-tb32-muted: #5f6472;
  --color-tb32-muted: oklch(0.47 0.015 265);
  --color-tb32-accent: #3d5afe;
  --color-tb32-accent: oklch(0.52 0.22 268);
  --color-tb32-accent-soft: #8a9bff;
  --color-tb32-accent-soft: oklch(0.72 0.13 268);
  --color-tb32-accent-glow: #3d5afe73;
  --color-tb32-accent-glow: oklch(0.52 0.22 268 / 0.45);
  --color-tb32-stroke-a: #e3e6ee;
  --color-tb32-stroke-a: oklch(0.92 0.008 265);
  --color-tb32-stroke-b: #c9cede;
  --color-tb32-stroke-b: oklch(0.85 0.012 265);
  --color-tb32-chip: #1011140f;
  --color-tb32-chip: oklch(0.17 0.008 265 / 0.06);
  --color-tb32-chip-line: #10111416;
  --color-tb32-chip-line: oklch(0.17 0.008 265 / 0.09);
  --color-tb32-shadow-1: #10111414;
  --color-tb32-shadow-1: oklch(0.17 0.008 265 / 0.08);
  --color-tb32-shadow-2: #10111473;
  --color-tb32-shadow-2: oklch(0.17 0.008 265 / 0.45);
  --font-tb32-sans: "Manrope", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb32-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-tb32-spring: cubic-bezier(0.16, 1, 0.3, 1);
}

@supports (transition-timing-function: linear(0, 1)) {
  @theme {
    --ease-tb32-spring: linear(0, 0.4 7%, 0.83 15%, 1.06 23%, 1.09 28%, 1.03 37%, 1 52%, 1);
  }
}

.tb-32 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(48rem 30rem at 50% -10%, color-mix(in oklab, var(--color-tb32-accent) 8%, transparent), transparent 70%), var(--color-tb32-bg);
}
/* The -webkit- mask-composite keyword differs from the standard one ('xor' vs
   'exclude') and cannot ride the same arbitrary utility. */

.tb-32__btn::before {
  -webkit-mask-composite: xor;
}

@media (prefers-color-scheme: dark) {
  .tb-32:not([data-theme="light"]) {
    --color-tb32-bg: oklch(0.13 0.008 265);
    --color-tb32-surface: oklch(0.19 0.01 265);
    --color-tb32-surface-lo: oklch(0.17 0.01 265);
    --color-tb32-ink: oklch(0.96 0.004 265);
    --color-tb32-muted: oklch(0.72 0.015 265);
    --color-tb32-stroke-a: oklch(0.29 0.012 265);
    --color-tb32-stroke-b: oklch(0.38 0.015 265);
    --color-tb32-accent: oklch(0.7 0.15 268);
    --color-tb32-chip: oklch(0.96 0.004 265 / 0.08);
    --color-tb32-chip-line: oklch(0.96 0.004 265 / 0.12);
  }
}

.tb-32[data-theme="dark"] {
  --color-tb32-bg: oklch(0.13 0.008 265);
  --color-tb32-surface: oklch(0.19 0.01 265);
  --color-tb32-surface-lo: oklch(0.17 0.01 265);
  --color-tb32-ink: oklch(0.96 0.004 265);
  --color-tb32-muted: oklch(0.72 0.015 265);
  --color-tb32-accent: oklch(0.7 0.15 268);
}

@media (forced-colors: active) {
  .tb-32__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-32__btn::before {
    display: none;
  }

  .tb-32__btn kbd {
    border: 1px solid ButtonText;
    background: ButtonFace;
  }
}
```
