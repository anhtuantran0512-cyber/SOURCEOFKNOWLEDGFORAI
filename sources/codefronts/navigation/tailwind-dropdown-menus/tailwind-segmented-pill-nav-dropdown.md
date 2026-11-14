---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-segmented-pill-nav-dropdown/"
title: "Tailwind Segmented Pill Nav Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "An iOS-style segmented control where each pill lifts on hover and drops its own panel."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Segmented Pill Nav Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-segmented-pill-nav-dropdown/

An iOS-style segmented control where each pill lifts on hover and drops its own panel. The port is small and the lesson is about surfaces: a trough (shadow-[inset_…]) plus a raised pill (shadow-sm) is two utilities, and the whole control reads correctly without a single custom rule.
## HTML
```html
<section class="tdd-14 w-full min-h-svh grid justify-center content-start bg-linear-[135deg,var(--color-tdd14-bg1),var(--color-tdd14-bg2)] font-tdd14-sans text-tdd14-ink px-5 py-9" aria-label="Segmented pill nav dropdown demo">
  <nav class="relative z-10 flex gap-1 rounded-full bg-tdd14-trough p-1 shadow-[inset_0_1px_3px_oklch(0_0_0/0.08)]" aria-label="Sections">
    <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
      <button type="button" class="flex cursor-pointer items-center gap-1.5 whitespace-nowrap rounded-full border-0 bg-transparent px-4.5 py-2.5 font-tdd14-sans text-[13.5px] font-semibold text-tdd14-mut transition-[background,color,box-shadow] duration-200 group-hover:bg-white group-hover:text-tdd14-ink group-hover:shadow-sm focus-visible:bg-white focus-visible:text-tdd14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd14-acc">&#127968; Home</button>
      <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-40 -translate-x-1/2 -translate-y-1.5 flex-col gap-0.5 rounded-xl border border-tdd14-edge bg-white p-1.5 opacity-0 shadow-[0_12px_36px_oklch(0_0_0/0.12)] transition-[opacity,translate] duration-260 ease-tdd14 before:absolute before:inset-x-0 before:-top-2.5 before:h-2.5 before:content-[''] group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:duration-150">
        <a href="#dashboard" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Dashboard</a>
        <a href="#overview" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Overview</a>
        <a href="#widgets" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Widgets</a>
      </div>
    </div>
    <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
      <button type="button" class="flex cursor-pointer items-center gap-1.5 whitespace-nowrap rounded-full border-0 bg-transparent px-4.5 py-2.5 font-tdd14-sans text-[13.5px] font-semibold text-tdd14-mut transition-[background,color,box-shadow] duration-200 group-hover:bg-white group-hover:text-tdd14-ink group-hover:shadow-sm focus-visible:bg-white focus-visible:text-tdd14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd14-acc">&#128202; Analytics</button>
      <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-40 -translate-x-1/2 -translate-y-1.5 flex-col gap-0.5 rounded-xl border border-tdd14-edge bg-white p-1.5 opacity-0 shadow-[0_12px_36px_oklch(0_0_0/0.12)] transition-[opacity,translate] duration-260 ease-tdd14 before:absolute before:inset-x-0 before:-top-2.5 before:h-2.5 before:content-[''] group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:duration-150">
        <a href="#traffic" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Traffic</a>
        <a href="#conversions" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Conversions</a>
        <a href="#funnels" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Funnels</a>
        <a href="#cohorts" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Cohorts</a>
      </div>
    </div>
    <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
      <button type="button" class="flex cursor-pointer items-center gap-1.5 whitespace-nowrap rounded-full border-0 bg-transparent px-4.5 py-2.5 font-tdd14-sans text-[13.5px] font-semibold text-tdd14-mut transition-[background,color,box-shadow] duration-200 group-hover:bg-white group-hover:text-tdd14-ink group-hover:shadow-sm focus-visible:bg-white focus-visible:text-tdd14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd14-acc">&#128101; Audience</button>
      <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-40 -translate-x-1/2 -translate-y-1.5 flex-col gap-0.5 rounded-xl border border-tdd14-edge bg-white p-1.5 opacity-0 shadow-[0_12px_36px_oklch(0_0_0/0.12)] transition-[opacity,translate] duration-260 ease-tdd14 before:absolute before:inset-x-0 before:-top-2.5 before:h-2.5 before:content-[''] group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:duration-150">
        <a href="#segments" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Segments</a>
        <a href="#profiles" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Profiles</a>
        <a href="#behaviour" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Behaviour</a>
      </div>
    </div>
    <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
      <button type="button" class="flex cursor-pointer items-center gap-1.5 whitespace-nowrap rounded-full border-0 bg-transparent px-4.5 py-2.5 font-tdd14-sans text-[13.5px] font-semibold text-tdd14-mut transition-[background,color,box-shadow] duration-200 group-hover:bg-white group-hover:text-tdd14-ink group-hover:shadow-sm focus-visible:bg-white focus-visible:text-tdd14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd14-acc">&#9881; Settings</button>
      <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-40 -translate-x-1/2 -translate-y-1.5 flex-col gap-0.5 rounded-xl border border-tdd14-edge bg-white p-1.5 opacity-0 shadow-[0_12px_36px_oklch(0_0_0/0.12)] transition-[opacity,translate] duration-260 ease-tdd14 before:absolute before:inset-x-0 before:-top-2.5 before:h-2.5 before:content-[''] group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:duration-150">
        <a href="#general" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">General</a>
        <a href="#integrations" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Integrations</a>
        <a href="#billing" class="block rounded-lg px-3.5 py-2.5 text-[13.5px] font-medium text-tdd14-ink no-underline transition-colors duration-150 hover:bg-tdd14-tint hover:text-tdd14-acc focus-visible:bg-tdd14-tint focus-visible:outline-none">Billing</a>
      </div>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd14-bg1: #f8fafc;
  --color-tdd14-bg1: oklch(0.98 0.005 255);
  --color-tdd14-bg2: #f1f5f9;
  --color-tdd14-bg2: oklch(0.97 0.005 250);
  --color-tdd14-trough: #f1f5f9;
  --color-tdd14-trough: oklch(0.97 0.005 250);
  --color-tdd14-ink: #0f172a;
  --color-tdd14-ink: oklch(0.21 0.04 265);
  --color-tdd14-mut: #64748b;
  --color-tdd14-mut: oklch(0.55 0.03 255);
  --color-tdd14-edge: #e2e8f0;
  --color-tdd14-edge: oklch(0.92 0.01 255);
  --color-tdd14-tint: #eef2ff;
  --color-tdd14-tint: oklch(0.96 0.02 275);
  --color-tdd14-acc: #6366f1;
  --color-tdd14-acc: oklch(0.59 0.2 278);
  --font-tdd14-sans: 'DM Sans', system-ui, sans-serif;
  --ease-tdd14: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-14 {
  width: 100%;
  min-height: 100svh;
}

.tdd-14 ::selection {
  background: var(--color-tdd14-ink);
  color: #f8fafc;
}
```
