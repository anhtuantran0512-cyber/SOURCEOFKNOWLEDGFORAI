---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-color-swatch-radio-picker/"
title: "Tailwind Color Swatch Radio Picker"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "The e-commerce essential: circular colour swatches that are radio buttons, wired to a product photo that retints the moment you pick."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Color Swatch Radio Picker
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-color-swatch-radio-picker/

The e-commerce essential: circular colour swatches that are radio buttons, wired to a product photo that retints the moment you pick. The checked ring is Tailwind's own ring-2 ring-offset-3 ring-offset-trb14-bg, the swatch edge is inset-ring, and the photo filter, caption and stock note all switch with group-has-[[value=…]:checked]/pdp:.
## HTML
```html
<section class="trb-14 w-full min-h-svh grid place-items-center bg-trb14-bg px-6 py-14 font-trb14-sans text-trb14-ink" aria-label="Product color swatch selector demo">
  <div class="group/pdp flex flex-wrap items-center justify-center gap-10">
    <figure class="aspect-[4/5] w-[min(300px,80vw)] overflow-hidden rounded-3xl bg-trb14-media shadow-trb14-media">
      <img class="size-full object-cover transition-[filter] duration-500 group-has-[[value=ocean]:checked]/pdp:[filter:sepia(.9)_saturate(2.2)_hue-rotate(170deg)_brightness(.82)] group-has-[[value=sage]:checked]/pdp:[filter:sepia(.8)_saturate(1.6)_hue-rotate(70deg)_brightness(.9)] group-has-[[value=clay]:checked]/pdp:[filter:sepia(.95)_saturate(2)_hue-rotate(-15deg)_brightness(.85)] motion-reduce:transition-none" src="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=640&q=80&auto=format&fit=crop" alt="Classic crew-neck t-shirt on a hanger" loading="lazy">
    </figure>
    <fieldset class="w-64">
      <legend class="text-[26px] font-extrabold tracking-[-0.02em]">Classic Crew Tee</legend>
      <p class="mt-1 text-lg font-semibold">$38</p>
      <p class="mt-5 flex gap-1.5 text-sm text-trb14-mut">Colour:
        <span class="hidden font-bold text-trb14-ink group-has-[[value=natural]:checked]/pdp:inline">Natural white</span><span class="hidden font-bold text-trb14-ink group-has-[[value=ocean]:checked]/pdp:inline">Ocean blue</span><span class="hidden font-bold text-trb14-ink group-has-[[value=sage]:checked]/pdp:inline">Sage green</span><span class="hidden font-bold text-trb14-ink group-has-[[value=clay]:checked]/pdp:inline">Baked clay</span>
      </p>
      <div class="mt-3.5 flex gap-3.5">
        <label class="relative size-11 cursor-pointer rounded-full bg-(--sw) inset-ring inset-ring-black/12 ring-offset-trb14-bg transition-[scale,box-shadow] duration-250 ease-trb14-spring [--sw:#ece7dd] hover:scale-110 has-checked:scale-108 has-checked:ring-2 has-checked:ring-trb14-ink has-checked:ring-offset-3 has-focus-visible:outline-3 has-focus-visible:outline-offset-[7px] has-focus-visible:outline-trb14-ink motion-reduce:scale-100!"><input type="radio" name="trb-14" value="natural" class="sr-only" checked><span class="sr-only">Natural white</span></label>
        <label class="relative size-11 cursor-pointer rounded-full bg-(--sw) inset-ring inset-ring-black/12 ring-offset-trb14-bg transition-[scale,box-shadow] duration-250 ease-trb14-spring [--sw:oklch(0.55_0.12_240)] hover:scale-110 has-checked:scale-108 has-checked:ring-2 has-checked:ring-trb14-ink has-checked:ring-offset-3 has-focus-visible:outline-3 has-focus-visible:outline-offset-[7px] has-focus-visible:outline-trb14-ink motion-reduce:scale-100!"><input type="radio" name="trb-14" value="ocean" class="sr-only"><span class="sr-only">Ocean blue</span></label>
        <label class="relative size-11 cursor-pointer rounded-full bg-(--sw) inset-ring inset-ring-black/12 ring-offset-trb14-bg transition-[scale,box-shadow] duration-250 ease-trb14-spring [--sw:oklch(0.62_0.09_150)] hover:scale-110 has-checked:scale-108 has-checked:ring-2 has-checked:ring-trb14-ink has-checked:ring-offset-3 has-focus-visible:outline-3 has-focus-visible:outline-offset-[7px] has-focus-visible:outline-trb14-ink motion-reduce:scale-100!"><input type="radio" name="trb-14" value="sage" class="sr-only"><span class="sr-only">Sage green</span></label>
        <label class="relative size-11 cursor-pointer rounded-full bg-(--sw) inset-ring inset-ring-black/12 ring-offset-trb14-bg transition-[scale,box-shadow] duration-250 ease-trb14-spring [--sw:oklch(0.58_0.11_45)] hover:scale-110 has-checked:scale-108 has-checked:ring-2 has-checked:ring-trb14-ink has-checked:ring-offset-3 has-focus-visible:outline-3 has-focus-visible:outline-offset-[7px] has-focus-visible:outline-trb14-ink motion-reduce:scale-100!"><input type="radio" name="trb-14" value="clay" class="sr-only"><span class="sr-only">Baked clay</span></label>
      </div>
      <p class="mt-5 flex items-center gap-2 text-[13px] text-trb14-mut">
        <span aria-hidden="true" class="size-2 rounded-full bg-trb14-ok group-has-[[value=clay]:checked]/pdp:bg-trb14-low"></span>
        <span class="group-has-[[value=clay]:checked]/pdp:hidden">In stock · ships in 1–2 days</span><span class="hidden group-has-[[value=clay]:checked]/pdp:inline">Only 3 left in this colour</span>
      </p>
    </fieldset>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb14-bg: #f5f3ef;
  --color-trb14-bg: oklch(0.965 0.006 80);
  --color-trb14-media: #e8e4dc;
  --color-trb14-media: oklch(0.92 0.01 80);
  --color-trb14-ink: #211f1c;
  --color-trb14-ink: oklch(0.23 0.006 70);
  --color-trb14-mut: #625c52;
  --color-trb14-mut: oklch(0.47 0.015 75);
  --color-trb14-ok: #22a060;
  --color-trb14-ok: oklch(0.62 0.15 155);
  --color-trb14-low: #e07a1f;
  --color-trb14-low: oklch(0.68 0.16 55);
  --shadow-trb14-media: 0 30px 60px -30px oklch(0.3 0.02 70 / 0.35);
  --ease-trb14-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-14 {
  width: 100%;
  min-height: 100svh;
}
```
