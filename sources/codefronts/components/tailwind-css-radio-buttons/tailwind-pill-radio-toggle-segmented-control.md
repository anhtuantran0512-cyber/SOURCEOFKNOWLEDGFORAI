---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-pill-radio-toggle-segmented-control/"
title: "Tailwind Pill Radio Toggle (Segmented Control)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "The iOS-style billing toggle — Monthly / Yearly with a save badge — where a white thumb glides under the chosen option."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pill Radio Toggle (Segmented Control)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-pill-radio-toggle-segmented-control/

The iOS-style billing toggle — Monthly / Yearly with a save badge — where a white thumb glides under the chosen option. The thumb is a before: pseudo-element on the track, moved by one arbitrary variant: has-[label:nth-child(2)_input:checked]:before:translate-x-full. The price below re-renders from the same radio state.
## HTML
```html
<section class="trb-02 w-full min-h-svh grid place-items-center bg-trb02-bg px-6 py-14 font-trb02-sans text-trb02-ink" aria-label="Pill radio toggle segmented control demo">
  <fieldset class="group/bill grid justify-items-center gap-5">
    <legend class="mb-1 text-center text-2xl font-bold tracking-[-0.02em]">Billing period</legend>
    <div class="relative isolate grid grid-flow-col auto-cols-fr rounded-full bg-trb02-track p-[5px] shadow-[inset_0_1px_3px_oklch(0.2_0.03_265/0.1)] before:absolute before:top-[5px] before:left-[5px] before:-z-10 before:h-[calc(100%-10px)] before:w-[calc(50%-5px)] before:rounded-full before:bg-white before:shadow-trb02-thumb before:transition-transform before:duration-350 before:ease-trb02-glide before:content-[''] has-[label:nth-child(2)_input:checked]:before:translate-x-full motion-reduce:before:transition-none">
      <label class="group relative grid min-h-11 min-w-[9.5rem] cursor-pointer place-items-center rounded-full px-5 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb02-acc">
        <input type="radio" name="trb-02" value="monthly" class="sr-only" checked>
        <span class="text-[15px] font-semibold text-trb02-mut transition-colors duration-300 group-has-checked:text-trb02-ink">Monthly</span>
      </label>
      <label class="group relative grid min-h-11 min-w-[9.5rem] cursor-pointer place-items-center rounded-full px-5 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb02-acc">
        <input type="radio" name="trb-02" value="yearly" class="sr-only">
        <span class="flex items-center gap-2 text-[15px] font-semibold text-trb02-mut transition-colors duration-300 group-has-checked:text-trb02-ink">Yearly <em class="rounded-full bg-trb02-acc/15 px-2 py-0.5 text-[11px] font-bold not-italic text-trb02-acc-ink">−20%</em></span>
      </label>
    </div>
    <p class="grid justify-items-center text-center">
      <span class="text-4xl font-extrabold tracking-[-0.03em] tabular-nums"><span class="group-has-[[value=yearly]:checked]/bill:hidden">$24</span><span class="hidden group-has-[[value=yearly]:checked]/bill:inline">$19</span><small class="text-base font-semibold text-trb02-mut"> / month</small></span>
      <span class="mt-1 text-[13px] text-trb02-mut"><span class="group-has-[[value=yearly]:checked]/bill:hidden">Billed monthly · cancel anytime</span><span class="hidden group-has-[[value=yearly]:checked]/bill:inline">Billed $228 yearly · you save $60</span></span>
    </p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb02-bg: #f7f8fb;
  --color-trb02-bg: oklch(0.978 0.005 265);
  --color-trb02-track: #e9ebf2;
  --color-trb02-track: oklch(0.938 0.01 270);
  --color-trb02-ink: #1c2130;
  --color-trb02-ink: oklch(0.24 0.03 270);
  --color-trb02-mut: #5d6479;
  --color-trb02-mut: oklch(0.5 0.03 270);
  --color-trb02-acc: #1f9d5c;
  --color-trb02-acc: oklch(0.6 0.15 155);
  --color-trb02-acc-ink: #11683b;
  --color-trb02-acc-ink: oklch(0.45 0.12 155);
  --shadow-trb02-thumb: 0 2px 8px oklch(0.2 0.03 265 / 0.16);
  --ease-trb02-glide: cubic-bezier(0.22, 1, 0.36, 1);
  --font-trb02-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-02 {
  width: 100%;
  min-height: 100svh;
}
```
