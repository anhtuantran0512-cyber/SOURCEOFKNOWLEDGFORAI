---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-neon-plasma-burst-button/"
title: "Tailwind Neon Plasma Burst Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A neon tube that idles at low current, floods with plasma on hover, and fires an expanding shock ring on press."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Plasma Burst Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-neon-plasma-burst-button/

A neon tube that idles at low current, floods with plasma on hover, and fires an expanding shock ring on press. The glow is layered text-shadow and box-shadow rather than a blur filter, so it stays crisp at any zoom — and both stacks are single arbitrary utilities, because a glow is one recipe, not six values.
## HTML
```html
<div class="tb-17 w-full min-h-svh grid place-items-center font-tb17-sans p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="group relative overflow-hidden isolate cursor-pointer min-h-14 px-8 border-0 rounded-[0.6rem] text-[0.9375rem] font-semibold uppercase tracking-[0.14em] text-tb17-tube bg-tb17-shell animate-tb17-flicker transition-[box-shadow,color,scale] duration-[350ms] ease-tb17-out [text-shadow:0_0_4px_var(--color-tb17-tube-90),0_0_12px_var(--color-tb17-tube-55),0_0_34px_var(--color-tb17-tube-30)] shadow-[inset_0_0_14px_var(--color-tb17-tube-20),0_0_0_1px_var(--color-tb17-tube-50),0_0_30px_-8px_var(--color-tb17-tube-40)] hover:text-tb17-hot hover:shadow-[inset_0_0_22px_var(--color-tb17-tube-32),0_0_0_1px_var(--color-tb17-tube-80),0_0_46px_-6px_var(--color-tb17-c2-60)] focus-visible:text-tb17-hot focus-visible:shadow-[inset_0_0_22px_var(--color-tb17-tube-32),0_0_0_1px_var(--color-tb17-tube-80),0_0_46px_-6px_var(--color-tb17-c2-60)] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb17-c1 active:scale-[0.97] motion-reduce:animate-none motion-reduce:transition-none">
    <span aria-hidden="true" class="absolute -inset-[40%] z-10 pointer-events-none opacity-30 blur-[16px] saturate-150 bg-[conic-gradient(from_var(--tb-17-a),var(--color-tb17-c1),var(--color-tb17-c2),var(--color-tb17-c3),var(--color-tb17-c1))] animate-tb17-spin transition-opacity duration-[400ms] group-hover:opacity-[0.62] group-hover:[animation-duration:3.2s] group-focus-visible:opacity-[0.62] motion-reduce:animate-none"></span>
    <span aria-hidden="true" class="absolute z-10 top-1/2 left-1/2 size-24 -mt-12 -ml-12 rounded-full border-2 border-tb17-c1 opacity-0 pointer-events-none group-active:animate-tb17-burst motion-reduce:hidden"></span>
    <span class="relative z-20">Initiate sequence</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@property --tb-17-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-tb17-bg: #05060a;
  --color-tb17-bg: oklch(0.1 0.015 265);
  --color-tb17-shell: #0b0d16;
  --color-tb17-shell: oklch(0.15 0.025 270);
  --color-tb17-tube: #22d3ee;
  --color-tb17-tube: oklch(0.82 0.14 200);
  --color-tb17-hot: #f4feff;
  --color-tb17-tube-90: #22d3eee6;
  --color-tb17-tube-90: oklch(0.82 0.14 200 / 0.9);
  --color-tb17-tube-80: #22d3eecc;
  --color-tb17-tube-80: oklch(0.82 0.14 200 / 0.8);
  --color-tb17-tube-55: #22d3ee8c;
  --color-tb17-tube-55: oklch(0.82 0.14 200 / 0.55);
  --color-tb17-tube-50: #22d3ee80;
  --color-tb17-tube-50: oklch(0.82 0.14 200 / 0.5);
  --color-tb17-tube-40: #22d3ee66;
  --color-tb17-tube-40: oklch(0.82 0.14 200 / 0.4);
  --color-tb17-tube-32: #22d3ee52;
  --color-tb17-tube-32: oklch(0.82 0.14 200 / 0.32);
  --color-tb17-tube-30: #22d3ee4d;
  --color-tb17-tube-30: oklch(0.82 0.14 200 / 0.3);
  --color-tb17-tube-20: #22d3ee33;
  --color-tb17-tube-20: oklch(0.82 0.14 200 / 0.2);
  --color-tb17-c1: #22d3ee;
  --color-tb17-c1: oklch(0.82 0.14 200);
  --color-tb17-c2: #a855f7;
  --color-tb17-c2: oklch(0.64 0.24 305);
  --color-tb17-c2-60: #a855f799;
  --color-tb17-c2-60: oklch(0.64 0.24 305 / 0.6);
  --color-tb17-c3: #f472b6;
  --color-tb17-c3: oklch(0.74 0.17 349);
  --font-tb17-sans: "Chakra Petch", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb17-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb17-flicker: tb-17-flicker 6s ease-in-out infinite;
  --animate-tb17-spin: tb-17-spin 7s linear infinite;
  --animate-tb17-burst: tb-17-burst 0.62s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes tb-17-flicker {
  0%,
    100% {
    opacity: 1;
  }

  48% {
    opacity: 0.94;
  }

  50% {
    opacity: 0.82;
  }

  52% {
    opacity: 0.97;
  }
}

@keyframes tb-17-spin {
  to {
    --tb-17-a: 360deg;
  }
}

@keyframes tb-17-burst {
  0% {
    opacity: 0.9;
    scale: 0.15;
  }

  100% {
    opacity: 0;
    scale: 3;
  }
}

.tb-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(44rem 26rem at 50% 50%, color-mix(in oklab, var(--color-tb17-c2) 12%, transparent), transparent 72%), var(--color-tb17-bg);
}

@media (prefers-color-scheme: light) {
  .tb-17:not([data-theme="dark"]) {
    --color-tb17-bg: oklch(0.12 0.02 270);
    --color-tb17-shell: oklch(0.16 0.03 272);
  }
}

.tb-17[data-theme="light"] {
  --color-tb17-bg: oklch(0.12 0.02 270);
  --color-tb17-shell: oklch(0.16 0.03 272);
}

@media (forced-colors: active) {
  .tb-17 button {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
    text-shadow: none;
  }

  .tb-17 button span[aria-hidden] {
    display: none;
  }
}
```
