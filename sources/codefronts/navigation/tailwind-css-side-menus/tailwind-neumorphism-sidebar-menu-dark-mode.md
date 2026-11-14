---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-neumorphism-sidebar-menu-dark-mode/"
title: "Tailwind Neumorphism Sidebar Menu (Dark Mode)"
section: "navigation"
category: "tailwind-css-side-menus"
category_name: "Tailwind CSS Side Menus"
description: "Soft UI in the dark: links rest flat, extrude on hover and press into the surface when active, using two shadow tokens minted in @theme (shadow-tsm09-out,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neumorphism Sidebar Menu (Dark Mode)
Source: https://codefronts.com/navigation/tailwind-css-side-menus/tailwind-neumorphism-sidebar-menu-dark-mode/

Soft UI in the dark: links rest flat, extrude on hover and press into the surface when active, using two shadow tokens minted in @theme (shadow-tsm09-out, shadow-tsm09-in). The port fixes the illusion-breaking colour mismatch of the original — sidebar, page and cards now share one base tone — and adds the high-contrast focus ring neumorphism always needs.
## HTML
```html
<section class="tsm-09 flex w-full min-h-svh bg-tsm09-bg font-tsm09-sans text-tsm09-ink" aria-label="Neumorphism sidebar menu demo">
  <nav aria-label="Main" class="flex w-56 shrink-0 flex-col py-6 shadow-[inset_-1px_0_0_oklch(1_0_0/0.04),6px_0_18px_oklch(0_0_0/0.35)]">
    <div class="mx-[18px] mb-5 flex items-center gap-3 pb-5 shadow-[0_1px_0_oklch(1_0_0/0.04)]">
      <span aria-hidden="true" class="grid size-[38px] place-items-center rounded-[11px] bg-tsm09-bg text-base font-bold text-tsm09-acc shadow-tsm09-out">N</span>
      <p class="text-sm font-bold">Neura</p>
    </div>
    <ul class="grid gap-2 px-3">
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3.5 text-[13px] font-semibold text-tsm09-mut transition-[color,box-shadow] duration-200 hover:text-tsm09-ink hover:shadow-tsm09-out focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsm09-acc aria-[current=page]:text-tsm09-acc aria-[current=page]:shadow-tsm09-in motion-reduce:transition-none" aria-current="page"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg><span class="flex-1">Dashboard</span><span aria-hidden="true" class="size-[7px] rounded-full bg-tsm09-acc opacity-0 shadow-[0_0_8px_var(--color-tsm09-acc)] transition-opacity group-aria-[current=page]/l:opacity-100"></span></a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3.5 text-[13px] font-semibold text-tsm09-mut transition-[color,box-shadow] duration-200 hover:text-tsm09-ink hover:shadow-tsm09-out focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsm09-acc aria-[current=page]:text-tsm09-acc aria-[current=page]:shadow-tsm09-in motion-reduce:transition-none"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/></svg><span class="flex-1">Analytics</span><span aria-hidden="true" class="size-[7px] rounded-full bg-tsm09-acc opacity-0 shadow-[0_0_8px_var(--color-tsm09-acc)] transition-opacity group-aria-[current=page]/l:opacity-100"></span></a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3.5 text-[13px] font-semibold text-tsm09-mut transition-[color,box-shadow] duration-200 hover:text-tsm09-ink hover:shadow-tsm09-out focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsm09-acc aria-[current=page]:text-tsm09-acc aria-[current=page]:shadow-tsm09-in motion-reduce:transition-none"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg><span class="flex-1">Calendar</span><span aria-hidden="true" class="size-[7px] rounded-full bg-tsm09-acc opacity-0 shadow-[0_0_8px_var(--color-tsm09-acc)] transition-opacity group-aria-[current=page]/l:opacity-100"></span></a></li>
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3.5 text-[13px] font-semibold text-tsm09-mut transition-[color,box-shadow] duration-200 hover:text-tsm09-ink hover:shadow-tsm09-out focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsm09-acc aria-[current=page]:text-tsm09-acc aria-[current=page]:shadow-tsm09-in motion-reduce:transition-none"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg><span class="flex-1">Messages</span><span aria-hidden="true" class="size-[7px] rounded-full bg-tsm09-acc opacity-0 shadow-[0_0_8px_var(--color-tsm09-acc)] transition-opacity group-aria-[current=page]/l:opacity-100"></span></a></li>
      <li aria-hidden="true" class="mx-2 my-1 h-px bg-linear-to-r from-transparent via-white/8 to-transparent"></li>
      <li><a href="#" class="group/l flex min-h-11 items-center gap-3 rounded-xl px-3.5 text-[13px] font-semibold text-tsm09-mut transition-[color,box-shadow] duration-200 hover:text-tsm09-ink hover:shadow-tsm09-out focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsm09-acc aria-[current=page]:text-tsm09-acc aria-[current=page]:shadow-tsm09-in motion-reduce:transition-none"><svg class="size-[18px] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h9"/><path d="M19 6h1"/><circle cx="16" cy="6" r="2.5"/><path d="M4 12h2"/><path d="M12 12h8"/><circle cx="9" cy="12" r="2.5"/><path d="M4 18h11"/><circle cx="18" cy="18" r="2.5"/></svg><span class="flex-1">Settings</span><span aria-hidden="true" class="size-[7px] rounded-full bg-tsm09-acc opacity-0 shadow-[0_0_8px_var(--color-tsm09-acc)] transition-opacity group-aria-[current=page]/l:opacity-100"></span></a></li>
    </ul>
    <div class="mx-3 mt-auto flex items-center gap-2.5 rounded-2xl bg-tsm09-bg p-3.5 shadow-tsm09-in">
      <span aria-hidden="true" class="grid size-8 shrink-0 place-items-center rounded-full bg-linear-135 from-tsm09-acc to-tsm09-acc2 text-xs font-bold text-tsm09-bg shadow-[3px_3px_8px_oklch(0_0_0/0.5)]">PB</span>
      <div><p class="text-xs font-bold">P. Blake</p><p class="text-[10px] text-tsm09-mut">Designer</p></div>
    </div>
  </nav>
  <div class="min-w-0 flex-1 p-6">
    <div class="mx-auto max-w-3xl">
      <h1 class="text-lg font-bold">Dashboard</h1>
      <p class="mt-1.5 mb-6 max-w-prose text-[13px] leading-relaxed text-tsm09-mut text-pretty">Hover a link to raise it; the active page is pressed into the surface. Tab through to see the focus ring neumorphism needs.</p>
      <div class="grid grid-cols-2 gap-4 md:grid-cols-4">
        <div class="rounded-2xl bg-tsm09-bg p-4 shadow-tsm09-out"><p class="text-[22px] font-bold tabular-nums text-tsm09-acc">3,091</p><p class="mt-1 text-[11px] text-tsm09-mut">Sessions</p></div>
        <div class="rounded-2xl bg-tsm09-bg p-4 shadow-tsm09-out"><p class="text-[22px] font-bold tabular-nums text-tsm09-acc">71%</p><p class="mt-1 text-[11px] text-tsm09-mut">Engagement</p></div>
        <div class="rounded-2xl bg-tsm09-bg p-4 shadow-tsm09-out"><p class="text-[22px] font-bold tabular-nums text-tsm09-acc">$6.3k</p><p class="mt-1 text-[11px] text-tsm09-mut">Revenue</p></div>
        <div class="rounded-2xl bg-tsm09-bg p-4 shadow-tsm09-out"><p class="text-[22px] font-bold tabular-nums text-tsm09-acc">521</p><p class="mt-1 text-[11px] text-tsm09-mut">Sign-ups</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsm09-bg: #1e1e35;
  --color-tsm09-bg: oklch(0.247 0.043 282.8);
  --color-tsm09-acc: #8e98fa;
  --color-tsm09-acc: oklch(0.713 0.143 277.7);
  --color-tsm09-acc2: #c084fc;
  --color-tsm09-acc2: oklch(0.722 0.177 305.5);
  --color-tsm09-ink: #e2e8f0;
  --color-tsm09-ink: oklch(0.929 0.013 255.5);
  --color-tsm09-mut: #a3a9c2;
  --color-tsm09-mut: oklch(0.738 0.037 274.8);
  --font-tsm09-sans: 'Poppins', system-ui, sans-serif;
  --shadow-tsm09-out: 5px 5px 12px oklch(0 0 0 / 0.55), -3px -3px 9px oklch(1 0 0 / 0.05);
  --shadow-tsm09-in: inset 4px 4px 9px oklch(0 0 0 / 0.6), inset -3px -3px 8px oklch(1 0 0 / 0.05);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tsm-09 {
  width: 100%;
  min-height: 100svh;
}
```
