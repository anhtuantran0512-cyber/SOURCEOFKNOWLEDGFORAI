---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-stepper-checkout-flow/"
title: "Tailwind Material Design Stepper and Checkout Flow"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "A horizontal stepper, a vertical stepper and a three-step checkout &mdash; all radio-driven, and all three know which steps are done."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Stepper and Checkout Flow
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-stepper-checkout-flow/

A horizontal stepper, a vertical stepper and a three-step checkout &mdash; all radio-driven, and all three know which steps are done. That is the port's trick: a step's completed look comes from has-[~ …:checked]:, the subsequent-sibling form of :has(), so &ldquo;a later step is selected, therefore I am complete&rdquo; is expressible without a single line of script.
## HTML
```html
<section class="tmd-09 w-full min-h-svh bg-tmd09-bg font-tmd09-sans text-tmd09-onsurface px-5 py-9" aria-label="Material Design stepper demo">
  <div class="w-[min(880px,100%)] mx-auto grid gap-6">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Steppers</h2>
      <p class="text-sm text-tmd09-onvariant">Completed steps are inferred, not marked: <code class="font-tmd09-mono text-[12px]">has-[~li_input:checked]:</code> asks &ldquo;is a later step selected?&rdquo;</p>
    </header>

    <div class="group/hs grid gap-6 p-5.5 rounded-3xl bg-tmd09-surface shadow-tmd09-1">
      <ol class="grid grid-cols-3 list-none m-0 p-0">
        <li class="relative grid justify-items-center gap-2 text-center after:absolute after:top-5 after:left-1/2 after:-z-1 after:w-full after:h-0.5 after:bg-tmd09-outlinevariant last:after:hidden has-[~li_input:checked]:after:bg-tmd09-done">
          <input type="radio" name="tmd09-h" id="tmd09-h1" class="peer/h1 sr-only" checked>
          <label for="tmd09-h1" class="grid justify-items-center gap-2 cursor-pointer">
            <span class="relative z-1 grid place-items-center w-10 h-10 rounded-full bg-tmd09-surface border-2 border-tmd09-outlinevariant text-sm font-medium text-tmd09-onvariant transition-colors duration-200 group-has-[#tmd09-h1:checked]/hs:bg-tmd09-primary group-has-[#tmd09-h1:checked]/hs:border-tmd09-primary group-has-[#tmd09-h1:checked]/hs:text-white group-has-[#tmd09-h1:focus-visible]/hs:outline-2 group-has-[#tmd09-h1:focus-visible]/hs:outline-offset-2 group-has-[#tmd09-h1:focus-visible]/hs:outline-tmd09-primary motion-reduce:transition-none">1</span>
            <b class="text-[13px] font-medium">Details</b>
            <span class="text-[11px] text-tmd09-onvariant">Station &amp; depth</span>
          </label>
        </li>
        <li class="relative grid justify-items-center gap-2 text-center after:absolute after:top-5 after:left-1/2 after:-z-1 after:w-full after:h-0.5 after:bg-tmd09-outlinevariant last:after:hidden has-[~li_input:checked]:after:bg-tmd09-done">
          <input type="radio" name="tmd09-h" id="tmd09-h2" class="peer/h2 sr-only">
          <label for="tmd09-h2" class="grid justify-items-center gap-2 cursor-pointer">
            <span class="relative z-1 grid place-items-center w-10 h-10 rounded-full bg-tmd09-surface border-2 border-tmd09-outlinevariant text-sm font-medium text-tmd09-onvariant transition-colors duration-200 group-has-[#tmd09-h2:checked]/hs:bg-tmd09-primary group-has-[#tmd09-h2:checked]/hs:border-tmd09-primary group-has-[#tmd09-h2:checked]/hs:text-white group-has-[#tmd09-h2:focus-visible]/hs:outline-2 group-has-[#tmd09-h2:focus-visible]/hs:outline-offset-2 group-has-[#tmd09-h2:focus-visible]/hs:outline-tmd09-primary motion-reduce:transition-none">2</span>
            <b class="text-[13px] font-medium">Calibration</b>
            <span class="text-[11px] text-tmd09-onvariant">Sensor offsets</span>
          </label>
        </li>
        <li class="relative grid justify-items-center gap-2 text-center">
          <input type="radio" name="tmd09-h" id="tmd09-h3" class="peer/h3 sr-only">
          <label for="tmd09-h3" class="grid justify-items-center gap-2 cursor-pointer">
            <span class="relative z-1 grid place-items-center w-10 h-10 rounded-full bg-tmd09-surface border-2 border-tmd09-outlinevariant text-sm font-medium text-tmd09-onvariant transition-colors duration-200 group-has-[#tmd09-h3:checked]/hs:bg-tmd09-primary group-has-[#tmd09-h3:checked]/hs:border-tmd09-primary group-has-[#tmd09-h3:checked]/hs:text-white group-has-[#tmd09-h3:focus-visible]/hs:outline-2 group-has-[#tmd09-h3:focus-visible]/hs:outline-offset-2 group-has-[#tmd09-h3:focus-visible]/hs:outline-tmd09-primary motion-reduce:transition-none">3</span>
            <b class="text-[13px] font-medium">Review</b>
            <span class="text-[11px] text-tmd09-onvariant">Submit</span>
          </label>
        </li>
      </ol>

      <div class="p-4 rounded-2xl bg-tmd09-surface2 min-h-28">
        <div class="hidden gap-2 group-has-[#tmd09-h1:checked]/hs:grid"><b class="text-sm font-medium">Step 1 &mdash; details</b><p class="text-sm leading-6 text-tmd09-onvariant text-pretty">Panels are revealed with <span class="font-tmd09-mono text-[12px]">group-has-[#id:checked]/hs:grid</span>, so the whole stepper is stateless HTML.</p></div>
        <div class="hidden gap-2 group-has-[#tmd09-h2:checked]/hs:grid"><b class="text-sm font-medium">Step 2 &mdash; calibration</b><p class="text-sm leading-6 text-tmd09-onvariant text-pretty">Notice step 1's connector and circle turned green the moment this step became active &mdash; inferred, not toggled.</p></div>
        <div class="hidden gap-2 group-has-[#tmd09-h3:checked]/hs:grid"><b class="text-sm font-medium">Step 3 &mdash; review</b><p class="text-sm leading-6 text-tmd09-onvariant text-pretty">Two steps complete, no script involved.</p></div>
      </div>
    </div>

    <div class="grid gap-4 p-5.5 rounded-3xl bg-tmd09-surface shadow-tmd09-1">
      <span class="font-tmd09-mono text-[11px] uppercase tracking-[0.1em] text-tmd09-onvariant">Vertical stepper &mdash; checkout</span>
      <ol class="list-none m-0 p-0 grid gap-0">
        <li class="group/v relative grid grid-cols-[40px_1fr] gap-4 pb-6 after:absolute after:top-11 after:left-5 after:w-0.5 after:h-[calc(100%-2.75rem)] after:bg-tmd09-outlinevariant last:pb-0 last:after:hidden has-[~li_input:checked]:after:bg-tmd09-done">
          <input type="radio" name="tmd09-v" id="tmd09-v1" class="peer/v1 sr-only" checked>
          <label for="tmd09-v1" class="relative z-1 grid place-items-center w-10 h-10 self-start rounded-full bg-tmd09-surface border-2 border-tmd09-outlinevariant text-sm font-medium text-tmd09-onvariant cursor-pointer transition-colors duration-200 peer-checked/v1:bg-tmd09-primary peer-checked/v1:border-tmd09-primary peer-checked/v1:text-white peer-focus-visible/v1:outline-2 peer-focus-visible/v1:outline-offset-2 peer-focus-visible/v1:outline-tmd09-primary motion-reduce:transition-none">1</label>
          <div class="grid gap-2 pt-1.5">
            <label for="tmd09-v1" class="text-[15px] font-medium cursor-pointer">Shipping address</label>
            <div class="hidden group-has-[#tmd09-v1:checked]/v:grid gap-3 max-w-100">
              <p class="text-sm leading-6 text-tmd09-onvariant">Fjordgata 14, 7010 Trondheim, Norway</p>
              <label for="tmd09-v2" class="relative overflow-hidden justify-self-start inline-flex items-center min-h-10 px-5 rounded-full bg-tmd09-primary text-white text-sm font-medium cursor-pointer before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Continue</label>
            </div>
          </div>
        </li>
        <li class="group/v relative grid grid-cols-[40px_1fr] gap-4 pb-6 after:absolute after:top-11 after:left-5 after:w-0.5 after:h-[calc(100%-2.75rem)] after:bg-tmd09-outlinevariant last:pb-0 last:after:hidden has-[~li_input:checked]:after:bg-tmd09-done">
          <input type="radio" name="tmd09-v" id="tmd09-v2" class="peer/v2 sr-only">
          <label for="tmd09-v2" class="relative z-1 grid place-items-center w-10 h-10 self-start rounded-full bg-tmd09-surface border-2 border-tmd09-outlinevariant text-sm font-medium text-tmd09-onvariant cursor-pointer transition-colors duration-200 peer-checked/v2:bg-tmd09-primary peer-checked/v2:border-tmd09-primary peer-checked/v2:text-white peer-focus-visible/v2:outline-2 peer-focus-visible/v2:outline-offset-2 peer-focus-visible/v2:outline-tmd09-primary motion-reduce:transition-none">2</label>
          <div class="grid gap-2 pt-1.5">
            <label for="tmd09-v2" class="text-[15px] font-medium cursor-pointer">Delivery speed</label>
            <div class="hidden group-has-[#tmd09-v2:checked]/v:grid gap-3 max-w-100">
              <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer"><input type="radio" name="tmd09-speed" checked class="w-5 h-5 accent-tmd09-primary">Standard &mdash; 4 days</label>
              <label class="flex items-center gap-3 min-h-11 text-sm cursor-pointer"><input type="radio" name="tmd09-speed" class="w-5 h-5 accent-tmd09-primary">Express &mdash; overnight</label>
              <div class="flex gap-2">
                <label for="tmd09-v1" class="inline-flex items-center min-h-10 px-4 rounded-full text-sm font-medium text-tmd09-primary cursor-pointer hover:bg-tmd09-surface2">Back</label>
                <label for="tmd09-v3" class="relative overflow-hidden inline-flex items-center min-h-10 px-5 rounded-full bg-tmd09-primary text-white text-sm font-medium cursor-pointer before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Continue</label>
              </div>
            </div>
          </div>
        </li>
        <li class="group/v relative grid grid-cols-[40px_1fr] gap-4">
          <input type="radio" name="tmd09-v" id="tmd09-v3" class="peer/v3 sr-only">
          <label for="tmd09-v3" class="relative z-1 grid place-items-center w-10 h-10 self-start rounded-full bg-tmd09-surface border-2 border-tmd09-outlinevariant text-sm font-medium text-tmd09-onvariant cursor-pointer transition-colors duration-200 peer-checked/v3:bg-tmd09-primary peer-checked/v3:border-tmd09-primary peer-checked/v3:text-white peer-focus-visible/v3:outline-2 peer-focus-visible/v3:outline-offset-2 peer-focus-visible/v3:outline-tmd09-primary motion-reduce:transition-none">3</label>
          <div class="grid gap-2 pt-1.5">
            <label for="tmd09-v3" class="text-[15px] font-medium cursor-pointer">Confirm order</label>
            <div class="hidden group-has-[#tmd09-v3:checked]/v:grid gap-3 max-w-100">
              <dl class="grid grid-cols-2 gap-1 m-0 text-sm"><dt class="text-tmd09-onvariant">Subtotal</dt><dd class="m-0 text-right tabular-nums">kr 1 240</dd><dt class="text-tmd09-onvariant">Shipping</dt><dd class="m-0 text-right tabular-nums">kr 79</dd></dl>
              <div class="flex gap-2">
                <label for="tmd09-v2" class="inline-flex items-center min-h-10 px-4 rounded-full text-sm font-medium text-tmd09-primary cursor-pointer hover:bg-tmd09-surface2">Back</label>
                <button type="button" class="relative overflow-hidden inline-flex items-center min-h-10 px-5 rounded-full border-0 bg-tmd09-done text-white text-sm font-medium cursor-pointer before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Place order</button>
              </div>
            </div>
          </div>
        </li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd09-bg: #fff3e0;
  --color-tmd09-bg: oklch(0.969 0.028 79.5);
  --color-tmd09-surface: #ffffff;
  --color-tmd09-surface: oklch(1 0 89.9);
  --color-tmd09-surface2: #fff8ef;
  --color-tmd09-surface2: oklch(0.982 0.014 74.4);
  --color-tmd09-primary: #e65100;
  --color-tmd09-primary: oklch(0.631 0.197 40.3);
  --color-tmd09-done: #2e7d32;
  --color-tmd09-done: oklch(0.523 0.135 144.2);
  --color-tmd09-onsurface: #211a14;
  --color-tmd09-onsurface: oklch(0.224 0.016 62.5);
  --color-tmd09-onvariant: #6b5a4c;
  --color-tmd09-onvariant: oklch(0.48 0.031 61.4);
  --color-tmd09-outlinevariant: #e8d5c2;
  --color-tmd09-outlinevariant: oklch(0.883 0.033 67.4);
  --font-tmd09-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd09-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd09-icon: 'Material Symbols Outlined';
  --shadow-tmd09-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
}

.tmd-09 {
  width: 100%;
  min-height: 100svh;
}

.tmd-09 .font-tmd09-icon {
  font-feature-settings: 'liga';
}
/* Completed steps: a step whose circle should read "done" is one with a later checked
   sibling. The relationship is expressible as a utility, but the numeral-to-check swap
   needs content substitution, which has no utility form. */

.tmd-09 li:has(~ li input:checked) label > span:first-child {
  background: var(--color-tmd09-done);
  border-color: var(--color-tmd09-done);
  color: #fff;
  font-family: 'Material Symbols Outlined';
  font-size: 22px;
}

.tmd-09 li:has(~ li input:checked) label > span:first-child {
  font-size: 0;
}

.tmd-09 li:has(~ li input:checked) label > span:first-child::after {
  content: 'check';
  font-size: 22px;
  font-feature-settings: 'liga';
}
```
