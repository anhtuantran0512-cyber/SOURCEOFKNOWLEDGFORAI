---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-disabled-button-state-full-reference/"
title: "Tailwind Disabled Button State (Full State Reference)"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Every button state side by side — rest, hover, focus, pressed, truly disabled, and aria-disabled (focusable, explains itself, refuses activation)."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Disabled Button State (Full State Reference)
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-disabled-button-state-full-reference/

Every button state side by side — rest, hover, focus, pressed, truly disabled, and aria-disabled (focusable, explains itself, refuses activation). The frozen cards use data-force attributes rather than .is-* classes, which is the tidiest thing the port does: demo-only styling is visibly demo-only.
## HTML
```html
<div class="tb-07 w-full min-h-svh grid place-items-center bg-tb07-bg font-tb07-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <div class="flex flex-wrap justify-center gap-3 max-w-[44rem]">
    <button type="button" class="cursor-pointer grid place-items-center min-h-12 min-w-30 px-5 border-0 rounded-[0.7rem] text-[0.9375rem] font-semibold text-tb07-ink bg-tb07-fill shadow-[0_8px_18px_-12px_var(--color-tb07-glow)] transition-[background-color,translate,scale] duration-200 ease-tb07-out hover:bg-tb07-fill-h hover:-translate-y-px active:bg-tb07-fill-a active:translate-y-px active:scale-[0.985] active:shadow-none focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb07-accent disabled:bg-tb07-off disabled:text-tb07-muted disabled:cursor-not-allowed disabled:shadow-none disabled:translate-y-0 aria-disabled:bg-tb07-off aria-disabled:text-tb07-muted aria-disabled:cursor-not-allowed aria-disabled:shadow-none data-force-hover:bg-tb07-fill-h data-force-hover:-translate-y-px data-force-focus:outline-2 data-force-focus:outline-offset-[3px] data-force-focus:outline-tb07-accent data-force-active:bg-tb07-fill-a data-force-active:translate-y-px data-force-active:scale-[0.985] aria-disabled:active:animate-tb07-nope motion-reduce:transition-none motion-reduce:aria-disabled:active:animate-none">Rest</button>
    <button type="button" data-force-hover class="cursor-pointer grid place-items-center min-h-12 min-w-30 px-5 border-0 rounded-[0.7rem] text-[0.9375rem] font-semibold text-tb07-ink bg-tb07-fill shadow-[0_8px_18px_-12px_var(--color-tb07-glow)] transition-[background-color,translate,scale] duration-200 ease-tb07-out hover:bg-tb07-fill-h hover:-translate-y-px active:bg-tb07-fill-a active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb07-accent data-force-hover:bg-tb07-fill-h data-force-hover:-translate-y-px motion-reduce:transition-none">Hover</button>
    <button type="button" data-force-focus class="cursor-pointer grid place-items-center min-h-12 min-w-30 px-5 border-0 rounded-[0.7rem] text-[0.9375rem] font-semibold text-tb07-ink bg-tb07-fill shadow-[0_8px_18px_-12px_var(--color-tb07-glow)] transition-[background-color,translate,scale] duration-200 ease-tb07-out hover:bg-tb07-fill-h hover:-translate-y-px active:bg-tb07-fill-a active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb07-accent data-force-focus:outline-2 data-force-focus:outline-offset-[3px] data-force-focus:outline-tb07-accent motion-reduce:transition-none">Focus</button>
    <button type="button" data-force-active class="cursor-pointer grid place-items-center min-h-12 min-w-30 px-5 border-0 rounded-[0.7rem] text-[0.9375rem] font-semibold text-tb07-ink bg-tb07-fill transition-[background-color,translate,scale] duration-200 ease-tb07-out hover:bg-tb07-fill-h active:bg-tb07-fill-a focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb07-accent data-force-active:bg-tb07-fill-a data-force-active:translate-y-px data-force-active:scale-[0.985] data-force-active:shadow-none motion-reduce:transition-none">Pressed</button>
    <button type="button" disabled class="grid place-items-center min-h-12 min-w-30 px-5 border-0 rounded-[0.7rem] text-[0.9375rem] font-semibold text-tb07-ink bg-tb07-fill disabled:bg-tb07-off disabled:text-tb07-muted disabled:cursor-not-allowed disabled:shadow-none">Disabled</button>
    <button type="button" aria-disabled="true" aria-describedby="tb-07-why" class="cursor-pointer grid place-items-center min-h-12 min-w-30 px-5 border-0 rounded-[0.7rem] text-[0.9375rem] font-semibold text-tb07-ink bg-tb07-fill aria-disabled:bg-tb07-off aria-disabled:text-tb07-muted aria-disabled:cursor-not-allowed aria-disabled:shadow-none aria-disabled:active:animate-tb07-nope focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb07-accent motion-reduce:aria-disabled:active:animate-none motion-reduce:aria-disabled:active:outline-2 motion-reduce:aria-disabled:active:outline-dashed motion-reduce:aria-disabled:active:outline-tb07-muted">Unavailable</button>
    <span id="tb-07-why" class="sr-only">Complete the form above to enable this action</span>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb07-bg: #f5f5f3;
  --color-tb07-bg: oklch(0.968 0.004 110);
  --color-tb07-accent: #0f766e;
  --color-tb07-accent: oklch(0.48 0.1 180);
  --color-tb07-fill: #0f766e;
  --color-tb07-fill: oklch(0.48 0.1 180);
  --color-tb07-fill-h: #0d6a62;
  --color-tb07-fill-h: oklch(0.44 0.1 180);
  --color-tb07-fill-a: #0b5a53;
  --color-tb07-fill-a: oklch(0.39 0.09 180);
  --color-tb07-off: #dcdcd8;
  --color-tb07-off: oklch(0.89 0.006 110);
  --color-tb07-muted: #4b5157;
  --color-tb07-muted: oklch(0.42 0.012 260);
  --color-tb07-ink: #ffffff;
  --color-tb07-glow: #0f766ed9;
  --color-tb07-glow: oklch(0.48 0.1 180 / 0.85);
  --font-tb07-sans: "Schibsted Grotesk", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb07-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb07-nope: tb-07-nope 0.32s cubic-bezier(0.36, 0.07, 0.19, 0.97);
}

@keyframes tb-07-nope {
  0%,
    100% {
    translate: 0 0;
  }

  25% {
    translate: -3px 0;
  }

  75% {
    translate: 3px 0;
  }
}
/* Demo-only: the data-force-* variants need a custom variant declaration. */

@custom-variant data-force-hover (&[data-force-hover]);

@custom-variant data-force-focus (&[data-force-focus]);

@custom-variant data-force-active (&[data-force-active]);

.tb-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}

@media (prefers-color-scheme: dark) {
  .tb-07:not([data-theme="light"]) {
    --color-tb07-bg: oklch(0.14 0.008 190);
    --color-tb07-fill: oklch(0.72 0.12 180);
    --color-tb07-fill-h: oklch(0.66 0.12 180);
    --color-tb07-fill-a: oklch(0.6 0.11 180);
    --color-tb07-off: oklch(0.28 0.008 190);
    --color-tb07-muted: oklch(0.8 0.01 190);
    --color-tb07-ink: oklch(0.18 0.04 180);
    --color-tb07-accent: oklch(0.72 0.12 180);
  }
}

.tb-07[data-theme="dark"] {
  --color-tb07-bg: oklch(0.14 0.008 190);
  --color-tb07-fill: oklch(0.72 0.12 180);
  --color-tb07-off: oklch(0.28 0.008 190);
  --color-tb07-muted: oklch(0.8 0.01 190);
  --color-tb07-ink: oklch(0.18 0.04 180);
}

@media (forced-colors: active) {
  .tb-07 button {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-07 button:disabled,
    .tb-07 button[aria-disabled="true"] {
    color: GrayText;
    border-color: GrayText;
  }
}
```
