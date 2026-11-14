---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-brutalist-glitch-button/"
title: "Tailwind Brutalist Glitch Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Neo-brutalist slab with a hard offset shadow that snaps flat when pressed, and a hover glitch built from two duplicate labels sliced by clip-path and pushed…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Brutalist Glitch Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-brutalist-glitch-button/

Neo-brutalist slab with a hard offset shadow that snaps flat when pressed, and a hover glitch built from two duplicate labels sliced by clip-path and pushed apart in cyan and magenta. Steps-based timing keeps it digital — no easing, no blur, no JavaScript.
## HTML
```html
<div class="tb-16 w-full min-h-svh grid place-items-center font-tb16-mono p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" data-label="Enter the archive" class="relative cursor-pointer grid place-items-center min-h-14 px-8 border-2 border-tb16-ink rounded-none text-[0.9375rem] font-bold uppercase tracking-[0.1em] text-tb16-ink bg-tb16-slab shadow-[6px_6px_0_0_var(--color-tb16-ink)] transition-[translate,box-shadow,background-color] duration-[120ms] ease-[steps(2,end)] before:content-[attr(data-label)] before:absolute before:inset-0 before:grid before:place-items-center before:px-8 before:whitespace-nowrap before:pointer-events-none before:opacity-0 before:text-tb16-ghost-1 before:[clip-path:inset(0_0_55%_0)] after:content-[attr(data-label)] after:absolute after:inset-0 after:grid after:place-items-center after:px-8 after:whitespace-nowrap after:pointer-events-none after:opacity-0 after:text-tb16-ghost-2 after:[clip-path:inset(55%_0_0_0)] hover:bg-tb16-accent hover:before:animate-tb16-a hover:after:animate-tb16-b focus-visible:bg-tb16-accent focus-visible:before:animate-tb16-a focus-visible:after:animate-tb16-b focus-visible:outline-[3px] focus-visible:outline-dashed focus-visible:outline-tb16-ink focus-visible:outline-offset-[5px] active:translate-x-1.5 active:translate-y-1.5 active:shadow-none disabled:cursor-not-allowed disabled:text-tb16-ink-off disabled:shadow-[6px_6px_0_0_var(--color-tb16-ink-off)] motion-reduce:transition-none motion-reduce:before:hidden motion-reduce:after:hidden">Enter the archive</button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb16-bg: #e8e6df;
  --color-tb16-bg: oklch(0.92 0.008 95);
  --color-tb16-slab: #f7f5ef;
  --color-tb16-slab: oklch(0.97 0.008 95);
  --color-tb16-ink: #0a0a0a;
  --color-tb16-ink: oklch(0.15 0 0);
  --color-tb16-ink-off: #7d7d78;
  --color-tb16-ink-off: oklch(0.58 0.004 95);
  --color-tb16-accent: #facc15;
  --color-tb16-accent: oklch(0.87 0.17 92);
  --color-tb16-ghost-1: #0e9aab;
  --color-tb16-ghost-1: oklch(0.63 0.11 205);
  --color-tb16-ghost-2: #d1214a;
  --color-tb16-ghost-2: oklch(0.52 0.2 12);
  --color-tb16-grid: #0a0a0a0d;
  --color-tb16-grid: oklch(0.15 0 0 / 0.05);
  --font-tb16-mono: "Space Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
}

@keyframes tb-16-a {
  0%,
    100% {
    translate: 0 0;
    opacity: 0;
  }

  20% {
    translate: -3px -2px;
    opacity: 1;
  }

  45% {
    translate: 4px 1px;
    opacity: 1;
    clip-path: inset(0 0 68% 0);
  }

  70% {
    translate: -2px 2px;
    opacity: 1;
    clip-path: inset(0 0 42% 0);
  }
}

@keyframes tb-16-b {
  0%,
    100% {
    translate: 0 0;
    opacity: 0;
  }

  25% {
    translate: 3px 2px;
    opacity: 1;
  }

  50% {
    translate: -4px -1px;
    opacity: 1;
    clip-path: inset(48% 0 0 0);
  }

  75% {
    translate: 2px -2px;
    opacity: 1;
    clip-path: inset(62% 0 0 0);
  }
}

@theme {
  --animate-tb16-a: tb-16-a 0.48s steps(2, end) infinite;
  --animate-tb16-b: tb-16-b 0.56s steps(2, end) infinite;
}
/* The graph-paper stage: two repeating gradients over the base. Scene, not component. */

.tb-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: repeating-linear-gradient(90deg, var(--color-tb16-grid) 0 1px, transparent 1px 3rem), repeating-linear-gradient(0deg, var(--color-tb16-grid) 0 1px, transparent 1px 3rem), var(--color-tb16-bg);
}

@media (prefers-color-scheme: dark) {
  .tb-16:not([data-theme="light"]) {
    --color-tb16-bg: oklch(0.16 0 0);
    --color-tb16-slab: oklch(0.22 0 0);
    --color-tb16-ink: oklch(0.96 0.006 95);
    --color-tb16-ink-off: oklch(0.55 0.004 95);
    --color-tb16-grid: oklch(0.96 0.006 95 / 0.06);
    --color-tb16-ghost-1: oklch(0.82 0.13 200);
    --color-tb16-ghost-2: oklch(0.7 0.2 12);
  }
}

.tb-16[data-theme="dark"] {
  --color-tb16-bg: oklch(0.16 0 0);
  --color-tb16-slab: oklch(0.22 0 0);
  --color-tb16-ink: oklch(0.96 0.006 95);
  --color-tb16-grid: oklch(0.96 0.006 95 / 0.06);
}

@media (forced-colors: active) {
  .tb-16 button {
    background: ButtonFace;
    color: ButtonText;
    border-color: ButtonText;
    box-shadow: 6px 6px 0 0 ButtonText;
  }

  .tb-16 button::before,
    .tb-16 button::after {
    display: none;
  }
}
```
