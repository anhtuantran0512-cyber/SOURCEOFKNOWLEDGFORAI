---
source: "codefronts"
url: "https://codefronts.com/components/css-input-fields/credit-card/"
title: "Credit Card"
section: "components"
category: "css-input-fields"
category_name: "CSS Input Fields"
description: "Auto-formatted 16-digit card number with brand-aware accent (Visa, Mastercard, Amex)."
has_js: "true"
---

Here's a working CSS Input Field from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Credit Card
Source: https://codefronts.com/components/css-input-fields/credit-card/

Auto-formatted 16-digit card number with brand-aware accent (Visa, Mastercard, Amex). `inputmode="numeric"` on mobile; pattern validation; `autocomplete="cc-number"`.
## HTML
```html
<label class="if-26">
  <span class="if-26-label">Card number</span>
  <span class="if-26-wrap" data-if-26>
    <span class="if-26-brand" aria-hidden="true">CARD</span>
    <input
      type="text"
      name="cc"
      inputmode="numeric"
      autocomplete="cc-number"
      maxlength="19"
      placeholder="•••• •••• •••• ••••"
    />
  </span>
</label>
```
## CSS
```css
.if-26 {
  display: grid;
  gap: 6px;
  width: 100%;
  max-width: 320px;
}

.if-26-label {
  font-family: "JetBrains Mono", monospace;
  font-size: 10px;
  letter-spacing: 0.12em;
  color: #b8b6d4;
  text-transform: uppercase;
}

.if-26-wrap {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 0 12px 0 14px;
  background: #1a1a22;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 10px;
  transition: border-color 0.2s;
}

.if-26-wrap:focus-within {
  border-color: #f5a84a;
}

.if-26-brand {
  font-family: "JetBrains Mono", monospace;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 3px 7px;
  background: rgba(245, 168, 74, 0.12);
  color: #f5a84a;
  border-radius: 4px;
  flex-shrink: 0;
  transition: background 0.2s, color 0.2s;
}

.if-26-wrap[data-brand="visa"] .if-26-brand {
  background: rgba(67, 127, 193, 0.18);
  color: #6aa3e0;
}

.if-26-wrap[data-brand="mastercard"] .if-26-brand {
  background: rgba(255, 90, 90, 0.16);
  color: #ff7a7a;
}

.if-26-wrap[data-brand="amex"] .if-26-brand {
  background: rgba(46, 184, 138, 0.16);
  color: #2eb88a;
}

.if-26 input {
  flex: 1;
  min-width: 0;
  padding: 13px 0;
  border: 0;
  outline: none;
  background: transparent;
  color: #f0eeff;
  font: 600 14px/1 "JetBrains Mono", monospace;
  letter-spacing: 0.08em;
}

.if-26 input::placeholder {
  color: #b8b6d4;
}
```

## JavaScript
```js
// Credit Card — auto-format groups of 4 + brand detection
document.querySelectorAll("[data-if-26] input").forEach(function (input) {
  var wrap = input.closest("[data-if-26]");
  var brand = wrap.querySelector(".if-26-brand");

  function detect(digits) {
    if (/^4/.test(digits)) return ["visa", "VISA"];
    if (/^(5[1-5]|2[2-7])/.test(digits)) return ["mastercard", "MC"];
    if (/^3[47]/.test(digits)) return ["amex", "AMEX"];
    if (/^6(011|5)/.test(digits)) return ["discover", "DISC"];
    return ["", "CARD"];
  }

  input.addEventListener("input", function () {
    var digits = input.value.replace(/\\D/g, "").slice(0, 19);
    input.value = (digits.match(/.{1,4}/g) || [""]).join(" ");
    var info = detect(digits);
    if (info[0]) wrap.setAttribute("data-brand", info[0]);
    else wrap.removeAttribute("data-brand");
    brand.textContent = info[1];
  });
});
```
