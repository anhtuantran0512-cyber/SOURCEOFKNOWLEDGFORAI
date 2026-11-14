---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-play-pause-button/"
title: "Tailwind Play Pause Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "One shape that morphs between a play triangle and two pause bars — no icon swap, no SVG."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Play Pause Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-play-pause-button/

One shape that morphs between a play triangle and two pause bars — no icon swap, no SVG. Both states are clip-path: polygon() with matching point counts, and Tailwind carries them as arbitrary utilities, which puts the play polygon and the pause polygon on the same line of markup for the first time.
## HTML
```html
<div class="tb-13 w-full min-h-svh grid place-items-center font-tb13-sans p-[clamp(1.5rem,6vw,4rem)]">
  <label class="group relative cursor-pointer grid place-items-center size-22 rounded-full bg-[linear-gradient(160deg,var(--color-tb13-surface-lift),var(--color-tb13-surface))] shadow-[inset_0_1px_0_var(--color-tb13-sheen),0_18px_40px_-18px_var(--color-tb13-glow)] transition-[scale,box-shadow] duration-[400ms] ease-tb13-out [-webkit-tap-highlight-color:transparent] hover:scale-105 active:scale-95 has-focus-visible:outline-2 has-focus-visible:outline-offset-[6px] has-focus-visible:outline-tb13-accent has-checked:shadow-[inset_0_1px_0_var(--color-tb13-sheen),0_22px_50px_-18px_var(--color-tb13-glow-2)] motion-reduce:transition-none motion-reduce:hover:scale-100">
    <input type="checkbox" aria-label="Play or pause the episode" class="sr-only">
    <span aria-hidden="true" class="absolute -inset-2 rounded-full opacity-[0.28] bg-[conic-gradient(from_0deg,transparent_0_55%,var(--color-tb13-accent-2),var(--color-tb13-accent),transparent)] [mask-image:radial-gradient(farthest-side,transparent_calc(100%-2.5px),#000_calc(100%-2.5px))] transition-opacity duration-[400ms] group-has-checked:opacity-100 group-has-checked:animate-tb13-spin motion-reduce:group-has-checked:animate-none"></span>
    <span aria-hidden="true" class="relative w-[42%] h-[42%] translate-x-[4%] transition-transform duration-500 ease-tb13-out group-has-checked:translate-x-0 motion-reduce:transition-none">
      <span class="absolute inset-0 bg-tb13-ink transition-[clip-path] duration-500 ease-tb13-out [clip-path:polygon(22%_6%,50%_24%,50%_76%,22%_94%)] group-has-checked:[clip-path:polygon(14%_6%,39%_6%,39%_94%,14%_94%)] motion-reduce:transition-none"></span>
      <span class="absolute inset-0 bg-tb13-ink transition-[clip-path] duration-500 ease-tb13-out [clip-path:polygon(50%_24%,90%_50%,90%_50%,50%_76%)] group-has-checked:[clip-path:polygon(61%_6%,86%_6%,86%_94%,61%_94%)] motion-reduce:transition-none"></span>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb13-bg: #0d0b14;
  --color-tb13-bg: oklch(0.14 0.02 295);
  --color-tb13-surface: #191426;
  --color-tb13-surface: oklch(0.22 0.04 295);
  --color-tb13-surface-lift: #221c33;
  --color-tb13-surface-lift: oklch(0.27 0.045 295);
  --color-tb13-ink: #f4f1ff;
  --color-tb13-ink: oklch(0.96 0.015 295);
  --color-tb13-accent: #c084fc;
  --color-tb13-accent: oklch(0.78 0.16 305);
  --color-tb13-accent-2: #38bdf8;
  --color-tb13-accent-2: oklch(0.78 0.13 222);
  --color-tb13-sheen: #ffffff33;
  --color-tb13-glow: #c084fcb3;
  --color-tb13-glow: oklch(0.78 0.16 305 / 0.7);
  --color-tb13-glow-2: #38bdf8cc;
  --color-tb13-glow-2: oklch(0.78 0.13 222 / 0.8);
  --font-tb13-sans: "Outfit", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb13-out: cubic-bezier(0.16, 1, 0.3, 1);
  --animate-tb13-spin: tb-13-spin 2.6s linear infinite;
}

@keyframes tb-13-spin {
  to {
    rotate: 1turn;
  }
}

.tb-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(40rem 26rem at 50% 45%, color-mix(in oklab, var(--color-tb13-accent) 16%, transparent), transparent 70%), var(--color-tb13-bg);
}
/* Safari ≤15.3 mask shim. */

.tb-13 [class*="mask-image"] {
  -webkit-mask-image: radial-gradient(farthest-side, transparent calc(100% - 2.5px), #000 calc(100% - 2.5px));
}

@media (prefers-color-scheme: light) {
  .tb-13:not([data-theme="dark"]) {
    --color-tb13-bg: oklch(0.95 0.02 295);
    --color-tb13-surface: #ffffff;
    --color-tb13-surface-lift: oklch(0.99 0.004 295);
    --color-tb13-ink: oklch(0.22 0.06 295);
    --color-tb13-accent: oklch(0.55 0.23 295);
    --color-tb13-accent-2: oklch(0.55 0.13 235);
  }
}

.tb-13[data-theme="light"] {
  --color-tb13-bg: oklch(0.95 0.02 295);
  --color-tb13-surface: #ffffff;
  --color-tb13-surface-lift: oklch(0.99 0.004 295);
  --color-tb13-ink: oklch(0.22 0.06 295);
  --color-tb13-accent: oklch(0.55 0.23 295);
}

@media (forced-colors: active) {
  .tb-13 label {
    border: 1px solid ButtonText;
    background: ButtonFace;
  }

  .tb-13 label span span {
    background: ButtonText;
  }

  .tb-13 label > span:first-of-type {
    display: none;
  }
}
```
