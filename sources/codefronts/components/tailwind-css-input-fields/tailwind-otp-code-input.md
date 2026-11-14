---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-otp-code-input/"
title: "Tailwind OTP Code Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Six single-character boxes in a <fieldset>, with auto-advance, backspace step-back and paste-to-fill."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind OTP Code Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-otp-code-input/

Six single-character boxes in a <fieldset>, with auto-advance, backspace step-back and paste-to-fill. autocomplete="one-time-code" on the first box is what surfaces the iOS SMS suggestion.
## HTML
```html
<div class="tif-10 grid min-h-svh w-full place-items-center bg-tif10-bg px-6 py-14 font-tif10-mono" aria-label="OTP code input demo">
  <fieldset class="grid w-full max-w-70 grid-cols-6 gap-2 border-0 p-0">
    <legend class="sr-only">Verification code</legend>
    <input type="text" inputmode="numeric" maxlength="1" autocomplete="one-time-code" pattern="[0-9]" aria-label="Digit 1" data-tif10
      class="aspect-square w-full rounded-[10px] border border-white/10 bg-tif10-field text-center text-lg font-bold text-tif10-ink caret-tif10-acc outline-none transition-[border-color,background-color,transform] duration-150 focus:-translate-y-px focus:border-tif10-acc focus:bg-tif10-acc/10 motion-reduce:transition-none motion-reduce:focus:translate-y-0">
    <input type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" aria-label="Digit 2" data-tif10
      class="aspect-square w-full rounded-[10px] border border-white/10 bg-tif10-field text-center text-lg font-bold text-tif10-ink caret-tif10-acc outline-none transition-[border-color,background-color,transform] duration-150 focus:-translate-y-px focus:border-tif10-acc focus:bg-tif10-acc/10 motion-reduce:transition-none motion-reduce:focus:translate-y-0">
    <input type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" aria-label="Digit 3" data-tif10
      class="aspect-square w-full rounded-[10px] border border-white/10 bg-tif10-field text-center text-lg font-bold text-tif10-ink caret-tif10-acc outline-none transition-[border-color,background-color,transform] duration-150 focus:-translate-y-px focus:border-tif10-acc focus:bg-tif10-acc/10 motion-reduce:transition-none motion-reduce:focus:translate-y-0">
    <input type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" aria-label="Digit 4" data-tif10
      class="aspect-square w-full rounded-[10px] border border-white/10 bg-tif10-field text-center text-lg font-bold text-tif10-ink caret-tif10-acc outline-none transition-[border-color,background-color,transform] duration-150 focus:-translate-y-px focus:border-tif10-acc focus:bg-tif10-acc/10 motion-reduce:transition-none motion-reduce:focus:translate-y-0">
    <input type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" aria-label="Digit 5" data-tif10
      class="aspect-square w-full rounded-[10px] border border-white/10 bg-tif10-field text-center text-lg font-bold text-tif10-ink caret-tif10-acc outline-none transition-[border-color,background-color,transform] duration-150 focus:-translate-y-px focus:border-tif10-acc focus:bg-tif10-acc/10 motion-reduce:transition-none motion-reduce:focus:translate-y-0">
    <input type="text" inputmode="numeric" maxlength="1" pattern="[0-9]" aria-label="Digit 6" data-tif10
      class="aspect-square w-full rounded-[10px] border border-white/10 bg-tif10-field text-center text-lg font-bold text-tif10-ink caret-tif10-acc outline-none transition-[border-color,background-color,transform] duration-150 focus:-translate-y-px focus:border-tif10-acc focus:bg-tif10-acc/10 motion-reduce:transition-none motion-reduce:focus:translate-y-0">
  </fieldset>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif10-bg: #12121a;
  --color-tif10-bg: oklch(0.19 0.015 285);
  --color-tif10-field: #1a1a22;
  --color-tif10-field: oklch(0.23 0.015 285);
  --color-tif10-ink: #f0eeff;
  --color-tif10-ink: oklch(0.95 0.02 290);
  --color-tif10-acc: #7c6cff;
  --color-tif10-acc: oklch(0.62 0.2 288);
  --font-tif10-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-10 {
  width: 100%;
}

.tif-10 ::selection {
  background: var(--color-tif10-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tif-10').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var inputs = Array.prototype.slice.call(root.querySelectorAll('[data-tif10]'));
    inputs.forEach(function (input, i) {
      input.addEventListener('input', function () {
        input.value = (input.value || '').replace(/\D/g, '').slice(0, 1);
        if (input.value && inputs[i + 1]) inputs[i + 1].focus();
      });
      input.addEventListener('keydown', function (e) {
        if (e.key === 'Backspace' && !input.value && inputs[i - 1]) {
          inputs[i - 1].focus();
        }
        if (e.key === 'ArrowLeft' && inputs[i - 1]) inputs[i - 1].focus();
        if (e.key === 'ArrowRight' && inputs[i + 1]) inputs[i + 1].focus();
      });
      input.addEventListener('paste', function (e) {
        var data = (e.clipboardData || window.clipboardData).getData('text');
        var digits = (data || '').replace(/\D/g, '').slice(0, inputs.length - i);
        if (!digits) return;
        e.preventDefault();
        for (var j = 0; j < digits.length; j++) {
          if (inputs[i + j]) inputs[i + j].value = digits[j];
        }
        inputs[Math.min(i + digits.length, inputs.length - 1)].focus();
      });
    });
  });
})();
```
