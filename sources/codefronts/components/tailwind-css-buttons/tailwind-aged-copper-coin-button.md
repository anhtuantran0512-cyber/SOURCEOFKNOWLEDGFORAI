---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-aged-copper-coin-button/"
title: "Tailwind Aged Copper Coin Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A struck copper coin with a milled edge, verdigris patina blooming in the low spots, and a real 3D flip to its reverse face."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Aged Copper Coin Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-aged-copper-coin-button/

A struck copper coin with a milled edge, verdigris patina blooming in the low spots, and a real 3D flip to its reverse face. v4 ships transform-3d, backface-hidden, perspective-* and rotate-y-* as utilities, so the entire flip construction ports — which it could not have done in v3.
## HTML
```html
<div class="tb-27 w-full min-h-svh grid place-items-center perspective-[900px] font-tb27-serif p-[clamp(1.5rem,6vw,4rem)]">
  <label class="group relative block cursor-pointer size-34 [-webkit-tap-highlight-color:transparent]">
    <input type="checkbox" aria-label="Flip the coin to see the reverse" class="sr-only">
    <span aria-hidden="true" class="relative block size-full transform-3d transition-[transform,translate] duration-[850ms] ease-tb27-out group-hover:-translate-y-[3px] group-active:scale-[0.97] group-has-checked:rotate-y-180 group-has-focus-visible:outline-2 group-has-focus-visible:outline-offset-[6px] group-has-focus-visible:outline-tb27-cu-hi group-has-focus-visible:rounded-full motion-reduce:transition-none">
      <span class="tb-27__face absolute inset-0 grid place-items-center isolate overflow-hidden rounded-full backface-hidden text-tb27-ink shadow-[inset_0_2px_4px_#ffffff59,inset_0_-3px_6px_#00000066,0_16px_26px_-12px_#000000b3]">
        <span class="absolute inset-0 z-20 rounded-full opacity-90 bg-[repeating-conic-gradient(from_0deg,var(--color-tb27-reed-hi)_0deg_1.5deg,var(--color-tb27-reed-lo)_1.5deg_3deg)] [mask-image:radial-gradient(farthest-side,transparent_calc(100%-6px),#000_calc(100%-6px))]"></span>
        <span class="tb-27__patina absolute inset-0 z-10 rounded-full opacity-55"></span>
        <span class="relative z-30 text-2xl font-bold tracking-[0.12em] tabular-nums [text-shadow:0_1px_0_#ffffff6b,0_-1px_0_#00000073]">1892</span>
      </span>
      <span class="tb-27__face absolute inset-0 grid place-items-center isolate overflow-hidden rounded-full backface-hidden rotate-y-180 text-tb27-ink shadow-[inset_0_2px_4px_#ffffff59,inset_0_-3px_6px_#00000066,0_16px_26px_-12px_#000000b3]">
        <span class="absolute inset-0 z-20 rounded-full opacity-90 bg-[repeating-conic-gradient(from_0deg,var(--color-tb27-reed-hi)_0deg_1.5deg,var(--color-tb27-reed-lo)_1.5deg_3deg)] [mask-image:radial-gradient(farthest-side,transparent_calc(100%-6px),#000_calc(100%-6px))]"></span>
        <span class="tb-27__patina absolute inset-0 z-10 rounded-full opacity-55"></span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="relative z-30 w-[36%] h-[36%] drop-shadow-[0_1px_0_#ffffff66]"><path d="M12 3.5 14.4 9l5.6.6-4.2 3.8 1.2 5.6L12 16.3 7 19l1.2-5.6L4 9.6 9.6 9 12 3.5z"/></svg>
      </span>
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb27-bg: #1c2420;
  --color-tb27-bg: oklch(0.24 0.02 160);
  --color-tb27-cu: #b06a3c;
  --color-tb27-cu: oklch(0.6 0.11 48);
  --color-tb27-cu-hi: #e8a76d;
  --color-tb27-cu-hi: oklch(0.78 0.1 62);
  --color-tb27-cu-lo: #6d3c1c;
  --color-tb27-cu-lo: oklch(0.4 0.09 45);
  --color-tb27-patina: #3f8f74;
  --color-tb27-patina: oklch(0.6 0.09 165);
  --color-tb27-ink: #33180a;
  --color-tb27-ink: oklch(0.26 0.06 45);
  --color-tb27-reed-hi: #dc9a63;
  --color-tb27-reed-hi: oklch(0.73 0.1 58);
  --color-tb27-reed-lo: #7d4623;
  --color-tb27-reed-lo: oklch(0.44 0.09 46);
  --font-tb27-serif: "Cinzel", ui-serif, Georgia, "Times New Roman", serif;
  --ease-tb27-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-27 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(34rem 22rem at 50% 42%, color-mix(in oklab, var(--color-tb27-cu) 16%, transparent), transparent 72%), var(--color-tb27-bg);
}
/* STRUCK METAL: two offset speculars over a diagonal base. */

.tb-27__face {
  background: radial-gradient(circle at 32% 26%, var(--color-tb27-cu-hi), transparent 52%), radial-gradient(circle at 70% 78%, var(--color-tb27-cu-lo), transparent 55%), linear-gradient(150deg, var(--color-tb27-cu), color-mix(in oklab, var(--color-tb27-cu) 78%, black));
}
/* PATINA: three blotches in the low spots, blended into the metal rather than
   painted on. color-burn has no utility form, and shouldn't. */

.tb-27__patina {
  mix-blend-mode: color-burn;
  background: radial-gradient(2.4rem 1.8rem at 22% 72%, var(--color-tb27-patina), transparent 70%), radial-gradient(1.8rem 2.2rem at 78% 30%, var(--color-tb27-patina), transparent 72%), radial-gradient(1.2rem 1rem at 58% 84%, var(--color-tb27-patina), transparent 70%);
}
/* Safari ≤15.3 mask shim. */

.tb-27 [class*="mask-image"] {
  -webkit-mask-image: radial-gradient(farthest-side, transparent calc(100% - 6px), #000 calc(100% - 6px));
}

@media (prefers-color-scheme: light) {
  .tb-27:not([data-theme="dark"]) {
    --color-tb27-bg: oklch(0.32 0.025 160);
  }
}

.tb-27[data-theme="light"] {
  --color-tb27-bg: oklch(0.32 0.025 160);
}

@media (forced-colors: active) {
  .tb-27__face {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-27__patina,
    .tb-27__face > span:first-child {
    display: none;
  }
}
```
