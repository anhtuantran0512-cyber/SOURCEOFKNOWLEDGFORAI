---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-full-height-flexbox-sidebar-layout/"
title: "Tailwind Full-Height Flexbox Sidebar Layout"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "The canonical app layout, done right: a flex flex-col sidebar where the link region takes flex-1 min-h-0 overflow-y-auto, pinning the brand to the top and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Full-Height Flexbox Sidebar Layout
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-full-height-flexbox-sidebar-layout/

The canonical app layout, done right: a flex flex-col sidebar where the link region takes flex-1 min-h-0 overflow-y-auto, pinning the brand to the top and the storage card plus user footer to the bottom — no absolute positioning, and long menus scroll inside the middle region instead of pushing the footer off-screen.
## HTML
```html
<section class="tsm-08 flex w-full min-h-svh bg-tsm08-bg font-tsm08-sans text-tsm08-ink" aria-label="Full-height flexbox sidebar layout demo">
  <nav aria-label="Main" class="sticky top-0 flex h-svh w-60 shrink-0 flex-col self-start bg-tsm08-nav text-tsm08-navink">
    <div class="flex items-center gap-3 border-b border-white/8 px-[18px] py-5">
      <span aria-hidden="true" class="grid size-9 place-items-center rounded-[9px] bg-linear-135 from-tsm08-acc to-tsm08-acc2 text-base font-extrabold">A</span>
      <p class="text-base font-bold">Apex</p>
    </div>
    <div class="min-h-0 flex-1 overflow-y-auto px-2.5 py-3">
      <p class="px-3 pt-3 pb-1 text-[10px] font-bold tracking-[0.14em] text-tsm08-navlbl uppercase">Workspace</p>
      <ul class="grid gap-0.5">
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm08-navmut transition-colors hover:bg-white/7 hover:text-tsm08-navink focus-visible:outline-2 focus-visible:outline-tsm08-acc2 aria-[current=page]:bg-tsm08-acc/30 aria-[current=page]:text-tsm08-navink" aria-current="page"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>Dashboard</a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm08-navmut transition-colors hover:bg-white/7 hover:text-tsm08-navink focus-visible:outline-2 focus-visible:outline-tsm08-acc2 aria-[current=page]:bg-tsm08-acc/30 aria-[current=page]:text-tsm08-navink"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>Projects</a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm08-navmut transition-colors hover:bg-white/7 hover:text-tsm08-navink focus-visible:outline-2 focus-visible:outline-tsm08-acc2 aria-[current=page]:bg-tsm08-acc/30 aria-[current=page]:text-tsm08-navink"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/></svg>Tasks<span class="ml-auto rounded-full bg-tsm08-acc2/20 px-2 py-0.5 text-[10px] font-bold text-tsm08-acc2">14</span></a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm08-navmut transition-colors hover:bg-white/7 hover:text-tsm08-navink focus-visible:outline-2 focus-visible:outline-tsm08-acc2 aria-[current=page]:bg-tsm08-acc/30 aria-[current=page]:text-tsm08-navink"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 13h5l1.5 3h5l1.5-3h5"/><path d="M5.5 5h13L21 13v6H3v-6z"/></svg>Inbox<span class="ml-auto rounded-full bg-tsm08-acc2/20 px-2 py-0.5 text-[10px] font-bold text-tsm08-acc2">6</span></a></li>
      </ul>
      <p class="px-3 pt-3 pb-1 text-[10px] font-bold tracking-[0.14em] text-tsm08-navlbl uppercase">Team</p>
      <ul class="grid gap-0.5">
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm08-navmut transition-colors hover:bg-white/7 hover:text-tsm08-navink focus-visible:outline-2 focus-visible:outline-tsm08-acc2 aria-[current=page]:bg-tsm08-acc/30 aria-[current=page]:text-tsm08-navink"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7"/><path d="M18 14.5a6.5 6.5 0 0 1 3.5 5.5"/></svg>Members</a></li>
        <li><a href="#" class="flex min-h-11 items-center gap-3 rounded-[10px] px-3 text-[13px] font-semibold text-tsm08-navmut transition-colors hover:bg-white/7 hover:text-tsm08-navink focus-visible:outline-2 focus-visible:outline-tsm08-acc2 aria-[current=page]:bg-tsm08-acc/30 aria-[current=page]:text-tsm08-navink"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 4 6v6c0 4.5 3.4 8.3 8 9 4.6-.7 8-4.5 8-9V6z"/></svg>Roles</a></li>
      </ul>
    </div>
    <div class="mx-2.5 mb-3.5 rounded-xl border border-tsm08-acc/30 bg-tsm08-acc/15 p-3.5">
      <div class="flex items-baseline justify-between"><p class="text-[13px] font-bold">Storage</p><p class="text-[11px] tabular-nums text-tsm08-navmut">6.8 / 10 GB</p></div>
      <div role="meter" aria-label="Storage used" aria-valuemin="0" aria-valuemax="100" aria-valuenow="68" class="mt-2.5 h-1.5 overflow-hidden rounded-full bg-white/10"><div class="h-full w-[68%] rounded-full bg-linear-to-r from-tsm08-acc to-tsm08-acc2"></div></div>
      <a href="#" class="mt-2.5 inline-flex min-h-8 items-center text-[11px] font-semibold text-tsm08-acc2 underline-offset-2 hover:underline focus-visible:outline-2 focus-visible:outline-tsm08-acc2">Upgrade for unlimited storage</a>
    </div>
    <div class="flex items-center gap-2.5 border-t border-white/8 px-[18px] py-3.5">
      <span aria-hidden="true" class="grid size-[34px] shrink-0 place-items-center rounded-full bg-linear-135 from-amber-500 to-red-500 text-xs font-bold">TN</span>
      <div class="min-w-0"><p class="text-[13px] font-bold">Tom N.</p><p class="text-[11px] text-tsm08-acc2">Pro plan</p></div>
      <button type="button" class="ml-auto grid size-11 place-items-center rounded-lg text-tsm08-navmut transition-colors hover:bg-white/10 hover:text-tsm08-navink focus-visible:outline-2 focus-visible:outline-tsm08-acc2"><span class="sr-only">Sign out</span><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h4a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-4"/><path d="m9 8-4 4 4 4"/><path d="M5 12h11"/></svg></button>
    </div>
  </nav>
  <div class="flex min-w-0 flex-1 flex-col">
    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-tsm08-line px-6 py-4">
      <h1 class="text-lg font-extrabold">Dashboard</h1>
      <div class="flex gap-2">
        <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-lg border border-tsm08-line bg-transparent px-4 text-[13px] font-bold transition-colors hover:bg-tsm08-line/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsm08-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11"/><path d="m7 10 5 5 5-5"/><path d="M5 20h14"/></svg>Export</button>
        <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-lg bg-tsm08-acc px-4 text-[13px] font-bold text-white transition-colors hover:bg-tsm08-acc/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsm08-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>New project</button>
      </div>
    </div>
    <div class="mx-auto w-full max-w-3xl flex-1 p-6">
      <p class="mb-5 max-w-prose text-[13px] leading-relaxed text-tsm08-mut text-pretty">The sidebar is one flex column: brand on top, a <code class="rounded bg-tsm08-line px-1">flex-1 min-h-0</code> link region that scrolls, and storage plus profile pinned to the bottom — no absolute positioning.</p>
      <div class="grid grid-cols-2 gap-3 md:grid-cols-4">
          <div class="rounded-xl border border-tsm08-line bg-tsm08-surface p-4 shadow-[0_1px_3px_oklch(0.2_0.01_60/0.06)]"><p class="text-2xl font-extrabold tabular-nums text-tsm08-acc">28</p><p class="mt-1 text-xs text-tsm08-mut">Active projects</p></div>
          <div class="rounded-xl border border-tsm08-line bg-tsm08-surface p-4 shadow-[0_1px_3px_oklch(0.2_0.01_60/0.06)]"><p class="text-2xl font-extrabold tabular-nums text-tsm08-acc">142</p><p class="mt-1 text-xs text-tsm08-mut">Open tasks</p></div>
          <div class="rounded-xl border border-tsm08-line bg-tsm08-surface p-4 shadow-[0_1px_3px_oklch(0.2_0.01_60/0.06)]"><p class="text-2xl font-extrabold tabular-nums text-tsm08-acc">7</p><p class="mt-1 text-xs text-tsm08-mut">Team members</p></div>
          <div class="rounded-xl border border-tsm08-line bg-tsm08-surface p-4 shadow-[0_1px_3px_oklch(0.2_0.01_60/0.06)]"><p class="text-2xl font-extrabold tabular-nums text-tsm08-acc">99%</p><p class="mt-1 text-xs text-tsm08-mut">SLA</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm08-bg: #fafaf9;
  --color-tsm08-bg: oklch(0.985 0.001 0);
  --color-tsm08-surface: #ffffff;
  --color-tsm08-surface: oklch(1 0 0);
  --color-tsm08-line: #e7e5e4;
  --color-tsm08-line: oklch(0.923 0.003 48.7);
  --color-tsm08-nav: #1c1917;
  --color-tsm08-nav: oklch(0.216 0.006 56);
  --color-tsm08-navink: #fafaf9;
  --color-tsm08-navink: oklch(0.985 0.001 0);
  --color-tsm08-navmut: #b5afaa;
  --color-tsm08-navmut: oklch(0.758 0.01 62.5);
  --color-tsm08-navlbl: #8f8984;
  --color-tsm08-navlbl: oklch(0.634 0.01 62.5);
  --color-tsm08-acc: #7c3aed;
  --color-tsm08-acc: oklch(0.541 0.247 293);
  --color-tsm08-acc2: #b49cfc;
  --color-tsm08-acc2: oklch(0.751 0.137 294.4);
  --color-tsm08-ink: #1c1917;
  --color-tsm08-ink: oklch(0.216 0.006 56);
  --color-tsm08-mut: #57534e;
  --color-tsm08-mut: oklch(0.444 0.01 73.6);
  --font-tsm08-sans: 'Outfit', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-08 {
  width: 100%;
  min-height: 100svh;
}
```
