---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-multi-level-nested-tree-sidebar-details/"
title: "Tailwind Multi-Level Nested Tree Sidebar with Details Branches"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "A file-explorer-grade tree: three levels of nested <details>, rotating chevrons, indent guides drawn as logical borders, and progressive padding from one…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Multi-Level Nested Tree Sidebar with Details Branches
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-multi-level-nested-tree-sidebar-details/

A file-explorer-grade tree: three levels of nested <details>, rotating chevrons, indent guides drawn as logical borders, and progressive padding from one --indent variable. Keyboard-operable out of the box because disclosure is native.
## HTML
```html
<section class="tsl-24 w-full h-svh min-h-svh grid grid-cols-[264px_1fr] font-tsl24-sans bg-tsl24-bg text-tsl24-ink">
  <aside aria-label="Project files" class="bg-tsl24-panel border-r border-tsl24-line px-2.5 py-4 overflow-y-auto font-tsl24-mono [scrollbar-gutter:stable]">
    <h2 class="px-3 pt-0.5 pb-3 text-[10.5px] font-semibold uppercase tracking-[0.12em] text-tsl24-mut">explorer</h2>
    <details open class="group">
      <summary class="flex items-center gap-[7px] min-h-9 px-2.5 ps-[calc(0.625rem+var(--indent,0)*1.125rem)] rounded-lg text-[13px] font-medium text-tsl24-ink cursor-pointer list-none transition-colors duration-150 hover:bg-tsl24-hover [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-tsl24-mut stroke-2 [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-open:rotate-90 motion-reduce:transition-none"><path d="m9 6 6 6-6 6"/></svg>src</summary>
      <div class="[--indent:1] flex flex-col border-s border-tsl24-line ms-[calc(1rem+(var(--indent)-1)*1.125rem)]">
        <details open class="group/b2">
          <summary class="flex items-center gap-[7px] min-h-9 ps-3 pe-2.5 rounded-lg text-[13px] font-medium text-tsl24-ink cursor-pointer list-none transition-colors duration-150 hover:bg-tsl24-hover [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-tsl24-mut stroke-2 [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-open/b2:rotate-90 motion-reduce:transition-none"><path d="m9 6 6 6-6 6"/></svg>components</summary>
          <div class="[--indent:2] flex flex-col border-s border-tsl24-line ms-[calc(1rem+(var(--indent)-1)*1.125rem)]">
            <a href="#" aria-current="page" class="flex items-center gap-[7px] min-h-9 ps-3 pe-2.5 rounded-lg text-[13px] text-tsl24-mut no-underline transition-colors duration-150 hover:text-tsl24-ink hover:bg-tsl24-hover aria-[current=page]:text-tsl24-accent aria-[current=page]:bg-tsl24-tint focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-current stroke-[1.7] [stroke-linejoin:round]"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>Sidebar.css</a>
            <a href="#" class="flex items-center gap-[7px] min-h-9 ps-3 pe-2.5 rounded-lg text-[13px] text-tsl24-mut no-underline transition-colors duration-150 hover:text-tsl24-ink hover:bg-tsl24-hover focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-current stroke-[1.7] [stroke-linejoin:round]"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>Sidebar.html</a>
          </div>
        </details>
        <details class="group/b3">
          <summary class="flex items-center gap-[7px] min-h-9 ps-3 pe-2.5 rounded-lg text-[13px] font-medium text-tsl24-ink cursor-pointer list-none transition-colors duration-150 hover:bg-tsl24-hover [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-tsl24-mut stroke-2 [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-open/b3:rotate-90 motion-reduce:transition-none"><path d="m9 6 6 6-6 6"/></svg>tokens</summary>
          <div class="[--indent:2] flex flex-col border-s border-tsl24-line ms-[calc(1rem+(var(--indent)-1)*1.125rem)]">
            <a href="#" class="flex items-center gap-[7px] min-h-9 ps-3 pe-2.5 rounded-lg text-[13px] text-tsl24-mut no-underline transition-colors duration-150 hover:text-tsl24-ink hover:bg-tsl24-hover focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-current stroke-[1.7] [stroke-linejoin:round]"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>colors.css</a>
            <a href="#" class="flex items-center gap-[7px] min-h-9 ps-3 pe-2.5 rounded-lg text-[13px] text-tsl24-mut no-underline transition-colors duration-150 hover:text-tsl24-ink hover:bg-tsl24-hover focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-current stroke-[1.7] [stroke-linejoin:round]"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>spacing.css</a>
          </div>
        </details>
        <a href="#" class="flex items-center gap-[7px] min-h-9 ps-3 pe-2.5 rounded-lg text-[13px] text-tsl24-mut no-underline transition-colors duration-150 hover:text-tsl24-ink hover:bg-tsl24-hover focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-current stroke-[1.7] [stroke-linejoin:round]"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>index.html</a>
      </div>
    </details>
    <details class="group/b4">
      <summary class="flex items-center gap-[7px] min-h-9 px-2.5 rounded-lg text-[13px] font-medium text-tsl24-ink cursor-pointer list-none transition-colors duration-150 hover:bg-tsl24-hover [&amp;::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-tsl24-mut stroke-2 [stroke-linecap:round] [stroke-linejoin:round] transition-[rotate] duration-200 group-open/b4:rotate-90 motion-reduce:transition-none"><path d="m9 6 6 6-6 6"/></svg>docs</summary>
      <div class="[--indent:1] flex flex-col border-s border-tsl24-line ms-[calc(1rem+(var(--indent)-1)*1.125rem)]">
        <a href="#" class="flex items-center gap-[7px] min-h-9 ps-3 pe-2.5 rounded-lg text-[13px] text-tsl24-mut no-underline transition-colors duration-150 hover:text-tsl24-ink hover:bg-tsl24-hover focus-visible:outline-2 focus-visible:outline-tsl24-accent focus-visible:outline-offset-1"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-current stroke-[1.7] [stroke-linejoin:round]"><path d="M6 2h9l5 5v15H6zM14 2v6h6"/></svg>README.md</a>
      </div>
    </details>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Sidebar.css</h1>
    <p class="max-w-[48ch] text-sm leading-relaxed text-tsl24-mut text-pretty">Every branch is a native <code class="font-tsl24-mono text-[12.5px]">&lt;details&gt;</code> &mdash; keyboard toggling and state come free. Indent guides keep level 3 legible.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl24-bg: #101317;
  --color-tsl24-bg: oklch(0.13 0.01 250);
  --color-tsl24-panel: #171a1f;
  --color-tsl24-panel: oklch(0.16 0.012 250);
  --color-tsl24-ink: #e8e9ed;
  --color-tsl24-ink: oklch(0.92 0.005 250);
  --color-tsl24-mut: #8e9299;
  --color-tsl24-mut: oklch(0.62 0.012 250);
  --color-tsl24-line: #363a41;
  --color-tsl24-line: oklch(0.27 0.014 250);
  --color-tsl24-accent: #5cc6e3;
  --color-tsl24-accent: oklch(0.75 0.12 210);
  --color-tsl24-hover: rgb(232 233 237 / 0.06);
  --color-tsl24-hover: color-mix(in oklab, oklch(0.92 0.005 250) 6%, transparent);
  --color-tsl24-tint: rgb(92 198 227 / 0.12);
  --color-tsl24-tint: color-mix(in oklab, oklch(0.75 0.12 210) 12%, transparent);
  --font-tsl24-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl24-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-24 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
