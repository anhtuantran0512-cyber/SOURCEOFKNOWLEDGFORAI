---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-ai-model-selector-button-group/"
title: "Tailwind AI Model Selector Button Group (LLM Model Picker with Badges)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "A model picker for AI products: radio cards with a provider badge, capability chips, context window and an animated check."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind AI Model Selector Button Group (LLM Model Picker with Badges)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-ai-model-selector-button-group/

A model picker for AI products: radio cards with a provider badge, capability chips, context window and an animated check. Each row sets one inline variable, --brand, and v4's variable shorthand does the rest — bg-(--brand) on the badge, has-checked:border-(--brand) on the row, and a color-mix() tint behind the selection — so every provider is selected in its own colour.
## HTML
```html
<section class="tbg-11 w-full min-h-svh grid place-items-center bg-tbg11-bg bg-linear-165 from-tbg11-bg to-tbg11-bg2 px-5 py-14 font-tbg11-sans text-tbg11-ink" aria-label="AI model selector demo">
  <div class="w-full max-w-[32rem] rounded-[1.25rem] border border-tbg11-line bg-tbg11-panel px-5 pt-6 pb-5 shadow-tbg11-panel sm:px-6">
    <p class="text-xs font-bold uppercase tracking-[0.16em] text-tbg11-acc">Model</p>
    <h3 id="tbg11-title" class="mt-1 mb-4.5 text-[22px] font-bold tracking-[-0.02em]">Select a model</h3>
    <div role="radiogroup" aria-labelledby="tbg11-title" class="flex flex-col gap-2">
      <label style="--brand:#10a37f" class="group/row flex min-h-16 cursor-pointer items-center gap-3.5 rounded-2xl border-[1.5px] border-tbg11-rowline bg-tbg11-row px-4 py-3 transition-[border-color,background-color] duration-200 hover:border-tbg11-hover has-checked:border-(--brand) has-checked:bg-[color-mix(in_oklab,var(--brand)_12%,var(--color-tbg11-row))] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg11-acc motion-reduce:transition-none">
        <input type="radio" name="tbg11" class="sr-only" checked>
        <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-(--brand) text-[13px] font-extrabold text-white shadow-[0_4px_14px_-4px_var(--brand)]">AI</span>
        <span class="flex min-w-0 flex-col gap-1.5"><span class="text-[15px] font-semibold">GPT-class Turbo</span><span class="flex flex-wrap gap-1.5"><i class="rounded-md bg-tbg11-chip px-1.5 py-0.5 text-[10.5px] font-semibold not-italic text-tbg11-mut">Vision</i><i class="rounded-md bg-tbg11-chip px-1.5 py-0.5 text-[10.5px] font-semibold not-italic text-tbg11-mut">Tools</i></span></span>
        <span class="ml-auto font-tbg11-mono text-xs whitespace-nowrap text-tbg11-mut">128K ctx</span>
        <span aria-hidden="true" class="grid size-6 flex-none scale-75 place-items-center rounded-full border-2 border-tbg11-hover text-white opacity-40 transition duration-200 ease-[cubic-bezier(.34,1.5,.5,1)] group-has-checked/row:scale-100 group-has-checked/row:border-(--brand) group-has-checked/row:bg-(--brand) group-has-checked/row:opacity-100 motion-reduce:transition-none"><svg class="opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>
      </label>
      <label style="--brand:#d97757" class="group/row flex min-h-16 cursor-pointer items-center gap-3.5 rounded-2xl border-[1.5px] border-tbg11-rowline bg-tbg11-row px-4 py-3 transition-[border-color,background-color] duration-200 hover:border-tbg11-hover has-checked:border-(--brand) has-checked:bg-[color-mix(in_oklab,var(--brand)_12%,var(--color-tbg11-row))] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg11-acc motion-reduce:transition-none">
        <input type="radio" name="tbg11" class="sr-only">
        <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-(--brand) text-[13px] font-extrabold text-white shadow-[0_4px_14px_-4px_var(--brand)]">CL</span>
        <span class="flex min-w-0 flex-col gap-1.5"><span class="text-[15px] font-semibold">Claude-class Opus</span><span class="flex flex-wrap gap-1.5"><i class="rounded-md bg-tbg11-chip px-1.5 py-0.5 text-[10.5px] font-semibold not-italic text-tbg11-mut">Vision</i><i class="rounded-md bg-tbg11-chip px-1.5 py-0.5 text-[10.5px] font-semibold not-italic text-tbg11-mut">Reasoning</i></span></span>
        <span class="ml-auto font-tbg11-mono text-xs whitespace-nowrap text-tbg11-mut">200K ctx</span>
        <span aria-hidden="true" class="grid size-6 flex-none scale-75 place-items-center rounded-full border-2 border-tbg11-hover text-white opacity-40 transition duration-200 ease-[cubic-bezier(.34,1.5,.5,1)] group-has-checked/row:scale-100 group-has-checked/row:border-(--brand) group-has-checked/row:bg-(--brand) group-has-checked/row:opacity-100 motion-reduce:transition-none"><svg class="opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>
      </label>
      <label style="--brand:#4285f4" class="group/row flex min-h-16 cursor-pointer items-center gap-3.5 rounded-2xl border-[1.5px] border-tbg11-rowline bg-tbg11-row px-4 py-3 transition-[border-color,background-color] duration-200 hover:border-tbg11-hover has-checked:border-(--brand) has-checked:bg-[color-mix(in_oklab,var(--brand)_12%,var(--color-tbg11-row))] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg11-acc motion-reduce:transition-none">
        <input type="radio" name="tbg11" class="sr-only">
        <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-(--brand) text-[13px] font-extrabold text-white shadow-[0_4px_14px_-4px_var(--brand)]">GM</span>
        <span class="flex min-w-0 flex-col gap-1.5"><span class="text-[15px] font-semibold">Gemini-class Pro</span><span class="flex flex-wrap gap-1.5"><i class="rounded-md bg-tbg11-chip px-1.5 py-0.5 text-[10.5px] font-semibold not-italic text-tbg11-mut">Multimodal</i><i class="rounded-md bg-tbg11-chip px-1.5 py-0.5 text-[10.5px] font-semibold not-italic text-tbg11-mut">Long context</i></span></span>
        <span class="ml-auto font-tbg11-mono text-xs whitespace-nowrap text-tbg11-mut">1M ctx</span>
        <span aria-hidden="true" class="grid size-6 flex-none scale-75 place-items-center rounded-full border-2 border-tbg11-hover text-white opacity-40 transition duration-200 ease-[cubic-bezier(.34,1.5,.5,1)] group-has-checked/row:scale-100 group-has-checked/row:border-(--brand) group-has-checked/row:bg-(--brand) group-has-checked/row:opacity-100 motion-reduce:transition-none"><svg class="opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>
      </label>
      <label style="--brand:#8e6fe6" class="group/row flex min-h-16 cursor-pointer items-center gap-3.5 rounded-2xl border-[1.5px] border-tbg11-rowline bg-tbg11-row px-4 py-3 transition-[border-color,background-color] duration-200 hover:border-tbg11-hover has-checked:border-(--brand) has-checked:bg-[color-mix(in_oklab,var(--brand)_12%,var(--color-tbg11-row))] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg11-acc motion-reduce:transition-none">
        <input type="radio" name="tbg11" class="sr-only">
        <span aria-hidden="true" class="grid size-10 flex-none place-items-center rounded-xl bg-(--brand) text-[13px] font-extrabold text-white shadow-[0_4px_14px_-4px_var(--brand)]">LL</span>
        <span class="flex min-w-0 flex-col gap-1.5"><span class="text-[15px] font-semibold">Llama-class 70B</span><span class="flex flex-wrap gap-1.5"><i class="rounded-md bg-tbg11-chip px-1.5 py-0.5 text-[10.5px] font-semibold not-italic text-tbg11-mut">Open weights</i><i class="rounded-md bg-tbg11-chip px-1.5 py-0.5 text-[10.5px] font-semibold not-italic text-tbg11-mut">Fast</i></span></span>
        <span class="ml-auto font-tbg11-mono text-xs whitespace-nowrap text-tbg11-mut">64K ctx</span>
        <span aria-hidden="true" class="grid size-6 flex-none scale-75 place-items-center rounded-full border-2 border-tbg11-hover text-white opacity-40 transition duration-200 ease-[cubic-bezier(.34,1.5,.5,1)] group-has-checked/row:scale-100 group-has-checked/row:border-(--brand) group-has-checked/row:bg-(--brand) group-has-checked/row:opacity-100 motion-reduce:transition-none"><svg class="opacity-0 group-has-checked/row:opacity-100" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg11-bg: #0c1220;
  --color-tbg11-bg2: #0a0f1a;
  --color-tbg11-panel: #111827;
  --color-tbg11-line: #1f2b40;
  --color-tbg11-row: #0e1524;
  --color-tbg11-rowline: #1e2a3f;
  --color-tbg11-hover: #364866;
  --color-tbg11-chip: #1a2438;
  --color-tbg11-ink: #e8eefa;
  --color-tbg11-mut: #a3b4cf;
  --color-tbg11-mut: oklch(0.77 0.04 255);
  --color-tbg11-acc: #50b2f0;
  --color-tbg11-acc: oklch(0.73 0.13 235);
  --shadow-tbg11-panel: 0 34px 80px -40px rgb(0 0 0 / 0.9);
  --font-tbg11-sans: 'Geist', system-ui, sans-serif;
  --font-tbg11-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-11 {
  width: 100%;
  min-height: 100svh;
}
```
