---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-mega-menu-header-css-grid/"
title: "Tailwind Mega Menu Header with CSS Grid"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "A mega panel that is a genuine CSS Grid — a capabilities column with icons, a 2×2 grid of use-case cards and a promo rail — opened by group-hover/mega or…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mega Menu Header with CSS Grid
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-mega-menu-header-css-grid/

A mega panel that is a genuine CSS Grid — a capabilities column with icons, a 2×2 grid of use-case cards and a promo rail — opened by group-hover/mega or group-focus-within/mega. Closed, the panel is invisible, so its links leave the tab order instead of swallowing keyboard focus.
## HTML
```html
<div class="thd-13 group/thd13 w-full min-h-svh bg-thd13-bg font-thd13-sans text-thd13-ink antialiased">
  <a href="#thd-13-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd13-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <header class="sticky top-0 z-40 border-b border-thd13-line bg-thd13-panel">
    <div class="mx-auto flex h-16 max-w-7xl items-center gap-4 px-[clamp(.75rem,3vw,1.5rem)]">
      <a href="#thd-13-main" class="flex items-center gap-2 text-lg font-extrabold tracking-tight"><span aria-hidden="true" class="grid size-7 grid-cols-2 gap-0.5"><span class="rounded-[3px] bg-thd13-acc"></span><span class="rounded-[3px] bg-amber-400"></span><span class="rounded-[3px] bg-sky-400"></span><span class="rounded-[3px] bg-thd13-acc/40"></span></span>Mosaic</a>
      <nav aria-label="Main" class="ml-4 hidden md:block">
        <ul class="flex items-center gap-1 text-sm font-semibold">
          <li class="group/mega before:pointer-events-none before:invisible before:fixed before:inset-0 before:top-16 before:-z-10 before:bg-black/25 before:opacity-0 before:transition-opacity before:content-[''] hover:before:visible hover:before:opacity-100 focus-within:before:visible focus-within:before:opacity-100">
            <a href="#thd-13-main" aria-haspopup="true" class="flex min-h-11 items-center gap-1 rounded-lg px-3 hover:bg-thd13-ink/5 group-hover/mega:bg-thd13-ink/5 group-hover/mega:text-thd13-acc">Platform <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true" class="size-3.5 transition-transform group-hover/mega:rotate-180 group-focus-within/mega:rotate-180"><path d="m6 9 6 6 6-6"/></svg></a>
            <div class="invisible absolute inset-x-0 top-full border-b border-thd13-line bg-thd13-panel opacity-0 shadow-[0_30px_60px_-30px_rgb(0_0_0/.3)] transition-[opacity,visibility,translate] duration-200 -translate-y-1 group-hover/mega:visible group-hover/mega:translate-y-0 group-hover/mega:opacity-100 group-focus-within/mega:visible group-focus-within/mega:translate-y-0 group-focus-within/mega:opacity-100">
              <div class="mx-auto grid max-w-7xl gap-8 px-[clamp(.75rem,3vw,1.5rem)] py-8 lg:grid-cols-[14rem_1fr_17rem]">
                <div>
                  <p class="mb-2 text-[11px] font-bold uppercase tracking-[.14em] text-thd13-mut">Capabilities</p>
                  <ul class="grid gap-0.5 font-medium">
                    <li><a href="#thd-13-main" class="flex min-h-10 items-center gap-2.5 rounded-lg px-2 hover:bg-thd13-ink/5 hover:text-thd13-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-thd13-acc"></span>Content model</a></li>
                    <li><a href="#thd-13-main" class="flex min-h-10 items-center gap-2.5 rounded-lg px-2 hover:bg-thd13-ink/5 hover:text-thd13-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-amber-400"></span>Workflows</a></li>
                    <li><a href="#thd-13-main" class="flex min-h-10 items-center gap-2.5 rounded-lg px-2 hover:bg-thd13-ink/5 hover:text-thd13-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-sky-400"></span>Localisation</a></li>
                    <li><a href="#thd-13-main" class="flex min-h-10 items-center gap-2.5 rounded-lg px-2 hover:bg-thd13-ink/5 hover:text-thd13-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-emerald-400"></span>Asset pipeline</a></li>
                    <li><a href="#thd-13-main" class="flex min-h-10 items-center gap-2.5 rounded-lg px-2 hover:bg-thd13-ink/5 hover:text-thd13-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-rose-400"></span>Permissions</a></li>
                    <li><a href="#thd-13-main" class="flex min-h-10 items-center gap-2.5 rounded-lg px-2 hover:bg-thd13-ink/5 hover:text-thd13-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-thd13-mut"></span>Audit log</a></li>
                  </ul>
                </div>
                <div>
                  <p class="mb-2 text-[11px] font-bold uppercase tracking-[.14em] text-thd13-mut">What teams build</p>
                  <ul class="grid gap-3 sm:grid-cols-2">
                    <li><a href="#thd-13-main" class="block h-full rounded-xl border border-thd13-line p-4 font-normal transition hover:-translate-y-0.5 hover:border-thd13-acc/40 hover:shadow-[0_12px_30px_-16px_var(--color-thd13-acc)]"><span class="block font-bold">Editorial desks</span><span class="mt-1 block text-sm text-thd13-mut">Draft, review and schedule with real approvals.</span></a></li>
                    <li><a href="#thd-13-main" class="block h-full rounded-xl border border-thd13-line p-4 font-normal transition hover:-translate-y-0.5 hover:border-thd13-acc/40 hover:shadow-[0_12px_30px_-16px_var(--color-thd13-acc)]"><span class="block font-bold">Design systems</span><span class="mt-1 block text-sm text-thd13-mut">One token source, every surface in sync.</span></a></li>
                    <li><a href="#thd-13-main" class="block h-full rounded-xl border border-thd13-line p-4 font-normal transition hover:-translate-y-0.5 hover:border-thd13-acc/40 hover:shadow-[0_12px_30px_-16px_var(--color-thd13-acc)]"><span class="flex items-center gap-2 font-bold">Commerce catalogues <span class="rounded-full bg-thd13-acc px-1.5 py-0.5 text-[10px] font-bold uppercase text-white">New</span></span><span class="mt-1 block text-sm text-thd13-mut">40k SKUs with variant-aware previews.</span></a></li>
                    <li><a href="#thd-13-main" class="block h-full rounded-xl border border-thd13-line p-4 font-normal transition hover:-translate-y-0.5 hover:border-thd13-acc/40 hover:shadow-[0_12px_30px_-16px_var(--color-thd13-acc)]"><span class="flex items-center gap-2 font-bold">Migrating from files <span class="rounded-full bg-amber-400/25 px-1.5 py-0.5 text-[10px] font-bold uppercase text-amber-700">Guide</span></span><span class="mt-1 block text-sm text-thd13-mut">A three-week plan that survived contact.</span></a></li>
                  </ul>
                </div>
                <div class="relative overflow-hidden rounded-2xl bg-thd13-acc p-5 text-white">
                  <div aria-hidden="true" class="absolute -right-10 -top-10 size-40 rounded-full bg-white/15"></div>
                  <p class="relative inline-flex items-center gap-1.5 rounded-full bg-white/20 px-2 py-0.5 text-[11px] font-bold uppercase"><span class="size-1.5 animate-pulse rounded-full bg-white"></span>Live</p>
                  <p class="relative mt-3 text-xl font-extrabold leading-tight">Workflow builder, now visual</p>
                  <p class="relative mt-2 text-sm font-normal text-white/85">Draw the states, set the approvers, ship it the same afternoon.</p>
                  <a href="#thd-13-main" class="relative mt-4 inline-flex min-h-10 items-center rounded-full bg-white px-4 text-sm font-bold text-thd13-acc">Watch the 4 min tour &rarr;</a>
                </div>
              </div>
            </div>
          </li>
          <li><a href="#thd-13-main" class="flex min-h-11 items-center rounded-lg px-3 hover:bg-thd13-ink/5">Solutions</a></li>
          <li><a href="#thd-13-main" class="flex min-h-11 items-center rounded-lg px-3 hover:bg-thd13-ink/5">Pricing</a></li>
          <li><a href="#thd-13-main" class="flex min-h-11 items-center rounded-lg px-3 hover:bg-thd13-ink/5">Docs</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-1.5">
        <input id="thd-13-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-13-t" class="grid size-11 cursor-pointer place-items-center rounded-full text-thd13-mut hover:bg-thd13-ink/5 hover:text-thd13-ink peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd13-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-[18px] group-has-[#thd-13-t:checked]/thd13:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-[18px] group-has-[#thd-13-t:checked]/thd13:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-13-main" class="hidden rounded-lg px-3 py-2 text-sm font-semibold hover:bg-thd13-ink/5 sm:block">Sign in</a>
        <a href="#thd-13-main" class="grid min-h-11 place-items-center whitespace-nowrap rounded-full bg-thd13-ink px-5 text-sm font-bold text-thd13-panel transition-colors hover:bg-thd13-acc hover:text-white">Book a demo</a>
      </div>
    </div>
  </header>
  <main id="thd-13-main" class="mx-auto max-w-7xl px-[clamp(.75rem,3vw,1.5rem)] py-[clamp(3rem,9vw,6rem)]">
    <h1 class="max-w-[16ch] text-[clamp(2.4rem,7vw,4.4rem)] font-extrabold leading-[1] tracking-[-.04em] text-balance">Structured content for teams that ship.</h1>
    <p class="mt-5 max-w-[50ch] text-lg text-thd13-mut">Hover or Tab to <strong class="text-thd13-ink">Platform</strong>: a three-track grid opens and the page dims behind it.</p>
    <div aria-hidden="true" class="h-[60svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd13-bg: var(--thd13-bg);
  --color-thd13-panel: var(--thd13-panel);
  --color-thd13-ink: var(--thd13-ink);
  --color-thd13-mut: var(--thd13-mut);
  --color-thd13-line: var(--thd13-line);
  --color-thd13-acc: var(--thd13-acc);
}

@theme {
  --font-thd13-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.thd-13 {
  width: 100%;
  min-height: 100svh;
  --thd13-bg: #f6f5fb;
  --thd13-panel: #ffffff;
  --thd13-ink: #15122b;
  --thd13-mut: #5a5775;
  --thd13-line: #e6e3f0;
  --thd13-acc: #5b3df5;
}

.thd-13:has(#thd-13-t:checked) {
  --thd13-bg: #0c0b16;
  --thd13-panel: #14121f;
  --thd13-ink: #eeecf8;
  --thd13-mut: #a4a1bd;
  --thd13-line: #2a2740;
  --thd13-acc: #8b74ff;
}
```
