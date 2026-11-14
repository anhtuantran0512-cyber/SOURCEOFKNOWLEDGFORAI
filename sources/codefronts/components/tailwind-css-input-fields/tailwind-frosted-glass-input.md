---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-input-fields/tailwind-frosted-glass-input/"
title: "Tailwind Frosted Glass Input"
section: "components"
category: "tailwind-css-input-fields"
category_name: "Tailwind CSS Input Fields"
description: "A frosted field floating over a blurred gradient."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Frosted Glass Input
Source: https://codefronts.com/components/tailwind-css-input-fields/tailwind-frosted-glass-input/

A frosted field floating over a blurred gradient. backdrop-blur-[20px] backdrop-saturate-150 does the frost, isolate traps the -z-10 backdrop inside the component, and the inner bevel is one inset shadow.
## HTML
```html
<div class="tif-04 grid min-h-svh w-full place-items-center bg-tif04-bg px-6 py-14 font-tif04-sans" aria-label="Frosted glass input demo">
  <div class="relative isolate w-full max-w-70 overflow-hidden rounded-2xl p-3.5">
    <div class="absolute inset-0 -z-10 scale-120 bg-[radial-gradient(40%_60%_at_30%_30%,#f59e0b_0%,transparent_60%),radial-gradient(50%_60%_at_80%_70%,#7c3aed_0%,transparent_60%)] bg-tif04-deep blur-2xl" aria-hidden="true"></div>
    <label class="grid gap-1.5">
      <span class="text-[11px] tracking-[0.1em] text-white/70 uppercase">Search</span>
      <input type="search" name="tif04-q" placeholder="Search anything…"
        class="w-full rounded-[10px] border border-white/20 bg-white/10 px-3 py-2.5 text-sm text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.18)] backdrop-blur-[20px] backdrop-saturate-150 outline-none transition-[border-color,background-color] duration-200 placeholder:text-white/45 focus:border-white/50 focus:bg-white/16">
    </label>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tif04-bg: #12121a;
  --color-tif04-bg: oklch(0.19 0.015 285);
  --color-tif04-deep: #0a0a14;
  --color-tif04-deep: oklch(0.15 0.014 280);
  --font-tif04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tif-04 {
  width: 100%;
}

.tif-04 ::selection {
  background: #f59e0b;
  color: #0a0a14;
}
```
