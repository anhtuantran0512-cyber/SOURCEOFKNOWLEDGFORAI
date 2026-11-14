---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sidebar-pinned-user-profile-footer/"
title: "Tailwind Sidebar Menu with Pinned User Profile Footer"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "Navigation up top, profile locked to the bottom &mdash; the answer is mt-auto in a flex column."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar Menu with Pinned User Profile Footer
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sidebar-pinned-user-profile-footer/

Navigation up top, profile locked to the bottom &mdash; the answer is mt-auto in a flex column. The middle nav scrolls when it outgrows the rail, with mask-gradient fades hinting at the overflow, and the demo's real lesson is one easily-forgotten utility: min-h-0.
## HTML
```html
<section class="tsl-17 w-full h-svh min-h-svh grid grid-cols-[256px_1fr] font-tsl17-sans bg-tsl17-bg text-tsl17-ink">
  <aside class="flex flex-col h-full bg-tsl17-panel border-r border-tsl17-line">
    <div class="flex items-center gap-2.5 px-[22px] pt-5 pb-4 text-[15px] font-bold tracking-tight"><span aria-hidden="true" class="w-[26px] h-[26px] rounded-lg bg-[conic-gradient(from_300deg,var(--color-tsl17-accent),oklch(0.6_0.14_30))]"></span>Basecamp OS</div>
    <nav aria-label="Main" class="flex-1 min-h-0 overflow-y-auto overscroll-contain flex flex-col gap-0.5 px-3 py-2 scroll-py-5 [mask-image:linear-gradient(180deg,transparent,#000_16px,#000_calc(100%-16px),transparent)]">
      <a href="#" aria-current="page" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover aria-[current=page]:text-tsl17-accent aria-[current=page]:bg-tsl17-tint focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Today</a>
      <a href="#" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Projects</a>
      <a href="#" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Messages</a>
      <a href="#" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Schedule</a>
      <a href="#" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Docs &amp; files</a>
      <a href="#" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Check-ins</a>
      <a href="#" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Reports</a>
      <a href="#" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Integrations</a>
      <a href="#" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Templates</a>
      <a href="#" class="flex-none flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl17-mut no-underline transition-colors duration-[180ms] hover:text-tsl17-ink hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:outline-offset-2">Archive</a>
    </nav>
    <a href="#" class="mt-auto grid grid-cols-[auto_1fr_auto] items-center gap-[11px] min-h-[68px] px-4 py-3.5 border-t border-tsl17-line no-underline text-inherit transition-colors duration-[180ms] hover:bg-tsl17-hover focus-visible:outline-2 focus-visible:outline-tsl17-accent focus-visible:-outline-offset-2">
      <span aria-hidden="true" class="relative grid place-items-center w-[34px] h-[34px] rounded-full text-[11px] font-bold text-white bg-[linear-gradient(135deg,var(--color-tsl17-accent),oklch(0.55_0.15_30))]">JV<i class="absolute -right-px -bottom-px w-2.5 h-2.5 rounded-full bg-tsl17-online border-2 border-tsl17-panel"></i></span>
      <span><strong class="block text-[13px] font-semibold leading-tight">Jonas Vieira</strong><small class="text-[11px] leading-snug text-tsl17-mut">Product &middot; online</small></span>
      <svg viewBox="0 0 24 24" aria-hidden="true" class="w-[15px] h-[15px] fill-none stroke-tsl17-mut stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="m8 9 4-4 4 4m-8 6 4 4 4-4"/></svg>
    </a>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Today</h1>
    <p class="max-w-[47ch] text-sm leading-relaxed text-tsl17-mut text-pretty">The nav scrolls in the middle (note the fade masks); brand and profile never move. One <code class="font-tsl17-mono text-[12.5px]">mt-auto</code> does the pinning.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl17-bg: #14120f;
  --color-tsl17-bg: oklch(0.13 0.012 60);
  --color-tsl17-panel: #1c1916;
  --color-tsl17-panel: oklch(0.17 0.016 60);
  --color-tsl17-ink: #efece7;
  --color-tsl17-ink: oklch(0.94 0.006 60);
  --color-tsl17-mut: #a39c92;
  --color-tsl17-mut: oklch(0.65 0.015 60);
  --color-tsl17-line: #3b362f;
  --color-tsl17-line: oklch(0.28 0.018 60);
  --color-tsl17-accent: #dba84c;
  --color-tsl17-accent: oklch(0.76 0.13 65);
  --color-tsl17-online: #4fd39a;
  --color-tsl17-online: oklch(0.75 0.17 155);
  --color-tsl17-hover: rgb(239 236 231 / 0.06);
  --color-tsl17-hover: color-mix(in oklab, oklch(0.94 0.006 60) 6%, transparent);
  --color-tsl17-tint: rgb(219 168 76 / 0.16);
  --color-tsl17-tint: color-mix(in oklab, oklch(0.76 0.13 65) 16%, transparent);
  --font-tsl17-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl17-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-17 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
