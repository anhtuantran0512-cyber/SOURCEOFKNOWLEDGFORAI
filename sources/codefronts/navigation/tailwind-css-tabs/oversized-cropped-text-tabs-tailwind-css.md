---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/oversized-cropped-text-tabs-tailwind-css/"
title: "Oversized Cropped Text Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "The active tab's word swells from a compact 15px label to 46px display type and is cropped by its own cell — the word overruns the box and the box cuts it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Oversized Cropped Text Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/oversized-cropped-text-tabs-tailwind-css/

The active tab's word swells from a compact 15px label to 46px display type and is cropped by its own cell — the word overruns the box and the box cuts it. Instrument Serif gives the crop a sharp editorial edge; a thin ruled frame keeps the strip reading like a specimen sheet.
## HTML
```html
<section class="ttb-14 group/tabs grid min-h-svh w-full place-items-center bg-ttb14-bg px-5 py-14 font-ttb14-serif text-ttb14-paper" aria-label="Oversized cropped text tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full">
      <div role="radiogroup" aria-label="Mode" class="flex border-y border-ttb14-paper/20">
        <label class="group/tab relative h-18 flex-1 cursor-pointer overflow-hidden border-r border-ttb14-paper/15 has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb14-paper"><input class="sr-only" type="radio" name="ttb14" id="ttb14-r1" checked><span class="absolute top-1/2 left-1/2 -translate-1/2 text-[15px] whitespace-nowrap text-ttb14-mut transition-[font-size,color] duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] group-hover/tab:text-ttb14-paper group-has-checked/tab:text-[46px] group-has-checked/tab:text-ttb14-paper motion-reduce:transition-none">Design</span></label>
        <label class="group/tab relative h-18 flex-1 cursor-pointer overflow-hidden border-r border-ttb14-paper/15 has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb14-paper"><input class="sr-only" type="radio" name="ttb14" id="ttb14-r2"><span class="absolute top-1/2 left-1/2 -translate-1/2 text-[15px] whitespace-nowrap text-ttb14-mut transition-[font-size,color] duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] group-hover/tab:text-ttb14-paper group-has-checked/tab:text-[46px] group-has-checked/tab:text-ttb14-paper motion-reduce:transition-none">Code</span></label>
        <label class="group/tab relative h-18 flex-1 cursor-pointer overflow-hidden has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb14-paper"><input class="sr-only" type="radio" name="ttb14" id="ttb14-r3"><span class="absolute top-1/2 left-1/2 -translate-1/2 text-[15px] whitespace-nowrap text-ttb14-mut transition-[font-size,color] duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] group-hover/tab:text-ttb14-paper group-has-checked/tab:text-[46px] group-has-checked/tab:text-ttb14-paper italic motion-reduce:transition-none">Preview</span></label>
      </div>
      <div class="px-1 pt-4 font-ttb14-mono text-[12.5px] leading-relaxed text-ttb14-mut">
        <p class="hidden group-has-[#ttb14-r1:checked]/tabs:block">01 — Tokens, components, motion.</p>
        <p class="hidden group-has-[#ttb14-r2:checked]/tabs:block">02 — Modern CSS, zero dependencies.</p>
        <p class="hidden group-has-[#ttb14-r3:checked]/tabs:block">03 — Live, with every state.</p>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb14-paper/15 px-3.5 py-2 font-ttb14-mono text-[11.5px] text-ttb14-mut">overflow-hidden cell · text-[15px] → text-[46px]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb14-bg: #161616;
  --color-ttb14-bg: oklch(0.200 0 0);
  --color-ttb14-paper: #ece6d4;
  --color-ttb14-paper: oklch(0.925 0.025 91.6);
  --color-ttb14-mut: #a8a293;
  --color-ttb14-mut: oklch(0.713 0.022 88.8);
  --font-ttb14-serif: 'Instrument Serif', Georgia, serif;
  --font-ttb14-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-14 {
  width: 100%;
  min-height: 100svh;
}
```
