---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-phone-input-with-country/"
title: "Tailwind Phone Input With Country"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A native <select> for the dialling code welded to a type=\"tel\" field inside one focus ring."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Phone Input With Country
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-phone-input-with-country/

A native <select> for the dialling code welded to a type="tel" field inside one focus ring. Semantic by default: the select is a real select, so iOS gives you the wheel and screen readers give you a listbox.
## HTML
```html
<div class="tif-13 grid min-h-svh w-full place-items-center bg-tif13-bg px-6 py-14 font-tif13-sans" aria-label="Phone input with country demo">
  <label class="grid w-full max-w-70 gap-1.5 text-[11px] text-tif13-mut">
    <span class="font-semibold">Phone</span>
    <span class="grid grid-cols-[auto_1fr] overflow-hidden rounded-lg border border-white/10 bg-tif13-field transition-[border-color,box-shadow] duration-200 focus-within:border-tif13-acc focus-within:ring-3 focus-within:ring-tif13-acc/15">
      <select aria-label="Country code" name="tif13-country"
        class="cursor-pointer appearance-none border-0 border-r border-white/10 bg-white/4 bg-[url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2210%22 height=%226%22 viewBox=%220 0 10 6%22 fill=%22none%22 stroke=%22%239d9bbf%22 stroke-width=%221.5%22 stroke-linecap=%22round%22><path d=%22M1 1l4 4 4-4%22/></svg>')] bg-[position:right_10px_center] bg-no-repeat py-2.5 pr-7 pl-3 text-[13px] text-tif13-ink outline-none [&>option]:bg-tif13-field [&>option]:text-tif13-ink">
        <option value="+44">🇬🇧 +44</option>
        <option value="+1" selected>🇺🇸 +1</option>
        <option value="+91">🇮🇳 +91</option>
        <option value="+33">🇫🇷 +33</option>
        <option value="+49">🇩🇪 +49</option>
        <option value="+81">🇯🇵 +81</option>
      </select>
      <input type="tel" name="tif13-phone" autocomplete="tel" placeholder="(555) 123-4567" required
        class="min-w-0 border-0 bg-transparent px-3 py-2.5 text-sm text-tif13-ink outline-none placeholder:text-tif13-mut">
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif13-bg: #12121a;
  --color-tif13-bg: oklch(0.19 0.015 285);
  --color-tif13-field: #1a1a22;
  --color-tif13-field: oklch(0.23 0.015 285);
  --color-tif13-ink: #f0eeff;
  --color-tif13-ink: oklch(0.95 0.02 290);
  --color-tif13-mut: #b8b6d4;
  --color-tif13-mut: oklch(0.77 0.03 290);
  --color-tif13-acc: #ef4444;
  --color-tif13-acc: oklch(0.63 0.22 27);
  --font-tif13-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-13 {
  width: 100%;
}

.tif-13 ::selection {
  background: var(--color-tif13-acc);
  color: #12121a;
}
```
