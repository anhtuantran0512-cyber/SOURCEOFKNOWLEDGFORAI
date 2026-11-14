---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-shared-panel-swap-content/"
title: "Tailwind Mega Menu with One Shared Panel That Swaps Content"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "Instead of one panel per item, three triggers share one glass panel that stays open while its content swaps &mdash; the continuous feel of a streaming app's…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mega Menu with One Shared Panel That Swaps Content
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-shared-panel-swap-content/

Instead of one panel per item, three triggers share one glass panel that stays open while its content swaps &mdash; the continuous feel of a streaming app's header. The panel height animates with grid-rows-[0fr] &rarr; data-open:grid-rows-[1fr], and each swapped-in section replays a lateral slide using Tailwind's starting: variant (@starting-style), so the script only flips hidden and two attributes.
## HTML
```html
<section class="tmm-12 relative flow-root w-full min-h-svh bg-tmm12-bg bg-[radial-gradient(60rem_30rem_at_18%_-8%,color-mix(in_oklab,var(--color-tmm12-acc)_22%,transparent),transparent_62%),radial-gradient(52rem_26rem_at_92%_6%,rgb(168_85_247/0.18),transparent_60%)] font-tmm12-sans leading-[1.55] text-tmm12-ink [&_:focus-visible]:rounded-lg [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm12-acc" aria-labelledby="tmm12-title">
  <h2 class="sr-only" id="tmm12-title">Prism TV</h2>

  <header data-tmm12-shell class="relative z-10 mx-auto mt-[clamp(1rem,3vw,1.75rem)] w-[min(76rem,calc(100%-2rem))] overflow-hidden rounded-[20px] border border-tmm12-line bg-tmm12-surf/76 shadow-tmm12-shell backdrop-blur-lg">
    <div class="absolute top-3 right-3 z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm12-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-xl border border-tmm12-line bg-tmm12-solid text-tmm12-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm12-acc" for="tmm12-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>
    <div class="flex min-h-17 flex-wrap items-center gap-[clamp(0.5rem,2vw,1.75rem)] border-b border-tmm12-line pr-16 pl-[clamp(0.85rem,2.5vw,1.4rem)] max-[52rem]:flex-col max-[52rem]:items-stretch max-[52rem]:py-2.5">
      <a class="inline-flex items-center gap-2 font-tmm12-display text-[1.05rem]/none font-bold tracking-[-0.03em] text-tmm12-ink" href="#tmm12-title">
        <svg class="size-5 text-tmm12-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="12" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8 21h8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="m10 8.5 4.5 2.5-4.5 2.5Z" fill="currentColor"/></svg>
        Prism<b class="text-tmm12-acc">TV</b>
      </a>
      <nav data-tmm12-nav class="min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-0.5 max-[52rem]:flex-col">
          <li><button data-tmm12-trigger data-for="tmm12-sec-browse" type="button" aria-expanded="false" aria-controls="tmm12-panel" class="inline-flex min-h-11 cursor-pointer items-center rounded-[10px] px-4 font-tmm12-display text-[0.92rem]/none font-semibold text-tmm12-ink transition-colors hover:text-tmm12-acc aria-expanded:bg-tmm12-acc/16 aria-expanded:text-tmm12-acc">Browse</button></li>
          <li><button data-tmm12-trigger data-for="tmm12-sec-live" type="button" aria-expanded="false" aria-controls="tmm12-panel" class="inline-flex min-h-11 cursor-pointer items-center rounded-[10px] px-4 font-tmm12-display text-[0.92rem]/none font-semibold text-tmm12-ink transition-colors hover:text-tmm12-acc aria-expanded:bg-tmm12-acc/16 aria-expanded:text-tmm12-acc">Live</button></li>
          <li><button data-tmm12-trigger data-for="tmm12-sec-kids" type="button" aria-expanded="false" aria-controls="tmm12-panel" class="inline-flex min-h-11 cursor-pointer items-center rounded-[10px] px-4 font-tmm12-display text-[0.92rem]/none font-semibold text-tmm12-ink transition-colors hover:text-tmm12-acc aria-expanded:bg-tmm12-acc/16 aria-expanded:text-tmm12-acc">Kids</button></li>
          <li><a class="inline-flex min-h-11 items-center rounded-[10px] px-4 font-tmm12-display text-[0.92rem]/none font-semibold text-tmm12-ink hover:text-tmm12-acc" href="#tmm12-title">My list</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-2 max-[52rem]:ml-0">
        <span class="grid size-10 place-items-center rounded-full border border-tmm12-line text-tmm12-mut" aria-hidden="true"><svg class="size-[18px]" viewBox="0 0 24 24" focusable="false"><circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
        <span class="grid size-[34px] place-items-center rounded-[10px] bg-tmm12-acc/24 font-tmm12-display text-[0.74rem]/none font-bold text-tmm12-acc" aria-hidden="true">SR</span>
      </div>
    </div>
    <div data-tmm12-panel class="group/panel relative grid grid-rows-[0fr] transition-[grid-template-rows] duration-280 ease-tmm12-out data-open:grid-rows-[1fr] motion-reduce:transition-none" id="tmm12-panel" aria-label="Browse">
      <div class="invisible min-h-0 overflow-hidden group-data-open/panel:visible">
        <div class="flex flex-wrap gap-1.5 px-[clamp(0.85rem,2.5vw,1.4rem)] pt-3" role="presentation">
          <span data-tab="tmm12-sec-browse" class="inline-flex min-h-[26px] items-center rounded-full bg-tmm12-ink/8 px-2.5 font-tmm12-display text-[0.68rem]/none font-semibold tracking-[0.1em] text-tmm12-mut uppercase transition-colors data-active:bg-tmm12-acc data-active:text-tmm12-on-acc">Browse</span>
          <span data-tab="tmm12-sec-live" class="inline-flex min-h-[26px] items-center rounded-full bg-tmm12-ink/8 px-2.5 font-tmm12-display text-[0.68rem]/none font-semibold tracking-[0.1em] text-tmm12-mut uppercase transition-colors data-active:bg-tmm12-acc data-active:text-tmm12-on-acc">Live</span>
          <span data-tab="tmm12-sec-kids" class="inline-flex min-h-[26px] items-center rounded-full bg-tmm12-ink/8 px-2.5 font-tmm12-display text-[0.68rem]/none font-semibold tracking-[0.1em] text-tmm12-mut uppercase transition-colors data-active:bg-tmm12-acc data-active:text-tmm12-on-acc">Kids</span>
        </div>
        <section class="px-[clamp(0.85rem,2.5vw,1.4rem)] pt-[clamp(0.9rem,2.6vw,1.4rem)] pb-[clamp(1.1rem,3vw,1.6rem)]" id="tmm12-sec-browse" aria-label="Browse">
              <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[clamp(0.85rem,2.6vw,2rem)] transition-[opacity,translate] duration-300 ease-tmm12-out starting:translate-x-4 starting:opacity-0 motion-reduce:transition-none">
                <div class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[220ms,320ms] ease-tmm12-out delay-40 group-data-open/panel:translate-x-0 group-data-open/panel:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none">
                  <h3 class="mb-1.5 font-tmm12-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm12-mut uppercase">Genres</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Drama</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Documentary</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Comedy</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Thriller</a></li>
                  </ul>
                </div>
                <div class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[220ms,320ms] ease-tmm12-out delay-90 group-data-open/panel:translate-x-0 group-data-open/panel:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none">
                  <h3 class="mb-1.5 font-tmm12-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm12-mut uppercase">Collections</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Prism Originals</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Award winners</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Leaving soon</a></li>
                  </ul>
                </div>
                <ul class="col-span-2 grid min-w-0 grid-cols-[repeat(auto-fit,minmax(min(100%,9rem),1fr))] gap-2.5 max-[52rem]:col-auto">
                  <li><a href="#tmm12-title" class="group/tile grid min-w-0 gap-0.5 text-tmm12-ink"><span class="relative block aspect-video overflow-hidden rounded-[10px] bg-linear-140 from-[#3b82f6] to-[#8b5cf6]" aria-hidden="true"><span class="absolute inset-0 grid place-items-center bg-black/30 opacity-0 transition-opacity group-hover/tile:opacity-100"><svg class="size-9 rounded-full bg-white/90 p-2.5 text-black" viewBox="0 0 24 24"><path d="M7 4v16l13-8Z" fill="currentColor"/></svg></span></span><b class="mt-1 min-w-0 font-tmm12-display text-[0.88rem]/tight font-semibold group-hover/tile:text-tmm12-acc">Northwind</b><span class="text-[0.75rem] text-tmm12-mut">S2 &middot; new episode</span></a></li>
                  <li><a href="#tmm12-title" class="group/tile grid min-w-0 gap-0.5 text-tmm12-ink"><span class="relative block aspect-video overflow-hidden rounded-[10px] bg-linear-140 from-[#0ea5e9] to-[#14b8a6]" aria-hidden="true"><span class="absolute inset-0 grid place-items-center bg-black/30 opacity-0 transition-opacity group-hover/tile:opacity-100"><svg class="size-9 rounded-full bg-white/90 p-2.5 text-black" viewBox="0 0 24 24"><path d="M7 4v16l13-8Z" fill="currentColor"/></svg></span></span><b class="mt-1 min-w-0 font-tmm12-display text-[0.88rem]/tight font-semibold group-hover/tile:text-tmm12-acc">The Long Coast</b><span class="text-[0.75rem] text-tmm12-mut">Documentary</span></a></li>
                  <li><a href="#tmm12-title" class="group/tile grid min-w-0 gap-0.5 text-tmm12-ink"><span class="relative block aspect-video overflow-hidden rounded-[10px] bg-linear-140 from-[#f43f5e] to-[#f59e0b]" aria-hidden="true"><span class="absolute inset-0 grid place-items-center bg-black/30 opacity-0 transition-opacity group-hover/tile:opacity-100"><svg class="size-9 rounded-full bg-white/90 p-2.5 text-black" viewBox="0 0 24 24"><path d="M7 4v16l13-8Z" fill="currentColor"/></svg></span></span><b class="mt-1 min-w-0 font-tmm12-display text-[0.88rem]/tight font-semibold group-hover/tile:text-tmm12-acc">Basalt</b><span class="text-[0.75rem] text-tmm12-mut">Limited series</span></a></li>
                </ul>
              </div>
            </section>
        <section class="px-[clamp(0.85rem,2.5vw,1.4rem)] pt-[clamp(0.9rem,2.6vw,1.4rem)] pb-[clamp(1.1rem,3vw,1.6rem)]" id="tmm12-sec-live" aria-label="Live" hidden>
              <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[clamp(0.85rem,2.6vw,2rem)] transition-[opacity,translate] duration-300 ease-tmm12-out starting:translate-x-4 starting:opacity-0 motion-reduce:transition-none">
                <div class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[220ms,320ms] ease-tmm12-out delay-40 group-data-open/panel:translate-x-0 group-data-open/panel:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none">
                  <h3 class="mb-1.5 font-tmm12-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm12-mut uppercase">Channels</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Prism One</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Prism News</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Prism Sport</a></li>
                  </ul>
                </div>
                <div class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[220ms,320ms] ease-tmm12-out delay-90 group-data-open/panel:translate-x-0 group-data-open/panel:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none">
                  <h3 class="mb-1.5 font-tmm12-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm12-mut uppercase">Tonight</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">20:00 &mdash; Match of the week</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">21:30 &mdash; Late review</a></li>
                  </ul>
                </div>
                <ul class="col-span-2 grid min-w-0 grid-cols-[repeat(auto-fit,minmax(min(100%,9rem),1fr))] gap-2.5 max-[52rem]:col-auto">
                  <li><a href="#tmm12-title" class="group/tile grid min-w-0 gap-0.5 text-tmm12-ink"><span class="relative block aspect-video overflow-hidden rounded-[10px] bg-linear-140 from-[#6366f1] to-[#0ea5e9]" aria-hidden="true"><span class="absolute inset-0 grid place-items-center bg-black/30 opacity-0 transition-opacity group-hover/tile:opacity-100"><svg class="size-9 rounded-full bg-white/90 p-2.5 text-black" viewBox="0 0 24 24"><path d="M7 4v16l13-8Z" fill="currentColor"/></svg></span></span><b class="mt-1 min-w-0 font-tmm12-display text-[0.88rem]/tight font-semibold group-hover/tile:text-tmm12-acc">On now</b><span class="text-[0.75rem] text-tmm12-mut">Prism News at Six</span></a></li>
                  <li><a href="#tmm12-title" class="group/tile grid min-w-0 gap-0.5 text-tmm12-ink"><span class="relative block aspect-video overflow-hidden rounded-[10px] bg-linear-140 from-[#3b82f6] to-[#8b5cf6]" aria-hidden="true"><span class="absolute inset-0 grid place-items-center bg-black/30 opacity-0 transition-opacity group-hover/tile:opacity-100"><svg class="size-9 rounded-full bg-white/90 p-2.5 text-black" viewBox="0 0 24 24"><path d="M7 4v16l13-8Z" fill="currentColor"/></svg></span></span><b class="mt-1 min-w-0 font-tmm12-display text-[0.88rem]/tight font-semibold group-hover/tile:text-tmm12-acc">Up next</b><span class="text-[0.75rem] text-tmm12-mut">Coastal Rescue</span></a></li>
                </ul>
              </div>
            </section>
        <section class="px-[clamp(0.85rem,2.5vw,1.4rem)] pt-[clamp(0.9rem,2.6vw,1.4rem)] pb-[clamp(1.1rem,3vw,1.6rem)]" id="tmm12-sec-kids" aria-label="Kids" hidden>
              <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-[clamp(0.85rem,2.6vw,2rem)] transition-[opacity,translate] duration-300 ease-tmm12-out starting:translate-x-4 starting:opacity-0 motion-reduce:transition-none">
                <div class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[220ms,320ms] ease-tmm12-out delay-40 group-data-open/panel:translate-x-0 group-data-open/panel:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none">
                  <h3 class="mb-1.5 font-tmm12-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm12-mut uppercase">Ages</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Under 5</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">5 to 8</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">9 and up</a></li>
                  </ul>
                </div>
                <div class="min-w-0 translate-x-3 opacity-0 transition-[opacity,translate] duration-[220ms,320ms] ease-tmm12-out delay-90 group-data-open/panel:translate-x-0 group-data-open/panel:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none">
                  <h3 class="mb-1.5 font-tmm12-display text-[0.68rem]/none font-bold tracking-[0.16em] text-tmm12-mut uppercase">Controls</h3>
                  <ul class="grid gap-px">
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Profile PIN</a></li>
                    <li><a href="#tmm12-title" class="-mx-2 flex min-h-11 min-w-0 items-center rounded-lg px-2 text-[0.9rem] text-tmm12-ink transition-colors hover:bg-tmm12-acc/12 hover:text-tmm12-acc">Watch limits</a></li>
                  </ul>
                </div>
                <ul class="col-span-2 grid min-w-0 grid-cols-[repeat(auto-fit,minmax(min(100%,9rem),1fr))] gap-2.5 max-[52rem]:col-auto">
                  <li><a href="#tmm12-title" class="group/tile grid min-w-0 gap-0.5 text-tmm12-ink"><span class="relative block aspect-video overflow-hidden rounded-[10px] bg-linear-140 from-[#22c55e] to-[#84cc16]" aria-hidden="true"><span class="absolute inset-0 grid place-items-center bg-black/30 opacity-0 transition-opacity group-hover/tile:opacity-100"><svg class="size-9 rounded-full bg-white/90 p-2.5 text-black" viewBox="0 0 24 24"><path d="M7 4v16l13-8Z" fill="currentColor"/></svg></span></span><b class="mt-1 min-w-0 font-tmm12-display text-[0.88rem]/tight font-semibold group-hover/tile:text-tmm12-acc">Fern and Friends</b><span class="text-[0.75rem] text-tmm12-mut">S4</span></a></li>
                  <li><a href="#tmm12-title" class="group/tile grid min-w-0 gap-0.5 text-tmm12-ink"><span class="relative block aspect-video overflow-hidden rounded-[10px] bg-linear-140 from-[#0ea5e9] to-[#14b8a6]" aria-hidden="true"><span class="absolute inset-0 grid place-items-center bg-black/30 opacity-0 transition-opacity group-hover/tile:opacity-100"><svg class="size-9 rounded-full bg-white/90 p-2.5 text-black" viewBox="0 0 24 24"><path d="M7 4v16l13-8Z" fill="currentColor"/></svg></span></span><b class="mt-1 min-w-0 font-tmm12-display text-[0.88rem]/tight font-semibold group-hover/tile:text-tmm12-acc">Orbit Explorers</b><span class="text-[0.75rem] text-tmm12-mut">New</span></a></li>
                </ul>
              </div>
            </section>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(76rem,calc(100%-2rem))] py-[clamp(1.75rem,5vw,3rem)]">
    <p class="mb-2.5 font-tmm12-display text-[0.72rem]/none font-bold tracking-[0.18em] text-tmm12-mut uppercase">Continue watching</p>
    <div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] gap-2.5">
      <span class="relative block aspect-video overflow-hidden rounded-xl bg-linear-140 from-[#f43f5e] to-[#f59e0b]" aria-hidden="true"><span class="absolute inset-x-0 bottom-0 h-1 bg-black/30"><span class="block h-full bg-white" style="width:72%"></span></span></span>
      <span class="relative block aspect-video overflow-hidden rounded-xl bg-linear-140 from-[#3b82f6] to-[#8b5cf6]" aria-hidden="true"><span class="absolute inset-x-0 bottom-0 h-1 bg-black/30"><span class="block h-full bg-white" style="width:35%"></span></span></span>
      <span class="relative block aspect-video overflow-hidden rounded-xl bg-linear-140 from-[#6366f1] to-[#0ea5e9]" aria-hidden="true"><span class="absolute inset-x-0 bottom-0 h-1 bg-black/30"><span class="block h-full bg-white" style="width:88%"></span></span></span>
      <span class="relative block aspect-video overflow-hidden rounded-xl bg-linear-140 from-[#0ea5e9] to-[#14b8a6]" aria-hidden="true"><span class="absolute inset-x-0 bottom-0 h-1 bg-black/30"><span class="block h-full bg-white" style="width:12%"></span></span></span>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm12-bg: #070a14;
  --color-tmm12-bg: oklch(0.14 0.02 265);
  --color-tmm12-solid: #101728;
  --color-tmm12-solid: oklch(0.2 0.03 265);
  --color-tmm12-surf: #101728;
  --color-tmm12-surf: oklch(0.2 0.03 265);
  --color-tmm12-line: #223052;
  --color-tmm12-line: oklch(0.31 0.05 265);
  --color-tmm12-ink: #e9eefb;
  --color-tmm12-ink: oklch(0.95 0.015 265);
  --color-tmm12-mut: #99a8c9;
  --color-tmm12-mut: oklch(0.73 0.04 265);
  --color-tmm12-acc: #6aa8ff;
  --color-tmm12-acc: oklch(0.74 0.15 258);
  --color-tmm12-on-acc: #04101f;
  --color-tmm12-on-acc: oklch(0.16 0.03 258);
  --font-tmm12-display: 'Schibsted Grotesk', system-ui, sans-serif;
  --font-tmm12-sans: 'Schibsted Grotesk', system-ui, sans-serif;
  --shadow-tmm12-shell: 0 30px 70px -42px rgb(0 0 0 / 0.8);
  --ease-tmm12-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-12 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-12:has(#tmm12-theme:checked) {
  --color-tmm12-bg: #eef2fb;
  --color-tmm12-bg: oklch(0.96 0.012 265);
  --color-tmm12-solid: #ffffff;
  --color-tmm12-solid: oklch(1 0 0);
  --color-tmm12-surf: #ffffff;
  --color-tmm12-surf: oklch(1 0 0);
  --color-tmm12-line: #ccd8f0;
  --color-tmm12-line: oklch(0.88 0.03 265);
  --color-tmm12-ink: #0b1730;
  --color-tmm12-ink: oklch(0.2 0.05 265);
  --color-tmm12-mut: #4f6284;
  --color-tmm12-mut: oklch(0.48 0.05 262);
  --color-tmm12-acc: #1d4ed8;
  --color-tmm12-acc: oklch(0.48 0.21 262);
  --color-tmm12-on-acc: #ffffff;
  --color-tmm12-on-acc: oklch(1 0 0);
}

@media (prefers-color-scheme: light) {
  .tmm-12 {
    --color-tmm12-bg: #eef2fb;
    --color-tmm12-bg: oklch(0.96 0.012 265);
    --color-tmm12-solid: #ffffff;
    --color-tmm12-solid: oklch(1 0 0);
    --color-tmm12-surf: #ffffff;
    --color-tmm12-surf: oklch(1 0 0);
    --color-tmm12-line: #ccd8f0;
    --color-tmm12-line: oklch(0.88 0.03 265);
    --color-tmm12-ink: #0b1730;
    --color-tmm12-ink: oklch(0.2 0.05 265);
    --color-tmm12-mut: #4f6284;
    --color-tmm12-mut: oklch(0.48 0.05 262);
    --color-tmm12-acc: #1d4ed8;
    --color-tmm12-acc: oklch(0.48 0.21 262);
    --color-tmm12-on-acc: #ffffff;
    --color-tmm12-on-acc: oklch(1 0 0);
  }

  .tmm-12:has(#tmm12-theme:checked) {
    --color-tmm12-bg: #070a14;
    --color-tmm12-bg: oklch(0.14 0.02 265);
    --color-tmm12-solid: #101728;
    --color-tmm12-solid: oklch(0.2 0.03 265);
    --color-tmm12-surf: #101728;
    --color-tmm12-surf: oklch(0.2 0.03 265);
    --color-tmm12-line: #223052;
    --color-tmm12-line: oklch(0.31 0.05 265);
    --color-tmm12-ink: #e9eefb;
    --color-tmm12-ink: oklch(0.95 0.015 265);
    --color-tmm12-mut: #99a8c9;
    --color-tmm12-mut: oklch(0.73 0.04 265);
    --color-tmm12-acc: #6aa8ff;
    --color-tmm12-acc: oklch(0.74 0.15 258);
    --color-tmm12-on-acc: #04101f;
    --color-tmm12-on-acc: oklch(0.16 0.03 258);
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tmm-12');
  if (!root || root.__tmmCleanup) return;
  const shell = root.querySelector('[data-tmm12-shell]');
  const nav = root.querySelector('[data-tmm12-nav]');
  const panel = root.querySelector('[data-tmm12-panel]');
  const triggers = [...nav.querySelectorAll('[data-tmm12-trigger]')];
  const tabs = [...panel.querySelectorAll('[data-tab]')];
  const canHover = window.matchMedia('(hover: hover)');

  // One shared panel: swapping sections un-hides the next one, and its starting: utilities
  // replay the slide-in on every swap with no extra script.
  const show = (trigger) => {
    const id = trigger.dataset.for;
    panel.querySelectorAll('section[id]').forEach((s) => { s.hidden = s.id !== id; });
    tabs.forEach((t) => t.toggleAttribute('data-active', t.dataset.tab === id));
    triggers.forEach((t) => t.setAttribute('aria-expanded', String(t === trigger)));
    panel.setAttribute('data-open', '');
    panel.setAttribute('aria-label', trigger.textContent.trim());
  };
  const close = () => {
    panel.removeAttribute('data-open');
    triggers.forEach((t) => t.setAttribute('aria-expanded', 'false'));
  };

  const onClick = (e) => {
    const t = e.target.closest('[data-tmm12-trigger]');
    if (!t) return;
    if (t.getAttribute('aria-expanded') === 'true') { if (!canHover.matches || e.pointerType !== 'mouse') close(); return; }
    show(t);
  };
  const onOver = (e) => {
    if (!canHover.matches || e.pointerType !== 'mouse') return;
    const t = e.target.closest('[data-tmm12-trigger]');
    if (t && t.getAttribute('aria-expanded') !== 'true') show(t);
  };
  const onLeave = () => { if (!shell.contains(document.activeElement)) close(); };
  const onKey = (e) => {
    if (e.key !== 'Escape') return;
    const active = triggers.find((t) => t.getAttribute('aria-expanded') === 'true');
    close();
    if (active) active.focus();
  };
  const onFocusOut = (e) => { if (!e.relatedTarget || !shell.contains(e.relatedTarget)) close(); };

  nav.addEventListener('click', onClick);
  nav.addEventListener('pointerover', onOver);
  shell.addEventListener('pointerleave', onLeave);
  shell.addEventListener('keydown', onKey);
  shell.addEventListener('focusout', onFocusOut);
  root.__tmmCleanup = () => {
    nav.removeEventListener('click', onClick);
    nav.removeEventListener('pointerover', onOver);
    shell.removeEventListener('pointerleave', onLeave);
    shell.removeEventListener('keydown', onKey);
    shell.removeEventListener('focusout', onFocusOut);
  };
})();
```
