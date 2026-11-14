---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/bauhaus-color-block-tabs-tailwind-css/"
title: "Bauhaus Color Block Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Four primary tiles — red, yellow, black and cream — each marked with a Bauhaus primitive: circle, square, triangle, half-moon."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bauhaus Color Block Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/bauhaus-color-block-tabs-tailwind-css/

Four primary tiles — red, yellow, black and cream — each marked with a Bauhaus primitive: circle, square, triangle, half-moon. The chosen tile rises 6px and drops a hard shadow; there's no shared highlight colour because the tile itself is the indicator.
## HTML
```html
<section class="ttb-22 group/tabs grid min-h-svh w-full place-items-center bg-ttb22-cream px-5 py-14 font-ttb22-sans text-ttb22-ink" aria-label="Bauhaus color block tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full">
      <div role="radiogroup" aria-label="Principle" class="grid grid-cols-2 gap-2 pb-1.5 sm:grid-cols-4">
        <label class="group/tab flex min-h-20 cursor-pointer flex-col items-start justify-between bg-ttb22-red p-3 text-ttb22-cream transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:-translate-y-0.5 has-checked:-translate-y-1.5 has-checked:shadow-[0_6px_0_var(--color-ttb22-ink)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-ttb22-ink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb22" id="ttb22-r1" checked><svg aria-hidden="true" class="size-5 transition-[scale] duration-300 group-has-checked/tab:scale-125" viewBox="0 0 20 20"><circle cx="10" cy="10" r="9" fill="currentColor"/></svg><span class="text-xs font-bold tracking-[0.22em] uppercase">Form</span></label>
        <label class="group/tab flex min-h-20 cursor-pointer flex-col items-start justify-between bg-ttb22-yellow p-3 text-ttb22-ink transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:-translate-y-0.5 has-checked:-translate-y-1.5 has-checked:shadow-[0_6px_0_var(--color-ttb22-ink)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-ttb22-ink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb22" id="ttb22-r2"><svg aria-hidden="true" class="size-5 transition-[rotate] duration-300 group-has-checked/tab:rotate-45" viewBox="0 0 20 20"><rect x="2" y="2" width="16" height="16" fill="currentColor"/></svg><span class="text-xs font-bold tracking-[0.22em] uppercase">Grid</span></label>
        <label class="group/tab flex min-h-20 cursor-pointer flex-col items-start justify-between bg-ttb22-ink p-3 text-ttb22-cream transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:-translate-y-0.5 has-checked:-translate-y-1.5 has-checked:shadow-[0_6px_0_var(--color-ttb22-red)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-ttb22-ink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb22" id="ttb22-r3"><svg aria-hidden="true" class="size-5 transition-[rotate] duration-300 group-has-checked/tab:rotate-180" viewBox="0 0 20 20"><path d="M10 1.5 19 18.5H1z" fill="currentColor"/></svg><span class="text-xs font-bold tracking-[0.22em] uppercase">Type</span></label>
        <label class="group/tab flex min-h-20 cursor-pointer flex-col items-start justify-between bg-ttb22-cream p-3 text-ttb22-ink ring-[1.5px] ring-ttb22-ink ring-inset transition-[translate,box-shadow] duration-300 ease-[cubic-bezier(0.34,1.56,0.64,1)] hover:-translate-y-0.5 has-checked:-translate-y-1.5 has-checked:shadow-[0_6px_0_var(--color-ttb22-ink)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-ttb22-ink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb22" id="ttb22-r4"><svg aria-hidden="true" class="size-5 transition-[rotate] duration-300 group-has-checked/tab:-rotate-90" viewBox="0 0 20 20"><path d="M1 14a9 9 0 0 1 18 0z" fill="currentColor"/></svg><span class="text-xs font-bold tracking-[0.22em] uppercase">Hue</span></label>
      </div>
      <div class="pt-5 font-ttb22-serif text-[16px] text-ttb22-ash italic">
        <p class="hidden group-has-[#ttb22-r1:checked]/tabs:block">Composition, weight and balance.</p>
        <p class="hidden group-has-[#ttb22-r2:checked]/tabs:block">Modular columns and rows.</p>
        <p class="hidden group-has-[#ttb22-r3:checked]/tabs:block">Specimens and pairings.</p>
        <p class="hidden group-has-[#ttb22-r4:checked]/tabs:block">A limited primary palette.</p>
      </div>
    </div>
    <p aria-hidden="true" class="border-[1.5px] border-ttb22-ink px-3.5 py-2 font-ttb22-mono text-[11.5px]">has-checked:-translate-y-1.5 · shadow-[0_6px_0] · primitives</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb22-cream: #f5ead0;
  --color-ttb22-cream: oklch(0.939 0.036 87.8);
  --color-ttb22-red: #c43a32;
  --color-ttb22-red: oklch(0.552 0.176 27.7);
  --color-ttb22-yellow: #e0aa1c;
  --color-ttb22-yellow: oklch(0.768 0.152 84.5);
  --color-ttb22-ink: #1a1a1a;
  --color-ttb22-ink: oklch(0.218 0 0);
  --color-ttb22-ash: #3a3a42;
  --color-ttb22-ash: oklch(0.352 0.014 285.7);
  --font-ttb22-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-ttb22-serif: 'Newsreader', Georgia, serif;
  --font-ttb22-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-22 {
  width: 100%;
  min-height: 100svh;
}
```
