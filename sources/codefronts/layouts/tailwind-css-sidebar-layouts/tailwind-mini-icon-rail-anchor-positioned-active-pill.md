---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-mini-icon-rail-anchor-positioned-active-pill/"
title: "Tailwind Mini Icon Rail Sidebar with Anchor-Positioned Active Pill"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The 68px icon rail perfected: 44px targets, hover tooltips, notification dots, a bottom-pinned avatar &mdash; and an active pill that glides between icons…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mini Icon Rail Sidebar with Anchor-Positioned Active Pill
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-mini-icon-rail-anchor-positioned-active-pill/

The 68px icon rail perfected: 44px targets, hover tooltips, notification dots, a bottom-pinned avatar &mdash; and an active pill that glides between icons using CSS anchor positioning. The effect teams reach for a motion library to get, with no script and a clean fallback.
## HTML
```html
<section class="tsl-14 w-full h-svh min-h-svh grid grid-cols-[68px_1fr] font-tsl14-sans bg-tsl14-bg text-tsl14-ink">
  <aside aria-label="Primary" class="relative flex flex-col items-center gap-1.5 py-3.5 bg-tsl14-panel border-r border-tsl14-line">
    <span aria-hidden="true" class="w-[30px] h-[30px] mb-3 rounded-[9px] bg-[conic-gradient(from_45deg,var(--color-tsl14-accent),oklch(0.62_0.17_285))]"></span>
    <span aria-hidden="true" class="tsl-14-pill absolute left-2 w-[3.5px] h-[26px] rounded"></span>
    <nav class="flex flex-col gap-1.5">
      <label data-tooltip="Home" class="relative z-[1] grid place-items-center w-11 h-11 rounded-xl text-tsl14-mut cursor-pointer transition-colors duration-200 hover:text-tsl14-ink has-checked:text-tsl14-accent has-checked:bg-tsl14-tint has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tsl14-accent has-[:focus-visible]:outline-offset-2 after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+12px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl14-tip after:border after:border-tsl14-line after:text-tsl14-ink after:text-xs after:font-medium after:whitespace-nowrap after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-[250ms] after:z-10 hover:after:opacity-100 hover:after:translate-x-0 has-[:focus-visible]:after:opacity-100 has-[:focus-visible]:after:translate-x-0"><input type="radio" name="tsl14" checked class="absolute inset-0 m-0 opacity-0 cursor-pointer"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-5 h-5 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg><span class="sr-only">Home</span></label>
      <label data-tooltip="Inbox" class="relative z-[1] grid place-items-center w-11 h-11 rounded-xl text-tsl14-mut cursor-pointer transition-colors duration-200 hover:text-tsl14-ink has-checked:text-tsl14-accent has-checked:bg-tsl14-tint has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tsl14-accent has-[:focus-visible]:outline-offset-2 after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+12px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl14-tip after:border after:border-tsl14-line after:text-tsl14-ink after:text-xs after:font-medium after:whitespace-nowrap after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-[250ms] after:z-10 hover:after:opacity-100 hover:after:translate-x-0 has-[:focus-visible]:after:opacity-100 has-[:focus-visible]:after:translate-x-0"><input type="radio" name="tsl14" class="absolute inset-0 m-0 opacity-0 cursor-pointer"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-5 h-5 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M3 13h5l2 3h4l2-3h5M5 5h14l2 8v6H3v-6z"/></svg><span class="sr-only">Inbox</span><i aria-hidden="true" class="absolute top-[9px] right-[9px] w-2 h-2 rounded-full bg-tsl14-alert shadow-[0_0_0_2.5px_var(--color-tsl14-panel)]"></i></label>
      <label data-tooltip="Projects" class="relative z-[1] grid place-items-center w-11 h-11 rounded-xl text-tsl14-mut cursor-pointer transition-colors duration-200 hover:text-tsl14-ink has-checked:text-tsl14-accent has-checked:bg-tsl14-tint has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tsl14-accent has-[:focus-visible]:outline-offset-2 after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+12px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl14-tip after:border after:border-tsl14-line after:text-tsl14-ink after:text-xs after:font-medium after:whitespace-nowrap after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-[250ms] after:z-10 hover:after:opacity-100 hover:after:translate-x-0 has-[:focus-visible]:after:opacity-100 has-[:focus-visible]:after:translate-x-0"><input type="radio" name="tsl14" class="absolute inset-0 m-0 opacity-0 cursor-pointer"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-5 h-5 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span class="sr-only">Projects</span></label>
      <label data-tooltip="Analytics" class="relative z-[1] grid place-items-center w-11 h-11 rounded-xl text-tsl14-mut cursor-pointer transition-colors duration-200 hover:text-tsl14-ink has-checked:text-tsl14-accent has-checked:bg-tsl14-tint has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tsl14-accent has-[:focus-visible]:outline-offset-2 after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+12px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl14-tip after:border after:border-tsl14-line after:text-tsl14-ink after:text-xs after:font-medium after:whitespace-nowrap after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-[250ms] after:z-10 hover:after:opacity-100 hover:after:translate-x-0 has-[:focus-visible]:after:opacity-100 has-[:focus-visible]:after:translate-x-0"><input type="radio" name="tsl14" class="absolute inset-0 m-0 opacity-0 cursor-pointer"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-5 h-5 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M4 20V10m6 10V4m6 16v-7"/></svg><span class="sr-only">Analytics</span></label>
    </nav>
    <span data-tooltip="Ada Kim" class="relative grid place-items-center w-11 h-11 mt-auto rounded-full text-[11.5px] font-bold text-white cursor-pointer bg-[linear-gradient(135deg,var(--color-tsl14-accent),oklch(0.6_0.17_285))] after:content-[attr(data-tooltip)] after:absolute after:left-[calc(100%+12px)] after:top-1/2 after:-translate-y-1/2 after:-translate-x-1 after:px-2.5 after:py-[7px] after:rounded-lg after:bg-tsl14-tip after:border after:border-tsl14-line after:text-tsl14-ink after:text-xs after:font-medium after:whitespace-nowrap after:opacity-0 after:pointer-events-none after:transition-[opacity,translate] after:duration-200 after:delay-[250ms] after:z-10 hover:after:opacity-100 hover:after:translate-x-0">AK</span>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Home</h1>
    <p class="max-w-[46ch] text-sm leading-relaxed text-tsl14-mut text-pretty">Click the rail icons &mdash; the active pill slides between them with CSS anchor positioning. Hover for tooltips.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl14-bg: #121519;
  --color-tsl14-bg: oklch(0.13 0.015 255);
  --color-tsl14-panel: #181b21;
  --color-tsl14-panel: oklch(0.16 0.02 255);
  --color-tsl14-tip: #262a32;
  --color-tsl14-tip: oklch(0.24 0.02 255);
  --color-tsl14-ink: #e9ebef;
  --color-tsl14-ink: oklch(0.93 0.005 255);
  --color-tsl14-mut: #82868f;
  --color-tsl14-mut: oklch(0.58 0.014 255);
  --color-tsl14-line: #373b44;
  --color-tsl14-line: oklch(0.27 0.02 255);
  --color-tsl14-accent: #4fc9e0;
  --color-tsl14-accent: oklch(0.74 0.14 195);
  --color-tsl14-alert: #e7603f;
  --color-tsl14-alert: oklch(0.68 0.21 25);
  --color-tsl14-tint: rgb(79 201 224 / 0.14);
  --color-tsl14-tint: color-mix(in oklab, oklch(0.74 0.14 195) 14%, transparent);
  --color-tsl14-glow: rgb(79 201 224 / 0.6);
  --color-tsl14-glow: color-mix(in oklab, oklch(0.74 0.14 195) 60%, transparent);
  --font-tsl14-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-14 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* Anchor names are identifiers, not design values — no utility mints them,
   and the sliding pill is pure enhancement over the has-checked: tint. */

.tsl-14 nav label:nth-child(1) {
  anchor-name: --tsl14-a1;
}

.tsl-14 nav label:nth-child(2) {
  anchor-name: --tsl14-a2;
}

.tsl-14 nav label:nth-child(3) {
  anchor-name: --tsl14-a3;
}

.tsl-14 nav label:nth-child(4) {
  anchor-name: --tsl14-a4;
}

.tsl-14-pill {
  background: var(--color-tsl14-accent);
  box-shadow: 0 0 10px var(--color-tsl14-glow);
  position-anchor: --tsl14-a1;
  top: calc(anchor(top) + 9px);
  transition: top .3s cubic-bezier(.5,0,.2,1.2);
}

.tsl-14:has(nav label:nth-child(2) input:checked) .tsl-14-pill {
  position-anchor: --tsl14-a2;
}

.tsl-14:has(nav label:nth-child(3) input:checked) .tsl-14-pill {
  position-anchor: --tsl14-a3;
}

.tsl-14:has(nav label:nth-child(4) input:checked) .tsl-14-pill {
  position-anchor: --tsl14-a4;
}

@supports not (anchor-name: --x) {
  .tsl-14-pill {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tsl-14-pill {
    transition: none;
  }
}
```
