---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-underline-sweep-input/"
title: "Tailwind Underline Sweep Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A hairline underline that draws outward from the centre on focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Underline Sweep Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-underline-sweep-input/

A hairline underline that draws outward from the centre on focus. The whole effect is one element and one variant: an after: bar pinned at left-1/2 right-1/2, released to focus-within:after:inset-x-0.
## HTML
```html
<div class="tif-02 grid min-h-svh w-full place-items-center bg-tif02-bg px-6 py-14 font-tif02-sans" aria-label="Underline sweep input demo">
  <label class="grid w-full max-w-70 gap-1.5">
    <span class="text-[11px] tracking-[0.08em] text-tif02-mut uppercase">Username</span>
    <span class="relative block border-b border-white/14 after:absolute after:bottom-[-1px] after:left-1/2 after:right-1/2 after:h-0.5 after:bg-linear-to-r after:from-tif02-acc after:to-tif02-acc2 after:transition-[left,right] after:duration-300 after:ease-out after:content-[''] focus-within:after:inset-x-0 motion-reduce:after:transition-none">
      <input type="text" name="tif02-user" autocomplete="username" placeholder="@codefronts" required
        class="w-full appearance-none border-0 bg-transparent py-2 text-sm text-tif02-ink outline-none placeholder:text-tif02-mut">
    </span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif02-bg: #12121a;
  --color-tif02-bg: oklch(0.19 0.015 285);
  --color-tif02-ink: #f0eeff;
  --color-tif02-ink: oklch(0.95 0.02 290);
  --color-tif02-mut: #b8b6d4;
  --color-tif02-mut: oklch(0.77 0.03 290);
  --color-tif02-acc: #ff6c8a;
  --color-tif02-acc: oklch(0.72 0.17 15);
  --color-tif02-acc2: #ff9a76;
  --color-tif02-acc2: oklch(0.78 0.14 45);
  --font-tif02-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-02 {
  width: 100%;
}

.tif-02 ::selection {
  background: var(--color-tif02-acc);
  color: #12121a;
}
```
