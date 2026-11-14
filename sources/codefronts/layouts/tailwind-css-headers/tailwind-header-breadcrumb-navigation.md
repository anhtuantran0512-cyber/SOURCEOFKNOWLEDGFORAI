---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-header-breadcrumb-navigation/"
title: "Tailwind Header with Breadcrumb Navigation"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "A two-tier header for deep pages: brand, section nav and utilities on top; a breadcrumb trail below with page actions aligned right."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Header with Breadcrumb Navigation
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-header-breadcrumb-navigation/

A two-tier header for deep pages: brand, section nav and utilities on top; a breadcrumb trail below with page actions aligned right. The trail is a real <nav aria-label="Breadcrumb"> around an <ol>, separators come from not-first:before:content-['/'] so they are never read aloud, and the middle crumbs collapse to an ellipsis on phones.
## HTML
```html
<div class="thd-09 group/thd09 w-full min-h-svh bg-thd09-bg font-thd09-sans text-thd09-ink antialiased">
  <a href="#thd-09-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded focus:bg-thd09-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <header class="sticky top-0 z-40 border-b border-thd09-line bg-thd09-panel">
    <div class="flex h-14 items-center gap-3 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-09-main" class="flex items-center gap-2 whitespace-nowrap font-bold tracking-tight"><span aria-hidden="true" class="grid size-7 place-items-center rounded-md bg-thd09-acc text-white"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" class="size-4"><path d="M12 3v4M12 17v4M3 12h4M17 12h4"/><circle cx="12" cy="12" r="3"/></svg></span>Beacon Cloud</a>
      <nav aria-label="Main" class="ml-4 hidden md:block">
        <ul class="flex items-center gap-1 text-sm font-medium">
          <li><a href="#thd-09-main" class="rounded-md px-3 py-2 text-thd09-mut hover:bg-thd09-ink/5 hover:text-thd09-ink">Home</a></li>
          <li><a href="#thd-09-main" aria-current="page" class="rounded-md px-3 py-2 text-thd09-mut hover:bg-thd09-ink/5 hover:text-thd09-ink aria-[current=page]:bg-thd09-acc/10 aria-[current=page]:text-thd09-acc">Products</a></li>
          <li><a href="#thd-09-main" class="rounded-md px-3 py-2 text-thd09-mut hover:bg-thd09-ink/5 hover:text-thd09-ink">Reports</a></li>
          <li><a href="#thd-09-main" class="rounded-md px-3 py-2 text-thd09-mut hover:bg-thd09-ink/5 hover:text-thd09-ink">Admin</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-0.5">
        <input id="thd-09-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-09-t" class="grid size-11 cursor-pointer place-items-center rounded-md text-thd09-mut hover:bg-thd09-ink/5 hover:text-thd09-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd09-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-09-t:checked]/thd09:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-09-t:checked]/thd09:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <button type="button" aria-label="Search" class="grid size-11 place-items-center rounded-md text-thd09-mut hover:bg-thd09-ink/5 hover:text-thd09-ink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px]"><circle cx="11" cy="11" r="6.4"/><path d="m15.8 15.8 5.2 5.2"/></svg></button>
        <button type="button" aria-label="Help" class="hidden size-11 place-items-center rounded-md text-thd09-mut hover:bg-thd09-ink/5 hover:text-thd09-ink sm:grid"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-[18px]"><circle cx="12" cy="12" r="8.5"/><path d="M9.8 9.6a2.3 2.3 0 1 1 3.4 2.1c-.8.5-1.2 1-1.2 1.9M12 16.6h.01"/></svg></button>
        <div class="group/acct relative ml-1">
          <button type="button" aria-haspopup="menu" class="flex min-h-11 items-center gap-2 rounded-md px-1.5 hover:bg-thd09-ink/5"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-thd09-acc/15 text-xs font-bold text-thd09-acc">SR</span><span class="hidden text-sm font-medium lg:block">Sam Rivera</span></button>
          <div role="menu" aria-label="Account" class="invisible absolute right-0 top-full z-50 mt-1 w-56 rounded-lg border border-thd09-line bg-thd09-panel p-1.5 opacity-0 shadow-xl shadow-black/10 transition-[opacity,visibility] duration-150 group-hover/acct:visible group-hover/acct:opacity-100 group-focus-within/acct:visible group-focus-within/acct:opacity-100">
            <a role="menuitem" href="#thd-09-main" class="flex min-h-10 items-center rounded px-2.5 text-sm hover:bg-thd09-ink/5 focus-visible:bg-thd09-ink/5">Account settings</a>
            <a role="menuitem" href="#thd-09-main" class="flex min-h-10 items-center rounded px-2.5 text-sm hover:bg-thd09-ink/5 focus-visible:bg-thd09-ink/5">Organisation</a>
            <a role="menuitem" href="#thd-09-main" class="flex min-h-10 items-center rounded px-2.5 text-sm hover:bg-thd09-ink/5 focus-visible:bg-thd09-ink/5">API tokens</a>
            <a role="menuitem" href="#thd-09-main" class="mt-1 flex min-h-10 items-center rounded border-t border-thd09-line px-2.5 text-sm text-red-600 hover:bg-red-500/10 focus-visible:bg-red-500/10">Sign out</a>
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-wrap items-center gap-x-4 gap-y-2 border-t border-thd09-line bg-thd09-bg/60 px-[clamp(.75rem,3vw,1.5rem)] py-2">
      <nav aria-label="Breadcrumb" class="min-w-0 flex-1">
        <ol class="flex min-w-0 items-center text-sm text-thd09-mut">
          <li class="flex-none"><a href="#thd-09-main" class="rounded px-1 py-1 hover:text-thd09-ink hover:underline">Home</a></li>
          <li class="flex-none not-first:before:mx-1.5 not-first:before:text-thd09-line2 not-first:before:content-['/'] sm:hidden"><a href="#thd-09-main" aria-label="Show full path" class="rounded px-1 py-1 hover:text-thd09-ink">&hellip;</a></li>
          <li class="flex-none not-first:before:mx-1.5 not-first:before:text-thd09-line2 not-first:before:content-['/'] max-sm:hidden"><a href="#thd-09-main" class="rounded px-1 py-1 hover:text-thd09-ink hover:underline">Products</a></li>
          <li class="flex-none not-first:before:mx-1.5 not-first:before:text-thd09-line2 not-first:before:content-['/'] max-sm:hidden"><a href="#thd-09-main" class="rounded px-1 py-1 hover:text-thd09-ink hover:underline">Observability</a></li>
          <li aria-current="page" class="min-w-0 truncate font-semibold text-thd09-ink not-first:before:mx-1.5 not-first:before:font-normal not-first:before:text-thd09-line2 not-first:before:content-['/']">Analytics Dashboard</li>
        </ol>
      </nav>
      <div class="flex items-center gap-2">
        <button type="button" class="min-h-9 rounded-md border border-thd09-line bg-thd09-panel px-3 text-sm font-medium hover:border-thd09-line2">Export CSV</button>
        <button type="button" class="min-h-9 rounded-md bg-thd09-acc px-3 text-sm font-semibold text-white hover:brightness-110">Edit dashboard</button>
      </div>
    </div>
  </header>
  <main id="thd-09-main" class="px-[clamp(.75rem,3vw,1.5rem)] py-8">
    <h1 class="text-2xl font-bold tracking-tight">Analytics Dashboard</h1>
    <p class="mt-1 text-sm text-thd09-mut">Narrow the frame: the middle crumbs fold into &hellip; and the current page truncates instead of wrapping.</p>
    <ul class="mt-6 grid grid-cols-[repeat(auto-fit,minmax(min(100%,14rem),1fr))] gap-3">
      <li class="rounded-lg border border-thd09-line bg-thd09-panel p-4"><p class="text-xs font-semibold uppercase tracking-wider text-thd09-mut">p95 latency</p><p class="mt-2 text-2xl font-bold tabular-nums">182 ms</p></li>
      <li class="rounded-lg border border-thd09-line bg-thd09-panel p-4"><p class="text-xs font-semibold uppercase tracking-wider text-thd09-mut">Error rate</p><p class="mt-2 text-2xl font-bold tabular-nums">0.12%</p></li>
      <li class="rounded-lg border border-thd09-line bg-thd09-panel p-4"><p class="text-xs font-semibold uppercase tracking-wider text-thd09-mut">Requests / min</p><p class="mt-2 text-2xl font-bold tabular-nums">48.2k</p></li>
    </ul>
    <div aria-hidden="true" class="h-[60svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd09-bg: var(--thd09-bg);
  --color-thd09-panel: var(--thd09-panel);
  --color-thd09-ink: var(--thd09-ink);
  --color-thd09-mut: var(--thd09-mut);
  --color-thd09-line: var(--thd09-line);
  --color-thd09-line2: var(--thd09-line2);
  --color-thd09-acc: var(--thd09-acc);
}

@theme {
  --font-thd09-sans: 'IBM Plex Sans', system-ui, sans-serif;
}

.thd-09 {
  width: 100%;
  min-height: 100svh;
  --thd09-bg: #f4f6f9;
  --thd09-panel: #ffffff;
  --thd09-ink: #0f172a;
  --thd09-mut: #52607a;
  --thd09-line: #e2e7ef;
  --thd09-line2: #a3aec2;
  --thd09-acc: #1d5bd8;
}

.thd-09:has(#thd-09-t:checked) {
  --thd09-bg: #0b1020;
  --thd09-panel: #111831;
  --thd09-ink: #e7ecf6;
  --thd09-mut: #9aa6bf;
  --thd09-line: #222c48;
  --thd09-line2: #56627f;
  --thd09-acc: #6c9bff;
}
```
