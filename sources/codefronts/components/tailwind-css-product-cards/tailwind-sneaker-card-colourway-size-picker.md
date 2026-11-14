---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-sneaker-card-colourway-size-picker/"
title: "Tailwind Sneaker Card with Colourway &amp; Size Picker"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "Colourway swatches that retint the whole card and a row of size chips — no JavaScript, and in v4 no bespoke selectors either."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sneaker Card with Colourway &amp; Size Picker
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-sneaker-card-colourway-size-picker/

Colourway swatches that retint the whole card and a row of size chips — no JavaScript, and in v4 no bespoke selectors either. peer-checked: styles the swatch from its own hidden radio, and has-[.tpc14-sw1_input:checked]:[--tint:…] on the root turns the picked colour into a live custom property the media and CTA both read.
## HTML
```html
<section class="tpc-14 w-full min-h-svh grid place-items-center bg-tpc14-bg font-tpc14-sans px-5 py-12 [--tint:oklch(0.6_0.16_25)] has-[.tpc14-sw1_input:checked]:[--tint:oklch(0.6_0.16_25)] has-[.tpc14-sw2_input:checked]:[--tint:oklch(0.6_0.14_250)] has-[.tpc14-sw3_input:checked]:[--tint:oklch(0.62_0.15_150)] has-[.tpc14-sw4_input:checked]:[--tint:oklch(0.42_0.03_260)]" aria-label="Sneaker colourway and size picker demo">
  <article class="w-[min(340px,100%)] rounded-[20px] overflow-hidden bg-tpc14-card shadow-[0_18px_44px_-24px_oklch(0.25_0.03_260/0.45)]">
    <div role="img" aria-label="Product photo: Aurora Runner sneaker" class="aspect-[16/11] bg-[image:linear-gradient(135deg,color-mix(in_oklch,var(--tint)_42%,transparent),color-mix(in_oklch,var(--tint)_16%,transparent)),url('https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?w=800&h=550&fit=crop&q=70')] bg-cover bg-center transition-[background] duration-400 motion-reduce:transition-none"></div>
    <div class="px-5 pt-4.5 pb-5">
      <p class="font-tpc14-sans text-[11px] font-medium tracking-[0.2em] uppercase text-tpc14-mut">Aerolite</p>
      <h3 class="mt-1 text-[20px] font-bold text-tpc14-ink">Aurora Runner</h3>

      <fieldset class="mt-4 border-0">
        <legend class="mb-2 text-[11px] font-bold tracking-[0.08em] uppercase text-tpc14-mut">Colour</legend>
        <div class="flex gap-2.5">
          <label class="tpc14-sw1 cursor-pointer [--sw:oklch(0.6_0.16_25)]">
            <input type="radio" name="tpc14-color" class="peer sr-only" checked>
            <span aria-hidden="true" class="block size-7 rounded-full bg-[var(--sw)] shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_3px_var(--color-tpc14-edge)] transition-[box-shadow,transform] duration-200 hover:scale-108 peer-checked:shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_3px_var(--sw),0_0_0_5px_color-mix(in_oklch,var(--sw)_30%,oklch(1_0_0))] peer-focus-visible:shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_4px_var(--color-tpc14-ink)] motion-reduce:transition-none"></span>
            <span class="sr-only">Ember red</span>
          </label>
          <label class="tpc14-sw2 cursor-pointer [--sw:oklch(0.6_0.14_250)]">
            <input type="radio" name="tpc14-color" class="peer sr-only">
            <span aria-hidden="true" class="block size-7 rounded-full bg-[var(--sw)] shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_3px_var(--color-tpc14-edge)] transition-[box-shadow,transform] duration-200 hover:scale-108 peer-checked:shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_3px_var(--sw),0_0_0_5px_color-mix(in_oklch,var(--sw)_30%,oklch(1_0_0))] peer-focus-visible:shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_4px_var(--color-tpc14-ink)] motion-reduce:transition-none"></span>
            <span class="sr-only">Cobalt blue</span>
          </label>
          <label class="tpc14-sw3 cursor-pointer [--sw:oklch(0.62_0.15_150)]">
            <input type="radio" name="tpc14-color" class="peer sr-only">
            <span aria-hidden="true" class="block size-7 rounded-full bg-[var(--sw)] shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_3px_var(--color-tpc14-edge)] transition-[box-shadow,transform] duration-200 hover:scale-108 peer-checked:shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_3px_var(--sw),0_0_0_5px_color-mix(in_oklch,var(--sw)_30%,oklch(1_0_0))] peer-focus-visible:shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_4px_var(--color-tpc14-ink)] motion-reduce:transition-none"></span>
            <span class="sr-only">Pine green</span>
          </label>
          <label class="tpc14-sw4 cursor-pointer [--sw:oklch(0.42_0.03_260)]">
            <input type="radio" name="tpc14-color" class="peer sr-only">
            <span aria-hidden="true" class="block size-7 rounded-full bg-[var(--sw)] shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_3px_var(--color-tpc14-edge)] transition-[box-shadow,transform] duration-200 hover:scale-108 peer-checked:shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_3px_var(--sw),0_0_0_5px_color-mix(in_oklch,var(--sw)_30%,oklch(1_0_0))] peer-focus-visible:shadow-[0_0_0_2px_var(--color-tpc14-card),0_0_0_4px_var(--color-tpc14-ink)] motion-reduce:transition-none"></span>
            <span class="sr-only">Graphite</span>
          </label>
        </div>
      </fieldset>

      <fieldset class="mt-4 border-0">
        <legend class="mb-2 text-[11px] font-bold tracking-[0.08em] uppercase text-tpc14-mut">Size (UK)</legend>
        <div class="flex flex-wrap gap-2">
          <label class="cursor-pointer"><input type="radio" name="tpc14-size" class="peer sr-only"><span class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border border-tpc14-edge bg-tpc14-card text-tpc14-chipink text-[14px] font-semibold transition-colors duration-200 hover:border-tpc14-mut peer-checked:bg-tpc14-ink peer-checked:text-tpc14-onacc peer-checked:border-tpc14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-tpc14-ink peer-focus-visible:outline-offset-2 motion-reduce:transition-none">7</span></label>
          <label class="cursor-pointer"><input type="radio" name="tpc14-size" class="peer sr-only" checked><span class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border border-tpc14-edge bg-tpc14-card text-tpc14-chipink text-[14px] font-semibold transition-colors duration-200 hover:border-tpc14-mut peer-checked:bg-tpc14-ink peer-checked:text-tpc14-onacc peer-checked:border-tpc14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-tpc14-ink peer-focus-visible:outline-offset-2 motion-reduce:transition-none">8</span></label>
          <label class="cursor-pointer"><input type="radio" name="tpc14-size" class="peer sr-only"><span class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border border-tpc14-edge bg-tpc14-card text-tpc14-chipink text-[14px] font-semibold transition-colors duration-200 hover:border-tpc14-mut peer-checked:bg-tpc14-ink peer-checked:text-tpc14-onacc peer-checked:border-tpc14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-tpc14-ink peer-focus-visible:outline-offset-2 motion-reduce:transition-none">9</span></label>
          <label class="cursor-pointer"><input type="radio" name="tpc14-size" class="peer sr-only"><span class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border border-tpc14-edge bg-tpc14-card text-tpc14-chipink text-[14px] font-semibold transition-colors duration-200 hover:border-tpc14-mut peer-checked:bg-tpc14-ink peer-checked:text-tpc14-onacc peer-checked:border-tpc14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-tpc14-ink peer-focus-visible:outline-offset-2 motion-reduce:transition-none">10</span></label>
          <label class="cursor-pointer"><input type="radio" name="tpc14-size" class="peer sr-only"><span class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border border-tpc14-edge bg-tpc14-card text-tpc14-chipink text-[14px] font-semibold transition-colors duration-200 hover:border-tpc14-mut peer-checked:bg-tpc14-ink peer-checked:text-tpc14-onacc peer-checked:border-tpc14-ink peer-focus-visible:outline-2 peer-focus-visible:outline-tpc14-ink peer-focus-visible:outline-offset-2 motion-reduce:transition-none">11</span></label>
        </div>
      </fieldset>

      <div class="mt-4.5 flex items-center justify-between gap-3">
        <p class="text-[22px] font-bold text-tpc14-ink tabular-nums">$140</p>
        <button type="button" class="min-h-11 h-11.5 px-5.5 rounded-xl border-0 cursor-pointer bg-[var(--tint)] text-tpc14-onacc text-[14px] font-bold transition-[background-color,filter] duration-300 hover:brightness-108 focus-visible:outline-3 focus-visible:outline-tpc14-ink focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc14-bg: #f0f1f4;
  --color-tpc14-bg: oklch(0.95 0.004 265);
  --color-tpc14-card: #ffffff;
  --color-tpc14-card: oklch(1 0 0);
  --color-tpc14-ink: #1b2233;
  --color-tpc14-ink: oklch(0.26 0.025 265);
  --color-tpc14-mut: #5c6577;
  --color-tpc14-mut: oklch(0.5 0.022 265);
  --color-tpc14-chipink: #344054;
  --color-tpc14-chipink: oklch(0.4 0.03 265);
  --color-tpc14-edge: #d0d5dd;
  --color-tpc14-edge: oklch(0.86 0.012 265);
  --color-tpc14-onacc: #ffffff;
  --color-tpc14-onacc: oklch(1 0 0);
  --font-tpc14-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* --tint is NOT declared here on purpose. An unlayered rule outranks anything in
   @layer utilities, so a fallback written here would permanently beat the
   has-[…]:[--tint:…] utilities. The default ships as a utility instead. */

.tpc-14 {
  width: 100%;
  min-height: 100svh;
}

.tpc-14 ::selection {
  background: var(--tint);
  color: #fff;
}
```
