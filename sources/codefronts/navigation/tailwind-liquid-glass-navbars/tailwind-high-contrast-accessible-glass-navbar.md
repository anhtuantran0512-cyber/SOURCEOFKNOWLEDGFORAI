---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-high-contrast-accessible-glass-navbar/"
title: "Tailwind High-Contrast Accessible Glass Navbar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "A glass navbar that refuses to trade beauty for accessibility &mdash; and the port where two whole media-query blocks become two variants."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind High-Contrast Accessible Glass Navbar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-high-contrast-accessible-glass-navbar/

A glass navbar that refuses to trade beauty for accessibility &mdash; and the port where two whole media-query blocks become two variants. forced-colors: maps the bar to system colours; contrast-more: darkens the scrim. A semi-opaque scrim under the frost guarantees 4.5:1 over a bright, busy photograph, and the focus ring is a 4px high-contrast outline.
## HTML
```html
<section class="nbtw-20 grid place-items-center w-full min-h-svh p-5 font-nb20-sans bg-[linear-gradient(120deg,#f7971e,#ffd200_60%,#f7f7f7),url('https://picsum.photos/seed/nb20bright/1000/700')] bg-center bg-cover [background-blend-mode:overlay]" aria-label="High contrast accessible glass navbar demo">
  <nav class="relative flex flex-wrap items-center gap-x-5 gap-y-3 w-[min(760px,100%)] px-4.5 py-3.5 rounded-2xl text-white bg-[rgba(18,20,28,.66)] border border-white/50 shadow-[inset_0_1px_0_rgba(255,255,255,.55),inset_0_0_0_1px_rgba(0,0,0,.25),0_18px_40px_-22px_rgba(0,0,0,.7)] backdrop-blur-[16px] backdrop-saturate-150 contrast-more:bg-[rgba(10,10,16,.9)] forced-colors:bg-[Canvas] forced-colors:border-[CanvasText] forced-colors:text-[CanvasText]" aria-label="Primary">
    <span class="text-base font-extrabold [text-shadow:0_1px_2px_rgba(0,0,0,.6)]">◆ Access</span>
    <div class="flex flex-wrap gap-1 ms-auto">
      <a class="flex items-center min-h-11 px-[15px] rounded-[10px] no-underline text-white text-[15px] font-semibold [text-shadow:0_1px_2px_rgba(0,0,0,.55)] transition-colors duration-200 hover:bg-white/[0.18] focus-visible:outline-4 focus-visible:outline-[#ffe000] focus-visible:outline-offset-2 aria-[current=page]:bg-white/[0.24] aria-[current=page]:underline aria-[current=page]:underline-offset-4 forced-colors:text-[LinkText]" href="#nbtw-20" aria-current="page">Home</a>
      <a class="flex items-center min-h-11 px-[15px] rounded-[10px] no-underline text-white text-[15px] font-semibold [text-shadow:0_1px_2px_rgba(0,0,0,.55)] transition-colors duration-200 hover:bg-white/[0.18] focus-visible:outline-4 focus-visible:outline-[#ffe000] focus-visible:outline-offset-2 forced-colors:text-[LinkText]" href="#nbtw-20">Guides</a>
      <a class="flex items-center min-h-11 px-[15px] rounded-[10px] no-underline text-white text-[15px] font-semibold [text-shadow:0_1px_2px_rgba(0,0,0,.55)] transition-colors duration-200 hover:bg-white/[0.18] focus-visible:outline-4 focus-visible:outline-[#ffe000] focus-visible:outline-offset-2 forced-colors:text-[LinkText]" href="#nbtw-20">Tools</a>
      <a class="flex items-center min-h-11 px-[15px] rounded-[10px] no-underline text-white text-[15px] font-semibold [text-shadow:0_1px_2px_rgba(0,0,0,.55)] transition-colors duration-200 hover:bg-white/[0.18] focus-visible:outline-4 focus-visible:outline-[#ffe000] focus-visible:outline-offset-2 forced-colors:text-[LinkText]" href="#nbtw-20">Contact</a>
    </div>
    <button class="min-h-11 px-4.5 rounded-[10px] border-2 border-white bg-white text-[#101018] text-[15px] font-extrabold cursor-pointer focus-visible:outline-4 focus-visible:outline-[#ffe000] focus-visible:outline-offset-2 forced-colors:bg-[ButtonFace] forced-colors:text-[ButtonText] forced-colors:border-[ButtonText]" type="button">Get help</button>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb20-sans: system-ui, 'Segoe UI', sans-serif;
}
```
