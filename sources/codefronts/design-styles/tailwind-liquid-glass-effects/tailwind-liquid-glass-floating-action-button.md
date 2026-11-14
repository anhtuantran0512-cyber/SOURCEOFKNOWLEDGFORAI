---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-floating-action-button/"
title: "Tailwind Liquid Glass Floating Action Button"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "A glass FAB that fans out into frosted sub-actions on tap, staggered like droplets."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Floating Action Button
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-floating-action-button/

A glass FAB that fans out into frosted sub-actions on tap, staggered like droplets. All of it is one sr-only checkbox and peer-checked: transforms &mdash; and because each sub-action carries its own delay utility, the stagger is readable in the markup instead of computed in a stylesheet.
## HTML
```html
<section class="lgt-18 relative w-full min-h-svh overflow-hidden bg-lgt18-bg font-lgt18-sans" aria-label="Tailwind liquid glass floating action button">
  <img src="https://picsum.photos/seed/lgfab/1000/750" width="1000" height="750" alt="App backdrop" class="absolute inset-0 size-full object-cover">

  <div class="absolute right-8 bottom-8 size-15.5">
    <input type="checkbox" id="lgt-18-open" class="peer sr-only">

    <a href="#lgt-18" aria-label="Share" class="pointer-events-none absolute right-2.75 bottom-2.75 z-2 grid size-11 scale-0 place-items-center rounded-full border border-white/40 bg-white/16 text-[17px] text-white no-underline opacity-0 backdrop-blur-[14px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_10px_22px_-10px_rgba(0,0,0,.6)] transition-[transform,opacity] duration-400 ease-lgt18 delay-0 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white peer-checked:pointer-events-auto peer-checked:scale-100 peer-checked:opacity-100 peer-checked:-translate-y-[74px] motion-reduce:transition-opacity motion-reduce:peer-checked:translate-y-0 motion-reduce:peer-checked:-translate-y-[74px]">&#8599;</a>

    <a href="#lgt-18" aria-label="Add photo" class="pointer-events-none absolute right-2.75 bottom-2.75 z-2 grid size-11 scale-0 place-items-center rounded-full border border-white/40 bg-white/16 text-[17px] text-white no-underline opacity-0 backdrop-blur-[14px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_10px_22px_-10px_rgba(0,0,0,.6)] transition-[transform,opacity] duration-400 ease-lgt18 delay-75 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white peer-checked:pointer-events-auto peer-checked:scale-100 peer-checked:opacity-100 peer-checked:-translate-x-[52px] peer-checked:-translate-y-[52px] motion-reduce:transition-opacity">&#9704;</a>

    <a href="#lgt-18" aria-label="New note" class="pointer-events-none absolute right-2.75 bottom-2.75 z-2 grid size-11 scale-0 place-items-center rounded-full border border-white/40 bg-white/16 text-[17px] text-white no-underline opacity-0 backdrop-blur-[14px] backdrop-saturate-170 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_10px_22px_-10px_rgba(0,0,0,.6)] transition-[transform,opacity] duration-400 ease-lgt18 delay-150 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white peer-checked:pointer-events-auto peer-checked:scale-100 peer-checked:opacity-100 peer-checked:-translate-x-[74px] motion-reduce:transition-opacity">&#9998;</a>

    <label for="lgt-18-open" aria-label="Open actions" class="absolute inset-0 z-3 grid cursor-pointer place-items-center rounded-full border border-lgt18-accent/60 bg-linear-to-b from-lgt18-accent-top to-lgt18-accent shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_16px_30px_-12px_rgba(0,0,0,.7)] transition-transform duration-300 peer-checked:rotate-135 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-white motion-reduce:transition-none">
      <span aria-hidden="true" class="relative size-5.5 before:absolute before:top-1/2 before:left-1/2 before:h-[2.5px] before:w-5 before:-translate-x-1/2 before:-translate-y-1/2 before:rounded-sm before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-[2.5px] after:w-5 after:-translate-x-1/2 after:-translate-y-1/2 after:rotate-90 after:rounded-sm after:bg-white"></span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt18-bg: #100c1e;
  --color-lgt18-accent: #6d4cf2;
  --color-lgt18-accent: oklch(0.64 0.2 285);
  --color-lgt18-accent-top: #8a6ff7;
  --color-lgt18-accent-top: oklch(0.7 0.17 285);
  --font-lgt18-sans: 'Manrope', system-ui, sans-serif;
  --ease-lgt18: cubic-bezier(0.3, 1.3, 0.5, 1);
}
```
