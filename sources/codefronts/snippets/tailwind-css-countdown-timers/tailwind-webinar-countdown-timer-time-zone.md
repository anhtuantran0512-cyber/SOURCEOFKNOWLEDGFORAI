---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-webinar-countdown-timer-time-zone/"
title: "Tailwind Webinar Countdown Timer with Time Zone Display"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A registration card that counts down to a live session and states the start time twice &mdash; in the visitor's own zone (resolved from the browser) and in…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Webinar Countdown Timer with Time Zone Display
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-webinar-countdown-timer-time-zone/

A registration card that counts down to a live session and states the start time twice &mdash; in the visitor's own zone (resolved from the browser) and in the host's &mdash; from one UTC instant. New in the port: Add to calendar downloads a real .ics file, Save my seat has a registered state, and a seat meter shows scarcity honestly.
## HTML
```html
<section class="tcd-10 w-full min-h-svh grid place-items-center bg-tcd10-page bg-[linear-gradient(var(--color-tcd10-grid)_1px,transparent_1px),linear-gradient(90deg,var(--color-tcd10-grid)_1px,transparent_1px)] bg-[length:32px_32px] px-4 py-12 font-tcd10-sans text-tcd10-ink antialiased" aria-labelledby="tcd-10-title">
  <article data-card class="group/card w-full max-w-[640px] rounded-2xl border border-tcd10-rule bg-tcd10-card p-[clamp(20px,4.4vw,36px)] shadow-tcd10-card">
    <div class="mb-5 flex flex-wrap items-center gap-x-3 gap-y-2">
      <span class="inline-flex items-center gap-1.5 rounded-full bg-tcd10-soft px-2.5 py-1.5 text-[11px] font-semibold tracking-[0.04em] text-tcd10-acc"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcd10-acc"></span>Live session</span>
      <span class="flex min-w-[180px] flex-1 items-center gap-2.5 text-xs text-tcd10-mut"><span class="whitespace-nowrap"><b data-left class="font-semibold text-tcd10-ink">62</b> of 300 seats left</span><span aria-hidden="true" class="h-1 flex-1 overflow-hidden rounded-full bg-tcd10-rule"><span data-meter class="block h-full w-[79%] rounded-full bg-tcd10-acc transition-[width] duration-500"></span></span></span>
    </div>

    <h2 id="tcd-10-title" class="mb-2 text-[clamp(22px,4vw,30px)] font-semibold leading-[1.15] tracking-[-0.02em] text-balance">Shipping schema changes without downtime</h2>
    <p class="mb-6 flex flex-wrap items-center gap-2 text-[13.5px] text-tcd10-mut"><span aria-hidden="true" class="grid size-6 place-items-center rounded-full bg-tcd10-ink text-[10px] font-semibold text-white">AC</span>Alex Chen · Staff engineer at Talon · 45 minutes, live Q&amp;A after</p>

    <div role="timer" class="rounded-xl border border-tcd10-rule bg-tcd10-page/60 p-4">
      <time datetime="" data-clock aria-hidden="true" class="grid grid-cols-4 gap-2 font-tcd10-mono tabular-nums">
        <span class="grid justify-items-center gap-1 rounded-lg bg-tcd10-card py-3 shadow-[0_1px_0_var(--color-tcd10-rule)]"><b data-d class="text-[clamp(26px,7vw,40px)] font-semibold leading-none tracking-[-0.03em]">01</b><i class="font-tcd10-sans text-[10px] font-semibold not-italic uppercase tracking-[0.14em] text-tcd10-mut">days</i></span>
        <span class="grid justify-items-center gap-1 rounded-lg bg-tcd10-card py-3 shadow-[0_1px_0_var(--color-tcd10-rule)]"><b data-h class="text-[clamp(26px,7vw,40px)] font-semibold leading-none tracking-[-0.03em]">04</b><i class="font-tcd10-sans text-[10px] font-semibold not-italic uppercase tracking-[0.14em] text-tcd10-mut">hrs</i></span>
        <span class="grid justify-items-center gap-1 rounded-lg bg-tcd10-card py-3 shadow-[0_1px_0_var(--color-tcd10-rule)]"><b data-m class="text-[clamp(26px,7vw,40px)] font-semibold leading-none tracking-[-0.03em]">36</b><i class="font-tcd10-sans text-[10px] font-semibold not-italic uppercase tracking-[0.14em] text-tcd10-mut">min</i></span>
        <span class="grid justify-items-center gap-1 rounded-lg bg-tcd10-card py-3 shadow-[0_1px_0_var(--color-tcd10-rule)]"><b data-s class="text-[clamp(26px,7vw,40px)] font-semibold leading-none tracking-[-0.03em] text-tcd10-acc">12</b><i class="font-tcd10-sans text-[10px] font-semibold not-italic uppercase tracking-[0.14em] text-tcd10-mut">sec</i></span>
      </time>
      <p data-rel class="mt-3 text-center text-[13px] font-medium text-tcd10-mut">starts in about a day</p>
    </div>

    <dl class="mt-4 grid gap-2 sm:grid-cols-2">
      <div class="rounded-xl border border-tcd10-acc/30 bg-tcd10-soft px-4 py-3"><dt class="text-[11px] font-semibold uppercase tracking-[0.12em] text-tcd10-acc">Your time</dt><dd data-local class="mt-1 text-[13.5px] font-medium [overflow-wrap:anywhere]">—</dd></div>
      <div class="rounded-xl border border-tcd10-rule px-4 py-3"><dt class="text-[11px] font-semibold uppercase tracking-[0.12em] text-tcd10-mut">Host time</dt><dd data-host class="mt-1 text-[13.5px] font-medium [overflow-wrap:anywhere]">—</dd></div>
    </dl>

    <div class="mt-6 flex flex-wrap gap-2.5">
      <button type="button" data-save class="inline-flex min-h-11 flex-[1_1_160px] cursor-pointer items-center justify-center gap-2 rounded-xl bg-tcd10-acc px-5 text-sm font-semibold text-white transition hover:brightness-110 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd10-ink group-data-registered/card:bg-tcd10-ok">
        <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true" class="hidden group-data-registered/card:block"><path d="M3 8.4 6.4 11.5 13 4.8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="group-data-registered/card:hidden">Save my seat</span><span class="hidden group-data-registered/card:inline">You're registered</span>
      </button>
      <button type="button" data-ics class="inline-flex min-h-11 flex-[1_1_160px] cursor-pointer items-center justify-center gap-2 rounded-xl border border-tcd10-rule px-5 text-sm font-semibold transition hover:border-tcd10-ink/30 hover:bg-tcd10-page active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd10-acc">
        <svg viewBox="0 0 18 18" width="15" height="15" aria-hidden="true"><rect x="2.5" y="4" width="13" height="11.5" rx="2" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M2.5 7.6h13M6.2 2.6v2.6M11.8 2.6v2.6" stroke="currentColor" stroke-width="1.4"/></svg>
        Add to calendar (.ics)
      </button>
    </div>

    <p class="mt-5 border-t border-tcd10-rule pt-4 text-[12.5px] leading-relaxed text-tcd10-mut text-pretty">Stored as one UTC instant and rendered twice. A wall-clock string such as <code class="rounded bg-tcd10-page px-1 py-0.5 font-tcd10-mono text-[11.5px] text-tcd10-ink">2026-09-01 14:00</code> would be parsed in each visitor's own zone and shift the session by hours.</p>
    <output data-live aria-live="polite" class="sr-only"></output>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd10-page: #f4f5f7;
  --color-tcd10-page: oklch(0.965 0.004 265);
  --color-tcd10-grid: #e9ebef;
  --color-tcd10-grid: oklch(0.93 0.005 265);
  --color-tcd10-card: #ffffff;
  --color-tcd10-card: oklch(1 0 0);
  --color-tcd10-ink: #17191f;
  --color-tcd10-ink: oklch(0.22 0.012 265);
  --color-tcd10-mut: #5a5e66;
  --color-tcd10-mut: oklch(0.48 0.012 265);
  --color-tcd10-rule: #e3e5e9;
  --color-tcd10-rule: oklch(0.91 0.006 265);
  --color-tcd10-acc: #2563d8;
  --color-tcd10-acc: oklch(0.52 0.19 262);
  --color-tcd10-soft: #eef3fd;
  --color-tcd10-soft: oklch(0.96 0.026 262);
  --color-tcd10-ok: #1f7a4d;
  --color-tcd10-ok: oklch(0.5 0.12 155);
  --font-tcd10-sans: 'Geist', system-ui, sans-serif;
  --font-tcd10-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tcd10-card: 0 1px 2px rgb(23 25 31 / 0.04), 0 24px 50px -32px rgb(23 25 31 / 0.4);
}

.tcd-10 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-10');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const HOST = 'Europe/Berlin', SEATS = 300, card = q('[data-card]'), clock = q('[data-clock]'), live = q('[data-live]');
  const target = new Date(Date.now() + 28 * 3600e3 + 36 * 60e3 + 12e3);
  const zone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  const fmt = (tz) => new Intl.DateTimeFormat([], { weekday: 'short', day: 'numeric', month: 'short', hour: 'numeric', minute: '2-digit', timeZone: tz, timeZoneName: 'short' }).format(target);
  const rel = new Intl.RelativeTimeFormat([], { numeric: 'auto' });
  const pad = (n) => String(n).padStart(2, '0');
  let left = 62, seen = null, id = 0;
  clock.dateTime = target.toISOString();
  q('[data-local]').textContent = fmt(zone) + ' · ' + zone.replace(/_/g, ' ');
  q('[data-host]').textContent = fmt(HOST) + ' · ' + HOST;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.floor(ms / 1000);
    q('[data-d]').textContent = pad(Math.floor(s / 86400));
    q('[data-h]').textContent = pad(Math.floor(s / 3600) % 24);
    q('[data-m]').textContent = pad(Math.floor(s / 60) % 60);
    q('[data-s]').textContent = pad(s % 60);
    q('[data-rel]').textContent = ms <= 0 ? 'The room is open — join now' : s >= 86400 ? 'starts ' + rel.format(Math.round(s / 86400), 'day') : s >= 3600 ? 'starts ' + rel.format(Math.round(s / 3600), 'hour') : 'starts ' + rel.format(Math.ceil(s / 60), 'minute');
    const b = ms <= 0 ? 'end' : ms < 600e3 ? 'm10' : ms < 3600e3 ? 'h1' : ms < 86400e3 ? 'd1' : 'far';
    if (b !== seen) { seen = b; live.textContent = { far: '', d1: 'Session starts within a day.', h1: 'Session starts within the hour.', m10: 'Session starts in ten minutes.', end: 'The session room is open.' }[b]; }
    if (ms > 0) id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  q('[data-save]').addEventListener('click', () => {
    if (card.hasAttribute('data-registered')) return;
    card.setAttribute('data-registered', ''); left -= 1;
    q('[data-left]').textContent = left;
    q('[data-meter]').style.width = ((SEATS - left) / SEATS * 100).toFixed(1) + '%';
    live.textContent = 'You are registered. A confirmation is on its way.';
  });
  q('[data-ics]').addEventListener('click', () => {
    const z = (d) => d.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, '');
    const end = new Date(target.getTime() + 45 * 60e3);
    const ics = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Talon//Webinar//EN', 'BEGIN:VEVENT', 'UID:' + target.getTime() + '@talon.dev', 'DTSTAMP:' + z(new Date()), 'DTSTART:' + z(target), 'DTEND:' + z(end), 'SUMMARY:Shipping schema changes without downtime', 'DESCRIPTION:Live session with Alex Chen', 'END:VEVENT', 'END:VCALENDAR'].join('\r\n');
    const url = URL.createObjectURL(new Blob([ics], { type: 'text/calendar' }));
    const a = Object.assign(document.createElement('a'), { href: url, download: 'talon-webinar.ics' });
    document.body.append(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    live.textContent = 'Calendar file downloaded.';
  });
  tick();
  root.cleanup = () => clearTimeout(id);
})();
```
