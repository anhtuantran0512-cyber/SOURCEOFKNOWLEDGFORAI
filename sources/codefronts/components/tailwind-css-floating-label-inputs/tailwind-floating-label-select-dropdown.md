---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-floating-label-select-dropdown/"
title: "Tailwind Floating Label for Select Dropdowns"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "<select> has no placeholder, so the port uses the constraint API: a required select with an empty first option is :invalid until a real choice is made, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Floating Label for Select Dropdowns
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-floating-label-select-dropdown/

<select> has no placeholder, so the port uses the constraint API: a required select with an empty first option is :invalid until a real choice is made, and peer-valid: floats the label into a solid accent pill on the top border. The chevron is a rotated border square that flips with peer-focus:rotate-225.
## HTML
```html
<section class="tfl-08 w-full min-h-svh grid place-items-center bg-tfl08-bg bg-[radial-gradient(80%_60%_at_50%_0%,var(--color-tfl08-glow),transparent_70%)] px-5 py-12 font-tfl08-sans scheme-light" aria-label="Floating label select demo">
  <form class="flex w-full max-w-[380px] flex-col gap-6 rounded-3xl bg-white p-8 shadow-[0_22px_55px_-30px_oklch(0.35_0.08_40/0.4)] ring-1 ring-tfl08-ink/5" novalidate>
    <div class="grid gap-1">
      <h3 class="font-tfl08-serif text-[26px] tracking-[-0.01em] text-tfl08-ink">Book a table</h3>
      <p class="text-sm text-tfl08-mut">Tonight at Osteria Verde</p>
    </div>
    <div class="relative">
      <select class="peer h-14 w-full cursor-pointer appearance-none rounded-xl border-[1.5px] border-tfl08-line bg-white pr-11 pl-4 text-base text-tfl08-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl08-line-hover focus:border-tfl08-acc focus:ring-4 focus:ring-tfl08-acc/15 motion-reduce:transition-none" id="tfl-08-party" name="party" required>
        <option value="" selected disabled hidden></option>
        <option value="2">2 guests</option>
        <option value="4">4 guests</option>
        <option value="6">6 guests</option>
        <option value="8">8+ guests</option>
      </select>
      <label class="pointer-events-none absolute left-4 top-1/2 -ml-2.5 origin-left -translate-y-1/2 rounded-full px-2.5 py-[3px] text-base text-tfl08-mut transition-[translate,scale,color,background-color] duration-[220ms] peer-focus:translate-y-[calc(-50%_-_28px)] peer-focus:scale-74 peer-focus:bg-tfl08-acc peer-focus:font-semibold peer-focus:text-white peer-valid:translate-y-[calc(-50%_-_28px)] peer-valid:scale-74 peer-valid:bg-tfl08-acc peer-valid:font-semibold peer-valid:text-white motion-reduce:transition-none" for="tfl-08-party">Party size</label>
      <span class="pointer-events-none absolute top-[calc(50%_-_7px)] right-[18px] size-2.5 rotate-45 border-r-[2.5px] border-b-[2.5px] border-tfl08-mut transition-[rotate,top,border-color] duration-200 peer-focus:top-[calc(50%_-_2px)] peer-focus:rotate-225 peer-focus:border-tfl08-acc motion-reduce:transition-none" aria-hidden="true"></span>
    </div>
    <div class="relative">
      <select class="peer h-14 w-full cursor-pointer appearance-none rounded-xl border-[1.5px] border-tfl08-line bg-white pr-11 pl-4 text-base text-tfl08-ink outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl08-line-hover focus:border-tfl08-acc focus:ring-4 focus:ring-tfl08-acc/15 motion-reduce:transition-none" id="tfl-08-time" name="time" required>
        <option value="" selected disabled hidden></option>
        <option value="18">6:00 PM</option>
        <option value="19">7:00 PM</option>
        <option value="20">8:00 PM</option>
        <option value="21">9:00 PM</option>
      </select>
      <label class="pointer-events-none absolute left-4 top-1/2 -ml-2.5 origin-left -translate-y-1/2 rounded-full px-2.5 py-[3px] text-base text-tfl08-mut transition-[translate,scale,color,background-color] duration-[220ms] peer-focus:translate-y-[calc(-50%_-_28px)] peer-focus:scale-74 peer-focus:bg-tfl08-acc peer-focus:font-semibold peer-focus:text-white peer-valid:translate-y-[calc(-50%_-_28px)] peer-valid:scale-74 peer-valid:bg-tfl08-acc peer-valid:font-semibold peer-valid:text-white motion-reduce:transition-none" for="tfl-08-time">Preferred time</label>
      <span class="pointer-events-none absolute top-[calc(50%_-_7px)] right-[18px] size-2.5 rotate-45 border-r-[2.5px] border-b-[2.5px] border-tfl08-mut transition-[rotate,top,border-color] duration-200 peer-focus:top-[calc(50%_-_2px)] peer-focus:rotate-225 peer-focus:border-tfl08-acc motion-reduce:transition-none" aria-hidden="true"></span>
    </div>
    <button class="min-h-12 cursor-pointer rounded-xl bg-tfl08-acc text-[15px] font-bold text-white shadow-[0_10px_24px_-12px_var(--color-tfl08-acc)] transition-[filter,scale] duration-150 hover:brightness-110 active:scale-98 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl08-acc/50" type="button">Find a table</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl08-bg: #f6f2ee;
  --color-tfl08-bg: oklch(0.96 0.008 60);
  --color-tfl08-glow: #fffaf5;
  --color-tfl08-glow: oklch(0.99 0.008 60);
  --color-tfl08-ink: #26201b;
  --color-tfl08-ink: oklch(0.24 0.015 55);
  --color-tfl08-mut: #6e645a;
  --color-tfl08-mut: oklch(0.5 0.02 60);
  --color-tfl08-line: #ddd4cb;
  --color-tfl08-line: oklch(0.87 0.015 60);
  --color-tfl08-line-hover: #c3b6a9;
  --color-tfl08-line-hover: oklch(0.78 0.025 60);
  --color-tfl08-acc: #b24a2c;
  --color-tfl08-acc: oklch(0.52 0.15 35);
  --font-tfl08-serif: 'Young Serif', Georgia, serif;
  --font-tfl08-sans: 'DM Sans', system-ui, sans-serif;
}

.tfl-08 {
  width: 100%;
  min-height: 100svh;
}
```
