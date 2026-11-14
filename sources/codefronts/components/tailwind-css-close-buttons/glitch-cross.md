---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/glitch-cross/"
title: "Glitch Effect Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "RGB-split glitch on a cyber-terminal button: the × is painted from two gradient bars stored in one arbitrary custom property, and two tinted ghost copies —…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Effect Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/glitch-cross/

RGB-split glitch on a cyber-terminal button: the × is painted from two gradient bars stored in one arbitrary custom property, and two tinted ghost copies — cyan and magenta via before:text-* and currentColor — jitter on desynced steps() tracks while clip-path: inset() tears them into scanlines. Keyframes live in @theme; the rest is markup.
## HTML
```html
<section class="tcb-16 w-full min-h-svh grid place-items-center bg-tcb16-bg bg-[radial-gradient(100%_110%_at_50%_0%,var(--color-tcb16-glow),transparent_60%)] px-6 py-12 font-tcb16-mono" aria-label="Glitch close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button type="button" aria-label="Close" class="group isolate grid size-18 cursor-pointer place-items-center rounded-xl border border-tcb16-c1/35 bg-tcb16-btn shadow-[0_0_0_1px_rgb(0_0_0/0.6),0_18px_40px_-20px_rgb(0_0_0/0.9)] transition-colors duration-200 hover:border-tcb16-c1 focus-visible:border-tcb16-c1 focus-visible:outline-[2.5px] focus-visible:outline-offset-3 focus-visible:outline-tcb16-c1 active:scale-93 motion-reduce:transition-none">
      <span aria-hidden="true" class="relative size-6.5 bg-(image:--tcb16-bars) text-white [--tcb16-bars:linear-gradient(45deg,transparent_calc(50%_-_1.25px),currentColor_calc(50%_-_1.25px)_calc(50%_+_1.25px),transparent_calc(50%_+_1.25px)),linear-gradient(-45deg,transparent_calc(50%_-_1.25px),currentColor_calc(50%_-_1.25px)_calc(50%_+_1.25px),transparent_calc(50%_+_1.25px))] before:absolute before:inset-0 before:bg-(image:--tcb16-bars) before:text-tcb16-c1 before:opacity-0 before:mix-blend-screen after:absolute after:inset-0 after:bg-(image:--tcb16-bars) after:text-tcb16-c2 after:opacity-0 after:mix-blend-screen group-hover:before:animate-tcb16-g1 group-hover:before:opacity-100 group-hover:after:animate-tcb16-g2 group-hover:after:opacity-100 group-focus-visible:before:animate-tcb16-g1 group-focus-visible:before:opacity-100 group-focus-visible:after:animate-tcb16-g2 group-focus-visible:after:opacity-100 motion-reduce:before:hidden motion-reduce:after:hidden"></span>
    </button>
    <p aria-hidden="true" class="rounded-md border border-tcb16-c1/25 px-3.5 py-2 text-[11.5px] text-tcb16-mut">bg-(image:--tcb16-bars) · before:mix-blend-screen · steps(2,jump-none)</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb16-bg: #0b0a14;
  --color-tcb16-bg: oklch(0.13 0.015 280);
  --color-tcb16-glow: #1c1a2ee6;
  --color-tcb16-glow: oklch(0.22 0.03 280 / 0.9);
  --color-tcb16-btn: #13121e;
  --color-tcb16-btn: oklch(0.17 0.02 280);
  --color-tcb16-c1: #3de6f2;
  --color-tcb16-c1: oklch(0.85 0.15 195);
  --color-tcb16-c2: #f0369b;
  --color-tcb16-c2: oklch(0.65 0.26 345);
  --color-tcb16-mut: #9cc9cf;
  --color-tcb16-mut: oklch(0.8 0.05 200);
  --font-tcb16-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tcb16-g1: tcb16-g1 0.32s steps(2, jump-none) infinite;
  --animate-tcb16-g2: tcb16-g2 0.44s steps(2, jump-none) infinite;

  @keyframes tcb16-g1 {
    0% {
      transform: translateX(-3px);
      clip-path: inset(0 0 62% 0);
    }

    23% {
      transform: translateX(2px);
      clip-path: inset(38% 0 21% 0);
    }

    41% {
      transform: translateX(-2px);
      clip-path: inset(71% 0 0 0);
    }

    67% {
      transform: translateX(3px);
      clip-path: inset(12% 0 55% 0);
    }

    100% {
      transform: translateX(-1px);
      clip-path: inset(45% 0 32% 0);
    }
  }

  @keyframes tcb16-g2 {
    0% {
      transform: translateX(3px);
      clip-path: inset(58% 0 8% 0);
    }

    19% {
      transform: translateX(-2px);
      clip-path: inset(9% 0 70% 0);
    }

    47% {
      transform: translateX(2px);
      clip-path: inset(33% 0 40% 0);
    }

    73% {
      transform: translateX(-3px);
      clip-path: inset(80% 0 2% 0);
    }

    100% {
      transform: translateX(1px);
      clip-path: inset(21% 0 48% 0);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-16 {
  width: 100%;
  min-height: 100svh;
}
```
