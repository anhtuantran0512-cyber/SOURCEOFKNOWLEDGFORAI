---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-brutalist-concrete-slab-button/"
title: "Tailwind Brutalist Concrete Slab Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Board-formed concrete: shutter lines from the timber mould, aggregate speckle through the mix, chipped corners cut by clip-path, and a press that drops the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Brutalist Concrete Slab Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-brutalist-concrete-slab-button/

Board-formed concrete: shutter lines from the timber mould, aggregate speckle through the mix, chipped corners cut by clip-path, and a press that drops the slab into its own shadow with a puff of dust at the base.
## HTML
```html
<div class="tb-30 w-full min-h-svh grid place-items-center font-tb30-black p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-30__slab group relative cursor-pointer grid place-items-center min-h-18 px-12 border-0 text-xl uppercase tracking-[0.06em] text-tb30-ink [clip-path:polygon(2.5%_0,100%_0,100%_88%,97%_100%,0_100%,0_9%)] [text-shadow:0_1px_0_#ffffff47,0_-1px_0_#0000004d] shadow-[0_8px_0_0_var(--color-tb30-grey-lo),0_16px_22px_-8px_#00000080] transition-[translate,box-shadow,filter] duration-100 ease-linear hover:brightness-105 active:translate-y-2 active:shadow-[0_0_0_0_var(--color-tb30-grey-lo),0_4px_8px_-4px_#00000080] focus-visible:outline-4 focus-visible:outline-offset-[6px] focus-visible:outline-tb30-ink disabled:cursor-not-allowed disabled:grayscale-50 disabled:brightness-[0.85] disabled:shadow-[0_4px_0_0_var(--color-tb30-grey-lo)] motion-reduce:transition-none">
    <span aria-hidden="true" class="absolute left-1/2 -bottom-1.5 w-36 h-4.5 -ml-18 rounded-[50%] pointer-events-none opacity-0 blur-[4px] bg-[radial-gradient(closest-side,rgba(255,255,255,0.85),transparent_72%)] group-active:animate-tb30-dust motion-reduce:hidden"></span>
    <span class="relative z-20">Pour it</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb30-bg: #c9c6c0;
  --color-tb30-bg: oklch(0.82 0.004 85);
  --color-tb30-grey: #8f8d88;
  --color-tb30-grey: oklch(0.62 0.004 85);
  --color-tb30-grey-hi: #a8a6a1;
  --color-tb30-grey-hi: oklch(0.7 0.004 85);
  --color-tb30-grey-lo: #5d5b57;
  --color-tb30-grey-lo: oklch(0.44 0.004 85);
  --color-tb30-fleck: #e6e3dc;
  --color-tb30-fleck: oklch(0.91 0.004 85);
  --color-tb30-fleck-2: #54524e;
  --color-tb30-fleck-2: oklch(0.4 0.004 85);
  --color-tb30-ink: #141412;
  --color-tb30-ink: oklch(0.16 0.004 85);
  --font-tb30-black: "Archivo Black", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --animate-tb30-dust: tb-30-dust 0.55s ease-out;
}

@keyframes tb-30-dust {
  0% {
    opacity: 0.85;
    scale: 0.4 0.5;
  }

  100% {
    opacity: 0;
    scale: 1.5 1.3;
  }
}

.tb-30 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: repeating-linear-gradient(0deg, rgba(0,0,0,.035) 0 1px, transparent 1px 22px), var(--color-tb30-bg);
}
/* THE MIX: three aggregate tiles (13/19/29px), the 14px formwork rhythm, and the
   cast base. Five layers whose sizes only mean anything together. */

.tb-30__slab {
  background-color: var(--color-tb30-grey);
  background-image: radial-gradient(.055rem .055rem at 18% 32%, color-mix(in oklab, var(--color-tb30-fleck) 55%, transparent) 99%, transparent), radial-gradient(.045rem .045rem at 62% 71%, color-mix(in oklab, var(--color-tb30-fleck-2) 45%, transparent) 99%, transparent), radial-gradient(.04rem .04rem at 84% 18%, color-mix(in oklab, var(--color-tb30-fleck) 40%, transparent) 99%, transparent), repeating-linear-gradient(0deg, rgba(0,0,0,.07) 0 1px, transparent 1px 14px), linear-gradient(168deg, var(--color-tb30-grey-hi), var(--color-tb30-grey) 55%, var(--color-tb30-grey-lo));
  background-size: 13px 13px, 19px 19px, 29px 29px, 100% 100%, 100% 100%;
}

@media (prefers-color-scheme: dark) {
  .tb-30:not([data-theme="light"]) {
    --color-tb30-bg: oklch(0.26 0.004 85);
    --color-tb30-grey: oklch(0.38 0.004 85);
    --color-tb30-grey-hi: oklch(0.44 0.004 85);
    --color-tb30-grey-lo: oklch(0.26 0.004 85);
    --color-tb30-fleck: oklch(0.62 0.004 85);
    --color-tb30-fleck-2: oklch(0.22 0.004 85);
    --color-tb30-ink: oklch(0.95 0.004 85);
  }
}

.tb-30[data-theme="dark"] {
  --color-tb30-bg: oklch(0.26 0.004 85);
  --color-tb30-grey: oklch(0.38 0.004 85);
  --color-tb30-grey-lo: oklch(0.26 0.004 85);
  --color-tb30-ink: oklch(0.95 0.004 85);
}

@media (forced-colors: active) {
  .tb-30__slab {
    background: ButtonFace;
    color: ButtonText;
    border: 2px solid ButtonText;
    box-shadow: none;
    text-shadow: none;
    clip-path: none;
  }

  .tb-30__slab span[aria-hidden] {
    display: none;
  }
}
```
