---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-collapsible-sidebar-navigation/"
title: "Tailwind CSS Collapsible Sidebar Navigation"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "An admin-dashboard sidebar that collapses from 240px to a 68px icon rail with an edge handle."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Collapsible Sidebar Navigation
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-collapsible-sidebar-navigation/

An admin-dashboard sidebar that collapses from 240px to a 68px icon rail with an edge handle. In rail mode, labels fold away, count badges become notification dots, and hovering an icon shows a tooltip — all from one sr-only checkbox read by group-has-checked/root:. Ships with a dashboard: stat cards and an orders table. Zero JavaScript.
## HTML
```html
<div class="tnv-07 group/root flex min-h-svh w-full bg-tnv07-bg font-tnv07-sans text-tnv07-ink antialiased selection:bg-tnv07-acc selection:text-white">
  <input type="checkbox" id="tnv07-collapse" class="sr-only" aria-label="Collapse sidebar">
  <aside aria-label="Sidebar" class="sticky top-0 z-20 flex h-svh w-60 flex-none flex-col bg-tnv07-side text-white transition-[width] duration-300 ease-[cubic-bezier(.4,0,.2,1)] group-has-checked/root:w-[68px] motion-reduce:transition-none">
    <div class="flex h-16 items-center gap-2.5 border-b border-white/[0.07] px-[18px]">
      <span class="grid size-8 flex-none place-items-center rounded-lg bg-linear-135 from-tnv07-acc to-indigo-500"><svg class="size-4 fill-white" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></span>
      <span class="max-w-40 overflow-hidden font-semibold tracking-[-0.02em] whitespace-nowrap transition-[max-width,opacity] duration-300 group-has-checked/root:max-w-0 group-has-checked/root:opacity-0">Quantum</span>
    </div>
    <label for="tnv07-collapse" title="Toggle sidebar" class="absolute top-5 -right-3 z-30 grid size-6 cursor-pointer place-items-center rounded-full border border-white/10 bg-tnv07-side-2 text-white shadow-lg transition hover:bg-tnv07-acc group-has-[#tnv07-collapse:focus-visible]/root:ring-2 group-has-[#tnv07-collapse:focus-visible]/root:ring-tnv07-acc">
      <svg class="size-3 transition-transform duration-300 group-has-checked/root:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>
    </label>
    <nav class="flex-1 px-2 py-3 [&_[data-label]]:max-w-40 [&_[data-label]]:overflow-hidden [&_[data-label]]:whitespace-nowrap [&_[data-label]]:transition-[max-width,opacity] [&_[data-label]]:duration-300 group-has-checked/root:[&_[data-label]]:max-w-0 group-has-checked/root:[&_[data-label]]:opacity-0 [&_[data-tip]]:pointer-events-none [&_[data-tip]]:absolute [&_[data-tip]]:left-full [&_[data-tip]]:ml-4 [&_[data-tip]]:hidden [&_[data-tip]]:rounded-md [&_[data-tip]]:bg-slate-900 [&_[data-tip]]:px-2.5 [&_[data-tip]]:py-1.5 [&_[data-tip]]:text-xs [&_[data-tip]]:font-semibold [&_[data-tip]]:whitespace-nowrap [&_[data-tip]]:text-white [&_[data-tip]]:opacity-0 [&_[data-tip]]:shadow-xl [&_[data-tip]]:ring-1 [&_[data-tip]]:ring-white/10 [&_[data-tip]]:transition-opacity group-has-checked/root:[&_[data-tip]]:block [&_a:hover_[data-tip]]:opacity-100 [&_a:focus-visible_[data-tip]]:opacity-100 [&_svg]:size-[18px] [&_svg]:flex-none">
      <p class="px-[17px] pt-2 pb-1.5 text-[10px] font-semibold tracking-[0.1em] text-white/45 uppercase transition-opacity group-has-checked/root:opacity-0">Main</p>
      <ul class="space-y-0.5 text-sm font-medium [&_a]:relative [&_a]:flex [&_a]:h-10 [&_a]:items-center [&_a]:gap-3 [&_a]:rounded-lg [&_a]:px-[17px] [&_a]:text-tnv07-side-mut [&_a]:outline-none [&_a]:transition-colors [&_a:hover]:bg-white/[0.06] [&_a:hover]:text-white [&_a:focus-visible]:ring-2 [&_a:focus-visible]:ring-tnv07-acc [&_a[aria-current]]:bg-tnv07-acc/15 [&_a[aria-current]]:text-tnv07-acc">
        <li><a href="#" aria-current="page"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg><span data-label>Dashboard</span><span data-tip aria-hidden="true">Dashboard</span></a></li>
        <li><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg><span data-label>Analytics</span><span class="ml-auto rounded-full bg-tnv07-acc px-1.5 py-px text-[10px] font-bold text-white transition-all group-has-checked/root:absolute group-has-checked/root:top-2 group-has-checked/root:left-[30px] group-has-checked/root:ml-0 group-has-checked/root:size-2 group-has-checked/root:p-0 group-has-checked/root:text-[0px] group-has-checked/root:ring-2 group-has-checked/root:ring-tnv07-side">5</span><span data-tip aria-hidden="true">Analytics · 5 new</span></a></li>
        <li><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg><span data-label>Users</span><span data-tip aria-hidden="true">Users</span></a></li>
        <li><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18M16 10a4 4 0 01-8 0"/></svg><span data-label>Orders</span><span class="ml-auto rounded-full bg-tnv07-acc px-1.5 py-px text-[10px] font-bold text-white transition-all group-has-checked/root:absolute group-has-checked/root:top-2 group-has-checked/root:left-[30px] group-has-checked/root:ml-0 group-has-checked/root:size-2 group-has-checked/root:p-0 group-has-checked/root:text-[0px] group-has-checked/root:ring-2 group-has-checked/root:ring-tnv07-side">12</span><span data-tip aria-hidden="true">Orders · 12 pending</span></a></li>
      </ul>
      <p class="mt-4 px-[17px] pt-2 pb-1.5 text-[10px] font-semibold tracking-[0.1em] text-white/45 uppercase transition-opacity group-has-checked/root:opacity-0">System</p>
      <ul class="space-y-0.5 text-sm font-medium [&_a]:relative [&_a]:flex [&_a]:h-10 [&_a]:items-center [&_a]:gap-3 [&_a]:rounded-lg [&_a]:px-[17px] [&_a]:text-tnv07-side-mut [&_a]:outline-none [&_a]:transition-colors [&_a:hover]:bg-white/[0.06] [&_a:hover]:text-white [&_a:focus-visible]:ring-2 [&_a:focus-visible]:ring-tnv07-acc">
        <li><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 11-2.83 2.83l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 11-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 11-2.83-2.83l.06-.06A1.65 1.65 0 004.6 15a1.65 1.65 0 00-1.51-1H3a2 2 0 110-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 112.83-2.83l.06.06A1.65 1.65 0 009 4.6a1.65 1.65 0 001-1.51V3a2 2 0 114 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 112.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 110 4h-.09a1.65 1.65 0 00-1.51 1z"/></svg><span data-label>Settings</span><span data-tip aria-hidden="true">Settings</span></a></li>
        <li><a href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" aria-hidden="true"><path d="M12 2v6M12 16v6M4.9 4.9l4.2 4.2M14.9 14.9l4.2 4.2M2 12h6M16 12h6"/></svg><span data-label>Integrations</span><span data-tip aria-hidden="true">Integrations</span></a></li>
      </ul>
    </nav>
    <div class="flex items-center gap-2.5 border-t border-white/[0.07] px-[17px] py-3">
      <span class="grid size-[34px] flex-none place-items-center rounded-full bg-linear-135 from-tnv07-acc to-indigo-500 text-xs font-bold">JD</span>
      <span class="max-w-40 overflow-hidden whitespace-nowrap transition-[max-width,opacity] duration-300 group-has-checked/root:max-w-0 group-has-checked/root:opacity-0"><b class="block text-[13px] font-semibold">Jane Doe</b><span class="text-[11px] text-white/55">Admin</span></span>
    </div>
  </aside>
  <main class="min-w-0 flex-1 p-5 sm:p-8">
    <div class="mb-7 flex flex-wrap items-center gap-3 rounded-xl border border-tnv07-line bg-white px-6 py-4">
      <h1 class="font-semibold">Dashboard overview</h1>
      <div class="ml-auto flex gap-2 text-[13px] font-medium text-tnv07-mut [&_button]:h-9 [&_button]:rounded-md [&_button]:border [&_button]:border-tnv07-line [&_button]:bg-tnv07-bg [&_button]:px-3 [&_button]:transition-colors [&_button:hover]:bg-tnv07-line"><button type="button">This month</button><button type="button">Export</button></div>
    </div>
    <div class="mb-6 grid gap-4 sm:grid-cols-3 [&>div]:rounded-xl [&>div]:border [&>div]:border-tnv07-line [&>div]:bg-white [&>div]:px-5 [&>div]:py-5 [&_dt]:text-xs [&_dt]:font-medium [&_dt]:tracking-wide [&_dt]:text-tnv07-mut [&_dt]:uppercase [&_dd]:mt-2 [&_dd]:text-3xl [&_dd]:font-bold [&_dd]:tracking-[-0.03em] [&_small]:mt-1 [&_small]:block [&_small]:text-xs [&_small]:font-semibold [&_small]:text-emerald-700">
      <div><dl><dt>Revenue</dt><dd>$84.2k</dd></dl><small>↑ 12.4% vs last month</small></div>
      <div><dl><dt>Users</dt><dd>4,218</dd></dl><small>↑ 8.1% vs last month</small></div>
      <div><dl><dt>Orders</dt><dd>1,093</dd></dl><small>↑ 5.2% vs last month</small></div>
    </div>
    <div class="overflow-x-auto rounded-xl border border-tnv07-line bg-white">
      <table class="w-full min-w-[32rem] text-left text-sm [&_td]:px-5 [&_td]:py-3.5 [&_th]:px-5 [&_th]:py-3 [&_th]:text-xs [&_th]:font-semibold [&_th]:tracking-wide [&_th]:text-tnv07-mut [&_th]:uppercase [&_tbody_tr]:border-t [&_tbody_tr]:border-tnv07-line [&_tbody_tr]:transition-colors [&_tbody_tr:hover]:bg-tnv07-bg">
        <thead><tr><th>Order</th><th>Amount</th><th>Date</th><th>Status</th></tr></thead>
        <tbody class="font-tnv07-mono text-[13px]">
          <tr><td class="font-tnv07-sans">#1082 · Acme Corp</td><td>$2,400</td><td>Jun 11</td><td><span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-2 py-0.5 font-tnv07-sans text-xs font-semibold text-emerald-700 before:size-1.5 before:rounded-full before:bg-emerald-500 before:content-['']">Paid</span></td></tr>
          <tr><td class="font-tnv07-sans">#1081 · Globex Inc</td><td>$980</td><td>Jun 10</td><td><span class="inline-flex items-center gap-1.5 rounded-full bg-amber-50 px-2 py-0.5 font-tnv07-sans text-xs font-semibold text-amber-700 before:size-1.5 before:rounded-full before:bg-amber-500 before:content-['']">Pending</span></td></tr>
          <tr><td class="font-tnv07-sans">#1080 · Initech</td><td>$3,150</td><td>Jun 9</td><td><span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-2 py-0.5 font-tnv07-sans text-xs font-semibold text-emerald-700 before:size-1.5 before:rounded-full before:bg-emerald-500 before:content-['']">Paid</span></td></tr>
          <tr><td class="font-tnv07-sans">#1079 · Umbrella</td><td>$640</td><td>Jun 8</td><td><span class="inline-flex items-center gap-1.5 rounded-full bg-red-50 px-2 py-0.5 font-tnv07-sans text-xs font-semibold text-red-700 before:size-1.5 before:rounded-full before:bg-red-500 before:content-['']">Failed</span></td></tr>
        </tbody>
      </table>
    </div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv07-bg: #f5f5f4;
  --color-tnv07-bg: oklch(0.97 0.001 106);
  --color-tnv07-line: #e7e5e4;
  --color-tnv07-line: oklch(0.923 0.003 49);
  --color-tnv07-ink: #1c1917;
  --color-tnv07-ink: oklch(0.216 0.006 56);
  --color-tnv07-mut: #57534e;
  --color-tnv07-mut: oklch(0.444 0.011 74);
  --color-tnv07-side: #1e1e2e;
  --color-tnv07-side: oklch(0.24 0.025 285);
  --color-tnv07-side-2: #2a2a3e;
  --color-tnv07-side-2: oklch(0.29 0.03 285);
  --color-tnv07-side-mut: #b9b9c6;
  --color-tnv07-side-mut: oklch(0.79 0.018 285);
  --color-tnv07-acc: #818cf8;
  --color-tnv07-acc: oklch(0.673 0.182 277);
  --font-tnv07-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-tnv07-mono: 'IBM Plex Mono', ui-monospace, monospace;
}

.tnv-07 {
  width: 100%;
  min-height: 100svh;
}
```
