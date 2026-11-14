---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-brutalist-input/"
title: "Tailwind Brutalist Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A hard 2.5px border, zero radius and a flat offset shadow that the field presses into on focus. The whole aesthetic is four utilities, and the RTL flip the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Brutalist Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-brutalist-input/

A hard 2.5px border, zero radius and a flat offset shadow that the field presses into on focus. The whole aesthetic is four utilities, and the RTL flip the CSS original leaves as a gotcha is one rtl: variant here.
## HTML
```html
<div class="tif-28 grid min-h-svh w-full place-items-center bg-tif28-bg px-6 py-14 font-tif28-mono" aria-label="Brutalist input demo">
  <label class="grid w-full max-w-70 gap-2">
    <span class="text-[11px] font-bold tracking-[0.12em] text-tif28-ink">USERNAME_</span>
    <input type="text" name="tif28-user" placeholder="enter handle…" pattern="[a-z0-9_]{3,}" required
      class="w-full rounded-none border-[2.5px] border-tif28-edge bg-tif28-paper px-3.5 py-3 text-[13px] font-bold tracking-[0.06em] text-tif28-edge shadow-[5px_5px_0_var(--color-tif28-acc)] outline-none transition-[transform,box-shadow] duration-100 placeholder:text-tif28-edge/50 focus:translate-x-0.5 focus:translate-y-0.5 focus:shadow-[3px_3px_0_var(--color-tif28-acc)] user-invalid:shadow-[5px_5px_0_var(--color-tif28-bad)] rtl:shadow-[-5px_5px_0_var(--color-tif28-acc)] rtl:focus:-translate-x-0.5 rtl:focus:shadow-[-3px_3px_0_var(--color-tif28-acc)] motion-reduce:transition-none">
    <span class="text-[10px] tracking-[0.08em] text-tif28-ink/60">LOWERCASE_LETTERS_DIGITS_UNDERSCORE · MIN_3</span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif28-bg: #12121a;
  --color-tif28-bg: oklch(0.19 0.015 285);
  --color-tif28-paper: #f0eeff;
  --color-tif28-paper: oklch(0.95 0.02 290);
  --color-tif28-edge: #1a1a2e;
  --color-tif28-edge: oklch(0.22 0.04 285);
  --color-tif28-ink: #f0eeff;
  --color-tif28-ink: oklch(0.95 0.02 290);
  --color-tif28-acc: #ff6c8a;
  --color-tif28-acc: oklch(0.72 0.17 15);
  --color-tif28-bad: #ff5d6c;
  --color-tif28-bad: oklch(0.69 0.19 20);
  --font-tif28-mono: 'Space Mono', ui-monospace, monospace;
}

.tif-28 {
  width: 100%;
}

.tif-28 ::selection {
  background: var(--color-tif28-acc);
  color: #1a1a2e;
}
```
