---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-password-strength-meter/"
title: "Tailwind Password Strength Meter"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A live strength bar graded from native constraints alone — minlength and a character-class pattern, read through group-has-[…] into four bar widths."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Password Strength Meter
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-password-strength-meter/

A live strength bar graded from native constraints alone — minlength and a character-class pattern, read through group-has-[…] into four bar widths. No scoring library, no script.
## HTML
```html
<div class="tif-09 grid min-h-svh w-full place-items-center bg-tif09-bg px-6 py-14 font-tif09-sans" aria-label="Password strength meter demo">
  <label class="group grid w-full max-w-70 gap-1.5 text-[11px] text-tif09-mut">
    <span class="font-semibold">Password</span>
    <input type="password" name="tif09-pw" autocomplete="new-password" placeholder="At least 12 characters" minlength="12" pattern="(?=.*\d)(?=.*[^A-Za-z0-9]).{12,}" required aria-describedby="tif09-hint"
      class="w-full rounded-lg border border-white/10 bg-tif09-field px-3.5 py-2.5 text-sm text-tif09-ink outline-none transition-colors duration-200 focus:border-tif09-acc">
    <span class="relative h-1 overflow-hidden rounded-full bg-white/8" aria-hidden="true">
      <span class="absolute inset-y-0 left-0 w-0 rounded-full bg-linear-to-r from-tif09-bad via-tif09-warn to-tif09-ok transition-[width] duration-300 ease-out group-has-[input:not(:placeholder-shown):invalid]:w-[30%] group-has-[input:not(:placeholder-shown):valid]:w-[65%] group-has-[input:focus:valid]:w-full motion-reduce:transition-none"></span>
    </span>
    <span id="tif09-hint" class="text-[10.5px] text-tif09-mut">Use 12+ characters with letters, numbers, and a symbol.</span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif09-bg: #12121a;
  --color-tif09-bg: oklch(0.19 0.015 285);
  --color-tif09-field: #1a1a22;
  --color-tif09-field: oklch(0.23 0.015 285);
  --color-tif09-ink: #f0eeff;
  --color-tif09-ink: oklch(0.95 0.02 290);
  --color-tif09-mut: #b8b6d4;
  --color-tif09-mut: oklch(0.77 0.03 290);
  --color-tif09-acc: #c084fc;
  --color-tif09-acc: oklch(0.75 0.17 305);
  --color-tif09-bad: #ef4444;
  --color-tif09-bad: oklch(0.63 0.22 27);
  --color-tif09-warn: #f59e0b;
  --color-tif09-warn: oklch(0.76 0.16 70);
  --color-tif09-ok: #22c55e;
  --color-tif09-ok: oklch(0.73 0.19 145);
  --font-tif09-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-09 {
  width: 100%;
}

.tif-09 ::selection {
  background: var(--color-tif09-acc);
  color: #12121a;
}
```
