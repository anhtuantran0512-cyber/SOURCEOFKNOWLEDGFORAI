---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-performance-tuned-glass-navbar/"
title: "Tailwind Performance-Tuned Glass Navbar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The glass navbar built for a steady 60fps and clean Core Web Vitals: the expensive paint is boxed with [contain:layout_paint_style] and isolate, the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Performance-Tuned Glass Navbar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-performance-tuned-glass-navbar/

The glass navbar built for a steady 60fps and clean Core Web Vitals: the expensive paint is boxed with [contain:layout_paint_style] and isolate, the compositor is hinted with will-change-transform on the one animating layer, the specular sweep animates transform only, and the blur is capped on purpose. The port keeps every one of those decisions visible on the element it applies to.
## HTML
```html
<section class="nbtw-22 grid place-items-center w-full min-h-svh p-5 font-nb22-sans bg-[linear-gradient(120deg,#2c3e50,#4ca1af_70%,#c4e0e5)]" aria-label="Performance tuned glass navbar demo">
  <nav class="relative overflow-hidden isolate [contain:layout_paint_style] flex flex-wrap items-center gap-x-4.5 gap-y-3 w-[min(740px,100%)] px-4.5 py-3.5 rounded-2xl text-white bg-[color-mix(in_oklab,white_12%,transparent)] border border-white/[0.34] shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_16px_38px_-22px_rgba(0,0,0,.55)] backdrop-blur-[18px] backdrop-saturate-[1.7]" aria-label="Primary">
    <span class="absolute inset-0 z-0 pointer-events-none -translate-x-[120%] will-change-transform bg-[linear-gradient(105deg,transparent_40%,rgba(255,255,255,.35)_50%,transparent_60%)] animate-nb22-sweep motion-reduce:hidden" aria-hidden="true"></span>
    <span class="relative z-[1] text-base font-extrabold">⚡ Sixty</span>
    <div class="relative z-[1] flex flex-wrap gap-1">
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:opacity-100 aria-[current=page]:bg-white/[0.18]" href="#nbtw-22" aria-current="page">Home</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-22">Metrics</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-22">Budget</a>
      <a class="flex items-center min-h-10 px-3.5 rounded-[10px] no-underline text-white opacity-90 text-[14.5px] font-semibold transition-[background-color,opacity] duration-200 hover:opacity-100 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-22">Docs</a>
    </div>
    <span class="relative z-[1] ms-auto text-[11px] font-bold tracking-[0.06em] uppercase tabular-nums text-white/70" aria-hidden="true">60 fps</span>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb22-sans: system-ui, 'Segoe UI', sans-serif;
  --animate-nb22-sweep: nb22-sweep 5s ease-in-out infinite;
}
/* Transform only, with a long idle phase, so the specular pass stays on the
   compositor and never touches layout or paint. */

@keyframes nb22-sweep {
  0%,
    60% {
    transform: translateX(-120%);
  }

  100% {
    transform: translateX(120%);
  }
}
```
