---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-tabbed-sidebar-radio-panel-switching/"
title: "Tailwind Tabbed Sidebar with Radio-Driven Panel Switching"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "One sidebar, three personalities: Files, Search and Activity, switched by a segmented control."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tabbed Sidebar with Radio-Driven Panel Switching
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-tabbed-sidebar-radio-panel-switching/

One sidebar, three personalities: Files, Search and Activity, switched by a segmented control. Hidden radios drive which panel renders, a thumb glides between tabs, and panels enter with a few pixels of lift &mdash; with native arrow-key switching for free.
## HTML
```html
<section class="tsl-25 w-full h-svh min-h-svh grid grid-cols-[272px_1fr] font-tsl25-sans bg-tsl25-bg text-tsl25-ink">
  <aside class="flex flex-col overflow-hidden bg-tsl25-panel border-r border-tsl25-line px-3 py-3.5">
    <input type="radio" name="tsl25" id="tsl25-t1" checked class="sr-only"><input type="radio" name="tsl25" id="tsl25-t2" class="sr-only"><input type="radio" name="tsl25" id="tsl25-t3" class="sr-only">
    <div role="group" aria-label="Sidebar panels" class="relative grid grid-cols-3 p-1 rounded-[11px] bg-tsl25-well border border-tsl25-line has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-tsl25-accent has-[:focus-visible]:outline-offset-2">
      <div aria-hidden="true" class="tsl-25-thumb absolute top-1 bottom-1 left-1 w-[calc((100%-8px)/3)] rounded-lg bg-tsl25-thumb border border-tsl25-thumbline translate-x-0 transition-transform duration-[280ms] ease-[cubic-bezier(.5,0,.2,1.1)] motion-reduce:transition-none"></div>
      <label for="tsl25-t1" class="tsl-25-tab relative z-[1] grid place-items-center min-h-11 rounded-lg text-[12.5px] font-semibold text-tsl25-mut cursor-pointer transition-colors duration-200">Files</label>
      <label for="tsl25-t2" class="tsl-25-tab relative z-[1] grid place-items-center min-h-11 rounded-lg text-[12.5px] font-semibold text-tsl25-mut cursor-pointer transition-colors duration-200">Search</label>
      <label for="tsl25-t3" class="tsl-25-tab relative z-[1] grid place-items-center min-h-11 rounded-lg text-[12.5px] font-semibold text-tsl25-mut cursor-pointer transition-colors duration-200">Activity</label>
    </div>
    <div data-panel="1" class="tsl-25-panel hidden flex-col gap-0.5 pt-3.5 min-h-0 overflow-y-auto animate-tsl25-in motion-reduce:animate-none">
      <a href="#" aria-current="page" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl25-mut no-underline transition-colors duration-150 hover:text-tsl25-ink hover:bg-tsl25-hover aria-[current=page]:text-tsl25-accent aria-[current=page]:bg-tsl25-tint focus-visible:outline-2 focus-visible:outline-tsl25-accent focus-visible:outline-offset-1">proposal-v3.md</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl25-mut no-underline transition-colors duration-150 hover:text-tsl25-ink hover:bg-tsl25-hover focus-visible:outline-2 focus-visible:outline-tsl25-accent focus-visible:outline-offset-1">budget-2027.xlsx</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl25-mut no-underline transition-colors duration-150 hover:text-tsl25-ink hover:bg-tsl25-hover focus-visible:outline-2 focus-visible:outline-tsl25-accent focus-visible:outline-offset-1">kickoff-notes.md</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl25-mut no-underline transition-colors duration-150 hover:text-tsl25-ink hover:bg-tsl25-hover focus-visible:outline-2 focus-visible:outline-tsl25-accent focus-visible:outline-offset-1">brand-audit.pdf</a>
    </div>
    <div data-panel="2" class="tsl-25-panel hidden flex-col gap-0.5 pt-3.5 min-h-0 overflow-y-auto animate-tsl25-in motion-reduce:animate-none">
      <label class="grid grid-cols-[auto_1fr] items-center gap-2 h-11 px-3 mb-2.5 rounded-[10px] border border-tsl25-line bg-tsl25-well focus-within:border-tsl25-accent focus-within:shadow-[0_0_0_3px_var(--color-tsl25-ring)]"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[15px] h-[15px] fill-none stroke-tsl25-mut stroke-2 [stroke-linecap:round]"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input type="search" placeholder="Search workspace&hellip;" aria-label="Search workspace" class="min-w-0 border-0 bg-transparent text-tsl25-ink text-[13px] outline-none placeholder:text-tsl25-placeholder"></label>
      <span class="px-3 pt-1.5 pb-1 text-[10.5px] font-semibold uppercase tracking-[0.08em] text-tsl25-mut">Recent</span>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl25-mut no-underline transition-colors duration-150 hover:text-tsl25-ink hover:bg-tsl25-hover focus-visible:outline-2 focus-visible:outline-tsl25-accent focus-visible:outline-offset-1">container queries</a>
      <a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-[13.5px] font-medium text-tsl25-mut no-underline transition-colors duration-150 hover:text-tsl25-ink hover:bg-tsl25-hover focus-visible:outline-2 focus-visible:outline-tsl25-accent focus-visible:outline-offset-1">q3 roadmap</a>
    </div>
    <div data-panel="3" class="tsl-25-panel hidden flex-col pt-3.5 min-h-0 overflow-y-auto animate-tsl25-in motion-reduce:animate-none">
      <p class="px-3 py-2.5 border-b border-tsl25-line text-[13px] leading-[1.5] text-tsl25-mut"><strong class="font-semibold text-tsl25-ink">Priya</strong> edited proposal-v3 <time class="float-right text-[11px]">12m</time></p>
      <p class="px-3 py-2.5 border-b border-tsl25-line text-[13px] leading-[1.5] text-tsl25-mut"><strong class="font-semibold text-tsl25-ink">Marcus</strong> commented <time class="float-right text-[11px]">1h</time></p>
      <p class="px-3 py-2.5 border-b border-tsl25-line text-[13px] leading-[1.5] text-tsl25-mut"><strong class="font-semibold text-tsl25-ink">Amara</strong> uploaded 2 files <time class="float-right text-[11px]">3h</time></p>
    </div>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">proposal-v3.md</h1>
    <p class="max-w-[46ch] text-sm leading-relaxed text-tsl25-mut text-pretty">Switch tabs &mdash; the thumb glides, panels cross-fade. Radios give the group arrow-key switching natively.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl25-bg: #171210;
  --color-tsl25-bg: oklch(0.13 0.013 35);
  --color-tsl25-panel: #201a16;
  --color-tsl25-panel: oklch(0.17 0.016 35);
  --color-tsl25-well: #1a1512;
  --color-tsl25-well: oklch(0.14 0.014 35);
  --color-tsl25-ink: #f2ece7;
  --color-tsl25-ink: oklch(0.94 0.006 35);
  --color-tsl25-mut: #a3968c;
  --color-tsl25-mut: oklch(0.65 0.014 35);
  --color-tsl25-placeholder: #8a7d73;
  --color-tsl25-placeholder: oklch(0.57 0.014 35);
  --color-tsl25-line: #3d342e;
  --color-tsl25-line: oklch(0.28 0.018 35);
  --color-tsl25-accent: #e0904f;
  --color-tsl25-accent: oklch(0.72 0.15 40);
  --color-tsl25-thumb: rgb(224 144 79 / 0.22);
  --color-tsl25-thumb: color-mix(in oklab, oklch(0.72 0.15 40) 22%, transparent);
  --color-tsl25-thumbline: rgb(224 144 79 / 0.4);
  --color-tsl25-thumbline: color-mix(in oklab, oklch(0.72 0.15 40) 40%, transparent);
  --color-tsl25-ring: rgb(224 144 79 / 0.2);
  --color-tsl25-ring: color-mix(in oklab, oklch(0.72 0.15 40) 20%, transparent);
  --color-tsl25-hover: rgb(242 236 231 / 0.06);
  --color-tsl25-hover: color-mix(in oklab, oklch(0.94 0.006 35) 6%, transparent);
  --color-tsl25-tint: rgb(224 144 79 / 0.12);
  --color-tsl25-tint: color-mix(in oklab, oklch(0.72 0.15 40) 12%, transparent);
  --font-tsl25-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-tsl25-in: tsl25-in .25s ease;
}

@keyframes tsl25-in {
  from {
    opacity: 0;
    translate: 0 4px;
  }
}

.tsl-25 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
/* STATE — thumb position, tab colour and which panel is displayed.
   display, not opacity: a hidden panel must leave the tab order. */

#tsl25-t2:checked ~ [role="group"] .tsl-25-thumb {
  translate: 100% 0;
}

#tsl25-t3:checked ~ [role="group"] .tsl-25-thumb {
  translate: 200% 0;
}

#tsl25-t1:checked ~ [role="group"] label[for="tsl25-t1"],
#tsl25-t2:checked ~ [role="group"] label[for="tsl25-t2"],
#tsl25-t3:checked ~ [role="group"] label[for="tsl25-t3"] {
  color: var(--color-tsl25-ink);
}

#tsl25-t1:checked ~ [data-panel="1"],
#tsl25-t2:checked ~ [data-panel="2"],
#tsl25-t3:checked ~ [data-panel="3"] {
  display: flex;
}
```
