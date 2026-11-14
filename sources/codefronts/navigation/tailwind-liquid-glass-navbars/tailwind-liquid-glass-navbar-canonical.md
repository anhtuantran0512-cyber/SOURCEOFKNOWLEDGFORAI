---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-liquid-glass-navbar-canonical/"
title: "Tailwind Liquid Glass Navbar (Canonical)"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The canonical version, and the only demo in the collection written almost entirely from Tailwind's default scale &mdash; backdrop-blur-xl, bg-white/10,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Navbar (Canonical)
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-liquid-glass-navbar-canonical/

The canonical version, and the only demo in the collection written almost entirely from Tailwind's default scale &mdash; backdrop-blur-xl, bg-white/10, ring-1 ring-white/20, rounded-full. No bracket values in the bar itself, nothing to tune, nothing to name. If you want one glass header to paste into a project and move on, this is it.
## HTML
```html
<section class="nbtw-07 grid place-items-start justify-center w-full min-h-svh px-5 py-6.5 font-nb07-sans bg-[linear-gradient(120deg,#3a1c71,#d76d77_50%,#ffaf7b)] bg-[length:180%_180%] animate-nb07-bg motion-reduce:animate-none" aria-label="Tailwind liquid glass navbar demo">
  <header class="flex flex-wrap items-center gap-x-5 gap-y-3 w-[min(820px,100%)] ps-5.5 pe-4 py-3 rounded-full text-white bg-white/10 ring-1 ring-white/20 inset-ring inset-ring-white/25 backdrop-blur-xl backdrop-saturate-150 shadow-[0_18px_40px_-22px_rgba(0,0,0,.6)]">
    <a class="text-[17px] font-extrabold tracking-[-0.01em] no-underline text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-07">◆ Utility</a>
    <nav class="flex flex-wrap gap-1 ms-auto" aria-label="Primary">
      <a class="flex items-center min-h-10 px-[15px] rounded-full no-underline text-white/85 text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.14] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:bg-white/20 aria-[current=page]:text-white" href="#nbtw-07" aria-current="page">Product</a>
      <a class="flex items-center min-h-10 px-[15px] rounded-full no-underline text-white/85 text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.14] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-07">Docs</a>
      <a class="flex items-center min-h-10 px-[15px] rounded-full no-underline text-white/85 text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.14] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-07">Pricing</a>
      <a class="flex items-center min-h-10 px-[15px] rounded-full no-underline text-white/85 text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.14] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-07">Blog</a>
    </nav>
    <button class="min-h-10 px-5 rounded-full border-0 bg-white text-[#3a1c71] text-[14.5px] font-bold cursor-pointer transition-transform duration-200 hover:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-[3px] motion-reduce:transition-none" type="button">Sign up</button>
  </header>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb07-sans: system-ui, 'Segoe UI', sans-serif;
  --animate-nb07-bg: nb07-bg 16s ease-in-out infinite;
}

@keyframes nb07-bg {
  50% {
    background-position: 100% 100%;
  }
}
```
