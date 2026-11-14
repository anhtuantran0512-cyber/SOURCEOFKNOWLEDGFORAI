---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sidebar-sticky-search-bar-rail/"
title: "Tailwind Sidebar with Sticky Search Bar Inside the Rail"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The command-centre rail: a search field pinned above a long scrolling menu &mdash; sticky inside the sidebar's own scroll context, not the page's &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar with Sticky Search Bar Inside the Rail
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-sidebar-sticky-search-bar-rail/

The command-centre rail: a search field pinned above a long scrolling menu &mdash; sticky inside the sidebar's own scroll context, not the page's &mdash; with a &#8984;K keycap chip and focus-within ring-lighting the entire field when the input takes focus.
## HTML
```html
<section class="tsl-21 w-full h-svh min-h-svh grid grid-cols-[264px_1fr] font-tsl21-sans bg-tsl21-bg text-tsl21-ink">
  <aside aria-label="Channels" class="bg-tsl21-panel border-r border-tsl21-line overflow-y-auto overscroll-contain">
    <div class="sticky top-0 z-[2] px-3 pt-3.5 pb-2.5 bg-tsl21-panel border-b border-tsl21-line">
      <label class="grid grid-cols-[auto_1fr_auto] items-center gap-2.5 h-11 px-3 rounded-[11px] border border-tsl21-line bg-tsl21-field transition-[border-color,box-shadow] duration-200 focus-within:border-tsl21-accent focus-within:shadow-[0_0_0_3px_var(--color-tsl21-ring)] motion-reduce:transition-none">
        <svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tsl21-mut stroke-2 [stroke-linecap:round]"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input type="search" placeholder="Jump to&hellip;" aria-label="Search channels" class="min-w-0 border-0 bg-transparent text-tsl21-ink text-[13.5px] outline-none placeholder:text-tsl21-placeholder">
        <kbd class="font-tsl21-mono text-[10.5px] font-semibold px-[5px] py-[3px] rounded-[5px] border border-tsl21-line bg-tsl21-chip text-tsl21-mut">&#8984;K</kbd>
      </label>
    </div>
    <nav class="flex flex-col gap-px px-3 pt-2.5 pb-4">
      <a href="#" aria-current="page" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover aria-[current=page]:text-tsl21-ink aria-[current=page]:bg-tsl21-tint focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># general</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># announcements</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># engineering</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># design-systems</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># frontend-guild</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># css-wizardry</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># accessibility</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># performance</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># releases</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># random</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># watercooler</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl21-mut no-underline transition-colors duration-150 hover:text-tsl21-ink hover:bg-tsl21-hover focus-visible:outline-2 focus-visible:outline-tsl21-accent focus-visible:outline-offset-1"># reading-club</a>
    </nav>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5"># general</h1>
    <p class="max-w-[47ch] text-sm leading-relaxed text-tsl21-mut text-pretty">Scroll the channel list &mdash; the search stays pinned inside the rail's own scroll context, and channels slide beneath it.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl21-bg: #161219;
  --color-tsl21-bg: oklch(0.13 0.015 310);
  --color-tsl21-panel: #1e1822;
  --color-tsl21-panel: oklch(0.17 0.02 310);
  --color-tsl21-field: #181320;
  --color-tsl21-field: oklch(0.14 0.016 310);
  --color-tsl21-chip: rgb(239 234 243 / 0.08);
  --color-tsl21-chip: color-mix(in oklab, oklch(0.94 0.005 310) 8%, transparent);
  --color-tsl21-ink: #efeaf3;
  --color-tsl21-ink: oklch(0.94 0.005 310);
  --color-tsl21-mut: #a0949f;
  --color-tsl21-mut: oklch(0.64 0.014 310);
  --color-tsl21-placeholder: #857a86;
  --color-tsl21-placeholder: oklch(0.56 0.014 310);
  --color-tsl21-line: #3b3441;
  --color-tsl21-line: oklch(0.28 0.02 310);
  --color-tsl21-accent: #c07ae0;
  --color-tsl21-accent: oklch(0.72 0.15 310);
  --color-tsl21-ring: rgb(192 122 224 / 0.22);
  --color-tsl21-ring: color-mix(in oklab, oklch(0.72 0.15 310) 22%, transparent);
  --color-tsl21-hover: rgb(239 234 243 / 0.06);
  --color-tsl21-hover: color-mix(in oklab, oklch(0.94 0.005 310) 6%, transparent);
  --color-tsl21-tint: rgb(192 122 224 / 0.16);
  --color-tsl21-tint: color-mix(in oklab, oklch(0.72 0.15 310) 16%, transparent);
  --font-tsl21-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl21-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-21 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
