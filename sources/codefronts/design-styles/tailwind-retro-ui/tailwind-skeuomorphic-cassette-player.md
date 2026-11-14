---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-skeuomorphic-cassette-player/"
title: "Tailwind Skeuomorphic Cassette Player"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "A portable tape deck with turning reels, a mechanical counter, and transport keys that travel when pressed."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Skeuomorphic Cassette Player
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-skeuomorphic-cassette-player/

A portable tape deck with turning reels, a mechanical counter, and transport keys that travel when pressed. It is the counterpoint to the one-bit bevel: skeuomorphic depth models a light source and a material, so it needs graded shadows and inner reflections &mdash; long arbitrary values that are worth keeping inline precisely because every control's depth is slightly different.
## HTML
```html
<section class="twr-13 relative block w-full min-h-svh box-border bg-twr13-bg text-twr13-ink font-twr13-cond" aria-labelledby="twr-13-title">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-13-title">Skeuomorphic portable cassette deck</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-13-theme">
    <label class="grid place-items-center size-11 rounded-full cursor-pointer bg-twr13-surface text-twr13-ink2 border border-twr13-line [box-shadow:0_1px_2px_rgba(0,0,0,0.2)] peer-focus-visible:outline-2 peer-focus-visible:outline-twr13-acc peer-focus-visible:outline-offset-2" for="twr-13-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle dark surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-5 max-w-[60rem] mx-auto px-[clamp(0.9rem,0.6rem+2vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <p class="m-0 justify-self-start min-w-0 rounded-sm border border-twr13-line bg-twr13-surface px-2.5 py-1.5 text-[0.68rem] tracking-[0.14em] uppercase text-twr13-ink2">Portable stereo cassette deck &middot; type II tape</p>

    <div class="min-w-0 grid gap-4 rounded-[18px] p-[clamp(0.9rem,0.6rem+1.6vw,1.6rem)] bg-twr13-case [background-image:repeating-linear-gradient(180deg,rgba(255,255,255,0.04)_0_1px,rgba(0,0,0,0.04)_1px_3px)] [box-shadow:inset_0_2px_0_rgba(255,255,255,0.7),inset_0_-3px_6px_rgba(0,0,0,0.25),0_22px_44px_-20px_rgba(0,0,0,0.55)]">
      <div class="min-w-0 rounded-xl p-[clamp(0.7rem,0.5rem+1.2vw,1.2rem)] bg-[linear-gradient(180deg,rgba(255,255,255,0.35),rgba(0,0,0,0.08))] [box-shadow:inset_0_2px_4px_rgba(255,255,255,0.55),inset_0_-2px_6px_rgba(0,0,0,0.3),0_1px_0_rgba(255,255,255,0.5)]">
        <div class="twr-13__tape min-w-0 grid gap-3 rounded-lg p-3.5 bg-[#26231d] [box-shadow:inset_0_1px_0_rgba(255,255,255,0.18),0_6px_14px_-6px_rgba(0,0,0,0.7)]">
          <div class="flex flex-wrap items-baseline justify-between gap-2 min-w-0 px-2.5 py-2 bg-[#efe6cf] text-[#221f19] [box-shadow:inset_0_-1px_0_rgba(0,0,0,0.25)]">
            <span class="font-twr13-mono text-[0.9rem] font-bold">A</span>
            <span class="min-w-0 overflow-hidden text-ellipsis whitespace-nowrap text-[0.8rem] tracking-[0.14em] uppercase">Night Drive Mix</span>
            <span class="font-twr13-mono text-[0.7rem] text-twr13-ink2">C-60</span>
          </div>
          <div class="flex items-center justify-between gap-3 min-w-0">
            <span class="twr-13__reel grid place-items-center size-[clamp(48px,10vw,72px)] rounded-full bg-[conic-gradient(from_0deg,#3b3830_0_25%,#575246_0_50%,#3b3830_0_75%,#575246_0_100%)] animate-twr13-spin [animation-duration:2.6s] motion-reduce:animate-none [box-shadow:inset_0_0_0_3px_#2a2721,inset_0_2px_6px_rgba(0,0,0,0.6)]" aria-hidden="true"><span class="block size-3 rounded-full bg-[#e8e2d2] [box-shadow:0_0_0_4px_#2a2721]"></span></span>
            <span class="flex-1 min-w-0 h-[clamp(28px,5vw,40px)] rounded-sm bg-[rgba(180,205,215,0.22)] [box-shadow:inset_0_2px_5px_rgba(0,0,0,0.5),inset_0_-1px_0_rgba(255,255,255,0.25)]" aria-hidden="true"></span>
            <span class="twr-13__reel grid place-items-center size-[clamp(48px,10vw,72px)] rounded-full bg-[conic-gradient(from_0deg,#3b3830_0_25%,#575246_0_50%,#3b3830_0_75%,#575246_0_100%)] animate-twr13-spin [animation-duration:3.4s] motion-reduce:animate-none [box-shadow:inset_0_0_0_3px_#2a2721,inset_0_2px_6px_rgba(0,0,0,0.6)]" aria-hidden="true"><span class="block size-3 rounded-full bg-[#e8e2d2] [box-shadow:0_0_0_4px_#2a2721]"></span></span>
          </div>
          <div class="flex justify-between gap-2 min-w-0 px-3" aria-hidden="true">
            <span class="size-1.5 rounded-full bg-[#141310]"></span><span class="size-1.5 rounded-full bg-[#141310]"></span><span class="size-1.5 rounded-full bg-[#141310]"></span><span class="size-1.5 rounded-full bg-[#141310]"></span><span class="size-1.5 rounded-full bg-[#141310]"></span>
          </div>
        </div>
      </div>

      <div class="min-w-0 grid gap-4">
        <div class="flex flex-wrap items-end justify-between gap-4 min-w-0">
          <div class="flex gap-1" role="img" aria-label="Tape counter reading 0 3 7">
            <span class="grid place-items-center w-7 h-9 bg-[#1b1913] text-[#f0e3c2] font-twr13-mono text-[1.35rem] tabular-nums [box-shadow:inset_0_2px_5px_rgba(0,0,0,0.8),inset_0_-1px_0_rgba(255,255,255,0.12)]">0</span><span class="grid place-items-center w-7 h-9 bg-[#1b1913] text-[#f0e3c2] font-twr13-mono text-[1.35rem] tabular-nums [box-shadow:inset_0_2px_5px_rgba(0,0,0,0.8),inset_0_-1px_0_rgba(255,255,255,0.12)]">3</span><span class="grid place-items-center w-7 h-9 bg-[#1b1913] text-[#f0e3c2] font-twr13-mono text-[1.35rem] tabular-nums [box-shadow:inset_0_2px_5px_rgba(0,0,0,0.8),inset_0_-1px_0_rgba(255,255,255,0.12)]">7</span>
          </div>
          <div class="flex items-end gap-1 h-10 px-2 py-1 bg-[#1b1913] [box-shadow:inset_0_2px_5px_rgba(0,0,0,0.8)]" aria-hidden="true">
            <span class="block w-2 self-end bg-[linear-gradient(180deg,#e0b64f,#b3452b)] [height:40%]"></span><span class="block w-2 self-end bg-[linear-gradient(180deg,#e0b64f,#b3452b)] [height:62%]"></span><span class="block w-2 self-end bg-[linear-gradient(180deg,#e0b64f,#b3452b)] [height:88%]"></span><span class="block w-2 self-end bg-[linear-gradient(180deg,#e0b64f,#b3452b)] [height:71%]"></span><span class="block w-2 self-end bg-[linear-gradient(180deg,#e0b64f,#b3452b)] [height:46%]"></span><span class="block w-2 self-end bg-[linear-gradient(180deg,#e0b64f,#b3452b)] [height:30%]"></span>
          </div>
        </div>

        <div class="flex flex-wrap gap-2.5 min-w-0">
          <input class="peer absolute size-px opacity-0 m-0" type="checkbox" id="twr-13-play" checked>
          <label class="group relative flex flex-col items-center justify-center gap-1 min-h-11 min-w-[4.5rem] px-3 py-2 border-0 cursor-pointer font-inherit bg-[linear-gradient(180deg,#e6e1d6_0%,#c8c1b4_100%)] text-twr13-ink [box-shadow:inset_0_1px_0_rgba(255,255,255,0.8),inset_0_-2px_2px_rgba(0,0,0,0.14),0_3px_0_var(--color-twr13-casek),0_6px_8px_-4px_rgba(0,0,0,0.45)] active:translate-y-0.5 active:[box-shadow:inset_0_1px_0_rgba(255,255,255,0.5),inset_0_2px_4px_rgba(0,0,0,0.28),0_1px_0_var(--color-twr13-casek)] focus-visible:outline-2 focus-visible:outline-twr13-acc focus-visible:outline-offset-2 peer-focus-visible:outline-2 peer-focus-visible:outline-twr13-acc peer-focus-visible:outline-offset-2" for="twr-13-play">
            <span class="block size-3 bg-twr13-ink [clip-path:polygon(0_0,100%_50%,0_100%)]" aria-hidden="true"></span>
            <span class="text-[0.6rem] tracking-[0.1em] uppercase text-twr13-ink2">Play / Pause</span>
          </label>
          <button class="group relative flex flex-col items-center justify-center gap-1 min-h-11 min-w-[4.5rem] px-3 py-2 border-0 cursor-pointer font-inherit bg-[linear-gradient(180deg,#e6e1d6_0%,#c8c1b4_100%)] text-twr13-ink [box-shadow:inset_0_1px_0_rgba(255,255,255,0.8),inset_0_-2px_2px_rgba(0,0,0,0.14),0_3px_0_var(--color-twr13-casek),0_6px_8px_-4px_rgba(0,0,0,0.45)] active:translate-y-0.5 active:[box-shadow:inset_0_1px_0_rgba(255,255,255,0.5),inset_0_2px_4px_rgba(0,0,0,0.28),0_1px_0_var(--color-twr13-casek)] focus-visible:outline-2 focus-visible:outline-twr13-acc focus-visible:outline-offset-2" type="button"><span class="block size-3 bg-twr13-ink [clip-path:polygon(100%_0,100%_100%,0_50%)]" aria-hidden="true"></span><span class="text-[0.6rem] tracking-[0.1em] uppercase text-twr13-ink2">Rewind</span></button>
          <button class="group relative flex flex-col items-center justify-center gap-1 min-h-11 min-w-[4.5rem] px-3 py-2 border-0 cursor-pointer font-inherit bg-[linear-gradient(180deg,#e6e1d6_0%,#c8c1b4_100%)] text-twr13-ink [box-shadow:inset_0_1px_0_rgba(255,255,255,0.8),inset_0_-2px_2px_rgba(0,0,0,0.14),0_3px_0_var(--color-twr13-casek),0_6px_8px_-4px_rgba(0,0,0,0.45)] active:translate-y-0.5 active:[box-shadow:inset_0_1px_0_rgba(255,255,255,0.5),inset_0_2px_4px_rgba(0,0,0,0.28),0_1px_0_var(--color-twr13-casek)] focus-visible:outline-2 focus-visible:outline-twr13-acc focus-visible:outline-offset-2" type="button"><span class="block size-3 bg-twr13-ink [clip-path:polygon(0_0,100%_50%,0_100%)]" aria-hidden="true"></span><span class="text-[0.6rem] tracking-[0.1em] uppercase text-twr13-ink2">Forward</span></button>
          <button class="group relative flex flex-col items-center justify-center gap-1 min-h-11 min-w-[4.5rem] px-3 py-2 border-0 cursor-pointer font-inherit bg-[linear-gradient(180deg,#e6e1d6_0%,#c8c1b4_100%)] text-twr13-ink [box-shadow:inset_0_1px_0_rgba(255,255,255,0.8),inset_0_-2px_2px_rgba(0,0,0,0.14),0_3px_0_var(--color-twr13-casek),0_6px_8px_-4px_rgba(0,0,0,0.45)] active:translate-y-0.5 active:[box-shadow:inset_0_1px_0_rgba(255,255,255,0.5),inset_0_2px_4px_rgba(0,0,0,0.28),0_1px_0_var(--color-twr13-casek)] focus-visible:outline-2 focus-visible:outline-twr13-acc focus-visible:outline-offset-2" type="button"><span class="block size-3 bg-twr13-ink" aria-hidden="true"></span><span class="text-[0.6rem] tracking-[0.1em] uppercase text-twr13-ink2">Stop</span></button>
          <button class="group relative flex flex-col items-center justify-center gap-1 min-h-11 min-w-[4.5rem] px-3 py-2 border-0 cursor-pointer font-inherit bg-[linear-gradient(180deg,#e6e1d6_0%,#c8c1b4_100%)] text-twr13-ink [box-shadow:inset_0_1px_0_rgba(255,255,255,0.8),inset_0_-2px_2px_rgba(0,0,0,0.14),0_3px_0_var(--color-twr13-casek),0_6px_8px_-4px_rgba(0,0,0,0.45)] active:translate-y-0.5 active:[box-shadow:inset_0_1px_0_rgba(255,255,255,0.5),inset_0_2px_4px_rgba(0,0,0,0.28),0_1px_0_var(--color-twr13-casek)] focus-visible:outline-2 focus-visible:outline-twr13-acc focus-visible:outline-offset-2" type="button"><span class="block size-3 rounded-full bg-twr13-red" aria-hidden="true"></span><span class="text-[0.6rem] tracking-[0.1em] uppercase text-twr13-ink2">Record</span></button>
        </div>

        <p class="m-0 min-w-0 max-w-[62ch] text-[0.82rem] leading-relaxed text-pretty text-twr13-ink2">Depth here is graded and blurred because it models a light source and a material. The bevelled chrome elsewhere in this collection is four flat insets and nothing else.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr13-case: #cfc9bd;
  --color-twr13-cased: #a49c8e;
  --color-twr13-casek: #4a463f;
  --color-twr13-ink: #211f1b;
  --color-twr13-red: #c0392b;
  --color-twr13-bg: #e6e1d7;
  --color-twr13-bg: oklch(0.91 0.013 88);
  --color-twr13-surface: #f7f4ee;
  --color-twr13-surface: oklch(0.97 0.008 88);
  --color-twr13-ink2: #58524a;
  --color-twr13-ink2: oklch(0.45 0.014 80);
  --color-twr13-line: #b2aa9c;
  --color-twr13-line: oklch(0.74 0.017 88);
  --color-twr13-acc: #9c3a10;
  --color-twr13-acc: oklch(0.45 0.15 45);
  --font-twr13-cond: 'Archivo', ui-sans-serif, 'Arial Narrow', Helvetica, sans-serif;
  --font-twr13-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}

@keyframes twr-13-spin {
  to {
    transform: rotate(360deg);
  }
}

@theme {
  --animate-twr13-spin: twr-13-spin 3s linear infinite;
}
/* Pausing is not a variant. Toggling the animate-* utility would restart the
   reels from zero — a tape does not rewind when you press pause — so the state
   is a play-state write driven by :has(). */

.twr-13:has(#twr-13-play:not(:checked)) .twr-13__reel {
  animation-play-state: paused;
}

.twr-13:has(#twr-13-theme:checked) {
  --color-twr13-bg: #18160f;
  --color-twr13-bg: oklch(0.20 0.012 88);
  --color-twr13-surface: #232019;
  --color-twr13-surface: oklch(0.26 0.014 88);
  --color-twr13-ink2: #b0a897;
  --color-twr13-ink2: oklch(0.75 0.016 88);
  --color-twr13-line: #46413a;
  --color-twr13-line: oklch(0.38 0.015 88);
  --color-twr13-acc: #ff9469;
  --color-twr13-acc: oklch(0.78 0.13 45);
}
```
