---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-fixed-sidebar-independently-scrolling-content/"
title: "Tailwind Fixed Sidebar Layout with Independently Scrolling Content"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The foundational app shell every dashboard starts from &mdash; locked rail, independently scrolling main pane &mdash; built as a height-constrained grid…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Fixed Sidebar Layout with Independently Scrolling Content
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-fixed-sidebar-independently-scrolling-content/

The foundational app shell every dashboard starts from &mdash; locked rail, independently scrolling main pane &mdash; built as a height-constrained grid rather than position:fixed plus a magic margin. Each pane owns its overflow, so nothing overlaps and the whole thing nests inside any container.
## HTML
```html
<section class="tsl-09 w-full h-svh min-h-svh grid grid-cols-[260px_1fr] font-tsl09-sans bg-tsl09-bg text-tsl09-ink">
  <aside aria-label="Workspace" class="flex flex-col bg-tsl09-panel border-r border-tsl09-line px-3 py-5 overflow-y-auto overscroll-contain [scrollbar-width:thin] [scrollbar-color:var(--color-tsl09-line)_transparent]">
    <div class="flex items-center gap-2.5 px-2.5 pt-0.5 pb-[18px] text-[15px] font-bold tracking-tight"><span aria-hidden="true" class="w-6 h-6 rounded-[7px] bg-[conic-gradient(from_45deg,var(--color-tsl09-accent),oklch(0.6_0.15_260))]"></span>Ledgerly</div>
    <nav class="flex flex-col gap-0.5">
      <a href="#" aria-current="page" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover aria-[current=page]:text-tsl09-accent aria-[current=page]:bg-tsl09-tint focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Overview</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Transactions</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Invoices</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Recurring</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Vendors</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Categories</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Receipts</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Tax reports</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Bank feeds</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Rules</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Integrations</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Team</a>
      <a href="#" class="flex items-center min-h-11 px-3.5 rounded-[9px] text-[13.5px] font-medium text-tsl09-mut no-underline transition-colors duration-[180ms] hover:text-tsl09-ink hover:bg-tsl09-hover focus-visible:outline-2 focus-visible:outline-tsl09-accent focus-visible:outline-offset-2">Settings</a>
    </nav>
  </aside>
  <main class="p-8 overflow-y-auto overscroll-contain [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Overview</h1>
    <p class="max-w-[52ch] mb-6 text-sm leading-relaxed text-tsl09-mut text-pretty">Both panes scroll independently. The sidebar nav is intentionally long &mdash; scroll it, then scroll this pane; neither moves the other.</p>
    <div class="grid gap-4">
      <div class="h-[130px] rounded-2xl bg-tsl09-panel border border-tsl09-line"></div>
      <div class="h-[130px] rounded-2xl bg-tsl09-panel border border-tsl09-line"></div>
      <div class="h-[130px] rounded-2xl bg-tsl09-panel border border-tsl09-line"></div>
      <div class="h-[130px] rounded-2xl bg-tsl09-panel border border-tsl09-line"></div>
      <div class="h-[130px] rounded-2xl bg-tsl09-panel border border-tsl09-line"></div>
      <div class="h-[130px] rounded-2xl bg-tsl09-panel border border-tsl09-line"></div>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl09-bg: #111518;
  --color-tsl09-bg: oklch(0.13 0.012 235);
  --color-tsl09-panel: #191d21;
  --color-tsl09-panel: oklch(0.17 0.015 235);
  --color-tsl09-ink: #e9ebed;
  --color-tsl09-ink: oklch(0.93 0.005 235);
  --color-tsl09-mut: #90959b;
  --color-tsl09-mut: oklch(0.63 0.012 235);
  --color-tsl09-line: #383d42;
  --color-tsl09-line: oklch(0.28 0.015 235);
  --color-tsl09-accent: #5cc4dd;
  --color-tsl09-accent: oklch(0.72 0.13 210);
  --color-tsl09-hover: rgb(233 235 237 / 0.06);
  --color-tsl09-hover: color-mix(in oklab, oklch(0.93 0.005 235) 6%, transparent);
  --color-tsl09-tint: rgb(92 196 221 / 0.17);
  --color-tsl09-tint: color-mix(in oklab, oklch(0.72 0.13 210) 17%, transparent);
  --font-tsl09-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-09 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
