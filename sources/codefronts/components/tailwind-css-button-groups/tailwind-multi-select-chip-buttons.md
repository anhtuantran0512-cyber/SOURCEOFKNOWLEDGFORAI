---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-multi-select-chip-buttons/"
title: "Tailwind Multi-Select Chip Buttons (Tag Filter Checkboxes with Count)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "Toggleable tag chips on hidden checkboxes, lit up with an acid-green neon glow when selected."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Select Chip Buttons (Tag Filter Checkboxes with Count)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-multi-select-chip-buttons/

Toggleable tag chips on hidden checkboxes, lit up with an acid-green neon glow when selected. Two genuinely useful additions run on pure HTML and CSS: a live “3 selected” count drawn with a CSS counter (checked:[counter-increment:tbg14] → after:content-[counter(tbg14)]), and a Clear button that is simply type="reset" on the surrounding form.
## HTML
```html
<section class="tbg-14 w-full min-h-svh grid place-items-center bg-tbg14-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-tbg14-glow),transparent_70%)] px-5 py-14 font-tbg14-sans text-tbg14-ink" aria-label="Multi-select chip buttons demo">
  <form class="grid w-full max-w-[36rem] gap-4 [counter-reset:tbg14]" onsubmit="return false">
    <fieldset class="grid gap-4">
      <legend class="mb-4 ml-0.5 font-tbg14-mono text-xs font-bold uppercase tracking-[0.14em] text-tbg14-acid">Stack — select all that apply</legend>
      <div class="flex flex-wrap gap-3">
        <label class="flex min-h-11 cursor-pointer items-center gap-2 rounded-full border-[1.5px] border-tbg14-line bg-white/3 px-4.5 text-[14.5px] font-semibold text-tbg14-mut transition-[color,border-color,background-color,box-shadow] duration-200 before:size-3.5 before:flex-none before:rounded-full before:border-2 before:border-tbg14-ring before:transition before:content-[''] hover:border-tbg14-hover hover:text-tbg14-ink has-checked:border-tbg14-acid has-checked:bg-tbg14-acid has-checked:text-tbg14-on has-checked:shadow-tbg14-glow has-checked:before:border-tbg14-on has-checked:before:bg-tbg14-on has-checked:before:shadow-[inset_0_0_0_2px_var(--color-tbg14-acid)] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white motion-reduce:transition-none"><input type="checkbox" name="stack" value="ts" class="sr-only checked:[counter-increment:tbg14]" checked>TypeScript</label>
        <label class="flex min-h-11 cursor-pointer items-center gap-2 rounded-full border-[1.5px] border-tbg14-line bg-white/3 px-4.5 text-[14.5px] font-semibold text-tbg14-mut transition-[color,border-color,background-color,box-shadow] duration-200 before:size-3.5 before:flex-none before:rounded-full before:border-2 before:border-tbg14-ring before:transition before:content-[''] hover:border-tbg14-hover hover:text-tbg14-ink has-checked:border-tbg14-acid has-checked:bg-tbg14-acid has-checked:text-tbg14-on has-checked:shadow-tbg14-glow has-checked:before:border-tbg14-on has-checked:before:bg-tbg14-on has-checked:before:shadow-[inset_0_0_0_2px_var(--color-tbg14-acid)] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white motion-reduce:transition-none"><input type="checkbox" name="stack" value="rust" class="sr-only checked:[counter-increment:tbg14]">Rust</label>
        <label class="flex min-h-11 cursor-pointer items-center gap-2 rounded-full border-[1.5px] border-tbg14-line bg-white/3 px-4.5 text-[14.5px] font-semibold text-tbg14-mut transition-[color,border-color,background-color,box-shadow] duration-200 before:size-3.5 before:flex-none before:rounded-full before:border-2 before:border-tbg14-ring before:transition before:content-[''] hover:border-tbg14-hover hover:text-tbg14-ink has-checked:border-tbg14-acid has-checked:bg-tbg14-acid has-checked:text-tbg14-on has-checked:shadow-tbg14-glow has-checked:before:border-tbg14-on has-checked:before:bg-tbg14-on has-checked:before:shadow-[inset_0_0_0_2px_var(--color-tbg14-acid)] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white motion-reduce:transition-none"><input type="checkbox" name="stack" value="webgpu" class="sr-only checked:[counter-increment:tbg14]" checked>WebGPU</label>
        <label class="flex min-h-11 cursor-pointer items-center gap-2 rounded-full border-[1.5px] border-tbg14-line bg-white/3 px-4.5 text-[14.5px] font-semibold text-tbg14-mut transition-[color,border-color,background-color,box-shadow] duration-200 before:size-3.5 before:flex-none before:rounded-full before:border-2 before:border-tbg14-ring before:transition before:content-[''] hover:border-tbg14-hover hover:text-tbg14-ink has-checked:border-tbg14-acid has-checked:bg-tbg14-acid has-checked:text-tbg14-on has-checked:shadow-tbg14-glow has-checked:before:border-tbg14-on has-checked:before:bg-tbg14-on has-checked:before:shadow-[inset_0_0_0_2px_var(--color-tbg14-acid)] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white motion-reduce:transition-none"><input type="checkbox" name="stack" value="edge" class="sr-only checked:[counter-increment:tbg14]">Edge Functions</label>
        <label class="flex min-h-11 cursor-pointer items-center gap-2 rounded-full border-[1.5px] border-tbg14-line bg-white/3 px-4.5 text-[14.5px] font-semibold text-tbg14-mut transition-[color,border-color,background-color,box-shadow] duration-200 before:size-3.5 before:flex-none before:rounded-full before:border-2 before:border-tbg14-ring before:transition before:content-[''] hover:border-tbg14-hover hover:text-tbg14-ink has-checked:border-tbg14-acid has-checked:bg-tbg14-acid has-checked:text-tbg14-on has-checked:shadow-tbg14-glow has-checked:before:border-tbg14-on has-checked:before:bg-tbg14-on has-checked:before:shadow-[inset_0_0_0_2px_var(--color-tbg14-acid)] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white motion-reduce:transition-none"><input type="checkbox" name="stack" value="vector" class="sr-only checked:[counter-increment:tbg14]">Vector DB</label>
        <label class="flex min-h-11 cursor-pointer items-center gap-2 rounded-full border-[1.5px] border-tbg14-line bg-white/3 px-4.5 text-[14.5px] font-semibold text-tbg14-mut transition-[color,border-color,background-color,box-shadow] duration-200 before:size-3.5 before:flex-none before:rounded-full before:border-2 before:border-tbg14-ring before:transition before:content-[''] hover:border-tbg14-hover hover:text-tbg14-ink has-checked:border-tbg14-acid has-checked:bg-tbg14-acid has-checked:text-tbg14-on has-checked:shadow-tbg14-glow has-checked:before:border-tbg14-on has-checked:before:bg-tbg14-on has-checked:before:shadow-[inset_0_0_0_2px_var(--color-tbg14-acid)] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-white motion-reduce:transition-none"><input type="checkbox" name="stack" value="wasm" class="sr-only checked:[counter-increment:tbg14]" checked>WASM</label>
      </div>
    </fieldset>
    <div class="flex items-center justify-between gap-4 border-t border-tbg14-line pt-4">
      <p aria-hidden="true" class="font-tbg14-mono text-[13px] text-tbg14-mut"><span class="font-bold text-tbg14-acid after:content-[counter(tbg14)]"></span> selected</p>
      <button type="reset" class="min-h-11 cursor-pointer rounded-full px-4 text-[14px] font-semibold text-tbg14-mut transition hover:bg-white/6 hover:text-tbg14-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white">Reset</button>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg14-bg: #050703;
  --color-tbg14-glow: #10170b;
  --color-tbg14-ink: #e6f2da;
  --color-tbg14-mut: #9eae92;
  --color-tbg14-mut: oklch(0.73 0.04 135);
  --color-tbg14-line: #253019;
  --color-tbg14-ring: #4a5c36;
  --color-tbg14-hover: #4a5f2f;
  --color-tbg14-on: #0a1204;
  --color-tbg14-acid: #b6f23a;
  --color-tbg14-acid: oklch(0.89 0.22 128);
  --shadow-tbg14-glow: 0 0 0 1px var(--color-tbg14-acid), 0 0 22px -2px var(--color-tbg14-acid), 0 0 46px 2px color-mix(in oklab, var(--color-tbg14-acid) 45%, transparent);
  --font-tbg14-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tbg14-mono: 'Space Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-14 {
  width: 100%;
  min-height: 100svh;
}
```
