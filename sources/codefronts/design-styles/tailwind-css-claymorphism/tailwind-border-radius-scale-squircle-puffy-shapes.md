---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-border-radius-scale-squircle-puffy-shapes/"
title: "Tailwind Border Radius Scale & Squircle Corners for Puffy Shapes"
section: "design-styles"
category: "tailwind-css-claymorphism"
category_name: "Tailwind CSS Claymorphism"
description: "Radius is what makes clay clay."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Border Radius Scale & Squircle Corners for Puffy Shapes
Source: https://codefronts.com/design-styles/tailwind-css-claymorphism/tailwind-border-radius-scale-squircle-puffy-shapes/

Radius is what makes clay clay. This is the working scale — 16px to a hero 44px — minted as --radius-tcl03-* tokens so they become rounded-tcl03-lg utilities, plus the elliptical slash-syntax blob and corner-shape: squircle behind supports-[corner-shape:squircle]:. New: the flat→puffy ruler now tracks whichever shape you hover.
## HTML
```html
<section class="tcl-03 w-full min-h-svh grid place-items-center bg-tcl03-bg bg-[radial-gradient(85%_60%_at_50%_0%,var(--color-tcl03-glow),transparent_68%)] px-5 py-14 font-tcl03-sans text-tcl03-ink" aria-label="Border radius scale for puffy shapes demo">
  <div class="group/scale grid w-full justify-items-center gap-[clamp(26px,4vw,42px)]">
    <header class="grid max-w-[56ch] gap-2.5 text-center">
      <h2 class="font-tcl03-display text-[clamp(28px,4.2vw,40px)] font-extrabold leading-[1.05] tracking-[-0.03em] text-balance">The puffy radius scale</h2>
      <p class="text-[15px] leading-relaxed text-tcl03-mut text-pretty">Same size, same shadow, same fill. Only the corner changes — hover a shape and watch where a card becomes clay.</p>
    </header>
    <ul class="grid w-full max-w-[900px] grid-cols-[repeat(auto-fit,minmax(132px,1fr))] gap-[clamp(16px,2.5vw,26px)]">
      <li class="group grid justify-items-center gap-1 text-center text-[12.5px] text-tcl03-mut"><span aria-hidden="true" class="aspect-square w-full max-w-[124px] rounded-tcl03-sm bg-tcl03-clay shadow-tcl03-clay transition-[translate,scale] duration-300 ease-[cubic-bezier(.34,1.35,.5,1)] group-hover:-translate-y-2 group-hover:scale-[1.03] motion-reduce:transition-none"></span><b class="mt-3 font-tcl03-mono text-[13px] font-semibold text-tcl03-ink">16px</b><span>chips, tags</span></li>
      <li class="group grid justify-items-center gap-1 text-center text-[12.5px] text-tcl03-mut"><span aria-hidden="true" class="aspect-square w-full max-w-[124px] rounded-tcl03-md bg-tcl03-clay shadow-tcl03-clay transition-[translate,scale] duration-300 ease-[cubic-bezier(.34,1.35,.5,1)] group-hover:-translate-y-2 group-hover:scale-[1.03] motion-reduce:transition-none"></span><b class="mt-3 font-tcl03-mono text-[13px] font-semibold text-tcl03-ink">24px</b><span>inputs</span></li>
      <li class="group grid justify-items-center gap-1 text-center text-[12.5px] text-tcl03-mut"><span aria-hidden="true" class="aspect-square w-full max-w-[124px] rounded-tcl03-lg bg-tcl03-clay shadow-tcl03-clay transition-[translate,scale] duration-300 ease-[cubic-bezier(.34,1.35,.5,1)] group-hover:-translate-y-2 group-hover:scale-[1.03] motion-reduce:transition-none"></span><b class="mt-3 font-tcl03-mono text-[13px] font-semibold text-tcl03-ink">32px</b><span>cards, tiles</span></li>
      <li class="group grid justify-items-center gap-1 text-center text-[12.5px] text-tcl03-mut"><span aria-hidden="true" class="aspect-square w-full max-w-[124px] rounded-tcl03-xl bg-tcl03-clay shadow-tcl03-clay transition-[translate,scale] duration-300 ease-[cubic-bezier(.34,1.35,.5,1)] group-hover:-translate-y-2 group-hover:scale-[1.03] motion-reduce:transition-none"></span><b class="mt-3 font-tcl03-mono text-[13px] font-semibold text-tcl03-ink">44px</b><span>hero objects</span></li>
      <li class="group grid justify-items-center gap-1 text-center text-[12.5px] text-tcl03-mut"><span aria-hidden="true" class="aspect-square w-full max-w-[124px] rounded-[46%_38%_44%_40%/40%_46%_38%_44%] bg-tcl03-clay shadow-tcl03-clay transition-[translate,scale] duration-300 ease-[cubic-bezier(.34,1.35,.5,1)] group-hover:-translate-y-2 group-hover:scale-[1.03] motion-reduce:transition-none"></span><b class="mt-3 font-tcl03-mono text-[13px] font-semibold text-tcl03-ink">46% / 38%</b><span>elliptical blob</span></li>
      <li class="group grid justify-items-center gap-1 text-center text-[12.5px] text-tcl03-mut"><span aria-hidden="true" class="aspect-square w-full max-w-[124px] rounded-tcl03-lg bg-tcl03-clay shadow-tcl03-clay transition-[translate,scale] duration-300 ease-[cubic-bezier(.34,1.35,.5,1)] group-hover:-translate-y-2 group-hover:scale-[1.03] supports-[corner-shape:squircle]:rounded-[38%] supports-[corner-shape:squircle]:[corner-shape:squircle] motion-reduce:transition-none"></span><b class="mt-3 font-tcl03-mono text-[13px] font-semibold text-tcl03-ink">squircle</b><span>corner-shape</span></li>
    </ul>
    <div class="flex w-full max-w-[540px] items-center gap-3.5 text-[11.5px] font-semibold uppercase tracking-[0.12em] text-tcl03-mut">
      <span>flat</span>
      <span aria-hidden="true" class="h-3 flex-1 overflow-hidden rounded-full bg-tcl03-soft shadow-tcl03-track"><i class="block h-full w-[60%] rounded-full bg-tcl03-clay shadow-[inset_0_6px_8px_-6px_var(--color-tcl03-light)] transition-[width] duration-500 ease-[cubic-bezier(.34,1.3,.5,1)] group-has-[li:nth-child(1):hover]/scale:w-[16%] group-has-[li:nth-child(2):hover]/scale:w-[32%] group-has-[li:nth-child(3):hover]/scale:w-[52%] group-has-[li:nth-child(4):hover]/scale:w-[72%] group-has-[li:nth-child(5):hover]/scale:w-[90%] group-has-[li:nth-child(6):hover]/scale:w-full motion-reduce:transition-none"></i></span>
      <span>puffy</span>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/55 px-4 py-2 text-center font-tcl03-mono text-[11.5px] text-tcl03-mut shadow-tcl03-chip">rounded-tcl03-xl · slash syntax · supports-[corner-shape:squircle]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcl03-bg: #d1f3f2;
  --color-tcl03-bg: oklch(0.94 0.035 195);
  --color-tcl03-glow: #e1fdff;
  --color-tcl03-glow: oklch(0.975 0.03 200);
  --color-tcl03-clay: #68d4e0;
  --color-tcl03-clay: oklch(0.81 0.1 205);
  --color-tcl03-shade: color-mix(in oklch, var(--color-tcl03-clay) 45%, oklch(0.4 0.1 220));
  --color-tcl03-light: #edfffff2;
  --color-tcl03-light: oklch(0.99 0.02 200 / 0.95);
  --color-tcl03-ink: #012e3a;
  --color-tcl03-ink: oklch(0.28 0.05 220);
  --color-tcl03-mut: #325c67;
  --color-tcl03-mut: oklch(0.45 0.05 215);
  --color-tcl03-soft: color-mix(in oklch, var(--color-tcl03-bg) 84%, white);
  --font-tcl03-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcl03-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcl03-mono: 'JetBrains Mono', ui-monospace, monospace;
  --radius-tcl03-sm: 16px;
  --radius-tcl03-md: 24px;
  --radius-tcl03-lg: 32px;
  --radius-tcl03-xl: 44px;
  --shadow-tcl03-clay: 0 20px 34px -14px var(--color-tcl03-shade), inset 0 -14px 22px -10px var(--color-tcl03-shade), inset 0 16px 22px -8px var(--color-tcl03-light);
  --shadow-tcl03-track: inset 0 -5px 10px -6px var(--color-tcl03-shade), inset 0 6px 10px -5px var(--color-tcl03-light);
  --shadow-tcl03-chip: inset 0 -4px 10px -8px var(--color-tcl03-shade), inset 0 6px 10px -6px white;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcl-03 {
  width: 100%;
  min-height: 100svh;
}
```
