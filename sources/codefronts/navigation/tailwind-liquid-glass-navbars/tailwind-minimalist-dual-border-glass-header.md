---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-minimalist-dual-border-glass-header/"
title: "Tailwind Minimalist Dual-Border Glass Header"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The most restrained take: a header defined almost entirely by light."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Dual-Border Glass Header
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-minimalist-dual-border-glass-header/

The most restrained take: a header defined almost entirely by light. A 1px outer hairline pairs with a 1px inner highlight to read as the two faces of a physical pane, over the lightest frost in the collection. In the port this is where v4's inset-ring shines &mdash; the inner edge becomes a real utility instead of an arbitrary inset shadow.
## HTML
```html
<section class="nbtw-23 grid place-items-center w-full min-h-svh p-5 font-nb23-sans bg-[linear-gradient(120deg,#485563,#29323c_60%,#7b6b8f)]" aria-label="Minimalist dual border glass header demo">
  <header class="flex flex-wrap items-center gap-x-6 gap-y-3 w-[min(720px,100%)] px-5 py-3.75 rounded-[14px] text-white bg-white/[0.08] border border-white/[0.55] inset-ring inset-ring-white/[0.75] shadow-[inset_0_-1px_0_rgba(255,255,255,.3),0_18px_36px_-22px_rgba(0,0,0,.55)] backdrop-blur-[14px] backdrop-saturate-150">
    <span class="text-[15px] font-bold tracking-[0.02em] text-white/95">— clear</span>
    <nav class="flex flex-wrap gap-0.5 ms-auto" aria-label="Primary">
      <a class="flex items-center min-h-10 px-3.25 rounded-lg no-underline text-white/[0.66] text-sm font-medium tracking-[0.01em] transition-[color,background-color] duration-200 hover:text-white hover:bg-white/[0.08] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:text-white" href="#nbtw-23" aria-current="page">Index</a>
      <a class="flex items-center min-h-10 px-3.25 rounded-lg no-underline text-white/[0.66] text-sm font-medium tracking-[0.01em] transition-[color,background-color] duration-200 hover:text-white hover:bg-white/[0.08] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-23">Work</a>
      <a class="flex items-center min-h-10 px-3.25 rounded-lg no-underline text-white/[0.66] text-sm font-medium tracking-[0.01em] transition-[color,background-color] duration-200 hover:text-white hover:bg-white/[0.08] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-23">Info</a>
    </nav>
    <a class="flex items-center min-h-10 px-3.25 rounded-lg no-underline text-white/90 text-sm font-medium tracking-[0.01em] border border-white/[0.28] shadow-[inset_0_1px_0_rgba(255,255,255,.4)] transition-[color,background-color] duration-200 hover:text-white hover:bg-white/[0.08] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-23">Contact →</a>
  </header>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb23-sans: system-ui, 'Segoe UI', sans-serif;
}
```
