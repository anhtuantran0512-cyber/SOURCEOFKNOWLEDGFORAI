---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-accordion-marquee-scrolling-title/"
title: "Tailwind CSS Accordion with Marquee Scrolling Title"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A festival line-up where the open stage's header turns into a ticker: the title, doubled exactly, scrolls across an acid-green band while closed headers stay…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Accordion with Marquee Scrolling Title
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-accordion-marquee-scrolling-title/

A festival line-up where the open stage's header turns into a ticker: the title, doubled exactly, scrolls across an acid-green band while closed headers stay still. The loop is one --animate-tac18-marquee theme token, the pause on hover and focus is [animation-play-state:paused] behind a group variant, and motion-reduce: swaps the ticker back to a static title. <details name> means only one marquee ever runs.
## HTML
```html
<section class="tac-18 w-full min-h-svh grid place-items-center bg-tac18-bg bg-[radial-gradient(70%_45%_at_50%_110%,var(--color-tac18-glow),transparent_70%)] px-5 py-14 font-tac18-sans text-tac18-ink [interpolate-size:allow-keywords]" aria-label="Marquee scrolling title accordion demo">
  <div class="grid w-full justify-items-center gap-8">
    <div class="w-full max-w-[680px]">
      <header class="mb-6 flex flex-wrap items-end justify-between gap-x-6 gap-y-3">
        <div>
          <p class="font-tac18-mono text-xs tracking-[0.18em] uppercase text-tac18-acc">Line-up · 24–26 July · Rotterdam</p>
          <h2 class="mt-2 font-tac18-display text-[clamp(30px,6vw,46px)] leading-none font-black tracking-[-0.03em] uppercase">Nocturne<span class="text-tac18-acc">’26</span></h2>
        </div>
        <p class="inline-flex items-center gap-2 rounded-full border border-white/15 px-3 py-1.5 font-tac18-mono text-xs text-tac18-mut"><span class="size-1.5 animate-pulse rounded-full bg-tac18-acc motion-reduce:animate-none" aria-hidden="true"></span>Weekend pass · 87% sold</p>
      </header>

      <div class="border-b-2 border-tac18-ink">
        <details name="tac18-stage" class="group border-t-2 border-tac18-ink [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-500 [&::details-content]:ease-[cubic-bezier(.2,.8,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none" open>
          <summary class="group/sum relative flex min-h-[clamp(68px,11vw,92px)] cursor-pointer list-none items-center overflow-hidden transition-colors duration-300 group-open:bg-tac18-acc group-open:text-tac18-bg focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tac18-acc group-open:focus-visible:outline-tac18-bg [&::-webkit-details-marker]:hidden">
            <span class="flex items-baseline gap-4 px-3 pr-16 transition-opacity duration-200 group-open:opacity-0 motion-reduce:group-open:opacity-100">
              <span class="font-tac18-mono text-xs text-tac18-mut group-open:text-tac18-bg">01</span>
              <span class="font-tac18-display text-[clamp(24px,5vw,40px)] leading-none font-extrabold tracking-[-0.02em] uppercase group-hover/sum:text-tac18-acc group-open:group-hover/sum:text-tac18-bg">Turbine Hall</span>
            </span>
            <span class="absolute inset-0 hidden items-center group-open:flex motion-reduce:group-open:hidden" aria-hidden="true">
              <span class="flex w-max animate-tac18-marquee group-focus-within:[animation-play-state:paused] group-hover/sum:[animation-play-state:paused]">
                <span class="flex shrink-0 items-center gap-6 pr-6 font-tac18-display text-[clamp(24px,5vw,40px)] font-extrabold tracking-[-0.02em] whitespace-nowrap uppercase">Turbine Hall<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Fri 24 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Turbine Hall<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Fri 24 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg></span>
                <span class="flex shrink-0 items-center gap-6 pr-6 font-tac18-display text-[clamp(24px,5vw,40px)] font-extrabold tracking-[-0.02em] whitespace-nowrap uppercase">Turbine Hall<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Fri 24 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Turbine Hall<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Fri 24 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg></span>
              </span>
            </span>
            <span class="absolute inset-y-0 right-0 z-10 grid place-items-center pr-3 pl-10 group-open:bg-linear-to-l group-open:from-tac18-acc group-open:from-60% group-open:to-transparent" aria-hidden="true">
              <span class="grid size-10 place-items-center rounded-full border border-white/25 transition duration-300 group-hover/sum:border-tac18-acc group-hover/sum:text-tac18-acc group-open:rotate-45 group-open:border-tac18-bg group-open:bg-tac18-bg group-open:text-tac18-acc motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 16 16"><path d="M8 2.5v11M2.5 8h11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
            </span>
          </summary>
          <div class="grid gap-6 px-3 pt-5 pb-7 sm:grid-cols-[1fr_auto]">
            <ul class="grid gap-px overflow-hidden rounded-xl bg-white/10 ring-1 ring-white/10">
              <li class="flex items-center gap-4 bg-tac18-panel px-4 py-3"><span class="w-12 font-tac18-mono text-sm text-tac18-acc">22:00</span><span class="flex-1 font-semibold">Mono Tide</span><span class="font-tac18-mono text-xs text-tac18-mut">dub techno</span></li>
              <li class="flex items-center gap-4 bg-tac18-panel px-4 py-3"><span class="w-12 font-tac18-mono text-sm text-tac18-acc">00:00</span><span class="flex-1 font-semibold">Sólveig Ray <span class="ml-1 inline-block rounded bg-tac18-acc px-1.5 py-0.5 align-[2px] whitespace-nowrap font-tac18-mono text-[10px] font-bold text-tac18-bg uppercase">Live AV</span></span><span class="font-tac18-mono text-xs text-tac18-mut">industrial</span></li>
              <li class="flex items-center gap-4 bg-tac18-panel px-4 py-3"><span class="w-12 font-tac18-mono text-sm text-tac18-acc">02:30</span><span class="flex-1 font-semibold">Odd Forma b2b Lune</span><span class="font-tac18-mono text-xs text-tac18-mut">electro</span></li>
            </ul>
            <div class="flex flex-col justify-between gap-4 sm:w-44">
              <p class="text-sm leading-relaxed text-tac18-mut">Capacity 4,200. Doors 21:30, last entry 03:00. Earplugs at the bar, free.</p>
              <button type="button" class="inline-flex min-h-11 items-center justify-center gap-2 rounded-full border-2 border-tac18-acc px-4 text-sm font-bold text-tac18-acc transition hover:bg-tac18-acc hover:text-tac18-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac18-acc">Add to my plan</button>
            </div>
          </div>
        </details>

        <details name="tac18-stage" class="group border-t-2 border-tac18-ink [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-500 [&::details-content]:ease-[cubic-bezier(.2,.8,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none">
          <summary class="group/sum relative flex min-h-[clamp(68px,11vw,92px)] cursor-pointer list-none items-center overflow-hidden transition-colors duration-300 group-open:bg-tac18-acc group-open:text-tac18-bg focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tac18-acc group-open:focus-visible:outline-tac18-bg [&::-webkit-details-marker]:hidden">
            <span class="flex items-baseline gap-4 px-3 pr-16 transition-opacity duration-200 group-open:opacity-0 motion-reduce:group-open:opacity-100">
              <span class="font-tac18-mono text-xs text-tac18-mut group-open:text-tac18-bg">02</span>
              <span class="font-tac18-display text-[clamp(24px,5vw,40px)] leading-none font-extrabold tracking-[-0.02em] uppercase group-hover/sum:text-tac18-acc group-open:group-hover/sum:text-tac18-bg">Basement</span>
            </span>
            <span class="absolute inset-0 hidden items-center group-open:flex motion-reduce:group-open:hidden" aria-hidden="true">
              <span class="flex w-max animate-tac18-marquee group-focus-within:[animation-play-state:paused] group-hover/sum:[animation-play-state:paused]">
                <span class="flex shrink-0 items-center gap-6 pr-6 font-tac18-display text-[clamp(24px,5vw,40px)] font-extrabold tracking-[-0.02em] whitespace-nowrap uppercase">Basement<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Sat 25 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Basement<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Sat 25 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg></span>
                <span class="flex shrink-0 items-center gap-6 pr-6 font-tac18-display text-[clamp(24px,5vw,40px)] font-extrabold tracking-[-0.02em] whitespace-nowrap uppercase">Basement<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Sat 25 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Basement<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Sat 25 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg></span>
              </span>
            </span>
            <span class="absolute inset-y-0 right-0 z-10 grid place-items-center pr-3 pl-10 group-open:bg-linear-to-l group-open:from-tac18-acc group-open:from-60% group-open:to-transparent" aria-hidden="true">
              <span class="grid size-10 place-items-center rounded-full border border-white/25 transition duration-300 group-hover/sum:border-tac18-acc group-hover/sum:text-tac18-acc group-open:rotate-45 group-open:border-tac18-bg group-open:bg-tac18-bg group-open:text-tac18-acc motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 16 16"><path d="M8 2.5v11M2.5 8h11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
            </span>
          </summary>
          <div class="grid gap-6 px-3 pt-5 pb-7 sm:grid-cols-[1fr_auto]">
            <ul class="grid gap-px overflow-hidden rounded-xl bg-white/10 ring-1 ring-white/10">
              <li class="flex items-center gap-4 bg-tac18-panel px-4 py-3"><span class="w-12 font-tac18-mono text-sm text-tac18-acc">23:00</span><span class="flex-1 font-semibold">Hexa Juno</span><span class="font-tac18-mono text-xs text-tac18-mut">acid house</span></li>
              <li class="flex items-center gap-4 bg-tac18-panel px-4 py-3"><span class="w-12 font-tac18-mono text-sm text-tac18-acc">01:30</span><span class="flex-1 font-semibold">Kiri Ost</span><span class="font-tac18-mono text-xs text-tac18-mut">breaks</span></li>
              <li class="flex items-center gap-4 bg-tac18-panel px-4 py-3"><span class="w-12 font-tac18-mono text-sm text-tac18-acc">04:00</span><span class="flex-1 font-semibold">Pale Signal <span class="ml-1 inline-block rounded bg-tac18-acc px-1.5 py-0.5 align-[2px] whitespace-nowrap font-tac18-mono text-[10px] font-bold text-tac18-bg uppercase">All night</span></span><span class="font-tac18-mono text-xs text-tac18-mut">minimal</span></li>
            </ul>
            <div class="flex flex-col justify-between gap-4 sm:w-44">
              <p class="text-sm leading-relaxed text-tac18-mut">Low ceiling, one Funktion-One rig, no phones on the floor. Capacity 600.</p>
              <button type="button" class="inline-flex min-h-11 items-center justify-center gap-2 rounded-full border-2 border-tac18-acc px-4 text-sm font-bold text-tac18-acc transition hover:bg-tac18-acc hover:text-tac18-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac18-acc">Add to my plan</button>
            </div>
          </div>
        </details>

        <details name="tac18-stage" class="group border-t-2 border-tac18-ink [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-500 [&::details-content]:ease-[cubic-bezier(.2,.8,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none">
          <summary class="group/sum relative flex min-h-[clamp(68px,11vw,92px)] cursor-pointer list-none items-center overflow-hidden transition-colors duration-300 group-open:bg-tac18-acc group-open:text-tac18-bg focus-visible:outline-3 focus-visible:-outline-offset-3 focus-visible:outline-tac18-acc group-open:focus-visible:outline-tac18-bg [&::-webkit-details-marker]:hidden">
            <span class="flex items-baseline gap-4 px-3 pr-16 transition-opacity duration-200 group-open:opacity-0 motion-reduce:group-open:opacity-100">
              <span class="font-tac18-mono text-xs text-tac18-mut group-open:text-tac18-bg">03</span>
              <span class="font-tac18-display text-[clamp(24px,5vw,40px)] leading-none font-extrabold tracking-[-0.02em] uppercase group-hover/sum:text-tac18-acc group-open:group-hover/sum:text-tac18-bg">Rooftop</span>
            </span>
            <span class="absolute inset-0 hidden items-center group-open:flex motion-reduce:group-open:hidden" aria-hidden="true">
              <span class="flex w-max animate-tac18-marquee group-focus-within:[animation-play-state:paused] group-hover/sum:[animation-play-state:paused]">
                <span class="flex shrink-0 items-center gap-6 pr-6 font-tac18-display text-[clamp(24px,5vw,40px)] font-extrabold tracking-[-0.02em] whitespace-nowrap uppercase">Rooftop<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Sun 26 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Rooftop<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Sun 26 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg></span>
                <span class="flex shrink-0 items-center gap-6 pr-6 font-tac18-display text-[clamp(24px,5vw,40px)] font-extrabold tracking-[-0.02em] whitespace-nowrap uppercase">Rooftop<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Sun 26 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Rooftop<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg>Sun 26 Jul<svg class="size-[0.6em]" viewBox="0 0 20 20"><path d="M10 0c.6 5.6 4.4 9.4 10 10-5.6.6-9.4 4.4-10 10-.6-5.6-4.4-9.4-10-10 5.6-.6 9.4-4.4 10-10z" fill="currentColor"/></svg></span>
              </span>
            </span>
            <span class="absolute inset-y-0 right-0 z-10 grid place-items-center pr-3 pl-10 group-open:bg-linear-to-l group-open:from-tac18-acc group-open:from-60% group-open:to-transparent" aria-hidden="true">
              <span class="grid size-10 place-items-center rounded-full border border-white/25 transition duration-300 group-hover/sum:border-tac18-acc group-hover/sum:text-tac18-acc group-open:rotate-45 group-open:border-tac18-bg group-open:bg-tac18-bg group-open:text-tac18-acc motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 16 16"><path d="M8 2.5v11M2.5 8h11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
            </span>
          </summary>
          <div class="grid gap-6 px-3 pt-5 pb-7 sm:grid-cols-[1fr_auto]">
            <ul class="grid gap-px overflow-hidden rounded-xl bg-white/10 ring-1 ring-white/10">
              <li class="flex items-center gap-4 bg-tac18-panel px-4 py-3"><span class="w-12 font-tac18-mono text-sm text-tac18-acc">14:00</span><span class="flex-1 font-semibold">Ama Lua</span><span class="font-tac18-mono text-xs text-tac18-mut">balearic</span></li>
              <li class="flex items-center gap-4 bg-tac18-panel px-4 py-3"><span class="w-12 font-tac18-mono text-sm text-tac18-acc">17:00</span><span class="flex-1 font-semibold">The Verandas</span><span class="font-tac18-mono text-xs text-tac18-mut">disco</span></li>
              <li class="flex items-center gap-4 bg-tac18-panel px-4 py-3"><span class="w-12 font-tac18-mono text-sm text-tac18-acc">20:30</span><span class="flex-1 font-semibold">Nils Arc <span class="ml-1 inline-block rounded bg-tac18-acc px-1.5 py-0.5 align-[2px] whitespace-nowrap font-tac18-mono text-[10px] font-bold text-tac18-bg uppercase">Closing</span></span><span class="font-tac18-mono text-xs text-tac18-mut">house</span></li>
            </ul>
            <div class="flex flex-col justify-between gap-4 sm:w-44">
              <p class="text-sm leading-relaxed text-tac18-mut">Open air, sunset at 21:48. Day tickets only, no re-entry after 22:00.</p>
              <button type="button" class="inline-flex min-h-11 items-center justify-center gap-2 rounded-full border-2 border-tac18-acc px-4 text-sm font-bold text-tac18-acc transition hover:bg-tac18-acc hover:text-tac18-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac18-acc">Add to my plan</button>
            </div>
          </div>
        </details>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/15 px-3.5 py-2 font-tac18-mono text-[11.5px] text-tac18-mut">animate-tac18-marquee · group-hover/sum:[animation-play-state:paused] · details name</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac18-bg: #0a0a0a;
  --color-tac18-bg: oklch(0.15 0 0);
  --color-tac18-glow: #2f420080;
  --color-tac18-glow: oklch(0.36 0.09 125 / 0.5);
  --color-tac18-panel: #141414;
  --color-tac18-panel: oklch(0.2 0 0);
  --color-tac18-ink: #f4f4ef;
  --color-tac18-ink: oklch(0.966 0.006 107);
  --color-tac18-mut: #a6a69e;
  --color-tac18-mut: oklch(0.73 0.01 107);
  --color-tac18-acc: #c6ff3d;
  --color-tac18-acc: oklch(0.93 0.21 128);
  --font-tac18-display: 'Unbounded', 'Arial Black', system-ui, sans-serif;
  --font-tac18-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tac18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tac18-marquee: tac18-marquee 22s linear infinite;

  @keyframes tac18-marquee {
    from {
      transform: translateX(0);
    }

    to {
      transform: translateX(-50%);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-18 {
  width: 100%;
  min-height: 100svh;
}
```
