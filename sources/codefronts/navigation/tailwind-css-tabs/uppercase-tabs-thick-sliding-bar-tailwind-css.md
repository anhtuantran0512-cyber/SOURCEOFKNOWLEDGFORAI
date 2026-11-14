---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/uppercase-tabs-thick-sliding-bar-tailwind-css/"
title: "Uppercase Tabs with Thick Sliding Bar in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Tracked mono caps above a single heavy pressroom-red bar that slides like a bookmark along a typecase shelf."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Uppercase Tabs with Thick Sliding Bar in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/uppercase-tabs-thick-sliding-bar-tailwind-css/

Tracked mono caps above a single heavy pressroom-red bar that slides like a bookmark along a typecase shelf. The original measured each label's width; the port gives the four volumes equal columns and a second line of dates, so the bar steps by quarters with the index trick.
## HTML
```html
<section class="ttb-18 group/tabs grid min-h-svh w-full place-items-center bg-ttb18-bg px-5 py-14 font-ttb18-mono text-ttb18-paper" aria-label="Uppercase tabs with sliding bar demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full">
      <div role="radiogroup" aria-label="Volume" class="relative grid grid-cols-4 pb-4 [--i:0] has-[#ttb18-r2:checked]:[--i:1] has-[#ttb18-r3:checked]:[--i:2] has-[#ttb18-r4:checked]:[--i:3]">
        <label class="group/tab flex min-h-12 cursor-pointer flex-col justify-end gap-1 pr-2 transition-colors has-focus-visible:outline-1 has-focus-visible:outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-ttb18-paper"><input class="sr-only" type="radio" name="ttb18" id="ttb18-r1" checked><span class="text-[11px] font-bold tracking-[0.24em] text-ttb18-mut uppercase transition-colors group-hover/tab:text-ttb18-paper group-has-checked/tab:text-ttb18-paper">Vol. I</span><span class="text-[10.5px] text-ttb18-dim">1450–1600</span></label>
        <label class="group/tab flex min-h-12 cursor-pointer flex-col justify-end gap-1 pr-2 transition-colors has-focus-visible:outline-1 has-focus-visible:outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-ttb18-paper"><input class="sr-only" type="radio" name="ttb18" id="ttb18-r2"><span class="text-[11px] font-bold tracking-[0.24em] text-ttb18-mut uppercase transition-colors group-hover/tab:text-ttb18-paper group-has-checked/tab:text-ttb18-paper">Vol. II</span><span class="text-[10.5px] text-ttb18-dim">1600–1750</span></label>
        <label class="group/tab flex min-h-12 cursor-pointer flex-col justify-end gap-1 pr-2 transition-colors has-focus-visible:outline-1 has-focus-visible:outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-ttb18-paper"><input class="sr-only" type="radio" name="ttb18" id="ttb18-r3"><span class="text-[11px] font-bold tracking-[0.24em] text-ttb18-mut uppercase transition-colors group-hover/tab:text-ttb18-paper group-has-checked/tab:text-ttb18-paper">Vol. III</span><span class="text-[10.5px] text-ttb18-dim">1750–1900</span></label>
        <label class="group/tab flex min-h-12 cursor-pointer flex-col justify-end gap-1 pr-2 transition-colors has-focus-visible:outline-1 has-focus-visible:outline-offset-2 has-focus-visible:outline-dashed has-focus-visible:outline-ttb18-paper"><input class="sr-only" type="radio" name="ttb18" id="ttb18-r4"><span class="text-[11px] font-bold tracking-[0.24em] text-ttb18-mut uppercase transition-colors group-hover/tab:text-ttb18-paper group-has-checked/tab:text-ttb18-paper">Vol. IV</span><span class="text-[10.5px] text-ttb18-dim">1980–</span></label>
        <span aria-hidden="true" class="absolute bottom-0 left-0 h-px w-full bg-ttb18-paper/15"></span>
        <span aria-hidden="true" class="pointer-events-none absolute bottom-0 left-0 h-1.5 w-1/4 translate-x-[calc(var(--i)*100%)] bg-ttb18-red transition-transform duration-450 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:transition-none"></span>
      </div>
      <div class="pt-5 font-ttb18-serif text-[17px] text-ttb18-soft italic">
        <p class="hidden group-has-[#ttb18-r1:checked]/tabs:block">The Origins — movable type reaches Venice, Basel and Paris.</p>
        <p class="hidden group-has-[#ttb18-r2:checked]/tabs:block">The Reformation — pamphlets, presses and the Dutch type trade.</p>
        <p class="hidden group-has-[#ttb18-r3:checked]/tabs:block">The Industrial Cut — steam presses, fat faces and the poster.</p>
        <p class="hidden group-has-[#ttb18-r4:checked]/tabs:block">The Digital Era — outline fonts, the web and variable type.</p>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb18-paper/12 px-3.5 py-2 text-[11.5px] text-ttb18-mut">grid-cols-4 · h-1.5 w-1/4 bar · translate-x-[calc(var(--i)*100%)]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb18-bg: #1a1a1a;
  --color-ttb18-bg: oklch(0.218 0 0);
  --color-ttb18-paper: #ece6d4;
  --color-ttb18-paper: oklch(0.925 0.025 91.6);
  --color-ttb18-soft: #cfc9b8;
  --color-ttb18-soft: oklch(0.836 0.024 90.8);
  --color-ttb18-mut: #a8a293;
  --color-ttb18-mut: oklch(0.713 0.022 88.8);
  --color-ttb18-dim: #8f897c;
  --color-ttb18-dim: oklch(0.632 0.020 86.2);
  --color-ttb18-red: #d4433a;
  --color-ttb18-red: oklch(0.590 0.183 27.7);
  --font-ttb18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-ttb18-serif: 'Newsreader', Georgia, serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-18 {
  width: 100%;
  min-height: 100svh;
}
```
