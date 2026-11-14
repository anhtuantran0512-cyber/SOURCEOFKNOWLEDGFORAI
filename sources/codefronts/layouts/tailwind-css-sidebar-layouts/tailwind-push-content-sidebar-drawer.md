---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-push-content-sidebar-drawer/"
title: "Tailwind Push-Content Sidebar Drawer with GPU Transitions"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The drawer that pushes instead of covering: opening slides the entire canvas right by exactly the drawer's width, both elements moving as one welded unit."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Push-Content Sidebar Drawer with GPU Transitions
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-push-content-sidebar-drawer/

The drawer that pushes instead of covering: opening slides the entire canvas right by exactly the drawer's width, both elements moving as one welded unit. One shared variable feeds the drawer width and the canvas displacement, so they cannot drift.
## HTML
```html
<section class="tsl-18 relative w-full h-svh min-h-svh overflow-hidden [--w:280px] font-tsl18-sans bg-tsl18-bg text-tsl18-ink">
  <input type="checkbox" id="tsl18-p" class="sr-only peer">
  <aside aria-label="Layers" class="tsl-18-drawer absolute inset-y-0 left-0 z-[2] w-[var(--w)] px-3.5 py-5 bg-tsl18-panel border-r border-tsl18-line -translate-x-full transition-transform duration-[320ms] ease-[cubic-bezier(.4,0,.2,1)] motion-reduce:transition-none">
    <h2 class="px-2.5 pb-3.5 text-xs font-semibold uppercase tracking-[0.08em] text-tsl18-mut">Layers</h2>
    <nav class="flex flex-col gap-0.5">
      <a href="#" aria-current="page" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl18-mut no-underline transition-colors duration-[180ms] hover:text-tsl18-ink hover:bg-tsl18-hover aria-[current=page]:text-tsl18-accent aria-[current=page]:bg-tsl18-tint focus-visible:outline-2 focus-visible:outline-tsl18-accent focus-visible:outline-offset-2">Base map</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl18-mut no-underline transition-colors duration-[180ms] hover:text-tsl18-ink hover:bg-tsl18-hover focus-visible:outline-2 focus-visible:outline-tsl18-accent focus-visible:outline-offset-2">Traffic density</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl18-mut no-underline transition-colors duration-[180ms] hover:text-tsl18-ink hover:bg-tsl18-hover focus-visible:outline-2 focus-visible:outline-tsl18-accent focus-visible:outline-offset-2">Transit lines</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl18-mut no-underline transition-colors duration-[180ms] hover:text-tsl18-ink hover:bg-tsl18-hover focus-visible:outline-2 focus-visible:outline-tsl18-accent focus-visible:outline-offset-2">Bike network</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[10px] text-sm font-medium text-tsl18-mut no-underline transition-colors duration-[180ms] hover:text-tsl18-ink hover:bg-tsl18-hover focus-visible:outline-2 focus-visible:outline-tsl18-accent focus-visible:outline-offset-2">3D buildings</a>
    </nav>
  </aside>
  <div class="tsl-18-canvas h-full grid grid-rows-[auto_1fr] translate-x-0 transition-transform duration-[320ms] ease-[cubic-bezier(.4,0,.2,1)] motion-reduce:transition-none">
    <header class="flex items-center gap-3.5 h-[54px] px-4 bg-tsl18-panel border-b border-tsl18-line text-[15px] font-semibold">
      <label for="tsl18-p" class="inline-flex items-center gap-2 min-h-11 px-3.5 -ml-1 rounded-[10px] border border-tsl18-line text-[13px] font-medium text-tsl18-ink cursor-pointer transition-colors duration-200 hover:bg-tsl18-hover"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-current stroke-[1.9] [stroke-linecap:round]"><path d="M4 6h16M4 12h16M4 18h16"/></svg><span>Layers</span></label>
      <strong>Metroview</strong>
    </header>
    <main class="grid place-items-center bg-[repeating-linear-gradient(0deg,transparent_0_39px,oklch(0.2_0.014_220)_39px_40px),repeating-linear-gradient(90deg,transparent_0_39px,oklch(0.2_0.014_220)_39px_40px),oklch(0.16_0.012_220)]">
      <p class="max-w-[40ch] px-6 text-center text-sm leading-relaxed text-tsl18-mut text-pretty">Open Layers &mdash; the whole canvas slides right by exactly 280px (one shared variable), never squeezing. Both moves are GPU transforms.</p>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl18-bg: #101619;
  --color-tsl18-bg: oklch(0.14 0.012 220);
  --color-tsl18-panel: #161f24;
  --color-tsl18-panel: oklch(0.18 0.015 220);
  --color-tsl18-ink: #e8eef1;
  --color-tsl18-ink: oklch(0.94 0.005 220);
  --color-tsl18-mut: #929da3;
  --color-tsl18-mut: oklch(0.64 0.012 220);
  --color-tsl18-line: #343f45;
  --color-tsl18-line: oklch(0.29 0.016 220);
  --color-tsl18-accent: #57c2e0;
  --color-tsl18-accent: oklch(0.75 0.13 220);
  --color-tsl18-hover: rgb(232 238 241 / 0.06);
  --color-tsl18-hover: color-mix(in oklab, oklch(0.94 0.005 220) 6%, transparent);
  --color-tsl18-tint: rgb(87 194 224 / 0.14);
  --color-tsl18-tint: color-mix(in oklab, oklch(0.75 0.13 220) 14%, transparent);
  --font-tsl18-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-18 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* STATE — drawer and canvas move by the SAME variable, in the same frame. */

#tsl18-p:checked ~ .tsl-18-drawer {
  translate: 0;
}

#tsl18-p:checked ~ .tsl-18-canvas {
  translate: var(--w) 0;
}

#tsl18-p:focus-visible ~ .tsl-18-canvas label[for="tsl18-p"] {
  outline: 2px solid var(--color-tsl18-accent);
  outline-offset: 2px;
}
```
