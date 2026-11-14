---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-virtual-waiting-room-queue-countdown/"
title: "Tailwind Virtual Waiting Room Queue Countdown"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A virtual waiting room for a ticket drop: your place in line as the largest thing on screen, an estimated wait as a range beneath it, and a reassurance line…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Virtual Waiting Room Queue Countdown
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-virtual-waiting-room-queue-countdown/

A virtual waiting room for a ticket drop: your place in line as the largest thing on screen, an estimated wait as a range beneath it, and a reassurance line telling you not to refresh &mdash; the one action that costs a place. New in the port: a track with a you marker, and when it's your turn the page flips via data-turn to a live 10-minute checkout hold countdown instead of a static message.
## HTML
```html
<section class="tcd-15 group/root w-full min-h-svh bg-[linear-gradient(165deg,var(--color-tcd15-a),var(--color-tcd15-b)_62%,var(--color-tcd15-c))] font-tcd15-sans text-tcd15-ink antialiased" aria-labelledby="tcd-15-title">
  <div class="mx-auto grid min-h-svh max-w-[620px] content-center justify-items-center gap-4 px-[clamp(18px,5vw,56px)] py-14 text-center">
    <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-tcd15-mut">Orbit Live · Sable Arena, 14 November</p>
    <h2 id="tcd-15-title" class="text-[clamp(24px,4.6vw,34px)] font-extrabold leading-tight tracking-[-0.02em] group-data-turn/root:hidden">You are in the queue</h2>

    <div role="timer" class="grid w-full justify-items-center gap-1 group-data-turn/root:hidden">
      <p class="text-xs font-bold uppercase tracking-[0.16em] text-tcd15-mut">Position in line</p>
      <p data-pos class="text-[clamp(64px,20vw,132px)] font-black leading-[0.95] tracking-[-0.05em] tabular-nums">#1,247</p>
      <p class="text-[15px] font-semibold">Estimated wait <time datetime="" data-clock>7–9 minutes</time></p>
      <div aria-hidden="true" class="relative mt-5 h-2.5 w-full max-w-[460px] rounded-full bg-tcd15-ink/12">
        <span data-fill class="absolute inset-y-0 left-0 w-(--pos) rounded-full bg-tcd15-ink transition-[width] duration-1000 ease-linear motion-reduce:transition-none [--pos:4%]"></span>
        <span data-mark class="absolute top-1/2 left-(--pos) grid -translate-1/2 place-items-center rounded-full bg-tcd15-acc px-2 py-1 text-[10px] font-extrabold uppercase tracking-[0.08em] text-white shadow-[0_6px_14px_-6px_var(--color-tcd15-acc)] transition-[left] duration-1000 ease-linear motion-reduce:transition-none [--pos:4%]">You</span>
        <span class="absolute -top-6 right-0 text-[10.5px] font-bold uppercase tracking-[0.12em] text-tcd15-mut">Front</span>
      </div>
    </div>

    <div class="mt-3 flex max-w-[480px] items-start gap-3 rounded-2xl border border-tcd15-ink/14 bg-white/45 px-4 py-3.5 text-left supports-[backdrop-filter:blur(1px)]:backdrop-blur-md group-data-turn/root:hidden">
      <svg viewBox="0 0 18 18" width="18" height="18" aria-hidden="true" class="mt-0.5 flex-none text-tcd15-acc"><path d="M9 1.8 2 4.6v4.2c0 3.4 2.9 6.3 7 7.4 4.1-1.1 7-4 7-7.4V4.6L9 1.8Z" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M6.2 8.9 8.4 11l3.6-3.8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      <p class="text-[13.5px] leading-relaxed text-pretty"><strong class="font-bold">Do not refresh or close this tab.</strong> Your place is held here. Refreshing sends you to the back of the line, and there is no way for us to restore it.</p>
    </div>

    <div role="status" class="hidden w-full max-w-[480px] justify-items-center gap-3 rounded-3xl bg-tcd15-card p-[clamp(22px,5vw,34px)] shadow-[0_30px_60px_-30px_rgb(51_23_10/0.6)] transition duration-500 starting:scale-95 starting:opacity-0 group-data-turn/root:grid">
      <span aria-hidden="true" class="grid size-12 place-items-center rounded-full bg-tcd15-acc text-white"><svg viewBox="0 0 20 20" width="22" height="22"><path d="M4 10.5 8.2 14.5 16 5.8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      <p class="text-[clamp(24px,5vw,30px)] font-extrabold tracking-[-0.02em]">It's your turn</p>
      <p class="text-[14px] leading-relaxed text-tcd15-mut text-pretty">Choose seats and check out before the hold releases.</p>
      <p role="timer" class="flex items-baseline gap-2 text-sm font-semibold text-tcd15-mut">Hold releases in <time datetime="" data-hold class="text-[28px] font-black tracking-[-0.02em] tabular-nums text-tcd15-ink">10:00</time></p>
      <button type="button" class="mt-1 min-h-12 w-full cursor-pointer rounded-xl bg-tcd15-ink px-5 font-bold text-white transition hover:bg-tcd15-ink/90 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd15-acc">Enter seat selection</button>
    </div>

    <p class="mt-2 max-w-[52ch] text-[12.5px] leading-relaxed text-tcd15-mut text-pretty">A shared queue is a real-time event: one person's window cannot be extended without reordering everyone else. If this tab sits idle for 30 minutes the place is released.</p>
    <output data-live aria-live="polite" class="sr-only"></output>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd15-a: #ff8a4c;
  --color-tcd15-a: oklch(0.76 0.16 48);
  --color-tcd15-b: #ffd4a3;
  --color-tcd15-b: oklch(0.89 0.08 62);
  --color-tcd15-c: #fff3e4;
  --color-tcd15-c: oklch(0.97 0.025 70);
  --color-tcd15-card: #fffaf4;
  --color-tcd15-card: oklch(0.99 0.01 70);
  --color-tcd15-ink: #33170a;
  --color-tcd15-ink: oklch(0.28 0.07 44);
  --color-tcd15-mut: #6e3d22;
  --color-tcd15-mut: oklch(0.43 0.08 46);
  --color-tcd15-acc: #d13d18;
  --color-tcd15-acc: oklch(0.54 0.19 32);
  --font-tcd15-sans: 'Archivo', system-ui, sans-serif;
}

.tcd-15 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-15');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const pos = q('[data-pos]'), clock = q('[data-clock]'), fill = q('[data-fill]'), mark = q('[data-mark]');
  const hold = q('[data-hold]'), live = q('[data-live]');
  const START = 1247, RATE = 9, HOLD = 10 * 60e3;
  const t0 = Date.now(), target = t0 + Math.ceil(START / RATE) * 1000;
  let id = 0, seen = Math.ceil(START / 1000), holdEnd = 0, holdSeen = null;
  const pad = (n) => String(n).padStart(2, '0');
  const holdTick = () => {
    const ms = Math.max(0, holdEnd - Date.now()), s = Math.ceil(ms / 1000);
    hold.textContent = Math.floor(s / 60) + ':' + pad(s % 60);
    hold.dateTime = new Date(holdEnd).toISOString();
    const b = ms <= 0 ? 'end' : ms <= 60e3 ? 'm1' : ms <= 300e3 ? 'm5' : 'far';
    if (b !== holdSeen) { holdSeen = b; live.textContent = { far: '', m5: 'Five minutes left on your seat hold.', m1: 'One minute left on your seat hold.', end: 'Your seat hold has been released.' }[b]; }
    if (ms > 0) id = setTimeout(holdTick, 1000 - (Date.now() % 1000));
  };
  const tick = () => {
    const left = Math.max(0, START - Math.floor((Date.now() - t0) / 1000) * RATE);
    const secs = Math.ceil(left / RATE), lo = Math.floor(secs / 60), hi = lo + Math.max(1, Math.round(lo * 0.25));
    pos.textContent = '#' + left.toLocaleString();
    clock.dateTime = new Date(target).toISOString();
    clock.textContent = lo < 1 ? 'under a minute' : lo + '–' + hi + ' minutes';
    const p = ((1 - left / START) * 92 + 4).toFixed(1) + '%';
    fill.style.setProperty('--pos', p); mark.style.setProperty('--pos', p);
    const band = Math.ceil(left / 1000);
    if (band !== seen) { seen = band; live.textContent = 'Queue position now about ' + left.toLocaleString() + '.'; }
    if (left > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); return; }
    root.setAttribute('data-turn', '');
    live.textContent = 'It is your turn. You have ten minutes to choose seats and check out.';
    holdEnd = Date.now() + HOLD; holdTick();
  };
  tick();
  root.cleanup = () => clearTimeout(id);
})();
```
