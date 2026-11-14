---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-tabs-subgrid-underline-indicator/"
title: "Tailwind Tab Button Group with Subgrid Underline Indicator"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "Dashboard tabs with a glowing underline that always matches each tab's exact width — because the underline row shares the tabs' columns through…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tab Button Group with Subgrid Underline Indicator
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-tabs-subgrid-underline-indicator/

Dashboard tabs with a glowing underline that always matches each tab's exact width — because the underline row shares the tabs' columns through grid-cols-subgrid. The CSS original moved one beam between columns, which can't animate; this port gives every column its own beam segment, so the old one shrinks out while the new one grows in &mdash; a smooth hand-off, still with zero JavaScript.
## HTML
```html
<section class="tbg-13 w-full min-h-svh grid place-items-center bg-tbg13-bg bg-linear-180 from-tbg13-bg to-tbg13-bg2 px-5 py-14 font-tbg13-sans text-tbg13-ink" aria-label="Subgrid underline tabs demo">
  <div class="w-full max-w-[38rem] overflow-x-auto pb-2">
    <div role="radiogroup" aria-label="Dashboard sections" class="group/tabs grid w-fit grid-cols-[repeat(4,auto)] gap-x-1.5 border-b border-white/8">
      <label class="relative row-start-1 flex min-h-12 cursor-pointer items-center gap-2 rounded-lg px-4.5 text-[15.5px] font-semibold [font-stretch:110%] text-tbg13-mut transition-colors duration-250 hover:text-tbg13-hover has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg13-acc"><input type="radio" name="tbg13" id="tbg13-1" class="sr-only" checked>Overview</label>
      <label class="relative row-start-1 flex min-h-12 cursor-pointer items-center gap-2 rounded-lg px-4.5 text-[15.5px] font-semibold [font-stretch:110%] text-tbg13-mut transition-colors duration-250 hover:text-tbg13-hover has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg13-acc"><input type="radio" name="tbg13" id="tbg13-2" class="sr-only">Analytics <span class="rounded-full bg-tbg13-acc/18 px-1.5 text-[11px] font-bold text-tbg13-acc">New</span></label>
      <label class="relative row-start-1 flex min-h-12 cursor-pointer items-center gap-2 rounded-lg px-4.5 text-[15.5px] font-semibold [font-stretch:110%] text-tbg13-mut transition-colors duration-250 hover:text-tbg13-hover has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg13-acc"><input type="radio" name="tbg13" id="tbg13-3" class="sr-only">Reports <span class="rounded-full bg-white/8 px-1.5 text-[11px] font-bold tabular-nums">3</span></label>
      <label class="relative row-start-1 flex min-h-12 cursor-pointer items-center gap-2 rounded-lg px-4.5 text-[15.5px] font-semibold [font-stretch:110%] text-tbg13-mut transition-colors duration-250 hover:text-tbg13-hover has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg13-acc"><input type="radio" name="tbg13" id="tbg13-4" class="sr-only">Settings</label>
      <div aria-hidden="true" class="col-span-full row-start-2 -mb-px grid h-[5px] grid-cols-subgrid not-supports-[grid-template-columns:subgrid]:grid-cols-4">
        <span class="scale-x-0 rounded-full bg-tbg13-acc opacity-0 shadow-tbg13-glow transition-[scale,opacity] duration-400 ease-[cubic-bezier(.3,.7,.3,1)] group-has-[#tbg13-1:checked]/tabs:scale-x-100 group-has-[#tbg13-1:checked]/tabs:opacity-100 motion-reduce:transition-none"></span>
        <span class="scale-x-0 rounded-full bg-tbg13-acc opacity-0 shadow-tbg13-glow transition-[scale,opacity] duration-400 ease-[cubic-bezier(.3,.7,.3,1)] group-has-[#tbg13-2:checked]/tabs:scale-x-100 group-has-[#tbg13-2:checked]/tabs:opacity-100 motion-reduce:transition-none"></span>
        <span class="scale-x-0 rounded-full bg-tbg13-acc opacity-0 shadow-tbg13-glow transition-[scale,opacity] duration-400 ease-[cubic-bezier(.3,.7,.3,1)] group-has-[#tbg13-3:checked]/tabs:scale-x-100 group-has-[#tbg13-3:checked]/tabs:opacity-100 motion-reduce:transition-none"></span>
        <span class="scale-x-0 rounded-full bg-tbg13-acc opacity-0 shadow-tbg13-glow transition-[scale,opacity] duration-400 ease-[cubic-bezier(.3,.7,.3,1)] group-has-[#tbg13-4:checked]/tabs:scale-x-100 group-has-[#tbg13-4:checked]/tabs:opacity-100 motion-reduce:transition-none"></span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg13-bg: #12100e;
  --color-tbg13-bg2: #191510;
  --color-tbg13-ink: #f4ede4;
  --color-tbg13-mut: #a79c90;
  --color-tbg13-mut: oklch(0.7 0.02 70);
  --color-tbg13-hover: #e1d7ca;
  --color-tbg13-acc: #ff7d2e;
  --color-tbg13-acc: oklch(0.72 0.19 45);
  --shadow-tbg13-glow: 0 0 16px 1px var(--color-tbg13-acc), 0 0 40px 2px color-mix(in oklab, var(--color-tbg13-acc) 60%, transparent);
  --font-tbg13-sans: 'Archivo', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-13 {
  width: 100%;
  min-height: 100svh;
}
```
