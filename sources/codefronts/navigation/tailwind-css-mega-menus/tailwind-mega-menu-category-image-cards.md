---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-category-image-cards/"
title: "Tailwind Mega Menu with Category Image Cards"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "A plant studio's Shop by room panel built as a grid of photo cards: aspect-[4/3] object-cover crops, a New chip where a range has just landed, and a gentle…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mega Menu with Category Image Cards
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-mega-menu-category-image-cards/

A plant studio's Shop by room panel built as a grid of photo cards: aspect-[4/3] object-cover crops, a New chip where a range has just landed, and a gentle zoom on hover. Cards settle in on a slow, organic stagger and a care-and-setup aside offers the service links. auto-fit decides how many cards fit per row, so six rooms and three pot types use the same markup. Zero JavaScript.
## HTML
```html
<section class="tmm-17 relative w-full min-h-svh bg-tmm17-bg bg-[radial-gradient(64rem_32rem_at_88%_-8%,color-mix(in_oklab,var(--color-tmm17-acc)_14%,transparent),transparent_62%)] font-tmm17-sans leading-[1.55] text-tmm17-ink [&_:focus-visible]:rounded-xl [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-3 [&_:focus-visible]:outline-tmm17-acc" aria-labelledby="tmm17-title">
  <h2 class="sr-only" id="tmm17-title">Fern Studio</h2>

  <div class="absolute top-[13px] right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm17-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmm17-line bg-tmm17-surf text-tmm17-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm17-acc" for="tmm17-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b border-tmm17-line bg-tmm17-surf">
    <div class="mx-auto flex min-h-[70px] w-[min(80rem,calc(100%-2rem))] flex-wrap items-center gap-[clamp(0.5rem,2vw,2rem)] pr-15 max-[52rem]:flex-col max-[52rem]:items-stretch max-[52rem]:py-2.5">
      <a class="inline-flex items-center gap-2 font-tmm17-display text-[1.15rem]/none font-semibold tracking-[-0.01em] text-tmm17-ink" href="#tmm17-title">
        <svg class="size-[22px] text-tmm17-acc" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 21h10l1-6H6Z" fill="currentColor"/><path d="M12 15V8m0 3c-3 0-5-2-5-5 3 0 5 2 5 5Zm0-1c0-3 2-6 6-6 0 3-2 6-6 6Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
        Fern Studio
      </a>
      <nav class="min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-1 max-[52rem]:flex-col">
          <li data-tmm17-item class="flex items-center max-[52rem]:block">
            <button type="button" id="tmm17-trigger-shop" aria-expanded="false" aria-controls="tmm17-panel-shop" class="relative after:absolute after:inset-x-0 after:top-full after:h-9 after:pointer-events-none tmm17-open:after:pointer-events-auto max-[52rem]:after:hidden inline-flex min-h-11 cursor-pointer items-center gap-1.5 rounded-full px-4 font-tmm17-display text-[0.92rem]/none font-semibold text-tmm17-ink transition-colors hover:text-tmm17-acc tmm17-open:bg-tmm17-acc/16 tmm17-open:text-tmm17-acc!">Shop by room<svg class="size-3.5 transition-transform duration-200 tmm17-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm17-line bg-tmm17-surf opacity-0 shadow-tmm17-panel pointer-events-none transition-[opacity,visibility] duration-180 tmm17-open:visible tmm17-open:opacity-100 tmm17-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:shadow-none max-[52rem]:tmm17-open:block" id="tmm17-panel-shop" aria-labelledby="tmm17-trigger-shop">
              <div class="mx-auto grid w-[min(80rem,calc(100%-2rem))] gap-[clamp(1rem,3vw,2rem)] py-[clamp(1.1rem,3vw,2rem)] min-[68rem]:grid-cols-[minmax(0,1fr)_17rem] max-[52rem]:w-full max-[52rem]:px-4">
                <ul class="grid min-w-0 grid-cols-[repeat(auto-fit,minmax(11rem,1fr))] gap-[clamp(0.6rem,2vw,1rem)]">
                  <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-40 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="group/card grid min-w-0 gap-0.5 text-inherit">
                    <span class="relative block aspect-[4/3] overflow-hidden rounded-[14px] bg-tmm17-line"><img class="block size-full object-cover transition-[scale] duration-320 ease-tmm17-settle group-hover/card:scale-106 motion-reduce:transition-none" src="https://picsum.photos/seed/fern-living/480/360" alt="" width="480" height="360" decoding="async"></span>
                    <span class="mt-1.5 flex items-center justify-between gap-2 font-tmm17-display text-[0.98rem]/snug font-semibold group-hover/card:text-tmm17-acc">Living room<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></span>
                    <span class="text-[0.78rem] text-tmm17-mut">34 pieces &middot; low light</span>
                  </a></li>
                  <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-130 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="group/card grid min-w-0 gap-0.5 text-inherit">
                    <span class="relative block aspect-[4/3] overflow-hidden rounded-[14px] bg-tmm17-line"><img class="block size-full object-cover transition-[scale] duration-320 ease-tmm17-settle group-hover/card:scale-106 motion-reduce:transition-none" src="https://picsum.photos/seed/fern-kitchen/480/360" alt="" width="480" height="360" decoding="async"></span>
                    <span class="mt-1.5 flex items-center justify-between gap-2 font-tmm17-display text-[0.98rem]/snug font-semibold group-hover/card:text-tmm17-acc">Kitchen<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></span>
                    <span class="text-[0.78rem] text-tmm17-mut">21 pieces &middot; herbs</span>
                  </a></li>
                  <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-220 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="group/card grid min-w-0 gap-0.5 text-inherit">
                    <span class="relative block aspect-[4/3] overflow-hidden rounded-[14px] bg-tmm17-line"><img class="block size-full object-cover transition-[scale] duration-320 ease-tmm17-settle group-hover/card:scale-106 motion-reduce:transition-none" src="https://picsum.photos/seed/fern-studio/480/360" alt="" width="480" height="360" decoding="async"></span>
                    <span class="mt-1.5 flex items-center justify-between gap-2 font-tmm17-display text-[0.98rem]/snug font-semibold group-hover/card:text-tmm17-acc">Workspace<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></span>
                    <span class="text-[0.78rem] text-tmm17-mut">18 pieces &middot; desk scale</span>
                  </a></li>
                  <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-310 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="group/card grid min-w-0 gap-0.5 text-inherit">
                    <span class="relative block aspect-[4/3] overflow-hidden rounded-[14px] bg-tmm17-line"><img class="block size-full object-cover transition-[scale] duration-320 ease-tmm17-settle group-hover/card:scale-106 motion-reduce:transition-none" src="https://picsum.photos/seed/fern-bath/480/360" alt="" width="480" height="360" loading="lazy" decoding="async"></span>
                    <span class="mt-1.5 flex items-center justify-between gap-2 font-tmm17-display text-[0.98rem]/snug font-semibold group-hover/card:text-tmm17-acc">Bathroom<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></span>
                    <span class="text-[0.78rem] text-tmm17-mut">12 pieces &middot; humidity</span>
                  </a></li>
                  <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-400 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="group/card grid min-w-0 gap-0.5 text-inherit">
                    <span class="relative block aspect-[4/3] overflow-hidden rounded-[14px] bg-tmm17-line"><img class="block size-full object-cover transition-[scale] duration-320 ease-tmm17-settle group-hover/card:scale-106 motion-reduce:transition-none" src="https://picsum.photos/seed/fern-balcony/480/360" alt="" width="480" height="360" loading="lazy" decoding="async"></span>
                    <span class="mt-1.5 flex items-center justify-between gap-2 font-tmm17-display text-[0.98rem]/snug font-semibold group-hover/card:text-tmm17-acc">Balcony<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></span>
                    <span class="text-[0.78rem] text-tmm17-mut">27 pieces &middot; hardy</span>
                  </a></li>
                  <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-490 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="group/card grid min-w-0 gap-0.5 text-inherit">
                    <span class="relative block aspect-[4/3] overflow-hidden rounded-[14px] bg-tmm17-line"><img class="block size-full object-cover transition-[scale] duration-320 ease-tmm17-settle group-hover/card:scale-106 motion-reduce:transition-none" src="https://picsum.photos/seed/fern-hall/480/360" alt="" width="480" height="360" loading="lazy" decoding="async"></span>
                    <span class="mt-1.5 flex items-center justify-between gap-2 font-tmm17-display text-[0.98rem]/snug font-semibold group-hover/card:text-tmm17-acc">Hallway<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></span>
                    <span class="text-[0.78rem] text-tmm17-mut">9 pieces &middot; shade</span>
                  </a></li>
                </ul>
                <div class="grid min-w-0 content-start gap-1 rounded-2xl bg-tmm17-acc/9 p-[clamp(0.9rem,2.4vw,1.2rem)]">
                  <p class="font-tmm17-display text-[0.7rem]/none font-bold tracking-[0.16em] text-tmm17-acc uppercase">Care and setup</p>
                  <ul class="grid gap-px">
                    <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-260 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm17-ink underline-offset-3 hover:text-tmm17-acc hover:underline">Light and watering guide</a></li>
                    <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-330 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm17-ink underline-offset-3 hover:text-tmm17-acc hover:underline">Repotting service</a></li>
                    <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-400 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm17-ink underline-offset-3 hover:text-tmm17-acc hover:underline">Studio consultations</a></li>
                    <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-470 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm17-ink underline-offset-3 hover:text-tmm17-acc hover:underline">Plant doctor</a></li>
                  </ul>
                  <a class="mt-1.5 inline-flex min-h-11 w-fit items-center gap-2 rounded-full bg-tmm17-acc px-4 font-tmm17-display text-[0.86rem]/none font-bold text-tmm17-on-acc hover:brightness-110" href="#tmm17-title">Book a home visit <span aria-hidden="true">&rarr;</span></a>
                </div>
              </div>
            </div>
          </li>
          <li data-tmm17-item class="flex items-center max-[52rem]:block">
            <button type="button" id="tmm17-trigger-pots" aria-expanded="false" aria-controls="tmm17-panel-pots" class="relative after:absolute after:inset-x-0 after:top-full after:h-9 after:pointer-events-none tmm17-open:after:pointer-events-auto max-[52rem]:after:hidden inline-flex min-h-11 cursor-pointer items-center gap-1.5 rounded-full px-4 font-tmm17-display text-[0.92rem]/none font-semibold text-tmm17-ink transition-colors hover:text-tmm17-acc tmm17-open:bg-tmm17-acc/16 tmm17-open:text-tmm17-acc!">Pots &amp; care<svg class="size-3.5 transition-transform duration-200 tmm17-open:rotate-180 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm17-line bg-tmm17-surf opacity-0 shadow-tmm17-panel pointer-events-none transition-[opacity,visibility] duration-180 tmm17-open:visible tmm17-open:opacity-100 tmm17-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:shadow-none max-[52rem]:tmm17-open:block" id="tmm17-panel-pots" aria-labelledby="tmm17-trigger-pots">
              <div class="mx-auto grid w-[min(80rem,calc(100%-2rem))] gap-[clamp(1rem,3vw,2rem)] py-[clamp(1.1rem,3vw,2rem)] min-[68rem]:grid-cols-[minmax(0,1fr)_17rem] max-[52rem]:w-full max-[52rem]:px-4">
                <ul class="grid min-w-0 grid-cols-[repeat(auto-fit,minmax(11rem,1fr))] gap-[clamp(0.6rem,2vw,1rem)]">
                  <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-40 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="group/card grid min-w-0 gap-0.5 text-inherit">
                    <span class="relative block aspect-[4/3] overflow-hidden rounded-[14px] bg-tmm17-line"><img class="block size-full object-cover transition-[scale] duration-320 ease-tmm17-settle group-hover/card:scale-106 motion-reduce:transition-none" src="https://picsum.photos/seed/fern-terracotta/480/360" alt="" width="480" height="360" loading="lazy" decoding="async"></span>
                    <span class="mt-1.5 flex items-center justify-between gap-2 font-tmm17-display text-[0.98rem]/snug font-semibold group-hover/card:text-tmm17-acc">Terracotta<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></span>
                    <span class="text-[0.78rem] text-tmm17-mut">6 sizes</span>
                  </a></li>
                  <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-130 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="group/card grid min-w-0 gap-0.5 text-inherit">
                    <span class="relative block aspect-[4/3] overflow-hidden rounded-[14px] bg-tmm17-line"><img class="block size-full object-cover transition-[scale] duration-320 ease-tmm17-settle group-hover/card:scale-106 motion-reduce:transition-none" src="https://picsum.photos/seed/fern-stoneware/480/360" alt="" width="480" height="360" loading="lazy" decoding="async"></span>
                    <span class="mt-1.5 flex items-center justify-between gap-2 font-tmm17-display text-[0.98rem]/snug font-semibold group-hover/card:text-tmm17-acc">Stoneware<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></span>
                    <span class="text-[0.78rem] text-tmm17-mut">glazed</span>
                  </a></li>
                  <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-220 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="group/card grid min-w-0 gap-0.5 text-inherit">
                    <span class="relative block aspect-[4/3] overflow-hidden rounded-[14px] bg-tmm17-line"><img class="block size-full object-cover transition-[scale] duration-320 ease-tmm17-settle group-hover/card:scale-106 motion-reduce:transition-none" src="https://picsum.photos/seed/fern-stands/480/360" alt="" width="480" height="360" loading="lazy" decoding="async"><span class="absolute top-2 left-2 rounded-full bg-tmm17-surf/90 px-2 py-1 text-[0.68rem]/none font-semibold text-tmm17-ink backdrop-blur-sm">New</span></span>
                    <span class="mt-1.5 flex items-center justify-between gap-2 font-tmm17-display text-[0.98rem]/snug font-semibold group-hover/card:text-tmm17-acc">Stands<span aria-hidden="true" class="-translate-x-1 opacity-0 transition-[opacity,translate] group-hover/card:translate-x-0 group-hover/card:opacity-100">&rarr;</span></span>
                    <span class="text-[0.78rem] text-tmm17-mut">oak and steel</span>
                  </a></li>
                </ul>
                <div class="grid min-w-0 content-start gap-1 rounded-2xl bg-tmm17-acc/9 p-[clamp(0.9rem,2.4vw,1.2rem)]">
                  <p class="font-tmm17-display text-[0.7rem]/none font-bold tracking-[0.16em] text-tmm17-acc uppercase">Essentials</p>
                  <ul class="grid gap-px">
                    <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-260 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm17-ink underline-offset-3 hover:text-tmm17-acc hover:underline">Soil and grit</a></li>
                    <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-330 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm17-ink underline-offset-3 hover:text-tmm17-acc hover:underline">Feed</a></li>
                    <li class="translate-y-3 scale-[0.985] opacity-0 transition-[opacity,translate,scale] duration-[420ms,580ms,580ms] ease-tmm17-settle delay-400 tmm17-open:translate-y-0 tmm17-open:scale-100 tmm17-open:opacity-100 motion-reduce:translate-y-0 motion-reduce:scale-100 motion-reduce:opacity-100 motion-reduce:transition-none"><a href="#tmm17-title" class="flex min-h-11 min-w-0 items-center text-[0.92rem] text-tmm17-ink underline-offset-3 hover:text-tmm17-acc hover:underline">Tools</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>
          <li class="flex items-center"><a class="inline-flex min-h-11 items-center rounded-full px-4 font-tmm17-display text-[0.92rem]/none font-semibold text-tmm17-ink hover:text-tmm17-acc" href="#tmm17-title">Journal</a></li>
          <li class="flex items-center"><a class="inline-flex min-h-11 items-center rounded-full px-4 font-tmm17-display text-[0.92rem]/none font-semibold text-tmm17-ink hover:text-tmm17-acc" href="#tmm17-title">Studio</a></li>
        </ul>
      </nav>
      <div class="ml-auto flex items-center gap-2 max-[52rem]:ml-0">
        <a class="inline-flex min-h-11 items-center px-2.5 font-tmm17-display text-[0.88rem]/none font-semibold text-tmm17-mut hover:text-tmm17-ink" href="#tmm17-title">Account</a>
        <a class="inline-flex min-h-10 items-center gap-2 rounded-full border border-tmm17-line px-4 font-tmm17-display text-[0.86rem]/none font-semibold text-tmm17-ink transition-colors hover:border-tmm17-acc" href="#tmm17-title">Basket <span class="grid size-5 place-items-center rounded-full bg-tmm17-acc text-[0.68rem] text-tmm17-on-acc">2</span></a>
      </div>
    </div>
  </header>

  <main class="mx-auto w-[min(80rem,calc(100%-2rem))] py-[clamp(3rem,9vw,5.5rem)]">
    <div class="grid max-w-[34rem] gap-2.5">
      <p class="font-tmm17-display text-[0.72rem]/none font-bold tracking-[0.2em] text-tmm17-acc uppercase">Delivered in 3 days, potted and fed</p>
      <h1 class="font-tmm17-display text-[clamp(2rem,6vw,3.4rem)]/[1.06] font-semibold tracking-[-0.025em] text-balance">Plants chosen for the light you actually have.</h1>
      <a class="mt-1.5 inline-flex min-h-12 w-fit items-center gap-2 rounded-full bg-tmm17-acc px-5.5 font-tmm17-display text-[0.94rem]/none font-bold text-tmm17-on-acc hover:brightness-110" href="#tmm17-title">Take the light quiz <span aria-hidden="true">&rarr;</span></a>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm17-bg: #f3f1ea;
  --color-tmm17-bg: oklch(0.957 0.01 95);
  --color-tmm17-surf: #fbfaf6;
  --color-tmm17-surf: oklch(0.985 0.006 95);
  --color-tmm17-line: #ddd8c9;
  --color-tmm17-line: oklch(0.88 0.02 95);
  --color-tmm17-ink: #23261f;
  --color-tmm17-ink: oklch(0.26 0.012 125);
  --color-tmm17-mut: #5f6455;
  --color-tmm17-mut: oklch(0.48 0.02 125);
  --color-tmm17-acc: #4a6b46;
  --color-tmm17-acc: oklch(0.47 0.08 145);
  --color-tmm17-on-acc: #ffffff;
  --color-tmm17-on-acc: oklch(1 0 0);
  --font-tmm17-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tmm17-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --shadow-tmm17-panel: 0 34px 70px -40px rgb(35 38 31 / 0.55);
  --ease-tmm17-settle: cubic-bezier(0.16, 1, 0.3, 1);
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm17-open: instead of a repeated selector list. */

@custom-variant tmm17-open {
  &:where([data-tmm17-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm17-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-17 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-17:has(#tmm17-theme:checked) {
  --color-tmm17-bg: #0e100d;
  --color-tmm17-bg: oklch(0.16 0.008 130);
  --color-tmm17-surf: #171a14;
  --color-tmm17-surf: oklch(0.2 0.012 130);
  --color-tmm17-line: #2a2f25;
  --color-tmm17-line: oklch(0.3 0.016 130);
  --color-tmm17-ink: #eef1e8;
  --color-tmm17-ink: oklch(0.95 0.012 125);
  --color-tmm17-mut: #9ba393;
  --color-tmm17-mut: oklch(0.71 0.02 125);
  --color-tmm17-acc: #8fce87;
  --color-tmm17-acc: oklch(0.8 0.12 145);
  --color-tmm17-on-acc: #0f1d0d;
  --color-tmm17-on-acc: oklch(0.2 0.04 145);
}

@media (prefers-color-scheme: dark) {
  .tmm-17 {
    --color-tmm17-bg: #0e100d;
    --color-tmm17-bg: oklch(0.16 0.008 130);
    --color-tmm17-surf: #171a14;
    --color-tmm17-surf: oklch(0.2 0.012 130);
    --color-tmm17-line: #2a2f25;
    --color-tmm17-line: oklch(0.3 0.016 130);
    --color-tmm17-ink: #eef1e8;
    --color-tmm17-ink: oklch(0.95 0.012 125);
    --color-tmm17-mut: #9ba393;
    --color-tmm17-mut: oklch(0.71 0.02 125);
    --color-tmm17-acc: #8fce87;
    --color-tmm17-acc: oklch(0.8 0.12 145);
    --color-tmm17-on-acc: #0f1d0d;
    --color-tmm17-on-acc: oklch(0.2 0.04 145);
  }

  .tmm-17:has(#tmm17-theme:checked) {
    --color-tmm17-bg: #f3f1ea;
    --color-tmm17-bg: oklch(0.957 0.01 95);
    --color-tmm17-surf: #fbfaf6;
    --color-tmm17-surf: oklch(0.985 0.006 95);
    --color-tmm17-line: #ddd8c9;
    --color-tmm17-line: oklch(0.88 0.02 95);
    --color-tmm17-ink: #23261f;
    --color-tmm17-ink: oklch(0.26 0.012 125);
    --color-tmm17-mut: #5f6455;
    --color-tmm17-mut: oklch(0.48 0.02 125);
    --color-tmm17-acc: #4a6b46;
    --color-tmm17-acc: oklch(0.47 0.08 145);
    --color-tmm17-on-acc: #ffffff;
    --color-tmm17-on-acc: oklch(1 0 0);
  }
}
```
