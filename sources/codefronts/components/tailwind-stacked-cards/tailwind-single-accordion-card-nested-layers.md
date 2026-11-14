---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-single-accordion-card-nested-layers/"
title: "Tailwind Single Accordion Card Nested Layers"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Three panels inside one card whose height never changes."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Single Accordion Card Nested Layers
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-single-accordion-card-nested-layers/

Three panels inside one card whose height never changes. The open section takes the space by growing its flex, not by getting taller &mdash; has-checked:flex-1 &mdash; so nothing outside the card reflows and CLS stays at zero. The status dot is a before: utility rather than a pseudo-element rule, which is the small win: the dot's colour change is visible on the header it belongs to.
## HTML
```html
<section class="stk-21 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk21-sans bg-stk21-bg" aria-label="Single accordion card">
  <div class="flex w-[min(360px,100%)] h-80 flex-col overflow-hidden rounded-[20px] border border-stk21-line bg-stk21-card shadow-[0_26px_54px_-30px_rgba(0,0,0,0.8)]">
    <div class="flex flex-none min-h-0 flex-col transition-[flex-grow] duration-450 ease-stk21 has-checked:flex-1 motion-reduce:transition-none">
      <input class="peer sr-only" type="radio" name="stk-21" id="stk-21-1" checked>
      <label class="flex items-center gap-2.5 border-t border-stk21-div px-5.5 py-4.5 text-base font-extrabold text-stk21-dim cursor-pointer first:border-t-0 before:size-2.25 before:shrink-0 before:rounded-full before:bg-stk21-off before:transition-colors before:duration-300 peer-checked:text-white peer-checked:before:bg-stk21-c1 peer-focus-visible:outline-3 peer-focus-visible:outline-stk21-c1 peer-focus-visible:-outline-offset-3" for="stk-21-1">Overview</label>
      <div class="max-h-0 overflow-hidden opacity-0 transition-[max-height,opacity] duration-400 peer-checked:max-h-50 peer-checked:opacity-100 motion-reduce:transition-none">
        <p class="m-0 px-5.5 pb-5.5 text-sm leading-relaxed text-stk21-body">A pocket knife of a component &mdash; three panels, one fixed card, zero layout shift.</p>
      </div>
    </div>
    <div class="flex flex-none min-h-0 flex-col transition-[flex-grow] duration-450 ease-stk21 has-checked:flex-1 motion-reduce:transition-none">
      <input class="peer sr-only" type="radio" name="stk-21" id="stk-21-2">
      <label class="flex items-center gap-2.5 border-t border-stk21-div px-5.5 py-4.5 text-base font-extrabold text-stk21-dim cursor-pointer before:size-2.25 before:shrink-0 before:rounded-full before:bg-stk21-off before:transition-colors before:duration-300 peer-checked:text-white peer-checked:before:bg-stk21-c2 peer-focus-visible:outline-3 peer-focus-visible:outline-stk21-c2 peer-focus-visible:-outline-offset-3" for="stk-21-2">Features</label>
      <div class="max-h-0 overflow-hidden opacity-0 transition-[max-height,opacity] duration-400 peer-checked:max-h-50 peer-checked:opacity-100 motion-reduce:transition-none">
        <p class="m-0 px-5.5 pb-5.5 text-sm leading-relaxed text-stk21-body">Keyboard-navigable, reduced-motion aware, and copy-paste ready with namespaced tokens.</p>
      </div>
    </div>
    <div class="flex flex-none min-h-0 flex-col transition-[flex-grow] duration-450 ease-stk21 has-checked:flex-1 motion-reduce:transition-none">
      <input class="peer sr-only" type="radio" name="stk-21" id="stk-21-3">
      <label class="flex items-center gap-2.5 border-t border-stk21-div px-5.5 py-4.5 text-base font-extrabold text-stk21-dim cursor-pointer before:size-2.25 before:shrink-0 before:rounded-full before:bg-stk21-off before:transition-colors before:duration-300 peer-checked:text-white peer-checked:before:bg-stk21-c3 peer-focus-visible:outline-3 peer-focus-visible:outline-stk21-c3 peer-focus-visible:-outline-offset-3" for="stk-21-3">Usage</label>
      <div class="max-h-0 overflow-hidden opacity-0 transition-[max-height,opacity] duration-400 peer-checked:max-h-50 peer-checked:opacity-100 motion-reduce:transition-none">
        <p class="m-0 px-5.5 pb-5.5 text-sm leading-relaxed text-stk21-body">Drop the markup in, keep the <code class="rounded-[5px] bg-stk21-code px-1.25 py-0.5 font-stk21-mono text-xs">stk-21</code> namespace, and swap the copy. Done.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk21-bg: #101219;
  --color-stk21-bg: oklch(0.19 0.012 265);
  --color-stk21-card: #1b1e28;
  --color-stk21-card: oklch(0.24 0.014 265);
  --color-stk21-line: #2a2e3a;
  --color-stk21-line: oklch(0.32 0.016 265);
  --color-stk21-div: #262a36;
  --color-stk21-div: oklch(0.30 0.014 265);
  --color-stk21-code: #0f1117;
  --color-stk21-code: oklch(0.17 0.012 265);
  --color-stk21-off: #3a4050;
  --color-stk21-off: oklch(0.40 0.018 265);
  --color-stk21-dim: #c9cde0;
  --color-stk21-dim: oklch(0.85 0.018 265);
  --color-stk21-body: #aab0c2;
  --color-stk21-body: oklch(0.75 0.018 265);
  --color-stk21-c1: #e07a5f;
  --color-stk21-c1: oklch(0.66 0.16 20);
  --color-stk21-c2: #4bbd8c;
  --color-stk21-c2: oklch(0.68 0.15 150);
  --color-stk21-c3: #6a83e8;
  --color-stk21-c3: oklch(0.66 0.16 265);
  --font-stk21-sans: 'Archivo', system-ui, sans-serif;
  --font-stk21-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk21: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
