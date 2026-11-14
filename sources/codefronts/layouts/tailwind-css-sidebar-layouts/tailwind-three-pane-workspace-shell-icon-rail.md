---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-three-pane-workspace-shell-icon-rail/"
title: "Tailwind Three-Pane Workspace Shell with Icon Rail and List"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The Slack/IDE archetype, assembled from this collection's parts: the 68px icon rail from demo 14, the sticky-search list from demo 21, and demo 09's…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Three-Pane Workspace Shell with Icon Rail and List
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-three-pane-workspace-shell-icon-rail/

The Slack/IDE archetype, assembled from this collection's parts: the 68px icon rail from demo 14, the sticky-search list from demo 21, and demo 09's independent scroller as the body. One grid declaration composes them, and panes drop by priority as space runs out.
## HTML
```html
<section class="tsl-28 w-full h-svh min-h-svh grid grid-cols-[68px_264px_minmax(0,1fr)] max-[1000px]:grid-cols-[68px_220px_minmax(0,1fr)] max-[820px]:grid-cols-[68px_minmax(0,1fr)] font-tsl28-sans bg-tsl28-bg text-tsl28-ink">
  <aside aria-label="Apps" class="flex flex-col items-center gap-2 py-3.5 bg-tsl28-dock border-r border-tsl28-line">
    <span aria-hidden="true" class="w-[30px] h-[30px] mb-2.5 rounded-[9px] bg-[conic-gradient(from_30deg,var(--color-tsl28-accent),oklch(0.62_0.16_320))]"></span>
    <a href="#" aria-current="page" aria-label="Messages" class="grid place-items-center w-11 h-11 rounded-xl text-tsl28-mut transition-colors duration-200 hover:text-tsl28-ink aria-[current=page]:text-tsl28-accent aria-[current=page]:bg-tsl28-tint focus-visible:outline-2 focus-visible:outline-tsl28-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-5 h-5 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M21 12a8 8 0 0 1-8 8H4l2.5-2.5A8 8 0 1 1 21 12z"/></svg></a>
    <a href="#" aria-label="Calendar" class="grid place-items-center w-11 h-11 rounded-xl text-tsl28-mut transition-colors duration-200 hover:text-tsl28-ink focus-visible:outline-2 focus-visible:outline-tsl28-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-5 h-5 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="M3 9h18M8 2v4m8-4v4"/></svg></a>
    <a href="#" aria-label="Tasks" class="grid place-items-center w-11 h-11 rounded-xl text-tsl28-mut transition-colors duration-200 hover:text-tsl28-ink focus-visible:outline-2 focus-visible:outline-tsl28-accent focus-visible:outline-offset-2"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-5 h-5 fill-none stroke-current stroke-[1.8] [stroke-linecap:round] [stroke-linejoin:round]"><path d="m4 12 4 4L20 4M4 19h16"/></svg></a>
    <span aria-hidden="true" class="mt-auto grid place-items-center w-11 h-11 rounded-full text-[11px] font-bold text-white bg-[linear-gradient(135deg,var(--color-tsl28-accent),oklch(0.58_0.16_320))]">JV</span>
  </aside>
  <aside aria-label="Conversations" class="max-[820px]:hidden bg-tsl28-panel border-r border-tsl28-line overflow-y-auto overscroll-contain">
    <div class="sticky top-0 z-[2] p-3 bg-tsl28-panel border-b border-tsl28-line">
      <label class="grid grid-cols-[auto_1fr] items-center gap-2 h-11 px-3 rounded-[10px] border border-tsl28-line bg-tsl28-well focus-within:border-tsl28-accent focus-within:shadow-[0_0_0_3px_var(--color-tsl28-ring)]"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-3.5 h-3.5 fill-none stroke-tsl28-mut stroke-2 [stroke-linecap:round]"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input type="search" placeholder="Search&hellip;" aria-label="Search conversations" class="min-w-0 border-0 bg-transparent text-tsl28-ink text-[13px] outline-none placeholder:text-tsl28-placeholder"></label>
    </div>
    <a href="#" aria-current="true" class="group grid gap-[3px] px-3.5 py-3 border-b border-tsl28-hairline no-underline text-inherit transition-colors duration-150 hover:bg-tsl28-rowhover aria-[current=true]:bg-tsl28-tint aria-[current=true]:shadow-[inset_2.5px_0_0_var(--color-tsl28-accent)] focus-visible:outline-2 focus-visible:outline-tsl28-accent focus-visible:-outline-offset-2"><strong class="flex items-center gap-[7px] text-[13px] font-semibold leading-tight"># frontend-guild</strong><em class="not-italic text-xs leading-snug text-tsl28-mut truncate">Priya: subgrid landed in the design sys&hellip;</em></a>
    <a href="#" data-unread class="group grid gap-[3px] px-3.5 py-3 border-b border-tsl28-hairline no-underline text-inherit transition-colors duration-150 hover:bg-tsl28-rowhover focus-visible:outline-2 focus-visible:outline-tsl28-accent focus-visible:-outline-offset-2"><strong class="flex items-center gap-[7px] text-[13px] font-semibold leading-tight"># releases<i aria-hidden="true" class="hidden group-data-unread:block w-[7px] h-[7px] rounded-full bg-tsl28-accent"></i></strong><em class="not-italic text-xs leading-snug text-tsl28-mut truncate">Deploy 4.2.0 is live in production</em></a>
    <a href="#" class="group grid gap-[3px] px-3.5 py-3 border-b border-tsl28-hairline no-underline text-inherit transition-colors duration-150 hover:bg-tsl28-rowhover focus-visible:outline-2 focus-visible:outline-tsl28-accent focus-visible:-outline-offset-2"><strong class="flex items-center gap-[7px] text-[13px] font-semibold leading-tight">Marcus Webb</strong><em class="not-italic text-xs leading-snug text-tsl28-mut truncate">You: sounds good, ship it</em></a>
    <a href="#" class="group grid gap-[3px] px-3.5 py-3 border-b border-tsl28-hairline no-underline text-inherit transition-colors duration-150 hover:bg-tsl28-rowhover focus-visible:outline-2 focus-visible:outline-tsl28-accent focus-visible:-outline-offset-2"><strong class="flex items-center gap-[7px] text-[13px] font-semibold leading-tight"># design-crit</strong><em class="not-italic text-xs leading-snug text-tsl28-mut truncate">Amara: posting Thursday's agenda</em></a>
  </aside>
  <main class="grid grid-rows-[auto_1fr_auto] min-w-0">
    <header class="flex items-baseline gap-3 px-5 py-4 border-b border-tsl28-line text-[14.5px] font-bold"># frontend-guild<span class="text-xs font-normal text-tsl28-mut">128 members</span></header>
    <div class="overflow-y-auto overscroll-contain px-5 py-[18px] grid gap-3.5 content-start">
      <p class="max-w-[64ch] text-[13.5px] leading-[1.55] text-tsl28-mut"><b class="mr-1.5 font-bold text-tsl28-ink">Priya</b>subgrid landed in the design system &mdash; sidebar badges finally align. <time class="ml-2 text-[11px] text-tsl28-faint">09:12</time></p>
      <p class="max-w-[64ch] text-[13.5px] leading-[1.55] text-tsl28-mut"><b class="mr-1.5 font-bold text-tsl28-ink">You</b>demo 05 energy. Shipping the workspace shell next. <time class="ml-2 text-[11px] text-tsl28-faint">09:15</time></p>
    </div>
    <div class="grid grid-cols-[1fr_auto] gap-2.5 px-5 py-3.5 border-t border-tsl28-line">
      <input type="text" placeholder="Message # frontend-guild" aria-label="Message input" class="h-11 px-3.5 rounded-[11px] border border-tsl28-line bg-tsl28-panel text-tsl28-ink text-[13.5px] outline-none placeholder:text-tsl28-placeholder focus-visible:border-tsl28-accent focus-visible:shadow-[0_0_0_3px_var(--color-tsl28-ring)]">
      <button type="button" class="min-h-11 px-[18px] rounded-[11px] border-0 bg-tsl28-accent text-white text-[13px] font-semibold cursor-pointer transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tsl28-accent focus-visible:outline-offset-2">Send</button>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl28-bg: #121319;
  --color-tsl28-bg: oklch(0.13 0.014 265);
  --color-tsl28-dock: #14151d;
  --color-tsl28-dock: oklch(0.14 0.02 265);
  --color-tsl28-panel: #1b1d26;
  --color-tsl28-panel: oklch(0.17 0.018 265);
  --color-tsl28-well: #16171f;
  --color-tsl28-well: oklch(0.14 0.015 265);
  --color-tsl28-ink: #eaebf0;
  --color-tsl28-ink: oklch(0.94 0.005 265);
  --color-tsl28-mut: #93959f;
  --color-tsl28-mut: oklch(0.63 0.013 265);
  --color-tsl28-faint: #74767f;
  --color-tsl28-faint: oklch(0.52 0.012 265);
  --color-tsl28-placeholder: #7f818b;
  --color-tsl28-placeholder: oklch(0.56 0.013 265);
  --color-tsl28-line: #383a45;
  --color-tsl28-line: oklch(0.28 0.018 265);
  --color-tsl28-hairline: rgb(56 58 69 / 0.55);
  --color-tsl28-hairline: color-mix(in oklab, oklch(0.28 0.018 265) 55%, transparent);
  --color-tsl28-accent: #8c7ae8;
  --color-tsl28-accent: oklch(0.7 0.15 265);
  --color-tsl28-tint: rgb(140 122 232 / 0.15);
  --color-tsl28-tint: color-mix(in oklab, oklch(0.7 0.15 265) 15%, transparent);
  --color-tsl28-ring: rgb(140 122 232 / 0.2);
  --color-tsl28-ring: color-mix(in oklab, oklch(0.7 0.15 265) 20%, transparent);
  --color-tsl28-rowhover: rgb(234 235 240 / 0.04);
  --color-tsl28-rowhover: color-mix(in oklab, oklch(0.94 0.005 265) 4%, transparent);
  --font-tsl28-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-28 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
