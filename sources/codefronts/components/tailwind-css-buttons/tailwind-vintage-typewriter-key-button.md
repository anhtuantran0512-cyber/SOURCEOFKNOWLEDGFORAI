---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-vintage-typewriter-key-button/"
title: "Tailwind Vintage Typewriter Key Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A 1930s typewriter keycap on its chrome stem: a concave dished face, a nickel collar, and 5px of mechanical travel that collapses the stem's stacked shadows…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vintage Typewriter Key Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-vintage-typewriter-key-button/

A 1930s typewriter keycap on its chrome stem: a concave dished face, a nickel collar, and 5px of mechanical travel that collapses the stem's stacked shadows on press, so the key genuinely descends rather than sliding.
## HTML
```html
<div class="tb-24 w-full min-h-svh grid place-items-center font-tb24-slab p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="group relative cursor-pointer border-0 bg-transparent p-0 pb-[5px] text-tb24-ink [-webkit-tap-highlight-color:transparent] focus-visible:outline-none">
    <span class="tb-24__cap grid place-items-center min-w-26 min-h-14 px-5.5 py-2 rounded-[1.6rem] shadow-[inset_0_0_0_2px_var(--color-tb24-collar),inset_0_-2px_3px_#0000002e,0_1px_0_#b9b2a6,0_2px_0_#a79f93,0_3px_0_#948c81,0_4px_0_#7f776d,0_5px_0_#6a635b,0_12px_18px_-8px_#000000a6] transition-[translate,box-shadow] duration-100 group-hover:-translate-y-px group-active:translate-y-[5px] group-active:shadow-[inset_0_0_0_2px_var(--color-tb24-collar),inset_0_3px_6px_#0000004d,0_1px_0_#948c81,0_3px_6px_-3px_#00000099] group-focus-visible:outline-2 group-focus-visible:outline-offset-4 group-focus-visible:outline-tb24-ring group-disabled:grayscale-50 group-disabled:brightness-90 motion-reduce:transition-none">
      <span class="text-[1.0625rem] tracking-[0.12em] uppercase text-tb24-ink [text-shadow:0_1px_0_#ffffffa6]">Type</span>
    </span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb24-bg: #1d1a16;
  --color-tb24-bg: oklch(0.2 0.012 70);
  --color-tb24-cap: #efe9dc;
  --color-tb24-cap: oklch(0.93 0.016 88);
  --color-tb24-cap-lo: #cfc7b6;
  --color-tb24-cap-lo: oklch(0.82 0.02 88);
  --color-tb24-ink: #211d18;
  --color-tb24-ink: oklch(0.22 0.012 70);
  --color-tb24-collar: #c8c3ba;
  --color-tb24-collar: oklch(0.8 0.008 80);
  --color-tb24-ring: #d9b061;
  --color-tb24-ring: oklch(0.76 0.11 80);
  --font-tb24-slab: "Special Elite", ui-monospace, "Courier New", Courier, monospace;
}

.tb-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(36rem 22rem at 50% 38%, color-mix(in oklab, #f0e6cf 12%, transparent), transparent 70%), var(--color-tb24-bg);
}
/* THE DISHED FACE: scoop (dark, centre-bottom) + rim catch (light, top) over the
   cap gradient. A concave surface is a shading recipe, and it inverts rather than
   darkens in dark mode — which is why it lives here and not in a class list. */

.tb-24__cap {
  background: radial-gradient(120% 90% at 50% 118%, rgba(0,0,0,.16), transparent 58%), radial-gradient(120% 80% at 50% -14%, rgba(255,255,255,.75), transparent 60%), linear-gradient(180deg, var(--color-tb24-cap), var(--color-tb24-cap-lo));
}

@media (prefers-color-scheme: light) {
  .tb-24:not([data-theme="dark"]) {
    --color-tb24-bg: oklch(0.3 0.018 70);
  }
}

.tb-24[data-theme="light"] {
  --color-tb24-bg: oklch(0.3 0.018 70);
}

@media (forced-colors: active) {
  .tb-24__cap {
    background: ButtonFace;
    box-shadow: none;
    border: 1px solid ButtonText;
  }

  .tb-24__cap span {
    color: ButtonText;
    text-shadow: none;
  }
}
```
