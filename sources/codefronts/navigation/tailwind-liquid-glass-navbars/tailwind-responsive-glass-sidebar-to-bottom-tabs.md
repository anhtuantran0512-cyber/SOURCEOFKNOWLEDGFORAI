---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-responsive-glass-sidebar-to-bottom-tabs/"
title: "Tailwind Responsive Glass Sidebar to Bottom Tabs"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "One glass navigation that adapts to its container: a floating vertical sidebar when there is room, re-flowing into a bottom tab bar when there is not."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Responsive Glass Sidebar to Bottom Tabs
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-responsive-glass-sidebar-to-bottom-tabs/

One glass navigation that adapts to its container: a floating vertical sidebar when there is room, re-flowing into a bottom tab bar when there is not. Same links, same material, no duplicated markup and no JavaScript. The port puts the whole reflow on the elements as @max-[560px]: utilities, which makes the two layouts readable side by side.
## HTML
```html
<section class="nbtw-24 w-full min-h-svh p-3.5 font-nb24-sans bg-[linear-gradient(130deg,#654ea3,#4776e6_60%,#8e54e9)]" aria-label="Responsive glass sidebar to bottom tabs demo">
  <div class="@container relative min-h-[calc(100svh-28px)] rounded-[20px] overflow-hidden bg-[radial-gradient(circle_at_30%_20%,rgba(255,255,255,.14),transparent_60%),url('https://picsum.photos/seed/nb24/1000/700')] bg-center bg-cover">
    <nav class="absolute z-[5] top-4 left-4 bottom-4 flex flex-col items-stretch gap-1.5 w-[150px] px-2.5 py-3.5 rounded-[18px] text-white bg-[color-mix(in_oklab,white_14%,transparent)] border border-white/40 shadow-[inset_0_1px_0_rgba(255,255,255,.5),0_20px_44px_-24px_rgba(0,0,0,.6)] backdrop-blur-[24px] backdrop-saturate-[1.8] @max-[560px]:top-auto @max-[560px]:inset-x-4 @max-[560px]:bottom-4 @max-[560px]:w-auto @max-[560px]:flex-row @max-[560px]:justify-around @max-[560px]:p-2" aria-label="Primary">
      <span class="py-1.5 pb-2.5 text-center text-[22px] @max-[560px]:hidden" aria-hidden="true">◆</span>
      <a class="flex items-center gap-3 min-h-11 px-3.5 rounded-xl no-underline text-white/85 text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 aria-[current=page]:bg-white/[0.24] aria-[current=page]:text-white @max-[560px]:flex-col @max-[560px]:gap-[3px] @max-[560px]:justify-center @max-[560px]:min-w-14 @max-[560px]:px-1.5 @max-[560px]:py-1.5" href="#nbtw-24" aria-current="page"><span class="w-5.5 text-center text-[19px] leading-none @max-[560px]:w-auto" aria-hidden="true">⌂</span><span class="@max-[560px]:text-[11px]">Home</span></a>
      <a class="flex items-center gap-3 min-h-11 px-3.5 rounded-xl no-underline text-white/85 text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 @max-[560px]:flex-col @max-[560px]:gap-[3px] @max-[560px]:justify-center @max-[560px]:min-w-14 @max-[560px]:px-1.5 @max-[560px]:py-1.5" href="#nbtw-24"><span class="w-5.5 text-center text-[19px] leading-none @max-[560px]:w-auto" aria-hidden="true">⌕</span><span class="@max-[560px]:text-[11px]">Search</span></a>
      <a class="flex items-center gap-3 min-h-11 px-3.5 rounded-xl no-underline text-white/85 text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 @max-[560px]:flex-col @max-[560px]:gap-[3px] @max-[560px]:justify-center @max-[560px]:min-w-14 @max-[560px]:px-1.5 @max-[560px]:py-1.5" href="#nbtw-24"><span class="w-5.5 text-center text-[19px] leading-none @max-[560px]:w-auto" aria-hidden="true">▤</span><span class="@max-[560px]:text-[11px]">Library</span></a>
      <a class="flex items-center gap-3 min-h-11 px-3.5 rounded-xl no-underline text-white/85 text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 @max-[560px]:flex-col @max-[560px]:gap-[3px] @max-[560px]:justify-center @max-[560px]:min-w-14 @max-[560px]:px-1.5 @max-[560px]:py-1.5" href="#nbtw-24"><span class="w-5.5 text-center text-[19px] leading-none @max-[560px]:w-auto" aria-hidden="true">◔</span><span class="@max-[560px]:text-[11px]">Activity</span></a>
      <a class="flex items-center gap-3 min-h-11 px-3.5 rounded-xl no-underline text-white/85 text-[14.5px] font-semibold transition-[background-color,color] duration-200 hover:bg-white/[0.16] hover:text-white focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2 @max-[560px]:flex-col @max-[560px]:gap-[3px] @max-[560px]:justify-center @max-[560px]:min-w-14 @max-[560px]:px-1.5 @max-[560px]:py-1.5" href="#nbtw-24"><span class="w-5.5 text-center text-[19px] leading-none @max-[560px]:w-auto" aria-hidden="true">◉</span><span class="@max-[560px]:text-[11px]">Profile</span></a>
    </nav>
    <div class="min-h-[calc(100svh-28px)] grid place-items-center p-6 ps-[190px] @max-[560px]:p-6 @max-[560px]:pb-30">
      <p class="max-w-[34ch] text-center text-white text-[15px] font-semibold leading-[1.6] [text-shadow:0_2px_14px_rgba(0,0,0,.35)]">Resize the preview: the glass sidebar re-flows into a bottom tab bar — one nav, one material, zero duplicate markup, and the whole reflow stated on the elements themselves.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb24-sans: system-ui, 'Segoe UI', sans-serif;
}
```
