---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-right-aligned-sidebar-inspector-panel/"
title: "Tailwind Right-Aligned Sidebar Layout for Inspector Panels"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The design-tool inspector: a right-hand properties panel tuned for its real job &mdash; dense labelled controls, hairline dividers, and logical-property…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Right-Aligned Sidebar Layout for Inspector Panels
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-right-aligned-sidebar-inspector-panel/

The design-tool inspector: a right-hand properties panel tuned for its real job &mdash; dense labelled controls, hairline dividers, and logical-property borders so an RTL locale flips the whole layout for free. The canvas stays first in the DOM, which is what screen readers and the tab order want.
## HTML
```html
<section class="tsl-11 w-full h-svh min-h-svh grid grid-cols-[1fr_300px] font-tsl11-sans bg-tsl11-bg text-tsl11-ink">
  <main aria-label="Canvas" class="grid place-items-center overflow-auto bg-[radial-gradient(var(--color-tsl11-grid)_1px,transparent_1px)] bg-[length:22px_22px]">
    <div class="grid gap-2.5 justify-items-center font-tsl11-mono text-xs font-medium text-tsl11-mut">
      <div aria-hidden="true" class="w-[320px] h-[180px] rounded-2xl bg-[linear-gradient(135deg,oklch(0.62_0.17_285),oklch(0.55_0.19_320))] outline outline-[1.5px] outline-tsl11-accent outline-offset-4"></div>
      <span>hero-card</span>
    </div>
  </main>
  <aside aria-label="Properties" class="border-s border-tsl11-line bg-tsl11-panel overflow-y-auto px-4 py-[18px] [scrollbar-gutter:stable]">
    <h2 class="pb-4 border-b border-tsl11-line text-sm font-semibold">Design</h2>
    <div class="grid gap-2.5 py-4 border-b border-tsl11-line">
      <h3 class="text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl11-mut">Layout</h3>
      <div class="grid grid-cols-[auto_1fr_auto_1fr] items-center gap-2">
        <label for="tsl11-w" class="text-[11.5px] font-medium text-tsl11-mut">W</label><input id="tsl11-w" type="number" value="320" class="min-w-0 w-full min-h-9 px-2.5 rounded-lg border border-tsl11-line bg-tsl11-field text-tsl11-ink font-tsl11-mono text-[12.5px] font-medium tabular-nums focus-visible:outline-2 focus-visible:outline-tsl11-accent focus-visible:outline-offset-1">
        <label for="tsl11-h" class="text-[11.5px] font-medium text-tsl11-mut">H</label><input id="tsl11-h" type="number" value="180" class="min-w-0 w-full min-h-9 px-2.5 rounded-lg border border-tsl11-line bg-tsl11-field text-tsl11-ink font-tsl11-mono text-[12.5px] font-medium tabular-nums focus-visible:outline-2 focus-visible:outline-tsl11-accent focus-visible:outline-offset-1">
      </div>
      <div class="grid grid-cols-[auto_1fr_auto_1fr] items-center gap-2">
        <label for="tsl11-x" class="text-[11.5px] font-medium text-tsl11-mut">X</label><input id="tsl11-x" type="number" value="64" class="min-w-0 w-full min-h-9 px-2.5 rounded-lg border border-tsl11-line bg-tsl11-field text-tsl11-ink font-tsl11-mono text-[12.5px] font-medium tabular-nums focus-visible:outline-2 focus-visible:outline-tsl11-accent focus-visible:outline-offset-1">
        <label for="tsl11-y" class="text-[11.5px] font-medium text-tsl11-mut">Y</label><input id="tsl11-y" type="number" value="42" class="min-w-0 w-full min-h-9 px-2.5 rounded-lg border border-tsl11-line bg-tsl11-field text-tsl11-ink font-tsl11-mono text-[12.5px] font-medium tabular-nums focus-visible:outline-2 focus-visible:outline-tsl11-accent focus-visible:outline-offset-1">
      </div>
    </div>
    <div class="grid gap-2.5 py-4 border-b border-tsl11-line">
      <h3 class="text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl11-mut">Appearance</h3>
      <div class="grid grid-cols-[auto_1fr_auto_1fr] items-center gap-2">
        <label for="tsl11-r" class="text-[11.5px] font-medium text-tsl11-mut">Radius</label><input id="tsl11-r" type="number" value="16" class="min-w-0 w-full min-h-9 px-2.5 rounded-lg border border-tsl11-line bg-tsl11-field text-tsl11-ink font-tsl11-mono text-[12.5px] font-medium tabular-nums focus-visible:outline-2 focus-visible:outline-tsl11-accent focus-visible:outline-offset-1">
        <label for="tsl11-o" class="text-[11.5px] font-medium text-tsl11-mut">Opacity</label><input id="tsl11-o" type="number" value="100" class="min-w-0 w-full min-h-9 px-2.5 rounded-lg border border-tsl11-line bg-tsl11-field text-tsl11-ink font-tsl11-mono text-[12.5px] font-medium tabular-nums focus-visible:outline-2 focus-visible:outline-tsl11-accent focus-visible:outline-offset-1">
      </div>
      <div class="grid grid-cols-[auto_auto_1fr] items-center gap-2">
        <label for="tsl11-f" class="text-[11.5px] font-medium text-tsl11-mut">Fill</label>
        <input id="tsl11-f" type="color" value="#7c6ff0" class="w-11 h-11 p-0.5 rounded-lg border border-tsl11-line bg-transparent cursor-pointer focus-visible:outline-2 focus-visible:outline-tsl11-accent focus-visible:outline-offset-1">
        <code class="font-tsl11-mono text-xs font-medium text-tsl11-mut">#7C6FF0</code>
      </div>
    </div>
    <div class="grid gap-2.5 py-4">
      <h3 class="text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl11-mut">Export</h3>
      <button type="button" class="min-h-11 px-3 rounded-[9px] border border-tsl11-accentline bg-tsl11-accenttint text-tsl11-ink text-[12.5px] font-semibold cursor-pointer transition-colors duration-200 hover:bg-tsl11-accenthover focus-visible:outline-2 focus-visible:outline-tsl11-accent focus-visible:outline-offset-1">Export PNG &middot;2x</button>
    </div>
  </aside>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl11-bg: #16171c;
  --color-tsl11-bg: oklch(0.15 0.01 280);
  --color-tsl11-panel: #1d1e25;
  --color-tsl11-panel: oklch(0.19 0.012 280);
  --color-tsl11-field: #18191f;
  --color-tsl11-field: oklch(0.16 0.01 280);
  --color-tsl11-grid: #222430;
  --color-tsl11-grid: oklch(0.22 0.012 280);
  --color-tsl11-ink: #e9e9ef;
  --color-tsl11-ink: oklch(0.93 0.005 280);
  --color-tsl11-mut: #8b8b99;
  --color-tsl11-mut: oklch(0.6 0.012 280);
  --color-tsl11-line: #393a46;
  --color-tsl11-line: oklch(0.29 0.015 280);
  --color-tsl11-accent: #8b74e8;
  --color-tsl11-accent: oklch(0.66 0.17 285);
  --color-tsl11-accentline: rgb(139 116 232 / 0.5);
  --color-tsl11-accentline: color-mix(in oklab, oklch(0.66 0.17 285) 50%, transparent);
  --color-tsl11-accenttint: rgb(139 116 232 / 0.16);
  --color-tsl11-accenttint: color-mix(in oklab, oklch(0.66 0.17 285) 16%, transparent);
  --color-tsl11-accenthover: rgb(139 116 232 / 0.26);
  --color-tsl11-accenthover: color-mix(in oklab, oklch(0.66 0.17 285) 26%, transparent);
  --font-tsl11-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl11-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-11 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
