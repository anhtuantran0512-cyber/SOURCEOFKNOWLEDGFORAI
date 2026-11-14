---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-like-heart-button/"
title: "Tailwind Like Heart Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A like button with a springy heart pop, eight radial sparks and a count that rolls over — no JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Like Heart Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-like-heart-button/

A like button with a springy heart pop, eight radial sparks and a count that rolls over — no JavaScript. State lives in a checkbox, and has-checked: turns every downstream reaction into a variant on the element that reacts.
## HTML
```html
<div class="tb-11 w-full min-h-svh grid place-items-center bg-tb11-bg text-tb11-text font-tb11-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <label class="group relative cursor-pointer inline-flex items-center gap-2 min-h-12 pl-3.5 pr-4 rounded-full bg-tb11-surface border border-tb11-line text-[0.9375rem] font-bold tabular-nums text-tb11-muted shadow-[0_8px_20px_-16px_var(--color-tb11-shadow)] transition-[border-color,color,scale,background-color] duration-250 ease-tb11-out [-webkit-tap-highlight-color:transparent] hover:border-tb11-like-line hover:text-tb11-text hover:scale-[1.02] active:scale-[0.97] has-focus-visible:outline-2 has-focus-visible:outline-offset-[3px] has-focus-visible:outline-tb11-like has-checked:text-tb11-like has-checked:border-tb11-like-line has-checked:bg-tb11-like-tint motion-reduce:transition-none motion-reduce:hover:scale-100">
    <input type="checkbox" aria-label="Like this post" class="sr-only">
    <span aria-hidden="true" class="relative grid place-items-center size-7 text-tb11-muted group-hover:text-tb11-like group-has-checked:text-tb11-like">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="size-6 transition-[scale,color,fill] duration-350 ease-tb11-out group-has-checked:fill-tb11-like group-has-checked:animate-tb11-pop motion-reduce:transition-none motion-reduce:group-has-checked:animate-none"><path d="M12 20.2s-7.4-4.3-7.4-9.4A4.3 4.3 0 0 1 12 8.1a4.3 4.3 0 0 1 7.4 2.7c0 5.1-7.4 9.4-7.4 9.4z"/></svg>
      <span class="absolute inset-0 pointer-events-none motion-reduce:hidden">
        <span class="absolute top-1/2 left-1/2 size-[0.28rem] -mt-[0.14rem] -ml-[0.14rem] rounded-full bg-tb11-like opacity-0 rotate-0 group-has-checked:animate-tb11-spark"></span>
        <span class="absolute top-1/2 left-1/2 size-[0.28rem] -mt-[0.14rem] -ml-[0.14rem] rounded-full bg-tb11-spark-warm opacity-0 rotate-45 group-has-checked:animate-tb11-spark"></span>
        <span class="absolute top-1/2 left-1/2 size-[0.28rem] -mt-[0.14rem] -ml-[0.14rem] rounded-full bg-tb11-like opacity-0 rotate-90 group-has-checked:animate-tb11-spark"></span>
        <span class="absolute top-1/2 left-1/2 size-[0.28rem] -mt-[0.14rem] -ml-[0.14rem] rounded-full bg-tb11-spark-warm opacity-0 rotate-[135deg] group-has-checked:animate-tb11-spark"></span>
        <span class="absolute top-1/2 left-1/2 size-[0.28rem] -mt-[0.14rem] -ml-[0.14rem] rounded-full bg-tb11-like opacity-0 rotate-180 group-has-checked:animate-tb11-spark"></span>
        <span class="absolute top-1/2 left-1/2 size-[0.28rem] -mt-[0.14rem] -ml-[0.14rem] rounded-full bg-tb11-spark-cool opacity-0 rotate-[225deg] group-has-checked:animate-tb11-spark"></span>
        <span class="absolute top-1/2 left-1/2 size-[0.28rem] -mt-[0.14rem] -ml-[0.14rem] rounded-full bg-tb11-like opacity-0 rotate-[270deg] group-has-checked:animate-tb11-spark"></span>
        <span class="absolute top-1/2 left-1/2 size-[0.28rem] -mt-[0.14rem] -ml-[0.14rem] rounded-full bg-tb11-spark-cool opacity-0 rotate-[315deg] group-has-checked:animate-tb11-spark"></span>
      </span>
    </span>
    <span aria-hidden="true" class="block h-5 overflow-hidden">
      <span class="tb-11__roll grid transition-[translate] duration-[550ms] ease-tb11-spring group-has-checked:-translate-y-5 motion-reduce:transition-none">
        <span class="block h-5 leading-5">2,417</span>
        <span class="block h-5 leading-5">2,418</span>
      </span>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb11-bg: #fbf7f7;
  --color-tb11-bg: oklch(0.976 0.006 15);
  --color-tb11-surface: #ffffff;
  --color-tb11-line: #eadfe0;
  --color-tb11-line: oklch(0.91 0.014 15);
  --color-tb11-text: #241a1c;
  --color-tb11-text: oklch(0.24 0.015 15);
  --color-tb11-muted: #6f6266;
  --color-tb11-muted: oklch(0.48 0.015 15);
  --color-tb11-like: #e11d48;
  --color-tb11-like: oklch(0.56 0.22 12);
  --color-tb11-like-line: #e11d4894;
  --color-tb11-like-line: oklch(0.56 0.22 12 / 0.55);
  --color-tb11-like-tint: #e11d4812;
  --color-tb11-like-tint: oklch(0.56 0.22 12 / 0.07);
  --color-tb11-spark-warm: #ef6a2a;
  --color-tb11-spark-warm: oklch(0.67 0.19 42);
  --color-tb11-spark-cool: #b13ba5;
  --color-tb11-spark-cool: oklch(0.55 0.21 330);
  --color-tb11-shadow: #241a1c99;
  --color-tb11-shadow: oklch(0.24 0.015 15 / 0.6);
  --font-tb11-sans: "Manrope", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb11-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-tb11-spring: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb11-pop: tb-11-pop 0.6s var(--ease-tb11-spring);
  --animate-tb11-spark: tb-11-spark 0.62s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@supports (transition-timing-function: linear(0, 1)) {
  @theme {
    --ease-tb11-spring: linear(0, 0.45 7%, 0.85 15%, 1.12 23%, 1.18 28%, 1.1 36%, 1 50%, 1);
  }
}

@keyframes tb-11-pop {
  0% {
    scale: 1;
  }

  22% {
    scale: 0.75;
  }

  55% {
    scale: 1.28;
  }

  100% {
    scale: 1;
  }
}

@keyframes tb-11-spark {
  0% {
    opacity: 0;
    scale: 0.3;
    translate: 0 0;
  }

  25% {
    opacity: 1;
    scale: 1.1;
  }

  100% {
    opacity: 0;
    scale: 0.5;
    translate: 0 -1.55rem;
  }
}

.tb-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}

@media (prefers-color-scheme: dark) {
  .tb-11:not([data-theme="light"]) {
    --color-tb11-bg: oklch(0.13 0.01 15);
    --color-tb11-surface: oklch(0.18 0.012 15);
    --color-tb11-line: oklch(0.28 0.015 15);
    --color-tb11-text: oklch(0.95 0.008 15);
    --color-tb11-muted: oklch(0.74 0.015 15);
    --color-tb11-like: oklch(0.72 0.17 12);
  }
}

.tb-11[data-theme="dark"] {
  --color-tb11-bg: oklch(0.13 0.01 15);
  --color-tb11-surface: oklch(0.18 0.012 15);
  --color-tb11-line: oklch(0.28 0.015 15);
  --color-tb11-text: oklch(0.95 0.008 15);
  --color-tb11-muted: oklch(0.74 0.015 15);
  --color-tb11-like: oklch(0.72 0.17 12);
}

@media (forced-colors: active) {
  .tb-11 label {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }

  .tb-11 label:has(input:checked) {
    background: Highlight;
    color: HighlightText;
  }

  .tb-11 label span span span {
    display: none;
  }
}
```
