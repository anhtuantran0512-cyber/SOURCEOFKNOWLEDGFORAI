---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-sidebar-drawer-navigation/"
title: "Tailwind Sidebar Drawer Navigation"
section: "navigation"
category: "tailwind-css-responsive-navbars"
category_name: "Tailwind CSS Responsive Navbars"
description: "The dashboard drawer: off-canvas below md, permanently docked above it, and the same element in both cases."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar Drawer Navigation
Source: https://codefronts.com/navigation/tailwind-css-responsive-navbars/tailwind-sidebar-drawer-navigation/

The dashboard drawer: off-canvas below md, permanently docked above it, and the same element in both cases. -translate-x-full group-has-checked:translate-x-0 md:translate-x-0 is the entire state machine, and the backdrop is a <label>, so tapping it unchecks the box — no script, and no click handler that only a mouse can reach.
## HTML
```html
<div class="tnb-03 group w-full min-h-svh bg-tnb03-page font-tnb03-sans text-tnb03-ink" aria-label="Sidebar drawer navigation demo">
  <input type="checkbox" id="tnb03-drawer" class="sr-only peer" aria-label="Toggle sidebar">
  <header class="fixed inset-x-0 top-0 z-300 flex h-15 items-center gap-4 border-b border-tnb03-edge bg-tnb03-bar px-4 md:px-6">
    <label for="tnb03-drawer" class="flex size-11 shrink-0 cursor-pointer flex-col items-center justify-center gap-1.5 rounded-lg transition-colors hover:bg-white/7 md:hidden" aria-hidden="true">
      <span class="block h-px w-4.5 rounded-sm bg-tnb03-ink transition-transform duration-300 group-has-checked:translate-y-1.5 group-has-checked:rotate-45 motion-reduce:transition-none"></span>
      <span class="block h-px w-4.5 rounded-sm bg-tnb03-ink transition-opacity duration-300 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
      <span class="block h-px w-4.5 rounded-sm bg-tnb03-ink transition-transform duration-300 group-has-checked:-translate-y-1.5 group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
    </label>
    <a href="#home" class="text-lg font-extrabold tracking-[-0.02em] text-tnb03-ink no-underline">Arch<span class="text-tnb03-acc">ive</span></a>
    <div class="relative ml-2 hidden max-w-85 flex-1 sm:block">
      <span class="pointer-events-none absolute top-1/2 left-2.5 -translate-y-1/2 text-sm text-tnb03-mut" aria-hidden="true">&#128269;</span>
      <input type="search" placeholder="Search the archive" aria-label="Search" class="h-9 w-full rounded-lg border border-tnb03-edge bg-white/5 pr-3 pl-8.5 text-sm text-tnb03-ink outline-none transition-colors placeholder:text-tnb03-mut focus:border-tnb03-acc focus:bg-tnb03-acc/5">
    </div>
    <div class="ml-auto flex items-center gap-2">
      <button type="button" class="grid size-9 cursor-pointer place-items-center rounded-lg border-0 bg-transparent text-base text-tnb03-mut transition-colors hover:bg-white/7 hover:text-tnb03-ink" aria-label="Notifications">&#128276;</button>
      <span class="grid size-8 place-items-center rounded-full bg-linear-[135deg,var(--color-tnb03-acc),var(--color-tnb03-acc2)] text-[11px] font-bold text-white">VR</span>
    </div>
  </header>
  <label for="tnb03-drawer" class="pointer-events-none fixed inset-0 z-200 bg-black/60 opacity-0 transition-opacity duration-300 group-has-checked:pointer-events-auto group-has-checked:opacity-100 md:hidden motion-reduce:transition-none" aria-hidden="true"></label>
  <nav class="fixed inset-y-0 left-0 z-250 flex w-70 -translate-x-full flex-col overflow-y-auto border-r border-tnb03-edge bg-tnb03-side pt-15 transition-transform duration-350 ease-out group-has-checked:translate-x-0 md:translate-x-0 motion-reduce:transition-none" aria-label="Sidebar">
    <div class="grid px-2 py-3">
      <p class="px-3 pt-3 pb-1.5 text-[11px] font-semibold tracking-[0.1em] uppercase text-tnb03-mut">Main</p>
      <a href="#dashboard" aria-current="page" class="relative flex min-h-11 items-center gap-3 rounded-md px-3 text-sm font-medium text-tnb03-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb03-ink aria-[current=page]:bg-tnb03-acc/10 aria-[current=page]:text-tnb03-ink aria-[current=page]:before:absolute aria-[current=page]:before:top-1/2 aria-[current=page]:before:left-0 aria-[current=page]:before:h-3/5 aria-[current=page]:before:w-[3px] aria-[current=page]:before:-translate-y-1/2 aria-[current=page]:before:rounded-r-sm aria-[current=page]:before:bg-tnb03-acc aria-[current=page]:before:content-['']"><span class="w-5 text-center" aria-hidden="true">&#127968;</span>Dashboard</a>
      <a href="#analytics" class="flex min-h-11 items-center gap-3 rounded-md px-3 text-sm font-medium text-tnb03-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb03-ink"><span class="w-5 text-center" aria-hidden="true">&#128202;</span>Analytics <span class="ml-auto rounded-full bg-tnb03-acc px-1.5 text-[11px] font-bold text-white">New</span></a>
      <a href="#projects" class="flex min-h-11 items-center gap-3 rounded-md px-3 text-sm font-medium text-tnb03-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb03-ink"><span class="w-5 text-center" aria-hidden="true">&#128193;</span>Projects</a>
      <a href="#messages" class="flex min-h-11 items-center gap-3 rounded-md px-3 text-sm font-medium text-tnb03-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb03-ink"><span class="w-5 text-center" aria-hidden="true">&#9993;</span>Messages <span class="ml-auto rounded-full bg-tnb03-acc px-1.5 text-[11px] font-bold text-white">4</span></a>
      <p class="px-3 pt-4 pb-1.5 text-[11px] font-semibold tracking-[0.1em] uppercase text-tnb03-mut">Workspace</p>
      <a href="#tasks" class="flex min-h-11 items-center gap-3 rounded-md px-3 text-sm font-medium text-tnb03-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb03-ink"><span class="w-5 text-center" aria-hidden="true">&#128203;</span>Tasks</a>
      <a href="#calendar" class="flex min-h-11 items-center gap-3 rounded-md px-3 text-sm font-medium text-tnb03-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb03-ink"><span class="w-5 text-center" aria-hidden="true">&#128197;</span>Calendar</a>
      <a href="#files" class="flex min-h-11 items-center gap-3 rounded-md px-3 text-sm font-medium text-tnb03-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb03-ink"><span class="w-5 text-center" aria-hidden="true">&#128450;</span>Files</a>
      <p class="px-3 pt-4 pb-1.5 text-[11px] font-semibold tracking-[0.1em] uppercase text-tnb03-mut">Account</p>
      <a href="#settings" class="flex min-h-11 items-center gap-3 rounded-md px-3 text-sm font-medium text-tnb03-mut no-underline transition-colors hover:bg-white/5 hover:text-tnb03-ink"><span class="w-5 text-center" aria-hidden="true">&#9881;</span>Settings</a>
    </div>
    <div class="mt-auto flex items-center gap-3 border-t border-tnb03-edge p-4">
      <span class="grid size-8 shrink-0 place-items-center rounded-full bg-linear-[135deg,var(--color-tnb03-acc),var(--color-tnb03-acc2)] text-[11px] font-bold text-white">VR</span>
      <span><span class="block text-sm font-semibold text-tnb03-ink">Vimal Raj</span><span class="block text-xs text-tnb03-mut">Admin</span></span>
    </div>
  </nav>
  <main class="px-5 pt-24 pb-16 md:pl-75 md:pr-8">
    <h1 class="mb-4 text-3xl font-extrabold tracking-[-0.03em] text-tnb03-ink md:text-4xl">Sidebar Drawer <span class="text-tnb03-acc">Navigation</span></h1>
    <p class="max-w-xl text-lg leading-relaxed text-tnb03-mut">Above <code class="rounded bg-white/7 px-1.5 py-0.5 text-[0.9em]">md</code> the rail is docked. Below it, the same element is off-canvas and the hamburger — a real <code class="rounded bg-white/7 px-1.5 py-0.5 text-[0.9em]">&lt;label&gt;</code> — slides it in over a scrim that is also a label, so tapping the dim area closes it.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnb03-page: #0d1117;
  --color-tnb03-page: oklch(0.19 0.02 265);
  --color-tnb03-bar: #161b22;
  --color-tnb03-bar: oklch(0.23 0.02 265);
  --color-tnb03-side: #0d1117;
  --color-tnb03-side: oklch(0.19 0.02 265);
  --color-tnb03-ink: #e6edf3;
  --color-tnb03-ink: oklch(0.93 0.01 250);
  --color-tnb03-mut: #7d8590;
  --color-tnb03-mut: oklch(0.63 0.02 255);
  --color-tnb03-edge: #2a313c;
  --color-tnb03-edge: oklch(0.31 0.02 260);
  --color-tnb03-acc: #f78166;
  --color-tnb03-acc: oklch(0.73 0.15 38);
  --color-tnb03-acc2: #ffa657;
  --color-tnb03-acc2: oklch(0.79 0.15 63);
  --font-tnb03-sans: 'Syne', system-ui, sans-serif;
}

.tnb-03 {
  width: 100%;
  min-height: 100svh;
}

.tnb-03 ::selection {
  background: var(--color-tnb03-acc);
  color: #0d1117;
}
```
