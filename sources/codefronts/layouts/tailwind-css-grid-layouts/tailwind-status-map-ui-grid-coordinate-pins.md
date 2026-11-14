---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-status-map-ui-grid-coordinate-pins/"
title: "Tailwind Status Map UI with Grid Coordinate Pins"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A network status map for an ops console: a graticule and aurora drawn entirely with gradients, edge nodes placed on grid CELLS — [grid-area:3/9] is a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Status Map UI with Grid Coordinate Pins
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-status-map-ui-grid-coordinate-pins/

A network status map for an ops console: a graticule and aurora drawn entirely with gradients, edge nodes placed on grid CELLS — [grid-area:3/9] is a coordinate you can diff in review — and latency tooltips on hover or focus.
## HTML
```html
<section class="tgx-28 w-full min-h-svh bg-tgx28-page font-tgx28-sans p-6 grid content-center gap-3">
  <header class="flex items-end justify-between gap-4 flex-wrap">
    <div class="flex flex-col gap-1">
      <p class="font-tgx28-mono text-[0.66rem] tracking-[0.16em] uppercase text-tgx28-legend">Vantage · Edge network</p>
      <h2 class="text-[1.25rem] font-semibold text-white tracking-[-0.01em]">14 regions, 1 degraded</h2>
    </div>
    <div class="flex items-center gap-2 text-[0.72rem] text-tgx28-legend">
      <span class="inline-flex items-center gap-1.5 rounded-full border border-tgx28-aura/30 px-2.5 py-1"><span class="size-1.5 rounded-full bg-tgx28-aura"></span>Healthy</span>
      <span class="inline-flex items-center gap-1.5 rounded-full border border-tgx28-alert/40 px-2.5 py-1"><span class="size-1.5 rounded-full bg-tgx28-alert"></span>Degraded</span>
    </div>
  </header>
  <div class="relative grid grid-cols-12 grid-rows-8 aspect-[12/7] rounded-2xl border border-tgx28-aura/30 overflow-hidden bg-tgx28-plane bg-[image:repeating-linear-gradient(90deg,oklch(0.6_0.1_200/0.1)_0_1px,transparent_1px_calc(100%/12)),repeating-linear-gradient(0deg,oklch(0.6_0.1_200/0.1)_0_1px,transparent_1px_calc(100%/8)),radial-gradient(70%_90%_at_20%_15%,color-mix(in_oklab,var(--color-tgx28-aura)_45%,transparent),transparent_60%),radial-gradient(60%_80%_at_85%_75%,color-mix(in_oklab,var(--color-tgx28-aurb)_40%,transparent),transparent_60%)] [background-blend-mode:normal,normal,screen,screen]">
    <button type="button" class="group relative [grid-area:3/9] place-self-center grid place-items-center min-w-11 min-h-11 bg-transparent border-0 cursor-pointer rounded-lg focus-visible:outline-2 focus-visible:outline-tgx28-aura focus-visible:outline-offset-2">
      <i class="relative block size-3 rounded-full bg-tgx28-aura shadow-[0_0_12px_var(--color-tgx28-aura)] after:content-[''] after:absolute after:-inset-1 after:rounded-full after:border-[1.5px] after:border-tgx28-aura after:animate-tgx28-ping motion-reduce:after:animate-none motion-reduce:after:opacity-0"></i>
      <span class="absolute bottom-full mb-1 text-[0.66rem] whitespace-nowrap text-tgx28-label bg-tgx28-tip border border-tgx28-aura/40 rounded-md px-2 py-1 opacity-0 translate-y-1 transition duration-200 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Reykjavík · <span class="tabular-nums">42ms</span></span>
    </button>
    <button type="button" class="group relative [grid-area:5/3] place-self-center grid place-items-center min-w-11 min-h-11 bg-transparent border-0 cursor-pointer rounded-lg focus-visible:outline-2 focus-visible:outline-tgx28-aura focus-visible:outline-offset-2">
      <i class="relative block size-3 rounded-full bg-tgx28-aura shadow-[0_0_12px_var(--color-tgx28-aura)] after:content-[''] after:absolute after:-inset-1 after:rounded-full after:border-[1.5px] after:border-tgx28-aura after:animate-tgx28-ping motion-reduce:after:animate-none motion-reduce:after:opacity-0"></i>
      <span class="absolute bottom-full mb-1 text-[0.66rem] whitespace-nowrap text-tgx28-label bg-tgx28-tip border border-tgx28-aura/40 rounded-md px-2 py-1 opacity-0 translate-y-1 transition duration-200 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Denver · <span class="tabular-nums">18ms</span></span>
    </button>
    <button type="button" class="group relative [grid-area:6/11] place-self-center grid place-items-center min-w-11 min-h-11 bg-transparent border-0 cursor-pointer rounded-lg focus-visible:outline-2 focus-visible:outline-tgx28-alert focus-visible:outline-offset-2">
      <i class="relative block size-3 rounded-full bg-tgx28-alert shadow-[0_0_12px_var(--color-tgx28-alert)] after:content-[''] after:absolute after:-inset-1 after:rounded-full after:border-[1.5px] after:border-tgx28-alert after:animate-tgx28-ping motion-reduce:after:animate-none motion-reduce:after:opacity-0"></i>
      <span class="absolute bottom-full mb-1 text-[0.66rem] whitespace-nowrap text-tgx28-label bg-tgx28-tip border border-tgx28-alert/50 rounded-md px-2 py-1 opacity-0 translate-y-1 transition duration-200 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Sydney · packet loss 4.1%</span>
    </button>
    <button type="button" class="group relative [grid-area:4/6] place-self-center grid place-items-center min-w-11 min-h-11 bg-transparent border-0 cursor-pointer rounded-lg focus-visible:outline-2 focus-visible:outline-tgx28-aura focus-visible:outline-offset-2">
      <i class="relative block size-3 rounded-full bg-tgx28-aura shadow-[0_0_12px_var(--color-tgx28-aura)] after:content-[''] after:absolute after:-inset-1 after:rounded-full after:border-[1.5px] after:border-tgx28-aura after:animate-tgx28-ping motion-reduce:after:animate-none motion-reduce:after:opacity-0"></i>
      <span class="absolute bottom-full mb-1 text-[0.66rem] whitespace-nowrap text-tgx28-label bg-tgx28-tip border border-tgx28-aura/40 rounded-md px-2 py-1 opacity-0 translate-y-1 transition duration-200 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Azores buoy · <span class="tabular-nums">61ms</span></span>
    </button>
    <button type="button" class="group relative [grid-area:2/5] place-self-center grid place-items-center min-w-11 min-h-11 bg-transparent border-0 cursor-pointer rounded-lg focus-visible:outline-2 focus-visible:outline-tgx28-aura focus-visible:outline-offset-2">
      <i class="relative block size-3 rounded-full bg-tgx28-aura shadow-[0_0_12px_var(--color-tgx28-aura)] after:content-[''] after:absolute after:-inset-1 after:rounded-full after:border-[1.5px] after:border-tgx28-aura after:animate-tgx28-ping motion-reduce:after:animate-none motion-reduce:after:opacity-0"></i>
      <span class="absolute bottom-full mb-1 text-[0.66rem] whitespace-nowrap text-tgx28-label bg-tgx28-tip border border-tgx28-aura/40 rounded-md px-2 py-1 opacity-0 translate-y-1 transition duration-200 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Anchorage · <span class="tabular-nums">77ms</span></span>
    </button>
    <p class="absolute bottom-2 left-3 font-tgx28-mono text-[0.6rem] tracking-[0.06em] text-tgx28-legend">pins are grid coordinates — [grid-area: row / column]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx28-page: #101724;
  --color-tgx28-page: oklch(0.16 0.02 240);
  --color-tgx28-plane: #131a26;
  --color-tgx28-plane: oklch(0.16 0.03 240);
  --color-tgx28-aura: #63d5da;
  --color-tgx28-aura: oklch(0.8 0.11 190);
  --color-tgx28-aurb: #7b63cf;
  --color-tgx28-aurb: oklch(0.55 0.16 300);
  --color-tgx28-alert: #f08a6c;
  --color-tgx28-alert: oklch(0.75 0.16 35);
  --color-tgx28-tip: #17202e;
  --color-tgx28-tip: oklch(0.21 0.03 240);
  --color-tgx28-label: #e8f5f6;
  --color-tgx28-label: oklch(0.96 0.02 200);
  --color-tgx28-legend: #a9c4c8;
  --color-tgx28-legend: oklch(0.79 0.03 200);
  --font-tgx28-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx28-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tgx28-ping: tgx28-ping 2.2s ease-out infinite;
}

@keyframes tgx28-ping {
  75%,
    100% {
    scale: 2.4;
    opacity: 0;
  }
}

.tgx-28 {
  width: 100%;
  min-height: 100svh;
}
```
