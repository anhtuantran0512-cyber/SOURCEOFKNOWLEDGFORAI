---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-docs-header-version-switcher-search/"
title: "Tailwind Docs Header with Version Switcher and Search"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "The three controls docs readers hunt for — a version switcher with channel chips, a search field with its / hint, and a Docs / API / Blog / GitHub row —…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Docs Header with Version Switcher and Search
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-docs-header-version-switcher-search/

The three controls docs readers hunt for — a version switcher with channel chips, a search field with its / hint, and a Docs / API / Blog / GitHub row — above a sticky sidebar. The version menu opens on group-hover/ver: and group-focus-within/ver:, so it is keyboard-operable with zero script.
## HTML
```html
<div class="thd-02 group/thd02 w-full min-h-svh bg-thd02-bg font-thd02-sans text-thd02-ink antialiased">
  <a href="#thd-02-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd02-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <header class="sticky top-0 z-40 flex h-16 items-center gap-3 border-b border-thd02-line bg-thd02-bg/85 px-[clamp(.75rem,3vw,1.5rem)] backdrop-blur-lg">
    <a href="#thd-02-main" class="flex items-center gap-2 whitespace-nowrap text-[1.05rem] font-extrabold tracking-tight">
      <span aria-hidden="true" class="grid size-7 place-items-center rounded-lg bg-thd02-acc text-white"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" class="size-4"><path d="M4 18 9 6l3 7 3-7 5 12"/></svg></span>
      meridian<span class="font-medium text-thd02-mut">/docs</span>
    </a>
    <div class="group/ver relative">
      <button type="button" aria-haspopup="menu" class="flex min-h-9 items-center gap-1.5 rounded-lg border border-thd02-line bg-thd02-panel px-2.5 font-thd02-mono text-xs font-medium transition-colors hover:border-thd02-mut/50">v3.4.2 <span class="hidden rounded-full bg-thd02-acc/12 px-1.5 py-0.5 font-thd02-sans text-[10px] font-bold uppercase tracking-wide text-thd02-acc sm:inline">Latest</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" class="size-3.5 text-thd02-mut transition-transform group-hover/ver:rotate-180 group-focus-within/ver:rotate-180"><path d="m6 9 6 6 6-6"/></svg></button>
      <ul role="menu" aria-label="Documentation version" class="invisible absolute left-0 top-full z-50 mt-2 w-64 translate-y-1 rounded-xl border border-thd02-line bg-thd02-panel p-1.5 opacity-0 shadow-[0_20px_50px_-20px_rgb(0_0_0/.35)] transition-[opacity,translate,visibility] duration-150 before:absolute before:inset-x-0 before:-top-2 before:h-2 before:content-[''] group-hover/ver:visible group-hover/ver:translate-y-0 group-hover/ver:opacity-100 group-focus-within/ver:visible group-focus-within/ver:translate-y-0 group-focus-within/ver:opacity-100">
        <li role="none"><a role="menuitem" href="#thd-02-main" aria-current="true" class="flex min-h-10 items-center justify-between rounded-lg px-2.5 font-thd02-mono text-[13px] hover:bg-thd02-ink/5 focus-visible:bg-thd02-ink/5 aria-[current=true]:text-thd02-acc">v3.4.2 <span class="rounded-full bg-thd02-acc/12 px-2 py-0.5 font-thd02-sans text-[10px] font-bold uppercase text-thd02-acc">Latest</span></a></li>
        <li role="none"><a role="menuitem" href="#thd-02-main" class="flex min-h-10 items-center justify-between rounded-lg px-2.5 font-thd02-mono text-[13px] hover:bg-thd02-ink/5 focus-visible:bg-thd02-ink/5">v3.3.8 <span class="rounded-full bg-thd02-blue/12 px-2 py-0.5 font-thd02-sans text-[10px] font-bold uppercase text-thd02-blue">Stable</span></a></li>
        <li role="none"><a role="menuitem" href="#thd-02-main" class="flex min-h-10 items-center justify-between rounded-lg px-2.5 font-thd02-mono text-[13px] hover:bg-thd02-ink/5 focus-visible:bg-thd02-ink/5">v3.0.14 <span class="rounded-full bg-thd02-amber/15 px-2 py-0.5 font-thd02-sans text-[10px] font-bold uppercase text-thd02-amber">LTS</span></a></li>
        <li role="none"><a role="menuitem" href="#thd-02-main" class="flex min-h-10 items-center justify-between rounded-lg px-2.5 font-thd02-mono text-[13px] text-thd02-mut hover:bg-thd02-ink/5 focus-visible:bg-thd02-ink/5">v2.9.4 <span class="rounded-full bg-thd02-ink/8 px-2 py-0.5 font-thd02-sans text-[10px] font-bold uppercase">Maintenance</span></a></li>
        <li role="none" class="mt-1 border-t border-thd02-line pt-1"><a role="menuitem" href="#thd-02-main" class="flex min-h-10 items-center rounded-lg px-2.5 text-[13px] font-semibold text-thd02-acc hover:bg-thd02-ink/5 focus-visible:bg-thd02-ink/5">All releases &rarr;</a></li>
      </ul>
    </div>
    <search class="mx-auto hidden min-w-0 max-w-sm flex-1 sm:flex">
      <label class="flex min-h-10 w-full items-center gap-2 rounded-lg border border-thd02-line bg-thd02-panel px-3 text-sm text-thd02-mut transition focus-within:border-thd02-acc focus-within:ring-4 focus-within:ring-thd02-acc/15">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true" class="size-4 flex-none"><circle cx="11" cy="11" r="6.4"/><path d="m15.8 15.8 5.2 5.2"/></svg>
        <input type="search" placeholder="Search docs" aria-label="Search documentation" class="min-w-0 flex-1 bg-transparent text-thd02-ink outline-none placeholder:text-thd02-mut">
        <kbd class="rounded border border-thd02-line px-1.5 font-thd02-mono text-[11px]">/</kbd>
      </label>
    </search>
    <nav aria-label="Main" class="ml-auto hidden md:block">
      <ul class="flex items-center gap-1 text-sm font-medium">
        <li><a href="#thd-02-main" aria-current="page" class="rounded-md px-2.5 py-2 text-thd02-mut hover:text-thd02-ink aria-[current=page]:text-thd02-ink aria-[current=page]:underline aria-[current=page]:decoration-thd02-acc aria-[current=page]:decoration-2 aria-[current=page]:underline-offset-[22px]">Docs</a></li>
        <li><a href="#thd-02-main" class="rounded-md px-2.5 py-2 text-thd02-mut hover:text-thd02-ink">API</a></li>
        <li><a href="#thd-02-main" class="rounded-md px-2.5 py-2 text-thd02-mut hover:text-thd02-ink">Blog</a></li>
      </ul>
    </nav>
    <div class="ml-auto flex items-center md:ml-0">
      <a href="#thd-02-main" aria-label="Meridian on GitHub" class="grid size-11 place-items-center rounded-full text-thd02-mut hover:bg-thd02-ink/5 hover:text-thd02-ink"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="size-5"><path d="M12 .5C5.7.5.5 5.7.5 12a11.5 11.5 0 0 0 7.9 10.9c.6.1.8-.3.8-.6v-2c-3.2.7-3.9-1.5-3.9-1.5-.5-1.3-1.3-1.7-1.3-1.7-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.6-.3-5.3-1.3-5.3-5.7 0-1.3.5-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.2 1.2a11 11 0 0 1 5.8 0c2.2-1.5 3.2-1.2 3.2-1.2.6 1.6.2 2.8.1 3.1.8.8 1.2 1.9 1.2 3.1 0 4.4-2.7 5.4-5.3 5.7.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A11.5 11.5 0 0 0 23.5 12C23.5 5.7 18.3.5 12 .5Z"/></svg></a>
      <input id="thd-02-t" type="checkbox" class="peer/t sr-only">
      <label for="thd-02-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-thd02-mut hover:bg-thd02-ink/5 hover:text-thd02-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd02-acc">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-02-t:checked]/thd02:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-02-t:checked]/thd02:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
        <span class="sr-only">Switch light or dark theme</span>
      </label>
    </div>
  </header>
  <div class="mx-auto flex max-w-7xl">
    <nav aria-label="Documentation" class="sticky top-16 hidden h-[calc(100svh-4rem)] w-60 flex-none overflow-y-auto border-r border-thd02-line px-4 py-6 md:block">
      <p class="px-2 text-[11px] font-bold uppercase tracking-[.12em] text-thd02-mut">Getting started</p>
      <ul class="mb-6 mt-2 text-sm">
        <li><a href="#thd-02-main" aria-current="page" class="flex min-h-9 items-center rounded-md px-2 text-thd02-mut hover:bg-thd02-ink/5 hover:text-thd02-ink aria-[current=page]:bg-thd02-acc/10 aria-[current=page]:font-semibold aria-[current=page]:text-thd02-acc">Installation</a></li>
        <li><a href="#thd-02-main" class="flex min-h-9 items-center rounded-md px-2 text-thd02-mut hover:bg-thd02-ink/5 hover:text-thd02-ink">Project structure</a></li>
        <li><a href="#thd-02-main" class="flex min-h-9 items-center rounded-md px-2 text-thd02-mut hover:bg-thd02-ink/5 hover:text-thd02-ink">Configuration</a></li>
      </ul>
      <p class="px-2 text-[11px] font-bold uppercase tracking-[.12em] text-thd02-mut">Core concepts</p>
      <ul class="mt-2 text-sm">
        <li><a href="#thd-02-main" class="flex min-h-9 items-center rounded-md px-2 text-thd02-mut hover:bg-thd02-ink/5 hover:text-thd02-ink">Routing</a></li>
        <li><a href="#thd-02-main" class="flex min-h-9 items-center rounded-md px-2 text-thd02-mut hover:bg-thd02-ink/5 hover:text-thd02-ink">Data loading</a></li>
        <li><a href="#thd-02-main" class="flex min-h-9 items-center rounded-md px-2 text-thd02-mut hover:bg-thd02-ink/5 hover:text-thd02-ink">Caching</a></li>
        <li><a href="#thd-02-main" class="flex min-h-9 items-center rounded-md px-2 text-thd02-mut hover:bg-thd02-ink/5 hover:text-thd02-ink">Middleware</a></li>
      </ul>
    </nav>
    <main id="thd-02-main" class="min-w-0 flex-1 px-[clamp(1rem,4vw,3rem)] py-10">
      <p class="text-sm font-semibold text-thd02-acc">Getting started</p>
      <h1 class="mt-2 text-[clamp(1.9rem,4.5vw,2.75rem)] font-extrabold leading-tight tracking-tight">Installation</h1>
      <p class="mt-3 max-w-[60ch] text-[1.05rem] leading-relaxed text-thd02-mut">Meridian needs Node 20 or newer. Scaffold a project, install dependencies and start the dev server in under a minute.</p>
      <pre class="mt-6 max-w-2xl overflow-x-auto rounded-xl border border-thd02-line bg-thd02-panel p-4 font-thd02-mono text-[13px] leading-relaxed"><code><span class="text-thd02-mut">$</span> npm create meridian@latest my-app
<span class="text-thd02-mut">$</span> cd my-app &amp;&amp; npm run dev</code></pre>
      <div class="mt-6 flex max-w-2xl gap-3 rounded-xl border border-thd02-acc/30 bg-thd02-acc/8 p-4 text-sm"><span aria-hidden="true" class="font-bold text-thd02-acc">Tip</span><p>Hover or Tab to <strong>v3.4.2</strong> in the header to switch versions &mdash; the menu is pure CSS.</p></div>
      <div aria-hidden="true" class="h-[60svh]"></div>
    </main>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd02-bg: var(--thd02-bg);
  --color-thd02-panel: var(--thd02-panel);
  --color-thd02-ink: var(--thd02-ink);
  --color-thd02-mut: var(--thd02-mut);
  --color-thd02-line: var(--thd02-line);
  --color-thd02-acc: var(--thd02-acc);
  --color-thd02-blue: var(--thd02-blue);
  --color-thd02-amber: var(--thd02-amber);
}

@theme {
  --font-thd02-sans: 'Hanken Grotesk', system-ui, sans-serif;
  --font-thd02-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.thd-02 {
  width: 100%;
  min-height: 100svh;
  --thd02-bg: #fbfcfb;
  --thd02-panel: #ffffff;
  --thd02-ink: #0f1a17;
  --thd02-mut: #56645f;
  --thd02-line: #e2e8e5;
  --thd02-acc: #0b7f63;
  --thd02-blue: #2563eb;
  --thd02-amber: #a15c07;
}

.thd-02:has(#thd-02-t:checked) {
  --thd02-bg: #0c1210;
  --thd02-panel: #121a17;
  --thd02-ink: #e8f0ed;
  --thd02-mut: #97a8a1;
  --thd02-line: #22302b;
  --thd02-acc: #34d3a4;
  --thd02-blue: #7aa7ff;
  --thd02-amber: #f3b54a;
}
```
