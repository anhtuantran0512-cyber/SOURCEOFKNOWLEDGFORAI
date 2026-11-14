---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-retro-arcade-game-interface/"
title: "Tailwind Retro Arcade Game Interface"
section: "design-styles"
category: "tailwind-retro-ui"
category_name: "Tailwind Retro UI"
description: "An arcade attract screen: illuminated marquee, high-score table with initials, and the insert-coin prompt cycling on the cabinet's own cadence."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Retro Arcade Game Interface
Source: https://codefronts.com/design-styles/tailwind-retro-ui/tailwind-retro-arcade-game-interface/

An arcade attract screen: illuminated marquee, high-score table with initials, and the insert-coin prompt cycling on the cabinet's own cadence. The blink is the interesting part &mdash; exactly the pattern the pause-and-stop criterion exists for &mdash; and in utilities the whole rotation becomes a group-data-[attract=...] state machine, with the script owning nothing but the attribute.
## HTML
```html
<section class="twr-15 group relative block w-full min-h-svh box-border bg-twr15-bg text-[#eef1f5] font-twr15-mono" aria-labelledby="twr-15-title" data-attract="scores">
  <h2 class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap" id="twr-15-title">Arcade cabinet attract screen</h2>

  <div class="absolute top-4 right-4 z-6">
    <input class="peer absolute inset-0 size-11 m-0 opacity-0 cursor-pointer" type="checkbox" id="twr-15-theme">
    <label class="grid place-items-center size-11 rounded-full cursor-pointer border border-twr15-edge bg-twr15-shell text-twr15-ink2 peer-focus-visible:outline-2 peer-focus-visible:outline-twr15-acc peer-focus-visible:outline-offset-2" for="twr-15-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Toggle light surround</span>
    </label>
  </div>

  <div class="grid grid-cols-[minmax(0,1fr)] gap-5 max-w-[60rem] mx-auto px-[clamp(0.75rem,0.5rem+2vw,2rem)] pt-[clamp(3.5rem,3rem+3vw,5rem)] pb-16">
    <div class="min-w-0 grid gap-4 rounded-2xl p-[clamp(0.8rem,0.5rem+1.6vw,1.5rem)] [background:linear-gradient(180deg,var(--color-twr15-shell)_0%,var(--color-twr15-shell2)_100%)] [box-shadow:inset_0_2px_0_rgba(255,255,255,0.1),0_24px_50px_-24px_rgba(0,0,0,0.9)]">
      <div class="min-w-0 grid justify-items-center gap-1 rounded-lg px-4 py-4 text-center [background:linear-gradient(90deg,rgba(255,194,71,0.08)_0%,rgba(255,194,71,0.35)_50%,rgba(255,194,71,0.08)_100%)] [box-shadow:inset_0_0_24px_rgba(255,194,71,0.35),0_10px_30px_-14px_rgba(255,194,71,0.5)]">
        <span class="min-w-0 font-bold uppercase tracking-[0.2em] text-twr15-amber text-[clamp(1.1rem,0.8rem+2.4vw,2.4rem)] [text-shadow:0_0_10px_rgba(255,194,71,0.65)]">Vector Patrol</span>
        <span class="text-[0.66rem] tracking-[0.28em] uppercase text-twr15-amber/80">1 or 2 players</span>
      </div>

      <div class="min-w-0 grid content-start gap-4 rounded-lg bg-[#05070a] p-[clamp(0.9rem,0.6rem+1.6vw,1.75rem)] min-h-[clamp(280px,42vw,380px)] [box-shadow:inset_0_0_0_2px_#000,inset_0_0_40px_rgba(0,0,0,0.9)]">
        <div class="flex flex-wrap justify-between gap-x-5 gap-y-1 min-w-0 text-[clamp(0.6rem,0.5rem+0.5vw,0.8rem)] tracking-[0.14em] text-twr15-cyan">
          <span>1UP <b class="font-bold tabular-nums text-white">0032100</b></span>
          <span>HI <b class="font-bold tabular-nums text-twr15-amber">0198750</b></span>
          <span>2UP <b class="font-bold tabular-nums text-white">0000000</b></span>
        </div>

        <div class="grid min-w-0 place-content-center">
          <section class="min-w-0 hidden group-data-[attract=scores]:grid content-start justify-items-center gap-3 text-center" data-twr-15-panel="scores" aria-labelledby="twr-15-p1">
            <h3 class="m-0 text-[clamp(0.95rem,0.8rem+1vw,1.4rem)] font-bold tracking-[0.24em] text-twr15-amber" id="twr-15-p1">HIGH SCORES</h3>
            <ol class="list-none m-0 p-0 grid gap-1.5 min-w-0 w-full max-w-[22rem]">
              <li class="grid grid-cols-[3.5rem_3.5rem_minmax(0,1fr)] items-baseline gap-3 text-[clamp(0.7rem,0.6rem+0.6vw,0.95rem)]"><span class="text-twr15-cyan">1ST</span><span class="text-twr15-green">AJC</span><span class="tabular-nums text-end text-white">0198750</span></li>
              <li class="grid grid-cols-[3.5rem_3.5rem_minmax(0,1fr)] items-baseline gap-3 text-[clamp(0.7rem,0.6rem+0.6vw,0.95rem)]"><span class="text-twr15-cyan">2ND</span><span class="text-twr15-green">PSA</span><span class="tabular-nums text-end text-white">0176420</span></li>
              <li class="grid grid-cols-[3.5rem_3.5rem_minmax(0,1fr)] items-baseline gap-3 text-[clamp(0.7rem,0.6rem+0.6vw,0.95rem)]"><span class="text-twr15-cyan">3RD</span><span class="text-twr15-green">JLE</span><span class="tabular-nums text-end text-white">0154900</span></li>
              <li class="grid grid-cols-[3.5rem_3.5rem_minmax(0,1fr)] items-baseline gap-3 text-[clamp(0.7rem,0.6rem+0.6vw,0.95rem)]"><span class="text-twr15-cyan">4TH</span><span class="text-twr15-green">SRV</span><span class="tabular-nums text-end text-white">0132080</span></li>
              <li class="grid grid-cols-[3.5rem_3.5rem_minmax(0,1fr)] items-baseline gap-3 text-[clamp(0.7rem,0.6rem+0.6vw,0.95rem)]"><span class="text-twr15-cyan">5TH</span><span class="text-twr15-green">ZZZ</span><span class="tabular-nums text-end text-white">0100000</span></li>
            </ol></section>

          <section class="min-w-0 hidden group-data-[attract=title]:grid content-start justify-items-center gap-3 text-center" data-twr-15-panel="title" aria-labelledby="twr-15-p2">
            <h3 class="m-0 text-[clamp(0.95rem,0.8rem+1vw,1.4rem)] font-bold tracking-[0.24em] text-twr15-amber" id="twr-15-p2">VECTOR PATROL</h3>
            <p class="m-0 text-[0.8rem] tracking-[0.2em] text-twr15-green">DEFEND SECTOR SEVEN</p>
            <ul class="list-none m-0 p-0 grid gap-2 text-[0.72rem] tracking-[0.12em] text-white/85">
              <li class="flex items-center gap-2.5"><span class="size-2.5 bg-twr15-green" aria-hidden="true"></span>SCOUT &mdash; 100 PTS</li>
              <li class="flex items-center gap-2.5"><span class="size-2.5 bg-twr15-cyan" aria-hidden="true"></span>RUNNER &mdash; 250 PTS</li>
              <li class="flex items-center gap-2.5"><span class="size-2.5 bg-twr15-red" aria-hidden="true"></span>CARRIER &mdash; 1000 PTS</li>
            </ul></section>

          <section class="min-w-0 hidden group-data-[attract=credits]:grid content-start justify-items-center gap-3 text-center" data-twr-15-panel="credits" aria-labelledby="twr-15-p3">
            <h3 class="m-0 text-[clamp(0.95rem,0.8rem+1vw,1.4rem)] font-bold tracking-[0.24em] text-twr15-amber" id="twr-15-p3">CREDITS 00</h3>
            <p class="m-0 font-bold tracking-[0.24em] text-twr15-red text-[clamp(1.1rem,0.9rem+1.6vw,2rem)] animate-twr15-blink motion-reduce:animate-none">INSERT COIN</p>
            <p class="m-0 text-[0.68rem] tracking-[0.16em] text-white/70">1 COIN 1 PLAY &nbsp;&middot;&nbsp; 2 COINS 3 PLAYS</p></section>
        </div>

        <p class="m-0 min-w-0 text-center text-[0.6rem] tracking-[0.16em] text-white/55">&copy; 1983 NORTHGATE ELECTRONICS &middot; ALL RIGHTS RESERVED</p>
      </div>

      <div class="flex flex-wrap items-center justify-between gap-4 min-w-0 rounded-lg px-4 py-3.5 [background:linear-gradient(180deg,#2a2e35,#171a1f)] [box-shadow:inset_0_1px_0_rgba(255,255,255,0.12)]">
        <span class="relative block size-10 rounded-full bg-[#c8342b] [box-shadow:inset_0_-4px_0_rgba(0,0,0,0.35),0_6px_10px_-4px_rgba(0,0,0,0.8)]" aria-hidden="true"></span>
        <div class="flex flex-wrap gap-3">
          <button class="min-h-11 min-w-11 px-4 py-2.5 rounded-full border-0 cursor-pointer font-inherit text-[0.72rem] font-bold tracking-[0.14em] text-[#14161a] [box-shadow:inset_0_-3px_0_rgba(0,0,0,0.35),0_3px_0_#0a0b0d] active:translate-y-[3px] active:[box-shadow:inset_0_-2px_0_rgba(0,0,0,0.3)] focus-visible:outline-2 focus-visible:outline-twr15-acc focus-visible:outline-offset-2 bg-twr15-red" type="button">FIRE</button>
          <button class="min-h-11 min-w-11 px-4 py-2.5 rounded-full border-0 cursor-pointer font-inherit text-[0.72rem] font-bold tracking-[0.14em] text-[#14161a] [box-shadow:inset_0_-3px_0_rgba(0,0,0,0.35),0_3px_0_#0a0b0d] active:translate-y-[3px] active:[box-shadow:inset_0_-2px_0_rgba(0,0,0,0.3)] focus-visible:outline-2 focus-visible:outline-twr15-acc focus-visible:outline-offset-2 bg-twr15-amber" type="button">THRUST</button>
          <button class="min-h-11 min-w-11 px-4 py-2.5 rounded-full border-0 cursor-pointer font-inherit text-[0.72rem] font-bold tracking-[0.14em] text-[#14161a] [box-shadow:inset_0_-3px_0_rgba(0,0,0,0.35),0_3px_0_#0a0b0d] active:translate-y-[3px] active:[box-shadow:inset_0_-2px_0_rgba(0,0,0,0.3)] focus-visible:outline-2 focus-visible:outline-twr15-acc focus-visible:outline-offset-2 bg-twr15-green" type="button">1P START</button>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twr15-shell: #1d1f24;
  --color-twr15-shell2: #101216;
  --color-twr15-edge: #34383f;
  --color-twr15-green: #4dff9a;
  --color-twr15-amber: #ffc247;
  --color-twr15-red: #ff5a4d;
  --color-twr15-cyan: #52e5ff;
  --color-twr15-bg: #0c0d10;
  --color-twr15-bg: oklch(0.15 0.006 280);
  --color-twr15-ink2: #a2a7b0;
  --color-twr15-ink2: oklch(0.73 0.01 280);
  --color-twr15-acc: #52e5ff;
  --color-twr15-acc: oklch(0.84 0.11 218);
  --font-twr15-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, 'Cascadia Mono', Consolas, monospace;
  --animate-twr15-blink: twr-15-blink 1.4s steps(1, end) infinite;
}
/* 1.4s period is about 0.7 flashes per second — well under the three-per-second
   threshold, and the rotation takes the prompt off screen entirely. */

@keyframes twr-15-blink {
  0%,
    59% {
    opacity: 1;
  }

  60%,
    100% {
    opacity: 0;
  }
}

.twr-15:has(#twr-15-theme:checked) {
  --color-twr15-bg: #e7e9ee;
  --color-twr15-bg: oklch(0.92 0.005 280);
  --color-twr15-ink2: #4c515a;
  --color-twr15-ink2: oklch(0.44 0.012 280);
}
```

## JavaScript
```js
/* State only: one attribute on the root. No classes, no styles, no DOM writes. */
(function () {
  var root = document.querySelector('.twr-15');
  if (!root) return;
  var states = ['scores', 'title', 'credits'];
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var i = 0;
  var timer = null;

  function start() {
    if (reduce.matches) {
      root.dataset.attract = 'scores';
      return;
    }
    timer = setInterval(function () {
      i = (i + 1) % states.length;
      root.dataset.attract = states[i];
    }, 4200);
  }
  function stop() { if (timer) { clearInterval(timer); timer = null; } }

  start();
  reduce.addEventListener('change', function () { stop(); start(); });

  root.__twrCleanup = function () {
    stop();
    root.dataset.attract = 'scores';
  };
})();
```
