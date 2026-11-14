---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/drop-cap-initial-letter-tabs-tailwind-css/"
title: "Drop Cap Initial Letter Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Inactive tabs are single serif initials; the chosen one tips its capital into a terracotta drop cap (rotate −4°, scale 1.15 from the baseline) and unfolds…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Drop Cap Initial Letter Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/drop-cap-initial-letter-tabs-tailwind-css/

Inactive tabs are single serif initials; the chosen one tips its capital into a terracotta drop cap (rotate −4°, scale 1.15 from the baseline) and unfolds the rest of the word in italic. Set in Fraunces, whose 900 cut and soft italic give the woodblock-and-ink contrast the idea needs.
## HTML
```html
<section class="ttb-19 group/tabs grid min-h-svh w-full place-items-center bg-ttb19-bg px-5 py-14 font-ttb19-serif text-ttb19-teal" aria-label="Drop cap initial letter tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full rounded-2xl bg-ttb19-paper p-7 shadow-[0_18px_40px_-24px_rgb(12_85_96/0.4)] ring-1 ring-ttb19-teal/12">
      <div role="radiogroup" aria-label="Section" class="flex items-baseline gap-7 border-b border-ttb19-teal/20 pb-4">
        <label class="group/tab flex min-h-11 cursor-pointer items-baseline text-ttb19-dim transition-colors hover:text-ttb19-teal has-checked:text-ttb19-teal has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-ttb19-cap"><input class="sr-only" type="radio" name="ttb19" id="ttb19-r1" checked><span class="sr-only">Article</span><span aria-hidden="true" class="inline-block origin-bottom text-[30px] leading-none font-black transition-[rotate,scale,color] duration-500 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:-rotate-4 group-has-checked/tab:scale-115 group-has-checked/tab:text-ttb19-cap motion-reduce:transition-none">A</span><span aria-hidden="true" class="ml-px max-w-0 overflow-hidden text-[19px] whitespace-nowrap italic transition-[max-width] delay-100 duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] group-has-checked/tab:max-w-[8ch] motion-reduce:transition-none">rticle</span></label>
        <label class="group/tab flex min-h-11 cursor-pointer items-baseline text-ttb19-dim transition-colors hover:text-ttb19-teal has-checked:text-ttb19-teal has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-ttb19-cap"><input class="sr-only" type="radio" name="ttb19" id="ttb19-r2"><span class="sr-only">Gallery</span><span aria-hidden="true" class="inline-block origin-bottom text-[30px] leading-none font-black transition-[rotate,scale,color] duration-500 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:-rotate-4 group-has-checked/tab:scale-115 group-has-checked/tab:text-ttb19-cap motion-reduce:transition-none">G</span><span aria-hidden="true" class="ml-px max-w-0 overflow-hidden text-[19px] whitespace-nowrap italic transition-[max-width] delay-100 duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] group-has-checked/tab:max-w-[8ch] motion-reduce:transition-none">allery</span></label>
        <label class="group/tab flex min-h-11 cursor-pointer items-baseline text-ttb19-dim transition-colors hover:text-ttb19-teal has-checked:text-ttb19-teal has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-ttb19-cap"><input class="sr-only" type="radio" name="ttb19" id="ttb19-r3"><span class="sr-only">Notes</span><span aria-hidden="true" class="inline-block origin-bottom text-[30px] leading-none font-black transition-[rotate,scale,color] duration-500 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:-rotate-4 group-has-checked/tab:scale-115 group-has-checked/tab:text-ttb19-cap motion-reduce:transition-none">N</span><span aria-hidden="true" class="ml-px max-w-0 overflow-hidden text-[19px] whitespace-nowrap italic transition-[max-width] delay-100 duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] group-has-checked/tab:max-w-[8ch] motion-reduce:transition-none">otes</span></label>
      </div>
      <div class="pt-4 text-[16px] leading-relaxed text-ttb19-ash italic">
        <p class="hidden group-has-[#ttb19-r1:checked]/tabs:block">The body copy of an editorial feature, set long and generously leaded.</p>
        <p class="hidden group-has-[#ttb19-r2:checked]/tabs:block">A curated set of plates and engravings, each with a full caption.</p>
        <p class="hidden group-has-[#ttb19-r3:checked]/tabs:block">Marginalia and footnote annotations gathered from the margins.</p>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb19-teal/15 bg-ttb19-paper/60 px-3.5 py-2 font-ttb19-mono text-[11.5px] text-ttb19-ash">origin-bottom -rotate-4 scale-115 · tail max-w-0 → 8ch</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb19-bg: #e8dec8;
  --color-ttb19-bg: oklch(0.903 0.031 86.5);
  --color-ttb19-paper: #f6f0e2;
  --color-ttb19-paper: oklch(0.956 0.020 87.5);
  --color-ttb19-teal: #0c5560;
  --color-ttb19-teal: oklch(0.414 0.068 210.7);
  --color-ttb19-dim: #4f7c83;
  --color-ttb19-dim: oklch(0.556 0.050 208.2);
  --color-ttb19-cap: #c4441f;
  --color-ttb19-cap: oklch(0.561 0.171 36.1);
  --color-ttb19-ash: #3a3a42;
  --color-ttb19-ash: oklch(0.352 0.014 285.7);
  --font-ttb19-serif: 'Fraunces', Georgia, serif;
  --font-ttb19-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-19 {
  width: 100%;
  min-height: 100svh;
}
```
