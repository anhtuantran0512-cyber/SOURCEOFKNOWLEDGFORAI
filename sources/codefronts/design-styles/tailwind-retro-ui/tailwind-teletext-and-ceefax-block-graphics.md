---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-teletext-and-ceefax-block-graphics/"
title: "Tailwind Teletext and Ceefax Block Graphics"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "The British broadcast text format rebuilt cell by cell: 40&times;25 characters, seven saturated colours on black, double-height headline rows, and mosaic…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Teletext and Ceefax Block Graphics
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-teletext-and-ceefax-block-graphics/

The British broadcast text format rebuilt cell by cell: 40&times;25 characters, seven saturated colours on black, double-height headline rows, and mosaic graphics assembled from 2&times;3 subcells inside single character cells. In utilities the mosaic becomes something the CSS version could not be &mdash; every subcell states its own colour, so the picture is legible in the markup.
## HTML
```html
<section class="twr-07 relative block w-full min-h-svh box-border bg-twr07-bg text-twr07-ink font-twr07-mono" aria-labelledby="twr-07-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-07-title">Teletext Level 1 page with mosaic block graphics</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-07-theme">
    <label class="grid place-items-center size-11 border border-twr07-line bg-twr07-surface text-twr07-ink2 cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-twr07-acc peer-focus-visible:outline-offset-2" for="twr-07-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle light surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-4.5 max-w-[68rem] mx-auto px-[clamp(0.6rem,0.4rem+1.5vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16 lg:grid-cols-[minmax(0,1.5fr)_minmax(0,1fr)]">
    <p class="m-0 justify-self-start min-w-0 lg:col-span-2 border border-twr07-line bg-twr07-surface px-2.5 py-1.5 text-[0.68rem] tracking-[0.12em] uppercase text-twr07-ink2">Teletext Level 1 &middot; 40 &times; 25 cells &middot; 7 colours + black</p>

    <div class="min-w-0 rounded-lg bg-[#3a3d42] p-[clamp(0.5rem,0.3rem+1vw,0.9rem)] [box-shadow:inset_0_1px_0_rgba(255,255,255,0.2),0_16px_34px_-18px_rgba(0,0,0,0.7)]">
      <div class="twr-07__page @container min-w-0 overflow-hidden bg-twr07-k text-twr07-w px-[0.5ch] py-2 leading-[1.28] tracking-[0.02em] text-[min(1rem,4.4cqi)]">
        <p class="m-0 min-w-0 overflow-hidden whitespace-pre"><span class="text-twr07-w">P170</span> <span class="text-twr07-c">CEEFAX 170</span> <span class="text-twr07-g">Mon 07 Sep</span> <span class="text-twr07-y animate-twr07-flash motion-reduce:animate-none">20:14/32</span></p>

        <p class="m-0 min-w-0 overflow-hidden whitespace-pre font-bold tracking-[0.06em] text-twr07-y scale-y-200 origin-top-left">WEATHER</p>
        <p class="m-0 min-w-0 overflow-hidden whitespace-pre h-[1.28em]" aria-hidden="true">&nbsp;</p>

        <p class="m-0 min-w-0 overflow-hidden whitespace-pre text-twr07-c">────────────────────────────────────────</p>

        <div class="grid gap-2 py-1.5 min-w-0">
          <div class="grid grid-cols-[repeat(15,2ch)] justify-start min-w-0" aria-hidden="true"><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-y"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-y"></i><i class="block"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-y"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block bg-twr07-y"></i><i class="block"></i><i class="block bg-twr07-y"></i><i class="block"></i><i class="block bg-twr07-y"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-y"></i><i class="block"></i><i class="block bg-twr07-y"></i><i class="block"></i><i class="block bg-twr07-y"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-w"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-w"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block"></i><i class="block bg-twr07-y"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block bg-twr07-y"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block bg-twr07-w"></i><i class="block"></i><i class="block bg-twr07-w"></i><i class="block"></i><i class="block bg-twr07-c"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block"></i><i class="block bg-twr07-c"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block"></i><i class="block bg-twr07-c"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block bg-twr07-w"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-c"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-c"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-c"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-c"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-c"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-c"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-c"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block bg-twr07-c"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block bg-twr07-c"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span><span class="grid grid-cols-2 grid-rows-3 h-[3ch]"><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i><i class="block"></i></span></div>
          <p class="m-0 min-w-0 text-[0.78em] leading-snug text-pretty text-twr07-c">Mosaic graphic: a yellow sun beside a white cloud, with three cyan rain strokes below it.</p>
        </div>

        <p class="m-0 min-w-0 overflow-hidden whitespace-pre text-twr07-w">SOUTH EAST&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-twr07-y">18C</span>&nbsp;&nbsp;SUNNY SPELLS</p>
        <p class="m-0 min-w-0 overflow-hidden whitespace-pre text-twr07-w">MIDLANDS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-twr07-y">15C</span>&nbsp;&nbsp;SHOWERS LATER</p>
        <p class="m-0 min-w-0 overflow-hidden whitespace-pre text-twr07-w">HIGHLANDS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-twr07-y">11C</span>&nbsp;&nbsp;RAIN, WINDY</p>
        <p class="m-0 min-w-0 overflow-hidden whitespace-pre text-twr07-w">N IRELAND&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-twr07-y">14C</span>&nbsp;&nbsp;BRIGHT, COOL</p>

        <p class="m-0 min-w-0 overflow-hidden whitespace-pre text-twr07-c">────────────────────────────────────────</p>
        <p class="m-0 min-w-0 overflow-hidden whitespace-pre text-twr07-g">OUTLOOK  Unsettled through midweek with</p>
        <p class="m-0 min-w-0 overflow-hidden whitespace-pre text-twr07-g">brighter intervals from Thursday.</p>

        <nav class="mt-2.5 min-w-0" aria-label="FASTEXT links">
          <ul class="list-none m-0 p-0 flex flex-wrap gap-0.5">
            <li class="flex-1"><button class="flex-1 min-h-11 min-w-11 px-2.5 py-1.5 border-0 font-inherit text-[0.82em] font-bold cursor-pointer text-twr07-k focus-visible:outline-2 focus-visible:outline-twr07-w focus-visible:outline-offset-[-4px] bg-twr07-r text-twr07-w" type="button">Index</button></li>
            <li class="flex-1"><button class="flex-1 min-h-11 min-w-11 px-2.5 py-1.5 border-0 font-inherit text-[0.82em] font-bold cursor-pointer text-twr07-k focus-visible:outline-2 focus-visible:outline-twr07-w focus-visible:outline-offset-[-4px] bg-twr07-g" type="button">Regions</button></li>
            <li class="flex-1"><button class="flex-1 min-h-11 min-w-11 px-2.5 py-1.5 border-0 font-inherit text-[0.82em] font-bold cursor-pointer text-twr07-k focus-visible:outline-2 focus-visible:outline-twr07-w focus-visible:outline-offset-[-4px] bg-twr07-y" type="button">Charts</button></li>
            <li class="flex-1"><button class="flex-1 min-h-11 min-w-11 px-2.5 py-1.5 border-0 font-inherit text-[0.82em] font-bold cursor-pointer text-twr07-k focus-visible:outline-2 focus-visible:outline-twr07-w focus-visible:outline-offset-[-4px] bg-twr07-c" type="button">Travel</button></li>
          </ul>
        </nav>
      </div>
    </div>

    <aside class="min-w-0 grid content-start gap-2.5 border border-twr07-line bg-twr07-surface p-[clamp(0.8rem,0.6rem+0.8vw,1.1rem)]">
      <h3 class="m-0 text-[0.72rem] tracking-[0.1em] uppercase text-twr07-ink2">Level 1 palette &mdash; three bits, eight states</h3>
      <ul class="list-none m-0 p-0 min-w-0 grid gap-1.5 grid-cols-[repeat(auto-fit,minmax(min(100%,8rem),1fr))]">
        <li class="flex items-center gap-2 min-w-0 text-[0.75rem] text-twr07-ink2"><span class="flex-none size-[18px] border border-twr07-line bg-[#ff0000]"></span>100 red</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.75rem] text-twr07-ink2"><span class="flex-none size-[18px] border border-twr07-line bg-[#00ff00]"></span>010 green</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.75rem] text-twr07-ink2"><span class="flex-none size-[18px] border border-twr07-line bg-[#ffff00]"></span>110 yellow</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.75rem] text-twr07-ink2"><span class="flex-none size-[18px] border border-twr07-line bg-[#0000ff]"></span>001 blue</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.75rem] text-twr07-ink2"><span class="flex-none size-[18px] border border-twr07-line bg-[#ff00ff]"></span>101 magenta</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.75rem] text-twr07-ink2"><span class="flex-none size-[18px] border border-twr07-line bg-[#00ffff]"></span>011 cyan</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.75rem] text-twr07-ink2"><span class="flex-none size-[18px] border border-twr07-line bg-[#ffffff]"></span>111 white</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.75rem] text-twr07-ink2"><span class="flex-none size-[18px] border border-twr07-line bg-[#000000]"></span>000 black</li>
      </ul>
      <p class="m-0 min-w-0 text-[0.8rem] leading-relaxed text-pretty text-twr07-ink2">One bit per primary, fully on or fully off. That is the whole palette &mdash; there is no bit left for an intermediate value.</p>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr07-r: #ff0000;
  --color-twr07-g: #00ff00;
  --color-twr07-y: #ffff00;
  --color-twr07-b: #0000ff;
  --color-twr07-m: #ff00ff;
  --color-twr07-c: #00ffff;
  --color-twr07-w: #ffffff;
  --color-twr07-k: #000000;
  --color-twr07-bg: #23252b;
  --color-twr07-bg: oklch(0.26 0.008 275);
  --color-twr07-surface: #32353d;
  --color-twr07-surface: oklch(0.34 0.01 275);
  --color-twr07-ink: #f0f1f5;
  --color-twr07-ink: oklch(0.96 0.004 275);
  --color-twr07-ink2: #b3b7c0;
  --color-twr07-ink2: oklch(0.78 0.01 275);
  --color-twr07-line: #4c505a;
  --color-twr07-line: oklch(0.43 0.012 275);
  --color-twr07-acc: #7fd7ff;
  --color-twr07-acc: oklch(0.84 0.11 225);
  --font-twr07-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, 'Cascadia Mono', Consolas, monospace;
  --animate-twr07-flash: twr-07-flash 2s steps(1, end) infinite;
}

@keyframes twr-07-flash {
  0%,
    74% {
    opacity: 1;
  }

  75%,
    100% {
    opacity: 0.25;
  }
}
/* Substitutes the property it tests, so it cannot be a variant. */

@supports not (font-size: 1cqi) {
  .twr-07__page {
    font-size: clamp(0.5rem, 2.6vw, 1rem);
  }
}

.twr-07:has(#twr-07-theme:checked) {
  --color-twr07-bg: #dcdee4;
  --color-twr07-bg: oklch(0.89 0.007 275);
  --color-twr07-surface: #f3f4f7;
  --color-twr07-surface: oklch(0.96 0.004 275);
  --color-twr07-ink: #16181d;
  --color-twr07-ink: oklch(0.20 0.008 275);
  --color-twr07-ink2: #4a4f59;
  --color-twr07-ink2: oklch(0.43 0.013 275);
  --color-twr07-line: #a8adb8;
  --color-twr07-line: oklch(0.74 0.012 275);
  --color-twr07-acc: #0f5f8a;
  --color-twr07-acc: oklch(0.45 0.11 232);
}
```
