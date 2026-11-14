---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-hover-intent-delay/"
title: "Tailwind Mega Menu with Hover Intent Delay (No Flicker)"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "A travel-airline header whose panels wait 120ms before opening and 250ms before closing, so a pointer sweeping across the bar on its way to the page never…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mega Menu with Hover Intent Delay (No Flicker)
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-hover-intent-delay/

A travel-airline header whose panels wait 120ms before opening and 250ms before closing, so a pointer sweeping across the bar on its way to the page never strobes three panels in a row. The script only toggles a data-open attribute; every visual state &mdash; the warm underline, the fade, the card spring &mdash; is a tmm02-open: utility. Once one panel is open, moving to the next swaps instantly.
## HTML
```html
<section class="tmm-02 relative w-full min-h-svh bg-tmm02-bg bg-[radial-gradient(72rem_34rem_at_12%_-14%,color-mix(in_oklab,var(--color-tmm02-acc)_22%,transparent),transparent_62%),radial-gradient(50rem_26rem_at_96%_6%,color-mix(in_oklab,var(--color-tmm02-warm)_16%,transparent),transparent_60%)] font-tmm02-sans leading-normal text-tmm02-page-ink [&_:focus-visible]:rounded-md [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm02-acc" aria-labelledby="tmm02-title">
  <h2 class="sr-only" id="tmm02-title">Orbit Air</h2>

  <div class="absolute top-[42px] right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm02-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmm02-line bg-tmm02-chrome text-tmm02-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm02-acc" for="tmm02-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full bg-tmm02-chrome text-tmm02-ink">
    <div class="mx-auto flex min-h-[34px] w-[min(82rem,calc(100%-2rem))] flex-wrap items-center gap-5 border-b border-tmm02-line text-[0.72rem]/none font-medium tracking-[0.04em] text-tmm02-mut">
      <span class="inline-flex items-center gap-1.5"><span aria-hidden="true" class="size-1.5 rounded-full bg-tmm02-warm"></span>Orbit Club</span>
      <span>English &middot; GBP</span>
      <a class="ml-auto inline-flex min-h-[34px] items-center text-tmm02-warm hover:underline" href="#tmm02-title">Flight status</a>
    </div>

    <div class="mx-auto flex min-h-17 w-[min(82rem,calc(100%-2rem))] flex-wrap items-stretch gap-x-[clamp(0.5rem,2vw,2rem)] pr-15 max-[56rem]:flex-col max-[56rem]:py-2.5">
      <a class="inline-flex items-center gap-2 font-tmm02-display text-[1.1rem]/none font-bold tracking-[0.06em] text-tmm02-ink uppercase" href="#tmm02-title">
        <svg class="size-6 text-tmm02-warm" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M2.5 13.5 21 5l-5 9.5 1.5 5.5-4-3.5-4 2 .5-4Z" fill="currentColor"/></svg>
        Orbit Air
      </a>

      <nav data-tmm02-nav class="flex min-w-0" aria-label="Primary" data-open-delay="120" data-close-delay="250">
        <ul class="flex flex-wrap gap-0.5 max-[56rem]:flex-col">
          <li data-tmm02-item class="flex items-stretch max-[56rem]:block">
            <button data-tmm02-trigger type="button" aria-expanded="false" aria-controls="tmm02-panel-book" class="relative inline-flex min-h-11 cursor-pointer items-center self-stretch px-3.5 font-tmm02-display text-[0.92rem]/none font-semibold tracking-[0.1em] text-tmm02-ink uppercase transition-colors hover:text-tmm02-warm after:absolute after:inset-x-3 after:bottom-0 after:h-[3px] after:origin-center after:scale-x-0 after:rounded-full after:bg-tmm02-warm after:transition-transform tmm02-open:text-tmm02-warm! tmm02-open:after:scale-x-100 max-[56rem]:self-auto">Book</button>
            <div data-tmm02-panel class="invisible absolute inset-x-0 top-full z-30 -translate-y-2 border-b-3 border-tmm02-warm bg-tmm02-panel opacity-0 shadow-tmm02-panel pointer-events-none transition-[opacity,translate,visibility] duration-150 tmm02-open:visible tmm02-open:translate-y-0 tmm02-open:opacity-100 tmm02-open:pointer-events-auto motion-reduce:transition-none max-[56rem]:static max-[56rem]:hidden max-[56rem]:visible max-[56rem]:translate-y-0 max-[56rem]:opacity-100 max-[56rem]:shadow-none max-[56rem]:[[data-open]>&]:block" id="tmm02-panel-book" aria-label="Book">
              <div class="mx-auto grid w-[min(82rem,calc(100%-2rem))] gap-[clamp(0.9rem,2.6vw,2rem)] py-[clamp(1.1rem,3vw,1.75rem)] min-[62rem]:grid-cols-[minmax(0,1fr)_15rem] max-[56rem]:w-full max-[56rem]:px-4">
                <ul class="min-w-0 origin-bottom scale-97 opacity-0 transition-[opacity,scale] duration-[200ms,380ms] ease-tmm02-spring delay-30 tmm02-open:scale-100 tmm02-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-2.5">
                  <li><a href="#tmm02-title" class="group/card grid min-h-23 content-start gap-0.5 rounded-xl border border-tmm02-line bg-tmm02-ink/[0.02] px-4 py-3.5 text-tmm02-ink transition-[border-color,background-color,translate] hover:-translate-y-0.5 hover:border-tmm02-warm hover:bg-tmm02-warm/6"><span class="font-tmm02-display text-[0.64rem]/none font-bold tracking-[0.18em] text-tmm02-warm uppercase">Return</span><b class="mt-1 flex items-center justify-between gap-2 text-[0.98rem]/tight font-semibold">Flights<span aria-hidden="true" class="text-tmm02-warm opacity-0 transition-[opacity,translate] -translate-x-1 group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></b><span class="text-[0.78rem] text-tmm02-mut">Economy to Business</span></a></li>
                  <li><a href="#tmm02-title" class="group/card grid min-h-23 content-start gap-0.5 rounded-xl border border-tmm02-line bg-tmm02-ink/[0.02] px-4 py-3.5 text-tmm02-ink transition-[border-color,background-color,translate] hover:-translate-y-0.5 hover:border-tmm02-warm hover:bg-tmm02-warm/6"><span class="font-tmm02-display text-[0.64rem]/none font-bold tracking-[0.18em] text-tmm02-warm uppercase">Bundle</span><b class="mt-1 flex items-center justify-between gap-2 text-[0.98rem]/tight font-semibold">Flight and hotel<span aria-hidden="true" class="text-tmm02-warm opacity-0 transition-[opacity,translate] -translate-x-1 group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></b><span class="text-[0.78rem] text-tmm02-mut">Save up to 18%</span></a></li>
                  <li><a href="#tmm02-title" class="group/card grid min-h-23 content-start gap-0.5 rounded-xl border border-tmm02-line bg-tmm02-ink/[0.02] px-4 py-3.5 text-tmm02-ink transition-[border-color,background-color,translate] hover:-translate-y-0.5 hover:border-tmm02-warm hover:bg-tmm02-warm/6"><span class="font-tmm02-display text-[0.64rem]/none font-bold tracking-[0.18em] text-tmm02-warm uppercase">Group</span><b class="mt-1 flex items-center justify-between gap-2 text-[0.98rem]/tight font-semibold">10+ travellers<span aria-hidden="true" class="text-tmm02-warm opacity-0 transition-[opacity,translate] -translate-x-1 group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></b><span class="text-[0.78rem] text-tmm02-mut">Held fares</span></a></li>
                </ul>
                <div class="min-w-0 origin-bottom scale-97 opacity-0 transition-[opacity,scale] duration-[200ms,380ms] ease-tmm02-spring delay-120 tmm02-open:scale-100 tmm02-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none grid content-start gap-0.5 rounded-xl bg-tmm02-acc/12 p-[clamp(0.85rem,2.2vw,1.1rem)]">
                  <p class="mb-1 font-tmm02-display text-[0.66rem]/none font-bold tracking-[0.18em] text-tmm02-acc uppercase">Quick actions</p>
                  <ul class="grid gap-px">
                    <li class="translate-x-3.5 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm02-out delay-180 tmm02-open:translate-x-0 tmm02-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm02-title" class="flex min-h-11 items-center text-[0.87rem] text-tmm02-ink transition-colors hover:text-tmm02-warm">Manage a booking</a></li>
                    <li class="translate-x-3.5 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm02-out delay-225 tmm02-open:translate-x-0 tmm02-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm02-title" class="flex min-h-11 items-center text-[0.87rem] text-tmm02-ink transition-colors hover:text-tmm02-warm">Check in</a></li>
                    <li class="translate-x-3.5 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm02-out delay-270 tmm02-open:translate-x-0 tmm02-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm02-title" class="flex min-h-11 items-center text-[0.87rem] text-tmm02-ink transition-colors hover:text-tmm02-warm">Add extra bags</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <li data-tmm02-item class="flex items-stretch max-[56rem]:block">
            <button data-tmm02-trigger type="button" aria-expanded="false" aria-controls="tmm02-panel-where" class="relative inline-flex min-h-11 cursor-pointer items-center self-stretch px-3.5 font-tmm02-display text-[0.92rem]/none font-semibold tracking-[0.1em] text-tmm02-ink uppercase transition-colors hover:text-tmm02-warm after:absolute after:inset-x-3 after:bottom-0 after:h-[3px] after:origin-center after:scale-x-0 after:rounded-full after:bg-tmm02-warm after:transition-transform tmm02-open:text-tmm02-warm! tmm02-open:after:scale-x-100 max-[56rem]:self-auto">Destinations</button>
            <div data-tmm02-panel class="invisible absolute inset-x-0 top-full z-30 -translate-y-2 border-b-3 border-tmm02-warm bg-tmm02-panel opacity-0 shadow-tmm02-panel pointer-events-none transition-[opacity,translate,visibility] duration-150 tmm02-open:visible tmm02-open:translate-y-0 tmm02-open:opacity-100 tmm02-open:pointer-events-auto motion-reduce:transition-none max-[56rem]:static max-[56rem]:hidden max-[56rem]:visible max-[56rem]:translate-y-0 max-[56rem]:opacity-100 max-[56rem]:shadow-none max-[56rem]:[[data-open]>&]:block" id="tmm02-panel-where" aria-label="Destinations">
              <div class="mx-auto grid w-[min(82rem,calc(100%-2rem))] gap-[clamp(0.9rem,2.6vw,2rem)] py-[clamp(1.1rem,3vw,1.75rem)] min-[62rem]:grid-cols-[minmax(0,1fr)_15rem] max-[56rem]:w-full max-[56rem]:px-4">
                <div class="min-w-0 origin-bottom scale-97 opacity-0 transition-[opacity,scale] duration-[200ms,380ms] ease-tmm02-spring delay-30 tmm02-open:scale-100 tmm02-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none">
                  <p class="mb-2 font-tmm02-display text-[0.7rem]/none font-semibold tracking-[0.2em] text-tmm02-mut uppercase">From London &middot; direct</p>
                  <ul class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))] gap-0.5">
                    <li><a href="#tmm02-title" class="grid min-h-13 grid-cols-[3.2rem_minmax(0,1fr)_auto] items-center gap-x-3 rounded-lg px-2.5 py-1.5 text-tmm02-ink transition-colors hover:bg-tmm02-acc/12"><span class="row-span-2 grid h-9 w-[3.2rem] place-items-center rounded-md bg-tmm02-acc/18 font-tmm02-display text-[0.82rem]/none font-bold tracking-[0.08em] text-tmm02-acc">LIS</span><b class="min-w-0 text-[0.95rem]/tight font-semibold">Lisbon</b><span class="col-start-2 text-[0.74rem]/tight text-tmm02-mut">2h 45m</span><span class="col-start-3 row-span-2 row-start-1 text-right font-tmm02-display text-base/none font-bold text-tmm02-warm tabular-nums"><small class="block text-[0.6rem] font-semibold tracking-[0.14em] text-tmm02-mut uppercase">from</small>&pound;68</span></a></li>
                    <li><a href="#tmm02-title" class="grid min-h-13 grid-cols-[3.2rem_minmax(0,1fr)_auto] items-center gap-x-3 rounded-lg px-2.5 py-1.5 text-tmm02-ink transition-colors hover:bg-tmm02-acc/12"><span class="row-span-2 grid h-9 w-[3.2rem] place-items-center rounded-md bg-tmm02-acc/18 font-tmm02-display text-[0.82rem]/none font-bold tracking-[0.08em] text-tmm02-acc">KEF</span><b class="min-w-0 text-[0.95rem]/tight font-semibold">Reykjavik</b><span class="col-start-2 text-[0.74rem]/tight text-tmm02-mut">3h 05m</span><span class="col-start-3 row-span-2 row-start-1 text-right font-tmm02-display text-base/none font-bold text-tmm02-warm tabular-nums"><small class="block text-[0.6rem] font-semibold tracking-[0.14em] text-tmm02-mut uppercase">from</small>&pound;94</span></a></li>
                    <li><a href="#tmm02-title" class="grid min-h-13 grid-cols-[3.2rem_minmax(0,1fr)_auto] items-center gap-x-3 rounded-lg px-2.5 py-1.5 text-tmm02-ink transition-colors hover:bg-tmm02-acc/12"><span class="row-span-2 grid h-9 w-[3.2rem] place-items-center rounded-md bg-tmm02-acc/18 font-tmm02-display text-[0.82rem]/none font-bold tracking-[0.08em] text-tmm02-acc">ATH</span><b class="min-w-0 text-[0.95rem]/tight font-semibold">Athens</b><span class="col-start-2 text-[0.74rem]/tight text-tmm02-mut">3h 50m</span><span class="col-start-3 row-span-2 row-start-1 text-right font-tmm02-display text-base/none font-bold text-tmm02-warm tabular-nums"><small class="block text-[0.6rem] font-semibold tracking-[0.14em] text-tmm02-mut uppercase">from</small>&pound;112</span></a></li>
                    <li><a href="#tmm02-title" class="grid min-h-13 grid-cols-[3.2rem_minmax(0,1fr)_auto] items-center gap-x-3 rounded-lg px-2.5 py-1.5 text-tmm02-ink transition-colors hover:bg-tmm02-acc/12"><span class="row-span-2 grid h-9 w-[3.2rem] place-items-center rounded-md bg-tmm02-acc/18 font-tmm02-display text-[0.82rem]/none font-bold tracking-[0.08em] text-tmm02-acc">TLL</span><b class="min-w-0 text-[0.95rem]/tight font-semibold">Tallinn</b><span class="col-start-2 text-[0.74rem]/tight text-tmm02-mut">2h 55m</span><span class="col-start-3 row-span-2 row-start-1 text-right font-tmm02-display text-base/none font-bold text-tmm02-warm tabular-nums"><small class="block text-[0.6rem] font-semibold tracking-[0.14em] text-tmm02-mut uppercase">from</small>&pound;79</span></a></li>
                    <li><a href="#tmm02-title" class="grid min-h-13 grid-cols-[3.2rem_minmax(0,1fr)_auto] items-center gap-x-3 rounded-lg px-2.5 py-1.5 text-tmm02-ink transition-colors hover:bg-tmm02-acc/12"><span class="row-span-2 grid h-9 w-[3.2rem] place-items-center rounded-md bg-tmm02-acc/18 font-tmm02-display text-[0.82rem]/none font-bold tracking-[0.08em] text-tmm02-acc">JFK</span><b class="min-w-0 text-[0.95rem]/tight font-semibold">New York</b><span class="col-start-2 text-[0.74rem]/tight text-tmm02-mut">7h 40m</span><span class="col-start-3 row-span-2 row-start-1 text-right font-tmm02-display text-base/none font-bold text-tmm02-warm tabular-nums"><small class="block text-[0.6rem] font-semibold tracking-[0.14em] text-tmm02-mut uppercase">from</small>&pound;322</span></a></li>
                    <li><a href="#tmm02-title" class="grid min-h-13 grid-cols-[3.2rem_minmax(0,1fr)_auto] items-center gap-x-3 rounded-lg px-2.5 py-1.5 text-tmm02-ink transition-colors hover:bg-tmm02-acc/12"><span class="row-span-2 grid h-9 w-[3.2rem] place-items-center rounded-md bg-tmm02-acc/18 font-tmm02-display text-[0.82rem]/none font-bold tracking-[0.08em] text-tmm02-acc">YYZ</span><b class="min-w-0 text-[0.95rem]/tight font-semibold">Toronto</b><span class="col-start-2 text-[0.74rem]/tight text-tmm02-mut">7h 55m</span><span class="col-start-3 row-span-2 row-start-1 text-right font-tmm02-display text-base/none font-bold text-tmm02-warm tabular-nums"><small class="block text-[0.6rem] font-semibold tracking-[0.14em] text-tmm02-mut uppercase">from</small>&pound;348</span></a></li>
                  </ul>
                </div>
                <div class="min-w-0 origin-bottom scale-97 opacity-0 transition-[opacity,scale] duration-[200ms,380ms] ease-tmm02-spring delay-120 tmm02-open:scale-100 tmm02-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none grid content-start gap-0.5 rounded-xl bg-tmm02-acc/12 p-[clamp(0.85rem,2.2vw,1.1rem)]">
                  <p class="mb-1 font-tmm02-display text-[0.66rem]/none font-bold tracking-[0.18em] text-tmm02-acc uppercase">Browse</p>
                  <ul class="grid gap-px">
                    <li class="translate-x-3.5 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm02-out delay-180 tmm02-open:translate-x-0 tmm02-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm02-title" class="flex min-h-11 items-center text-[0.87rem] text-tmm02-ink transition-colors hover:text-tmm02-warm">Route map</a></li>
                    <li class="translate-x-3.5 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm02-out delay-225 tmm02-open:translate-x-0 tmm02-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm02-title" class="flex min-h-11 items-center text-[0.87rem] text-tmm02-ink transition-colors hover:text-tmm02-warm">Seasonal routes</a></li>
                    <li class="translate-x-3.5 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm02-out delay-270 tmm02-open:translate-x-0 tmm02-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm02-title" class="flex min-h-11 items-center text-[0.87rem] text-tmm02-ink transition-colors hover:text-tmm02-warm">Where can I fly?</a></li>
                  </ul>
                  <a class="mt-1 inline-flex min-h-11 items-center gap-1.5 text-[0.84rem] font-semibold text-tmm02-warm hover:underline hover:underline-offset-3" href="#tmm02-title">Open the fare finder <span aria-hidden="true">&rarr;</span></a>
                </div>
              </div>
            </div>
          </li>

          <li data-tmm02-item class="flex items-stretch max-[56rem]:block">
            <button data-tmm02-trigger type="button" aria-expanded="false" aria-controls="tmm02-panel-onboard" class="relative inline-flex min-h-11 cursor-pointer items-center self-stretch px-3.5 font-tmm02-display text-[0.92rem]/none font-semibold tracking-[0.1em] text-tmm02-ink uppercase transition-colors hover:text-tmm02-warm after:absolute after:inset-x-3 after:bottom-0 after:h-[3px] after:origin-center after:scale-x-0 after:rounded-full after:bg-tmm02-warm after:transition-transform tmm02-open:text-tmm02-warm! tmm02-open:after:scale-x-100 max-[56rem]:self-auto">Onboard</button>
            <div data-tmm02-panel class="invisible absolute inset-x-0 top-full z-30 -translate-y-2 border-b-3 border-tmm02-warm bg-tmm02-panel opacity-0 shadow-tmm02-panel pointer-events-none transition-[opacity,translate,visibility] duration-150 tmm02-open:visible tmm02-open:translate-y-0 tmm02-open:opacity-100 tmm02-open:pointer-events-auto motion-reduce:transition-none max-[56rem]:static max-[56rem]:hidden max-[56rem]:visible max-[56rem]:translate-y-0 max-[56rem]:opacity-100 max-[56rem]:shadow-none max-[56rem]:[[data-open]>&]:block" id="tmm02-panel-onboard" aria-label="Onboard">
              <div class="mx-auto grid w-[min(82rem,calc(100%-2rem))] gap-[clamp(0.9rem,2.6vw,2rem)] py-[clamp(1.1rem,3vw,1.75rem)] min-[62rem]:grid-cols-[minmax(0,1fr)_15rem] max-[56rem]:w-full max-[56rem]:px-4">
                <ul class="min-w-0 origin-bottom scale-97 opacity-0 transition-[opacity,scale] duration-[200ms,380ms] ease-tmm02-spring delay-30 tmm02-open:scale-100 tmm02-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none grid grid-cols-[repeat(auto-fit,minmax(min(100%,13rem),1fr))] gap-2.5">
                  <li><a href="#tmm02-title" class="group/card grid min-h-23 content-start gap-0.5 rounded-xl border border-tmm02-line bg-tmm02-ink/[0.02] px-4 py-3.5 text-tmm02-ink transition-[border-color,background-color,translate] hover:-translate-y-0.5 hover:border-tmm02-warm hover:bg-tmm02-warm/6"><span class="font-tmm02-display text-[0.64rem]/none font-bold tracking-[0.18em] text-tmm02-warm uppercase">Cabins</span><b class="mt-1 flex items-center justify-between gap-2 text-[0.98rem]/tight font-semibold">Seats and space<span aria-hidden="true" class="text-tmm02-warm opacity-0 transition-[opacity,translate] -translate-x-1 group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></b><span class="text-[0.78rem] text-tmm02-mut">Pitch and recline</span></a></li>
                  <li><a href="#tmm02-title" class="group/card grid min-h-23 content-start gap-0.5 rounded-xl border border-tmm02-line bg-tmm02-ink/[0.02] px-4 py-3.5 text-tmm02-ink transition-[border-color,background-color,translate] hover:-translate-y-0.5 hover:border-tmm02-warm hover:bg-tmm02-warm/6"><span class="font-tmm02-display text-[0.64rem]/none font-bold tracking-[0.18em] text-tmm02-warm uppercase">Service</span><b class="mt-1 flex items-center justify-between gap-2 text-[0.98rem]/tight font-semibold">Food and drink<span aria-hidden="true" class="text-tmm02-warm opacity-0 transition-[opacity,translate] -translate-x-1 group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></b><span class="text-[0.78rem] text-tmm02-mut">Pre-order to save</span></a></li>
                  <li><a href="#tmm02-title" class="group/card grid min-h-23 content-start gap-0.5 rounded-xl border border-tmm02-line bg-tmm02-ink/[0.02] px-4 py-3.5 text-tmm02-ink transition-[border-color,background-color,translate] hover:-translate-y-0.5 hover:border-tmm02-warm hover:bg-tmm02-warm/6"><span class="font-tmm02-display text-[0.64rem]/none font-bold tracking-[0.18em] text-tmm02-warm uppercase">Wi-Fi</span><b class="mt-1 flex items-center justify-between gap-2 text-[0.98rem]/tight font-semibold">Stay connected<span aria-hidden="true" class="text-tmm02-warm opacity-0 transition-[opacity,translate] -translate-x-1 group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></b><span class="text-[0.78rem] text-tmm02-mut">Free for Club</span></a></li>
                </ul>
                <div class="min-w-0 origin-bottom scale-97 opacity-0 transition-[opacity,scale] duration-[200ms,380ms] ease-tmm02-spring delay-120 tmm02-open:scale-100 tmm02-open:opacity-100 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none grid content-start gap-0.5 rounded-xl bg-tmm02-acc/12 p-[clamp(0.85rem,2.2vw,1.1rem)]">
                  <p class="mb-1 font-tmm02-display text-[0.66rem]/none font-bold tracking-[0.18em] text-tmm02-acc uppercase">Before you fly</p>
                  <ul class="grid gap-px">
                    <li class="translate-x-3.5 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm02-out delay-180 tmm02-open:translate-x-0 tmm02-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm02-title" class="flex min-h-11 items-center text-[0.87rem] text-tmm02-ink transition-colors hover:text-tmm02-warm">Baggage rules</a></li>
                    <li class="translate-x-3.5 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm02-out delay-225 tmm02-open:translate-x-0 tmm02-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm02-title" class="flex min-h-11 items-center text-[0.87rem] text-tmm02-ink transition-colors hover:text-tmm02-warm">Special assistance</a></li>
                    <li class="translate-x-3.5 opacity-0 transition-[opacity,translate] duration-[200ms,320ms] ease-tmm02-out delay-270 tmm02-open:translate-x-0 tmm02-open:opacity-100 motion-reduce:translate-x-0 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm02-title" class="flex min-h-11 items-center text-[0.87rem] text-tmm02-ink transition-colors hover:text-tmm02-warm">Travelling with pets</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-3.5 font-tmm02-display text-[0.92rem]/none font-semibold tracking-[0.1em] text-tmm02-ink uppercase hover:text-tmm02-warm" href="#tmm02-title">Help</a></li>
        </ul>
      </nav>

      <div class="ml-auto flex items-center gap-1.5 max-[56rem]:ml-0">
        <a class="inline-flex min-h-11 items-center px-3 text-[0.85rem] font-semibold text-tmm02-mut hover:text-tmm02-ink" href="#tmm02-title">Sign in</a>
        <a class="inline-flex min-h-11 items-center rounded-full bg-tmm02-warm px-4.5 text-[0.85rem] font-bold text-tmm02-on-warm hover:brightness-105" href="#tmm02-title">Check in</a>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(82rem,calc(100%-2rem))] py-[clamp(3rem,9vw,5.5rem)]">
    <div class="grid gap-4">
      <p class="font-tmm02-display text-[0.74rem]/none font-semibold tracking-[0.24em] text-[color-mix(in_oklab,var(--color-tmm02-acc)_45%,var(--color-tmm02-page-ink))] uppercase">Winter timetable now open</p>
      <h1 class="max-w-[22ch] font-tmm02-display text-[clamp(2.1rem,6.5vw,4rem)]/[1.02] font-bold tracking-[-0.01em] text-balance">Twelve new direct routes from London.</h1>
      <div class="mt-2.5 grid grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))] overflow-hidden rounded-2xl shadow-tmm02-search" role="group" aria-label="Search flights">
        <div class="grid min-w-0 gap-0.5 border-r border-b border-tmm02-page-ink/10 bg-tmm02-card px-4 py-3.5"><span class="font-tmm02-display text-[0.66rem]/none font-semibold tracking-[0.16em] text-tmm02-page-mut uppercase">From</span><b class="text-base/tight font-semibold text-tmm02-page-ink">London LHR</b></div>
        <div class="grid min-w-0 gap-0.5 border-r border-b border-tmm02-page-ink/10 bg-tmm02-card px-4 py-3.5"><span class="font-tmm02-display text-[0.66rem]/none font-semibold tracking-[0.16em] text-tmm02-page-mut uppercase">To</span><b class="text-base/tight font-semibold text-tmm02-page-ink">Anywhere</b></div>
        <div class="grid min-w-0 gap-0.5 border-r border-b border-tmm02-page-ink/10 bg-tmm02-card px-4 py-3.5"><span class="font-tmm02-display text-[0.66rem]/none font-semibold tracking-[0.16em] text-tmm02-page-mut uppercase">Depart</span><b class="text-base/tight font-semibold text-tmm02-page-ink">12 Nov</b></div>
        <div class="grid min-w-0 gap-0.5 border-r border-b border-tmm02-page-ink/10 bg-tmm02-card px-4 py-3.5"><span class="font-tmm02-display text-[0.66rem]/none font-semibold tracking-[0.16em] text-tmm02-page-mut uppercase">Travellers</span><b class="text-base/tight font-semibold text-tmm02-page-ink">1 adult</b></div>
        <a class="inline-flex min-h-13 items-center justify-center gap-2 bg-tmm02-warm px-5.5 text-[0.95rem] font-bold text-tmm02-on-warm transition-[filter] hover:brightness-105" href="#tmm02-title">Search fares <span aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm02-chrome: #0f1a2e;
  --color-tmm02-chrome: oklch(0.22 0.04 262);
  --color-tmm02-panel: #0b1424;
  --color-tmm02-panel: oklch(0.19 0.035 262);
  --color-tmm02-line: #23324c;
  --color-tmm02-line: oklch(0.31 0.045 262);
  --color-tmm02-ink: #e8eef7;
  --color-tmm02-ink: oklch(0.95 0.012 255);
  --color-tmm02-mut: #9aa9c2;
  --color-tmm02-mut: oklch(0.73 0.035 260);
  --color-tmm02-acc: #7ea6ff;
  --color-tmm02-acc: oklch(0.76 0.14 262);
  --color-tmm02-warm: #ffb454;
  --color-tmm02-warm: oklch(0.8 0.14 70);
  --color-tmm02-on-warm: #241503;
  --color-tmm02-on-warm: oklch(0.2 0.04 70);
  --color-tmm02-bg: #e9edf4;
  --color-tmm02-bg: oklch(0.94 0.012 262);
  --color-tmm02-page-ink: #0d1b33;
  --color-tmm02-page-ink: oklch(0.2 0.05 262);
  --color-tmm02-page-mut: #55657f;
  --color-tmm02-page-mut: oklch(0.49 0.04 262);
  --color-tmm02-card: #ffffff;
  --color-tmm02-card: oklch(1 0 0);
  --font-tmm02-display: 'Archivo Narrow', 'Roboto Condensed', sans-serif;
  --font-tmm02-sans: 'Archivo', system-ui, sans-serif;
  --shadow-tmm02-panel: 0 30px 60px -36px rgb(0 0 0 / 0.75);
  --shadow-tmm02-search: 0 1px 0 rgb(13 27 51 / 0.06), 0 24px 48px -28px rgb(13 27 51 / 0.35);
  --ease-tmm02-spring: cubic-bezier(0.34, 1.45, 0.64, 1);
  --ease-tmm02-out: cubic-bezier(0.22, 1, 0.36, 1);
}
/* The open state as ONE variant: focus-within or a scripted [data-open] (hover is driven by the script).
   Every panel, chevron and entry utility reads tmm02-open: instead of a repeated selector list. */

@custom-variant tmm02-open {
  &:where([data-tmm02-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-02 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-02:has(#tmm02-theme:checked) {
  --color-tmm02-bg: #070c15;
  --color-tmm02-bg: oklch(0.15 0.025 262);
  --color-tmm02-page-ink: #e8eef7;
  --color-tmm02-page-ink: oklch(0.95 0.012 255);
  --color-tmm02-page-mut: #9aa9c2;
  --color-tmm02-page-mut: oklch(0.73 0.035 260);
  --color-tmm02-chrome: #0c1424;
  --color-tmm02-chrome: oklch(0.2 0.035 262);
  --color-tmm02-panel: #090f1c;
  --color-tmm02-panel: oklch(0.17 0.03 262);
  --color-tmm02-card: #101a2c;
  --color-tmm02-card: oklch(0.22 0.035 262);
}

@media (prefers-color-scheme: dark) {
  .tmm-02 {
    --color-tmm02-bg: #070c15;
    --color-tmm02-bg: oklch(0.15 0.025 262);
    --color-tmm02-page-ink: #e8eef7;
    --color-tmm02-page-ink: oklch(0.95 0.012 255);
    --color-tmm02-page-mut: #9aa9c2;
    --color-tmm02-page-mut: oklch(0.73 0.035 260);
    --color-tmm02-chrome: #0c1424;
    --color-tmm02-chrome: oklch(0.2 0.035 262);
    --color-tmm02-panel: #090f1c;
    --color-tmm02-panel: oklch(0.17 0.03 262);
    --color-tmm02-card: #101a2c;
    --color-tmm02-card: oklch(0.22 0.035 262);
  }

  .tmm-02:has(#tmm02-theme:checked) {
    --color-tmm02-chrome: #0f1a2e;
    --color-tmm02-chrome: oklch(0.22 0.04 262);
    --color-tmm02-panel: #0b1424;
    --color-tmm02-panel: oklch(0.19 0.035 262);
    --color-tmm02-line: #23324c;
    --color-tmm02-line: oklch(0.31 0.045 262);
    --color-tmm02-ink: #e8eef7;
    --color-tmm02-ink: oklch(0.95 0.012 255);
    --color-tmm02-mut: #9aa9c2;
    --color-tmm02-mut: oklch(0.73 0.035 260);
    --color-tmm02-acc: #7ea6ff;
    --color-tmm02-acc: oklch(0.76 0.14 262);
    --color-tmm02-warm: #ffb454;
    --color-tmm02-warm: oklch(0.8 0.14 70);
    --color-tmm02-on-warm: #241503;
    --color-tmm02-on-warm: oklch(0.2 0.04 70);
    --color-tmm02-bg: #e9edf4;
    --color-tmm02-bg: oklch(0.94 0.012 262);
    --color-tmm02-page-ink: #0d1b33;
    --color-tmm02-page-ink: oklch(0.2 0.05 262);
    --color-tmm02-page-mut: #55657f;
    --color-tmm02-page-mut: oklch(0.49 0.04 262);
    --color-tmm02-card: #ffffff;
    --color-tmm02-card: oklch(1 0 0);
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tmm-02');
  if (!root || root.__tmmCleanup) return;
  const nav = root.querySelector('[data-tmm02-nav]');
  const openMs = Number(nav.dataset.openDelay || 120);
  const closeMs = Number(nav.dataset.closeDelay || 250);
  const canHover = window.matchMedia('(hover: hover)');
  let openT = 0, closeT = 0;

  const setOpen = (item, on) => {
    item.toggleAttribute('data-open', on);
    item.querySelector('[data-tmm02-trigger]').setAttribute('aria-expanded', String(on));
  };
  const closeAll = () => nav.querySelectorAll('[data-tmm02-item][data-open]').forEach((i) => setOpen(i, false));

  const onEnter = (e) => {
    const item = e.target.closest('[data-tmm02-item]');
    if (!item || !canHover.matches) return;
    clearTimeout(closeT); clearTimeout(openT);
    if (item.hasAttribute('data-open')) return;
    // A panel already open means the user is scanning: swap instantly instead of waiting again.
    const delay = nav.querySelector('[data-tmm02-item][data-open]') ? 0 : openMs;
    openT = setTimeout(() => { closeAll(); setOpen(item, true); }, delay);
  };
  const onLeave = (e) => {
    if (!canHover.matches || !e.target.closest('[data-tmm02-item]')) return;
    clearTimeout(openT);
    clearTimeout(closeT);
    closeT = setTimeout(() => { if (!nav.contains(document.activeElement)) closeAll(); }, closeMs);
  };
  const onClick = (e) => {
    const trigger = e.target.closest('[data-tmm02-trigger]');
    if (!trigger) return;
    const item = trigger.closest('[data-tmm02-item]');
    const open = item.hasAttribute('data-open');
    clearTimeout(openT); clearTimeout(closeT);
    if (open && canHover.matches) return; // hover already opened it; a click must not close it again
    closeAll(); setOpen(item, !open);
  };
  const onKey = (e) => {
    if (e.key !== 'Escape') return;
    const open = nav.querySelector('[data-tmm02-item][data-open]');
    if (!open) return;
    clearTimeout(openT); clearTimeout(closeT);
    setOpen(open, false);
    open.querySelector('[data-tmm02-trigger]').focus();
  };

  nav.addEventListener('pointerenter', onEnter, true);
  nav.addEventListener('pointerleave', onLeave, true);
  nav.addEventListener('click', onClick);
  nav.addEventListener('keydown', onKey);
  root.__tmmCleanup = () => {
    nav.removeEventListener('pointerenter', onEnter, true);
    nav.removeEventListener('pointerleave', onLeave, true);
    nav.removeEventListener('click', onClick);
    nav.removeEventListener('keydown', onKey);
    clearTimeout(openT); clearTimeout(closeT);
  };
})();
```
