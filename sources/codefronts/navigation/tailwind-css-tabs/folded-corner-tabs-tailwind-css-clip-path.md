---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/folded-corner-tabs-tailwind-css-clip-path/"
title: "Folded Corner Tabs in Tailwind CSS (clip-path)"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Sand-coloured folio tabs on charcoal whose top-right corner folds down — 8px on hover, 18px when chosen — with a darker underside triangle and a 4px lift."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Folded Corner Tabs in Tailwind CSS (clip-path)
Source: https://codefronts.com/navigation/tailwind-css-tabs/folded-corner-tabs-tailwind-css-clip-path/

Sand-coloured folio tabs on charcoal whose top-right corner folds down — 8px on hover, 18px when chosen — with a darker underside triangle and a 4px lift. The port fixes two bugs in the original: its shadow was clipped away by its own clip-path, and its 4-point and 5-point polygons couldn't interpolate smoothly.
## HTML
```html
<section class="ttb-30 group/tabs grid min-h-svh w-full place-items-center bg-ttb30-bg px-5 py-14 font-ttb30-serif text-ttb30-ink" aria-label="Folded corner tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full">
      <div role="radiogroup" aria-label="Page" class="flex gap-2 pt-1">
        <label class="group/tab relative isolate flex min-h-14 flex-1 cursor-pointer items-center px-4 text-[15px] font-semibold text-ttb30-ink/70 transition-[translate,filter,color] duration-300 hover:text-ttb30-ink has-checked:-translate-y-1 has-checked:text-ttb30-ink has-checked:drop-shadow-[0_8px_10px_rgb(0_0_0/0.45)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-ttb30-sand motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb30" id="ttb30-r1" checked><span aria-hidden="true" class="absolute inset-0 -z-10 bg-ttb30-sand transition-[clip-path,background-color] duration-450 ease-[cubic-bezier(0.65,0,0.35,1)] [clip-path:polygon(0_0,100%_0,100%_0,100%_100%,0_100%)] group-has-checked/tab:bg-ttb30-sand-hi group-has-checked/tab:[clip-path:polygon(0_0,calc(100%_-_18px)_0,100%_18px,100%_100%,0_100%)] group-not-has-checked/tab:group-hover/tab:[clip-path:polygon(0_0,calc(100%_-_8px)_0,100%_8px,100%_100%,0_100%)] motion-reduce:transition-none"></span><span aria-hidden="true" class="absolute top-0 right-0 size-[18px] scale-0 origin-top-right bg-ttb30-fold [clip-path:polygon(0_0,100%_100%,0_100%)] transition-transform duration-450 ease-[cubic-bezier(0.65,0,0.35,1)] group-has-checked/tab:scale-100 group-not-has-checked/tab:group-hover/tab:scale-[0.45] motion-reduce:transition-none"></span>Page 1</label>
        <label class="group/tab relative isolate flex min-h-14 flex-1 cursor-pointer items-center px-4 text-[15px] font-semibold text-ttb30-ink/70 transition-[translate,filter,color] duration-300 hover:text-ttb30-ink has-checked:-translate-y-1 has-checked:text-ttb30-ink has-checked:drop-shadow-[0_8px_10px_rgb(0_0_0/0.45)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-ttb30-sand motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb30" id="ttb30-r2"><span aria-hidden="true" class="absolute inset-0 -z-10 bg-ttb30-sand transition-[clip-path,background-color] duration-450 ease-[cubic-bezier(0.65,0,0.35,1)] [clip-path:polygon(0_0,100%_0,100%_0,100%_100%,0_100%)] group-has-checked/tab:bg-ttb30-sand-hi group-has-checked/tab:[clip-path:polygon(0_0,calc(100%_-_18px)_0,100%_18px,100%_100%,0_100%)] group-not-has-checked/tab:group-hover/tab:[clip-path:polygon(0_0,calc(100%_-_8px)_0,100%_8px,100%_100%,0_100%)] motion-reduce:transition-none"></span><span aria-hidden="true" class="absolute top-0 right-0 size-[18px] scale-0 origin-top-right bg-ttb30-fold [clip-path:polygon(0_0,100%_100%,0_100%)] transition-transform duration-450 ease-[cubic-bezier(0.65,0,0.35,1)] group-has-checked/tab:scale-100 group-not-has-checked/tab:group-hover/tab:scale-[0.45] motion-reduce:transition-none"></span>Page 2</label>
        <label class="group/tab relative isolate flex min-h-14 flex-1 cursor-pointer items-center px-4 text-[15px] font-semibold text-ttb30-ink/70 transition-[translate,filter,color] duration-300 hover:text-ttb30-ink has-checked:-translate-y-1 has-checked:text-ttb30-ink has-checked:drop-shadow-[0_8px_10px_rgb(0_0_0/0.45)] has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-ttb30-sand motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb30" id="ttb30-r3"><span aria-hidden="true" class="absolute inset-0 -z-10 bg-ttb30-sand transition-[clip-path,background-color] duration-450 ease-[cubic-bezier(0.65,0,0.35,1)] [clip-path:polygon(0_0,100%_0,100%_0,100%_100%,0_100%)] group-has-checked/tab:bg-ttb30-sand-hi group-has-checked/tab:[clip-path:polygon(0_0,calc(100%_-_18px)_0,100%_18px,100%_100%,0_100%)] group-not-has-checked/tab:group-hover/tab:[clip-path:polygon(0_0,calc(100%_-_8px)_0,100%_8px,100%_100%,0_100%)] motion-reduce:transition-none"></span><span aria-hidden="true" class="absolute top-0 right-0 size-[18px] scale-0 origin-top-right bg-ttb30-fold [clip-path:polygon(0_0,100%_100%,0_100%)] transition-transform duration-450 ease-[cubic-bezier(0.65,0,0.35,1)] group-has-checked/tab:scale-100 group-not-has-checked/tab:group-hover/tab:scale-[0.45] motion-reduce:transition-none"></span>Page 3</label>
      </div>
      <div class="pt-5 text-[17px] text-ttb30-sand italic">
        <p class="hidden group-has-[#ttb30-r1:checked]/tabs:block">The opening recto.</p>
        <p class="hidden group-has-[#ttb30-r2:checked]/tabs:block">The continuation, folded back to keep your place.</p>
        <p class="hidden group-has-[#ttb30-r3:checked]/tabs:block">The closing leaf.</p>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb30-sand/20 px-3.5 py-2 font-ttb30-mono text-[11.5px] text-ttb30-sand">5-point polygons · drop-shadow on unclipped label · not-has-checked:hover</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb30-bg: #25222e;
  --color-ttb30-bg: oklch(0.261 0.023 296.3);
  --color-ttb30-sand: #d4a574;
  --color-ttb30-sand: oklch(0.754 0.085 67.1);
  --color-ttb30-sand-hi: #e6c39c;
  --color-ttb30-sand-hi: oklch(0.838 0.065 69.8);
  --color-ttb30-fold: #1c1a24;
  --color-ttb30-fold: oklch(0.225 0.019 293.9);
  --color-ttb30-ink: #1a1a1a;
  --color-ttb30-ink: oklch(0.218 0 0);
  --font-ttb30-serif: 'Newsreader', Georgia, serif;
  --font-ttb30-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-30 {
  width: 100%;
  min-height: 100svh;
}
```
