---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-clay-press-button/"
title: "Tailwind Clay Press Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Fat, matte, extruded clay: two inner shadows carve the highlight and the shade, an outer shadow grounds it, and pressing squashes the shape on both axes so…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Clay Press Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-clay-press-button/

Fat, matte, extruded clay: two inner shadows carve the highlight and the shade, an outer shadow grounds it, and pressing squashes the shape on both axes so it deforms like real material. The shadows swap direction on press — the whole demo is one shadow-[…] and its active: twin.
## HTML
```html
<div class="tb-18 w-full min-h-svh grid place-items-center font-tb18-sans p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="group cursor-pointer inline-grid grid-flow-col items-center gap-3 min-h-16 pl-5.5 pr-8 border-0 rounded-3xl text-[1.0625rem] font-extrabold tracking-[-0.01em] text-white bg-tb18-clay shadow-[inset_8px_8px_16px_var(--color-tb18-light),inset_-10px_-10px_20px_var(--color-tb18-shade),0_18px_32px_-16px_var(--color-tb18-ground)] transition-[translate,scale,box-shadow] duration-500 ease-tb18-spring [-webkit-tap-highlight-color:transparent] hover:-translate-y-[3px] active:translate-y-0.5 active:scale-x-[0.96] active:scale-y-[0.9] active:shadow-[inset_7px_7px_15px_var(--color-tb18-shade-press),inset_-7px_-7px_14px_var(--color-tb18-light-press),0_6px_12px_-10px_var(--color-tb18-ground)] focus-visible:outline-[3px] focus-visible:outline-tb18-ring focus-visible:outline-offset-[5px] disabled:cursor-not-allowed disabled:grayscale-[0.6] disabled:opacity-60 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
    <span aria-hidden="true" class="grid place-items-center size-8.5 rounded-full text-tb18-deep bg-tb18-chip shadow-[inset_3px_3px_6px_var(--color-tb18-light),inset_-3px_-3px_6px_var(--color-tb18-shade-chip)] transition-transform duration-500 ease-tb18-spring group-hover:rotate-90 motion-reduce:transition-none motion-reduce:group-hover:rotate-0">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="size-[1.05rem]"><path d="M12 5v14M5 12h14"/></svg>
    </span>
    <span>Make something</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb18-bg: #e8ecf7;
  --color-tb18-bg: oklch(0.935 0.02 265);
  --color-tb18-clay: #7c8cf8;
  --color-tb18-clay: oklch(0.68 0.16 275);
  --color-tb18-deep: #2a3480;
  --color-tb18-deep: oklch(0.35 0.14 275);
  --color-tb18-chip: #fbbf24;
  --color-tb18-chip: oklch(0.84 0.16 82);
  --color-tb18-ring: #3d4aa8;
  --color-tb18-ring: oklch(0.45 0.15 275);
  --color-tb18-light: #ffffff73;
  --color-tb18-light-press: #ffffff52;
  --color-tb18-shade: #2a34806b;
  --color-tb18-shade: oklch(0.35 0.14 275 / 0.42);
  --color-tb18-shade-press: #2a348061;
  --color-tb18-shade-press: oklch(0.35 0.14 275 / 0.38);
  --color-tb18-shade-chip: #2a34804d;
  --color-tb18-shade-chip: oklch(0.35 0.14 275 / 0.3);
  --color-tb18-ground: #2a3480a6;
  --color-tb18-ground: oklch(0.35 0.14 275 / 0.65);
  --font-tb18-sans: "Nunito", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb18-spring: cubic-bezier(0.16, 1, 0.3, 1);
}

@supports (transition-timing-function: linear(0, 1)) {
  @theme {
    --ease-tb18-spring: linear(0, 0.38 7%, 0.82 15%, 1.08 23%, 1.12 28%, 1.05 37%, 1 52%, 1);
  }
}

.tb-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(30rem 20rem at 50% 40%, #ffffff, transparent 70%), var(--color-tb18-bg);
}

@media (prefers-color-scheme: dark) {
  .tb-18:not([data-theme="light"]) {
    --color-tb18-bg: oklch(0.22 0.03 275);
    --color-tb18-clay: oklch(0.58 0.17 275);
    --color-tb18-deep: oklch(0.15 0.06 275);
    --color-tb18-light: #ffffff40;
    --color-tb18-light-press: #ffffff2e;
  }
}

.tb-18[data-theme="dark"] {
  --color-tb18-bg: oklch(0.22 0.03 275);
  --color-tb18-clay: oklch(0.58 0.17 275);
  --color-tb18-deep: oklch(0.15 0.06 275);
  --color-tb18-light: #ffffff40;
}

@media (forced-colors: active) {
  .tb-18 button {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-18 button span {
    box-shadow: none;
    border: 1px solid ButtonText;
  }
}
```
