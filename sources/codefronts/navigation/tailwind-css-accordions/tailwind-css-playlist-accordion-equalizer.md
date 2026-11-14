---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-playlist-accordion-equalizer/"
title: "Tailwind CSS Playlist Accordion with Equalizer Animation"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A music-app playlist where the open track is the one \"playing\": its index number swaps for a four-bar equalizer bouncing on staggered, non-repeating loops,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Playlist Accordion with Equalizer Animation
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-playlist-accordion-equalizer/

A music-app playlist where the open track is the one "playing": its index number swaps for a four-bar equalizer bouncing on staggered, non-repeating loops, the title lights up in a magenta→orange gradient and the row slides open to liner notes, a progress scrubber and track metadata. Exclusive <details name>, a two-way height animation through the details-content: variant, and keyframes declared as an --animate-* token.
## HTML
```html
<section class="tac-21 w-full min-h-svh grid place-items-center bg-tac21-bg bg-[radial-gradient(60%_45%_at_15%_0%,var(--color-tac21-glow1),transparent_70%),radial-gradient(55%_45%_at_95%_100%,var(--color-tac21-glow2),transparent_70%)] px-4 py-14 font-tac21-sans text-tac21-ink [interpolate-size:allow-keywords]" aria-label="Playlist accordion with equalizer animation demo">
  <div class="grid w-full justify-items-center gap-7">
    <article class="w-full max-w-xl overflow-hidden rounded-[28px] bg-tac21-card shadow-[0_1px_0_oklch(1_0_0/0.06)_inset,0_30px_80px_-24px_oklch(0_0_0/0.8)] ring-1 ring-white/10">
      <header class="relative flex items-center gap-5 p-5 sm:p-6">
        <div aria-hidden="true" class="pointer-events-none absolute inset-0 bg-[radial-gradient(80%_120%_at_0%_0%,var(--color-tac21-glow1),transparent_60%)] opacity-70"></div>
        <svg class="relative size-20 flex-none rounded-2xl shadow-[0_12px_30px_-8px_oklch(0.55_0.25_350/0.6)] ring-1 ring-white/15 sm:size-28" viewBox="0 0 112 112" aria-hidden="true">
          <rect width="112" height="112" fill="#1a0b2b"/>
          <rect width="112" height="70" fill="#3b0f4f"/>
          <rect y="22" width="112" height="48" fill="#7a1a5c" opacity="0.7"/>
          <rect y="44" width="112" height="26" fill="#d9466b" opacity="0.55"/>
          <circle cx="56" cy="64" r="24" fill="#ff8a3d"/>
          <rect y="50" width="112" height="3" fill="#3b0f4f"/>
          <rect y="57" width="112" height="3.5" fill="#3b0f4f"/>
          <rect y="64" width="112" height="4" fill="#3b0f4f"/>
          <rect y="70" width="112" height="42" fill="#12081f"/>
          <path d="M56 70 L4 112 H108 Z" fill="#241038"/>
          <path d="M56 70 L54 112 H58 Z" fill="#ff8a3d" opacity="0.8"/>
          <path d="M0 70 L22 56 L38 70 Z" fill="#12081f"/>
          <path d="M74 70 L94 52 L112 66 V70 Z" fill="#12081f"/>
          <path d="M8 112 L56 70" stroke="#e0458f" stroke-width="1" opacity="0.6"/>
          <path d="M104 112 L56 70" stroke="#e0458f" stroke-width="1" opacity="0.6"/>
        </svg>
        <div class="relative min-w-0">
          <p class="text-[11px] font-semibold tracking-[0.18em] uppercase text-tac21-amb">Playlist</p>
          <h2 class="mt-1 text-2xl font-bold tracking-[-0.02em] text-balance sm:text-[28px]">Night Drive Sessions</h2>
          <p class="mt-1.5 text-sm text-tac21-mut">Curated by Halcyon Radio · <span class="whitespace-nowrap">5 tracks · 19 min</span></p>
        </div>
      </header>

      <div class="flex items-center justify-between border-y border-white/8 px-5 py-2.5 font-tac21-mono text-[11px] tracking-[0.08em] uppercase text-tac21-mut sm:px-6">
        <span># &nbsp;Title</span>
        <svg class="size-4" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M8 4.6V8l2.2 1.4" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
      </div>

      <div class="p-2 sm:p-3">
        <details name="tac21-track" class="group rounded-2xl transition-colors duration-300 open:bg-white/[0.045] open:ring-1 open:ring-white/8 details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="grid min-h-14 cursor-pointer list-none grid-cols-[2.25rem_minmax(0,1fr)_auto_1.25rem] items-center gap-3 rounded-2xl px-3 py-2.5 transition-colors hover:bg-white/[0.04] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac21-mag [&::-webkit-details-marker]:hidden">
            <span class="grid h-6 place-items-center font-tac21-mono text-sm text-tac21-mut">
              <span class="group-open:hidden">01</span>
              <span aria-hidden="true" class="hidden h-[18px] items-end gap-[3px] group-open:flex">
                <span class="h-full w-[3px] origin-bottom scale-y-[.45] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.1s] [animation-duration:.62s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.9] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.3s] [animation-duration:.44s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.65] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.5s] [animation-duration:.78s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.35] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.2s] [animation-duration:.53s] motion-reduce:animate-none"></span>
              </span>
            </span>
            <span class="min-w-0">
              <span class="block truncate text-[15.5px] font-semibold"><span class="group-open:bg-linear-to-r group-open:from-tac21-mag group-open:to-tac21-amb group-open:bg-clip-text group-open:text-transparent">Neon Overpass</span></span>
              <span class="block truncate text-[13px] text-tac21-mut">Mira Solene</span>
            </span>
            <span class="font-tac21-mono text-[13px] text-tac21-mut tabular-nums">3:52</span>
            <svg class="size-4 text-tac21-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac21-amb motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-3 pb-4 sm:ps-[3.75rem]">
            <p class="text-[14px] leading-relaxed text-tac21-soft">Recorded in one take at 2 a.m. on a borrowed Juno-60 — the arpeggio was supposed to be a scratch track, and nobody could bring themselves to replace it.</p>
            <div class="mt-4 flex items-center gap-3 font-tac21-mono text-[11.5px] text-tac21-mut tabular-nums">
              <span>1:24</span>
              <span class="relative h-1 flex-1 overflow-hidden rounded-full bg-white/10"><span class="absolute inset-y-0 left-0 w-full origin-left scale-x-0 rounded-full bg-linear-to-r from-tac21-mag to-tac21-amb transition-transform delay-200 duration-700 ease-out group-open:scale-x-[.36] motion-reduce:transition-none"></span></span>
              <span>3:52</span>
            </div>
            <ul class="mt-3.5 flex flex-wrap gap-2 font-tac21-mono text-[11px] text-tac21-soft">
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">104 BPM</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">A minor</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">Synthwave</li>
            </ul>
          </div>
        </details>

        <details name="tac21-track" class="group rounded-2xl transition-colors duration-300 open:bg-white/[0.045] open:ring-1 open:ring-white/8 details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none" open>
          <summary class="grid min-h-14 cursor-pointer list-none grid-cols-[2.25rem_minmax(0,1fr)_auto_1.25rem] items-center gap-3 rounded-2xl px-3 py-2.5 transition-colors hover:bg-white/[0.04] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac21-mag [&::-webkit-details-marker]:hidden">
            <span class="grid h-6 place-items-center font-tac21-mono text-sm text-tac21-mut">
              <span class="group-open:hidden">02</span>
              <span aria-hidden="true" class="hidden h-[18px] items-end gap-[3px] group-open:flex">
                <span class="h-full w-[3px] origin-bottom scale-y-[.45] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.1s] [animation-duration:.62s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.9] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.3s] [animation-duration:.44s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.65] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.5s] [animation-duration:.78s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.35] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.2s] [animation-duration:.53s] motion-reduce:animate-none"></span>
              </span>
            </span>
            <span class="min-w-0">
              <span class="block truncate text-[15.5px] font-semibold"><span class="group-open:bg-linear-to-r group-open:from-tac21-mag group-open:to-tac21-amb group-open:bg-clip-text group-open:text-transparent">Sodium Lights</span></span>
              <span class="block truncate text-[13px] text-tac21-mut">The Hollow Coast</span>
            </span>
            <span class="font-tac21-mono text-[13px] text-tac21-mut tabular-nums">4:17</span>
            <svg class="size-4 text-tac21-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac21-amb motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-3 pb-4 sm:ps-[3.75rem]">
            <p class="text-[14px] leading-relaxed text-tac21-soft">A slow-burn duet built around a field recording of highway hum outside Barstow. The bassline enters at 1:40 and never leaves — turn it up for the second chorus.</p>
            <div class="mt-4 flex items-center gap-3 font-tac21-mono text-[11.5px] text-tac21-mut tabular-nums">
              <span>2:09</span>
              <span class="relative h-1 flex-1 overflow-hidden rounded-full bg-white/10"><span class="absolute inset-y-0 left-0 w-full origin-left scale-x-0 rounded-full bg-linear-to-r from-tac21-mag to-tac21-amb transition-transform delay-200 duration-700 ease-out group-open:scale-x-[.5] motion-reduce:transition-none"></span></span>
              <span>4:17</span>
            </div>
            <ul class="mt-3.5 flex flex-wrap gap-2 font-tac21-mono text-[11px] text-tac21-soft">
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">88 BPM</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">F♯ minor</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">Dream pop</li>
            </ul>
          </div>
        </details>

        <details name="tac21-track" class="group rounded-2xl transition-colors duration-300 open:bg-white/[0.045] open:ring-1 open:ring-white/8 details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="grid min-h-14 cursor-pointer list-none grid-cols-[2.25rem_minmax(0,1fr)_auto_1.25rem] items-center gap-3 rounded-2xl px-3 py-2.5 transition-colors hover:bg-white/[0.04] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac21-mag [&::-webkit-details-marker]:hidden">
            <span class="grid h-6 place-items-center font-tac21-mono text-sm text-tac21-mut">
              <span class="group-open:hidden">03</span>
              <span aria-hidden="true" class="hidden h-[18px] items-end gap-[3px] group-open:flex">
                <span class="h-full w-[3px] origin-bottom scale-y-[.45] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.1s] [animation-duration:.62s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.9] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.3s] [animation-duration:.44s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.65] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.5s] [animation-duration:.78s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.35] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.2s] [animation-duration:.53s] motion-reduce:animate-none"></span>
              </span>
            </span>
            <span class="min-w-0">
              <span class="block truncate text-[15.5px] font-semibold"><span class="group-open:bg-linear-to-r group-open:from-tac21-mag group-open:to-tac21-amb group-open:bg-clip-text group-open:text-transparent">Afterglow Protocol</span></span>
              <span class="block truncate text-[13px] text-tac21-mut">Kaito Rhee &amp; Vela</span>
            </span>
            <span class="font-tac21-mono text-[13px] text-tac21-mut tabular-nums">3:08</span>
            <svg class="size-4 text-tac21-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac21-amb motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-3 pb-4 sm:ps-[3.75rem]">
            <p class="text-[14px] leading-relaxed text-tac21-soft">Vela's vocal was tracked through a broken cassette deck, then rebuilt from the tape hiss up. The drop at 2:20 is the reason this playlist exists.</p>
            <div class="mt-4 flex items-center gap-3 font-tac21-mono text-[11.5px] text-tac21-mut tabular-nums">
              <span>0:47</span>
              <span class="relative h-1 flex-1 overflow-hidden rounded-full bg-white/10"><span class="absolute inset-y-0 left-0 w-full origin-left scale-x-0 rounded-full bg-linear-to-r from-tac21-mag to-tac21-amb transition-transform delay-200 duration-700 ease-out group-open:scale-x-[.25] motion-reduce:transition-none"></span></span>
              <span>3:08</span>
            </div>
            <ul class="mt-3.5 flex flex-wrap gap-2 font-tac21-mono text-[11px] text-tac21-soft">
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">122 BPM</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">D major</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">Electronic</li>
            </ul>
          </div>
        </details>

        <details name="tac21-track" class="group rounded-2xl transition-colors duration-300 open:bg-white/[0.045] open:ring-1 open:ring-white/8 details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="grid min-h-14 cursor-pointer list-none grid-cols-[2.25rem_minmax(0,1fr)_auto_1.25rem] items-center gap-3 rounded-2xl px-3 py-2.5 transition-colors hover:bg-white/[0.04] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac21-mag [&::-webkit-details-marker]:hidden">
            <span class="grid h-6 place-items-center font-tac21-mono text-sm text-tac21-mut">
              <span class="group-open:hidden">04</span>
              <span aria-hidden="true" class="hidden h-[18px] items-end gap-[3px] group-open:flex">
                <span class="h-full w-[3px] origin-bottom scale-y-[.45] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.1s] [animation-duration:.62s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.9] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.3s] [animation-duration:.44s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.65] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.5s] [animation-duration:.78s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.35] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.2s] [animation-duration:.53s] motion-reduce:animate-none"></span>
              </span>
            </span>
            <span class="min-w-0">
              <span class="block truncate text-[15.5px] font-semibold"><span class="group-open:bg-linear-to-r group-open:from-tac21-mag group-open:to-tac21-amb group-open:bg-clip-text group-open:text-transparent">Static on Channel 9</span></span>
              <span class="block truncate text-[13px] text-tac21-mut">Low Orbit Club</span>
            </span>
            <span class="font-tac21-mono text-[13px] text-tac21-mut tabular-nums">4:41</span>
            <svg class="size-4 text-tac21-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac21-amb motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-3 pb-4 sm:ps-[3.75rem]">
            <p class="text-[14px] leading-relaxed text-tac21-soft">An instrumental that samples a 1987 late-night TV sign-off. Halfway through, the drums cut out and the strings carry it home on their own.</p>
            <div class="mt-4 flex items-center gap-3 font-tac21-mono text-[11.5px] text-tac21-mut tabular-nums">
              <span>3:02</span>
              <span class="relative h-1 flex-1 overflow-hidden rounded-full bg-white/10"><span class="absolute inset-y-0 left-0 w-full origin-left scale-x-0 rounded-full bg-linear-to-r from-tac21-mag to-tac21-amb transition-transform delay-200 duration-700 ease-out group-open:scale-x-[.65] motion-reduce:transition-none"></span></span>
              <span>4:41</span>
            </div>
            <ul class="mt-3.5 flex flex-wrap gap-2 font-tac21-mono text-[11px] text-tac21-soft">
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">96 BPM</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">C minor</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">Instrumental</li>
            </ul>
          </div>
        </details>

        <details name="tac21-track" class="group rounded-2xl transition-colors duration-300 open:bg-white/[0.045] open:ring-1 open:ring-white/8 details-content:h-0 details-content:overflow-hidden details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:details-content:transition-none">
          <summary class="grid min-h-14 cursor-pointer list-none grid-cols-[2.25rem_minmax(0,1fr)_auto_1.25rem] items-center gap-3 rounded-2xl px-3 py-2.5 transition-colors hover:bg-white/[0.04] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac21-mag [&::-webkit-details-marker]:hidden">
            <span class="grid h-6 place-items-center font-tac21-mono text-sm text-tac21-mut">
              <span class="group-open:hidden">05</span>
              <span aria-hidden="true" class="hidden h-[18px] items-end gap-[3px] group-open:flex">
                <span class="h-full w-[3px] origin-bottom scale-y-[.45] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.1s] [animation-duration:.62s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.9] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.3s] [animation-duration:.44s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.65] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.5s] [animation-duration:.78s] motion-reduce:animate-none"></span>
                <span class="h-full w-[3px] origin-bottom scale-y-[.35] rounded-full bg-linear-to-t from-tac21-mag to-tac21-amb group-open:animate-tac21-eq [animation-delay:-.2s] [animation-duration:.53s] motion-reduce:animate-none"></span>
              </span>
            </span>
            <span class="min-w-0">
              <span class="block truncate text-[15.5px] font-semibold"><span class="group-open:bg-linear-to-r group-open:from-tac21-mag group-open:to-tac21-amb group-open:bg-clip-text group-open:text-transparent">Coastline, 4 A.M.</span></span>
              <span class="block truncate text-[13px] text-tac21-mut">Juniper Vale</span>
            </span>
            <span class="font-tac21-mono text-[13px] text-tac21-mut tabular-nums">3:29</span>
            <svg class="size-4 text-tac21-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac21-amb motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="px-3 pb-4 sm:ps-[3.75rem]">
            <p class="text-[14px] leading-relaxed text-tac21-soft">The closer: a piano sketch over tide sounds, mixed quiet on purpose so the playlist fades out instead of stopping.</p>
            <div class="mt-4 flex items-center gap-3 font-tac21-mono text-[11.5px] text-tac21-mut tabular-nums">
              <span>0:31</span>
              <span class="relative h-1 flex-1 overflow-hidden rounded-full bg-white/10"><span class="absolute inset-y-0 left-0 w-full origin-left scale-x-0 rounded-full bg-linear-to-r from-tac21-mag to-tac21-amb transition-transform delay-200 duration-700 ease-out group-open:scale-x-[.15] motion-reduce:transition-none"></span></span>
              <span>3:29</span>
            </div>
            <ul class="mt-3.5 flex flex-wrap gap-2 font-tac21-mono text-[11px] text-tac21-soft">
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">72 BPM</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">E♭ major</li>
              <li class="rounded-full bg-white/[0.06] px-2.5 py-1 ring-1 ring-white/10">Ambient</li>
            </ul>
          </div>
        </details>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tac21-mono text-[11.5px] text-tac21-mut ring-1 ring-white/10">group-open:animate-tac21-eq · origin-bottom · details-content:h-0</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac21-bg: #0b0810;
  --color-tac21-bg: oklch(0.14 0.015 310);
  --color-tac21-glow1: #5a1647a6;
  --color-tac21-glow1: oklch(0.33 0.11 345 / 0.65);
  --color-tac21-glow2: #5a2a0d80;
  --color-tac21-glow2: oklch(0.35 0.09 55 / 0.5);
  --color-tac21-card: #17121d;
  --color-tac21-card: oklch(0.19 0.018 310);
  --color-tac21-ink: #f6f2f7;
  --color-tac21-ink: oklch(0.97 0.006 320);
  --color-tac21-soft: #d3cad6;
  --color-tac21-soft: oklch(0.86 0.016 320);
  --color-tac21-mut: #a89eac;
  --color-tac21-mut: oklch(0.73 0.018 320);
  --color-tac21-mag: #f2459c;
  --color-tac21-mag: oklch(0.67 0.22 355);
  --color-tac21-amb: #ff9a4a;
  --color-tac21-amb: oklch(0.78 0.15 55);
  --font-tac21-sans: 'Outfit', system-ui, sans-serif;
  --font-tac21-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tac21-eq: tac21-eq 0.7s ease-in-out infinite;

  @keyframes tac21-eq {
    0%,
        100% {
      scale: 1 0.28;
    }

    50% {
      scale: 1 1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-21 {
  width: 100%;
  min-height: 100svh;
}
```
