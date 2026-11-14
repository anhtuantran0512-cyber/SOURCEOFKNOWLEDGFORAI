---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-sliding-capsule-tab-bar-group-has/"
title: "Tailwind Sliding Capsule Tab Bar (group-has)"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "A segmented glass tab bar where the capsule slides behind the selected item with no JavaScript &mdash; and the port that best justifies itself."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sliding Capsule Tab Bar (group-has)
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-sliding-capsule-tab-bar-group-has/

A segmented glass tab bar where the capsule slides behind the selected item with no JavaScript &mdash; and the port that best justifies itself. The CSS version needs four :has() rules in a stylesheet; here the whole state table lives on the capsule as group-has-[#nbtw-17-2:checked]:translate-x-[86px], one utility per tab, readable in place.
## HTML
```html
<section class="nbtw-17 grid place-items-center w-full min-h-svh p-5 font-nb17-sans bg-[conic-gradient(from_200deg_at_50%_50%,#00c2ff,#8e2de2,#ff6a88,#00c2ff)] bg-[length:200%_200%] animate-nb17-bg motion-reduce:animate-none" aria-label="Sliding capsule active tab demo">
  <div class="group relative flex p-[7px] rounded-full isolate bg-[color-mix(in_oklab,white_14%,transparent)] border border-white/40 shadow-[inset_0_1px_0_rgba(255,255,255,.55),0_20px_44px_-24px_rgba(0,0,0,.55)] backdrop-blur-[22px] backdrop-saturate-[1.8]">
    <span class="absolute inset-y-[7px] left-[7px] z-0 w-[86px] rounded-full bg-white/[0.26] border border-white/[0.55] shadow-[inset_0_1px_0_rgba(255,255,255,.7)] transition-transform duration-[450ms] ease-nb17 group-has-[#nbtw-17-2:checked]:translate-x-[86px] group-has-[#nbtw-17-3:checked]:translate-x-[172px] group-has-[#nbtw-17-4:checked]:translate-x-[258px] motion-reduce:transition-none" aria-hidden="true"></span>
    <input class="peer sr-only" type="radio" name="nbtw-17" id="nbtw-17-1" checked>
    <label class="relative z-[1] flex items-center justify-center w-[86px] min-h-10 rounded-full cursor-pointer text-white/85 text-[14.5px] font-semibold transition-colors duration-250 peer-checked:text-white peer-focus-visible:outline-2 peer-focus-visible:outline-white peer-focus-visible:outline-offset-2" for="nbtw-17-1">Day</label>
    <input class="peer sr-only" type="radio" name="nbtw-17" id="nbtw-17-2">
    <label class="relative z-[1] flex items-center justify-center w-[86px] min-h-10 rounded-full cursor-pointer text-white/85 text-[14.5px] font-semibold transition-colors duration-250 peer-checked:text-white peer-focus-visible:outline-2 peer-focus-visible:outline-white peer-focus-visible:outline-offset-2" for="nbtw-17-2">Week</label>
    <input class="peer sr-only" type="radio" name="nbtw-17" id="nbtw-17-3">
    <label class="relative z-[1] flex items-center justify-center w-[86px] min-h-10 rounded-full cursor-pointer text-white/85 text-[14.5px] font-semibold transition-colors duration-250 peer-checked:text-white peer-focus-visible:outline-2 peer-focus-visible:outline-white peer-focus-visible:outline-offset-2" for="nbtw-17-3">Month</label>
    <input class="peer sr-only" type="radio" name="nbtw-17" id="nbtw-17-4">
    <label class="relative z-[1] flex items-center justify-center w-[86px] min-h-10 rounded-full cursor-pointer text-white/85 text-[14.5px] font-semibold transition-colors duration-250 peer-checked:text-white peer-focus-visible:outline-2 peer-focus-visible:outline-white peer-focus-visible:outline-offset-2" for="nbtw-17-4">Year</label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb17-sans: system-ui, 'Segoe UI', sans-serif;
  --ease-nb17: cubic-bezier(0.34, 1.56, 0.5, 1);
  --animate-nb17-bg: nb17-bg 20s ease-in-out infinite;
}

@keyframes nb17-bg {
  50% {
    background-position: 100% 100%;
  }
}
```
