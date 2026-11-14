---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-crt-scanlines-and-screen-curvature/"
title: "Tailwind CRT Scanlines and Screen Curvature"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A CRT look is not one effect, it is four: scanlines, curvature, phosphor bloom and mains flicker."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CRT Scanlines and Screen Curvature
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-crt-scanlines-and-screen-curvature/

A CRT look is not one effect, it is four: scanlines, curvature, phosphor bloom and mains flicker. Each is a separate layer with its own checkbox, so you can stack them one at a time and see what each contributes. The port is instructive because three of the four move cleanly into the class list &mdash; and the fourth, the fractional-DPR scanline fix, is the demo's whole reason for keeping a stylesheet.
## HTML
```html
<section class="twr-01 relative block w-full min-h-svh box-border bg-twr01-bg text-twr01-ink font-twr01-mono" aria-labelledby="twr-01-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-01-title">CRT scanline and curvature layer stack</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-01-theme">
    <label class="grid place-items-center size-11 rounded-full border border-twr01-line bg-twr01-surface text-twr01-ink2 cursor-pointer peer-focus-visible:outline-2 peer-focus-visible:outline-twr01-acc peer-focus-visible:outline-offset-2" for="twr-01-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-6 max-w-[74rem] mx-auto px-[clamp(0.85rem,0.5rem+2vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <p class="m-0 justify-self-start min-w-0 rounded-sm border border-twr01-line bg-twr01-surface px-2.5 py-1.5 text-[0.7rem] tracking-[0.16em] uppercase text-twr01-ink2">Cathode-ray tube &middot; shadow-mask display</p>

    <div class="grid grid-cols-[minmax(0,1fr)] items-start gap-5 lg:grid-cols-[minmax(0,1.55fr)_minmax(0,1fr)] lg:gap-8">
      <div class="relative min-w-0 rounded-[44px] p-[clamp(0.9rem,0.6rem+1.4vw,1.6rem)] [background:linear-gradient(180deg,var(--color-twr01-case)_0%,var(--color-twr01-case2)_100%)] [box-shadow:inset_0_2px_0_rgba(255,255,255,0.55),inset_0_-2px_0_rgba(0,0,0,0.35),0_18px_40px_-18px_rgba(0,0,0,0.65)]">
        <div class="twr-01__screen relative grid place-items-center isolate overflow-hidden aspect-4/3 rounded-[var(--twr-01-curve)] transition-[border-radius] duration-[240ms] [background:radial-gradient(120%_100%_at_50%_45%,#0a2018_0%,var(--color-twr01-tube)_72%)] [box-shadow:inset_0_0_0_2px_#06120d,inset_0_0_30px_6px_rgba(0,0,0,0.75)]">
          <div class="relative z-2 grid justify-items-center gap-2 min-w-0 p-[clamp(0.75rem,0.4rem+2vw,2rem)] text-center text-twr01-glow">
            <p class="m-0 text-[clamp(0.6rem,0.45rem+0.7vw,0.85rem)] tracking-[0.1em] text-twr01-glowdim">SYSTEM MONITOR &mdash; VT/CRT COMPOSITE</p>
            <p class="relative m-0 font-bold leading-none text-[clamp(1.6rem,0.6rem+6.5vw,4rem)] tracking-[0.14em]">PHOSPHOR<span class="absolute inset-0 grid place-items-center pointer-events-none mix-blend-screen blur-[3px] transition-opacity duration-200 [opacity:calc(0.85*var(--twr-01-bloom-on))]" aria-hidden="true">PHOSPHOR</span></p>
            <p class="m-0 text-[clamp(0.6rem,0.45rem+0.7vw,0.85rem)] tracking-[0.1em]">SCAN 15.734 kHz &nbsp; VERT 59.94 Hz</p>
            <p class="m-0 text-[clamp(0.6rem,0.45rem+0.7vw,0.85rem)] tracking-[0.1em]">MASK PITCH 0.28 mm &nbsp; DEFL 90&deg;</p>
            <p class="m-0 text-[clamp(0.6rem,0.45rem+0.7vw,0.85rem)] tracking-[0.1em] text-twr01-glowdim">READY<span class="inline-block w-[0.6em] h-[1em] ms-[0.3em] align-[-0.15em] bg-twr01-glow animate-twr01-blink motion-reduce:animate-none" aria-hidden="true"></span></p>
          </div>


          <div class="twr-01__scan absolute inset-0 z-4 pointer-events-none transition-opacity duration-200 [background-image:repeating-linear-gradient(to_bottom,rgba(0,0,0,0)_0,rgba(0,0,0,0)_calc(var(--twr-01-scan)-1px),rgba(0,0,0,0.72)_calc(var(--twr-01-scan)-1px),rgba(0,0,0,0.72)_var(--twr-01-scan))] [opacity:calc(0.55*var(--twr-01-scan-on))]" aria-hidden="true"></div>

          <div class="absolute -inset-px z-5 pointer-events-none transition-opacity duration-200 [background:radial-gradient(115%_105%_at_50%_50%,rgba(0,0,0,0)_52%,rgba(0,0,0,0.55)_84%,rgba(0,0,0,0.9)_100%),linear-gradient(90deg,rgba(255,255,255,0.05),rgba(255,255,255,0)_18%_82%,rgba(255,255,255,0.05))] [opacity:var(--twr-01-curve-on)]" aria-hidden="true"></div>

          <div class="twr-01__flick absolute inset-0 z-6 pointer-events-none opacity-0 bg-[rgba(120,255,190,0.05)] animate-twr01-flicker motion-reduce:animate-none" aria-hidden="true"></div>
        </div>

        <div class="flex items-center justify-between gap-3 min-w-0 pt-3 px-1.5 pb-0.5">
          <span class="min-w-0 text-[0.62rem] tracking-[0.22em] text-[#3c4038] [text-shadow:0_1px_0_rgba(255,255,255,0.45)]">TRINITRON&nbsp;/&nbsp;14"</span>
          <span class="flex-none size-[9px] rounded-full bg-[#63f0a0] [box-shadow:0_0_8px_2px_rgba(99,240,160,0.7),inset_0_0_2px_#0a3a22]" aria-hidden="true"></span>
        </div>
      </div>

      <ul class="list-none m-0 p-0 min-w-0 grid grid-cols-[minmax(0,1fr)] content-start gap-2 lg:gap-2.5">
        <li class="relative min-w-0">
          <input class="peer absolute top-0 left-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-01-scan" checked>
          <label class="grid grid-cols-[44px_minmax(0,1fr)] items-center gap-x-3 min-h-14 cursor-pointer rounded-[3px] border border-twr01-line bg-twr01-surface py-2 pr-3 pl-2 peer-checked:border-twr01-ink2 peer-checked:[&_[data-n]]:bg-twr01-ink peer-checked:[&_[data-n]]:border-twr01-ink peer-checked:[&_[data-n]]:text-twr01-surface peer-focus-visible:outline-2 peer-focus-visible:outline-twr01-acc peer-focus-visible:outline-offset-2" for="twr-01-scan">
            <span class="row-span-2 grid place-items-center size-[34px] ms-[5px] rounded-sm border-2 border-twr01-ink2 text-[0.72rem] tabular-nums text-twr01-ink2" data-n>01</span>
            <span class="min-w-0 text-sm font-semibold tracking-[0.02em]">Scanlines</span>
            <span class="min-w-0 text-[0.68rem] text-twr01-ink2 [overflow-wrap:anywhere]">repeating gradient, 3px period</span>
          </label>
        </li>
        <li class="relative min-w-0">
          <input class="peer absolute top-0 left-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-01-curve" checked>
          <label class="grid grid-cols-[44px_minmax(0,1fr)] items-center gap-x-3 min-h-14 cursor-pointer rounded-[3px] border border-twr01-line bg-twr01-surface py-2 pr-3 pl-2 peer-checked:border-twr01-ink2 peer-checked:[&_[data-n]]:bg-twr01-ink peer-checked:[&_[data-n]]:border-twr01-ink peer-checked:[&_[data-n]]:text-twr01-surface peer-focus-visible:outline-2 peer-focus-visible:outline-twr01-acc peer-focus-visible:outline-offset-2" for="twr-01-curve">
            <span class="row-span-2 grid place-items-center size-[34px] ms-[5px] rounded-sm border-2 border-twr01-ink2 text-[0.72rem] tabular-nums text-twr01-ink2" data-n>02</span>
            <span class="min-w-0 text-sm font-semibold tracking-[0.02em]">Curvature</span>
            <span class="min-w-0 text-[0.68rem] text-twr01-ink2 [overflow-wrap:anywhere]">radius plus inset corner vignette</span>
          </label>
        </li>
        <li class="relative min-w-0">
          <input class="peer absolute top-0 left-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-01-bloom" checked>
          <label class="grid grid-cols-[44px_minmax(0,1fr)] items-center gap-x-3 min-h-14 cursor-pointer rounded-[3px] border border-twr01-line bg-twr01-surface py-2 pr-3 pl-2 peer-checked:border-twr01-ink2 peer-checked:[&_[data-n]]:bg-twr01-ink peer-checked:[&_[data-n]]:border-twr01-ink peer-checked:[&_[data-n]]:text-twr01-surface peer-focus-visible:outline-2 peer-focus-visible:outline-twr01-acc peer-focus-visible:outline-offset-2" for="twr-01-bloom">
            <span class="row-span-2 grid place-items-center size-[34px] ms-[5px] rounded-sm border-2 border-twr01-ink2 text-[0.72rem] tabular-nums text-twr01-ink2" data-n>03</span>
            <span class="min-w-0 text-sm font-semibold tracking-[0.02em]">Phosphor bloom</span>
            <span class="min-w-0 text-[0.68rem] text-twr01-ink2 [overflow-wrap:anywhere]">blurred duplicate, mix-blend-screen</span>
          </label>
        </li>
        <li class="relative min-w-0">
          <input class="peer absolute top-0 left-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-01-flick" checked>
          <label class="grid grid-cols-[44px_minmax(0,1fr)] items-center gap-x-3 min-h-14 cursor-pointer rounded-[3px] border border-twr01-line bg-twr01-surface py-2 pr-3 pl-2 peer-checked:border-twr01-ink2 peer-checked:[&_[data-n]]:bg-twr01-ink peer-checked:[&_[data-n]]:border-twr01-ink peer-checked:[&_[data-n]]:text-twr01-surface peer-focus-visible:outline-2 peer-focus-visible:outline-twr01-acc peer-focus-visible:outline-offset-2" for="twr-01-flick">
            <span class="row-span-2 grid place-items-center size-[34px] ms-[5px] rounded-sm border-2 border-twr01-ink2 text-[0.72rem] tabular-nums text-twr01-ink2" data-n>04</span>
            <span class="min-w-0 text-sm font-semibold tracking-[0.02em]">Mains flicker</span>
            <span class="min-w-0 text-[0.68rem] text-twr01-ink2 [overflow-wrap:anywhere]">6s opacity cycle, off under motion-reduce</span>
          </label>
        </li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr01-bg: #d9dde1;
  --color-twr01-bg: oklch(0.88 0.006 240);
  --color-twr01-surface: #f4f6f7;
  --color-twr01-surface: oklch(0.97 0.003 240);
  --color-twr01-ink: #14181b;
  --color-twr01-ink: oklch(0.19 0.008 240);
  --color-twr01-ink2: #4a545c;
  --color-twr01-ink2: oklch(0.43 0.014 240);
  --color-twr01-line: #a9b1b8;
  --color-twr01-line: oklch(0.75 0.009 240);
  --color-twr01-acc: #0f6bd8;
  --color-twr01-acc: oklch(0.52 0.19 252);
  --color-twr01-glow: #7cf6b0;
  --color-twr01-glow: oklch(0.90 0.15 158);
  --color-twr01-glowdim: #4fbf88;
  --color-twr01-glowdim: oklch(0.74 0.13 158);
  --color-twr01-tube: #04100b;
  --color-twr01-tube: oklch(0.13 0.02 158);
  --color-twr01-case: #b9beb6;
  --color-twr01-case2: #8f948c;
  --font-twr01-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --animate-twr01-blink: twr-01-blink 1.2s steps(1, end) infinite;
  --animate-twr01-flicker: twr-01-flicker 6s ease-in-out infinite;
}
/* The layer switches and the tube geometry are plain custom properties, not tokens:
   they are read inside arbitrary utilities and never need a utility of their own. */

.twr-01 {
  --twr-01-scan: 3px;
  --twr-01-curve: 26px;
  --twr-01-scan-on: 1;
  --twr-01-curve-on: 1;
  --twr-01-bloom-on: 1;
}
/* :has() writes a custom property on the section from the state of an input nested
   inside it. A variant can select that, but it cannot perform the write — so these
   five rules are the port's irreducible CSS. */

.twr-01:has(#twr-01-scan:not(:checked)) {
  --twr-01-scan-on: 0;
}

.twr-01:has(#twr-01-curve:not(:checked)) {
  --twr-01-curve-on: 0;
  --twr-01-curve: 2px;
}

.twr-01:has(#twr-01-bloom:not(:checked)) {
  --twr-01-bloom-on: 0;
}

.twr-01:has(#twr-01-flick:not(:checked)) .twr-01__flick {
  animation: none;
  opacity: 0;
}

.twr-01:has(#twr-01-theme:checked) {
  --color-twr01-bg: #101314;
  --color-twr01-bg: oklch(0.18 0.005 200);
  --color-twr01-surface: #1b2022;
  --color-twr01-surface: oklch(0.24 0.007 200);
  --color-twr01-ink: #eef2f3;
  --color-twr01-ink: oklch(0.96 0.003 200);
  --color-twr01-ink2: #a2acb1;
  --color-twr01-ink2: oklch(0.74 0.009 200);
  --color-twr01-line: #394246;
  --color-twr01-line: oklch(0.35 0.01 200);
  --color-twr01-acc: #6fb2ff;
  --color-twr01-acc: oklch(0.76 0.13 252);
}

@keyframes twr-01-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

@keyframes twr-01-flicker {
  0%,
    96%,
    100% {
    opacity: 0;
  }

  97% {
    opacity: 0.5;
  }

  98% {
    opacity: 0.12;
  }

  99% {
    opacity: 0.38;
  }
}
/* A min-resolution query has no variant form. Unlayered rules outrank Tailwind's
   layered utilities, so this widens and softens the period with no ! prefix. */

@media (min-resolution: 1.5dppx) {
  .twr-01__scan {
    background-image: repeating-linear-gradient(
          to bottom,
          rgba(0, 0, 0, 0) 0,
          rgba(0, 0, 0, 0.62) calc(var(--twr-01-scan) * 0.5),
          rgba(0, 0, 0, 0) calc(var(--twr-01-scan) * 1.34)
        );
  }
}

@media (prefers-reduced-motion: reduce) {
  .twr-01__screen {
    transition: none;
  }
}
```
