---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-sidebar-drawer-opens-on-hover/"
title: "Tailwind Sidebar Drawer That Opens on Hover"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "A thin teal edge strip that slides a full navigation drawer out when you hover it — and, in this port, when you Tab to it or tap it on a touchscreen."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar Drawer That Opens on Hover
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-sidebar-drawer-opens-on-hover/

A thin teal edge strip that slides a full navigation drawer out when you hover it — and, in this port, when you Tab to it or tap it on a touchscreen. A 200ms grace delay on close (and none on open) stops the drawer snapping shut when the pointer wobbles off its edge. Pure Tailwind, no checkbox.
## HTML
```html
<section class="tsm-14 relative flex w-full min-h-svh bg-tsm14-bg font-tsm14-sans text-tsm14-ink" aria-label="Sidebar drawer that opens on hover demo">
  <div data-tsm14-drawer class="group/drawer absolute inset-y-0 left-0 z-20 flex">
    <button type="button" aria-label="Open navigation" class="relative z-10 grid w-8 cursor-pointer place-items-center border-r border-tsm14-acc/35 bg-tsm14-trig text-tsm14-acc2 shadow-[1px_0_12px_oklch(0.7_0.12_180/0.08)] transition-colors hover:bg-tsm14-acc/10 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsm14-acc2">
      <svg class="size-5 drop-shadow-[0_0_6px_oklch(0.7_0.12_180/0.5)] transition-transform duration-300 group-hover/drawer:rotate-180 group-focus-within/drawer:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>
    </button>
    <nav aria-label="Main" class="invisible absolute inset-y-0 left-8 flex w-60 -translate-x-full flex-col border-r border-tsm14-acc/15 bg-tsm14-surface py-6 transition-[translate,visibility,box-shadow] delay-200 duration-400 ease-[cubic-bezier(0.4,0,0.2,1)] after:absolute after:inset-y-0 after:right-0 after:w-px after:bg-linear-to-b after:from-transparent after:via-tsm14-acc after:to-transparent after:opacity-50 group-hover/drawer:visible group-hover/drawer:translate-x-0 group-hover/drawer:shadow-[8px_0_40px_oklch(0_0_0/0.5)] group-hover/drawer:delay-0 group-focus-within/drawer:visible group-focus-within/drawer:translate-x-0 group-focus-within/drawer:delay-0 motion-reduce:transition-none">
      <div class="mx-[18px] mb-4 flex items-center gap-2.5 border-b border-tsm14-acc/15 pb-[18px]">
        <span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-linear-135 from-tsm14-acc to-tsm14-acc2 text-sm font-extrabold text-black">T</span>
        <p class="text-[15px] font-extrabold">Tidal</p>
      </div>
      <ul class="grid flex-1 content-start gap-1 px-2.5">
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-[13px] font-bold whitespace-nowrap text-tsm14-mut transition-colors hover:bg-tsm14-acc/10 hover:text-tsm14-ink focus-visible:outline-2 focus-visible:outline-tsm14-acc2 aria-[current=page]:bg-tsm14-acc/12 aria-[current=page]:text-tsm14-acc2" aria-current="page"><svg class="size-[17px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>Overview</a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-[13px] font-bold whitespace-nowrap text-tsm14-mut transition-colors hover:bg-tsm14-acc/10 hover:text-tsm14-ink focus-visible:outline-2 focus-visible:outline-tsm14-acc2 aria-[current=page]:bg-tsm14-acc/12 aria-[current=page]:text-tsm14-acc2"><svg class="size-[17px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="2"/><path d="M7.8 7.8a6 6 0 0 0 0 8.4M16.2 16.2a6 6 0 0 0 0-8.4"/><path d="M4.9 4.9a10 10 0 0 0 0 14.2M19.1 19.1a10 10 0 0 0 0-14.2"/></svg>Streams</a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-[13px] font-bold whitespace-nowrap text-tsm14-mut transition-colors hover:bg-tsm14-acc/10 hover:text-tsm14-ink focus-visible:outline-2 focus-visible:outline-tsm14-acc2 aria-[current=page]:bg-tsm14-acc/12 aria-[current=page]:text-tsm14-acc2"><svg class="size-[17px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 9h14M5 15h14M10 4 8 20M16 4l-2 16"/></svg>Channels<span class="ml-auto rounded-full bg-tsm14-acc/20 px-2 py-0.5 text-[10px] font-extrabold text-tsm14-acc2">8</span></a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-[13px] font-bold whitespace-nowrap text-tsm14-mut transition-colors hover:bg-tsm14-acc/10 hover:text-tsm14-ink focus-visible:outline-2 focus-visible:outline-tsm14-acc2 aria-[current=page]:bg-tsm14-acc/12 aria-[current=page]:text-tsm14-acc2"><svg class="size-[17px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 16v-5a6 6 0 1 1 12 0v5l2 2H4z"/><path d="M10 21h4"/></svg>Alerts<span class="ml-auto rounded-full bg-tsm14-acc/20 px-2 py-0.5 text-[10px] font-extrabold text-tsm14-acc2">2</span></a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3.5 text-[13px] font-bold whitespace-nowrap text-tsm14-mut transition-colors hover:bg-tsm14-acc/10 hover:text-tsm14-ink focus-visible:outline-2 focus-visible:outline-tsm14-acc2 aria-[current=page]:bg-tsm14-acc/12 aria-[current=page]:text-tsm14-acc2"><svg class="size-[17px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg>Settings</a></li>
      </ul>
      <div class="mx-[18px] flex items-center gap-2.5 border-t border-tsm14-acc/15 pt-3.5">
        <span aria-hidden="true" class="grid size-[30px] place-items-center rounded-full bg-linear-135 from-tsm14-acc to-indigo-500 text-[11px] font-bold text-white">RJ</span>
        <div><p class="text-xs font-extrabold">R. Jensen</p><p class="text-[10px] text-tsm14-mut">Operator</p></div>
      </div>
    </nav>
  </div>
  <div class="min-w-0 flex-1 py-6 pr-6 pl-14">
    <div class="mx-auto max-w-3xl">
      <h1 class="text-xl font-extrabold">Hover drawer</h1>
      <p class="mt-1.5 mb-5 max-w-prose text-[13px] leading-relaxed text-tsm14-mut text-pretty">A slide-out sidebar triggered by the edge strip — hover it, Tab to it, or tap it. No checkbox and no JavaScript.</p>
      <p class="mb-5 flex items-center gap-2.5 rounded-[10px] border border-tsm14-acc/20 bg-tsm14-acc/8 px-3.5 py-3 text-[13px] font-semibold text-tsm14-acc2"><svg class="size-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 6-6 6 6 6"/></svg>Hover the teal strip on the left to open the menu</p>
      <div class="grid grid-cols-2 gap-2.5 md:grid-cols-4">
        <div class="rounded-xl border border-tsm14-acc/15 bg-tsm14-surface p-4"><p class="text-xl font-extrabold tabular-nums text-tsm14-acc2">4.1k</p><p class="mt-1 text-[11px] text-tsm14-mut">Events / sec</p></div>
        <div class="rounded-xl border border-tsm14-acc/15 bg-tsm14-surface p-4"><p class="text-xl font-extrabold tabular-nums text-tsm14-acc2">8</p><p class="mt-1 text-[11px] text-tsm14-mut">Active streams</p></div>
        <div class="rounded-xl border border-tsm14-acc/15 bg-tsm14-surface p-4"><p class="text-xl font-extrabold tabular-nums text-tsm14-acc2">0</p><p class="mt-1 text-[11px] text-tsm14-mut">Alerts</p></div>
        <div class="rounded-xl border border-tsm14-acc/15 bg-tsm14-surface p-4"><p class="text-xl font-extrabold tabular-nums text-tsm14-acc2">99.8%</p><p class="mt-1 text-[11px] text-tsm14-mut">Uptime</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm14-bg: #0a1628;
  --color-tsm14-bg: oklch(0.2 0.04 258.3);
  --color-tsm14-surface: #0f1f35;
  --color-tsm14-surface: oklch(0.238 0.048 256.7);
  --color-tsm14-trig: #071020;
  --color-tsm14-trig: oklch(0.174 0.036 260.6);
  --color-tsm14-acc: #14b8a6;
  --color-tsm14-acc: oklch(0.704 0.123 182.5);
  --color-tsm14-acc2: #2dd4bf;
  --color-tsm14-acc2: oklch(0.785 0.133 181.9);
  --color-tsm14-ink: #e2e8f0;
  --color-tsm14-ink: oklch(0.929 0.013 255.5);
  --color-tsm14-mut: #9db0c4;
  --color-tsm14-mut: oklch(0.749 0.036 249.7);
  --font-tsm14-sans: 'Mulish', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-14 {
  width: 100%;
  min-height: 100svh;
}
```
