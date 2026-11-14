---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-dropdown-menu-hover-keyboard-accessible/"
title: "Tailwind CSS Dropdown Menu — Hover & Keyboard Accessible"
section: "navigation"
category: "tailwind-css-navigation-menus"
category_name: "Tailwind CSS Navigation Menus"
description: "A product-site navbar with rich dropdowns — a two-column panel with icon tiles, a compact list and a resources menu — that open on group-hover/dd: and, just…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Dropdown Menu — Hover & Keyboard Accessible
Source: https://codefronts.com/navigation/tailwind-css-navigation-menus/tailwind-css-dropdown-menu-hover-keyboard-accessible/

A product-site navbar with rich dropdowns — a two-column panel with icon tiles, a compact list and a resources menu — that open on group-hover/dd: and, just as importantly, on group-focus-within/dd: so keyboard users get the same menu. An invisible hover bridge fixes the classic &lsquo;menu closes when you move to it&rsquo; bug. Zero JavaScript.
## HTML
```html
<div class="tnv-02 min-h-svh w-full bg-tnv02-bg bg-[radial-gradient(80%_60%_at_50%_0%,white,transparent)] font-tnv02-sans text-tnv02-ink antialiased selection:bg-tnv02-acc selection:text-white">
  <header class="sticky top-0 z-30 border-b border-tnv02-line bg-white/90 shadow-[0_2px_20px_-8px_var(--color-tnv02-shadow)] backdrop-blur-md">
    <nav aria-label="Main" class="mx-auto flex h-[68px] max-w-6xl items-center justify-between gap-6 px-5 sm:px-10">
      <a href="#" class="flex items-center gap-2.5 text-xl font-bold tracking-[-0.03em]">
        <span class="grid size-8 place-items-center rounded-lg bg-linear-135 from-tnv02-acc to-tnv02-acc2 shadow-[0_4px_12px_-4px_var(--color-tnv02-acc)]"><svg class="size-[18px] fill-white" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></span>Vertex
      </a>
      <ul class="hidden items-center gap-0.5 md:flex">
        <li class="group/dd relative">
          <button type="button" aria-haspopup="true" class="flex h-11 items-center gap-1.5 rounded-lg px-3.5 text-sm font-semibold text-tnv02-mut transition-colors group-hover/dd:bg-tnv02-bg group-hover/dd:text-tnv02-ink group-focus-within/dd:bg-tnv02-bg group-focus-within/dd:text-tnv02-ink focus-visible:outline-2 focus-visible:outline-tnv02-acc">Products<svg class="size-3.5 opacity-60 transition-transform duration-200 group-hover/dd:rotate-180 group-focus-within/dd:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>
          <div class="invisible absolute top-full left-1/2 z-40 mt-2.5 grid w-[30rem] -translate-x-1/2 translate-y-1.5 grid-cols-2 gap-1 rounded-2xl border border-tnv02-line bg-white p-2 opacity-0 shadow-[0_24px_60px_-16px_var(--color-tnv02-shadow)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(.16,1,.3,1)] before:absolute before:inset-x-0 before:-top-3 before:h-3 before:content-[''] group-hover/dd:visible group-hover/dd:translate-y-0 group-hover/dd:opacity-100 group-focus-within/dd:visible group-focus-within/dd:translate-y-0 group-focus-within/dd:opacity-100 motion-reduce:transition-none">
            <a href="#" class="group/it flex items-center gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv02-bg focus-visible:bg-tnv02-bg focus-visible:ring-2 focus-visible:ring-tnv02-acc/40"><span class="grid size-10 flex-none place-items-center rounded-lg bg-tnv02-bg text-tnv02-acc transition-colors group-hover/it:bg-tnv02-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span><span class="grid text-sm font-semibold">Dashboard<span class="text-xs font-medium text-tnv02-mut">Analytics &amp; insights</span></span></a>
            <a href="#" class="group/it flex items-center gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv02-bg focus-visible:bg-tnv02-bg focus-visible:ring-2 focus-visible:ring-tnv02-acc/40"><span class="grid size-10 flex-none place-items-center rounded-lg bg-tnv02-bg text-tnv02-acc transition-colors group-hover/it:bg-tnv02-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></span><span class="grid text-sm font-semibold">Monitoring<span class="text-xs font-medium text-tnv02-mut">Real-time metrics</span></span></a>
            <a href="#" class="group/it flex items-center gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv02-bg focus-visible:bg-tnv02-bg focus-visible:ring-2 focus-visible:ring-tnv02-acc/40"><span class="grid size-10 flex-none place-items-center rounded-lg bg-tnv02-bg text-tnv02-acc transition-colors group-hover/it:bg-tnv02-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg></span><span class="grid text-sm font-semibold">Teams<span class="text-xs font-medium text-tnv02-mut">Collaboration tools</span></span></a>
            <a href="#" class="group/it flex items-center gap-3 rounded-xl p-3 outline-none transition-colors hover:bg-tnv02-bg focus-visible:bg-tnv02-bg focus-visible:ring-2 focus-visible:ring-tnv02-acc/40"><span class="grid size-10 flex-none place-items-center rounded-lg bg-tnv02-bg text-tnv02-acc transition-colors group-hover/it:bg-tnv02-acc group-hover/it:text-white"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></span><span class="grid text-sm font-semibold"><span class="flex items-center gap-1.5">Automation<span class="rounded-full bg-tnv02-acc/10 px-1.5 py-px text-[10px] font-bold tracking-wide text-tnv02-acc uppercase">New</span></span><span class="text-xs font-medium text-tnv02-mut">Workflow builder</span></span></a>
            <a href="#" class="col-span-2 mt-1 flex min-h-11 items-center justify-between rounded-xl bg-linear-135 from-tnv02-bg to-tnv02-line px-4 py-3 text-[13px] font-bold text-tnv02-acc transition hover:brightness-[0.97] focus-visible:outline-2 focus-visible:outline-tnv02-acc">Explore all products<svg class="size-4 transition-transform group-hover/dd:translate-x-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
          </div>
        </li>
        <li class="group/dd relative">
          <button type="button" aria-haspopup="true" class="flex h-11 items-center gap-1.5 rounded-lg px-3.5 text-sm font-semibold text-tnv02-mut transition-colors group-hover/dd:bg-tnv02-bg group-hover/dd:text-tnv02-ink group-focus-within/dd:bg-tnv02-bg group-focus-within/dd:text-tnv02-ink focus-visible:outline-2 focus-visible:outline-tnv02-acc">Solutions<svg class="size-3.5 opacity-60 transition-transform duration-200 group-hover/dd:rotate-180 group-focus-within/dd:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>
          <ul class="invisible absolute top-full left-1/2 z-40 mt-2.5 grid w-56 -translate-x-1/2 translate-y-1.5 gap-0.5 rounded-2xl border border-tnv02-line bg-white p-2 text-sm font-semibold text-tnv02-mut opacity-0 shadow-[0_24px_60px_-16px_var(--color-tnv02-shadow)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(.16,1,.3,1)] before:absolute before:inset-x-0 before:-top-3 before:h-3 before:content-[''] group-hover/dd:visible group-hover/dd:translate-y-0 group-hover/dd:opacity-100 group-focus-within/dd:visible group-focus-within/dd:translate-y-0 group-focus-within/dd:opacity-100 motion-reduce:transition-none [&_a]:flex [&_a]:min-h-11 [&_a]:items-center [&_a]:rounded-lg [&_a]:px-3 [&_a]:outline-none [&_a:focus-visible]:bg-tnv02-bg [&_a:focus-visible]:text-tnv02-ink [&_a:hover]:bg-tnv02-bg [&_a:hover]:text-tnv02-ink">
            <li><a href="#">Enterprise</a></li>
            <li><a href="#">Startups</a></li>
            <li><a href="#">Agencies</a></li>
            <li role="separator" class="mx-2 my-1 h-px bg-tnv02-line"></li>
            <li><a href="#">Case studies</a></li>
          </ul>
        </li>
        <li><a href="#" class="flex h-11 items-center rounded-lg px-3.5 text-sm font-semibold text-tnv02-mut transition-colors hover:bg-tnv02-bg hover:text-tnv02-ink focus-visible:outline-2 focus-visible:outline-tnv02-acc">Pricing</a></li>
        <li class="group/dd relative">
          <button type="button" aria-haspopup="true" class="flex h-11 items-center gap-1.5 rounded-lg px-3.5 text-sm font-semibold text-tnv02-mut transition-colors group-hover/dd:bg-tnv02-bg group-hover/dd:text-tnv02-ink group-focus-within/dd:bg-tnv02-bg group-focus-within/dd:text-tnv02-ink focus-visible:outline-2 focus-visible:outline-tnv02-acc">Resources<svg class="size-3.5 opacity-60 transition-transform duration-200 group-hover/dd:rotate-180 group-focus-within/dd:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button>
          <ul class="invisible absolute top-full left-1/2 z-40 mt-2.5 grid w-56 -translate-x-1/2 translate-y-1.5 gap-0.5 rounded-2xl border border-tnv02-line bg-white p-2 text-sm font-semibold text-tnv02-mut opacity-0 shadow-[0_24px_60px_-16px_var(--color-tnv02-shadow)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(.16,1,.3,1)] before:absolute before:inset-x-0 before:-top-3 before:h-3 before:content-[''] group-hover/dd:visible group-hover/dd:translate-y-0 group-hover/dd:opacity-100 group-focus-within/dd:visible group-focus-within/dd:translate-y-0 group-focus-within/dd:opacity-100 motion-reduce:transition-none [&_a]:flex [&_a]:min-h-11 [&_a]:items-center [&_a]:justify-between [&_a]:rounded-lg [&_a]:px-3 [&_a]:outline-none [&_a:focus-visible]:bg-tnv02-bg [&_a:focus-visible]:text-tnv02-ink [&_a:hover]:bg-tnv02-bg [&_a:hover]:text-tnv02-ink">
            <li><a href="#">Documentation<kbd class="font-tnv02-mono text-[11px] font-medium text-tnv02-mut">D</kbd></a></li>
            <li><a href="#">Blog</a></li>
            <li><a href="#">Community</a></li>
          </ul>
        </li>
      </ul>
      <div class="flex items-center gap-2.5">
        <a href="#" class="hidden h-10 items-center rounded-lg border-[1.5px] border-tnv02-line px-4 text-sm font-semibold text-tnv02-acc transition hover:border-tnv02-acc2 hover:bg-tnv02-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnv02-acc sm:inline-flex">Log in</a>
        <a href="#" class="inline-flex h-10 items-center rounded-lg bg-tnv02-acc px-4 text-sm font-semibold text-white shadow-[0_6px_16px_-6px_var(--color-tnv02-acc)] transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tnv02-acc">Start free</a>
        <details class="group/m relative md:hidden">
          <summary aria-label="Menu" class="grid size-11 cursor-pointer list-none place-items-center rounded-lg border border-tnv02-line bg-white outline-none focus-visible:ring-2 focus-visible:ring-tnv02-acc/40 [&::-webkit-details-marker]:hidden"><svg class="size-5 group-open/m:hidden" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg><svg class="hidden size-5 group-open/m:block" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></summary>
          <ul class="absolute top-[calc(100%+10px)] right-0 z-40 grid w-64 gap-0.5 rounded-2xl border border-tnv02-line bg-white p-2 text-[15px] font-semibold shadow-[0_24px_60px_-16px_var(--color-tnv02-shadow)] transition-[opacity,translate] duration-200 starting:-translate-y-1 starting:opacity-0 [&_a]:flex [&_a]:min-h-11 [&_a]:items-center [&_a]:rounded-lg [&_a]:px-3 [&_a:hover]:bg-tnv02-bg">
            <li><a href="#">Products</a></li><li><a href="#">Solutions</a></li><li><a href="#">Pricing</a></li><li><a href="#">Resources</a></li><li><a href="#" class="text-tnv02-acc">Log in</a></li>
          </ul>
        </details>
      </div>
    </nav>
  </header>
  <main class="grid place-items-center px-5 py-24 text-center [&_code]:rounded [&_code]:bg-tnv02-line [&_code]:px-1.5 [&_code]:font-tnv02-mono [&_code]:text-[0.85em] [&_code]:text-tnv02-ink">
    <span class="mb-6 inline-flex items-center gap-2 rounded-full bg-tnv02-acc py-1 pr-3 pl-1 text-xs font-bold text-white"><span class="grid size-5 place-items-center rounded-full bg-white/25"><span class="size-1.5 rounded-full bg-white"></span></span>Hover or Tab to any item with an arrow</span>
    <h1 class="max-w-2xl text-[clamp(2.25rem,5vw,3.5rem)] leading-[1.1] font-extrabold tracking-[-0.035em] text-balance">Dropdowns that stay open when you reach for them</h1>
    <p class="mt-4 max-w-lg text-base/[1.7] text-tnv02-mut text-pretty">Panels open on <code>group-hover/dd:</code> <em>and</em> <code>group-focus-within/dd:</code>, slide in with <code>translate-y</code>, and an invisible bridge stops them closing as the pointer crosses the gap.</p>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tnv02-bg: #f5f3ff;
  --color-tnv02-bg: oklch(0.969 0.016 294);
  --color-tnv02-line: #ede9fe;
  --color-tnv02-line: oklch(0.943 0.029 295);
  --color-tnv02-ink: #1e1b4b;
  --color-tnv02-ink: oklch(0.257 0.09 281);
  --color-tnv02-mut: #4b5563;
  --color-tnv02-mut: oklch(0.446 0.026 257);
  --color-tnv02-acc: #7c3aed;
  --color-tnv02-acc: oklch(0.541 0.281 293);
  --color-tnv02-acc2: #a78bfa;
  --color-tnv02-acc2: oklch(0.702 0.183 294);
  --color-tnv02-shadow: #7c3aed33;
  --color-tnv02-shadow: oklch(0.541 0.281 293 / 0.2);
  --font-tnv02-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tnv02-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tnv-02 {
  width: 100%;
  min-height: 100svh;
}
```
