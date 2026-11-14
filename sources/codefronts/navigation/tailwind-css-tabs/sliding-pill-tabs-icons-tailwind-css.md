---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/sliding-pill-tabs-icons-tailwind-css/"
title: "Sliding Pill Tabs with Icons in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Grid / List / Cards: a solid indigo pill glides under icon-and-label tabs on cream stock, and the label inverts as the pill arrives."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliding Pill Tabs with Icons in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/sliding-pill-tabs-icons-tailwind-css/

Grid / List / Cards: a solid indigo pill glides under icon-and-label tabs on cream stock, and the label inverts as the pill arrives. The original measured the pill in JavaScript; the port slides it with the index trick and turns each panel into a live layout preview of the view you chose.
## HTML
```html
<section class="ttb-29 group/tabs grid min-h-svh w-full place-items-center bg-ttb29-bg px-5 py-14 font-ttb29-sans text-ttb29-indigo" aria-label="Sliding pill tabs with icons demo">
  <div class="grid w-full max-w-md justify-items-center gap-7">
    <div class="w-full">
      <div role="radiogroup" aria-label="View" class="relative flex rounded-full bg-ttb29-indigo/7 p-1.5 [--i:0] has-[#ttb29-r2:checked]:[--i:1] has-[#ttb29-r3:checked]:[--i:2]">
        <span aria-hidden="true" class="pointer-events-none absolute inset-y-1.5 left-1.5 w-[calc((100%-12px)/3)] translate-x-[calc(var(--i)*100%)] rounded-full bg-ttb29-indigo shadow-[0_6px_16px_-6px_color-mix(in_oklab,var(--color-ttb29-indigo)_60%,transparent)] transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:transition-none"></span>
        <label class="relative z-10 flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-2 rounded-full text-[13px] font-semibold text-ttb29-mut transition-colors delay-75 duration-300 hover:text-ttb29-indigo has-checked:text-ttb29-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb29-indigo"><input class="sr-only" type="radio" name="ttb29" id="ttb29-r1" checked><svg aria-hidden="true" class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>Grid</label>
        <label class="relative z-10 flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-2 rounded-full text-[13px] font-semibold text-ttb29-mut transition-colors delay-75 duration-300 hover:text-ttb29-indigo has-checked:text-ttb29-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb29-indigo"><input class="sr-only" type="radio" name="ttb29" id="ttb29-r2"><svg aria-hidden="true" class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M9 6h12M9 12h12M9 18h12"/><circle cx="4" cy="6" r="1"/><circle cx="4" cy="12" r="1"/><circle cx="4" cy="18" r="1"/></svg>List</label>
        <label class="relative z-10 flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-2 rounded-full text-[13px] font-semibold text-ttb29-mut transition-colors delay-75 duration-300 hover:text-ttb29-indigo has-checked:text-ttb29-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb29-indigo"><input class="sr-only" type="radio" name="ttb29" id="ttb29-r3"><svg aria-hidden="true" class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9"><rect x="3" y="4" width="18" height="6" rx="1.5"/><rect x="3" y="14" width="18" height="6" rx="1.5"/></svg>Cards</label>
      </div>
      <div aria-hidden="true" class="mt-4 rounded-2xl bg-white p-4 ring-1 ring-ttb29-indigo/8">
        <div class="hidden grid-cols-3 gap-2 group-has-[#ttb29-r1:checked]/tabs:grid"><i class="aspect-square rounded-lg bg-ttb29-indigo/10"></i><i class="aspect-square rounded-lg bg-ttb29-indigo/10"></i><i class="aspect-square rounded-lg bg-ttb29-indigo/10"></i><i class="aspect-square rounded-lg bg-ttb29-indigo/10"></i><i class="aspect-square rounded-lg bg-ttb29-indigo/10"></i><i class="aspect-square rounded-lg bg-ttb29-indigo/10"></i></div>
        <div class="hidden flex-col gap-2.5 group-has-[#ttb29-r2:checked]/tabs:flex"><i class="flex h-6 items-center gap-2.5"><b class="size-6 rounded-md bg-ttb29-indigo/15"></b><b class="h-2 w-2/3 rounded-full bg-ttb29-indigo/10"></b></i><i class="flex h-6 items-center gap-2.5"><b class="size-6 rounded-md bg-ttb29-indigo/15"></b><b class="h-2 w-1/2 rounded-full bg-ttb29-indigo/10"></b></i><i class="flex h-6 items-center gap-2.5"><b class="size-6 rounded-md bg-ttb29-indigo/15"></b><b class="h-2 w-3/4 rounded-full bg-ttb29-indigo/10"></b></i><i class="flex h-6 items-center gap-2.5"><b class="size-6 rounded-md bg-ttb29-indigo/15"></b><b class="h-2 w-2/5 rounded-full bg-ttb29-indigo/10"></b></i></div>
        <div class="hidden flex-col gap-2.5 group-has-[#ttb29-r3:checked]/tabs:flex"><i class="h-[58px] rounded-xl bg-ttb29-indigo/10"></i><i class="h-[58px] rounded-xl bg-ttb29-indigo/10"></i></div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-ttb29-mono text-[11.5px] text-ttb29-mut">CSS pill · label delay-75 · live layout preview</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb29-bg: #f4f3ee;
  --color-ttb29-bg: oklch(0.964 0.007 97.4);
  --color-ttb29-indigo: #3b3a8c;
  --color-ttb29-indigo: oklch(0.398 0.133 279.1);
  --color-ttb29-mut: #5d5c94;
  --color-ttb29-mut: oklch(0.500 0.088 283.5);
  --font-ttb29-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttb29-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-29 {
  width: 100%;
  min-height: 100svh;
}
```
