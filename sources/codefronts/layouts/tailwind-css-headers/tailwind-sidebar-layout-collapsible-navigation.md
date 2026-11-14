---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-sidebar-layout-collapsible-navigation/"
title: "Tailwind Sidebar Layout with Collapsible Navigation"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "When the header is vertical: a sidebar with logo, grouped navigation and a user footer, and a slim top bar for breadcrumb and page actions."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sidebar Layout with Collapsible Navigation
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-sidebar-layout-collapsible-navigation/

When the header is vertical: a sidebar with logo, grouped navigation and a user footer, and a slim top bar for breadcrumb and page actions. The shell is one CSS Grid whose first track animates from 16rem to 4.5rem on a pure-CSS toggle; collapsed icons get hover tooltips, and both regions scroll independently.
## HTML
```html
<div class="thd-20 group/thd20 grid w-full min-h-svh grid-cols-[4.5rem_minmax(0,1fr)] bg-thd20-bg font-thd20-sans text-thd20-ink antialiased transition-[grid-template-columns] duration-300 ease-[cubic-bezier(.2,.8,.2,1)] md:grid-cols-[16rem_minmax(0,1fr)] md:has-[#thd-20-rail:checked]:grid-cols-[4.5rem_minmax(0,1fr)]">
  <a href="#thd-20-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd20-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <input id="thd-20-rail" type="checkbox" class="sr-only" aria-label="Collapse sidebar">
  <header class="sticky top-0 z-40 flex h-svh flex-col self-start overflow-hidden border-r border-thd20-line bg-thd20-side">
    <div class="flex h-16 flex-none items-center gap-2 px-4">
      <a href="#thd-20-main" class="flex min-w-0 items-center gap-2.5 font-extrabold tracking-tight"><span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-xl bg-thd20-acc text-white"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="m3 18 6-9 4 5 3-4 5 8"/></svg></span><span class="truncate max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Ridgeline</span></a>
    </div>
    <nav aria-label="Workspace" class="min-h-0 flex-1 overflow-y-auto overflow-x-hidden px-3 py-2">
      <p class="px-2 pb-1.5 pt-3 text-[11px] font-bold uppercase tracking-[.12em] text-thd20-mut max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Workspace</p>
      <ul class="grid gap-0.5 text-sm font-medium">
        <li class="group/it relative"><a href="#thd-20-main" aria-current="page" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink aria-[current=page]:bg-thd20-acc/12 aria-[current=page]:text-thd20-acc"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-5 flex-none"><rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.5"/></svg><span class="truncate max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Overview</span></a><span aria-hidden="true" class="invisible absolute left-full top-1/2 z-50 ml-2 -translate-y-1/2 whitespace-nowrap rounded-md bg-thd20-ink px-2 py-1 text-xs font-semibold text-thd20-bg opacity-0 transition-opacity max-md:group-hover/it:visible max-md:group-hover/it:opacity-100 max-md:group-focus-within/it:visible max-md:group-focus-within/it:opacity-100 md:group-has-[#thd-20-rail:checked]/thd20:group-hover/it:visible md:group-has-[#thd-20-rail:checked]/thd20:group-hover/it:opacity-100 md:group-has-[#thd-20-rail:checked]/thd20:group-focus-within/it:visible md:group-has-[#thd-20-rail:checked]/thd20:group-focus-within/it:opacity-100">Overview</span></li>
        <li class="group/it relative"><a href="#thd-20-main" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-5 flex-none"><path d="M3.5 7.5a2 2 0 0 1 2-2h4l2 2h7a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2v-10Z"/></svg><span class="min-w-0 flex-1 truncate max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Projects</span><span class="rounded-full bg-thd20-ink/8 px-2 text-xs tabular-nums max-md:hidden md:group-has-[#thd-20-rail:checked]/thd20:hidden">12</span></a><span aria-hidden="true" class="invisible absolute left-full top-1/2 z-50 ml-2 -translate-y-1/2 whitespace-nowrap rounded-md bg-thd20-ink px-2 py-1 text-xs font-semibold text-thd20-bg opacity-0 transition-opacity max-md:group-hover/it:visible max-md:group-hover/it:opacity-100 max-md:group-focus-within/it:visible max-md:group-focus-within/it:opacity-100 md:group-has-[#thd-20-rail:checked]/thd20:group-hover/it:visible md:group-has-[#thd-20-rail:checked]/thd20:group-hover/it:opacity-100 md:group-has-[#thd-20-rail:checked]/thd20:group-focus-within/it:visible md:group-has-[#thd-20-rail:checked]/thd20:group-focus-within/it:opacity-100">Projects &middot; 12</span></li>
        <li class="group/it relative"><a href="#thd-20-main" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-5 flex-none"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg><span class="truncate max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Insights</span></a><span aria-hidden="true" class="invisible absolute left-full top-1/2 z-50 ml-2 -translate-y-1/2 whitespace-nowrap rounded-md bg-thd20-ink px-2 py-1 text-xs font-semibold text-thd20-bg opacity-0 transition-opacity max-md:group-hover/it:visible max-md:group-hover/it:opacity-100 max-md:group-focus-within/it:visible max-md:group-focus-within/it:opacity-100 md:group-has-[#thd-20-rail:checked]/thd20:group-hover/it:visible md:group-has-[#thd-20-rail:checked]/thd20:group-hover/it:opacity-100 md:group-has-[#thd-20-rail:checked]/thd20:group-focus-within/it:visible md:group-has-[#thd-20-rail:checked]/thd20:group-focus-within/it:opacity-100">Insights</span></li>
        <li class="group/it relative"><a href="#thd-20-main" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="size-5 flex-none"><path d="M13 3 5 13h6l-1 8 8-10h-6l1-8Z"/></svg><span class="truncate max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Automations</span></a><span aria-hidden="true" class="invisible absolute left-full top-1/2 z-50 ml-2 -translate-y-1/2 whitespace-nowrap rounded-md bg-thd20-ink px-2 py-1 text-xs font-semibold text-thd20-bg opacity-0 transition-opacity max-md:group-hover/it:visible max-md:group-hover/it:opacity-100 max-md:group-focus-within/it:visible max-md:group-focus-within/it:opacity-100 md:group-has-[#thd-20-rail:checked]/thd20:group-hover/it:visible md:group-has-[#thd-20-rail:checked]/thd20:group-hover/it:opacity-100 md:group-has-[#thd-20-rail:checked]/thd20:group-focus-within/it:visible md:group-has-[#thd-20-rail:checked]/thd20:group-focus-within/it:opacity-100">Automations</span></li>
      </ul>
      <p class="px-2 pb-1.5 pt-5 text-[11px] font-bold uppercase tracking-[.12em] text-thd20-mut max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Library</p>
      <ul class="grid gap-0.5 text-sm font-medium max-md:mt-3 max-md:border-t max-md:border-thd20-line max-md:pt-3">
        <li><a href="#thd-20-main" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-5 flex-none"><rect x="3.5" y="4.5" width="17" height="15" rx="2"/><path d="m3.5 16 5-5 4 4 3-3 5 5"/></svg><span class="truncate max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Assets</span></a></li>
        <li><a href="#thd-20-main" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-5 flex-none"><rect x="4.5" y="3.5" width="15" height="17" rx="2"/><path d="M8.5 8h7M8.5 12h7M8.5 16h4"/></svg><span class="truncate max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Templates</span></a></li>
        <li><a href="#thd-20-main" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-5 flex-none"><rect x="3.5" y="4" width="17" height="5" rx="1.5"/><path d="M5 9v9.5a1.5 1.5 0 0 0 1.5 1.5h11a1.5 1.5 0 0 0 1.5-1.5V9M10 13h4"/></svg><span class="truncate max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only">Archive</span></a></li>
      </ul>
    </nav>
    <div class="flex flex-none items-center gap-3 border-t border-thd20-line p-3.5">
      <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-amber-500/20 text-xs font-bold text-amber-600">PS</span>
      <span class="min-w-0 leading-tight max-md:sr-only md:group-has-[#thd-20-rail:checked]/thd20:sr-only"><span class="block truncate text-sm font-semibold">Priya Sharma</span><span class="block truncate text-xs text-thd20-mut">Owner &middot; Ridgeline</span></span>
    </div>
  </header>
  <div class="min-w-0">
    <div class="sticky top-0 z-30 flex h-16 items-center gap-2 border-b border-thd20-line bg-thd20-bg/90 px-3 backdrop-blur-md sm:px-5">
      <label for="thd-20-rail" class="hidden size-11 flex-none cursor-pointer place-items-center rounded-xl text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink md:grid group-has-[#thd-20-rail:focus-visible]/thd20:outline-2 group-has-[#thd-20-rail:focus-visible]/thd20:outline-thd20-acc">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="size-5 transition-transform group-has-[#thd-20-rail:checked]/thd20:rotate-180"><rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><path d="M9 4.5v15M15.5 10l-2 2 2 2"/></svg>
        <span class="sr-only">Collapse or expand the sidebar</span>
      </label>
      <nav aria-label="Breadcrumb" class="min-w-0 flex-1">
        <ol class="flex min-w-0 items-center text-sm text-thd20-mut">
          <li class="max-sm:hidden"><a href="#thd-20-main" class="hover:text-thd20-ink">Workspace</a></li>
          <li class="max-sm:hidden before:mx-2 before:text-thd20-line2 before:content-['/']"><a href="#thd-20-main" class="hover:text-thd20-ink">Projects</a></li>
          <li aria-current="page" class="min-w-0 truncate font-semibold text-thd20-ink sm:before:mx-2 sm:before:font-normal sm:before:text-thd20-line2 sm:before:content-['/']">Trail resurfacing</li>
        </ol>
      </nav>
      <input id="thd-20-t" type="checkbox" class="peer/t sr-only">
      <label for="thd-20-t" class="grid size-11 flex-none cursor-pointer place-items-center rounded-xl text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd20-acc">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-20-t:checked]/thd20:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-20-t:checked]/thd20:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
        <span class="sr-only">Switch light or dark theme</span>
      </label>
      <button type="button" aria-label="Star project" class="hidden size-11 flex-none place-items-center rounded-xl text-thd20-mut hover:bg-thd20-ink/5 hover:text-thd20-ink sm:grid"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px]"><path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9L12 3.5Z"/></svg></button>
      <a href="#thd-20-main" class="grid min-h-10 flex-none place-items-center rounded-xl bg-thd20-acc px-4 text-sm font-semibold text-white hover:brightness-110">Share</a>
    </div>
    <main id="thd-20-main" class="px-[clamp(1rem,3vw,2rem)] py-8">
      <h1 class="text-[clamp(1.6rem,4vw,2.2rem)] font-extrabold tracking-tight">Trail resurfacing</h1>
      <p class="mt-2 max-w-[56ch] text-thd20-mut">Use the panel icon in the top bar to collapse the sidebar to an icon rail &mdash; hover an icon for its tooltip. The grid track animates between 16rem and 4.5rem.</p>
      <ul class="mt-6 grid grid-cols-[repeat(auto-fit,minmax(min(100%,14rem),1fr))] gap-3">
        <li class="rounded-2xl border border-thd20-line bg-thd20-side p-5"><p class="text-sm text-thd20-mut">Segments done</p><p class="mt-2 text-3xl font-extrabold tabular-nums">14<span class="text-lg text-thd20-mut">/22</span></p></li>
        <li class="rounded-2xl border border-thd20-line bg-thd20-side p-5"><p class="text-sm text-thd20-mut">Volunteers</p><p class="mt-2 text-3xl font-extrabold tabular-nums">38</p></li>
        <li class="rounded-2xl border border-thd20-line bg-thd20-side p-5"><p class="text-sm text-thd20-mut">Next work day</p><p class="mt-2 text-3xl font-extrabold">Sat 4 Oct</p></li>
      </ul>
      <div aria-hidden="true" class="h-[80svh]"></div>
    </main>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd20-bg: var(--thd20-bg);
  --color-thd20-side: var(--thd20-side);
  --color-thd20-ink: var(--thd20-ink);
  --color-thd20-mut: var(--thd20-mut);
  --color-thd20-line: var(--thd20-line);
  --color-thd20-line2: var(--thd20-line2);
  --color-thd20-acc: var(--thd20-acc);
}

@theme {
  --font-thd20-sans: 'Albert Sans', system-ui, sans-serif;
}

.thd-20 {
  width: 100%;
  min-height: 100svh;
  --thd20-bg: #f5f7f4;
  --thd20-side: #ffffff;
  --thd20-ink: #142018;
  --thd20-mut: #56645a;
  --thd20-line: #e1e7e1;
  --thd20-line2: #a9b5ab;
  --thd20-acc: #1f7a4a;
}

.thd-20:has(#thd-20-t:checked) {
  --thd20-bg: #0b100d;
  --thd20-side: #111814;
  --thd20-ink: #e6efe8;
  --thd20-mut: #99a99d;
  --thd20-line: #1f2a23;
  --thd20-line2: #4b5a50;
  --thd20-acc: #4ade80;
}
```
