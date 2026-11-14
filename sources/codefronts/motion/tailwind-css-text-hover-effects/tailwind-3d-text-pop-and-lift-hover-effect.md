---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-3d-text-pop-and-lift-hover-effect/"
title: "Tailwind 3D Text Pop and Lift Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A festival headline that pops out of the page: six same-length text-shadow layers interpolate from 0 to an extruded side, with active: pressing it back in on…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Text Pop and Lift Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-3d-text-pop-and-lift-hover-effect/

A festival headline that pops out of the page: six same-length text-shadow layers interpolate from 0 to an extruded side, with active: pressing it back in on click. Matching neo-brutalist buttons lift and press with box-shadow. Everything rides a springy cubic-bezier(.34,1.8,.4,1).
## HTML
```html
<section class="tth-09 w-full min-h-svh grid place-items-center bg-tth09-bg bg-[radial-gradient(90%_70%_at_50%_20%,var(--color-tth09-glow),var(--color-tth09-bg)_75%)] px-5 py-14 font-tth09-sans text-tth09-ink" aria-label="3D pop lift text demo">
  <div class="flex flex-col items-center gap-[clamp(16px,3vw,24px)] text-center">
    <p class="text-[12.5px] font-extrabold uppercase tracking-[0.24em] text-tth09-mut">Riverside park &middot; Jan 30&ndash;31 &middot; all ages</p>
    <h2 class="leading-[0.96]"><a id="tth09-top" href="#tth09-top" class="inline-block rounded-md text-[clamp(58px,13vw,132px)] font-black tracking-[-0.015em] no-underline [text-shadow:0_0_0_var(--color-tth09-side),0_0_0_var(--color-tth09-side),0_0_0_var(--color-tth09-side),0_0_0_var(--color-tth09-side),0_0_0_var(--color-tth09-side),0_0_0_var(--color-tth09-side),0_0_0_transparent] transition-[translate,text-shadow] duration-300 ease-[cubic-bezier(.34,1.8,.4,1)] hover:translate-x-[0.05em] hover:-translate-y-[0.14em] hover:[text-shadow:.02em_.02em_0_var(--color-tth09-side),.045em_.045em_0_var(--color-tth09-side),.07em_.07em_0_var(--color-tth09-side),.095em_.095em_0_var(--color-tth09-side),.12em_.12em_0_var(--color-tth09-side),.145em_.145em_0_var(--color-tth09-side),.3em_.42em_1em_oklch(0.3_0.08_300/.35)] focus-visible:translate-x-[0.05em] focus-visible:-translate-y-[0.14em] focus-visible:[text-shadow:.02em_.02em_0_var(--color-tth09-side),.045em_.045em_0_var(--color-tth09-side),.07em_.07em_0_var(--color-tth09-side),.095em_.095em_0_var(--color-tth09-side),.12em_.12em_0_var(--color-tth09-side),.145em_.145em_0_var(--color-tth09-side),.3em_.42em_1em_oklch(0.3_0.08_300/.35)] focus-visible:outline-3 focus-visible:outline-offset-[10px] focus-visible:outline-tth09-side active:translate-x-[0.01em] active:translate-y-[0.02em] active:duration-90 active:[text-shadow:.008em_.008em_0_var(--color-tth09-side),.016em_.016em_0_var(--color-tth09-side),.024em_.024em_0_var(--color-tth09-side),.03em_.03em_0_var(--color-tth09-side),.036em_.036em_0_var(--color-tth09-side),.042em_.042em_0_var(--color-tth09-side),.05em_.08em_.2em_oklch(0.3_0.08_300/.3)] motion-reduce:transition-none">JELLY<br>JAM &rsquo;26</a></h2>
    <p class="max-w-[44ch] text-[15px] font-medium leading-[1.65] text-tth09-mut">Two days of wobble-pop, jam stalls and the inflatable orchestra. Hover the headline &mdash; then actually press it.</p>
    <div class="mt-1 flex flex-wrap justify-center gap-3.5">
      <a href="#tth09-top" class="grid min-h-[52px] place-items-center rounded-[14px] border-[2.5px] border-tth09-ink bg-tth09-side px-[26px] text-[15.5px] font-extrabold text-tth09-paper no-underline shadow-[0_0_0_0_var(--color-tth09-ink),0_0_0_0_transparent] transition-[translate,box-shadow] duration-220 ease-[cubic-bezier(.34,1.8,.4,1)] hover:-translate-x-0.5 hover:-translate-y-[5px] hover:shadow-[4px_6px_0_0_var(--color-tth09-ink),10px_16px_26px_-6px_oklch(0.3_0.08_300/0.3)] focus-visible:-translate-y-[5px] focus-visible:shadow-[4px_6px_0_0_var(--color-tth09-ink)] focus-visible:outline-3 focus-visible:outline-offset-[3px] focus-visible:outline-tth09-side active:translate-x-px active:translate-y-0.5 active:shadow-[0_0_0_0_var(--color-tth09-ink),0_0_0_0_transparent] active:duration-80 motion-reduce:transition-none">Get tickets</a>
      <a href="#tth09-top" class="grid min-h-[52px] place-items-center rounded-[14px] border-[2.5px] border-tth09-ink bg-tth09-paper px-[26px] text-[15.5px] font-extrabold no-underline shadow-[0_0_0_0_var(--color-tth09-ink),0_0_0_0_transparent] transition-[translate,box-shadow] duration-220 ease-[cubic-bezier(.34,1.8,.4,1)] hover:-translate-x-0.5 hover:-translate-y-[5px] hover:shadow-[4px_6px_0_0_var(--color-tth09-ink),10px_16px_26px_-6px_oklch(0.3_0.08_300/0.3)] focus-visible:-translate-y-[5px] focus-visible:shadow-[4px_6px_0_0_var(--color-tth09-ink)] focus-visible:outline-3 focus-visible:outline-offset-[3px] focus-visible:outline-tth09-side active:translate-x-px active:translate-y-0.5 active:shadow-[0_0_0_0_var(--color-tth09-ink),0_0_0_0_transparent] active:duration-80 motion-reduce:transition-none">Line-up</a>
    </div>
    <p class="text-[12.5px] text-tth09-mut">Same-length <code class="rounded bg-tth09-chip px-1.5 py-px font-tth09-mono text-[0.9em]">text-shadow</code> lists interpolate &mdash; the extrusion grows, never blinks. <code class="rounded bg-tth09-chip px-1.5 py-px font-tth09-mono text-[0.9em]">active:</code> presses it back into the page.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth09-bg: #f6efd9;
  --color-tth09-bg: oklch(0.95 0.035 95);
  --color-tth09-glow: #fbf6e6;
  --color-tth09-glow: oklch(0.975 0.025 95);
  --color-tth09-paper: #fbf9f1;
  --color-tth09-paper: oklch(0.98 0.01 95);
  --color-tth09-chip: #eae1c6;
  --color-tth09-chip: oklch(0.9 0.035 95);
  --color-tth09-ink: #3d1c55;
  --color-tth09-ink: oklch(0.3 0.09 305);
  --color-tth09-mut: #5f4c69;
  --color-tth09-mut: oklch(0.45 0.05 300);
  --color-tth09-side: #ee6545;
  --color-tth09-side: oklch(0.68 0.19 30);
  --font-tth09-sans: 'Rubik', system-ui, sans-serif;
  --font-tth09-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-09 {
  width: 100%;
  min-height: 100svh;
}
```
