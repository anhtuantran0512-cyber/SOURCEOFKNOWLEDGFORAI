---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-login-forms/tailwind-otp-code-input-grid-auto-advance/"
title: "Tailwind OTP Code Input Grid with Auto-Advance"
section: "components"
category: "tailwind-css-login-forms"
category_name: "Tailwind CSS Login Forms"
description: "The multi-factor confirmation screen: six evenly-sized digit boxes that auto-advance as you type, accept a full paste, and step back on Backspace."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind OTP Code Input Grid with Auto-Advance
Source: https://codefronts.com/components/tailwind-css-login-forms/tailwind-otp-code-input-grid-auto-advance/

The multi-factor confirmation screen: six evenly-sized digit boxes that auto-advance as you type, accept a full paste, and step back on Backspace. CSS holds the filled state via not-placeholder-shown:, so the boxes light up without the script tracking any visual state at all.
## HTML
```html
<section class="tlf-25 w-full min-h-svh grid place-items-center bg-tlf25-stage font-tlf25-sans p-6">
  <form novalidate class="tlf-25-form w-[min(420px,100%)] p-8 text-center bg-white border border-tlf25-edge rounded-[18px] shadow-[0_22px_50px_-38px_oklch(0.25_0.06_265/0.5)]">
    <h1 class="text-[22px] font-bold text-tlf25-ink">Verify your identity</h1>
    <p class="mt-1.5 mb-6 text-[13.5px]/[1.5] text-tlf25-mut">Enter the 6-digit code we sent to your email.</p>
    <div role="group" aria-label="6-digit verification code" class="grid grid-cols-6 gap-2 mb-6">
      <input class="tlf-25-box min-w-0 h-13 max-[420px]:h-12 text-center text-[22px] max-[420px]:text-[19px] font-bold text-tlf25-ink rounded-xl bg-tlf25-field border-[1.5px] border-tlf25-fieldedge transition-[border-color,box-shadow,background-color,translate] duration-150 placeholder:text-tlf25-ph not-placeholder-shown:border-tlf25-acc not-placeholder-shown:bg-tlf25-tint focus-visible:outline-none focus-visible:border-tlf25-acc focus-visible:ring-4 focus-visible:ring-tlf25-halo focus-visible:-translate-y-0.5 motion-reduce:transition-colors motion-reduce:focus-visible:translate-y-0" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="1" pattern="[0-9]" placeholder="&bull;" aria-label="Digit 1">
      <input class="tlf-25-box min-w-0 h-13 max-[420px]:h-12 text-center text-[22px] max-[420px]:text-[19px] font-bold text-tlf25-ink rounded-xl bg-tlf25-field border-[1.5px] border-tlf25-fieldedge transition-[border-color,box-shadow,background-color,translate] duration-150 placeholder:text-tlf25-ph not-placeholder-shown:border-tlf25-acc not-placeholder-shown:bg-tlf25-tint focus-visible:outline-none focus-visible:border-tlf25-acc focus-visible:ring-4 focus-visible:ring-tlf25-halo focus-visible:-translate-y-0.5 motion-reduce:transition-colors motion-reduce:focus-visible:translate-y-0" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="&bull;" aria-label="Digit 2">
      <input class="tlf-25-box min-w-0 h-13 max-[420px]:h-12 text-center text-[22px] max-[420px]:text-[19px] font-bold text-tlf25-ink rounded-xl bg-tlf25-field border-[1.5px] border-tlf25-fieldedge transition-[border-color,box-shadow,background-color,translate] duration-150 placeholder:text-tlf25-ph not-placeholder-shown:border-tlf25-acc not-placeholder-shown:bg-tlf25-tint focus-visible:outline-none focus-visible:border-tlf25-acc focus-visible:ring-4 focus-visible:ring-tlf25-halo focus-visible:-translate-y-0.5 motion-reduce:transition-colors motion-reduce:focus-visible:translate-y-0" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="&bull;" aria-label="Digit 3">
      <input class="tlf-25-box min-w-0 h-13 max-[420px]:h-12 text-center text-[22px] max-[420px]:text-[19px] font-bold text-tlf25-ink rounded-xl bg-tlf25-field border-[1.5px] border-tlf25-fieldedge transition-[border-color,box-shadow,background-color,translate] duration-150 placeholder:text-tlf25-ph not-placeholder-shown:border-tlf25-acc not-placeholder-shown:bg-tlf25-tint focus-visible:outline-none focus-visible:border-tlf25-acc focus-visible:ring-4 focus-visible:ring-tlf25-halo focus-visible:-translate-y-0.5 motion-reduce:transition-colors motion-reduce:focus-visible:translate-y-0" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="&bull;" aria-label="Digit 4">
      <input class="tlf-25-box min-w-0 h-13 max-[420px]:h-12 text-center text-[22px] max-[420px]:text-[19px] font-bold text-tlf25-ink rounded-xl bg-tlf25-field border-[1.5px] border-tlf25-fieldedge transition-[border-color,box-shadow,background-color,translate] duration-150 placeholder:text-tlf25-ph not-placeholder-shown:border-tlf25-acc not-placeholder-shown:bg-tlf25-tint focus-visible:outline-none focus-visible:border-tlf25-acc focus-visible:ring-4 focus-visible:ring-tlf25-halo focus-visible:-translate-y-0.5 motion-reduce:transition-colors motion-reduce:focus-visible:translate-y-0" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="&bull;" aria-label="Digit 5">
      <input class="tlf-25-box min-w-0 h-13 max-[420px]:h-12 text-center text-[22px] max-[420px]:text-[19px] font-bold text-tlf25-ink rounded-xl bg-tlf25-field border-[1.5px] border-tlf25-fieldedge transition-[border-color,box-shadow,background-color,translate] duration-150 placeholder:text-tlf25-ph not-placeholder-shown:border-tlf25-acc not-placeholder-shown:bg-tlf25-tint focus-visible:outline-none focus-visible:border-tlf25-acc focus-visible:ring-4 focus-visible:ring-tlf25-halo focus-visible:-translate-y-0.5 motion-reduce:transition-colors motion-reduce:focus-visible:translate-y-0" type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" placeholder="&bull;" aria-label="Digit 6">
    </div>
    <button type="submit" class="w-full h-[50px] rounded-xl border-0 cursor-pointer bg-tlf25-acc text-white text-[15px] font-semibold transition-[filter,scale] duration-150 hover:brightness-110 active:scale-[0.99] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tlf25-ring motion-reduce:transition-none motion-reduce:active:scale-100">Verify</button>
    <p class="mt-4 text-[13px] text-tlf25-mut">Didn&rsquo;t get it? <a href="#" class="font-semibold text-tlf25-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tlf25-acc">Resend code</a></p>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tlf25-stage: #eef1f7;
  --color-tlf25-stage: oklch(0.95 0.008 265);
  --color-tlf25-edge: #e5e9f2;
  --color-tlf25-edge: oklch(0.92 0.008 265);
  --color-tlf25-fieldedge: #d5dbe8;
  --color-tlf25-fieldedge: oklch(0.87 0.012 265);
  --color-tlf25-field: #fafbfe;
  --color-tlf25-field: oklch(0.99 0.003 265);
  --color-tlf25-tint: #eef1fc;
  --color-tlf25-tint: oklch(0.56 0.18 265 / 0.06);
  --color-tlf25-ink: #1a2237;
  --color-tlf25-ink: oklch(0.25 0.04 265);
  --color-tlf25-mut: #666e88;
  --color-tlf25-mut: oklch(0.52 0.03 265);
  --color-tlf25-ph: #bcc3d4;
  --color-tlf25-ph: oklch(0.8 0.015 265);
  --color-tlf25-acc: #4159cd;
  --color-tlf25-acc: oklch(0.51 0.18 265);
  --color-tlf25-halo: #bfc9f0;
  --color-tlf25-halo: oklch(0.51 0.18 265 / 0.2);
  --color-tlf25-ring: #94a2ea;
  --color-tlf25-ring: oklch(0.51 0.18 265 / 0.5);
  --font-tlf25-sans: 'DM Sans', system-ui, sans-serif;
}

.tlf-25 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
const boxes = [...document.querySelectorAll('.tlf-25-box')];

boxes.forEach((box, i) => {
  box.addEventListener('input', () => {
    box.value = box.value.replace(/[^0-9]/g, '').slice(0, 1);
    if (box.value && i < boxes.length - 1) boxes[i + 1].focus();
  });

  box.addEventListener('keydown', (e) => {
    if (e.key === 'Backspace' && !box.value && i > 0) boxes[i - 1].focus();
    if (e.key === 'ArrowLeft' && i > 0) boxes[i - 1].focus();
    if (e.key === 'ArrowRight' && i < boxes.length - 1) boxes[i + 1].focus();
  });

  box.addEventListener('paste', (e) => {
    e.preventDefault();
    const digits = (e.clipboardData.getData('text') || '').replace(/[^0-9]/g, '').split('');
    boxes.forEach((b, j) => { if (digits[j] != null) b.value = digits[j]; });
    boxes[Math.min(digits.length, boxes.length) - 1]?.focus();
  });
});
```
