---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-eight-bit-pixel-art-buttons-and-hud/"
title: "Tailwind Eight Bit Pixel Art Buttons and HUD"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A game HUD and control set built entirely from stepped box-shadow blocks: segmented health, score with tabular figures, a lives row, and buttons whose…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Eight Bit Pixel Art Buttons and HUD
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-eight-bit-pixel-art-buttons-and-hud/

A game HUD and control set built entirely from stepped box-shadow blocks: segmented health, score with tabular figures, a lives row, and buttons whose notched corners are shadow offsets rather than a border image. The palette is a fixed eight-colour NES subset, and the port makes the discipline enforceable &mdash; every colour in the markup is a palette utility, so a ninth colour would have to be typed as a raw hex and would stand out in review.
## HTML
```html
<section class="twr-11 relative block w-full min-h-svh box-border bg-twr11-bg text-twr11-ink font-twr11-mono" aria-labelledby="twr-11-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-11-title">Eight-bit pixel art HUD and button set</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-11-theme">
    <label class="grid place-items-center size-11 cursor-pointer bg-twr11-paper text-twr11-ink twr11-notch peer-focus-visible:outline-2 peer-focus-visible:outline-twr11-acc peer-focus-visible:outline-offset-[6px]" for="twr-11-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-6 max-w-[68rem] mx-auto px-[clamp(1rem,0.6rem+2vw,2.25rem)] pt-[clamp(3.75rem,3rem+3vw,5rem)] pb-16">
    <p class="m-0 justify-self-start min-w-0 bg-twr11-ink text-twr11-paper px-2.5 py-1.5 text-[0.68rem] tracking-[0.12em] uppercase">NES-era palette subset &middot; 8 colours, no anti-aliasing</p>

    <div class="min-w-0 bg-twr11-surface p-[clamp(1rem,0.7rem+1.4vw,1.6rem)] twr11-notch">
      <div class="grid gap-5 grid-cols-[repeat(auto-fit,minmax(min(100%,11rem),1fr))]">
        <div class="min-w-0 grid content-start gap-1.5">
          <span class="text-[0.62rem] tracking-[0.18em] text-twr11-ink/70">HEALTH</span>
          <div class="flex flex-wrap gap-[var(--twr-11-px)]" role="meter" aria-valuenow="7" aria-valuemin="0" aria-valuemax="10" aria-label="Health, 7 of 10">
            <span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-red"></span><span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-red"></span><span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-red"></span><span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-red"></span><span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-red"></span><span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-red"></span><span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-red"></span><span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-ink/25"></span><span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-ink/25"></span><span class="w-[calc(var(--twr-11-px)*3)] h-[calc(var(--twr-11-px)*5)] bg-twr11-ink/25"></span>
          </div>
          <span class="text-[0.72rem] tabular-nums">7 / 10</span>
        </div>

        <div class="min-w-0 grid content-start gap-1.5">
          <span class="text-[0.62rem] tracking-[0.18em] text-twr11-ink/70">SCORE</span>
          <p class="m-0 text-[clamp(1.2rem,1rem+1.4vw,1.9rem)] font-bold tabular-nums tracking-[0.08em]">0128450</p>
        </div>

        <div class="min-w-0 grid content-start gap-1.5">
          <span class="text-[0.62rem] tracking-[0.18em] text-twr11-ink/70">LIVES</span>
          <ul class="list-none m-0 p-0 flex gap-2" aria-label="Three lives remaining">
            <li><span class="block size-4 bg-twr11-red [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]" aria-hidden="true"></span></li>
            <li><span class="block size-4 bg-twr11-red [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]" aria-hidden="true"></span></li>
            <li><span class="block size-4 bg-twr11-red [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]" aria-hidden="true"></span></li>
          </ul>
        </div>

        <div class="min-w-0 grid content-start gap-1.5">
          <span class="text-[0.62rem] tracking-[0.18em] text-twr11-ink/70">STAGE</span>
          <p class="m-0 text-[clamp(1.2rem,1rem+1.4vw,1.9rem)] font-bold tabular-nums">2&ndash;4</p>
        </div>
      </div>
    </div>

    <div class="min-w-0 grid gap-4 bg-twr11-surface p-[clamp(1rem,0.7rem+1.4vw,1.6rem)] twr11-notch">
      <h3 class="m-0 text-[0.72rem] tracking-[0.16em] uppercase text-twr11-ink/70">Controls</h3>
      <div class="flex flex-wrap gap-4">
        <button class="min-h-11 min-w-11 px-4 py-2.5 border-0 cursor-pointer font-inherit text-[0.8rem] font-bold tracking-[0.12em] text-twr11-paper twr11-notch active:twr11-notch-in focus-visible:outline-2 focus-visible:outline-twr11-acc focus-visible:outline-offset-[6px] bg-twr11-red" type="button">START</button>
        <button class="min-h-11 min-w-11 px-4 py-2.5 border-0 cursor-pointer font-inherit text-[0.8rem] font-bold tracking-[0.12em] text-twr11-paper twr11-notch active:twr11-notch-in focus-visible:outline-2 focus-visible:outline-twr11-acc focus-visible:outline-offset-[6px] bg-twr11-blue" type="button">SELECT</button>
        <button class="min-h-11 min-w-11 px-4 py-2.5 border-0 cursor-pointer font-inherit text-[0.8rem] font-bold tracking-[0.12em] text-twr11-paper twr11-notch active:twr11-notch-in focus-visible:outline-2 focus-visible:outline-twr11-acc focus-visible:outline-offset-[6px] bg-twr11-green" type="button">CONTINUE</button>
        <button class="min-h-11 min-w-11 px-4 py-2.5 border-0 cursor-not-allowed font-inherit text-[0.8rem] font-bold tracking-[0.12em] bg-twr11-ink/25 text-twr11-ink twr11-notch" type="button" disabled>LOCKED</button>
      </div>

      <h3 class="m-0 text-[0.72rem] tracking-[0.16em] uppercase text-twr11-ink/70">Palette &mdash; eight entries, no ninth</h3>
      <ul class="list-none m-0 p-0 grid gap-2.5 grid-cols-[repeat(auto-fit,minmax(min(100%,7rem),1fr))]">
        <li class="flex items-center gap-2 min-w-0 text-[0.7rem]"><span class="flex-none size-4 bg-twr11-ink [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]"></span>ink</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.7rem]"><span class="flex-none size-4 bg-twr11-paper [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]"></span>paper</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.7rem]"><span class="flex-none size-4 bg-twr11-red [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]"></span>red</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.7rem]"><span class="flex-none size-4 bg-twr11-orange [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]"></span>orange</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.7rem]"><span class="flex-none size-4 bg-twr11-yellow [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]"></span>yellow</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.7rem]"><span class="flex-none size-4 bg-twr11-green [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]"></span>green</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.7rem]"><span class="flex-none size-4 bg-twr11-blue [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]"></span>blue</li>
        <li class="flex items-center gap-2 min-w-0 text-[0.7rem]"><span class="flex-none size-4 bg-twr11-sky [box-shadow:0_0_0_var(--twr-11-px)_var(--color-twr11-ink)]"></span>sky</li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr11-ink: #101820;
  --color-twr11-paper: #f8f8f8;
  --color-twr11-red: #d82800;
  --color-twr11-orange: #fc9838;
  --color-twr11-yellow: #fcfc54;
  --color-twr11-green: #00a844;
  --color-twr11-blue: #2038ec;
  --color-twr11-sky: #9cd2f8;
  --color-twr11-bg: #9cd2f8;
  --color-twr11-surface: #f8f8f8;
  --color-twr11-acc: #1a2ba8;
  --color-twr11-acc: oklch(0.38 0.2 265);
  --font-twr11-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, 'Cascadia Mono', Consolas, monospace;
}

.twr-11 {
  --twr-11-px: 4px;
}
/* Four cardinal offsets whose union is a plus shape: the box's own corners are
   left uncovered, which is the notch. Too long and too repeated to inline. */

@utility twr11-notch {
  box-shadow: calc(var(--twr-11-px) * -1) 0 0 0 var(--color-twr11-ink), var(--twr-11-px) 0 0 0 var(--color-twr11-ink), 0 calc(var(--twr-11-px) * -1) 0 0 var(--color-twr11-ink), 0 var(--twr-11-px) 0 0 var(--color-twr11-ink), inset 0 var(--twr-11-px) 0 0 rgba(255, 255, 255, 0.35), inset 0 calc(var(--twr-11-px) * -1) 0 0 rgba(0, 0, 0, 0.3);
}
/* Pressed: the inner light and shadow swap sides. The face colour never changes,
   because darkening it would introduce a colour outside the palette. */

@utility twr11-notch-in {
  box-shadow: calc(var(--twr-11-px) * -1) 0 0 0 var(--color-twr11-ink), var(--twr-11-px) 0 0 0 var(--color-twr11-ink), 0 calc(var(--twr-11-px) * -1) 0 0 var(--color-twr11-ink), 0 var(--twr-11-px) 0 0 var(--color-twr11-ink), inset 0 var(--twr-11-px) 0 0 rgba(0, 0, 0, 0.3), inset 0 calc(var(--twr-11-px) * -1) 0 0 rgba(255, 255, 255, 0.35);
}

.twr-11:has(#twr-11-theme:checked) {
  --color-twr11-bg: #14203a;
  --color-twr11-bg: oklch(0.24 0.06 265);
  --color-twr11-surface: #e4e6ec;
}
```
