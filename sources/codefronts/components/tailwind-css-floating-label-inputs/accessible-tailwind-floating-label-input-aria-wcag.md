---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/accessible-tailwind-floating-label-input-aria-wcag/"
title: "Accessible Tailwind Floating Label Input (ARIA + WCAG)"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "The floating label audited: real for/id binding, aria-describedby hints, a required marker that isn't colour-only, AA contrast in both label states, and a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind Floating Label Input (ARIA + WCAG)
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/accessible-tailwind-floating-label-input-aria-wcag/

The floating label audited: real for/id binding, aria-describedby hints, a required marker that isn't colour-only, AA contrast in both label states, and a thick focus-visible:outline-3 outline-offset-3 ring. The float barely shrinks (scale-85), bolds instead, and grows an accent tick via peer-focus:before:w-3 — low-vision users never lose it.
## HTML
```html
<section class="tfl-07 w-full min-h-svh grid place-items-center bg-tfl07-bg px-5 py-12 font-tfl07-sans" aria-label="Accessibility-first floating label demo">
  <form class="flex w-full max-w-[400px] flex-col gap-1.5 rounded-[18px] bg-white p-8 shadow-[0_20px_50px_-28px_oklch(0.3_0.06_265/0.35)] ring-1 ring-tfl07-ink/5" novalidate>
    <div class="mb-4 grid gap-1">
      <h3 class="text-2xl font-bold tracking-[-0.01em] text-tfl07-ink">Contact details</h3>
      <p class="text-sm text-tfl07-mut">Fields marked <span aria-hidden="true" class="font-bold text-tfl07-req">*</span> are required.</p>
    </div>
    <div class="relative pb-[30px]">
      <input class="peer h-[58px] w-full rounded-[10px] border-2 border-tfl07-line bg-white px-4 pt-6 pb-1.5 text-base text-tfl07-ink outline-hidden transition-[border-color] duration-200 hover:border-tfl07-line-hover focus:border-tfl07-acc focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-solid focus-visible:outline-tfl07-acc motion-reduce:transition-none" type="text" id="tfl-07-name" name="name" placeholder=" " required autocomplete="name" aria-describedby="tfl-07-name-hint">
      <label class="pointer-events-none absolute left-4 top-[29px] origin-left -translate-y-1/2 text-base text-tfl07-mut transition-[translate,scale,color] duration-200 before:inline-block before:h-[3px] before:w-0 before:rounded-sm before:bg-tfl07-acc before:align-middle before:transition-[width,margin] before:duration-200 before:content-[''] peer-focus:translate-y-[calc(-50%_-_15px)] peer-focus:scale-85 peer-focus:font-bold peer-focus:text-tfl07-acc peer-focus:before:mr-1.5 peer-focus:before:w-3 peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_15px)] peer-[:not(:placeholder-shown)]:scale-85 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:before:mr-1.5 peer-[:not(:placeholder-shown)]:before:w-3 motion-reduce:transition-none motion-reduce:before:transition-none" for="tfl-07-name">Full name <span class="font-bold text-tfl07-req" aria-hidden="true">*</span></label>
      <p class="absolute bottom-1.5 left-0.5 text-[13px]/snug text-tfl07-mut" id="tfl-07-name-hint">Required — as it appears on your ID</p>
    </div>
    <div class="relative pb-[30px]">
      <input class="peer h-[58px] w-full rounded-[10px] border-2 border-tfl07-line bg-white px-4 pt-6 pb-1.5 text-base text-tfl07-ink outline-hidden transition-[border-color] duration-200 hover:border-tfl07-line-hover focus:border-tfl07-acc focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-solid focus-visible:outline-tfl07-acc motion-reduce:transition-none" type="tel" id="tfl-07-tel" name="tel" placeholder=" " autocomplete="tel" inputmode="tel" aria-describedby="tfl-07-tel-hint">
      <label class="pointer-events-none absolute left-4 top-[29px] origin-left -translate-y-1/2 text-base text-tfl07-mut transition-[translate,scale,color] duration-200 before:inline-block before:h-[3px] before:w-0 before:rounded-sm before:bg-tfl07-acc before:align-middle before:transition-[width,margin] before:duration-200 before:content-[''] peer-focus:translate-y-[calc(-50%_-_15px)] peer-focus:scale-85 peer-focus:font-bold peer-focus:text-tfl07-acc peer-focus:before:mr-1.5 peer-focus:before:w-3 peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_15px)] peer-[:not(:placeholder-shown)]:scale-85 peer-[:not(:placeholder-shown)]:font-bold peer-[:not(:placeholder-shown)]:before:mr-1.5 peer-[:not(:placeholder-shown)]:before:w-3 motion-reduce:transition-none motion-reduce:before:transition-none" for="tfl-07-tel">Phone number</label>
      <p class="absolute bottom-1.5 left-0.5 text-[13px]/snug text-tfl07-mut" id="tfl-07-tel-hint">Optional — include country code</p>
    </div>
    <button class="min-h-[52px] cursor-pointer rounded-[10px] bg-tfl07-acc text-base font-bold text-white transition-[filter] duration-150 hover:brightness-115 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tfl07-acc" type="submit">Save contact</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl07-bg: #eef0f4;
  --color-tfl07-bg: oklch(0.95 0.007 265);
  --color-tfl07-ink: #171a26;
  --color-tfl07-ink: oklch(0.21 0.025 270);
  --color-tfl07-mut: #555a69;
  --color-tfl07-mut: oklch(0.45 0.025 270);
  --color-tfl07-line: #8f95a6;
  --color-tfl07-line: oklch(0.66 0.025 270);
  --color-tfl07-line-hover: #6d7386;
  --color-tfl07-line-hover: oklch(0.56 0.03 270);
  --color-tfl07-acc: #3b3fce;
  --color-tfl07-acc: oklch(0.46 0.21 272);
  --color-tfl07-req: #b8302a;
  --color-tfl07-req: oklch(0.5 0.19 27);
  --font-tfl07-sans: 'Atkinson Hyperlegible', system-ui, sans-serif;
}

.tfl-07 {
  width: 100%;
  min-height: 100svh;
}
```
