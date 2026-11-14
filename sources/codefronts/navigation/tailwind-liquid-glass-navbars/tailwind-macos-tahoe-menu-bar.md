---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-macos-tahoe-menu-bar/"
title: "Tailwind macOS Tahoe Menu Bar"
section: "navigation"
category: "tailwind-liquid-glass-navbars"
category_name: "Tailwind Liquid Glass Navbars"
description: "The razor-thin translucent strip from macOS Tahoe, and the cleanest port in the collection: not one rule survives into a stylesheet."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind macOS Tahoe Menu Bar
Source: https://codefronts.com/navigation/tailwind-liquid-glass-navbars/tailwind-macos-tahoe-menu-bar/

The razor-thin translucent strip from macOS Tahoe, and the cleanest port in the collection: not one rule survives into a stylesheet. Every property &mdash; the 34px height, the blur(30px) saturate(180%) frost, the hairline bottom border, the inset top rim, the margin-inline-start:auto status cluster &mdash; has a utility, so the whole menu bar is markup plus a four-line @theme block.
## HTML
```html
<section class="nbtw-02 relative block w-full min-h-svh overflow-hidden font-nb02-sans bg-[radial-gradient(120%_90%_at_20%_0%,#ff9d6c,#c14bd6_45%,#3b2a86_100%)]" aria-label="macOS Tahoe menu bar demo">
  <header class="sticky top-0 z-[5] flex items-center gap-1 h-[34px] px-3 text-white bg-[color-mix(in_oklab,white_14%,transparent)] border-b border-white/[0.28] shadow-[inset_0_1px_0_rgba(255,255,255,.4)] backdrop-blur-[30px] backdrop-saturate-[1.8] [text-shadow:0_1px_3px_rgba(0,0,0,.25)]">
    <span class="text-[17px] mr-1" aria-hidden="true">◐</span>
    <nav class="flex items-center" aria-label="Menu bar">
      <button class="min-h-[26px] px-[11px] py-[5px] rounded-[7px] font-bold text-[13.5px] text-white bg-transparent border-0 cursor-pointer transition-colors duration-150 hover:bg-white/[0.22] focus-within:bg-white/[0.22] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-1" type="button">Lumen</button>
      <button class="min-h-[26px] px-[11px] py-[5px] rounded-[7px] text-[13.5px] text-white bg-transparent border-0 cursor-pointer transition-colors duration-150 hover:bg-white/[0.22] focus-within:bg-white/[0.22] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-1" type="button">File</button>
      <button class="min-h-[26px] px-[11px] py-[5px] rounded-[7px] text-[13.5px] text-white bg-transparent border-0 cursor-pointer transition-colors duration-150 hover:bg-white/[0.22] focus-within:bg-white/[0.22] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-1" type="button">Edit</button>
      <button class="min-h-[26px] px-[11px] py-[5px] rounded-[7px] text-[13.5px] text-white bg-transparent border-0 cursor-pointer transition-colors duration-150 hover:bg-white/[0.22] focus-within:bg-white/[0.22] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-1" type="button">View</button>
      <button class="min-h-[26px] px-[11px] py-[5px] rounded-[7px] text-[13.5px] text-white bg-transparent border-0 cursor-pointer transition-colors duration-150 hover:bg-white/[0.22] focus-within:bg-white/[0.22] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-1" type="button">Window</button>
      <button class="min-h-[26px] px-[11px] py-[5px] rounded-[7px] text-[13.5px] text-white bg-transparent border-0 cursor-pointer transition-colors duration-150 hover:bg-white/[0.22] focus-within:bg-white/[0.22] focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-1" type="button">Help</button>
    </nav>
    <div class="ms-auto flex items-center gap-3.5 text-[13px]">
      <span class="opacity-95 cursor-default" title="Wi-Fi" aria-label="Wi-Fi">▲</span>
      <span class="opacity-95 cursor-default" title="Battery" aria-label="Battery">▮</span>
      <span class="opacity-95 cursor-default" title="Search" aria-label="Search">⌕</span>
      <span class="font-semibold tabular-nums">Wed 9:41 AM</span>
    </div>
  </header>
  <div class="h-[calc(100svh-34px)] grid place-items-center">
    <span class="text-[clamp(48px,12vw,96px)] font-extrabold tracking-[-0.04em] text-white/[0.14]">Tahoe</span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --font-nb02-sans: -apple-system, system-ui, 'Segoe UI', sans-serif;
}
```
