---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-vintage-calculator-key-button/"
title: "Tailwind Vintage Calculator Key Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A 1974 desk calculator key: warm beige ABS with a dished top, a chamfered skirt, tight 3px travel, and the orange function key beside it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vintage Calculator Key Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-vintage-calculator-key-button/

A 1974 desk calculator key: warm beige ABS with a dished top, a chamfered skirt, tight 3px travel, and the orange function key beside it. The dish is two counter-facing radial gradients, and the press collapses a hard shadow stack so it lands with a stop.
## HTML
```html
<div class="tb-47 w-full min-h-svh grid place-items-center font-tb47-sans p-[clamp(1.5rem,6vw,4rem)]">
  <div class="tb-47__pad flex gap-3 p-3.5 rounded-lg shadow-[inset_0_1px_0_#ffffff29,inset_0_-2px_5px_#00000073,0_16px_26px_-14px_#000000b3]">
    <button type="button" class="tb-47__key cursor-pointer grid place-items-center min-w-22 min-h-14 px-5 border-0 rounded-t-[0.3rem] rounded-b-[0.45rem] text-[0.9375rem] font-medium tracking-[0.12em] uppercase text-tb47-ink [text-shadow:0_1px_0_#ffffff8c] shadow-[inset_0_1px_0_#ffffff80,inset_0_-1px_0_#0000001f,0_1px_0_var(--color-tb47-skirt),0_2px_0_var(--color-tb47-skirt-lo),0_3px_0_var(--color-tb47-skirt-lo),0_7px_11px_-5px_#00000073] transition-[translate,box-shadow,filter] duration-[80ms] ease-linear [-webkit-tap-highlight-color:transparent] hover:brightness-105 active:translate-y-[3px] active:shadow-[inset_0_1px_3px_#00000047,0_1px_0_var(--color-tb47-skirt-lo),0_2px_4px_-2px_#00000073] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb47-accent disabled:cursor-not-allowed disabled:grayscale-50 disabled:brightness-95 motion-reduce:transition-none">Total</button>
    <button type="button" class="tb-47__key tb-47__key--accent cursor-pointer grid place-items-center min-w-14 min-h-14 px-5 border-0 rounded-t-[0.3rem] rounded-b-[0.45rem] text-[0.9375rem] font-medium tracking-[0.12em] uppercase text-tb47-accent-ink [text-shadow:0_1px_0_#00000059] shadow-[inset_0_1px_0_#ffffff59,inset_0_-1px_0_#00000040,0_1px_0_#a4400f,0_2px_0_#8d370c,0_3px_0_#8d370c,0_7px_11px_-5px_#00000080] transition-[translate,box-shadow,filter] duration-[80ms] ease-linear [-webkit-tap-highlight-color:transparent] hover:brightness-105 active:translate-y-[3px] active:shadow-[inset_0_1px_3px_#00000066,0_1px_0_#8d370c,0_2px_4px_-2px_#00000080] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tb47-accent disabled:cursor-not-allowed disabled:grayscale-50 motion-reduce:transition-none">C</button>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb47-bg: #3d3a33;
  --color-tb47-bg: oklch(0.36 0.012 85);
  --color-tb47-panel: #57534a;
  --color-tb47-panel: oklch(0.46 0.015 85);
  --color-tb47-cap: #e0d8c6;
  --color-tb47-cap: oklch(0.89 0.022 88);
  --color-tb47-cap-lo: #cdc4ae;
  --color-tb47-cap-lo: oklch(0.83 0.026 86);
  --color-tb47-skirt: #b3a992;
  --color-tb47-skirt: oklch(0.73 0.03 88);
  --color-tb47-skirt-lo: #8d8471;
  --color-tb47-skirt-lo: oklch(0.6 0.028 88);
  --color-tb47-ink: #3a352b;
  --color-tb47-ink: oklch(0.32 0.02 85);
  --color-tb47-accent: #c2551f;
  --color-tb47-accent: oklch(0.56 0.17 43);
  --color-tb47-accent-lo: #a4400f;
  --color-tb47-accent-lo: oklch(0.47 0.16 43);
  --color-tb47-accent-ink: #fff3e6;
  --font-tb47-sans: "Oswald", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
}

.tb-47 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(30rem 20rem at 50% 42%, rgba(255,255,255,.06), transparent 72%), var(--color-tb47-bg);
}

.tb-47__pad {
  background: linear-gradient(180deg, color-mix(in oklab, var(--color-tb47-panel) 88%, white 6%), var(--color-tb47-panel));
}
/* THE DISH: dark at the top edge, light at the bottom, so the surface scoops
   toward the user. On dark themes these two stops must INVERT, not darken —
   which is why the recipe lives here rather than in a class list. */

.tb-47__key {
  background: radial-gradient(120% 100% at 50% -18%, rgba(0,0,0,.15), transparent 58%), radial-gradient(120% 90% at 50% 118%, rgba(255,255,255,.6), transparent 56%), linear-gradient(180deg, var(--color-tb47-cap-lo), var(--color-tb47-cap));
}

.tb-47__key--accent {
  background: radial-gradient(120% 100% at 50% -18%, rgba(0,0,0,.22), transparent 58%), radial-gradient(120% 90% at 50% 118%, rgba(255,255,255,.32), transparent 56%), linear-gradient(180deg, var(--color-tb47-accent-lo), var(--color-tb47-accent));
}

@media (prefers-color-scheme: dark) {
  .tb-47:not([data-theme="light"]) {
    --color-tb47-bg: oklch(0.24 0.01 85);
    --color-tb47-panel: oklch(0.32 0.012 85);
  }
}

.tb-47[data-theme="dark"] {
  --color-tb47-bg: oklch(0.24 0.01 85);
  --color-tb47-panel: oklch(0.32 0.012 85);
}

@media (forced-colors: active) {
  .tb-47__pad {
    background: Canvas;
    box-shadow: none;
    border: 1px solid CanvasText;
  }

  .tb-47__key {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
    text-shadow: none;
  }
}
```
