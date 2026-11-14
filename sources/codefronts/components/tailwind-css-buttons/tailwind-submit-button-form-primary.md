---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-submit-button-form-primary/"
title: "Tailwind Submit Button (Form Primary)"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "The button every form ends with, ported: a two-layer elevation shadow that reads as physical depth, a masked sheen that sweeps once on hover, a real 1px…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Submit Button (Form Primary)
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-submit-button-form-primary/

The button every form ends with, ported: a two-layer elevation shadow that reads as physical depth, a masked sheen that sweeps once on hover, a real 1px press travel, and a focus ring that survives on any background. The port's win is that all four states now sit in one class list — hover:, active:, focus-visible: and disabled: read in the order a user meets them.
## HTML
```html
<div class="tb-01 w-full min-h-svh grid place-items-center bg-tb01-bg font-tb01-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <button type="submit" class="group relative isolate overflow-hidden cursor-pointer inline-grid grid-flow-col items-center gap-2.5 min-h-13 px-7 border-0 rounded-[0.9rem] text-base font-semibold tracking-[-0.01em] text-tb01-on-accent bg-[linear-gradient(180deg,var(--color-tb01-accent-lift),var(--color-tb01-accent))] transition-[translate,box-shadow,filter] duration-200 ease-tb01-out before:content-[''] before:absolute before:inset-0 before:-z-10 before:pointer-events-none before:-translate-x-[125%] before:bg-[linear-gradient(105deg,transparent_35%,rgba(255,255,255,0.42)_50%,transparent_65%)] before:transition-transform before:duration-[800ms] before:ease-tb01-out hover:-translate-y-0.5 hover:saturate-[1.06] hover:before:translate-x-[125%] focus-visible:before:translate-x-[125%] active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb01-ring disabled:cursor-not-allowed disabled:grayscale disabled:opacity-50 disabled:translate-y-0 disabled:shadow-none motion-reduce:transition-none motion-reduce:before:hidden shadow-[inset_0_1px_0_rgba(255,255,255,0.38),0_1px_2px_var(--color-tb01-shadow-soft),0_10px_24px_-8px_var(--color-tb01-shadow-wide)] active:shadow-[inset_0_2px_6px_var(--color-tb01-shadow-press)] focus-visible:shadow-[inset_0_1px_0_rgba(255,255,255,0.38),0_0_0_6px_var(--color-tb01-halo)]">
    <span>Create account</span>
    <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" class="w-[1.15rem] h-[1.15rem] transition-transform duration-300 ease-tb01-out group-hover:translate-x-1 motion-reduce:transition-none motion-reduce:group-hover:translate-x-0"><path d="M4 12h14"/><path d="M12.5 5.5 19 12l-6.5 6.5"/></svg>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb01-bg: #f2f1ee;
  --color-tb01-bg: oklch(0.965 0.006 95);
  --color-tb01-accent: #16a34a;
  --color-tb01-accent: oklch(0.58 0.15 152);
  --color-tb01-accent-lift: #2dbb60;
  --color-tb01-accent-lift: oklch(0.645 0.148 152);
  --color-tb01-on-accent: #ffffff;
  --color-tb01-ring: #0f7538;
  --color-tb01-ring: oklch(0.45 0.13 152);
  --color-tb01-shadow-soft: #0b3d2061;
  --color-tb01-shadow-soft: oklch(0.32 0.09 155 / 0.38);
  --color-tb01-shadow-wide: #0b3d208c;
  --color-tb01-shadow-wide: oklch(0.32 0.09 155 / 0.55);
  --color-tb01-shadow-press: #0b3d2073;
  --color-tb01-shadow-press: oklch(0.32 0.09 155 / 0.45);
  --color-tb01-halo: #16a34a38;
  --color-tb01-halo: oklch(0.58 0.15 152 / 0.22);
  --font-tb01-sans: "Schibsted Grotesk", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb01-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
/* Dark scheme re-points the same tokens; @theme cannot hold a media query. */

@media (prefers-color-scheme: dark) {
  .tb-01:not([data-theme="light"]) {
    --color-tb01-bg: oklch(0.17 0.012 165);
    --color-tb01-accent: oklch(0.72 0.17 152);
    --color-tb01-accent-lift: oklch(0.78 0.15 152);
    --color-tb01-on-accent: oklch(0.18 0.05 155);
    --color-tb01-shadow-soft: oklch(0 0 0 / 0.5);
    --color-tb01-shadow-wide: oklch(0 0 0 / 0.7);
  }
}

.tb-01[data-theme="dark"] {
  --color-tb01-bg: oklch(0.17 0.012 165);
  --color-tb01-accent: oklch(0.72 0.17 152);
  --color-tb01-accent-lift: oklch(0.78 0.15 152);
  --color-tb01-on-accent: oklch(0.18 0.05 155);
}

@media (forced-colors: active) {
  .tb-01 button {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-01 button::before {
    display: none;
  }
}
```
