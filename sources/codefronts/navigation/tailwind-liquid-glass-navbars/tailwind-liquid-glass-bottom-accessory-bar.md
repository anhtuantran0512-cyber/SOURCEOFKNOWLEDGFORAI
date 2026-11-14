---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-liquid-glass-bottom-accessory-bar/"
title: "Tailwind Liquid Glass Bottom Accessory Bar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The iOS 26 bottom-accessory pattern: a now-playing mini-player floating above the tab bar, two glass surfaces sharing one material at two elevations."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Bottom Accessory Bar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-liquid-glass-bottom-accessory-bar/

The iOS 26 bottom-accessory pattern: a now-playing mini-player floating above the tab bar, two glass surfaces sharing one material at two elevations. This is also the port's most honest lesson &mdash; with no @apply, the shared frost recipe is typed twice, and the notes explain why that is the right call rather than a workaround.
## HTML
```html
<section class="nbtw-05 relative block w-full min-h-svh overflow-hidden font-nb05-sans bg-[conic-gradient(from_120deg_at_70%_30%,#ff6a3d,#ff2d78,#7a2bff,#ff6a3d)] bg-[length:200%_200%] animate-nb05-bg motion-reduce:animate-none" aria-label="Liquid glass bottom accessory bar demo">
  <div class="min-h-svh grid place-items-center p-6 pb-50">
    <p class="max-w-[34ch] text-center text-white text-base font-semibold leading-[1.6] [text-shadow:0_2px_12px_rgba(0,0,0,.3)]">Now-playing accessory floats above the tab bar — two glass surfaces, one material, and the frost recipe typed twice because utilities have no shared class.</p>
  </div>
  <div class="absolute inset-x-3 bottom-3 flex flex-col gap-2">
    <div class="relative flex items-center gap-3 px-3 py-2.5 rounded-[20px] text-white bg-[color-mix(in_oklab,white_16%,transparent)] border border-white/40 shadow-[inset_0_1px_0_rgba(255,255,255,.55),0_20px_40px_-22px_rgba(0,0,0,.6)] backdrop-blur-[26px] backdrop-saturate-[1.8]" role="group" aria-label="Now playing">
      <span class="flex-none size-[46px] rounded-xl bg-[linear-gradient(135deg,#ffd36b,#ff5ea8)] shadow-[inset_0_1px_0_rgba(255,255,255,.6)]" aria-hidden="true"></span>
      <span class="flex flex-col min-w-0">
        <span class="text-[14.5px] font-bold truncate">Solar Fields</span>
        <span class="text-[12.5px] text-white/80 truncate">Nova — Aurora EP</span>
      </span>
      <span class="absolute inset-x-3 bottom-1 h-[3px] rounded-[3px] bg-white/[0.28]" aria-hidden="true"><span class="block w-[42%] h-full rounded-[3px] bg-white"></span></span>
      <span class="ms-auto flex items-center gap-1">
        <button class="size-11 rounded-xl border-0 bg-transparent text-white text-[17px] cursor-pointer transition-colors duration-200 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button" aria-label="Previous">⏮</button>
        <button class="size-11 rounded-xl border-0 bg-nb05-accent text-white text-base cursor-pointer transition-colors duration-200 hover:bg-[color-mix(in_oklab,var(--color-nb05-accent)_85%,white)] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button" aria-label="Play">⏵</button>
        <button class="size-11 rounded-xl border-0 bg-transparent text-white text-[17px] cursor-pointer transition-colors duration-200 hover:bg-white/[0.18] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" type="button" aria-label="Next">⏭</button>
      </span>
    </div>
    <nav class="flex justify-around p-2 rounded-[22px] bg-[color-mix(in_oklab,white_16%,transparent)] border border-white/40 shadow-[inset_0_1px_0_rgba(255,255,255,.55),0_20px_40px_-22px_rgba(0,0,0,.6)] backdrop-blur-[26px] backdrop-saturate-[1.8]" aria-label="Primary">
      <a class="flex flex-col items-center justify-center gap-[3px] min-w-14 min-h-11 rounded-[14px] no-underline text-white/[0.82] text-[11px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.12] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:bg-white/20 aria-[current=page]:text-white" href="#nbtw-05" aria-current="page"><span class="text-[19px]" aria-hidden="true">⌂</span>Home</a>
      <a class="flex flex-col items-center justify-center gap-[3px] min-w-14 min-h-11 rounded-[14px] no-underline text-white/[0.82] text-[11px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.12] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-05"><span class="text-[19px]" aria-hidden="true">◎</span>Radio</a>
      <a class="flex flex-col items-center justify-center gap-[3px] min-w-14 min-h-11 rounded-[14px] no-underline text-white/[0.82] text-[11px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.12] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-05"><span class="text-[19px]" aria-hidden="true">♪</span>Library</a>
      <a class="flex flex-col items-center justify-center gap-[3px] min-w-14 min-h-11 rounded-[14px] no-underline text-white/[0.82] text-[11px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.12] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2" href="#nbtw-05"><span class="text-[19px]" aria-hidden="true">⌕</span>Search</a>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-nb05-accent: #f0522f;
  --color-nb05-accent: oklch(0.66 0.2 20);
  --font-nb05-sans: system-ui, 'Segoe UI', sans-serif;
  --animate-nb05-bg: nb05-bg 20s ease-in-out infinite;
}

@keyframes nb05-bg {
  50% {
    background-position: 100% 100%;
  }
}
```
