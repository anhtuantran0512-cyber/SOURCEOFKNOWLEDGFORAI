---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-safari-toolbar-with-svg-refraction/"
title: "Tailwind Safari Toolbar with SVG Refraction"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The toolbar that goes past blur into real optical refraction, ported with the filter reference sitting on the element as an arbitrary utility:…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Safari Toolbar with SVG Refraction
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-safari-toolbar-with-svg-refraction/

The toolbar that goes past blur into real optical refraction, ported with the filter reference sitting on the element as an arbitrary utility: [filter:url(#nbtw-03-refract)]. The feTurbulence + feDisplacementMap pair stays in the markup where it belongs, the frost is backdrop-blur-[14px], and the only stylesheet rule is the @supports not fallback &mdash; a negated feature query has no variant form.
## HTML
```html
<section class="nbtw-03 relative block w-full min-h-svh overflow-hidden font-nb03-sans bg-[linear-gradient(125deg,#00c6fb,#7b5bff_45%,#ff5ea8),url('https://picsum.photos/seed/nb03/1000/700')] bg-center bg-cover [background-blend-mode:overlay]" aria-label="Safari liquid glass toolbar demo">
  <svg class="absolute w-0 h-0" aria-hidden="true" focusable="false"><filter id="nbtw-03-refract"><feTurbulence type="fractalNoise" baseFrequency="0.008 0.012" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="16" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
  <header class="sticky top-0 z-[5] flex items-center gap-2.5 h-13 px-3.5 isolate bg-[color-mix(in_oklab,white_12%,transparent)] border-b border-white/30 shadow-[inset_0_1px_0_rgba(255,255,255,.45),0_10px_30px_-18px_rgba(0,0,0,.5)] backdrop-blur-[14px] backdrop-saturate-[1.7]">
    <span class="nbtw-03__glass absolute inset-x-0 -inset-y-10 z-0 pointer-events-none opacity-60 [background:inherit] [filter:url(#nbtw-03-refract)] motion-reduce:[filter:none]" aria-hidden="true"></span>
    <div class="relative z-[2] flex gap-1">
      <button class="size-[34px] rounded-[10px] border border-white/35 bg-white/[0.16] text-white text-lg leading-none cursor-pointer transition-colors duration-200 hover:bg-white/30 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button" aria-label="Back">‹</button>
      <button class="size-[34px] rounded-[10px] border border-white/35 bg-white/[0.16] text-white text-lg leading-none cursor-pointer transition-colors duration-200 hover:bg-white/30 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button" aria-label="Forward">›</button>
    </div>
    <label class="relative z-[2] flex flex-1 items-center gap-2 h-[34px] px-3.5 rounded-[10px] bg-white/90 shadow-[inset_0_1px_3px_rgba(0,0,0,.15)] focus-within:shadow-[0_0_0_3px_rgba(255,255,255,.7),inset_0_1px_3px_rgba(0,0,0,.15)]">
      <span class="text-xs" aria-hidden="true">🔒</span>
      <input class="flex-1 min-w-0 border-0 bg-transparent outline-none text-sm text-[#111]" type="text" value="codefronts.com/liquid-glass" aria-label="Address" spellcheck="false">
    </label>
    <button class="relative z-[2] size-[34px] rounded-[10px] border border-white/35 bg-white/[0.16] text-white text-lg leading-none cursor-pointer transition-colors duration-200 hover:bg-white/30 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button" aria-label="Share">⤴</button>
  </header>
  <div class="px-6 py-10 text-white">
    <p class="max-w-[40ch] text-lg font-semibold leading-[1.6] [text-shadow:0_2px_12px_rgba(0,0,0,.35)]">Watch the background bend through the toolbar — that warp is a live SVG displacement map, not a blur.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb03-sans: -apple-system, system-ui, 'Segoe UI', sans-serif;
}
/* A negated feature query has no variant form, so this is the one rule that
   cannot move into the markup: where filter: url() will not resolve, the
   displaced layer is removed and the plain backdrop-blur tier remains. */

@supports not (filter: url(#nbtw-03-refract)) {
  .nbtw-03__glass {
    display: none;
  }
}
```
