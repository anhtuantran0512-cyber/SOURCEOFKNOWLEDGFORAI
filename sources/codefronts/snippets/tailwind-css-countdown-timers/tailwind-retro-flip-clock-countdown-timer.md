---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-retro-flip-clock-countdown-timer/"
title: "Tailwind Retro Flip Clock Countdown Timer"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A split-flap countdown with a hinge line through every card and a real flap rotation on each change, framed as a deadline &mdash; the last posting time for a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Retro Flip Clock Countdown Timer
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-retro-flip-clock-countdown-timer/

A split-flap countdown with a hinge line through every card and a real flap rotation on each change, framed as a deadline &mdash; the last posting time for a print run &mdash; rather than a decorative odometer. In the port the flaps are perspective-[420px] + backface-hidden + group-data-flip/d:animate-tcd22-fall, cards are sized from one --w custom property, and the done state now offers the next slot instead of a dead end.
## HTML
```html
<section class="tcd-22 w-full min-h-svh grid place-items-center bg-tcd22-page bg-[radial-gradient(60%_50%_at_50%_40%,var(--color-tcd22-glow),transparent_70%)] px-5 py-12 font-tcd22-sans text-tcd22-card" aria-labelledby="tcd-22-title">
  <div class="grid w-full max-w-[780px] justify-items-center gap-7 text-center">
    <header class="grid justify-items-center gap-2">
      <p class="text-[10.5px] font-semibold uppercase tracking-[0.24em] text-tcd22-acc">Quill Press · plate room</p>
      <h2 id="tcd-22-title" class="font-tcd22-slab text-[clamp(26px,5vw,40px)] font-semibold leading-[1.08] tracking-[-0.01em] text-balance">Last posting for the autumn run</h2>
      <p class="max-w-[48ch] text-[14px] leading-relaxed text-tcd22-mut text-pretty">Files in before the flaps stop moving make Thursday's press. After that the next slot is in eleven days.</p>
    </header>

    <div role="timer" data-clock style="--w: clamp(44px, 12.5vw, 84px)" class="flex flex-wrap items-start justify-center gap-[clamp(6px,2vw,16px)] rounded-[22px] bg-tcd22-frame p-[clamp(12px,3vw,22px)] shadow-[inset_0_2px_0_rgb(255_255_255/0.06),0_30px_60px_-30px_rgb(0_0_0/0.9)]">
      <div class="grid justify-items-center gap-2.5"><div class="flex gap-1.5">
        <span data-digit class="group/d relative block h-[calc(var(--w)*1.34)] w-(--w) rounded-lg bg-tcd22-low font-tcd22-slab text-[calc(var(--w)*0.92)] font-semibold tabular-nums text-tcd22-ink shadow-[0_8px_18px_-8px_rgb(0_0_0/0.7)] perspective-[420px]"><b class="absolute inset-x-0 top-0 h-1/2 overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card"><i class="grid h-[200%] place-items-center not-italic leading-none">0</i></b><b class="absolute inset-x-0 bottom-0 h-1/2 overflow-hidden rounded-b-lg bg-tcd22-low"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">0</i></b><b class="absolute inset-x-0 top-0 z-30 h-1/2 origin-bottom overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card opacity-0 backface-hidden group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-fall motion-reduce:hidden"><i class="grid h-[200%] place-items-center not-italic leading-none">0</i></b><b class="absolute inset-x-0 bottom-0 z-20 h-1/2 origin-top overflow-hidden rounded-b-lg bg-tcd22-low opacity-0 backface-hidden [transform:rotateX(90deg)] group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-rise motion-reduce:hidden"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">0</i></b><span aria-hidden="true" class="absolute top-1/2 -left-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span><span aria-hidden="true" class="absolute top-1/2 -right-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span></span>
        <span data-digit class="group/d relative block h-[calc(var(--w)*1.34)] w-(--w) rounded-lg bg-tcd22-low font-tcd22-slab text-[calc(var(--w)*0.92)] font-semibold tabular-nums text-tcd22-ink shadow-[0_8px_18px_-8px_rgb(0_0_0/0.7)] perspective-[420px]"><b class="absolute inset-x-0 top-0 h-1/2 overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card"><i class="grid h-[200%] place-items-center not-italic leading-none">6</i></b><b class="absolute inset-x-0 bottom-0 h-1/2 overflow-hidden rounded-b-lg bg-tcd22-low"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">6</i></b><b class="absolute inset-x-0 top-0 z-30 h-1/2 origin-bottom overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card opacity-0 backface-hidden group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-fall motion-reduce:hidden"><i class="grid h-[200%] place-items-center not-italic leading-none">6</i></b><b class="absolute inset-x-0 bottom-0 z-20 h-1/2 origin-top overflow-hidden rounded-b-lg bg-tcd22-low opacity-0 backface-hidden [transform:rotateX(90deg)] group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-rise motion-reduce:hidden"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">6</i></b><span aria-hidden="true" class="absolute top-1/2 -left-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span><span aria-hidden="true" class="absolute top-1/2 -right-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span></span>
      </div><p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-tcd22-mut">hours</p></div>
      <span aria-hidden="true" class="mt-[calc(var(--w)*0.45)] grid gap-[calc(var(--w)*0.22)]"><span class="size-1.5 rounded-full bg-tcd22-acc"></span><span class="size-1.5 rounded-full bg-tcd22-acc"></span></span>
      <div class="grid justify-items-center gap-2.5"><div class="flex gap-1.5">
        <span data-digit class="group/d relative block h-[calc(var(--w)*1.34)] w-(--w) rounded-lg bg-tcd22-low font-tcd22-slab text-[calc(var(--w)*0.92)] font-semibold tabular-nums text-tcd22-ink shadow-[0_8px_18px_-8px_rgb(0_0_0/0.7)] perspective-[420px]"><b class="absolute inset-x-0 top-0 h-1/2 overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card"><i class="grid h-[200%] place-items-center not-italic leading-none">2</i></b><b class="absolute inset-x-0 bottom-0 h-1/2 overflow-hidden rounded-b-lg bg-tcd22-low"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">2</i></b><b class="absolute inset-x-0 top-0 z-30 h-1/2 origin-bottom overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card opacity-0 backface-hidden group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-fall motion-reduce:hidden"><i class="grid h-[200%] place-items-center not-italic leading-none">2</i></b><b class="absolute inset-x-0 bottom-0 z-20 h-1/2 origin-top overflow-hidden rounded-b-lg bg-tcd22-low opacity-0 backface-hidden [transform:rotateX(90deg)] group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-rise motion-reduce:hidden"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">2</i></b><span aria-hidden="true" class="absolute top-1/2 -left-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span><span aria-hidden="true" class="absolute top-1/2 -right-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span></span>
        <span data-digit class="group/d relative block h-[calc(var(--w)*1.34)] w-(--w) rounded-lg bg-tcd22-low font-tcd22-slab text-[calc(var(--w)*0.92)] font-semibold tabular-nums text-tcd22-ink shadow-[0_8px_18px_-8px_rgb(0_0_0/0.7)] perspective-[420px]"><b class="absolute inset-x-0 top-0 h-1/2 overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card"><i class="grid h-[200%] place-items-center not-italic leading-none">4</i></b><b class="absolute inset-x-0 bottom-0 h-1/2 overflow-hidden rounded-b-lg bg-tcd22-low"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">4</i></b><b class="absolute inset-x-0 top-0 z-30 h-1/2 origin-bottom overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card opacity-0 backface-hidden group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-fall motion-reduce:hidden"><i class="grid h-[200%] place-items-center not-italic leading-none">4</i></b><b class="absolute inset-x-0 bottom-0 z-20 h-1/2 origin-top overflow-hidden rounded-b-lg bg-tcd22-low opacity-0 backface-hidden [transform:rotateX(90deg)] group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-rise motion-reduce:hidden"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">4</i></b><span aria-hidden="true" class="absolute top-1/2 -left-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span><span aria-hidden="true" class="absolute top-1/2 -right-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span></span>
      </div><p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-tcd22-mut">minutes</p></div>
      <span aria-hidden="true" class="mt-[calc(var(--w)*0.45)] grid gap-[calc(var(--w)*0.22)]"><span class="size-1.5 rounded-full bg-tcd22-acc"></span><span class="size-1.5 rounded-full bg-tcd22-acc"></span></span>
      <div class="grid justify-items-center gap-2.5"><div class="flex gap-1.5">
        <span data-digit class="group/d relative block h-[calc(var(--w)*1.34)] w-(--w) rounded-lg bg-tcd22-low font-tcd22-slab text-[calc(var(--w)*0.92)] font-semibold tabular-nums text-tcd22-ink shadow-[0_8px_18px_-8px_rgb(0_0_0/0.7)] perspective-[420px]"><b class="absolute inset-x-0 top-0 h-1/2 overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card"><i class="grid h-[200%] place-items-center not-italic leading-none">1</i></b><b class="absolute inset-x-0 bottom-0 h-1/2 overflow-hidden rounded-b-lg bg-tcd22-low"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">1</i></b><b class="absolute inset-x-0 top-0 z-30 h-1/2 origin-bottom overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card opacity-0 backface-hidden group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-fall motion-reduce:hidden"><i class="grid h-[200%] place-items-center not-italic leading-none">1</i></b><b class="absolute inset-x-0 bottom-0 z-20 h-1/2 origin-top overflow-hidden rounded-b-lg bg-tcd22-low opacity-0 backface-hidden [transform:rotateX(90deg)] group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-rise motion-reduce:hidden"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">1</i></b><span aria-hidden="true" class="absolute top-1/2 -left-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span><span aria-hidden="true" class="absolute top-1/2 -right-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span></span>
        <span data-digit class="group/d relative block h-[calc(var(--w)*1.34)] w-(--w) rounded-lg bg-tcd22-low font-tcd22-slab text-[calc(var(--w)*0.92)] font-semibold tabular-nums text-tcd22-acc-ink shadow-[0_8px_18px_-8px_rgb(0_0_0/0.7)] perspective-[420px]"><b class="absolute inset-x-0 top-0 h-1/2 overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card"><i class="grid h-[200%] place-items-center not-italic leading-none">8</i></b><b class="absolute inset-x-0 bottom-0 h-1/2 overflow-hidden rounded-b-lg bg-tcd22-low"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">8</i></b><b class="absolute inset-x-0 top-0 z-30 h-1/2 origin-bottom overflow-hidden rounded-t-lg border-b border-tcd22-ink/30 bg-tcd22-card opacity-0 backface-hidden group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-fall motion-reduce:hidden"><i class="grid h-[200%] place-items-center not-italic leading-none">8</i></b><b class="absolute inset-x-0 bottom-0 z-20 h-1/2 origin-top overflow-hidden rounded-b-lg bg-tcd22-low opacity-0 backface-hidden [transform:rotateX(90deg)] group-data-flip/d:opacity-100 group-data-flip/d:animate-tcd22-rise motion-reduce:hidden"><i class="relative -top-full grid h-[200%] place-items-center not-italic leading-none">8</i></b><span aria-hidden="true" class="absolute top-1/2 -left-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span><span aria-hidden="true" class="absolute top-1/2 -right-0.5 z-40 h-2 w-1 -translate-y-1/2 rounded-sm bg-tcd22-frame"></span></span>
      </div><p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-tcd22-mut">seconds</p></div>
      <span data-sentence class="sr-only"></span>
    </div>

    <div data-done hidden role="status" class="grid justify-items-center gap-3 rounded-2xl border border-tcd22-card/20 px-7 py-6">
      <strong class="font-tcd22-slab text-[clamp(26px,5vw,34px)] font-semibold">Posting closed</strong>
      <span class="text-[14px] text-tcd22-mut">The autumn run is locked. The next press slot opens in eleven days.</span>
      <button type="button" class="min-h-11 cursor-pointer rounded-full border border-tcd22-acc px-5 text-sm font-semibold text-tcd22-acc transition hover:bg-tcd22-acc hover:text-tcd22-page focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd22-acc">Reserve the next slot</button>
    </div>

    <div data-open class="flex flex-wrap items-center justify-center gap-x-5 gap-y-3">
      <p class="text-[13px] text-tcd22-mut tabular-nums">Cut-off <time datetime="" data-time class="font-semibold text-tcd22-card">—</time></p>
      <button type="button" class="min-h-11 cursor-pointer rounded-full bg-tcd22-acc px-5 text-sm font-semibold text-tcd22-page transition hover:brightness-110 active:scale-[0.97] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd22-acc">Upload print files</button>
    </div>
    <output data-live aria-live="polite" class="sr-only"></output>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd22-page: #17120d;
  --color-tcd22-page: oklch(0.18 0.02 55);
  --color-tcd22-glow: #2a2016;
  --color-tcd22-glow: oklch(0.25 0.03 60);
  --color-tcd22-frame: #0f0b08;
  --color-tcd22-frame: oklch(0.14 0.015 55);
  --color-tcd22-card: #f2e3c8;
  --color-tcd22-card: oklch(0.91 0.04 85);
  --color-tcd22-low: #e4d2b4;
  --color-tcd22-low: oklch(0.85 0.045 85);
  --color-tcd22-ink: #211812;
  --color-tcd22-ink: oklch(0.2 0.02 50);
  --color-tcd22-mut: #b09c82;
  --color-tcd22-mut: oklch(0.71 0.04 75);
  --color-tcd22-acc: #e0952f;
  --color-tcd22-acc: oklch(0.74 0.14 70);
  --color-tcd22-acc-ink: #9a5410;
  --color-tcd22-acc-ink: oklch(0.5 0.12 60);
  --font-tcd22-slab: 'Zilla Slab', Rockwell, Georgia, serif;
  --font-tcd22-sans: 'Instrument Sans', system-ui, sans-serif;
  --animate-tcd22-fall: tcd22-fall 0.32s ease-in forwards;
  --animate-tcd22-rise: tcd22-rise 0.32s ease-out 0.32s forwards;

  @keyframes tcd22-fall {
    from {
      transform: rotateX(0deg);
    }

    to {
      transform: rotateX(-90deg);
    }
  }

  @keyframes tcd22-rise {
    from {
      transform: rotateX(90deg);
    }

    to {
      transform: rotateX(0deg);
    }
  }
}

.tcd-22 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-22');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const digits = [...root.querySelectorAll('[data-digit]')], live = q('[data-live]');
  const target = new Date(Date.now() + 6 * 3600e3 + 24 * 60e3 + 18e3);
  let id = 0, seen = null;
  const timers = new Set();
  q('[data-time]').dateTime = target.toISOString();
  q('[data-time]').textContent = target.toLocaleString([], { weekday: 'short', hour: 'numeric', minute: '2-digit' });
  const set = (el, v) => {
    if (el.dataset.v === v) return;
    const prev = el.dataset.v ?? v; el.dataset.v = v;
    const [top, bot, ft, fb] = [...el.querySelectorAll('b > i')];
    ft.textContent = prev; fb.textContent = v; top.textContent = v;
    el.removeAttribute('data-flip'); void el.offsetWidth; el.setAttribute('data-flip', '');
    const t = setTimeout(() => { bot.textContent = v; timers.delete(t); }, 640);
    timers.add(t);
  };
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.floor(ms / 1000);
    const h = Math.floor(s / 3600), m = Math.floor(s / 60) % 60;
    const str = [h, m, s % 60].map((n) => String(n).padStart(2, '0')).join('');
    digits.forEach((el, i) => set(el, str[i]));
    q('[data-sentence]').textContent = h + ' hours ' + m + ' minutes until posting closes';
    const b = ms <= 0 ? 'end' : ms < 600e3 ? 'm10' : ms < 3600e3 ? 'h1' : 'far';
    if (b !== seen) { seen = b; live.textContent = { far: '', h1: 'Under an hour until posting closes.', m10: 'Ten minutes until posting closes.', end: 'Posting is closed for the autumn run.' }[b]; }
    if (ms > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); return; }
    q('[data-clock]').hidden = true; q('[data-open]').hidden = true; q('[data-done]').hidden = false;
  };
  tick();
  root.cleanup = () => { clearTimeout(id); timers.forEach(clearTimeout); };
})();
```
