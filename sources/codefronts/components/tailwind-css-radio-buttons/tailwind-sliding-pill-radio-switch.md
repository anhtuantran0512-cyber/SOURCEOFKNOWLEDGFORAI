---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-sliding-pill-radio-switch/"
title: "Tailwind Sliding Pill Radio Switch"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "A three-way pill where the thumb glides between options and changes colour as it lands — Pickup amber, Delivery green, Dine-in violet."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sliding Pill Radio Switch
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-sliding-pill-radio-switch/

A three-way pill where the thumb glides between options and changes colour as it lands — Pickup amber, Delivery green, Dine-in violet. Position and hue come from one custom property per state: has-[label:nth-child(2)_input:checked]:[--thumb:…] on the track, read by before:bg-(--thumb).
## HTML
```html
<section class="trb-08 w-full min-h-svh grid place-items-center bg-trb08-bg px-6 py-14 font-trb08-sans text-trb08-ink" aria-label="Sliding pill toggle switch demo">
  <fieldset class="group/how grid justify-items-center gap-5">
    <legend class="mb-1 text-center text-[26px] font-extrabold tracking-[-0.025em]">How do you want it?</legend>
    <div class="relative isolate grid grid-cols-3 rounded-full bg-trb08-track p-[5px] shadow-[inset_0_1px_3px_oklch(0.3_0.04_70/0.14)] [--thumb:var(--color-trb08-amber)] before:absolute before:top-[5px] before:left-[5px] before:-z-10 before:h-[calc(100%-10px)] before:w-[calc(33.333%-3.33px)] before:rounded-full before:bg-(--thumb) before:shadow-trb08-thumb before:transition-[translate,background-color] before:duration-400 before:ease-trb08-glide before:content-[''] has-[label:nth-child(2)_input:checked]:[--thumb:var(--color-trb08-green)] has-[label:nth-child(2)_input:checked]:before:translate-x-full has-[label:nth-child(3)_input:checked]:[--thumb:var(--color-trb08-violet)] has-[label:nth-child(3)_input:checked]:before:translate-x-[200%] motion-reduce:before:transition-[background-color]">
      <label class="group relative grid min-h-12 min-w-[6.5rem] cursor-pointer place-items-center rounded-full px-4 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb08-ink sm:min-w-[7.5rem]"><input type="radio" name="trb-08" value="pickup" class="sr-only" checked><span class="text-[15px] font-bold text-trb08-mut transition-colors duration-300 group-has-checked:text-trb08-ink">Pickup</span></label>
      <label class="group relative grid min-h-12 min-w-[6.5rem] cursor-pointer place-items-center rounded-full px-4 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb08-ink sm:min-w-[7.5rem]"><input type="radio" name="trb-08" value="delivery" class="sr-only"><span class="text-[15px] font-bold text-trb08-mut transition-colors duration-300 group-has-checked:text-white">Delivery</span></label>
      <label class="group relative grid min-h-12 min-w-[6.5rem] cursor-pointer place-items-center rounded-full px-4 has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb08-ink sm:min-w-[7.5rem]"><input type="radio" name="trb-08" value="dinein" class="sr-only"><span class="text-[15px] font-bold text-trb08-mut transition-colors duration-300 group-has-checked:text-white">Dine-in</span></label>
    </div>
    <p class="text-center text-sm text-trb08-mut">
      <span class="hidden group-has-[[value=pickup]:checked]/how:inline">Ready in <strong class="font-bold text-trb08-ink">15 min</strong> at 214 Bleecker St.</span>
      <span class="hidden group-has-[[value=delivery]:checked]/how:inline">At your door in <strong class="font-bold text-trb08-ink">30–40 min</strong> · $3.99 fee</span>
      <span class="hidden group-has-[[value=dinein]:checked]/how:inline">Table for two held until <strong class="font-bold text-trb08-ink">7:30 pm</strong></span>
    </p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb08-bg: #faf7f2;
  --color-trb08-bg: oklch(0.978 0.008 80);
  --color-trb08-track: #efe9df;
  --color-trb08-track: oklch(0.935 0.015 80);
  --color-trb08-ink: #221d16;
  --color-trb08-ink: oklch(0.23 0.015 70);
  --color-trb08-mut: #6b6252;
  --color-trb08-mut: oklch(0.5 0.025 80);
  --color-trb08-amber: #f0b43c;
  --color-trb08-amber: oklch(0.8 0.15 78);
  --color-trb08-green: #17864f;
  --color-trb08-green: oklch(0.55 0.14 155);
  --color-trb08-violet: #7a3fc8;
  --color-trb08-violet: oklch(0.5 0.2 300);
  --shadow-trb08-thumb: 0 3px 10px oklch(0.3 0.05 70 / 0.22);
  --ease-trb08-glide: cubic-bezier(0.22, 1, 0.36, 1);
  --font-trb08-sans: 'Bricolage Grotesque', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-08 {
  width: 100%;
  min-height: 100svh;
}
```
