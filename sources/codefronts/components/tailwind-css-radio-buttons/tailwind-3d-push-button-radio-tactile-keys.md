---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-3d-push-button-radio-tactile-keys/"
title: "Tailwind 3D Push Button Radio (Tactile Keys)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "Radio options as chunky mechanical keys: each sits proud on a hard shadow base, and the selected key stays pressed down — travel, shadow and a darker cap all…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Push Button Radio (Tactile Keys)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-3d-push-button-radio-tactile-keys/

Radio options as chunky mechanical keys: each sits proud on a hard shadow base, and the selected key stays pressed down — travel, shadow and a darker cap all agree it's IN. Three elevation tokens (shadow-trb23-up, -hover, -down) pair with translate utilities, and group-active: previews the travel mid-click.
## HTML
```html
<section class="trb-23 w-full min-h-svh grid place-items-center bg-trb23-bg px-6 py-14 font-trb23-sans text-trb23-ink" aria-label="Tactile 3D push button radio demo">
  <fieldset class="group/deck grid justify-items-center">
    <legend class="text-center text-[26px] font-bold tracking-[-0.02em]">Drive mode</legend>
    <div class="mt-8 flex flex-wrap justify-center gap-[18px] rounded-[20px] bg-trb23-deck px-[26px] pt-7 pb-5 shadow-[inset_0_2px_6px_oklch(0.35_0.03_80/0.25)]">
      <label class="group relative cursor-pointer"><input type="radio" name="trb-23" value="eco" class="sr-only"><span class="flex min-w-[7.5rem] -translate-y-1.5 items-center justify-center gap-2.5 rounded-xl bg-linear-to-b from-white to-trb23-cap px-6 py-[15px] text-[15px] font-bold shadow-trb23-up transition-[translate,box-shadow,background-color] duration-120 ease-out group-hover:-translate-y-[7px] group-hover:shadow-trb23-hover group-active:-translate-y-px group-active:shadow-trb23-down group-has-checked:-translate-y-px group-has-checked:from-trb23-cap group-has-checked:to-trb23-cap-down group-has-checked:shadow-trb23-down group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-trb23-ink"><span aria-hidden="true" class="size-2 rounded-full bg-trb23-led-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.25)] transition-[background-color,box-shadow] duration-150 group-has-checked:bg-trb23-led group-has-checked:shadow-trb23-led"></span>Eco</span></label>
      <label class="group relative cursor-pointer"><input type="radio" name="trb-23" value="comfort" class="sr-only" checked><span class="flex min-w-[7.5rem] -translate-y-1.5 items-center justify-center gap-2.5 rounded-xl bg-linear-to-b from-white to-trb23-cap px-6 py-[15px] text-[15px] font-bold shadow-trb23-up transition-[translate,box-shadow,background-color] duration-120 ease-out group-hover:-translate-y-[7px] group-hover:shadow-trb23-hover group-active:-translate-y-px group-active:shadow-trb23-down group-has-checked:-translate-y-px group-has-checked:from-trb23-cap group-has-checked:to-trb23-cap-down group-has-checked:shadow-trb23-down group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-trb23-ink"><span aria-hidden="true" class="size-2 rounded-full bg-trb23-led-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.25)] transition-[background-color,box-shadow] duration-150 group-has-checked:bg-trb23-led group-has-checked:shadow-trb23-led"></span>Comfort</span></label>
      <label class="group relative cursor-pointer"><input type="radio" name="trb-23" value="sport" class="sr-only"><span class="flex min-w-[7.5rem] -translate-y-1.5 items-center justify-center gap-2.5 rounded-xl bg-linear-to-b from-white to-trb23-cap px-6 py-[15px] text-[15px] font-bold shadow-trb23-up transition-[translate,box-shadow,background-color] duration-120 ease-out group-hover:-translate-y-[7px] group-hover:shadow-trb23-hover group-active:-translate-y-px group-active:shadow-trb23-down group-has-checked:-translate-y-px group-has-checked:from-trb23-cap group-has-checked:to-trb23-cap-down group-has-checked:shadow-trb23-down group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-3 group-has-focus-visible:outline-trb23-ink"><span aria-hidden="true" class="size-2 rounded-full bg-trb23-led-off shadow-[inset_0_1px_2px_oklch(0_0_0/0.25)] transition-[background-color,box-shadow] duration-150 group-has-checked:bg-trb23-led group-has-checked:shadow-trb23-led"></span>Sport</span></label>
    </div>
    <p class="mt-5 flex items-baseline gap-2 text-sm text-trb23-mut">Est. range
      <strong class="text-xl font-bold text-trb23-ink tabular-nums"><span class="hidden group-has-[[value=eco]:checked]/deck:inline">412 km</span><span class="hidden group-has-[[value=comfort]:checked]/deck:inline">368 km</span><span class="hidden group-has-[[value=sport]:checked]/deck:inline">301 km</span></strong>
    </p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb23-bg: #dcd5c8;
  --color-trb23-bg: oklch(0.87 0.018 80);
  --color-trb23-deck: #cfc7b7;
  --color-trb23-deck: oklch(0.83 0.022 80);
  --color-trb23-cap: #f2ede4;
  --color-trb23-cap: oklch(0.945 0.012 80);
  --color-trb23-cap-down: #e6dfd0;
  --color-trb23-cap-down: oklch(0.9 0.018 80);
  --color-trb23-ink: #3a3428;
  --color-trb23-ink: oklch(0.33 0.02 80);
  --color-trb23-mut: #5a5243;
  --color-trb23-mut: oklch(0.43 0.025 80);
  --color-trb23-led: #33c46a;
  --color-trb23-led: oklch(0.72 0.17 148);
  --color-trb23-led-off: #b8b0a0;
  --color-trb23-led-off: oklch(0.76 0.02 80);
  --shadow-trb23-up: 0 6px 0 #b3a88f, 0 10px 14px -4px oklch(0.35 0.03 80 / 0.35), inset 0 1px 0 #fff;
  --shadow-trb23-hover: 0 7px 0 #b3a88f, 0 12px 16px -4px oklch(0.35 0.03 80 / 0.35), inset 0 1px 0 #fff;
  --shadow-trb23-down: 0 1px 0 #b3a88f, 0 2px 4px -2px oklch(0.35 0.03 80 / 0.3), inset 0 2px 4px oklch(0.35 0.03 80 / 0.18);
  --shadow-trb23-led: 0 0 6px oklch(0.72 0.17 148), 0 0 14px oklch(0.72 0.17 148 / 0.55);
  --font-trb23-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-23 {
  width: 100%;
  min-height: 100svh;
}
```
