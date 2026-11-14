---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-material-design-outlined-text-field/"
title: "Tailwind Material Design Outlined Text Field"
section: "components"
category: "tailwind-css-floating-label-inputs"
category_name: "Tailwind CSS Floating Label Inputs"
description: "The Google-style outlined field: on focus the label glides up onto the border and the outline 'opens' a notch around it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Outlined Text Field
Source: https://codefronts.com/components/tailwind-css-floating-label-inputs/tailwind-material-design-outlined-text-field/

The Google-style outlined field: on focus the label glides up onto the border and the outline 'opens' a notch around it. The notch is the label's own bg-white px-[5px] erasing the border behind it — no fieldset, no legend, no JS measuring. Focus thickens the edge with focus:shadow-[inset_0_0_0_1px_…], so the text never shifts.
## HTML
```html
<section class="tfl-09 w-full min-h-svh grid place-items-center bg-tfl09-bg px-5 py-12 font-tfl09-sans" aria-label="Outlined material floating label demo">
  <form class="flex w-full max-w-[400px] flex-col gap-[22px] rounded-3xl bg-white p-8 shadow-[0_24px_60px_-32px_oklch(0.3_0.08_290/0.4)] ring-1 ring-tfl09-ink/5" novalidate>
    <div class="flex items-baseline justify-between gap-3">
      <h3 class="text-2xl font-extrabold tracking-[-0.02em] text-tfl09-ink">Payment details</h3>
      <span class="flex items-center gap-1.5 text-xs font-semibold text-tfl09-mut"><svg aria-hidden="true" viewBox="0 0 16 16" width="13" height="13" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="3" y="7" width="10" height="7" rx="1.5"></rect><path d="M5.5 7V5a2.5 2.5 0 0 1 5 0v2"></path></svg>Encrypted</span>
    </div>
    <div class="relative">
      <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl09-line bg-transparent px-4 text-base tracking-[.06em] text-tfl09-ink tabular-nums outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl09-line-hover focus:border-tfl09-acc focus:shadow-[inset_0_0_0_1px_var(--color-tfl09-acc)] motion-reduce:transition-none" type="text" id="tfl-09-card" name="cc-number" placeholder=" " inputmode="numeric" autocomplete="cc-number" maxlength="23">
      <label class="pointer-events-none absolute left-3 top-1/2 origin-left -translate-y-1/2 bg-white px-[5px] text-base text-tfl09-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_28px)] peer-focus:scale-76 peer-focus:font-semibold peer-focus:text-tfl09-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_28px)] peer-[:not(:placeholder-shown)]:scale-76 motion-reduce:transition-none" for="tfl-09-card">Card number</label>
    </div>
    <div class="grid grid-cols-2 gap-4">
      <div class="relative">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl09-line bg-transparent px-4 text-base text-tfl09-ink tabular-nums outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl09-line-hover focus:border-tfl09-acc focus:shadow-[inset_0_0_0_1px_var(--color-tfl09-acc)] motion-reduce:transition-none" type="text" id="tfl-09-exp" name="cc-exp" placeholder=" " inputmode="numeric" autocomplete="cc-exp" maxlength="7">
        <label class="pointer-events-none absolute left-3 top-1/2 origin-left -translate-y-1/2 bg-white px-[5px] text-base text-tfl09-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_28px)] peer-focus:scale-76 peer-focus:font-semibold peer-focus:text-tfl09-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_28px)] peer-[:not(:placeholder-shown)]:scale-76 motion-reduce:transition-none" for="tfl-09-exp">MM / YY</label>
      </div>
      <div class="relative">
        <input class="peer h-14 w-full rounded-xl border-[1.5px] border-tfl09-line bg-transparent px-4 text-base text-tfl09-ink tabular-nums outline-hidden transition-[border-color,box-shadow] duration-200 hover:border-tfl09-line-hover focus:border-tfl09-acc focus:shadow-[inset_0_0_0_1px_var(--color-tfl09-acc)] motion-reduce:transition-none" type="text" id="tfl-09-cvc" name="cc-csc" placeholder=" " inputmode="numeric" autocomplete="cc-csc" maxlength="4">
        <label class="pointer-events-none absolute left-3 top-1/2 origin-left -translate-y-1/2 bg-white px-[5px] text-base text-tfl09-mut transition-[translate,scale,color] duration-[180ms] peer-focus:translate-y-[calc(-50%_-_28px)] peer-focus:scale-76 peer-focus:font-semibold peer-focus:text-tfl09-acc peer-[:not(:placeholder-shown)]:translate-y-[calc(-50%_-_28px)] peer-[:not(:placeholder-shown)]:scale-76 motion-reduce:transition-none" for="tfl-09-cvc">CVC</label>
      </div>
    </div>
    <button class="min-h-[52px] cursor-pointer rounded-xl bg-tfl09-acc text-[15px] font-bold text-white shadow-[0_10px_24px_-12px_var(--color-tfl09-acc)] transition-[filter,scale] duration-150 hover:brightness-115 active:scale-[.985] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tfl09-acc/50" type="button">Pay $48.00</button>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfl09-bg: #ebe9f2;
  --color-tfl09-bg: oklch(0.94 0.01 290);
  --color-tfl09-ink: #1f1b2e;
  --color-tfl09-ink: oklch(0.22 0.03 290);
  --color-tfl09-mut: #635c79;
  --color-tfl09-mut: oklch(0.49 0.04 290);
  --color-tfl09-line: #c9c4da;
  --color-tfl09-line: oklch(0.83 0.025 290);
  --color-tfl09-line-hover: #a29bbc;
  --color-tfl09-line-hover: oklch(0.7 0.04 290);
  --color-tfl09-acc: #5a3fc0;
  --color-tfl09-acc: oklch(0.48 0.19 288);
  --font-tfl09-sans: 'Figtree', system-ui, sans-serif;
}

.tfl-09 {
  width: 100%;
  min-height: 100svh;
}
```
