---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/outlined-tabs-corner-markers-tailwind-css/"
title: "Outlined Tabs with Corner Markers in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Hairline-framed tabs on warm white."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Outlined Tabs with Corner Markers in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/outlined-tabs-corner-markers-tailwind-css/

Hairline-framed tabs on warm white. The chosen frame inks a 4px navy top edge and four dots pop onto its corners a beat later, like crop marks. The 4px top border is reserved transparent from the start, so selecting a tab never moves the row by a pixel.
## HTML
```html
<section class="ttb-24 group/tabs grid min-h-svh w-full place-items-center bg-ttb24-bg px-5 py-14 font-ttb24-serif text-ttb24-navy" aria-label="Outlined tabs with corner markers demo">
  <div class="grid w-full max-w-lg justify-items-center gap-7">
    <div class="w-full">
      <div role="radiogroup" aria-label="Stage" class="flex flex-wrap gap-3.5">
        <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center gap-2 border border-t-4 border-ttb24-navy/40 border-t-transparent px-5 text-[15px] font-semibold tracking-[0.03em] text-ttb24-mut transition-[color,border-color] duration-300 hover:text-ttb24-navy has-checked:border-ttb24-navy has-checked:border-t-ttb24-navy has-checked:text-ttb24-navy has-focus-visible:outline-2 has-focus-visible:outline-offset-5 has-focus-visible:outline-ttb24-navy"><input class="sr-only" type="radio" name="ttb24" id="ttb24-r1" checked>Drafts <span class="font-ttb24-mono text-[11px] font-medium tabular-nums">12</span><i aria-hidden="true" class="absolute -top-1 -left-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i><i aria-hidden="true" class="absolute -top-1 -right-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i><i aria-hidden="true" class="absolute -bottom-1 -left-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i><i aria-hidden="true" class="absolute -right-1 -bottom-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i></label>
        <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center gap-2 border border-t-4 border-ttb24-navy/40 border-t-transparent px-5 text-[15px] font-semibold tracking-[0.03em] text-ttb24-mut transition-[color,border-color] duration-300 hover:text-ttb24-navy has-checked:border-ttb24-navy has-checked:border-t-ttb24-navy has-checked:text-ttb24-navy has-focus-visible:outline-2 has-focus-visible:outline-offset-5 has-focus-visible:outline-ttb24-navy"><input class="sr-only" type="radio" name="ttb24" id="ttb24-r2">Proofs <span class="font-ttb24-mono text-[11px] font-medium tabular-nums">4</span><i aria-hidden="true" class="absolute -top-1 -left-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i><i aria-hidden="true" class="absolute -top-1 -right-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i><i aria-hidden="true" class="absolute -bottom-1 -left-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i><i aria-hidden="true" class="absolute -right-1 -bottom-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i></label>
        <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center gap-2 border border-t-4 border-ttb24-navy/40 border-t-transparent px-5 text-[15px] font-semibold tracking-[0.03em] text-ttb24-mut transition-[color,border-color] duration-300 hover:text-ttb24-navy has-checked:border-ttb24-navy has-checked:border-t-ttb24-navy has-checked:text-ttb24-navy has-focus-visible:outline-2 has-focus-visible:outline-offset-5 has-focus-visible:outline-ttb24-navy"><input class="sr-only" type="radio" name="ttb24" id="ttb24-r3">Final <span class="font-ttb24-mono text-[11px] font-medium tabular-nums">31</span><i aria-hidden="true" class="absolute -top-1 -left-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i><i aria-hidden="true" class="absolute -top-1 -right-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i><i aria-hidden="true" class="absolute -bottom-1 -left-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i><i aria-hidden="true" class="absolute -right-1 -bottom-1 size-[7px] scale-0 rounded-full bg-ttb24-navy transition-transform delay-100 duration-350 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-has-checked/tab:scale-100"></i></label>
      </div>
      <div class="pt-5 text-[16px] text-ttb24-ash italic">
        <p class="hidden group-has-[#ttb24-r1:checked]/tabs:block">Working files in progress.</p>
        <p class="hidden group-has-[#ttb24-r2:checked]/tabs:block">Galleys ready for review.</p>
        <p class="hidden group-has-[#ttb24-r3:checked]/tabs:block">Approved and locked.</p>
      </div>
    </div>
    <p aria-hidden="true" class="border border-ttb24-navy/30 px-3.5 py-2 font-ttb24-mono text-[11.5px] text-ttb24-mut">border-t-transparent reserved · corner dots delay-100</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb24-bg: #f5f1ea;
  --color-ttb24-bg: oklch(0.959 0.010 81.8);
  --color-ttb24-navy: #1a2842;
  --color-ttb24-navy: oklch(0.278 0.052 262.0);
  --color-ttb24-mut: #5a6478;
  --color-ttb24-mut: oklch(0.502 0.034 264.2);
  --color-ttb24-ash: #3a3a42;
  --color-ttb24-ash: oklch(0.352 0.014 285.7);
  --font-ttb24-serif: 'Newsreader', Georgia, serif;
  --font-ttb24-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-24 {
  width: 100%;
  min-height: 100svh;
}
```
