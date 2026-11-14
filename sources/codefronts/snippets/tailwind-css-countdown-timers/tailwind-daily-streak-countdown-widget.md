---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-daily-streak-countdown-widget/"
title: "Tailwind Daily Streak Countdown Widget for Habit Apps"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A habit-app streak widget counting down to local midnight, with a flame whose glow dims as the day runs out."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Daily Streak Countdown Widget for Habit Apps
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-daily-streak-countdown-widget/

A habit-app streak widget counting down to local midnight, with a flame whose glow dims as the day runs out. It builds tomorrow as a date at hour zero &mdash; not now + 24h &mdash; which survives daylight saving. New in the port: a working Log today's practice that bumps the streak and flips the card to a done state via data-done, a seven-day strip, and a Use a freeze counter.
## HTML
```html
<section class="tcd-16 w-full min-h-svh grid place-items-center bg-tcd16-page bg-[radial-gradient(50%_40%_at_50%_30%,var(--color-tcd16-glow),transparent_70%)] px-4 py-12 font-tcd16-sans text-tcd16-ink antialiased" aria-labelledby="tcd-16-title">
  <article data-card style="--glow: 1" class="group/card w-full max-w-[420px] rounded-[28px] border border-tcd16-rule bg-tcd16-card p-[clamp(22px,5vw,32px)] text-center shadow-[0_0_80px_-30px_var(--color-tcd16-acc)]">
    <header class="flex flex-wrap items-center justify-between gap-2">
      <p id="tcd-16-title" class="text-xs font-extrabold uppercase tracking-[0.12em] text-tcd16-mut">Ranger · daily practice</p>
      <span class="hidden rounded-full bg-tcd16-acc/15 px-2.5 py-1 text-[11px] font-extrabold text-tcd16-acc group-data-risk/card:inline-block group-data-done/card:hidden">Streak at risk</span>
      <span class="hidden rounded-full bg-tcd16-ok/15 px-2.5 py-1 text-[11px] font-extrabold text-tcd16-ok group-data-done/card:inline-block">Done for today ✓</span>
    </header>

    <div class="my-5 grid justify-items-center gap-2">
      <span aria-hidden="true" class="text-tcd16-acc opacity-(--glow) drop-shadow-[0_0_24px_var(--color-tcd16-acc)] transition-[opacity,transform] duration-700 group-data-done/card:scale-110 group-data-done/card:opacity-100">
        <svg viewBox="0 0 48 64" width="72" height="96"><path d="M24 2c8 11 4 15 9 21 6 7 9 12 9 20 0 10-8 19-18 19S6 53 6 43c0-7 3-12 8-17 4-4 6-8 5-14 2 3 4 5 5 8 1-6 0-12 0-18Z" fill="currentColor"/><path d="M24 26c3 5 1 7 4 11 3 3 4 6 4 10 0 6-4 11-8 11s-8-5-8-11c0-4 2-7 4-10 2-2 3-5 4-11Z" fill="rgba(255,255,255,0.45)"/></svg>
      </span>
      <p class="grid"><b data-streak class="text-[64px] font-black leading-none tracking-[-0.04em] tabular-nums">34</b><i class="text-sm font-bold not-italic text-tcd16-mut">day streak</i></p>
    </div>

    <ol aria-label="This week" data-week class="mb-5 grid grid-cols-7 gap-1.5">
      <li class="grid justify-items-center gap-1 text-[10.5px] font-bold text-tcd16-mut"><span class="size-7 rounded-full bg-tcd16-rule data-[day=done]:bg-tcd16-acc" data-day="done"></span>M</li>
      <li class="grid justify-items-center gap-1 text-[10.5px] font-bold text-tcd16-mut"><span class="size-7 rounded-full bg-tcd16-rule data-[day=done]:bg-tcd16-acc" data-day="done"></span>T</li>
      <li class="grid justify-items-center gap-1 text-[10.5px] font-bold text-tcd16-mut"><span class="size-7 rounded-full bg-tcd16-rule data-[day=done]:bg-tcd16-acc" data-day="done"></span>W</li>
      <li class="grid justify-items-center gap-1 text-[10.5px] font-bold text-tcd16-mut"><span class="size-7 rounded-full bg-tcd16-rule data-[day=done]:bg-tcd16-acc" data-day="done"></span>T</li>
      <li class="grid justify-items-center gap-1 text-[10.5px] font-bold text-tcd16-ink"><span data-today class="size-7 rounded-full border-2 border-dashed border-tcd16-acc data-[day=done]:border-solid data-[day=done]:bg-tcd16-acc"></span>Today</li>
      <li class="grid justify-items-center gap-1 text-[10.5px] font-bold text-tcd16-mut/60"><span class="size-7 rounded-full border border-tcd16-rule"></span>S</li>
      <li class="grid justify-items-center gap-1 text-[10.5px] font-bold text-tcd16-mut/60"><span class="size-7 rounded-full border border-tcd16-rule"></span>S</li>
    </ol>

    <div role="timer" class="rounded-2xl bg-tcd16-sunk px-4 py-4">
      <p class="text-xs font-extrabold uppercase tracking-[0.12em] text-tcd16-mut"><span class="group-data-done/card:hidden">Resets in</span><span class="hidden group-data-done/card:inline">Next streak day starts in</span></p>
      <time datetime="" data-clock class="mt-1 block text-[clamp(36px,10vw,46px)] font-black leading-none tracking-[-0.03em] tabular-nums group-data-risk/card:text-tcd16-acc group-data-done/card:text-tcd16-ink">6:42:11</time>
      <p data-zone class="mt-1.5 text-xs font-semibold text-tcd16-mut">at midnight, local time</p>
    </div>

    <div class="mt-5 grid gap-2.5">
      <button type="button" data-log class="min-h-12 cursor-pointer rounded-2xl bg-tcd16-acc px-4 text-[15px] font-extrabold text-tcd16-page shadow-[0_10px_24px_-10px_var(--color-tcd16-acc)] transition hover:brightness-110 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd16-ink disabled:cursor-default disabled:bg-tcd16-ok disabled:shadow-none">Log today's practice</button>
      <button type="button" data-freeze class="min-h-11 cursor-pointer rounded-2xl border border-tcd16-rule px-4 text-sm font-bold text-tcd16-ink transition hover:bg-tcd16-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd16-acc disabled:cursor-not-allowed disabled:opacity-50 group-data-done/card:hidden">Use a freeze · <span data-freezes>2</span> left</button>
    </div>

    <p class="mt-5 text-[12px] leading-relaxed text-tcd16-mut text-pretty">Tomorrow is built as a date at hour zero, not as now plus 24 hours — the second form is an hour wrong on both daylight-saving transitions and quietly breaks streaks twice a year.</p>
    <output data-live aria-live="polite" class="sr-only"></output>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd16-page: #17130f;
  --color-tcd16-page: oklch(0.18 0.016 60);
  --color-tcd16-glow: #2c2013;
  --color-tcd16-glow: oklch(0.26 0.04 65);
  --color-tcd16-card: #201a15;
  --color-tcd16-card: oklch(0.23 0.02 60);
  --color-tcd16-sunk: #282019;
  --color-tcd16-sunk: oklch(0.26 0.022 60);
  --color-tcd16-ink: #f7efe4;
  --color-tcd16-ink: oklch(0.95 0.02 75);
  --color-tcd16-mut: #b29f8a;
  --color-tcd16-mut: oklch(0.74 0.04 65);
  --color-tcd16-rule: #362c24;
  --color-tcd16-rule: oklch(0.33 0.022 60);
  --color-tcd16-acc: #ff9a2e;
  --color-tcd16-acc: oklch(0.76 0.17 62);
  --color-tcd16-ok: #6fd391;
  --color-tcd16-ok: oklch(0.8 0.14 152);
  --font-tcd16-sans: 'Nunito', ui-rounded, system-ui, sans-serif;
}

.tcd-16 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-16');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const card = q('[data-card]'), clock = q('[data-clock]'), live = q('[data-live]');
  const log = q('[data-log]'), freeze = q('[data-freeze]');
  const zone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  q('[data-zone]').textContent = 'at midnight · ' + zone.replace(/_/g, ' ');
  const nextMidnight = () => { const n = new Date(); return new Date(n.getFullYear(), n.getMonth(), n.getDate() + 1, 0, 0, 0, 0); };
  let target = nextMidnight(), id = 0, seen = null, streak = 34, freezes = 2;
  const pad = (n) => String(n).padStart(2, '0');
  const tick = () => {
    let ms = target - Date.now();
    if (ms <= 0) { target = nextMidnight(); ms = target - Date.now(); seen = null; card.removeAttribute('data-done'); log.disabled = false; log.textContent = "Log today's practice"; q('[data-today]').removeAttribute('data-day'); }
    const s = Math.floor(ms / 1000), h = Math.floor(s / 3600);
    clock.textContent = h + ':' + pad(Math.floor(s / 60) % 60) + ':' + pad(s % 60);
    clock.dateTime = target.toISOString();
    card.style.setProperty('--glow', (0.35 + 0.65 * Math.min(1, ms / 864e5)).toFixed(3));
    card.toggleAttribute('data-risk', ms <= 6 * 3600e3);
    const b = ms < 600e3 ? 'm10' : ms < 3600e3 ? 'h1' : ms < 6 * 3600e3 ? 'h6' : 'far';
    if (b !== seen) { seen = b; if (!card.hasAttribute('data-done')) live.textContent = { far: '', h6: 'Six hours left to keep your streak.', h1: 'One hour left to keep your streak.', m10: 'Ten minutes left to keep your streak.' }[b]; }
    id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  const complete = (msg) => {
    card.setAttribute('data-done', ''); streak += 1;
    q('[data-streak]').textContent = streak; q('[data-today]').dataset.day = 'done';
    log.disabled = true; log.textContent = 'Practice logged ✓';
    live.textContent = msg + ' Streak is now ' + streak + ' days.';
  };
  log.addEventListener('click', () => { if (!card.hasAttribute('data-done')) complete('Practice logged.'); });
  freeze.addEventListener('click', () => {
    if (freezes <= 0 || card.hasAttribute('data-done')) return;
    freezes -= 1; q('[data-freezes]').textContent = freezes; if (!freezes) freeze.disabled = true;
    complete('Freeze used.');
  });
  tick();
  root.cleanup = () => clearTimeout(id);
})();
```
