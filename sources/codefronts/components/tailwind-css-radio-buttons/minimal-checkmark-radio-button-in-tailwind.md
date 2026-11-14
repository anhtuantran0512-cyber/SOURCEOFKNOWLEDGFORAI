---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/minimal-checkmark-radio-button-in-tailwind/"
title: "Minimal Checkmark Radio Button in Tailwind"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "Radical restraint: a typography-first list where the only ornament is a checkmark that draws itself."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Checkmark Radio Button in Tailwind
Source: https://codefronts.com/components/tailwind-css-radio-buttons/minimal-checkmark-radio-button-in-tailwind/

Radical restraint: a typography-first list where the only ornament is a checkmark that draws itself. The tick is an SVG polyline animated with [stroke-dashoffset:28] → group-has-checked:[stroke-dashoffset:0], and each option now previews itself — the grotesk, serif and mono choices are set in the faces they name.
## HTML
```html
<section class="trb-13 w-full min-h-svh grid place-items-center bg-trb13-bg px-6 py-14 font-trb13-sans text-trb13-ink" aria-label="Minimal checkmark radio buttons demo">
  <fieldset class="w-full max-w-[22rem]">
    <legend class="text-xs font-semibold tracking-[0.18em] text-trb13-mut uppercase">Typeface</legend>
    <div class="mt-3.5 grid">
      <label class="group relative flex min-h-16 cursor-pointer items-center gap-3.5 border-b border-trb13-line has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-trb13-ink"><input type="radio" name="trb-13" value="grotesk" class="sr-only" checked><svg class="size-5 flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline class="[stroke-dasharray:28] [stroke-dashoffset:28] transition-[stroke-dashoffset] duration-350 ease-trb13-draw group-has-checked:[stroke-dashoffset:0] motion-reduce:transition-none" points="4.5 12.5 9.5 17.5 19.5 6.5"/></svg><span class="font-trb13-sans text-[21px] font-medium tracking-[-0.02em] text-trb13-ink/60 transition-colors duration-300 group-hover:text-trb13-ink/80 group-has-checked:text-trb13-ink">Neue Grotesk</span><span class="ml-auto font-trb13-mono text-[11px] text-trb13-mut">Sans</span></label>
      <label class="group relative flex min-h-16 cursor-pointer items-center gap-3.5 border-b border-trb13-line has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-trb13-ink"><input type="radio" name="trb-13" value="serif" class="sr-only"><svg class="size-5 flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline class="[stroke-dasharray:28] [stroke-dashoffset:28] transition-[stroke-dashoffset] duration-350 ease-trb13-draw group-has-checked:[stroke-dashoffset:0] motion-reduce:transition-none" points="4.5 12.5 9.5 17.5 19.5 6.5"/></svg><span class="font-trb13-serif text-[26px] leading-none text-trb13-ink/60 italic transition-colors duration-300 group-hover:text-trb13-ink/80 group-has-checked:text-trb13-ink">Editorial Serif</span><span class="ml-auto font-trb13-mono text-[11px] text-trb13-mut">Serif</span></label>
      <label class="group relative flex min-h-16 cursor-pointer items-center gap-3.5 border-b border-trb13-line has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-trb13-ink"><input type="radio" name="trb-13" value="mono" class="sr-only"><svg class="size-5 flex-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline class="[stroke-dasharray:28] [stroke-dashoffset:28] transition-[stroke-dashoffset] duration-350 ease-trb13-draw group-has-checked:[stroke-dashoffset:0] motion-reduce:transition-none" points="4.5 12.5 9.5 17.5 19.5 6.5"/></svg><span class="font-trb13-mono text-lg tracking-[-0.02em] text-trb13-ink/60 transition-colors duration-300 group-hover:text-trb13-ink/80 group-has-checked:text-trb13-ink">Studio Mono</span><span class="ml-auto font-trb13-mono text-[11px] text-trb13-mut">Mono</span></label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb13-bg: #fcfcfa;
  --color-trb13-bg: oklch(0.99 0.003 100);
  --color-trb13-ink: #191919;
  --color-trb13-ink: oklch(0.21 0 0);
  --color-trb13-mut: #6b6b66;
  --color-trb13-mut: oklch(0.52 0.008 100);
  --color-trb13-line: #e6e6e0;
  --color-trb13-line: oklch(0.92 0.006 100);
  --ease-trb13-draw: cubic-bezier(0.22, 1, 0.36, 1);
  --font-trb13-sans: 'Geist', system-ui, sans-serif;
  --font-trb13-serif: 'Instrument Serif', Georgia, serif;
  --font-trb13-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-13 {
  width: 100%;
  min-height: 100svh;
}
```
