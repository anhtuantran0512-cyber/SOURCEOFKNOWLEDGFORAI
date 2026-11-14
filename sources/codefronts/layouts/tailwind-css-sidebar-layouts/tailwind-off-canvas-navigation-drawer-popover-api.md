---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-off-canvas-navigation-drawer-popover-api/"
title: "Tailwind Off-Canvas Navigation Drawer with the Popover API"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The off-canvas drawer rebuilt on the platform's newest primitive."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Off-Canvas Navigation Drawer with the Popover API
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-off-canvas-navigation-drawer-popover-api/

The off-canvas drawer rebuilt on the platform's newest primitive. popover="auto" ships Esc-to-close, light dismissal, focus return and top-layer rendering; v4 contributes real variants for the hard part &mdash; starting: for the entry animation and an open: variant for the resting state.
## HTML
```html
<section class="tsl-10 w-full h-svh min-h-svh grid grid-rows-[auto_1fr] font-tsl10-sans bg-tsl10-bg text-tsl10-ink">
  <header class="flex items-center gap-4 h-[54px] px-4 bg-tsl10-panel border-b border-tsl10-line text-[15px] font-semibold">
    <button popovertarget="tsl10-d" class="inline-flex items-center gap-2 min-h-11 px-3.5 rounded-[10px] border border-tsl10-line bg-transparent text-tsl10-ink text-[13.5px] font-medium cursor-pointer transition-colors duration-200 hover:bg-tsl10-hover focus-visible:outline-2 focus-visible:outline-tsl10-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[17px] h-[17px] fill-none stroke-current stroke-[1.9] [stroke-linecap:round]"><path d="M4 6h16M4 12h16M4 18h16"/></svg>Menu</button>
    <strong>Waypoint</strong>
  </header>
  <aside popover="auto" id="tsl10-d" aria-label="Navigation drawer" class="fixed inset-y-0 left-0 right-auto w-[min(300px,85vw)] h-full max-h-none m-0 p-4 border-0 border-r border-tsl10-line bg-tsl10-panel text-tsl10-ink -translate-x-full open:translate-x-0 starting:open:-translate-x-full transition-[translate,display,overlay] duration-[320ms] ease-[cubic-bezier(.4,0,.2,1)] [transition-behavior:allow-discrete] backdrop:bg-[oklch(0_0_0/0.45)] backdrop:backdrop-blur-[3px] backdrop:opacity-0 backdrop:open:opacity-100 backdrop:starting:open:opacity-0 backdrop:transition-[opacity,display,overlay] backdrop:duration-[320ms] backdrop:[transition-behavior:allow-discrete] motion-reduce:transition-none">
    <div class="flex items-center justify-between px-1.5 pt-1 pb-4 text-[15px] font-bold">
      <strong>Waypoint</strong>
      <button popovertarget="tsl10-d" popovertargetaction="hide" aria-label="Close menu" class="grid place-items-center w-11 h-11 rounded-[9px] border-0 bg-transparent text-tsl10-mut cursor-pointer transition-colors hover:text-tsl10-ink hover:bg-tsl10-hover focus-visible:outline-2 focus-visible:outline-tsl10-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[17px] h-[17px] fill-none stroke-current stroke-[1.9] [stroke-linecap:round]"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
    </div>
    <nav class="flex flex-col gap-0.5">
      <a href="#" aria-current="page" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl10-mut no-underline transition-colors duration-200 hover:text-tsl10-ink hover:bg-tsl10-hover aria-[current=page]:text-tsl10-accent aria-[current=page]:bg-tsl10-tint focus-visible:outline-2 focus-visible:outline-tsl10-accent focus-visible:outline-offset-2">Trips</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl10-mut no-underline transition-colors duration-200 hover:text-tsl10-ink hover:bg-tsl10-hover focus-visible:outline-2 focus-visible:outline-tsl10-accent focus-visible:outline-offset-2">Explore</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl10-mut no-underline transition-colors duration-200 hover:text-tsl10-ink hover:bg-tsl10-hover focus-visible:outline-2 focus-visible:outline-tsl10-accent focus-visible:outline-offset-2">Saved places</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl10-mut no-underline transition-colors duration-200 hover:text-tsl10-ink hover:bg-tsl10-hover focus-visible:outline-2 focus-visible:outline-tsl10-accent focus-visible:outline-offset-2">Offline maps</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl10-mut no-underline transition-colors duration-200 hover:text-tsl10-ink hover:bg-tsl10-hover focus-visible:outline-2 focus-visible:outline-tsl10-accent focus-visible:outline-offset-2">Account</a>
    </nav>
  </aside>
  <main class="p-7 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Trips</h1>
    <p class="max-w-[48ch] text-sm leading-relaxed text-tsl10-mut text-pretty">Open the drawer, then press <kbd class="font-tsl10-mono text-[11px] font-semibold px-1.5 py-0.5 rounded-[5px] border border-tsl10-line bg-tsl10-hover">Esc</kbd> or click outside &mdash; dismissal, focus return and the blurred backdrop are all native Popover API behaviour. No script.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl10-bg: #111a16;
  --color-tsl10-bg: oklch(0.14 0.015 165);
  --color-tsl10-panel: #17221d;
  --color-tsl10-panel: oklch(0.18 0.02 165);
  --color-tsl10-ink: #e8efea;
  --color-tsl10-ink: oklch(0.94 0.005 165);
  --color-tsl10-mut: #93a099;
  --color-tsl10-mut: oklch(0.65 0.012 165);
  --color-tsl10-line: #35423b;
  --color-tsl10-line: oklch(0.29 0.02 165);
  --color-tsl10-accent: #5fdcae;
  --color-tsl10-accent: oklch(0.78 0.15 160);
  --color-tsl10-hover: rgb(232 239 234 / 0.07);
  --color-tsl10-hover: color-mix(in oklab, oklch(0.94 0.005 165) 7%, transparent);
  --color-tsl10-tint: rgb(95 220 174 / 0.14);
  --color-tsl10-tint: color-mix(in oklab, oklch(0.78 0.15 160) 14%, transparent);
  --font-tsl10-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl10-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-10 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* A popover's closed state is :not(:popover-open), and v4 has no negated
   open variant — two lines of CSS are cheaper than an arbitrary variant here. */

.tsl-10 [popover]:not(:popover-open) {
  display: none;
}
```
