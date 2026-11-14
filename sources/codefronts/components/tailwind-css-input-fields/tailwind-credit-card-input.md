---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-credit-card-input/"
title: "Tailwind Credit Card Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Auto-formatted card number with brand-aware accent."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Credit Card Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-credit-card-input/

Auto-formatted card number with brand-aware accent. The brand lives in a data-brand attribute and every colour reads it as a variant — and unlike the original, reformatting no longer throws your caret to the end of the field.
## HTML
```html
<div class="tif-26 grid min-h-svh w-full place-items-center bg-tif26-bg px-6 py-14 font-tif26-mono" aria-label="Credit card input demo">
  <label class="grid w-full max-w-80 gap-1.5">
    <span class="text-[10px] tracking-[0.12em] text-tif26-mut uppercase">Card number</span>
    <span data-tif26 class="group flex items-center gap-2.5 rounded-[10px] border border-white/12 bg-tif26-field py-0 pr-3 pl-3.5 transition-colors duration-200 focus-within:border-tif26-acc">
      <span aria-hidden="true" data-tif26-brand
        class="shrink-0 rounded bg-tif26-acc/12 px-1.75 py-0.75 text-[9px] font-bold tracking-[0.08em] text-tif26-acc transition-colors duration-200 group-data-[brand=visa]:bg-tif26-visa/18 group-data-[brand=visa]:text-tif26-visa group-data-[brand=mastercard]:bg-tif26-mc/16 group-data-[brand=mastercard]:text-tif26-mc group-data-[brand=amex]:bg-tif26-amex/16 group-data-[brand=amex]:text-tif26-amex group-data-[brand=discover]:bg-tif26-disc/16 group-data-[brand=discover]:text-tif26-disc">CARD</span>
      <input type="text" name="tif26-cc" inputmode="numeric" autocomplete="cc-number" maxlength="19" placeholder="•••• •••• •••• ••••" aria-describedby="tif26-note"
        class="min-w-0 flex-1 border-0 bg-transparent py-3.25 text-sm font-semibold tracking-[0.08em] tabular-nums text-tif26-ink outline-none placeholder:text-tif26-mut">
    </span>
    <span id="tif26-note" class="text-[10px] text-tif26-mut">Demo only — never collect raw card numbers outside a PCI-compliant iframe.</span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif26-bg: #12121a;
  --color-tif26-bg: oklch(0.19 0.015 285);
  --color-tif26-field: #1a1a22;
  --color-tif26-field: oklch(0.23 0.015 285);
  --color-tif26-ink: #f0eeff;
  --color-tif26-ink: oklch(0.95 0.02 290);
  --color-tif26-mut: #b8b6d4;
  --color-tif26-mut: oklch(0.77 0.03 290);
  --color-tif26-acc: #f5a84a;
  --color-tif26-acc: oklch(0.79 0.13 70);
  --color-tif26-visa: #6aa3e0;
  --color-tif26-visa: oklch(0.7 0.1 250);
  --color-tif26-mc: #ff7a7a;
  --color-tif26-mc: oklch(0.72 0.15 25);
  --color-tif26-amex: #2eb88a;
  --color-tif26-amex: oklch(0.7 0.13 165);
  --color-tif26-disc: #fbbf24;
  --color-tif26-disc: oklch(0.84 0.16 85);
  --font-tif26-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-26 {
  width: 100%;
}

.tif-26 ::selection {
  background: var(--color-tif26-acc);
  color: #12121a;
}
```

## JavaScript
```js
(function () {
  function detect(digits) {
    if (/^4/.test(digits)) return ['visa', 'VISA'];
    if (/^(5[1-5]|2[2-7])/.test(digits)) return ['mastercard', 'MC'];
    if (/^3[47]/.test(digits)) return ['amex', 'AMEX'];
    if (/^6(011|5)/.test(digits)) return ['discover', 'DISC'];
    return ['', 'CARD'];
  }

  document.querySelectorAll('.tif-26').forEach(function (root) {
    if (root.dataset.bound) return; root.dataset.bound = '1';
    var wrap = root.querySelector('[data-tif26]');
    var badge = root.querySelector('[data-tif26-brand]');
    var input = wrap && wrap.querySelector('input');
    if (!wrap || !input) return;

    input.addEventListener('input', function () {
      var caret = input.selectionStart;
      var digitsBefore = input.value.slice(0, caret).replace(/\D/g, '').length;
      var digits = input.value.replace(/\D/g, '').slice(0, 19);
      input.value = (digits.match(/.{1,4}/g) || ['']).join(' ');

      var seen = 0, pos = 0;
      while (pos < input.value.length && seen < digitsBefore) {
        if (/\d/.test(input.value[pos])) seen++;
        pos++;
      }
      input.setSelectionRange(pos, pos);

      var info = detect(digits);
      if (info[0]) wrap.setAttribute('data-brand', info[0]);
      else wrap.removeAttribute('data-brand');
      if (badge) badge.textContent = info[1];
    });
  });
})();
```
