---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-mega-menu-grid-dropdown/"
title: "Tailwind Mega Menu Grid Dropdown"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "The four-column mega menu — three link groups and a featured card — where the port is almost entirely about grid."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mega Menu Grid Dropdown
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-mega-menu-grid-dropdown/

The four-column mega menu — three link groups and a featured card — where the port is almost entirely about grid. grid-cols-[1fr_1fr_1fr_1.4fr] states the whole layout in one utility, and the responsive collapse that the CSS version leaves as a to-do becomes a single max-md:grid-cols-1.
## HTML
```html
<section class="tdd-07 w-full min-h-svh bg-linear-[135deg,var(--color-tdd07-bg1),var(--color-tdd07-bg2)] font-tdd07-sans text-tdd07-ink px-5 py-8" aria-label="Mega menu grid dropdown demo">
  <nav class="relative z-10 mx-auto flex w-[min(780px,100%)] items-center gap-1 rounded-2xl border border-tdd07-edge bg-white py-2.5 pr-2.5 pl-5 shadow-[0_2px_16px_oklch(0_0_0/0.06)]" aria-label="Primary">
    <span class="mr-2 text-lg font-bold tracking-[-0.5px] text-tdd07-acc">Prism</span>
    <div class="flex flex-1 items-center gap-0.5">
      <a href="#home" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd07-acc">Home</a>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-3 after:content-['']">
        <a href="#platform" class="block whitespace-nowrap rounded-lg px-3.5 py-2 text-sm font-medium text-tdd07-ink no-underline transition-colors duration-150 group-hover:bg-tdd07-tint group-hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd07-acc">Platform &#9662;</a>
        <div class="pointer-events-none absolute top-[calc(100%+12px)] left-1/2 grid w-[min(620px,88vw)] -translate-x-1/2 -translate-y-2 grid-cols-[1fr_1fr_1fr_1.4fr] gap-6 rounded-2xl border border-tdd07-edge bg-white p-6 opacity-0 shadow-[0_20px_60px_oklch(0_0_0/0.12)] transition-[opacity,translate] duration-300 ease-tdd07 before:absolute before:inset-x-0 before:-top-3 before:h-3 before:content-[''] group-hover:pointer-events-auto group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:translate-y-0 group-focus-within:opacity-100 max-md:grid-cols-1 motion-reduce:duration-150">
          <div class="flex flex-col gap-0.5">
            <p class="mb-2.5 border-b border-tdd07-edge pb-2 text-[10.5px] font-bold uppercase tracking-[0.1em] text-tdd07-mut">Core</p>
            <a href="#analytics" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#128202; Analytics</a>
            <a href="#integrations" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#128736; Integrations</a>
            <a href="#automations" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#127381; Automations</a>
            <a href="#security" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#128274; Security</a>
          </div>
          <div class="flex flex-col gap-0.5">
            <p class="mb-2.5 border-b border-tdd07-edge pb-2 text-[10.5px] font-bold uppercase tracking-[0.1em] text-tdd07-mut">Growth</p>
            <a href="#revenue" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#128184; Revenue Ops</a>
            <a href="#marketing" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#127775; Marketing Suite</a>
            <a href="#crm" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#128101; CRM</a>
            <a href="#support" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#128172; Support Hub</a>
          </div>
          <div class="flex flex-col gap-0.5">
            <p class="mb-2.5 border-b border-tdd07-edge pb-2 text-[10.5px] font-bold uppercase tracking-[0.1em] text-tdd07-mut">Infra</p>
            <a href="#cdn" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#9928; Edge CDN</a>
            <a href="#storage" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#128190; Storage</a>
            <a href="#config" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#9881; Config</a>
            <a href="#logs" class="block rounded-lg px-2 py-1.5 text-[13px] font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:bg-tdd07-tint focus-visible:outline-none">&#128203; Logs</a>
          </div>
          <div class="flex flex-col gap-2">
            <p class="mb-2.5 border-b border-tdd07-edge pb-2 text-[10.5px] font-bold uppercase tracking-[0.1em] text-tdd07-mut">What's New</p>
            <div class="flex flex-1 flex-col gap-1.5 rounded-xl border border-tdd07-cardedge bg-linear-[135deg,var(--color-tdd07-bg1),var(--color-tdd07-bg2)] p-4">
              <span class="self-start rounded bg-tdd07-bg2 px-1.5 py-0.5 text-[9px] font-bold tracking-[0.1em] text-tdd07-acc">NEW</span>
              <p class="text-sm font-bold text-tdd07-ink">AI Copilot</p>
              <p class="text-xs leading-relaxed text-tdd07-mut text-pretty">Intelligent workflow automation powered by large language models.</p>
              <a href="#learn-more" class="mt-auto text-xs font-semibold text-tdd07-acc no-underline hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd07-acc">Learn more &#8594;</a>
            </div>
          </div>
        </div>
      </div>
      <a href="#pricing" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd07-acc">Pricing</a>
      <a href="#docs" class="rounded-lg px-3.5 py-2 text-sm font-medium text-tdd07-ink no-underline transition-colors duration-150 hover:bg-tdd07-tint hover:text-tdd07-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd07-acc">Docs</a>
    </div>
    <a href="#signup" class="ml-auto whitespace-nowrap rounded-lg bg-tdd07-acc px-4.5 py-2 text-[13.5px] font-semibold text-white no-underline transition-opacity duration-150 hover:opacity-90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd07-acc">Sign Up Free</a>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd07-bg1: #f0f9ff;
  --color-tdd07-bg1: oklch(0.98 0.02 230);
  --color-tdd07-bg2: #e0f2fe;
  --color-tdd07-bg2: oklch(0.95 0.04 230);
  --color-tdd07-ink: #0f172a;
  --color-tdd07-ink: oklch(0.21 0.04 265);
  --color-tdd07-mut: #64748b;
  --color-tdd07-mut: oklch(0.55 0.03 255);
  --color-tdd07-edge: #e2e8f0;
  --color-tdd07-edge: oklch(0.92 0.01 255);
  --color-tdd07-cardedge: #bae6fd;
  --color-tdd07-cardedge: oklch(0.88 0.07 230);
  --color-tdd07-tint: #f0f9ff;
  --color-tdd07-tint: oklch(0.98 0.02 230);
  --color-tdd07-acc: #0ea5e9;
  --color-tdd07-acc: oklch(0.68 0.15 233);
  --font-tdd07-sans: 'Inter', system-ui, sans-serif;
  --ease-tdd07: cubic-bezier(0.16, 1, 0.3, 1);
}

.tdd-07 {
  width: 100%;
  min-height: 100svh;
}

.tdd-07 ::selection {
  background: var(--color-tdd07-acc);
  color: #fff;
}
```
