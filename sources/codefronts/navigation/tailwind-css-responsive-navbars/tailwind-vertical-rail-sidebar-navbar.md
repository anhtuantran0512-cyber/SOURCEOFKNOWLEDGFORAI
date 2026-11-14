---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-vertical-rail-sidebar-navbar/"
title: "Tailwind Vertical Rail Sidebar Navbar"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "A 64px icon rail that expands to 220px on toggle, with labels, section headings and a profile block fading in as it widens."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Rail Sidebar Navbar
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-vertical-rail-sidebar-navbar/

A 64px icon rail that expands to 220px on toggle, with labels, section headings and a profile block fading in as it widens. Five separate :checked ~ rules in the original become group-has-checked: on the five things that actually change — and the collapsed rail gains real tooltips, which the CSS version only suggested in its customization notes.
## HTML
```html
<div class="tnb-18 group flex w-full min-h-svh bg-tnb18-page font-tnb18-sans text-tnb18-ink" aria-label="Vertical rail sidebar demo">
  <input type="checkbox" id="tnb18-rail" class="sr-only peer" aria-label="Expand sidebar">
  <nav class="sticky top-0 flex h-svh w-16 shrink-0 flex-col overflow-hidden border-r border-tnb18-edge bg-tnb18-rail transition-[width] duration-300 ease-out group-has-checked:w-55 motion-reduce:transition-none" aria-label="Sidebar">
    <div class="flex h-14 shrink-0 items-center border-b border-tnb18-edge">
      <label for="tnb18-rail" class="grid h-14 w-16 shrink-0 cursor-pointer place-items-center text-lg text-tnb18-mut transition-colors hover:bg-white/4 hover:text-tnb18-ink" aria-hidden="true">&#8677;</label>
      <a href="#home" class="w-0 overflow-hidden text-[15px] font-bold tracking-[-0.02em] whitespace-nowrap text-tnb18-ink no-underline opacity-0 transition-[opacity,width] duration-300 group-has-checked:w-auto group-has-checked:opacity-100 motion-reduce:transition-none">Code<span class="text-tnb18-acc">Lab</span></a>
    </div>
    <div class="flex-1 overflow-y-auto py-3 [scrollbar-width:none]">
      <p class="h-0 overflow-hidden pl-5 text-[10px] font-bold tracking-[0.12em] whitespace-nowrap text-tnb18-mut uppercase opacity-0 transition-[opacity,height] duration-300 group-has-checked:h-6 group-has-checked:opacity-100 motion-reduce:transition-none">Main</p>
      <a href="#overview" aria-current="page" class="group/item relative flex h-11 items-center overflow-hidden text-tnb18-mut no-underline transition-colors hover:bg-white/3 hover:text-tnb18-ink aria-[current=page]:text-tnb18-acc aria-[current=page]:before:absolute aria-[current=page]:before:top-1/2 aria-[current=page]:before:left-0 aria-[current=page]:before:h-3/5 aria-[current=page]:before:w-[3px] aria-[current=page]:before:-translate-y-1/2 aria-[current=page]:before:rounded-r-sm aria-[current=page]:before:bg-tnb18-acc aria-[current=page]:before:content-['']">
        <span class="grid h-11 w-16 shrink-0 place-items-center text-base" aria-hidden="true">&#11041;</span>
        <span class="w-0 overflow-hidden text-sm font-medium whitespace-nowrap opacity-0 transition-[opacity,width] duration-300 group-has-checked:w-auto group-has-checked:opacity-100 motion-reduce:transition-none">Overview</span>
        <span class="pointer-events-none absolute left-18 z-10 rounded-md bg-tnb18-tip px-2 py-1 text-xs font-medium whitespace-nowrap text-tnb18-ink opacity-0 shadow-[0_4px_12px_oklch(0_0_0/0.4)] transition-opacity duration-150 group-not-has-checked:group-hover/item:opacity-100">Overview</span>
      </a>
      <a href="#analytics" class="group/item relative flex h-11 items-center overflow-hidden text-tnb18-mut no-underline transition-colors hover:bg-white/3 hover:text-tnb18-ink">
        <span class="grid h-11 w-16 shrink-0 place-items-center text-base" aria-hidden="true">&#128202;</span>
        <span class="w-0 overflow-hidden text-sm font-medium whitespace-nowrap opacity-0 transition-[opacity,width] duration-300 group-has-checked:w-auto group-has-checked:opacity-100 motion-reduce:transition-none">Analytics</span>
        <span class="mr-4 ml-auto rounded-full bg-tnb18-acc px-1.5 text-[10px] font-extrabold whitespace-nowrap text-tnb18-rail opacity-0 transition-opacity duration-300 group-has-checked:opacity-100">New</span>
        <span class="pointer-events-none absolute left-18 z-10 rounded-md bg-tnb18-tip px-2 py-1 text-xs font-medium whitespace-nowrap text-tnb18-ink opacity-0 shadow-[0_4px_12px_oklch(0_0_0/0.4)] transition-opacity duration-150 group-not-has-checked:group-hover/item:opacity-100">Analytics</span>
      </a>
      <a href="#deployments" class="group/item relative flex h-11 items-center overflow-hidden text-tnb18-mut no-underline transition-colors hover:bg-white/3 hover:text-tnb18-ink">
        <span class="grid h-11 w-16 shrink-0 place-items-center text-base" aria-hidden="true">&#128640;</span>
        <span class="w-0 overflow-hidden text-sm font-medium whitespace-nowrap opacity-0 transition-[opacity,width] duration-300 group-has-checked:w-auto group-has-checked:opacity-100 motion-reduce:transition-none">Deployments</span>
        <span class="pointer-events-none absolute left-18 z-10 rounded-md bg-tnb18-tip px-2 py-1 text-xs font-medium whitespace-nowrap text-tnb18-ink opacity-0 shadow-[0_4px_12px_oklch(0_0_0/0.4)] transition-opacity duration-150 group-not-has-checked:group-hover/item:opacity-100">Deployments</span>
      </a>
      <p class="h-0 overflow-hidden pl-5 text-[10px] font-bold tracking-[0.12em] whitespace-nowrap text-tnb18-mut uppercase opacity-0 transition-[opacity,height] duration-300 group-has-checked:h-6 group-has-checked:opacity-100 motion-reduce:transition-none">Resources</p>
      <a href="#storage" class="group/item relative flex h-11 items-center overflow-hidden text-tnb18-mut no-underline transition-colors hover:bg-white/3 hover:text-tnb18-ink">
        <span class="grid h-11 w-16 shrink-0 place-items-center text-base" aria-hidden="true">&#128452;</span>
        <span class="w-0 overflow-hidden text-sm font-medium whitespace-nowrap opacity-0 transition-[opacity,width] duration-300 group-has-checked:w-auto group-has-checked:opacity-100 motion-reduce:transition-none">Storage</span>
        <span class="pointer-events-none absolute left-18 z-10 rounded-md bg-tnb18-tip px-2 py-1 text-xs font-medium whitespace-nowrap text-tnb18-ink opacity-0 shadow-[0_4px_12px_oklch(0_0_0/0.4)] transition-opacity duration-150 group-not-has-checked:group-hover/item:opacity-100">Storage</span>
      </a>
      <a href="#auth" class="group/item relative flex h-11 items-center overflow-hidden text-tnb18-mut no-underline transition-colors hover:bg-white/3 hover:text-tnb18-ink">
        <span class="grid h-11 w-16 shrink-0 place-items-center text-base" aria-hidden="true">&#128272;</span>
        <span class="w-0 overflow-hidden text-sm font-medium whitespace-nowrap opacity-0 transition-[opacity,width] duration-300 group-has-checked:w-auto group-has-checked:opacity-100 motion-reduce:transition-none">Auth</span>
        <span class="pointer-events-none absolute left-18 z-10 rounded-md bg-tnb18-tip px-2 py-1 text-xs font-medium whitespace-nowrap text-tnb18-ink opacity-0 shadow-[0_4px_12px_oklch(0_0_0/0.4)] transition-opacity duration-150 group-not-has-checked:group-hover/item:opacity-100">Auth</span>
      </a>
      <a href="#logs" class="group/item relative flex h-11 items-center overflow-hidden text-tnb18-mut no-underline transition-colors hover:bg-white/3 hover:text-tnb18-ink">
        <span class="grid h-11 w-16 shrink-0 place-items-center text-base" aria-hidden="true">&#128203;</span>
        <span class="w-0 overflow-hidden text-sm font-medium whitespace-nowrap opacity-0 transition-[opacity,width] duration-300 group-has-checked:w-auto group-has-checked:opacity-100 motion-reduce:transition-none">Logs</span>
        <span class="mr-4 ml-auto rounded-full bg-tnb18-acc px-1.5 text-[10px] font-extrabold whitespace-nowrap text-tnb18-rail opacity-0 transition-opacity duration-300 group-has-checked:opacity-100">24</span>
        <span class="pointer-events-none absolute left-18 z-10 rounded-md bg-tnb18-tip px-2 py-1 text-xs font-medium whitespace-nowrap text-tnb18-ink opacity-0 shadow-[0_4px_12px_oklch(0_0_0/0.4)] transition-opacity duration-150 group-not-has-checked:group-hover/item:opacity-100">Logs</span>
      </a>
      <p class="h-0 overflow-hidden pl-5 text-[10px] font-bold tracking-[0.12em] whitespace-nowrap text-tnb18-mut uppercase opacity-0 transition-[opacity,height] duration-300 group-has-checked:h-6 group-has-checked:opacity-100 motion-reduce:transition-none">Account</p>
      <a href="#settings" class="group/item relative flex h-11 items-center overflow-hidden text-tnb18-mut no-underline transition-colors hover:bg-white/3 hover:text-tnb18-ink">
        <span class="grid h-11 w-16 shrink-0 place-items-center text-base" aria-hidden="true">&#128295;</span>
        <span class="w-0 overflow-hidden text-sm font-medium whitespace-nowrap opacity-0 transition-[opacity,width] duration-300 group-has-checked:w-auto group-has-checked:opacity-100 motion-reduce:transition-none">Settings</span>
        <span class="pointer-events-none absolute left-18 z-10 rounded-md bg-tnb18-tip px-2 py-1 text-xs font-medium whitespace-nowrap text-tnb18-ink opacity-0 shadow-[0_4px_12px_oklch(0_0_0/0.4)] transition-opacity duration-150 group-not-has-checked:group-hover/item:opacity-100">Settings</span>
      </a>
    </div>
    <div class="flex h-14 shrink-0 items-center border-t border-tnb18-edge">
      <span class="grid h-14 w-16 shrink-0 place-items-center" aria-hidden="true"><span class="grid size-8 place-items-center rounded-full bg-linear-[135deg,var(--color-tnb18-acc),var(--color-tnb18-acc2)] text-[11px] font-bold text-white">VR</span></span>
      <span class="w-0 overflow-hidden whitespace-nowrap opacity-0 transition-[opacity,width] duration-300 group-has-checked:w-auto group-has-checked:opacity-100 motion-reduce:transition-none"><span class="block text-[13px] font-semibold text-tnb18-ink">Vimal Raj</span><span class="block text-[11px] text-tnb18-mut">Pro plan</span></span>
    </div>
  </nav>
  <main class="min-w-0 flex-1 px-6 py-10">
    <h1 class="mb-4 text-2xl font-bold tracking-[-0.03em] text-tnb18-acc md:text-3xl">Vertical Rail Sidebar</h1>
    <p class="max-w-xl leading-relaxed text-tnb18-mut">Click <span class="text-tnb18-ink">&#8677;</span> to expand the rail from 64px to 220px. While it is collapsed, hovering an icon shows a tooltip — <code class="rounded bg-white/5 px-1.5 py-0.5 text-[0.9em] text-tnb18-ink">group-not-has-checked:group-hover/item:opacity-100</code>, a compound the stylesheet version never had.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb18-page: #1b1e26;
  --color-tnb18-page: oklch(0.25 0.01 265);
  --color-tnb18-rail: #16181f;
  --color-tnb18-rail: oklch(0.22 0.01 265);
  --color-tnb18-tip: #2b2f3a;
  --color-tnb18-tip: oklch(0.32 0.01 265);
  --color-tnb18-ink: #e8eaf2;
  --color-tnb18-ink: oklch(0.93 0.01 270);
  --color-tnb18-mut: #9aa0b4;
  --color-tnb18-mut: oklch(0.7 0.02 270);
  --color-tnb18-edge: #2c2f38;
  --color-tnb18-edge: oklch(0.31 0.01 265);
  --color-tnb18-acc: #f59e0b;
  --color-tnb18-acc: oklch(0.77 0.16 70);
  --color-tnb18-acc2: #ef4444;
  --color-tnb18-acc2: oklch(0.63 0.22 25);
  --font-tnb18-sans: 'Inter', system-ui, sans-serif;
}

.tnb-18 {
  width: 100%;
  min-height: 100svh;
}

.tnb-18 ::selection {
  background: var(--color-tnb18-acc);
  color: #16181f;
}

.tnb-18 div::-webkit-scrollbar {
  display: none;
}
```
