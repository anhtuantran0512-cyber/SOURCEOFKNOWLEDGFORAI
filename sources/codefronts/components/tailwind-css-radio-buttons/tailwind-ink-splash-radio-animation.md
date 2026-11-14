---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-ink-splash-radio-animation/"
title: "Tailwind Ink Splash Radio Animation"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "A Material-style ink ripple reimagined for radio rows: checking an option splashes ink from the indicator until it floods the row, while the dot stamps in…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Ink Splash Radio Animation
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-ink-splash-radio-animation/

A Material-style ink ripple reimagined for radio rows: checking an option splashes ink from the indicator until it floods the row, while the dot stamps in like a wet press. The splash is the row's before: circle, scaled 0 → 34 by has-checked: with an asymmetric transition, so ink soaks in slowly and dries fast.
## HTML
```html
<section class="trb-10 w-full min-h-svh grid place-items-center bg-trb10-bg px-6 py-14 font-trb10-sans text-trb10-body" aria-label="Ink splash radio buttons demo">
  <fieldset class="w-full max-w-[26rem]">
    <legend class="font-trb10-serif text-[30px] leading-tight font-medium tracking-[-0.01em]">Paper stock</legend>
    <p class="mt-1 text-sm text-trb10-mut">Printed on FSC-certified stock.</p>
    <div class="mt-5 grid gap-2">
      <label class="group relative isolate flex min-h-16 cursor-pointer items-center gap-3.5 overflow-hidden rounded-2xl border-[1.5px] border-trb10-line bg-trb10-card px-[18px] transition-colors duration-300 before:pointer-events-none before:absolute before:top-1/2 before:left-7 before:-z-10 before:-m-[15px] before:size-[30px] before:scale-0 before:rounded-full before:bg-[radial-gradient(circle,oklch(0.45_0.16_265/0.12),oklch(0.45_0.16_265/0.09)_55%,oklch(0.45_0.16_265/0.07)_80%,transparent_97%)] before:opacity-0 before:[transition:scale_.2s,opacity_.3s] before:content-[''] hover:border-trb10-ink/35 has-checked:border-trb10-ink/55 has-checked:before:scale-[34] has-checked:before:opacity-100 has-checked:before:[transition:scale_.8s_cubic-bezier(.22,1,.36,1),opacity_.2s] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb10-ink motion-reduce:has-checked:before:[transition:opacity_.2s]">
        <input type="radio" name="trb-10" value="matte" class="sr-only" checked>
        <span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-full border-2 border-trb10-ring transition-colors duration-300 after:size-[11px] after:scale-0 after:rounded-full after:bg-trb10-ink after:transition-transform after:duration-350 after:ease-trb10-stamp after:content-[''] group-has-checked:border-trb10-ink group-has-checked:after:scale-100 motion-reduce:after:transition-none"></span>
        <span class="grid flex-1"><span class="font-trb10-serif text-lg font-semibold">Matte</span><span class="text-[13px] text-trb10-mut">Soft, no glare</span></span>
        <span class="text-xs font-semibold tracking-[0.06em] text-trb10-mut uppercase">120 gsm</span>
      </label>
      <label class="group relative isolate flex min-h-16 cursor-pointer items-center gap-3.5 overflow-hidden rounded-2xl border-[1.5px] border-trb10-line bg-trb10-card px-[18px] transition-colors duration-300 before:pointer-events-none before:absolute before:top-1/2 before:left-7 before:-z-10 before:-m-[15px] before:size-[30px] before:scale-0 before:rounded-full before:bg-[radial-gradient(circle,oklch(0.45_0.16_265/0.12),oklch(0.45_0.16_265/0.09)_55%,oklch(0.45_0.16_265/0.07)_80%,transparent_97%)] before:opacity-0 before:[transition:scale_.2s,opacity_.3s] before:content-[''] hover:border-trb10-ink/35 has-checked:border-trb10-ink/55 has-checked:before:scale-[34] has-checked:before:opacity-100 has-checked:before:[transition:scale_.8s_cubic-bezier(.22,1,.36,1),opacity_.2s] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb10-ink motion-reduce:has-checked:before:[transition:opacity_.2s]">
        <input type="radio" name="trb-10" value="satin" class="sr-only">
        <span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-full border-2 border-trb10-ring transition-colors duration-300 after:size-[11px] after:scale-0 after:rounded-full after:bg-trb10-ink after:transition-transform after:duration-350 after:ease-trb10-stamp after:content-[''] group-has-checked:border-trb10-ink group-has-checked:after:scale-100 motion-reduce:after:transition-none"></span>
        <span class="grid flex-1"><span class="font-trb10-serif text-lg font-semibold">Satin</span><span class="text-[13px] text-trb10-mut">Gentle sheen</span></span>
        <span class="text-xs font-semibold tracking-[0.06em] text-trb10-mut uppercase">150 gsm</span>
      </label>
      <label class="group relative isolate flex min-h-16 cursor-pointer items-center gap-3.5 overflow-hidden rounded-2xl border-[1.5px] border-trb10-line bg-trb10-card px-[18px] transition-colors duration-300 before:pointer-events-none before:absolute before:top-1/2 before:left-7 before:-z-10 before:-m-[15px] before:size-[30px] before:scale-0 before:rounded-full before:bg-[radial-gradient(circle,oklch(0.45_0.16_265/0.12),oklch(0.45_0.16_265/0.09)_55%,oklch(0.45_0.16_265/0.07)_80%,transparent_97%)] before:opacity-0 before:[transition:scale_.2s,opacity_.3s] before:content-[''] hover:border-trb10-ink/35 has-checked:border-trb10-ink/55 has-checked:before:scale-[34] has-checked:before:opacity-100 has-checked:before:[transition:scale_.8s_cubic-bezier(.22,1,.36,1),opacity_.2s] has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb10-ink motion-reduce:has-checked:before:[transition:opacity_.2s]">
        <input type="radio" name="trb-10" value="gloss" class="sr-only">
        <span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-full border-2 border-trb10-ring transition-colors duration-300 after:size-[11px] after:scale-0 after:rounded-full after:bg-trb10-ink after:transition-transform after:duration-350 after:ease-trb10-stamp after:content-[''] group-has-checked:border-trb10-ink group-has-checked:after:scale-100 motion-reduce:after:transition-none"></span>
        <span class="grid flex-1"><span class="font-trb10-serif text-lg font-semibold">Gloss</span><span class="text-[13px] text-trb10-mut">Vivid, reflective</span></span>
        <span class="text-xs font-semibold tracking-[0.06em] text-trb10-mut uppercase">170 gsm</span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb10-bg: #f6f1e7;
  --color-trb10-bg: oklch(0.958 0.016 85);
  --color-trb10-card: #fffdf8;
  --color-trb10-card: oklch(0.995 0.006 85);
  --color-trb10-body: #2a2620;
  --color-trb10-body: oklch(0.27 0.012 75);
  --color-trb10-mut: #6a6150;
  --color-trb10-mut: oklch(0.5 0.025 80);
  --color-trb10-line: #e7dfd0;
  --color-trb10-line: oklch(0.91 0.02 85);
  --color-trb10-ring: #a99d84;
  --color-trb10-ring: oklch(0.7 0.03 85);
  --color-trb10-ink: #3a47a8;
  --color-trb10-ink: oklch(0.45 0.16 265);
  --ease-trb10-stamp: cubic-bezier(0.34, 1.7, 0.5, 1);
  --font-trb10-serif: 'Newsreader', Georgia, serif;
  --font-trb10-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-10 {
  width: 100%;
  min-height: 100svh;
}
```
