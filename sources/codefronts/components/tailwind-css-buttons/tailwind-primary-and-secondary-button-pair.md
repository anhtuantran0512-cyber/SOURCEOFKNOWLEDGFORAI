---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-primary-and-secondary-button-pair/"
title: "Tailwind Primary and Secondary Button Pair"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "One shared recipe, two visual weights, and a container that stacks them when the slot is narrow — not when the viewport is."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Primary and Secondary Button Pair
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-primary-and-secondary-button-pair/

One shared recipe, two visual weights, and a container that stacks them when the slot is narrow — not when the viewport is. The port is the honest test of "utilities can't do variants": they can, and the shared part stays literally identical because both buttons carry the same twenty classes and differ in four.
## HTML
```html
<div class="tb-02 w-full min-h-svh grid place-items-center bg-tb02-bg text-tb02-text font-tb02-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <div class="@container w-[min(100%,26rem)] flex flex-wrap justify-center gap-3">
    <button type="button" class="cursor-pointer grid place-items-center min-h-12 px-6 border-0 rounded-xl text-[0.9375rem] font-semibold tracking-[-0.01em] transition-[translate,background-color,box-shadow] duration-200 ease-tb02-out focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tb02-accent disabled:cursor-not-allowed disabled:opacity-45 disabled:translate-y-0 hover:-translate-y-px active:translate-y-px motion-reduce:transition-none motion-reduce:hover:translate-y-0 @max-[22rem]:basis-full bg-tb02-accent text-tb02-on-accent hover:bg-tb02-accent-deep shadow-[0_8px_20px_-10px_var(--color-tb02-accent-glow)]">Start free trial</button>
    <button type="button" class="cursor-pointer grid place-items-center min-h-12 px-6 border-0 rounded-xl text-[0.9375rem] font-semibold tracking-[-0.01em] transition-[translate,background-color,box-shadow] duration-200 ease-tb02-out focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tb02-accent disabled:cursor-not-allowed disabled:opacity-45 disabled:translate-y-0 hover:-translate-y-px active:translate-y-px motion-reduce:transition-none motion-reduce:hover:translate-y-0 @max-[22rem]:basis-full bg-tb02-surface text-tb02-text inset-ring-1 inset-ring-tb02-line hover:bg-tb02-tint hover:inset-ring-tb02-line-strong">Book a demo</button>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb02-bg: #f6f6f4;
  --color-tb02-bg: oklch(0.97 0.003 90);
  --color-tb02-surface: #ffffff;
  --color-tb02-tint: #f0f0ee;
  --color-tb02-tint: oklch(0.95 0.003 90);
  --color-tb02-text: #141416;
  --color-tb02-text: oklch(0.16 0.01 285);
  --color-tb02-muted: #5f5f68;
  --color-tb02-muted: oklch(0.45 0.015 285);
  --color-tb02-line: #dcdcd6;
  --color-tb02-line: oklch(0.89 0.008 90);
  --color-tb02-line-strong: #b4b4ad;
  --color-tb02-line-strong: oklch(0.76 0.01 90);
  --color-tb02-accent: #4f39f6;
  --color-tb02-accent: oklch(0.51 0.23 279);
  --color-tb02-accent-deep: #4029d6;
  --color-tb02-accent-deep: oklch(0.45 0.22 279);
  --color-tb02-accent-glow: #4f39f6cc;
  --color-tb02-accent-glow: oklch(0.51 0.23 279 / 0.8);
  --color-tb02-on-accent: #ffffff;
  --font-tb02-sans: "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb02-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}

@media (prefers-color-scheme: dark) {
  .tb-02:not([data-theme="light"]) {
    --color-tb02-bg: oklch(0.14 0.008 285);
    --color-tb02-surface: oklch(0.2 0.008 285);
    --color-tb02-tint: oklch(0.25 0.008 285);
    --color-tb02-text: oklch(0.96 0.004 285);
    --color-tb02-line: oklch(0.32 0.01 285);
    --color-tb02-line-strong: oklch(0.45 0.01 285);
    --color-tb02-accent: oklch(0.7 0.16 279);
    --color-tb02-on-accent: oklch(0.15 0.06 279);
  }
}

.tb-02[data-theme="dark"] {
  --color-tb02-bg: oklch(0.14 0.008 285);
  --color-tb02-surface: oklch(0.2 0.008 285);
  --color-tb02-tint: oklch(0.25 0.008 285);
  --color-tb02-text: oklch(0.96 0.004 285);
  --color-tb02-line: oklch(0.32 0.01 285);
  --color-tb02-accent: oklch(0.7 0.16 279);
  --color-tb02-on-accent: oklch(0.15 0.06 279);
}

@media (forced-colors: active) {
  .tb-02 button {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-02 button:first-child {
    background: Highlight;
    color: HighlightText;
  }
}
```
