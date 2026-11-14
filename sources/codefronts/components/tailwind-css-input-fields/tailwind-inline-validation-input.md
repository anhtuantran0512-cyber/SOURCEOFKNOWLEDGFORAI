---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-inline-validation-input/"
title: "Tailwind Inline Validation Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "Live valid/invalid feedback with zero JavaScript, graded on :user-valid and :user-invalid rather than :valid/:invalid — so the field is never marked wrong…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Inline Validation Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-inline-validation-input/

Live valid/invalid feedback with zero JavaScript, graded on :user-valid and :user-invalid rather than :valid/:invalid — so the field is never marked wrong before it has been touched. That is the gotcha the CSS original lists and does not fix.
## HTML
```html
<div class="tif-07 grid min-h-svh w-full place-items-center bg-tif07-bg px-6 py-14 font-tif07-sans" aria-label="Inline validation input demo">
  <label class="group grid w-full max-w-70 gap-1.5 text-[11px] text-tif07-mut">
    <span class="font-semibold tracking-[0.04em]">Email</span>
    <span class="relative block after:absolute after:top-1/2 after:right-3 after:size-4.5 after:-translate-y-1/2 after:scale-50 after:rounded-full after:bg-center after:bg-no-repeat after:opacity-0 after:transition-[transform,opacity,background-color] after:duration-200 after:content-[''] group-has-[input:user-invalid]:after:scale-100 group-has-[input:user-invalid]:after:bg-tif07-bad group-has-[input:user-invalid]:after:opacity-100 group-has-[input:user-invalid]:after:bg-[url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2210%22 height=%2210%22 viewBox=%220 0 10 10%22 fill=%22none%22 stroke=%22white%22 stroke-width=%221.6%22 stroke-linecap=%22round%22><path d=%22M2 2 L8 8 M8 2 L2 8%22/></svg>')] group-has-[input:user-valid]:after:scale-100 group-has-[input:user-valid]:after:bg-tif07-ok group-has-[input:user-valid]:after:opacity-100 group-has-[input:user-valid]:after:bg-[url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2210%22 height=%2210%22 viewBox=%220 0 10 10%22 fill=%22none%22 stroke=%22white%22 stroke-width=%221.8%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22><path d=%22M2 5 L4.2 7.2 L8 3%22/></svg>')] motion-reduce:after:transition-opacity">
      <input type="email" name="tif07-email" autocomplete="email" placeholder="[email protected]" required
        class="w-full rounded-lg border border-white/10 bg-tif07-field py-2.5 pr-9.5 pl-3.5 text-sm text-tif07-ink outline-none transition-colors duration-200 focus:border-tif07-acc user-invalid:border-tif07-bad/55 user-valid:border-tif07-ok/55">
    </span>
    <span class="text-[10.5px] text-tif07-mut">We'll never share your address.</span>
  </label>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif07-bg: #12121a;
  --color-tif07-bg: oklch(0.19 0.015 285);
  --color-tif07-field: #1a1a22;
  --color-tif07-field: oklch(0.23 0.015 285);
  --color-tif07-ink: #f0eeff;
  --color-tif07-ink: oklch(0.95 0.02 290);
  --color-tif07-mut: #b8b6d4;
  --color-tif07-mut: oklch(0.77 0.03 290);
  --color-tif07-acc: #7c6cff;
  --color-tif07-acc: oklch(0.62 0.2 288);
  --color-tif07-ok: #22c55e;
  --color-tif07-ok: oklch(0.73 0.19 145);
  --color-tif07-bad: #ef4444;
  --color-tif07-bad: oklch(0.63 0.22 27);
  --font-tif07-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-07 {
  width: 100%;
}

.tif-07 ::selection {
  background: var(--color-tif07-acc);
  color: #12121a;
}
```
