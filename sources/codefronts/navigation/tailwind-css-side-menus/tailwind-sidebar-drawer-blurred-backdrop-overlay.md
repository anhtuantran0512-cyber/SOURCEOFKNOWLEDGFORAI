---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-sidebar-drawer-blurred-backdrop-overlay/"
title: "Tailwind Sidebar Drawer with Blurred Backdrop Overlay"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A slide-over drawer that frosts the page behind it: the backdrop animates from clear to backdrop-blur-sm and 60% ink while the panel glides in on an…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar Drawer with Blurred Backdrop Overlay
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-sidebar-drawer-blurred-backdrop-overlay/

A slide-over drawer that frosts the page behind it: the backdrop animates from clear to backdrop-blur-sm and 60% ink while the panel glides in on an iOS-sheet curve. The backdrop is a second <label> for the same checkbox, so tapping anywhere outside closes the menu — no JavaScript, no event listeners.
## HTML
```html
<section class="tsm-02 group relative isolate w-full min-h-svh overflow-hidden bg-tsm02-bg font-tsm02-sans text-tsm02-ink" aria-label="Sidebar drawer with blurred backdrop overlay demo">
  <input type="checkbox" id="tsm-02-toggle" class="peer sr-only">
  <div class="flex items-center gap-4 border-b border-tsm02-acc/15 px-5 py-4">
    <label for="tsm-02-toggle" data-tsm02-burger class="relative z-50 grid size-11 cursor-pointer place-content-center gap-[5px] rounded-xl border border-tsm02-acc/25 bg-tsm02-acc/10 transition-colors hover:bg-tsm02-acc/25 group-has-[input:focus-visible]:outline-2 group-has-[input:focus-visible]:outline-offset-2 group-has-[input:focus-visible]:outline-tsm02-acc2">
      <span class="sr-only">Toggle navigation menu</span>
      <span aria-hidden="true" class="block h-0.5 w-[18px] rounded-full bg-tsm02-acc2 transition-transform duration-450 group-has-checked:translate-y-[7px] group-has-checked:rotate-45 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="block h-0.5 w-[18px] rounded-full bg-tsm02-acc2 transition-opacity duration-450 group-has-checked:opacity-0 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="block h-0.5 w-[18px] rounded-full bg-tsm02-acc2 transition-transform duration-450 group-has-checked:-translate-y-[7px] group-has-checked:-rotate-45 motion-reduce:transition-none"></span>
    </label>
    <h1 class="font-tsm02-display text-xl font-extrabold">Overview</h1>
    <span class="ml-auto hidden items-center gap-2 rounded-full border border-tsm02-acc/25 px-3 py-1 text-xs font-semibold text-tsm02-acc2 sm:inline-flex"><span aria-hidden="true" class="size-1.5 rounded-full bg-emerald-400"></span>All systems normal</span>
  </div>
  <label for="tsm-02-toggle" aria-hidden="true" class="pointer-events-none absolute inset-0 z-30 bg-tsm02-bg/0 transition-[background-color,backdrop-filter] duration-450 group-has-checked:pointer-events-auto group-has-checked:bg-tsm02-bg/60 group-has-checked:backdrop-blur-sm motion-reduce:transition-none"></label>
  <nav aria-label="Main" class="invisible absolute inset-y-0 left-0 z-40 flex w-[min(300px,86vw)] -translate-x-full flex-col border-r border-tsm02-acc/15 bg-tsm02-drawer pt-[88px] pb-5 transition-[translate,visibility,box-shadow] duration-450 ease-[cubic-bezier(0.32,0.72,0,1)] before:absolute before:inset-x-0 before:top-0 before:h-0.5 before:bg-linear-to-r before:from-transparent before:via-tsm02-acc before:to-transparent group-has-checked:visible group-has-checked:translate-x-0 group-has-checked:shadow-[0_0_60px_oklch(0.68_0.15_235/0.12),8px_0_40px_oklch(0_0_0/0.6)] motion-reduce:transition-none">
    <p class="px-5 pb-2 text-[10px] font-bold tracking-[0.15em] text-tsm02-mut uppercase">Navigation</p>
    <ul class="grid flex-1 content-start gap-0.5 px-3">
      <li><a href="#" class="group/l relative flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm02-mut transition-colors before:absolute before:top-1/2 before:left-0 before:h-0 before:w-[3px] before:-translate-y-1/2 before:rounded-full before:bg-tsm02-acc before:transition-[height] hover:bg-tsm02-acc/10 hover:text-tsm02-ink hover:before:h-[60%] focus-visible:outline-2 focus-visible:outline-tsm02-acc2 aria-[current=page]:bg-tsm02-acc/12 aria-[current=page]:text-tsm02-ink aria-[current=page]:before:h-[60%]" aria-current="page"><span aria-hidden="true" class="size-2 shrink-0 rounded-full bg-tsm02-mut/60 transition-[background-color,box-shadow] group-hover/l:bg-tsm02-acc group-hover/l:shadow-[0_0_8px_var(--color-tsm02-acc)] group-aria-[current=page]/l:bg-tsm02-acc group-aria-[current=page]/l:shadow-[0_0_8px_var(--color-tsm02-acc)]"></span>Overview</a></li>
      <li><a href="#" class="group/l relative flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm02-mut transition-colors before:absolute before:top-1/2 before:left-0 before:h-0 before:w-[3px] before:-translate-y-1/2 before:rounded-full before:bg-tsm02-acc before:transition-[height] hover:bg-tsm02-acc/10 hover:text-tsm02-ink hover:before:h-[60%] focus-visible:outline-2 focus-visible:outline-tsm02-acc2 aria-[current=page]:bg-tsm02-acc/12 aria-[current=page]:text-tsm02-ink aria-[current=page]:before:h-[60%]"><span aria-hidden="true" class="size-2 shrink-0 rounded-full bg-tsm02-mut/60 transition-[background-color,box-shadow] group-hover/l:bg-tsm02-acc group-hover/l:shadow-[0_0_8px_var(--color-tsm02-acc)] group-aria-[current=page]/l:bg-tsm02-acc group-aria-[current=page]/l:shadow-[0_0_8px_var(--color-tsm02-acc)]"></span>Deployments<span class="ml-auto rounded-full bg-tsm02-acc/20 px-2 py-0.5 text-[10px] font-bold text-tsm02-acc2">12</span></a></li>
      <li><a href="#" class="group/l relative flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm02-mut transition-colors before:absolute before:top-1/2 before:left-0 before:h-0 before:w-[3px] before:-translate-y-1/2 before:rounded-full before:bg-tsm02-acc before:transition-[height] hover:bg-tsm02-acc/10 hover:text-tsm02-ink hover:before:h-[60%] focus-visible:outline-2 focus-visible:outline-tsm02-acc2 aria-[current=page]:bg-tsm02-acc/12 aria-[current=page]:text-tsm02-ink aria-[current=page]:before:h-[60%]"><span aria-hidden="true" class="size-2 shrink-0 rounded-full bg-tsm02-mut/60 transition-[background-color,box-shadow] group-hover/l:bg-tsm02-acc group-hover/l:shadow-[0_0_8px_var(--color-tsm02-acc)] group-aria-[current=page]/l:bg-tsm02-acc group-aria-[current=page]/l:shadow-[0_0_8px_var(--color-tsm02-acc)]"></span>Integrations</a></li>
      <li><a href="#" class="group/l relative flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm02-mut transition-colors before:absolute before:top-1/2 before:left-0 before:h-0 before:w-[3px] before:-translate-y-1/2 before:rounded-full before:bg-tsm02-acc before:transition-[height] hover:bg-tsm02-acc/10 hover:text-tsm02-ink hover:before:h-[60%] focus-visible:outline-2 focus-visible:outline-tsm02-acc2 aria-[current=page]:bg-tsm02-acc/12 aria-[current=page]:text-tsm02-ink aria-[current=page]:before:h-[60%]"><span aria-hidden="true" class="size-2 shrink-0 rounded-full bg-tsm02-mut/60 transition-[background-color,box-shadow] group-hover/l:bg-tsm02-acc group-hover/l:shadow-[0_0_8px_var(--color-tsm02-acc)] group-aria-[current=page]/l:bg-tsm02-acc group-aria-[current=page]/l:shadow-[0_0_8px_var(--color-tsm02-acc)]"></span>Logs<span class="ml-auto rounded-full bg-tsm02-acc/20 px-2 py-0.5 text-[10px] font-bold text-tsm02-acc2">3</span></a></li>
      <li><a href="#" class="group/l relative flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-sm font-semibold text-tsm02-mut transition-colors before:absolute before:top-1/2 before:left-0 before:h-0 before:w-[3px] before:-translate-y-1/2 before:rounded-full before:bg-tsm02-acc before:transition-[height] hover:bg-tsm02-acc/10 hover:text-tsm02-ink hover:before:h-[60%] focus-visible:outline-2 focus-visible:outline-tsm02-acc2 aria-[current=page]:bg-tsm02-acc/12 aria-[current=page]:text-tsm02-ink aria-[current=page]:before:h-[60%]"><span aria-hidden="true" class="size-2 shrink-0 rounded-full bg-tsm02-mut/60 transition-[background-color,box-shadow] group-hover/l:bg-tsm02-acc group-hover/l:shadow-[0_0_8px_var(--color-tsm02-acc)] group-aria-[current=page]/l:bg-tsm02-acc group-aria-[current=page]/l:shadow-[0_0_8px_var(--color-tsm02-acc)]"></span>Settings</a></li>
    </ul>
    <div class="mx-5 flex items-center gap-2.5 border-t border-tsm02-acc/15 pt-4">
      <span aria-hidden="true" class="grid size-[34px] place-items-center rounded-full bg-linear-135 from-sky-500 to-indigo-500 text-xs font-bold">AK</span>
      <div><p class="text-[13px] font-bold">Alex Kim</p><p class="text-[11px] text-tsm02-mut">Admin</p></div>
    </div>
  </nav>
  <div class="mx-auto w-full max-w-3xl px-5 py-8">
    <p class="mb-6 max-w-prose text-sm leading-relaxed text-tsm02-mut text-pretty">Open the drawer and the page frosts over. Tap the blurred area to dismiss — the backdrop is a second label for the same checkbox.</p>
    <div class="grid grid-cols-2 gap-3 md:grid-cols-4">
      <div class="rounded-2xl border border-tsm02-acc/15 bg-tsm02-surface p-5"><p class="font-tsm02-display text-[26px] font-extrabold tabular-nums text-tsm02-acc2">99.9%</p><p class="mt-1 text-xs text-tsm02-mut">Uptime SLA</p></div>
      <div class="rounded-2xl border border-tsm02-acc/15 bg-tsm02-surface p-5"><p class="font-tsm02-display text-[26px] font-extrabold tabular-nums text-tsm02-acc2">4.2ms</p><p class="mt-1 text-xs text-tsm02-mut">Avg latency</p></div>
      <div class="rounded-2xl border border-tsm02-acc/15 bg-tsm02-surface p-5"><p class="font-tsm02-display text-[26px] font-extrabold tabular-nums text-tsm02-acc2">18k</p><p class="mt-1 text-xs text-tsm02-mut">Requests / hr</p></div>
      <div class="rounded-2xl border border-tsm02-acc/15 bg-tsm02-surface p-5"><p class="font-tsm02-display text-[26px] font-extrabold tabular-nums text-tsm02-acc2">0</p><p class="mt-1 text-xs text-tsm02-mut">Open incidents</p></div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm02-bg: #030712;
  --color-tsm02-bg: oklch(0.13 0.027 261.7);
  --color-tsm02-surface: #111827;
  --color-tsm02-surface: oklch(0.21 0.032 264.7);
  --color-tsm02-drawer: #060e1e;
  --color-tsm02-drawer: oklch(0.165 0.036 261.8);
  --color-tsm02-acc: #0ea5e9;
  --color-tsm02-acc: oklch(0.685 0.148 237.3);
  --color-tsm02-acc2: #38bdf8;
  --color-tsm02-acc2: oklch(0.754 0.139 232.7);
  --color-tsm02-ink: #f1f5f9;
  --color-tsm02-ink: oklch(0.968 0.007 247.9);
  --color-tsm02-mut: #94a3b8;
  --color-tsm02-mut: oklch(0.711 0.035 256.8);
  --font-tsm02-display: 'Syne', system-ui, sans-serif;
  --font-tsm02-sans: 'Manrope', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-02 {
  width: 100%;
  min-height: 100svh;
}
```
