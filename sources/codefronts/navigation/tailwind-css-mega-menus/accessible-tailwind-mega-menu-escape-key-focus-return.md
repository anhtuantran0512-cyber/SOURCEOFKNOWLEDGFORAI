---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/accessible-tailwind-mega-menu-escape-key-focus-return/"
title: "Accessible Tailwind Mega Menu with Escape Key and Focus Return"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "WCAG 1.4.13 says content that appears on hover or focus must be dismissible. This dark app shell implements the full contract: Escape closes the open panel…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind Mega Menu with Escape Key and Focus Return
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/accessible-tailwind-mega-menu-escape-key-focus-return/

WCAG 1.4.13 says content that appears on hover or focus must be dismissible. This dark app shell implements the full contract: Escape closes the open panel from anywhere inside it and returns focus to its trigger, aria-expanded tracks the real state, focus leaving the item closes it, and Tab onto a trigger does not throw a panel over the page. The panel only ever renders from [data-open].
## HTML
```html
<section class="tmm-07 relative w-full min-h-svh bg-tmm07-bg font-tmm07-sans leading-normal text-tmm07-ink [&_:focus-visible]:rounded-md [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm07-acc" aria-labelledby="tmm07-title">
  <h2 class="sr-only" id="tmm07-title">Talon workspace</h2>

  <div class="absolute top-2.5 right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm07-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-md border border-tmm07-line bg-tmm07-surf text-tmm07-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm07-acc" for="tmm07-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b border-tmm07-line bg-tmm07-surf">
    <div class="mx-auto flex min-h-16 w-[min(84rem,calc(100%-2rem))] flex-wrap items-stretch gap-x-[clamp(0.5rem,2vw,1.25rem)] pr-15 max-[52rem]:flex-col max-[52rem]:py-2.5">
      <a class="inline-flex items-center font-tmm07-mono text-[0.85rem]/none font-bold tracking-[0.3em] text-tmm07-acc" href="#tmm07-title">TALON</a>
      <span class="inline-flex min-h-7 w-fit items-center gap-1.5 self-center rounded border border-tmm07-line px-2.5 font-tmm07-mono text-[0.74rem]/none font-medium text-tmm07-mut"><span class="size-[7px] rounded-full bg-tmm07-acc shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-tmm07-acc)_25%,transparent)]" aria-hidden="true"></span>Northwind &middot; production</span>
      <nav data-tmm07-nav class="flex min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-0.5 max-[52rem]:flex-col">
          <li data-tmm07-item class="flex items-stretch max-[52rem]:block">
            <button data-tmm07-trigger type="button" aria-expanded="false" aria-controls="tmm07-panel-workspace" class="inline-flex min-h-11 cursor-pointer items-center px-3.5 font-tmm07-mono text-[0.86rem]/none font-semibold tracking-[0.02em] text-tmm07-ink transition-colors hover:text-tmm07-acc tmm07-open:bg-tmm07-acc tmm07-open:text-tmm07-on-acc!">Workspace</button>
            <div class="invisible absolute inset-x-0 top-full z-30 -translate-y-2 border-b border-tmm07-line bg-tmm07-panel opacity-0 shadow-tmm07-panel pointer-events-none transition-[opacity,translate,visibility] duration-150 tmm07-open:visible tmm07-open:translate-y-0 tmm07-open:opacity-100 tmm07-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:translate-y-0 max-[52rem]:opacity-100 max-[52rem]:tmm07-open:block" id="tmm07-panel-workspace" aria-label="Workspace">
              <div class="mx-auto grid w-[min(84rem,calc(100%-2rem))] gap-[clamp(0.9rem,2.5vw,1.75rem)] py-[clamp(1rem,3vw,1.6rem)] min-[62rem]:grid-cols-[minmax(0,1fr)_17rem] max-[52rem]:w-full max-[52rem]:px-4">
                <ul class="min-w-0 -translate-y-3 opacity-0 transition-[opacity,translate] duration-[160ms,240ms] ease-[linear,cubic-bezier(0.2,0.7,0.3,1)] delay-20 tmm07-open:translate-y-0 tmm07-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none grid grid-cols-[repeat(auto-fit,minmax(min(100%,14rem),1fr))] border-t border-l border-tmm07-line">
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 7h7l2 2h9v10H3Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">Projects</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">34 active</span></a></li>
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="3.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 19c.8-3 3.2-4.5 6-4.5s5.2 1.5 6 4.5M16 6.5a3 3 0 0 1 0 5.6M18 14.8c1.4.6 2.4 2 2.8 4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">People</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">128 seats</span></a></li>
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 20V4M4 20h16M8 16v-4M12 16V8M16 16v-6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">Insights</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">daily digest</span></a></li>
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M13 3 5 13h6l-1 8 8-10h-6Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">Automations</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">12 running</span></a></li>
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="3" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">Settings</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">workspace</span></a></li>
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 4h14v16H5ZM9 9h6M9 13h6M9 17h3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">Audit log</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">90 days</span></a></li>
                </ul>
                <div class="min-w-0 -translate-y-3 opacity-0 transition-[opacity,translate] duration-[160ms,240ms] ease-[linear,cubic-bezier(0.2,0.7,0.3,1)] delay-65 tmm07-open:translate-y-0 tmm07-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none grid content-start gap-1 border border-tmm07-line p-3.5">
                  <p class="mb-1 font-tmm07-mono text-[0.66rem]/none font-bold tracking-[0.2em] text-tmm07-mut uppercase">Switch workspace</p>
                  <ul class="grid gap-px">
                    <li><a href="#tmm07-title" class="grid min-h-11 grid-cols-[26px_minmax(0,1fr)_auto] items-center gap-2.5 rounded px-1.5 text-[0.87rem] text-tmm07-ink transition-colors hover:bg-tmm07-acc/12"><span class="grid h-[22px] w-[26px] place-items-center rounded-[3px] bg-tmm07-acc/20 font-tmm07-mono text-[0.64rem]/none font-bold text-tmm07-acc" aria-hidden="true">NW</span><span class="truncate">Northwind</span><span class="font-tmm07-mono text-[0.66rem]/none font-medium tracking-[0.08em] text-tmm07-mut uppercase">production</span></a></li>
                    <li><a href="#tmm07-title" class="grid min-h-11 grid-cols-[26px_minmax(0,1fr)_auto] items-center gap-2.5 rounded px-1.5 text-[0.87rem] text-tmm07-ink transition-colors hover:bg-tmm07-acc/12"><span class="grid h-[22px] w-[26px] place-items-center rounded-[3px] bg-tmm07-acc/20 font-tmm07-mono text-[0.64rem]/none font-bold text-tmm07-acc" aria-hidden="true">OR</span><span class="truncate">Orbit Retail</span><span class="font-tmm07-mono text-[0.66rem]/none font-medium tracking-[0.08em] text-tmm07-mut uppercase">staging</span></a></li>
                    <li><a href="#tmm07-title" class="grid min-h-11 grid-cols-[26px_minmax(0,1fr)_auto] items-center gap-2.5 rounded px-1.5 text-[0.87rem] text-tmm07-ink transition-colors hover:bg-tmm07-acc/12"><span class="grid h-[22px] w-[26px] place-items-center rounded-[3px] bg-tmm07-acc/20 font-tmm07-mono text-[0.64rem]/none font-bold text-tmm07-acc" aria-hidden="true">FS</span><span class="truncate">Fern Studio</span><span class="font-tmm07-mono text-[0.66rem]/none font-medium tracking-[0.08em] text-tmm07-mut uppercase">sandbox</span></a></li>
                  </ul>
                  <p class="mt-2 flex items-center gap-1.5 border-t border-tmm07-line pt-2.5 font-tmm07-mono text-[0.68rem]/none text-tmm07-mut"><kbd class="inline-grid h-[22px] min-w-[22px] place-items-center rounded border border-tmm07-line px-1 text-[0.66rem] font-semibold">Esc</kbd> closes and returns focus</p>
                </div>
              </div>
            </div>
          </li>

          <li data-tmm07-item class="flex items-stretch max-[52rem]:block">
            <button data-tmm07-trigger type="button" aria-expanded="false" aria-controls="tmm07-panel-develop" class="inline-flex min-h-11 cursor-pointer items-center px-3.5 font-tmm07-mono text-[0.86rem]/none font-semibold tracking-[0.02em] text-tmm07-ink transition-colors hover:text-tmm07-acc tmm07-open:bg-tmm07-acc tmm07-open:text-tmm07-on-acc!">Develop</button>
            <div class="invisible absolute inset-x-0 top-full z-30 -translate-y-2 border-b border-tmm07-line bg-tmm07-panel opacity-0 shadow-tmm07-panel pointer-events-none transition-[opacity,translate,visibility] duration-150 tmm07-open:visible tmm07-open:translate-y-0 tmm07-open:opacity-100 tmm07-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:translate-y-0 max-[52rem]:opacity-100 max-[52rem]:tmm07-open:block" id="tmm07-panel-develop" aria-label="Develop">
              <div class="mx-auto grid w-[min(84rem,calc(100%-2rem))] gap-[clamp(0.9rem,2.5vw,1.75rem)] py-[clamp(1rem,3vw,1.6rem)] min-[62rem]:grid-cols-[minmax(0,1fr)_17rem] max-[52rem]:w-full max-[52rem]:px-4">
                <ul class="min-w-0 -translate-y-3 opacity-0 transition-[opacity,translate] duration-[160ms,240ms] ease-[linear,cubic-bezier(0.2,0.7,0.3,1)] delay-20 tmm07-open:translate-y-0 tmm07-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none grid grid-cols-[repeat(auto-fit,minmax(min(100%,14rem),1fr))] border-t border-l border-tmm07-line">
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m8 8-4 4 4 4M16 8l4 4-4 4M14 5l-4 14" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">API reference</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">v4</span></a></li>
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h12l-3-3M20 17H8l3 3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">Migration guide</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">3 to 4</span></a></li>
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 12h4l2-5 4 10 2-5h6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">Status page</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">all systems go</span></a></li>
                  <li class="flex"><a href="#tmm07-title" class="grid min-h-15 w-full grid-cols-[22px_minmax(0,1fr)] grid-rows-[auto_auto] content-center items-center gap-x-3 border-r border-b border-tmm07-line bg-tmm07-panel px-3.5 py-3 text-tmm07-ink transition-colors hover:bg-[color-mix(in_oklab,var(--color-tmm07-acc)_14%,var(--color-tmm07-panel))]"><svg class="row-span-2 size-[22px] text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 5h16v14H4ZM8 10l2 2-2 2M12 14h4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg><b class="min-w-0 text-[0.9rem]/snug font-semibold">CLI download</b><span class="min-w-0 font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">1.9 MB</span></a></li>
                </ul>
                <div class="min-w-0 -translate-y-3 opacity-0 transition-[opacity,translate] duration-[160ms,240ms] ease-[linear,cubic-bezier(0.2,0.7,0.3,1)] delay-65 tmm07-open:translate-y-0 tmm07-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:opacity-100 motion-reduce:transition-none grid content-start gap-1 border border-tmm07-line p-3.5">
                  <p class="mb-1 font-tmm07-mono text-[0.66rem]/none font-bold tracking-[0.2em] text-tmm07-mut uppercase">Recent</p>
                  <ul class="grid gap-px">
                    <li><a href="#tmm07-title" class="grid min-h-11 grid-cols-[26px_minmax(0,1fr)_auto] items-center gap-2.5 rounded px-1.5 text-[0.87rem] text-tmm07-ink transition-colors hover:bg-tmm07-acc/12"><span class="grid h-[22px] w-[26px] place-items-center rounded-[3px] bg-tmm07-acc/20 font-tmm07-mono text-[0.64rem]/none font-bold text-tmm07-acc" aria-hidden="true">#</span><span class="truncate">4471 queue latency</span><span class="font-tmm07-mono text-[0.66rem]/none font-medium tracking-[0.08em] text-tmm07-mut uppercase">open</span></a></li>
                    <li><a href="#tmm07-title" class="grid min-h-11 grid-cols-[26px_minmax(0,1fr)_auto] items-center gap-2.5 rounded px-1.5 text-[0.87rem] text-tmm07-ink transition-colors hover:bg-tmm07-acc/12"><span class="grid h-[22px] w-[26px] place-items-center rounded-[3px] bg-tmm07-acc/20 font-tmm07-mono text-[0.64rem]/none font-bold text-tmm07-acc" aria-hidden="true">#</span><span class="truncate">4468 canary rollout</span><span class="font-tmm07-mono text-[0.66rem]/none font-medium tracking-[0.08em] text-tmm07-mut uppercase">merged</span></a></li>
                  </ul>
                  <p class="mt-2 flex items-center gap-1.5 border-t border-tmm07-line pt-2.5 font-tmm07-mono text-[0.68rem]/none text-tmm07-mut"><kbd class="inline-grid h-[22px] min-w-[22px] place-items-center rounded border border-tmm07-line px-1 text-[0.66rem] font-semibold">Esc</kbd> closes and returns focus</p>
                </div>
              </div>
            </div>
          </li>

          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 font-tmm07-mono text-[0.86rem]/none font-semibold text-tmm07-ink hover:text-tmm07-acc" href="#tmm07-title">Billing</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-2.5 max-[52rem]:ml-0">
        <span class="inline-flex gap-0.5" aria-hidden="true"><kbd class="inline-grid h-[22px] min-w-[22px] place-items-center rounded border border-tmm07-line font-tmm07-mono text-[0.7rem]/none font-semibold text-tmm07-mut">&#8984;</kbd><kbd class="inline-grid h-[22px] min-w-[22px] place-items-center rounded border border-tmm07-line font-tmm07-mono text-[0.7rem]/none font-semibold text-tmm07-mut">K</kbd></span>
        <span class="grid size-[30px] place-items-center rounded-full bg-tmm07-acc/26 font-tmm07-mono text-[0.7rem]/none font-bold text-tmm07-acc" aria-hidden="true">PS</span>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(84rem,calc(100%-2rem))] py-[clamp(1.5rem,5vw,3rem)]">
    <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))] gap-3">
      <div class="grid min-w-0 content-start gap-2 border border-tmm07-line bg-tmm07-surf p-3"><p class="flex items-center justify-between font-tmm07-mono text-[0.7rem]/none font-bold tracking-[0.18em] text-tmm07-mut uppercase">In progress <span class="text-tmm07-acc">4</span></p><article class="grid gap-0.5 border border-tmm07-line bg-tmm07-panel px-3.5 py-3"><b class="flex items-center gap-2 text-[0.88rem]/snug font-semibold">Region failover drill</b><span class="font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">Priya Sharma &middot; due Fri</span></article><article class="grid gap-0.5 border border-tmm07-line bg-tmm07-panel px-3.5 py-3"><b class="flex items-center gap-2 text-[0.88rem]/snug font-semibold">Trim CLI binary</b><span class="font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">Sam Rivera &middot; due Mon</span></article></div>
      <div class="grid min-w-0 content-start gap-2 border border-tmm07-line bg-tmm07-surf p-3"><p class="flex items-center justify-between font-tmm07-mono text-[0.7rem]/none font-bold tracking-[0.18em] text-tmm07-mut uppercase">In review <span class="text-tmm07-acc">2</span></p><article class="grid gap-0.5 border border-tmm07-line bg-tmm07-panel px-3.5 py-3"><b class="flex items-center gap-2 text-[0.88rem]/snug font-semibold">Read replica docs</b><span class="font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">Alex Chen &middot; 2 approvals</span></article></div>
      <div class="grid min-w-0 content-start gap-2 border border-tmm07-line bg-tmm07-surf p-3"><p class="flex items-center justify-between font-tmm07-mono text-[0.7rem]/none font-bold tracking-[0.18em] text-tmm07-mut uppercase">Shipped <span class="text-tmm07-acc">9</span></p><article class="grid gap-0.5 border border-tmm07-line bg-tmm07-panel px-3.5 py-3"><b class="flex items-center gap-2 text-[0.88rem]/snug font-semibold"><svg class="size-3.5 text-tmm07-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m5 12 5 5 9-10" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>Canary rollout v4.2</b><span class="font-tmm07-mono text-[0.72rem]/snug font-medium text-tmm07-mut">Jordan Lee &middot; today</span></article></div>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm07-bg: #000000;
  --color-tmm07-bg: oklch(0 0 0);
  --color-tmm07-surf: #0c0c10;
  --color-tmm07-surf: oklch(0.15 0.008 285);
  --color-tmm07-panel: #101016;
  --color-tmm07-panel: oklch(0.17 0.01 285);
  --color-tmm07-line: #26262f;
  --color-tmm07-line: oklch(0.28 0.014 285);
  --color-tmm07-ink: #f4f4f6;
  --color-tmm07-ink: oklch(0.97 0.004 285);
  --color-tmm07-mut: #9696a3;
  --color-tmm07-mut: oklch(0.68 0.018 285);
  --color-tmm07-acc: #a78bfa;
  --color-tmm07-acc: oklch(0.71 0.16 293);
  --color-tmm07-on-acc: #14101f;
  --color-tmm07-on-acc: oklch(0.17 0.03 293);
  --font-tmm07-mono: 'JetBrains Mono', ui-monospace, monospace;
  --font-tmm07-sans: 'Manrope', system-ui, sans-serif;
  --shadow-tmm07-panel: 0 30px 60px -30px rgb(0 0 0 / 0.8);
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-07 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-07:has(#tmm07-theme:checked) {
  --color-tmm07-bg: #f5f4f8;
  --color-tmm07-bg: oklch(0.97 0.006 290);
  --color-tmm07-surf: #ffffff;
  --color-tmm07-surf: oklch(1 0 0);
  --color-tmm07-panel: #fbfaff;
  --color-tmm07-panel: oklch(0.988 0.006 290);
  --color-tmm07-line: #dedbe8;
  --color-tmm07-line: oklch(0.89 0.016 290);
  --color-tmm07-ink: #15131c;
  --color-tmm07-ink: oklch(0.19 0.015 290);
  --color-tmm07-mut: #5f5b6e;
  --color-tmm07-mut: oklch(0.48 0.025 290);
  --color-tmm07-acc: #6d3fe0;
  --color-tmm07-acc: oklch(0.5 0.22 290);
  --color-tmm07-on-acc: #ffffff;
  --color-tmm07-on-acc: oklch(1 0 0);
}

@media (prefers-color-scheme: light) {
  .tmm-07 {
    --color-tmm07-bg: #f5f4f8;
    --color-tmm07-bg: oklch(0.97 0.006 290);
    --color-tmm07-surf: #ffffff;
    --color-tmm07-surf: oklch(1 0 0);
    --color-tmm07-panel: #fbfaff;
    --color-tmm07-panel: oklch(0.988 0.006 290);
    --color-tmm07-line: #dedbe8;
    --color-tmm07-line: oklch(0.89 0.016 290);
    --color-tmm07-ink: #15131c;
    --color-tmm07-ink: oklch(0.19 0.015 290);
    --color-tmm07-mut: #5f5b6e;
    --color-tmm07-mut: oklch(0.48 0.025 290);
    --color-tmm07-acc: #6d3fe0;
    --color-tmm07-acc: oklch(0.5 0.22 290);
    --color-tmm07-on-acc: #ffffff;
    --color-tmm07-on-acc: oklch(1 0 0);
  }

  .tmm-07:has(#tmm07-theme:checked) {
    --color-tmm07-bg: #000000;
    --color-tmm07-bg: oklch(0 0 0);
    --color-tmm07-surf: #0c0c10;
    --color-tmm07-surf: oklch(0.15 0.008 285);
    --color-tmm07-panel: #101016;
    --color-tmm07-panel: oklch(0.17 0.01 285);
    --color-tmm07-line: #26262f;
    --color-tmm07-line: oklch(0.28 0.014 285);
    --color-tmm07-ink: #f4f4f6;
    --color-tmm07-ink: oklch(0.97 0.004 285);
    --color-tmm07-mut: #9696a3;
    --color-tmm07-mut: oklch(0.68 0.018 285);
    --color-tmm07-acc: #a78bfa;
    --color-tmm07-acc: oklch(0.71 0.16 293);
    --color-tmm07-on-acc: #14101f;
    --color-tmm07-on-acc: oklch(0.17 0.03 293);
  }
}
/* The open state comes ONLY from the script: [data-open] on the item. */

@custom-variant tmm07-open (&: where([data-tmm07-item][data-open] *));
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tmm-07');
  if (!root || root.__tmmCleanup) return;
  const nav = root.querySelector('[data-tmm07-nav]');
  const canHover = window.matchMedia('(hover: hover)');
  let returning = false; // true while Escape hands focus back, so focusin does not re-open

  const itemOf = (el) => el.closest('[data-tmm07-item]');
  const setOpen = (item, on) => {
    item.toggleAttribute('data-open', on);
    item.querySelector('[data-tmm07-trigger]').setAttribute('aria-expanded', String(on));
  };
  const closeAll = (except) => nav.querySelectorAll('[data-tmm07-item][data-open]').forEach((i) => { if (i !== except) setOpen(i, false); });

  const onClick = (e) => {
    const t = e.target.closest('[data-tmm07-trigger]');
    if (!t) return;
    const item = itemOf(t), open = item.hasAttribute('data-open');
    if (open && canHover.matches && e.pointerType === 'mouse') return; // hover already opened it
    closeAll(item); setOpen(item, !open);
  };
  const onKeyDown = (e) => {
    if (e.key !== 'Escape') return;
    const item = itemOf(e.target);
    if (!item || !item.hasAttribute('data-open')) return;
    e.preventDefault();
    setOpen(item, false);
    returning = true;
    item.querySelector('[data-tmm07-trigger]').focus();
    returning = false;
  };
  const onFocusIn = (e) => {
    const item = itemOf(e.target);
    if (!item || returning) return;
    if (e.target.matches('[data-tmm07-trigger]') && !item.contains(e.relatedTarget)) { closeAll(item); return; }
    closeAll(item); setOpen(item, true);
  };
  const onFocusOut = (e) => {
    const item = itemOf(e.target);
    if (item && (!e.relatedTarget || !item.contains(e.relatedTarget))) setOpen(item, false);
  };
  const onEnter = (e) => {
    if (!canHover.matches || e.pointerType !== 'mouse') return;
    const item = itemOf(e.target);
    if (item && !item.hasAttribute('data-open')) { closeAll(item); setOpen(item, true); }
  };
  const onLeave = (e) => {
    if (!canHover.matches) return;
    const item = itemOf(e.target);
    if (!item || item.contains(document.activeElement)) return;
    if (e.relatedTarget && nav.contains(e.relatedTarget)) return;
    setOpen(item, false);
  };

  nav.addEventListener('click', onClick);
  nav.addEventListener('keydown', onKeyDown);
  nav.addEventListener('focusin', onFocusIn);
  nav.addEventListener('focusout', onFocusOut);
  nav.addEventListener('pointerenter', onEnter, true);
  nav.addEventListener('pointerleave', onLeave, true);
  root.__tmmCleanup = () => {
    nav.removeEventListener('click', onClick);
    nav.removeEventListener('keydown', onKeyDown);
    nav.removeEventListener('focusin', onFocusIn);
    nav.removeEventListener('focusout', onFocusOut);
    nav.removeEventListener('pointerenter', onEnter, true);
    nav.removeEventListener('pointerleave', onLeave, true);
  };
})();
```
