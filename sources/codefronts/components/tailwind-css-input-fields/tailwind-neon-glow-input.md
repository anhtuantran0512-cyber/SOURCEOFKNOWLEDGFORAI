---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-neon-glow-input/"
title: "Tailwind Neon Glow Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Cyan neon for dark dashboards and developer tools: a translucent cyan border on near-black, and three layered shadows that bloom together on focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Glow Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-neon-glow-input/

Cyan neon for dark dashboards and developer tools: a translucent cyan border on near-black, and three layered shadows that bloom together on focus. The layered shadow is one arbitrary utility — exactly the case Tailwind is not trying to tokenise.
## HTML
```html
<div class="tif-03 grid min-h-svh w-full place-items-center bg-tif03-bg px-6 py-14 font-tif03-mono" aria-label="Neon glow input demo">
  <label class="grid w-full max-w-70 gap-1.5">
    <span class="text-[10px] tracking-[0.18em] text-tif03-acc [text-shadow:0_0_8px_oklch(0.9_0.15_195/0.5)]">SECURE TOKEN</span>
    <input type="text" name="tif03-token" placeholder="sk_live_••••••••••••" required
      class="w-full rounded-md border border-tif03-acc/40 bg-tif03-field px-3.5 py-2.5 text-[13px] text-white outline-none transition-[border-color,box-shadow,background-color] duration-200 placeholder:text-tif03-acc/45 focus:border-tif03-acc focus:bg-tif03-field2 focus:shadow-[0_0_0_1px_var(--color-tif03-acc),0_0_16px_oklch(0.9_0.15_195/0.45),inset_0_0_12px_oklch(0.9_0.15_195/0.12)]">
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif03-bg: #07070f;
  --color-tif03-bg: oklch(0.13 0.012 280);
  --color-tif03-field: #0a0a14;
  --color-tif03-field: oklch(0.15 0.014 280);
  --color-tif03-field2: #0d1820;
  --color-tif03-field2: oklch(0.21 0.03 220);
  --color-tif03-acc: #6cffff;
  --color-tif03-acc: oklch(0.9 0.15 195);
  --font-tif03-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tif-03 {
  width: 100%;
}

.tif-03 ::selection {
  background: var(--color-tif03-acc);
  color: #07070f;
}
```
