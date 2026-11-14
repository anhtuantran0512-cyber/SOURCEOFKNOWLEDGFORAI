---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-animated-gradient-blobs-glass-navbar/"
title: "Tailwind Animated Gradient Blobs Glass Navbar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The showcase setup for any glass bar: three blurred blobs drift behind it so the frost has rich, moving colour to refract &mdash; because liquid glass over…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Gradient Blobs Glass Navbar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-animated-gradient-blobs-glass-navbar/

The showcase setup for any glass bar: three blurred blobs drift behind it so the frost has rich, moving colour to refract &mdash; because liquid glass over flat black is invisible. The port turns each orbit into an --animate-* theme entry, so three long keyframe loops become three single utilities and the blobs themselves are four classes each.
## HTML
```html
<section class="nbtw-16 relative overflow-hidden grid place-items-center w-full min-h-svh p-5 font-nb16-sans bg-[#0a0616]" aria-label="Animated gradient blobs glass navbar demo">
  <div class="absolute inset-0 z-0" aria-hidden="true">
    <span class="absolute -top-20 -left-10 size-85 rounded-full blur-[60px] opacity-85 will-change-transform bg-[radial-gradient(circle,#5b8cff,transparent_70%)] animate-nb16-a motion-reduce:animate-none"></span>
    <span class="absolute -bottom-25 -right-8 size-85 rounded-full blur-[60px] opacity-85 will-change-transform bg-[radial-gradient(circle,#ff5ea8,transparent_70%)] animate-nb16-b motion-reduce:animate-none"></span>
    <span class="absolute top-[40%] left-[45%] size-85 rounded-full blur-[60px] opacity-85 will-change-transform bg-[radial-gradient(circle,#38e8c6,transparent_70%)] animate-nb16-c motion-reduce:animate-none"></span>
  </div>
  <nav class="relative z-[1] flex flex-wrap items-center gap-x-5.5 gap-y-3 px-5 py-3.5 rounded-[20px] text-white bg-[color-mix(in_oklab,white_10%,transparent)] border border-white/30 shadow-[inset_0_1px_0_rgba(255,255,255,.45),0_24px_50px_-26px_rgba(0,0,0,.7)] backdrop-blur-[24px] backdrop-saturate-[1.9]" aria-label="Primary">
    <span class="text-base font-extrabold">◐ Prism</span>
    <div class="flex flex-wrap gap-1.5">
      <a class="flex items-center min-h-10 px-4 rounded-xl no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:opacity-100 aria-[current=page]:bg-white/[0.18]" href="#nbtw-16" aria-current="page">Gallery</a>
      <a class="flex items-center min-h-10 px-4 rounded-xl no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-16">Artists</a>
      <a class="flex items-center min-h-10 px-4 rounded-xl no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-16">Shop</a>
      <a class="flex items-center min-h-10 px-4 rounded-xl no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-16">Journal</a>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb16-sans: system-ui, 'Segoe UI', sans-serif;
  --animate-nb16-a: nb16-a 16s ease-in-out infinite;
  --animate-nb16-b: nb16-b 20s ease-in-out infinite;
  --animate-nb16-c: nb16-c 24s ease-in-out infinite;
}
/* Transform-only, so all three layers stay on the compositor. The durations
   are mutually non-divisible on purpose: the composition never realigns, so
   it keeps producing new colour instead of visibly looping. */

@keyframes nb16-a {
  50% {
    transform: translate(120px, 80px) scale(1.2);
  }
}

@keyframes nb16-b {
  50% {
    transform: translate(-120px, -60px) scale(1.15);
  }
}

@keyframes nb16-c {
  50% {
    transform: translate(-80px, 60px) scale(0.85);
  }
}
```
