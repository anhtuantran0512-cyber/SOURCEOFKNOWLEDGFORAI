---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-squash-and-stretch-pebble-toggle/"
title: "Tailwind Squash-and-Stretch Pebble Toggle"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A river pebble instead of a circle: the asymmetric blob squashes as it launches, stretches mid-flight and wobbles back into shape on landing."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Squash-and-Stretch Pebble Toggle
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-squash-and-stretch-pebble-toggle/

A river pebble instead of a circle: the asymmetric blob squashes as it launches, stretches mid-flight and wobbles back into shape on landing. Two --animate-* tokens &mdash; one for checking, one for unchecking &mdash; because a transition cannot sequence anticipate &rarr; stretch &rarr; settle.
## HTML
```html
<section class="ttg-25 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg25-bg font-ttg25-sans" aria-label="Bouncy pebble organic toggle">
  <label for="ttg-25-sw" class="flex items-center gap-8 px-7 py-5 rounded-[22px] cursor-pointer bg-ttg25-card shadow-[0_12px_30px_-20px_oklch(0.45_0.04_95/0.55)]">
    <span class="flex flex-col gap-0.5">
      <span class="text-[15.5px] font-semibold text-ttg25-ink">Rain sounds</span>
      <span class="text-[12.5px] text-ttg25-mute">Loops quietly while you write</span>
    </span>
    <input type="checkbox" id="ttg-25-sw" role="switch" class="appearance-none shrink-0 w-21 h-11 rounded-[26px] bg-ttg25-off relative cursor-pointer transition-colors duration-500 checked:bg-ttg25-on before:content-[''] before:absolute before:top-[5px] before:left-[5px] before:w-8.5 before:h-8.5 before:bg-ttg25-pebble before:shadow-[0_3px_7px_oklch(0.45_0.04_95/0.4)] before:rounded-[40%_60%_55%_45%/55%_45%_60%_40%] before:animate-ttg25-back checked:before:rounded-[60%_40%_45%_55%/45%_55%_40%_60%] checked:before:animate-ttg25-go focus-visible:outline-3 focus-visible:outline-ttg25-on focus-visible:outline-offset-4 motion-reduce:before:animate-none motion-reduce:checked:before:translate-x-[38px]">
  </label>
  <p class="text-[12px] tracking-[0.12em] uppercase text-ttg25-mute">Squash &middot; stretch &middot; wobble</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg25-bg: #e8e2d3;
  --color-ttg25-bg: oklch(0.91 0.02 95);
  --color-ttg25-card: #f4f0e4;
  --color-ttg25-card: oklch(0.95 0.015 95);
  --color-ttg25-off: #d3ccb8;
  --color-ttg25-off: oklch(0.85 0.025 95);
  --color-ttg25-on: #4e8f63;
  --color-ttg25-on: oklch(0.58 0.11 155);
  --color-ttg25-pebble: #f9f6ee;
  --color-ttg25-pebble: oklch(0.97 0.008 95);
  --color-ttg25-ink: #44412f;
  --color-ttg25-ink: oklch(0.37 0.02 100);
  --color-ttg25-mute: #857d64;
  --color-ttg25-mute: oklch(0.58 0.025 95);
  --font-ttg25-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-ttg25-go: ttg25-go 0.55s cubic-bezier(0.3, 0.7, 0.4, 1) forwards;
  --animate-ttg25-back: ttg25-back 0.55s cubic-bezier(0.3, 0.7, 0.4, 1) forwards;
}

@keyframes ttg25-go {
  0% {
    transform: translateX(0) scale(1, 1);
  }

  15% {
    transform: translateX(-3px) scale(0.85, 1.12);
  }

  45% {
    transform: translateX(20px) scale(1.28, 0.76);
  }

  70% {
    transform: translateX(38px) scale(0.9, 1.08);
  }

  85% {
    transform: translateX(38px) scale(1.06, 0.95);
  }

  100% {
    transform: translateX(38px) scale(1, 1);
  }
}

@keyframes ttg25-back {
  0% {
    transform: translateX(38px) scale(1, 1);
  }

  15% {
    transform: translateX(41px) scale(0.85, 1.12);
  }

  45% {
    transform: translateX(18px) scale(1.28, 0.76);
  }

  70% {
    transform: translateX(0) scale(0.9, 1.08);
  }

  85% {
    transform: translateX(0) scale(1.06, 0.95);
  }

  100% {
    transform: translateX(0) scale(1, 1);
  }
}

.ttg-25 {
  width: 100%;
  min-height: 100svh;
}

.ttg-25 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
