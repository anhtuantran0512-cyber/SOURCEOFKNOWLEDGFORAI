---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-album-shelf-horizontal-accordion/"
title: "Tailwind CSS Album Shelf Horizontal Accordion"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A record-shop listening wall: collapsed panels are cardboard album spines with the artist running down them, and the chosen one grows…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Album Shelf Horizontal Accordion
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-album-shelf-horizontal-accordion/

A record-shop listening wall: collapsed panels are cardboard album spines with the artist running down them, and the chosen one grows (lg:has-checked:grow-[9]) into its full sleeve while the vinyl slides half out and starts turning. The spin is declared on every disc and only [animation-play-state:running] while its radio is checked, so a closed record stops where it was instead of snapping back. Under lg the shelf becomes a vertical crate of 64px spines.
## HTML
```html
<section class="tac-30 w-full min-h-svh grid place-items-center bg-tac30-bg bg-[radial-gradient(60%_50%_at_50%_0%,var(--color-tac30-lamp),transparent_75%)] px-5 py-14 font-tac30-sans text-tac30-cream" aria-label="Album shelf horizontal accordion demo">
  <div class="grid w-full max-w-5xl justify-items-center gap-8">
    <header class="flex w-full flex-wrap items-end justify-between gap-x-8 gap-y-3">
      <div>
        <p class="font-tac30-mono text-[11.5px] tracking-[0.18em] uppercase text-tac30-acc">Side A Records · Staff picks</p>
        <h2 class="mt-2 font-tac30-serif text-[clamp(34px,5vw,52px)] leading-[0.98] font-semibold tracking-[-0.02em]">The listening wall</h2>
      </div>
      <p class="max-w-xs text-[14.5px] leading-[1.6] text-tac30-mut text-pretty">Pull a spine to hear what the shop is playing this week. Every record here is an original pressing, graded VG+ or better.</p>
    </header>
    <div class="relative flex w-full flex-col gap-2 rounded-2xl p-3 shadow-[inset_0_2px_14px_rgb(0_0_0/.6),0_30px_60px_-24px_rgb(0_0_0/.8)] ring-1 ring-white/6 [background:repeating-linear-gradient(90deg,rgb(0_0_0/.08)_0_3px,transparent_3px_11px,rgb(255_255_255/.03)_11px_13px,transparent_13px_29px),linear-gradient(180deg,var(--color-tac30-wood),var(--color-tac30-wood-dk))] after:pointer-events-none after:absolute after:inset-x-0 after:-bottom-2 after:h-3 after:rounded-b-xl after:bg-linear-to-b after:from-tac30-wood-dk after:to-black/60 lg:h-[26rem] lg:flex-row" role="radiogroup" aria-label="Record crate">
      <div class="group relative h-16 shrink-0 overflow-hidden rounded-md transition-[height,flex-grow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] has-checked:h-[34rem] has-focus-visible:ring-2 has-focus-visible:ring-tac30-cream has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac30-wood sm:has-checked:h-[22rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[9] motion-reduce:transition-none" style="--tac30-c:#c9452e;--tac30-s:#4a1913">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-3 px-4 text-[#f3e8d6] shadow-[inset_0_1px_0_rgb(255_255_255/.14),inset_0_-1px_0_rgb(0_0_0/.4)] transition-[opacity,filter] duration-300 [background:repeating-linear-gradient(90deg,rgb(255_255_255/.05)_0_2px,transparent_2px_7px),linear-gradient(90deg,rgb(0_0_0/.28),transparent_22%,transparent_78%,rgb(0_0_0/.32)),var(--tac30-s)] hover:brightness-125 group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-4 motion-reduce:transition-none">
          <input type="radio" name="tac30-crate" id="tac30-a" class="sr-only" checked>
          <span class="font-tac30-mono text-[10.5px] tracking-[0.08em] text-tac30-cream/80">MQ-004</span>
          <span class="flex min-w-0 flex-1 items-baseline gap-2 truncate lg:flex-none lg:[writing-mode:vertical-rl]"><span class="text-[14px] font-bold tracking-[0.06em]">Marlowe Quartet</span><span class="truncate text-[13px] text-tac30-cream/80 italic font-tac30-serif">Night Currents</span></span>
          <span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-full bg-(--tac30-c) ring-2 ring-black/35"><span class="size-1.5 rounded-full bg-black/70"></span></span>
        </label>
        <div class="invisible absolute inset-0 z-10 flex flex-col items-start gap-5 p-5 opacity-0 transition-[opacity,visibility] duration-200 [background:radial-gradient(70%_90%_at_22%_45%,color-mix(in_oklab,var(--tac30-c)_30%,transparent),transparent_72%),var(--color-tac30-well)] group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-200 group-has-checked:duration-500 sm:flex-row sm:items-center sm:gap-6 sm:p-7 lg:right-auto lg:w-[max(100%,40rem)] motion-reduce:transition-none">
          <div class="relative mr-[5.5rem] size-52 flex-none self-center sm:mr-[6.75rem] sm:size-60">
            <div aria-hidden="true" class="absolute inset-[3%] transition-transform duration-700 ease-[cubic-bezier(.3,1.25,.4,1)] group-has-checked:translate-x-[44%] group-has-checked:delay-300 motion-reduce:transition-none">
              <div class="relative size-full animate-tac30-spin rounded-full shadow-[0_12px_30px_rgb(0_0_0/.6)] [animation-play-state:paused] [background:repeating-radial-gradient(circle,#141312_0_1.3px,#211e1b_1.3px_2.7px)] group-has-checked:[animation-play-state:running] motion-reduce:animate-none">
                <span class="absolute inset-[33%] grid place-items-center rounded-full bg-(--tac30-c) ring-2 ring-black/50"><span class="-translate-y-3 font-tac30-mono text-[7px] font-semibold tracking-[0.2em] text-black/70">BLUE FEN</span><span class="absolute inset-0 m-auto size-2 rounded-full bg-tac30-bg"></span></span>
              </div>
              <span class="absolute inset-0 rounded-full bg-[conic-gradient(from_20deg,transparent_0_6%,rgb(255_255_255/.13)_13%,transparent_21%_55%,rgb(255_255_255/.09)_63%,transparent_71%)]"></span>
            </div>
            <div class="absolute inset-0 z-10 overflow-hidden rounded-[3px] shadow-[0_2px_4px_rgb(0_0_0/.4),0_20px_40px_-12px_rgb(0_0_0/.7)] ring-1 ring-white/12">
              <svg class="absolute inset-0 size-full" viewBox="0 0 100 100" aria-hidden="true">
                <rect width="100" height="100" fill="#10233f"/>
                <circle cx="80" cy="30" r="9" fill="#ead9b5"/>
                <circle cx="80" cy="30" r="13" fill="none" stroke="#ead9b5" stroke-width="0.5" opacity="0.4"/>
                <path d="M0 62 Q12.5 54 25 62 T50 62 T75 62 T100 62" fill="none" stroke="#7aa3d6" stroke-width="1.6"/>
                <path d="M0 69 Q12.5 61 25 69 T50 69 T75 69 T100 69" fill="none" stroke="#ead9b5" stroke-width="1.2" opacity="0.8"/>
                <path d="M0 76 Q12.5 68 25 76 T50 76 T75 76 T100 76" fill="none" stroke="#7aa3d6" stroke-width="1.6" opacity="0.7"/>
                <path d="M0 83 Q12.5 75 25 83 T50 83 T75 83 T100 83" fill="none" stroke="#ead9b5" stroke-width="1.2" opacity="0.5"/>
                <path d="M0 90 Q12.5 82 25 90 T50 90 T75 90 T100 90" fill="none" stroke="#7aa3d6" stroke-width="1.6" opacity="0.4"/>
              </svg>
              <span aria-hidden="true" class="absolute top-3 left-3 grid gap-0.5 text-[#f3e8d6]"><span class="font-tac30-mono text-[9px] font-semibold tracking-[0.22em] uppercase">Marlowe Quartet</span><span class="font-tac30-serif text-[17px] leading-none italic sm:text-[20px]">Night Currents</span></span>
              <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(120deg,rgb(255_255_255/.14),transparent_38%)]"></span>
            </div>
          </div>
          <div class="flex w-full min-w-0 flex-1 flex-col">
            <p class="flex items-center gap-2 font-tac30-mono text-[11px] tracking-[0.16em] uppercase text-tac30-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac30-acc shadow-[0_0_10px_var(--color-tac30-acc)]"></span>Now spinning · MQ-004</p>
            <h3 class="mt-2 font-tac30-serif text-[30px] leading-[1.05] font-semibold tracking-[-0.01em] text-tac30-cream">Night Currents</h3>
            <p class="mt-1 text-[13.5px] text-tac30-mut">Marlowe Quartet · 1974 · Blue Fen</p>
            <p class="mt-3 text-[14px] leading-[1.6] text-tac30-quiet text-pretty">Modal jazz cut live to tape in one November evening. Side B is a single nineteen-minute take with no edits.</p>
            <ol class="mt-4 grid gap-1.5 border-t border-white/10 pt-3 font-tac30-mono text-[12px] text-tac30-mut">
              <li class="flex gap-3"><span class="text-tac30-acc">A1</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Low Tide Blues</span><span>6:12</span></li>
              <li class="flex gap-3"><span class="text-tac30-acc">A2</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Night Currents</span><span>8:47</span></li>
              <li class="flex gap-3"><span class="text-tac30-acc">B1</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">The Long Crossing</span><span>19:03</span></li>
            </ol>
          </div>
        </div>
      </div>
      <div class="group relative h-16 shrink-0 overflow-hidden rounded-md transition-[height,flex-grow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] has-checked:h-[34rem] has-focus-visible:ring-2 has-focus-visible:ring-tac30-cream has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac30-wood sm:has-checked:h-[22rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[9] motion-reduce:transition-none" style="--tac30-c:#e3b04b;--tac30-s:#123a3c">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-3 px-4 text-[#f3e8d6] shadow-[inset_0_1px_0_rgb(255_255_255/.14),inset_0_-1px_0_rgb(0_0_0/.4)] transition-[opacity,filter] duration-300 [background:repeating-linear-gradient(90deg,rgb(255_255_255/.05)_0_2px,transparent_2px_7px),linear-gradient(90deg,rgb(0_0_0/.28),transparent_22%,transparent_78%,rgb(0_0_0/.32)),var(--tac30-s)] hover:brightness-125 group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-4 motion-reduce:transition-none">
          <input type="radio" name="tac30-crate" id="tac30-b" class="sr-only">
          <span class="font-tac30-mono text-[10.5px] tracking-[0.08em] text-tac30-cream/80">SR-011</span>
          <span class="flex min-w-0 flex-1 items-baseline gap-2 truncate lg:flex-none lg:[writing-mode:vertical-rl]"><span class="text-[14px] font-bold tracking-[0.06em]">Sofia Reyes Trio</span><span class="truncate text-[13px] text-tac30-cream/80 italic font-tac30-serif">Harbor Lights</span></span>
          <span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-full bg-(--tac30-c) ring-2 ring-black/35"><span class="size-1.5 rounded-full bg-black/70"></span></span>
        </label>
        <div class="invisible absolute inset-0 z-10 flex flex-col items-start gap-5 p-5 opacity-0 transition-[opacity,visibility] duration-200 [background:radial-gradient(70%_90%_at_22%_45%,color-mix(in_oklab,var(--tac30-c)_30%,transparent),transparent_72%),var(--color-tac30-well)] group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-200 group-has-checked:duration-500 sm:flex-row sm:items-center sm:gap-6 sm:p-7 lg:right-auto lg:w-[max(100%,40rem)] motion-reduce:transition-none">
          <div class="relative mr-[5.5rem] size-52 flex-none self-center sm:mr-[6.75rem] sm:size-60">
            <div aria-hidden="true" class="absolute inset-[3%] transition-transform duration-700 ease-[cubic-bezier(.3,1.25,.4,1)] group-has-checked:translate-x-[44%] group-has-checked:delay-300 motion-reduce:transition-none">
              <div class="relative size-full animate-tac30-spin rounded-full shadow-[0_12px_30px_rgb(0_0_0/.6)] [animation-play-state:paused] [background:repeating-radial-gradient(circle,#141312_0_1.3px,#211e1b_1.3px_2.7px)] group-has-checked:[animation-play-state:running] motion-reduce:animate-none">
                <span class="absolute inset-[33%] grid place-items-center rounded-full bg-(--tac30-c) ring-2 ring-black/50"><span class="-translate-y-3 font-tac30-mono text-[7px] font-semibold tracking-[0.2em] text-black/70">PELICAN</span><span class="absolute inset-0 m-auto size-2 rounded-full bg-tac30-bg"></span></span>
              </div>
              <span class="absolute inset-0 rounded-full bg-[conic-gradient(from_20deg,transparent_0_6%,rgb(255_255_255/.13)_13%,transparent_21%_55%,rgb(255_255_255/.09)_63%,transparent_71%)]"></span>
            </div>
            <div class="absolute inset-0 z-10 overflow-hidden rounded-[3px] shadow-[0_2px_4px_rgb(0_0_0/.4),0_20px_40px_-12px_rgb(0_0_0/.7)] ring-1 ring-white/12">
              <svg class="absolute inset-0 size-full" viewBox="0 0 100 100" aria-hidden="true">
                <rect width="100" height="100" fill="#0f4a4c"/>
                <polygon points="52,40 100,18 100,52" fill="#f4d27a" opacity="0.38"/>
                <polygon points="48,40 0,30 0,48" fill="#f4d27a" opacity="0.18"/>
                <rect x="45" y="44" width="10" height="36" fill="#efe7d8"/>
                <rect x="45" y="52" width="10" height="5" fill="#c9452e"/>
                <rect x="45" y="64" width="10" height="5" fill="#c9452e"/>
                <rect x="46" y="36" width="8" height="8" fill="#f4d27a"/>
                <rect x="43" y="33" width="14" height="3" fill="#0a2f31"/>
                <rect x="0" y="80" width="100" height="20" fill="#0a3436"/>
                <path d="M8 86H30M58 88H88M20 94H50" stroke="#5f9c97" stroke-width="1.2" stroke-linecap="round"/>
              </svg>
              <span aria-hidden="true" class="absolute top-3 left-3 grid gap-0.5 text-[#f3e8d6]"><span class="font-tac30-mono text-[9px] font-semibold tracking-[0.22em] uppercase">Sofia Reyes Trio</span><span class="font-tac30-serif text-[17px] leading-none italic sm:text-[20px]">Harbor Lights</span></span>
              <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(120deg,rgb(255_255_255/.14),transparent_38%)]"></span>
            </div>
          </div>
          <div class="flex w-full min-w-0 flex-1 flex-col">
            <p class="flex items-center gap-2 font-tac30-mono text-[11px] tracking-[0.16em] uppercase text-tac30-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac30-acc shadow-[0_0_10px_var(--color-tac30-acc)]"></span>Now spinning · SR-011</p>
            <h3 class="mt-2 font-tac30-serif text-[30px] leading-[1.05] font-semibold tracking-[-0.01em] text-tac30-cream">Harbor Lights</h3>
            <p class="mt-1 text-[13.5px] text-tac30-mut">Sofia Reyes Trio · 1981 · Pelican</p>
            <p class="mt-3 text-[14px] leading-[1.6] text-tac30-quiet text-pretty">Bossa-inflected standards recorded in a converted lighthouse. The foghorn on track three was not planned, and stayed.</p>
            <ol class="mt-4 grid gap-1.5 border-t border-white/10 pt-3 font-tac30-mono text-[12px] text-tac30-mut">
              <li class="flex gap-3"><span class="text-tac30-acc">A1</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Harbor Lights</span><span>4:38</span></li>
              <li class="flex gap-3"><span class="text-tac30-acc">A2</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Fog Signal</span><span>5:21</span></li>
              <li class="flex gap-3"><span class="text-tac30-acc">B1</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Lantern Room</span><span>7:02</span></li>
            </ol>
          </div>
        </div>
      </div>
      <div class="group relative h-16 shrink-0 overflow-hidden rounded-md transition-[height,flex-grow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] has-checked:h-[34rem] has-focus-visible:ring-2 has-focus-visible:ring-tac30-cream has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac30-wood sm:has-checked:h-[22rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[9] motion-reduce:transition-none" style="--tac30-c:#2c6e49;--tac30-s:#233b26">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-3 px-4 text-[#f3e8d6] shadow-[inset_0_1px_0_rgb(255_255_255/.14),inset_0_-1px_0_rgb(0_0_0/.4)] transition-[opacity,filter] duration-300 [background:repeating-linear-gradient(90deg,rgb(255_255_255/.05)_0_2px,transparent_2px_7px),linear-gradient(90deg,rgb(0_0_0/.28),transparent_22%,transparent_78%,rgb(0_0_0/.32)),var(--tac30-s)] hover:brightness-125 group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-4 motion-reduce:transition-none">
          <input type="radio" name="tac30-crate" id="tac30-c" class="sr-only">
          <span class="font-tac30-mono text-[10.5px] tracking-[0.08em] text-tac30-cream/80">ME-023</span>
          <span class="flex min-w-0 flex-1 items-baseline gap-2 truncate lg:flex-none lg:[writing-mode:vertical-rl]"><span class="text-[14px] font-bold tracking-[0.06em]">The Meridian Six</span><span class="truncate text-[13px] text-tac30-cream/80 italic font-tac30-serif">Slow Orbit</span></span>
          <span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-full bg-(--tac30-c) ring-2 ring-black/35"><span class="size-1.5 rounded-full bg-black/70"></span></span>
        </label>
        <div class="invisible absolute inset-0 z-10 flex flex-col items-start gap-5 p-5 opacity-0 transition-[opacity,visibility] duration-200 [background:radial-gradient(70%_90%_at_22%_45%,color-mix(in_oklab,var(--tac30-c)_30%,transparent),transparent_72%),var(--color-tac30-well)] group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-200 group-has-checked:duration-500 sm:flex-row sm:items-center sm:gap-6 sm:p-7 lg:right-auto lg:w-[max(100%,40rem)] motion-reduce:transition-none">
          <div class="relative mr-[5.5rem] size-52 flex-none self-center sm:mr-[6.75rem] sm:size-60">
            <div aria-hidden="true" class="absolute inset-[3%] transition-transform duration-700 ease-[cubic-bezier(.3,1.25,.4,1)] group-has-checked:translate-x-[44%] group-has-checked:delay-300 motion-reduce:transition-none">
              <div class="relative size-full animate-tac30-spin rounded-full shadow-[0_12px_30px_rgb(0_0_0/.6)] [animation-play-state:paused] [background:repeating-radial-gradient(circle,#141312_0_1.3px,#211e1b_1.3px_2.7px)] group-has-checked:[animation-play-state:running] motion-reduce:animate-none">
                <span class="absolute inset-[33%] grid place-items-center rounded-full bg-(--tac30-c) ring-2 ring-black/50"><span class="-translate-y-3 font-tac30-mono text-[7px] font-semibold tracking-[0.2em] text-black/70">HALCYON</span><span class="absolute inset-0 m-auto size-2 rounded-full bg-tac30-bg"></span></span>
              </div>
              <span class="absolute inset-0 rounded-full bg-[conic-gradient(from_20deg,transparent_0_6%,rgb(255_255_255/.13)_13%,transparent_21%_55%,rgb(255_255_255/.09)_63%,transparent_71%)]"></span>
            </div>
            <div class="absolute inset-0 z-10 overflow-hidden rounded-[3px] shadow-[0_2px_4px_rgb(0_0_0/.4),0_20px_40px_-12px_rgb(0_0_0/.7)] ring-1 ring-white/12">
              <svg class="absolute inset-0 size-full" viewBox="0 0 100 100" aria-hidden="true">
                <rect width="100" height="100" fill="#ece0c9"/>
                <circle cx="50" cy="40" r="8" fill="#1d1a17"/>
                <circle cx="50" cy="40" r="15" fill="none" stroke="#1d1a17" stroke-width="0.7"/>
                <circle cx="50" cy="40" r="22" fill="none" stroke="#1d1a17" stroke-width="0.7"/>
                <circle cx="50" cy="40" r="29" fill="none" stroke="#1d1a17" stroke-width="0.7"/>
                <circle cx="70.5" cy="19.5" r="4.5" fill="#c9452e"/>
                <circle cx="35" cy="34" r="2.2" fill="#2c6e49"/>
                <circle cx="64" cy="58" r="1.8" fill="#1d1a17"/>
                <rect x="10" y="76" width="80" height="0.8" fill="#1d1a17"/>
              </svg>
              <span aria-hidden="true" class="absolute bottom-3 left-3 grid gap-0.5 text-[#1d1a17]"><span class="font-tac30-mono text-[9px] font-semibold tracking-[0.22em] uppercase">The Meridian Six</span><span class="font-tac30-serif text-[17px] leading-none italic sm:text-[20px]">Slow Orbit</span></span>
              <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(120deg,rgb(255_255_255/.14),transparent_38%)]"></span>
            </div>
          </div>
          <div class="flex w-full min-w-0 flex-1 flex-col">
            <p class="flex items-center gap-2 font-tac30-mono text-[11px] tracking-[0.16em] uppercase text-tac30-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac30-acc shadow-[0_0_10px_var(--color-tac30-acc)]"></span>Now spinning · ME-023</p>
            <h3 class="mt-2 font-tac30-serif text-[30px] leading-[1.05] font-semibold tracking-[-0.01em] text-tac30-cream">Slow Orbit</h3>
            <p class="mt-1 text-[13.5px] text-tac30-mut">The Meridian Six · 1977 · Halcyon</p>
            <p class="mt-3 text-[14px] leading-[1.6] text-tac30-quiet text-pretty">Six horns and no rhythm section. Somehow it swings anyway — the arranger never explained how, and nobody asked twice.</p>
            <ol class="mt-4 grid gap-1.5 border-t border-white/10 pt-3 font-tac30-mono text-[12px] text-tac30-mut">
              <li class="flex gap-3"><span class="text-tac30-acc">A1</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Perihelion</span><span>5:44</span></li>
              <li class="flex gap-3"><span class="text-tac30-acc">A2</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Slow Orbit</span><span>9:10</span></li>
              <li class="flex gap-3"><span class="text-tac30-acc">B1</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Six Bodies</span><span>6:29</span></li>
            </ol>
          </div>
        </div>
      </div>
      <div class="group relative h-16 shrink-0 overflow-hidden rounded-md transition-[height,flex-grow] duration-700 ease-[cubic-bezier(.4,0,.2,1)] has-checked:h-[34rem] has-focus-visible:ring-2 has-focus-visible:ring-tac30-cream has-focus-visible:ring-offset-2 has-focus-visible:ring-offset-tac30-wood sm:has-checked:h-[22rem] lg:h-auto lg:min-w-0 lg:flex-1 lg:has-checked:h-auto lg:has-checked:grow-[9] motion-reduce:transition-none" style="--tac30-c:#e0782f;--tac30-s:#5a3510">
        <label class="absolute inset-0 flex cursor-pointer items-center gap-3 px-4 text-[#f3e8d6] shadow-[inset_0_1px_0_rgb(255_255_255/.14),inset_0_-1px_0_rgb(0_0_0/.4)] transition-[opacity,filter] duration-300 [background:repeating-linear-gradient(90deg,rgb(255_255_255/.05)_0_2px,transparent_2px_7px),linear-gradient(90deg,rgb(0_0_0/.28),transparent_22%,transparent_78%,rgb(0_0_0/.32)),var(--tac30-s)] hover:brightness-125 group-has-checked:opacity-0 lg:flex-col lg:justify-between lg:px-0 lg:py-4 motion-reduce:transition-none">
          <input type="radio" name="tac30-crate" id="tac30-d" class="sr-only">
          <span class="font-tac30-mono text-[10.5px] tracking-[0.08em] text-tac30-cream/80">AO-031</span>
          <span class="flex min-w-0 flex-1 items-baseline gap-2 truncate lg:flex-none lg:[writing-mode:vertical-rl]"><span class="text-[14px] font-bold tracking-[0.06em]">Ada Okafor</span><span class="truncate text-[13px] text-tac30-cream/80 italic font-tac30-serif">Ember Hours</span></span>
          <span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-full bg-(--tac30-c) ring-2 ring-black/35"><span class="size-1.5 rounded-full bg-black/70"></span></span>
        </label>
        <div class="invisible absolute inset-0 z-10 flex flex-col items-start gap-5 p-5 opacity-0 transition-[opacity,visibility] duration-200 [background:radial-gradient(70%_90%_at_22%_45%,color-mix(in_oklab,var(--tac30-c)_30%,transparent),transparent_72%),var(--color-tac30-well)] group-has-checked:visible group-has-checked:opacity-100 group-has-checked:delay-200 group-has-checked:duration-500 sm:flex-row sm:items-center sm:gap-6 sm:p-7 lg:right-auto lg:w-[max(100%,40rem)] motion-reduce:transition-none">
          <div class="relative mr-[5.5rem] size-52 flex-none self-center sm:mr-[6.75rem] sm:size-60">
            <div aria-hidden="true" class="absolute inset-[3%] transition-transform duration-700 ease-[cubic-bezier(.3,1.25,.4,1)] group-has-checked:translate-x-[44%] group-has-checked:delay-300 motion-reduce:transition-none">
              <div class="relative size-full animate-tac30-spin rounded-full shadow-[0_12px_30px_rgb(0_0_0/.6)] [animation-play-state:paused] [background:repeating-radial-gradient(circle,#141312_0_1.3px,#211e1b_1.3px_2.7px)] group-has-checked:[animation-play-state:running] motion-reduce:animate-none">
                <span class="absolute inset-[33%] grid place-items-center rounded-full bg-(--tac30-c) ring-2 ring-black/50"><span class="-translate-y-3 font-tac30-mono text-[7px] font-semibold tracking-[0.2em] text-black/70">KILN STREET</span><span class="absolute inset-0 m-auto size-2 rounded-full bg-tac30-bg"></span></span>
              </div>
              <span class="absolute inset-0 rounded-full bg-[conic-gradient(from_20deg,transparent_0_6%,rgb(255_255_255/.13)_13%,transparent_21%_55%,rgb(255_255_255/.09)_63%,transparent_71%)]"></span>
            </div>
            <div class="absolute inset-0 z-10 overflow-hidden rounded-[3px] shadow-[0_2px_4px_rgb(0_0_0/.4),0_20px_40px_-12px_rgb(0_0_0/.7)] ring-1 ring-white/12">
              <svg class="absolute inset-0 size-full" viewBox="0 0 100 100" aria-hidden="true">
                <rect width="100" height="100" fill="#f1a246"/>
                <rect x="0" y="0" width="100" height="44" fill="#d9622b"/>
                <rect x="0" y="44" width="100" height="10" fill="#e8823a"/>
                <circle cx="50" cy="78" r="26" fill="#fbe2b0"/>
                <rect x="0" y="66" width="100" height="3" fill="#d9622b"/>
                <rect x="0" y="74" width="100" height="4" fill="#d9622b"/>
                <rect x="0" y="83" width="100" height="5" fill="#b8431f"/>
                <rect x="0" y="92" width="100" height="8" fill="#8f3216"/>
              </svg>
              <span aria-hidden="true" class="absolute top-3 left-3 grid gap-0.5 text-[#fff4e4]"><span class="font-tac30-mono text-[9px] font-semibold tracking-[0.22em] uppercase">Ada Okafor</span><span class="font-tac30-serif text-[17px] leading-none italic sm:text-[20px]">Ember Hours</span></span>
              <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(120deg,rgb(255_255_255/.14),transparent_38%)]"></span>
            </div>
          </div>
          <div class="flex w-full min-w-0 flex-1 flex-col">
            <p class="flex items-center gap-2 font-tac30-mono text-[11px] tracking-[0.16em] uppercase text-tac30-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac30-acc shadow-[0_0_10px_var(--color-tac30-acc)]"></span>Now spinning · AO-031</p>
            <h3 class="mt-2 font-tac30-serif text-[30px] leading-[1.05] font-semibold tracking-[-0.01em] text-tac30-cream">Ember Hours</h3>
            <p class="mt-1 text-[13.5px] text-tac30-mut">Ada Okafor · 1979 · Kiln Street</p>
            <p class="mt-3 text-[14px] leading-[1.6] text-tac30-quiet text-pretty">Lagos highlife meets a Chicago horn section over two hot weeks in August. The title track runs long because nobody wanted to stop.</p>
            <ol class="mt-4 grid gap-1.5 border-t border-white/10 pt-3 font-tac30-mono text-[12px] text-tac30-mut">
              <li class="flex gap-3"><span class="text-tac30-acc">A1</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Ember Hours</span><span>11:26</span></li>
              <li class="flex gap-3"><span class="text-tac30-acc">A2</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Marina Walk</span><span>4:55</span></li>
              <li class="flex gap-3"><span class="text-tac30-acc">B1</span><span class="min-w-0 flex-1 truncate text-tac30-quiet">Harmattan</span><span>7:38</span></li>
            </ol>
          </div>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="mt-2 rounded-full border border-white/10 px-3.5 py-2 font-tac30-mono text-[11.5px] text-tac30-mut">has-checked:grow-[9] · [animation-play-state:running] · translate-x-[44%]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac30-bg: #130f0c;
  --color-tac30-bg: oklch(0.17 0.012 55);
  --color-tac30-lamp: #3d2a1a;
  --color-tac30-lamp: oklch(0.3 0.045 60);
  --color-tac30-wood: #5b3e28;
  --color-tac30-wood: oklch(0.39 0.06 55);
  --color-tac30-wood-dk: #3e2a1b;
  --color-tac30-wood-dk: oklch(0.31 0.045 55);
  --color-tac30-well: #1d1712;
  --color-tac30-well: oklch(0.2 0.014 60);
  --color-tac30-cream: #f3e8d6;
  --color-tac30-cream: oklch(0.94 0.025 80);
  --color-tac30-quiet: #dccfbd;
  --color-tac30-quiet: oklch(0.86 0.025 75);
  --color-tac30-mut: #bfae97;
  --color-tac30-mut: oklch(0.75 0.03 75);
  --color-tac30-acc: #eaa558;
  --color-tac30-acc: oklch(0.77 0.12 65);
  --font-tac30-serif: 'Fraunces', Georgia, serif;
  --font-tac30-sans: 'Manrope', system-ui, sans-serif;
  --font-tac30-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --animate-tac30-spin: tac30-spin 1.8s linear infinite;

  @keyframes tac30-spin {
    to {
      rotate: 360deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-30 {
  width: 100%;
  min-height: 100svh;
}
```
