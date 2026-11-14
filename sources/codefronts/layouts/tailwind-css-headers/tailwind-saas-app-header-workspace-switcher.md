---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-saas-app-header-workspace-switcher/"
title: "Tailwind SaaS App Header with Workspace Switcher"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "The chrome that wraps a multi-tenant product: a workspace picker showing the tenant's avatar, plan and seats; section nav; a toolbar of search, help and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind SaaS App Header with Workspace Switcher
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-saas-app-header-workspace-switcher/

The chrome that wraps a multi-tenant product: a workspace picker showing the tenant's avatar, plan and seats; section nav; a toolbar of search, help and notifications; and an account menu. Both menus open on group-hover and group-focus-within, and the active workspace is marked with aria-[current=true]:.
## HTML
```html
<div class="thd-03 group/thd03 w-full min-h-svh bg-thd03-bg font-thd03-sans text-thd03-ink antialiased">
  <a href="#thd-03-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd03-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <header class="sticky top-0 z-40 flex h-[60px] items-center gap-2 border-b border-thd03-line bg-thd03-panel px-3 sm:gap-4 sm:px-5">
    <div class="group/ws relative min-w-0">
      <button type="button" aria-haspopup="menu" class="flex min-h-11 min-w-0 items-center gap-2.5 rounded-xl py-1 pl-1 pr-2 text-left transition-colors hover:bg-thd03-ink/5">
        <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-lg bg-gradient-to-br from-indigo-500 to-violet-600 text-xs font-extrabold text-white">NW</span>
        <span class="hidden min-w-0 leading-tight sm:block"><span class="block truncate text-sm font-bold">Northwind Labs</span><span class="block truncate text-xs text-thd03-mut">Pro &middot; 24 seats</span></span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" class="size-4 flex-none text-thd03-mut"><path d="m8 10 4-4 4 4M8 14l4 4 4-4"/></svg>
      </button>
      <div role="menu" aria-label="Switch workspace" class="invisible absolute left-0 top-full z-50 mt-2 w-72 translate-y-1 rounded-2xl border border-thd03-line bg-thd03-panel p-2 opacity-0 shadow-[0_24px_60px_-24px_rgb(15_23_42/.4)] transition-[opacity,translate,visibility] duration-150 before:absolute before:inset-x-0 before:-top-2 before:h-2 before:content-[''] group-hover/ws:visible group-hover/ws:translate-y-0 group-hover/ws:opacity-100 group-focus-within/ws:visible group-focus-within/ws:translate-y-0 group-focus-within/ws:opacity-100">
        <p class="px-2.5 pb-1.5 pt-1 text-[11px] font-bold uppercase tracking-[.1em] text-thd03-mut">Workspaces</p>
        <a role="menuitem" href="#thd-03-main" aria-current="true" class="group/item flex min-h-11 items-center gap-3 rounded-lg px-2.5 text-sm hover:bg-thd03-ink/5 focus-visible:bg-thd03-ink/5 aria-[current=true]:bg-thd03-acc/10 aria-[current=true]:font-semibold"><span aria-hidden="true" class="grid size-7 place-items-center rounded-md bg-gradient-to-br from-indigo-500 to-violet-600 text-[10px] font-extrabold text-white">NW</span><span class="min-w-0 flex-1 truncate">Northwind Labs</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="hidden size-4 text-thd03-acc group-aria-[current=true]/item:block"><path d="m5 12 4.5 4.5L19 7"/></svg></a>
        <a role="menuitem" href="#thd-03-main" class="group/item flex min-h-11 items-center gap-3 rounded-lg px-2.5 text-sm hover:bg-thd03-ink/5 focus-visible:bg-thd03-ink/5"><span aria-hidden="true" class="grid size-7 place-items-center rounded-md bg-amber-500 text-[10px] font-extrabold text-white">AT</span><span class="min-w-0 flex-1 truncate">Atlas Freight</span></a>
        <a role="menuitem" href="#thd-03-main" class="group/item flex min-h-11 items-center gap-3 rounded-lg px-2.5 text-sm hover:bg-thd03-ink/5 focus-visible:bg-thd03-ink/5"><span aria-hidden="true" class="grid size-7 place-items-center rounded-md bg-emerald-600 text-[10px] font-extrabold text-white">FD</span><span class="min-w-0 flex-1 truncate">Foundry Design Co</span></a>
        <a role="menuitem" href="#thd-03-main" class="group/item flex min-h-11 items-center gap-3 rounded-lg px-2.5 text-sm hover:bg-thd03-ink/5 focus-visible:bg-thd03-ink/5"><span aria-hidden="true" class="grid size-7 place-items-center rounded-md bg-rose-500 text-[10px] font-extrabold text-white">HL</span><span class="min-w-0 flex-1 truncate">Halcyon Internal</span></a>
        <a role="menuitem" href="#thd-03-main" class="mt-1.5 flex min-h-11 items-center gap-3 rounded-lg border-t border-thd03-line px-2.5 pt-1.5 text-sm font-semibold text-thd03-acc hover:bg-thd03-ink/5 focus-visible:bg-thd03-ink/5"><span aria-hidden="true" class="grid size-7 place-items-center rounded-md border border-dashed border-thd03-acc/60"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" class="size-3.5"><path d="M12 5v14M5 12h14"/></svg></span>Create workspace</a>
      </div>
    </div>
    <span aria-hidden="true" class="hidden h-6 w-px bg-thd03-line md:block"></span>
    <nav aria-label="Sections" class="hidden md:block">
      <ul class="flex items-center gap-1 text-sm font-semibold">
        <li><a href="#thd-03-main" aria-current="page" class="relative block rounded-lg px-3 py-2 text-thd03-mut hover:bg-thd03-ink/5 hover:text-thd03-ink aria-[current=page]:text-thd03-ink aria-[current=page]:after:absolute aria-[current=page]:after:inset-x-3 aria-[current=page]:after:-bottom-[13px] aria-[current=page]:after:h-0.5 aria-[current=page]:after:rounded-full aria-[current=page]:after:bg-thd03-acc aria-[current=page]:after:content-['']">Overview</a></li>
        <li><a href="#thd-03-main" class="block rounded-lg px-3 py-2 text-thd03-mut hover:bg-thd03-ink/5 hover:text-thd03-ink">Projects</a></li>
        <li><a href="#thd-03-main" class="block rounded-lg px-3 py-2 text-thd03-mut hover:bg-thd03-ink/5 hover:text-thd03-ink">Insights</a></li>
        <li><a href="#thd-03-main" class="block rounded-lg px-3 py-2 text-thd03-mut hover:bg-thd03-ink/5 hover:text-thd03-ink">Billing</a></li>
      </ul>
    </nav>
    <div class="ml-auto flex items-center gap-0.5">
      <input id="thd-03-t" type="checkbox" class="peer/t sr-only">
      <label for="thd-03-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-thd03-mut hover:bg-thd03-ink/5 hover:text-thd03-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd03-acc">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-03-t:checked]/thd03:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-03-t:checked]/thd03:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
        <span class="sr-only">Switch light or dark theme</span>
      </label>
      <button type="button" aria-label="Search" class="hidden size-11 place-items-center rounded-full text-thd03-mut hover:bg-thd03-ink/5 hover:text-thd03-ink sm:grid"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px]"><circle cx="11" cy="11" r="6.4"/><path d="m15.8 15.8 5.2 5.2"/></svg></button>
      <button type="button" aria-label="Notifications, 2 unread" class="relative grid size-11 place-items-center rounded-full text-thd03-mut hover:bg-thd03-ink/5 hover:text-thd03-ink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="size-[18px]"><path d="M6 16v-5a6 6 0 0 1 12 0v5l1.5 2h-15L6 16Z"/><path d="M10 20.5a2 2 0 0 0 4 0"/></svg><span aria-hidden="true" class="absolute right-2.5 top-2.5 size-2 rounded-full bg-rose-500 ring-2 ring-thd03-panel"></span></button>
      <div class="group/acct relative ml-1">
        <button type="button" aria-haspopup="menu" aria-label="Account menu for Alex Chen" class="grid size-11 place-items-center rounded-full"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-thd03-acc text-xs font-bold text-white ring-2 ring-thd03-panel ring-offset-2 ring-offset-thd03-acc/30 transition group-hover/acct:ring-offset-thd03-acc">AC</span></button>
        <div role="menu" aria-label="Account" class="invisible absolute right-0 top-full z-50 mt-2 w-64 translate-y-1 rounded-2xl border border-thd03-line bg-thd03-panel p-2 opacity-0 shadow-[0_24px_60px_-24px_rgb(15_23_42/.4)] transition-[opacity,translate,visibility] duration-150 before:absolute before:inset-x-0 before:-top-2 before:h-2 before:content-[''] group-hover/acct:visible group-hover/acct:translate-y-0 group-hover/acct:opacity-100 group-focus-within/acct:visible group-focus-within/acct:translate-y-0 group-focus-within/acct:opacity-100">
          <p class="border-b border-thd03-line px-2.5 pb-2.5 pt-1.5 text-sm"><span class="block font-bold">Alex Chen</span><span class="block truncate text-thd03-mut">[email protected]</span></p>
          <a role="menuitem" href="#thd-03-main" class="mt-1 flex min-h-10 items-center rounded-lg px-2.5 text-sm hover:bg-thd03-ink/5 focus-visible:bg-thd03-ink/5">Profile</a>
          <a role="menuitem" href="#thd-03-main" class="flex min-h-10 items-center justify-between rounded-lg px-2.5 text-sm hover:bg-thd03-ink/5 focus-visible:bg-thd03-ink/5">Preferences <kbd class="rounded border border-thd03-line px-1.5 text-[11px] text-thd03-mut">&#8984;,</kbd></a>
          <a role="menuitem" href="#thd-03-main" class="flex min-h-10 items-center rounded-lg px-2.5 text-sm hover:bg-thd03-ink/5 focus-visible:bg-thd03-ink/5">Members and roles</a>
          <a role="menuitem" href="#thd-03-main" class="mt-1 flex min-h-10 items-center rounded-lg border-t border-thd03-line px-2.5 text-sm text-rose-600 hover:bg-rose-500/10 focus-visible:bg-rose-500/10">Sign out</a>
        </div>
      </div>
    </div>
  </header>
  <main id="thd-03-main" class="mx-auto max-w-6xl px-[clamp(1rem,4vw,2rem)] py-10">
    <div class="flex flex-wrap items-end justify-between gap-4">
      <div><p class="text-sm font-semibold text-thd03-mut">Northwind Labs</p><h1 class="mt-1 text-[clamp(1.6rem,4vw,2.2rem)] font-extrabold tracking-tight">Overview</h1></div>
      <p class="rounded-full border border-thd03-line bg-thd03-panel px-3 py-1.5 text-xs font-semibold text-thd03-mut">Last 30 days</p>
    </div>
    <ul class="mt-6 grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-3">
      <li class="rounded-2xl border border-thd03-line bg-thd03-panel p-5"><p class="text-sm text-thd03-mut">Active projects</p><p class="mt-2 text-3xl font-extrabold tabular-nums">38</p><p class="mt-1 text-xs font-semibold text-emerald-600">+4 this month</p></li>
      <li class="rounded-2xl border border-thd03-line bg-thd03-panel p-5"><p class="text-sm text-thd03-mut">Seats used</p><p class="mt-2 text-3xl font-extrabold tabular-nums">21<span class="text-lg text-thd03-mut">/24</span></p><div class="mt-3 h-1.5 rounded-full bg-thd03-ink/8"><div class="h-full w-[87%] rounded-full bg-thd03-acc"></div></div></li>
      <li class="rounded-2xl border border-thd03-line bg-thd03-panel p-5"><p class="text-sm text-thd03-mut">Invoices due</p><p class="mt-2 text-3xl font-extrabold tabular-nums">$4,280</p><p class="mt-1 text-xs text-thd03-mut">Next run 1 Oct</p></li>
    </ul>
    <div aria-hidden="true" class="h-[60svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd03-bg: var(--thd03-bg);
  --color-thd03-panel: var(--thd03-panel);
  --color-thd03-ink: var(--thd03-ink);
  --color-thd03-mut: var(--thd03-mut);
  --color-thd03-line: var(--thd03-line);
  --color-thd03-acc: var(--thd03-acc);
}

@theme {
  --font-thd03-sans: 'Manrope', system-ui, sans-serif;
}

.thd-03 {
  width: 100%;
  min-height: 100svh;
  --thd03-bg: #f5f6fa;
  --thd03-panel: #ffffff;
  --thd03-ink: #111827;
  --thd03-mut: #5b6475;
  --thd03-line: #e4e7ee;
  --thd03-acc: #4f46e5;
}

.thd-03:has(#thd-03-t:checked) {
  --thd03-bg: #0b0d14;
  --thd03-panel: #121521;
  --thd03-ink: #eef0f6;
  --thd03-mut: #9aa2b5;
  --thd03-line: #232839;
  --thd03-acc: #818cf8;
}
```
