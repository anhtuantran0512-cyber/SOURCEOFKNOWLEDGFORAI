---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/animated-counter-tabs-tailwind-css-type-specimen/"
title: "Animated Counter Tabs in Tailwind CSS (Type Specimen)"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A letterpress specimen card: a large mint serial number rolls to each typeface's catalogue number, a rule slides under the active name, and the panel shows a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Counter Tabs in Tailwind CSS (Type Specimen)
Source: https://codefronts.com/navigation/tailwind-css-tabs/animated-counter-tabs-tailwind-css-type-specimen/

A letterpress specimen card: a large mint serial number rolls to each typeface's catalogue number, a rule slides under the active name, and the panel shows a live specimen in that face. The original flipped the number with a setTimeout; the port stacks three serials in one grid cell and rolls them with translate-y.
## HTML
```html
<section class="ttb-13 group/tabs grid min-h-svh w-full place-items-center bg-ttb13-bg px-5 py-14 font-ttb13-mono text-ttb13-paper" aria-label="Type specimen counter tabs demo">
  <div class="grid w-full max-w-lg justify-items-center gap-7">
    <div class="w-full rounded-2xl bg-ttb13-card p-6 ring-1 ring-ttb13-mint/15">
      <div class="flex items-baseline justify-between">
        <span aria-hidden="true" class="grid overflow-hidden text-[44px] leading-none font-extrabold tracking-[0.02em] text-ttb13-mint [&>*]:[grid-area:1/1]"><span class="translate-y-full opacity-0 transition-[translate,opacity] duration-500 ease-[cubic-bezier(0.34,1.4,0.64,1)] group-has-[#ttb13-r1:checked]/tabs:translate-y-0 group-has-[#ttb13-r1:checked]/tabs:opacity-100 motion-reduce:transition-none">0317</span><span class="translate-y-full opacity-0 transition-[translate,opacity] duration-500 ease-[cubic-bezier(0.34,1.4,0.64,1)] group-has-[#ttb13-r2:checked]/tabs:translate-y-0 group-has-[#ttb13-r2:checked]/tabs:opacity-100 motion-reduce:transition-none">0211</span><span class="translate-y-full opacity-0 transition-[translate,opacity] duration-500 ease-[cubic-bezier(0.34,1.4,0.64,1)] group-has-[#ttb13-r3:checked]/tabs:translate-y-0 group-has-[#ttb13-r3:checked]/tabs:opacity-100 motion-reduce:transition-none">0489</span></span>
        <span class="text-[10.5px] tracking-[0.2em] text-ttb13-mut uppercase">Specimen No.</span>
      </div>
      <div role="radiogroup" aria-label="Typeface" class="relative mt-4 flex border-y border-ttb13-mint/20 [--i:0] has-[#ttb13-r2:checked]:[--i:1] has-[#ttb13-r3:checked]:[--i:2]">
        <label class="flex min-h-11 flex-1 cursor-pointer items-center justify-center text-[11px] font-bold tracking-[0.18em] text-ttb13-mut uppercase transition-colors hover:text-ttb13-paper has-checked:text-ttb13-mint has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb13-mint"><input class="sr-only" type="radio" name="ttb13" id="ttb13-r1" checked>Helvetica</label>
        <label class="flex min-h-11 flex-1 cursor-pointer items-center justify-center text-[11px] font-bold tracking-[0.18em] text-ttb13-mut uppercase transition-colors hover:text-ttb13-paper has-checked:text-ttb13-mint has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb13-mint"><input class="sr-only" type="radio" name="ttb13" id="ttb13-r2">Bodoni</label>
        <label class="flex min-h-11 flex-1 cursor-pointer items-center justify-center text-[11px] font-bold tracking-[0.18em] text-ttb13-mut uppercase transition-colors hover:text-ttb13-paper has-checked:text-ttb13-mint has-focus-visible:outline-1 has-focus-visible:-outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb13-mint"><input class="sr-only" type="radio" name="ttb13" id="ttb13-r3">Futura</label>
        <span aria-hidden="true" class="pointer-events-none absolute -bottom-px left-0 h-0.5 w-1/3 translate-x-[calc(var(--i)*100%)] bg-ttb13-mint transition-transform duration-400 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:transition-none"></span>
      </div>
      <div class="mt-5 min-h-24">
        <div class="hidden group-has-[#ttb13-r1:checked]/tabs:block"><p aria-hidden="true" class="font-ttb13-grot text-5xl font-bold tracking-tight">Aa Rr 3</p><p class="mt-2 font-ttb13-serif text-[13px] text-ttb13-mut italic">Cut by Max Miedinger, 1957. Neo-grotesque sans.</p></div>
        <div class="hidden group-has-[#ttb13-r2:checked]/tabs:block"><p aria-hidden="true" class="font-ttb13-serif text-5xl font-medium">Aa Rr 3</p><p class="mt-2 font-ttb13-serif text-[13px] text-ttb13-mut italic">Cut by Giambattista Bodoni, 1798. Modern serif.</p></div>
        <div class="hidden group-has-[#ttb13-r3:checked]/tabs:block"><p aria-hidden="true" class="font-ttb13-geo text-5xl font-medium">Aa Rr 3</p><p class="mt-2 font-ttb13-serif text-[13px] text-ttb13-mut italic">Cut by Paul Renner, 1927. Geometric sans.</p></div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb13-mint/15 px-3.5 py-2 text-[11.5px] text-ttb13-mut">stacked serials [grid-area:1/1] · translate-y roll · 0 KB JS</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb13-bg: #181b1e;
  --color-ttb13-bg: oklch(0.220 0.007 248.2);
  --color-ttb13-card: #1f2326;
  --color-ttb13-card: oklch(0.253 0.008 240.2);
  --color-ttb13-paper: #ece6d4;
  --color-ttb13-paper: oklch(0.925 0.025 91.6);
  --color-ttb13-mut: #a9a597;
  --color-ttb13-mut: oklch(0.721 0.020 93.7);
  --color-ttb13-mint: #51d5c2;
  --color-ttb13-mint: oklch(0.796 0.118 182.0);
  --font-ttb13-mono: 'Geist Mono', ui-monospace, monospace;
  --font-ttb13-grot: 'Helvetica Neue', Helvetica, 'Geist', system-ui, sans-serif;
  --font-ttb13-serif: 'Bodoni Moda', Georgia, serif;
  --font-ttb13-geo: 'Jost', 'Futura', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-13 {
  width: 100%;
  min-height: 100svh;
}
```
