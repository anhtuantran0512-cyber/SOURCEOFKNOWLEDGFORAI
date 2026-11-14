---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-fallback-first-glass-navbar/"
title: "Tailwind Fallback-First Glass Navbar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "A glass navbar engineered to never look broken, and the port where Tailwind wins outright: the entire @supports tiering moves into the markup as…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Fallback-First Glass Navbar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-fallback-first-glass-navbar/

A glass navbar engineered to never look broken, and the port where Tailwind wins outright: the entire @supports tiering moves into the markup as supports-[backdrop-filter:blur(1px)]: utilities. The base class list is the opaque, hand-tuned fallback; the variant twins upgrade it to real frost. Both tiers sit in one class list, so neither can be forgotten.
## HTML
```html
<section class="nbtw-19 grid place-items-center w-full min-h-svh p-5 font-nb19-sans bg-[linear-gradient(120deg,#134e5e,#71b280)]" aria-label="Fallback-first glass navbar demo">
  <nav class="flex flex-wrap items-center gap-x-5 gap-y-3 w-[min(720px,100%)] px-4.5 py-3.5 rounded-2xl text-white bg-[linear-gradient(180deg,rgba(30,50,55,.92),rgba(20,38,42,.96))] border border-white/[0.22] shadow-[inset_0_1px_0_rgba(255,255,255,.35),0_16px_38px_-22px_rgba(0,0,0,.6)] supports-[backdrop-filter:blur(1px)]:bg-none supports-[backdrop-filter:blur(1px)]:bg-[color-mix(in_oklab,white_12%,transparent)] supports-[backdrop-filter:blur(1px)]:backdrop-blur-[20px] supports-[backdrop-filter:blur(1px)]:backdrop-saturate-[1.8]" aria-label="Primary">
    <span class="text-base font-extrabold">⛬ Resilient</span>
    <div class="flex flex-wrap gap-1 ms-auto">
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white/[0.86] text-[14.5px] font-semibold transition-colors duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:bg-white/[0.16] aria-[current=page]:text-white" href="#nbtw-19" aria-current="page">Home</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white/[0.86] text-[14.5px] font-semibold transition-colors duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-19">Support</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white/[0.86] text-[14.5px] font-semibold transition-colors duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-19">Status</a>
    </div>
    <span class="text-[11px] font-bold tracking-[0.06em] uppercase text-white/60" aria-hidden="true">
      <span class="supports-[backdrop-filter:blur(1px)]:hidden">fallback tier</span>
      <span class="hidden supports-[backdrop-filter:blur(1px)]:inline">backdrop-filter tier</span>
    </span>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb19-sans: system-ui, 'Segoe UI', sans-serif;
}
```
