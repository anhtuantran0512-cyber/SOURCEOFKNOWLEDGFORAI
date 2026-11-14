---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/animated-svg-underline-tabs-tailwind-css/"
title: "Animated SVG Underline Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Italic slab-serif tabs on cream vellum; the active word gets an emerald swash that draws itself beneath the letters like a calligrapher's flourish."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated SVG Underline Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/animated-svg-underline-tabs-tailwind-css/

Italic slab-serif tabs on cream vellum; the active word gets an emerald swash that draws itself beneath the letters like a calligrapher's flourish. The port normalises the path with pathLength="1", so the draw is exact for any curve, and sets the labels in Zilla Slab italic.
## HTML
```html
<section class="ttb-27 group/tabs grid min-h-svh w-full place-items-center bg-ttb27-bg px-5 py-14 font-ttb27-slab text-ttb27-ink" aria-label="Animated SVG underline tabs demo">
  <div class="grid w-full max-w-xl justify-items-start gap-7">
    <div role="radiogroup" aria-label="Section" class="flex flex-wrap items-end gap-x-9 gap-y-4">
      <label class="group/tab relative min-h-11 cursor-pointer pb-2 text-[24px] font-bold text-ttb27-mut italic transition-colors hover:text-ttb27-ink has-checked:text-ttb27-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-6 has-focus-visible:outline-ttb27-ink"><input class="sr-only" type="radio" name="ttb27" id="ttb27-r1" checked>Manifesto<svg aria-hidden="true" class="absolute -bottom-2 left-0 h-3.5 w-full overflow-visible" viewBox="0 0 100 14" preserveAspectRatio="none"><path pathLength="1" d="M2 9 Q 22 2 44 7 T 86 6 q 8-1 10 3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" class="transition-[stroke-dashoffset] duration-700 ease-[cubic-bezier(0.65,0,0.35,1)] [stroke-dasharray:1] [stroke-dashoffset:1] group-has-checked/tab:[stroke-dashoffset:0] motion-reduce:transition-none"/></svg></label>
      <label class="group/tab relative min-h-11 cursor-pointer pb-2 text-[24px] font-bold text-ttb27-mut italic transition-colors hover:text-ttb27-ink has-checked:text-ttb27-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-6 has-focus-visible:outline-ttb27-ink"><input class="sr-only" type="radio" name="ttb27" id="ttb27-r2">Colophon<svg aria-hidden="true" class="absolute -bottom-2 left-0 h-3.5 w-full overflow-visible" viewBox="0 0 100 14" preserveAspectRatio="none"><path pathLength="1" d="M2 9 Q 22 2 44 7 T 86 6 q 8-1 10 3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" class="transition-[stroke-dashoffset] duration-700 ease-[cubic-bezier(0.65,0,0.35,1)] [stroke-dasharray:1] [stroke-dashoffset:1] group-has-checked/tab:[stroke-dashoffset:0] motion-reduce:transition-none"/></svg></label>
      <label class="group/tab relative min-h-11 cursor-pointer pb-2 text-[24px] font-bold text-ttb27-mut italic transition-colors hover:text-ttb27-ink has-checked:text-ttb27-ink has-focus-visible:outline-2 has-focus-visible:outline-offset-6 has-focus-visible:outline-ttb27-ink"><input class="sr-only" type="radio" name="ttb27" id="ttb27-r3">Errata<svg aria-hidden="true" class="absolute -bottom-2 left-0 h-3.5 w-full overflow-visible" viewBox="0 0 100 14" preserveAspectRatio="none"><path pathLength="1" d="M2 9 Q 22 2 44 7 T 86 6 q 8-1 10 3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" class="transition-[stroke-dashoffset] duration-700 ease-[cubic-bezier(0.65,0,0.35,1)] [stroke-dasharray:1] [stroke-dashoffset:1] group-has-checked/tab:[stroke-dashoffset:0] motion-reduce:transition-none"/></svg></label>
    </div>
    <div class="max-w-[40ch] pt-2 font-ttb27-serif text-[17px] leading-relaxed text-ttb27-ash italic">
      <p class="hidden group-has-[#ttb27-r1:checked]/tabs:block">The founding statement of intent, set in full measure.</p>
      <p class="hidden group-has-[#ttb27-r2:checked]/tabs:block">The closing inscription: type, paper and press notes.</p>
      <p class="hidden group-has-[#ttb27-r3:checked]/tabs:block">Corrections issued after the first printing.</p>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb27-ink/15 bg-white/50 px-3.5 py-2 font-ttb27-mono text-[11.5px] text-ttb27-ash">pathLength="1" · [stroke-dashoffset:1] → 0</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb27-bg: #fbf2d4;
  --color-ttb27-bg: oklch(0.960 0.040 93.2);
  --color-ttb27-ink: #0f4f3d;
  --color-ttb27-ink: oklch(0.383 0.070 169.3);
  --color-ttb27-mut: #4a7a6c;
  --color-ttb27-mut: oklch(0.541 0.057 173.6);
  --color-ttb27-ash: #3a3a42;
  --color-ttb27-ash: oklch(0.352 0.014 285.7);
  --font-ttb27-slab: 'Zilla Slab', Rockwell, serif;
  --font-ttb27-serif: 'Newsreader', Georgia, serif;
  --font-ttb27-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-27 {
  width: 100%;
  min-height: 100svh;
}
```
