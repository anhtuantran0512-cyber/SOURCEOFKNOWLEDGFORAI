---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-resizable-sidebar-css-resize-property/"
title: "Tailwind Resizable Sidebar Layout Using the CSS Resize Property"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "Drag-to-resize with no pointer listeners, no drag maths: resize-x plus overflow-auto and a min/max fence, and the browser runs the entire interaction."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Resizable Sidebar Layout Using the CSS Resize Property
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-resizable-sidebar-css-resize-property/

Drag-to-resize with no pointer listeners, no drag maths: resize-x plus overflow-auto and a min/max fence, and the browser runs the entire interaction. Tailwind ships the resize utility, so the whole mechanism is three classes.
## HTML
```html
<section class="tsl-27 w-full h-svh min-h-svh flex font-tsl27-sans bg-tsl27-bg text-tsl27-ink">
  <aside aria-label="Notes" class="relative flex-none w-[280px] min-w-[200px] max-w-[440px] resize-x overflow-auto bg-tsl27-panel border-r border-tsl27-line">
    <div class="min-w-[186px] px-3.5 py-5">
      <h2 class="px-2.5 pb-3.5 text-[14.5px] font-bold tracking-tight">Notebook</h2>
      <nav class="flex flex-col gap-0.5">
        <a href="#" aria-current="page" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium leading-snug truncate text-tsl27-mut no-underline transition-colors duration-150 hover:text-tsl27-ink hover:bg-tsl27-hover aria-[current=page]:text-tsl27-accent aria-[current=page]:bg-tsl27-tint focus-visible:outline-2 focus-visible:outline-tsl27-accent focus-visible:outline-offset-1">Container queries field guide</a>
        <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium leading-snug truncate text-tsl27-mut no-underline transition-colors duration-150 hover:text-tsl27-ink hover:bg-tsl27-hover focus-visible:outline-2 focus-visible:outline-tsl27-accent focus-visible:outline-offset-1">Subgrid recipes</a>
        <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium leading-snug truncate text-tsl27-mut no-underline transition-colors duration-150 hover:text-tsl27-ink hover:bg-tsl27-hover focus-visible:outline-2 focus-visible:outline-tsl27-accent focus-visible:outline-offset-1">The :has() cookbook</a>
        <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium leading-snug truncate text-tsl27-mut no-underline transition-colors duration-150 hover:text-tsl27-ink hover:bg-tsl27-hover focus-visible:outline-2 focus-visible:outline-tsl27-accent focus-visible:outline-offset-1">Anchor positioning notes</a>
        <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium leading-snug truncate text-tsl27-mut no-underline transition-colors duration-150 hover:text-tsl27-ink hover:bg-tsl27-hover focus-visible:outline-2 focus-visible:outline-tsl27-accent focus-visible:outline-offset-1">View transitions research</a>
      </nav>
    </div>
    <span aria-hidden="true" class="absolute inset-y-0 right-0 w-3.5 pointer-coarse:w-[22px] flex flex-col items-center justify-center gap-[3px] cursor-col-resize opacity-50 transition-opacity duration-200 hover:opacity-100 motion-reduce:transition-none">
      <i class="w-[3px] h-[3px] rounded-full bg-tsl27-mut"></i><i class="w-[3px] h-[3px] rounded-full bg-tsl27-mut"></i><i class="w-[3px] h-[3px] rounded-full bg-tsl27-mut"></i>
    </span>
  </aside>
  <main class="flex-1 min-w-0 p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Container queries field guide</h1>
    <p class="max-w-[54ch] text-sm leading-[1.65] text-tsl27-mut text-pretty">Drag the sidebar's bottom-right corner (or along the dotted grip) &mdash; <code class="font-tsl27-mono text-[12.5px]">resize-x</code> plus a min/max fence, zero drag JavaScript. The pane you are reading reflows live.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl27-bg: #141310;
  --color-tsl27-bg: oklch(0.13 0.012 85);
  --color-tsl27-panel: #1c1a15;
  --color-tsl27-panel: oklch(0.17 0.014 85);
  --color-tsl27-ink: #efece4;
  --color-tsl27-ink: oklch(0.94 0.006 85);
  --color-tsl27-mut: #a5a08f;
  --color-tsl27-mut: oklch(0.66 0.015 85);
  --color-tsl27-line: #3c382d;
  --color-tsl27-line: oklch(0.29 0.018 85);
  --color-tsl27-accent: #e2c559;
  --color-tsl27-accent: oklch(0.8 0.13 90);
  --color-tsl27-hover: rgb(239 236 228 / 0.06);
  --color-tsl27-hover: color-mix(in oklab, oklch(0.94 0.006 85) 6%, transparent);
  --color-tsl27-tint: rgb(226 197 89 / 0.13);
  --color-tsl27-tint: color-mix(in oklab, oklch(0.8 0.13 90) 13%, transparent);
  --font-tsl27-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl27-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-27 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
