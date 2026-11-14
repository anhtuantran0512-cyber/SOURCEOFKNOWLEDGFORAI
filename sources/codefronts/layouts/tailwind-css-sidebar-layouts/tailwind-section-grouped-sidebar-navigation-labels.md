---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-section-grouped-sidebar-navigation-labels/"
title: "Tailwind Section-Grouped Sidebar Navigation with Header Labels"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "How large admin tools stay navigable: links under quiet uppercase group labels, with no dividers anywhere."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Section-Grouped Sidebar Navigation with Header Labels
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-section-grouped-sidebar-navigation-labels/

How large admin tools stay navigable: links under quiet uppercase group labels, with no dividers anywhere. The whole technique is typographic &mdash; size, case, tracking, colour and a 10:1 spacing ratio &mdash; which makes it the demo where Tailwind's scale does the most work.
## HTML
```html
<section class="tsl-22 w-full h-svh min-h-svh grid grid-cols-[256px_1fr] font-tsl22-sans bg-tsl22-bg text-tsl22-ink">
  <aside aria-label="Admin" class="bg-tsl22-panel border-r border-tsl22-line px-3.5 py-5 overflow-y-auto [scrollbar-gutter:stable]">
    <div class="flex items-center gap-2.5 px-2.5 pt-0.5 pb-1.5 text-[15px] font-bold tracking-tight"><span aria-hidden="true" class="w-6 h-6 rounded-[7px] bg-[conic-gradient(from_80deg,var(--color-tsl22-accent),oklch(0.62_0.13_190))]"></span>Control Plane</div>
    <section aria-labelledby="tsl22-g1" class="mt-[22px]">
      <h2 id="tsl22-g1" class="px-3 pb-[7px] text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl22-label">Provisioning</h2>
      <ul class="list-none m-0 p-0 flex flex-col gap-0.5">
        <li><a href="#" aria-current="page" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover aria-[current=page]:text-tsl22-accent aria-[current=page]:bg-tsl22-tint aria-[current=page]:font-semibold focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">Clusters <span class="ms-auto rounded-full px-2 py-[3px] text-[11px] font-semibold text-tsl22-mut bg-tsl22-chip">8</span></a></li>
        <li><a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">Node pools</a></li>
        <li><a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">Volumes <span class="ms-auto rounded-full px-2 py-[3px] text-[11px] font-semibold text-tsl22-mut bg-tsl22-chip">42</span></a></li>
        <li><a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">Snapshots</a></li>
      </ul>
    </section>
    <section aria-labelledby="tsl22-g2" class="mt-[22px]">
      <h2 id="tsl22-g2" class="px-3 pb-[7px] text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl22-label">Networking</h2>
      <ul class="list-none m-0 p-0 flex flex-col gap-0.5">
        <li><a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">Load balancers</a></li>
        <li><a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">Firewalls <span class="ms-auto rounded-full px-2 py-[3px] text-[11px] font-semibold text-tsl22-mut bg-tsl22-chip">3</span></a></li>
        <li><a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">DNS zones</a></li>
      </ul>
    </section>
    <section aria-labelledby="tsl22-g3" class="mt-[22px]">
      <h2 id="tsl22-g3" class="px-3 pb-[7px] text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl22-label">Access</h2>
      <ul class="list-none m-0 p-0 flex flex-col gap-0.5">
        <li><a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">Team members</a></li>
        <li><a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">API tokens</a></li>
        <li><a href="#" class="flex items-center min-h-11 px-3 rounded-[9px] text-sm font-medium text-tsl22-mut no-underline transition-colors duration-150 hover:text-tsl22-ink hover:bg-tsl22-hover focus-visible:outline-2 focus-visible:outline-tsl22-accent focus-visible:outline-offset-1">Audit log</a></li>
      </ul>
    </section>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Clusters</h1>
    <p class="max-w-[48ch] text-sm leading-relaxed text-tsl22-mut text-pretty">No divider lines anywhere &mdash; the 22px-to-2px spacing rhythm and the label typography do all the grouping.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl22-bg: #fcfdfe;
  --color-tsl22-bg: oklch(0.99 0.002 230);
  --color-tsl22-panel: #f2f4f6;
  --color-tsl22-panel: oklch(0.965 0.005 230);
  --color-tsl22-ink: #383e47;
  --color-tsl22-ink: oklch(0.26 0.02 230);
  --color-tsl22-mut: #6f7680;
  --color-tsl22-mut: oklch(0.5 0.015 230);
  --color-tsl22-label: #7e848d;
  --color-tsl22-label: oklch(0.55 0.014 230);
  --color-tsl22-line: #dee1e5;
  --color-tsl22-line: oklch(0.89 0.008 230);
  --color-tsl22-accent: #2f62c4;
  --color-tsl22-accent: oklch(0.5 0.15 235);
  --color-tsl22-chip: rgb(56 62 71 / 0.07);
  --color-tsl22-chip: color-mix(in oklab, oklch(0.26 0.02 230) 7%, transparent);
  --color-tsl22-hover: rgb(56 62 71 / 0.05);
  --color-tsl22-hover: color-mix(in oklab, oklch(0.26 0.02 230) 5%, transparent);
  --color-tsl22-tint: rgb(47 98 196 / 0.1);
  --color-tsl22-tint: color-mix(in oklab, oklch(0.5 0.15 235) 10%, transparent);
  --font-tsl22-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-22 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: light;
}
```
