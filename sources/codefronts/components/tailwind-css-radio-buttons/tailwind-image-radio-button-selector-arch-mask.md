---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-image-radio-button-selector-arch-mask/"
title: "Tailwind Image Radio Button Selector (Arch Mask)"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "A destination picker where photography is the control: each option is a photo in a tall arch."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Radio Button Selector (Arch Mask)
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-image-radio-button-selector-arch-mask/

A destination picker where photography is the control: each option is a photo in a tall arch. Unselected images rest desaturated; picking one blooms it to full colour, relaxes the arch into a soft rounded card and slides the caption up. The mask morph is just rounded-[85px_85px_18px_18px] → group-has-checked:rounded-[26px] — border-radius interpolates natively.
## HTML
```html
<section class="trb-19 w-full min-h-svh grid place-items-center bg-trb19-bg px-6 py-14 font-trb19-sans text-trb19-ink" aria-label="Image clip mask option selector demo">
  <fieldset>
    <legend class="text-center font-trb19-serif text-[40px] leading-none italic">Where to next?</legend>
    <div class="mt-9 flex flex-wrap justify-center gap-6">
      <label class="group relative cursor-pointer">
        <input type="radio" name="trb-19" value="alps" class="sr-only" checked>
        <span class="relative block h-[16.5rem] w-44 overflow-hidden rounded-[88px_88px_18px_18px] transition-[border-radius,translate,box-shadow] duration-500 ease-trb19-relax group-has-checked:rounded-[26px] group-has-checked:shadow-trb19-lift group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-4 group-has-focus-visible:outline-trb19-ink motion-safe:group-has-checked:-translate-y-1.5">
          <img class="size-full scale-108 object-cover brightness-65 grayscale transition-[filter,scale] duration-550 ease-trb19-relax group-hover:brightness-85 group-hover:grayscale-40 group-has-checked:scale-100 group-has-checked:brightness-100 group-has-checked:grayscale-0 motion-reduce:transition-[filter]" src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=480&q=80&auto=format&fit=crop" alt="Snow-capped alpine peaks at dawn" loading="lazy">
          <span class="absolute inset-x-0 bottom-0 grid translate-y-2.5 bg-linear-to-b from-transparent to-black/75 px-3.5 pt-8 pb-3 text-center opacity-80 transition-[translate,opacity] duration-400 group-has-checked:translate-y-0 group-has-checked:opacity-100"><span class="font-trb19-serif text-[22px] leading-tight text-white">The Alps</span><span class="text-xs text-white/85">7 nights · from $1,240</span></span>
        </span>
      </label>
      <label class="group relative cursor-pointer">
        <input type="radio" name="trb-19" value="coast" class="sr-only">
        <span class="relative block h-[16.5rem] w-44 overflow-hidden rounded-[88px_88px_18px_18px] transition-[border-radius,translate,box-shadow] duration-500 ease-trb19-relax group-has-checked:rounded-[26px] group-has-checked:shadow-trb19-lift group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-4 group-has-focus-visible:outline-trb19-ink motion-safe:group-has-checked:-translate-y-1.5">
          <img class="size-full scale-108 object-cover brightness-65 grayscale transition-[filter,scale] duration-550 ease-trb19-relax group-hover:brightness-85 group-hover:grayscale-40 group-has-checked:scale-100 group-has-checked:brightness-100 group-has-checked:grayscale-0 motion-reduce:transition-[filter]" src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=480&q=80&auto=format&fit=crop" alt="Turquoise water on a white sand beach" loading="lazy">
          <span class="absolute inset-x-0 bottom-0 grid translate-y-2.5 bg-linear-to-b from-transparent to-black/75 px-3.5 pt-8 pb-3 text-center opacity-80 transition-[translate,opacity] duration-400 group-has-checked:translate-y-0 group-has-checked:opacity-100"><span class="font-trb19-serif text-[22px] leading-tight text-white">The Coast</span><span class="text-xs text-white/85">5 nights · from $980</span></span>
        </span>
      </label>
      <label class="group relative cursor-pointer">
        <input type="radio" name="trb-19" value="forest" class="sr-only">
        <span class="relative block h-[16.5rem] w-44 overflow-hidden rounded-[88px_88px_18px_18px] transition-[border-radius,translate,box-shadow] duration-500 ease-trb19-relax group-has-checked:rounded-[26px] group-has-checked:shadow-trb19-lift group-has-focus-visible:outline-3 group-has-focus-visible:outline-offset-4 group-has-focus-visible:outline-trb19-ink motion-safe:group-has-checked:-translate-y-1.5">
          <img class="size-full scale-108 object-cover brightness-65 grayscale transition-[filter,scale] duration-550 ease-trb19-relax group-hover:brightness-85 group-hover:grayscale-40 group-has-checked:scale-100 group-has-checked:brightness-100 group-has-checked:grayscale-0 motion-reduce:transition-[filter]" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=480&q=80&auto=format&fit=crop" alt="Sunlight through a tall green forest" loading="lazy">
          <span class="absolute inset-x-0 bottom-0 grid translate-y-2.5 bg-linear-to-b from-transparent to-black/75 px-3.5 pt-8 pb-3 text-center opacity-80 transition-[translate,opacity] duration-400 group-has-checked:translate-y-0 group-has-checked:opacity-100"><span class="font-trb19-serif text-[22px] leading-tight text-white">The Forest</span><span class="text-xs text-white/85">4 nights · from $760</span></span>
        </span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb19-bg: #141210;
  --color-trb19-bg: oklch(0.19 0.006 70);
  --color-trb19-ink: #f4efe8;
  --color-trb19-ink: oklch(0.955 0.01 75);
  --shadow-trb19-lift: 0 26px 50px -22px oklch(0 0 0 / 0.85);
  --ease-trb19-relax: cubic-bezier(0.22, 1, 0.36, 1);
  --font-trb19-serif: 'Instrument Serif', Georgia, serif;
  --font-trb19-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-19 {
  width: 100%;
  min-height: 100svh;
}
```
