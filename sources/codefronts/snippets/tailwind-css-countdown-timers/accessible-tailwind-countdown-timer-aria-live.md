---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/accessible-tailwind-countdown-timer-aria-live/"
title: "Accessible Tailwind CSS Countdown Timer with ARIA Live Region"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "The reference accessible countdown, rebuilt in utilities: a <time datetime> carries the machine-readable deadline, role=\"timer\" marks the display, and a…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind CSS Countdown Timer with ARIA Live Region
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/accessible-tailwind-countdown-timer-aria-live/

The reference accessible countdown, rebuilt in utilities: a <time datetime> carries the machine-readable deadline, role="timer" marks the display, and a polite live region speaks only at the hour, ten-minute, one-minute and expiry boundaries. New in the port: a visible announcement-band rail driven by one data-band attribute and group-data-[band=…]/root: variants, so you can watch exactly when the screen reader will talk.
## HTML
```html
<section class="tcd-01 group/root w-full min-h-svh bg-tcd01-page bg-[radial-gradient(110%_80%_at_0%_0%,var(--color-tcd01-glow),transparent_60%)] font-tcd01-sans text-tcd01-ink antialiased" data-band="far" aria-labelledby="tcd-01-title">
  <div class="mx-auto grid min-h-svh max-w-[1040px] grid-cols-1 content-center gap-6 px-[clamp(20px,5vw,56px)] py-14 min-[900px]:grid-cols-[minmax(0,1.4fr)_minmax(0,1fr)] min-[900px]:items-start">
    <article class="min-w-0 rounded-2xl border border-tcd01-rule bg-tcd01-card p-[clamp(22px,4vw,40px)] shadow-tcd01-card transition duration-700 starting:translate-y-3 starting:opacity-0">
      <p class="mb-4 flex items-center gap-2.5 text-[11px] font-semibold uppercase tracking-[0.16em] text-tcd01-acc"><span aria-hidden="true" class="h-px w-7 bg-tcd01-acc"></span>Reference implementation</p>
      <h2 id="tcd-01-title" class="mb-2.5 font-tcd01-serif text-[clamp(28px,4.4vw,42px)] font-normal leading-[1.08] tracking-[-0.015em] text-balance">Enrollment for Cohort 12 closes</h2>
      <p class="mb-7 max-w-[46ch] text-[15px] leading-relaxed text-tcd01-mut text-pretty">Meridian reviews applications in the order they arrive. The window below is the real cut-off, not a rolling banner.</p>

      <div role="timer" aria-describedby="tcd-01-hint" class="border-y border-tcd01-rule py-5">
        <time id="tcd-01-time" datetime="" aria-hidden="true" class="flex items-start gap-[clamp(6px,1.8vw,14px)] tabular-nums">
          <span class="grid min-w-0 justify-items-center gap-2"><b data-h class="font-tcd01-serif text-[clamp(40px,11vw,68px)] font-normal leading-[0.92] tracking-[-0.03em]">02</b><i class="text-[10px] font-semibold not-italic uppercase tracking-[0.14em] text-tcd01-mut">hours</i></span>
          <span class="pt-0.5 font-tcd01-serif text-[clamp(30px,8vw,48px)] leading-none text-tcd01-sep">:</span>
          <span class="grid min-w-0 justify-items-center gap-2"><b data-m class="font-tcd01-serif text-[clamp(40px,11vw,68px)] font-normal leading-[0.92] tracking-[-0.03em]">14</b><i class="text-[10px] font-semibold not-italic uppercase tracking-[0.14em] text-tcd01-mut">minutes</i></span>
          <span class="pt-0.5 font-tcd01-serif text-[clamp(30px,8vw,48px)] leading-none text-tcd01-sep">:</span>
          <span class="grid min-w-0 justify-items-center gap-2"><b data-s class="font-tcd01-serif text-[clamp(40px,11vw,68px)] font-normal leading-[0.92] tracking-[-0.03em] text-tcd01-acc">09</b><i class="text-[10px] font-semibold not-italic uppercase tracking-[0.14em] text-tcd01-mut">seconds</i></span>
        </time>
        <span data-sentence class="sr-only">2 hours 14 minutes remaining</span>
      </div>

      <div aria-hidden="true" class="mt-4">
        <ol class="grid grid-cols-5 gap-1.5 font-tcd01-mono text-[10.5px] font-semibold">
          <li class="rounded-md bg-tcd01-chip px-1 py-1.5 text-center text-tcd01-mut transition-colors group-data-[band=far]/root:bg-tcd01-ink group-data-[band=far]/root:text-tcd01-card">&gt; 1h</li>
          <li class="rounded-md bg-tcd01-chip px-1 py-1.5 text-center text-tcd01-mut transition-colors group-data-[band=h1]/root:bg-tcd01-acc group-data-[band=h1]/root:text-white">&lt; 1h</li>
          <li class="rounded-md bg-tcd01-chip px-1 py-1.5 text-center text-tcd01-mut transition-colors group-data-[band=m10]/root:bg-tcd01-acc group-data-[band=m10]/root:text-white">&lt; 10m</li>
          <li class="rounded-md bg-tcd01-chip px-1 py-1.5 text-center text-tcd01-mut transition-colors group-data-[band=m1]/root:bg-tcd01-acc group-data-[band=m1]/root:text-white">&lt; 1m</li>
          <li class="rounded-md bg-tcd01-chip px-1 py-1.5 text-center text-tcd01-mut transition-colors group-data-[band=end]/root:bg-tcd01-acc group-data-[band=end]/root:text-white">closed</li>
        </ol>
        <p class="mt-2 text-[11.5px] text-tcd01-mut">Announcement bands &mdash; the live region speaks only when the highlight moves.</p>
      </div>

      <p id="tcd-01-hint" class="mt-5 text-[13px] text-tcd01-mut">Closes <span data-local class="font-semibold text-tcd01-ink">tonight</span> · applications reviewed within two working days</p>
      <output data-live aria-live="polite" class="mt-2.5 block min-h-[1.2em] w-fit text-[13px] font-medium text-tcd01-acc data-expired:rounded-md data-expired:bg-tcd01-chip data-expired:px-2.5 data-expired:py-1"></output>

      <div class="mt-6 flex flex-wrap gap-2.5">
        <button type="button" class="inline-flex min-h-11 cursor-pointer items-center rounded-lg bg-tcd01-ink px-5 text-sm font-semibold text-tcd01-card transition hover:bg-tcd01-ink/85 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd01-acc">Start application</button>
        <button type="button" class="inline-flex min-h-11 cursor-pointer items-center rounded-lg border border-tcd01-rule px-5 text-sm font-semibold transition hover:border-tcd01-ink/40 hover:bg-tcd01-chip active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd01-acc">Email me the deadline</button>
      </div>
    </article>

    <aside aria-label="How this markup is annotated" class="min-w-0 rounded-2xl border border-tcd01-rule bg-tcd01-chip/70 p-[clamp(18px,3vw,28px)] transition delay-150 duration-700 starting:translate-y-3 starting:opacity-0">
      <h3 class="mb-4 text-[13px] font-semibold tracking-[0.02em]">What each attribute is doing</h3>
      <dl class="grid gap-3.5">
        <div class="grid gap-1 border-b border-tcd01-rule pb-3.5"><dt class="font-tcd01-mono text-xs font-semibold text-tcd01-acc">&lt;time datetime&gt;</dt><dd class="text-[12.5px] leading-relaxed text-tcd01-mut text-pretty">Machine-readable target in the DOM. Written from a real Date at load so a copied demo never renders expired.</dd></div>
        <div class="grid gap-1 border-b border-tcd01-rule pb-3.5"><dt class="font-tcd01-mono text-xs font-semibold text-tcd01-acc">role="timer"</dt><dd class="text-[12.5px] leading-relaxed text-tcd01-mut text-pretty">Names the region as a live countdown so assistive tech exposes it as one thing, not three numbers.</dd></div>
        <div class="grid gap-1 border-b border-tcd01-rule pb-3.5"><dt class="font-tcd01-mono text-xs font-semibold text-tcd01-acc">aria-hidden + sr-only</dt><dd class="text-[12.5px] leading-relaxed text-tcd01-mut text-pretty">"02:14:09" read aloud is noise. The digits are hidden and a full sentence is provided instead.</dd></div>
        <div class="grid gap-1"><dt class="font-tcd01-mono text-xs font-semibold text-tcd01-acc">aria-live="polite"</dt><dd class="text-[12.5px] leading-relaxed text-tcd01-mut text-pretty">Fires at 60 min, 10 min, 1 min and expiry only &mdash; the rail on the left shows which band is live.</dd></div>
      </dl>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd01-page: #f7f5f0;
  --color-tcd01-page: oklch(0.97 0.008 85);
  --color-tcd01-glow: #fffaf0;
  --color-tcd01-glow: oklch(0.99 0.012 85);
  --color-tcd01-card: #ffffff;
  --color-tcd01-card: oklch(1 0 0);
  --color-tcd01-ink: #16150f;
  --color-tcd01-ink: oklch(0.19 0.012 70);
  --color-tcd01-mut: #5f5b51;
  --color-tcd01-mut: oklch(0.46 0.014 75);
  --color-tcd01-rule: #e2ded3;
  --color-tcd01-rule: oklch(0.9 0.012 80);
  --color-tcd01-sep: #c9c3b4;
  --color-tcd01-sep: oklch(0.82 0.016 80);
  --color-tcd01-chip: #f1ece1;
  --color-tcd01-chip: oklch(0.94 0.014 82);
  --color-tcd01-acc: #8a2b1f;
  --color-tcd01-acc: oklch(0.43 0.14 30);
  --font-tcd01-serif: 'Newsreader', Georgia, serif;
  --font-tcd01-sans: 'Geist', system-ui, sans-serif;
  --font-tcd01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tcd01-card: 0 1px 2px rgb(22 21 15 / 0.04), 0 28px 56px -32px rgb(22 21 15 / 0.28);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcd-01 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-01');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const el = (s) => root.querySelector(s);
  const time = el('#tcd-01-time'), live = el('[data-live]'), sentence = el('[data-sentence]');
  const target = new Date(Date.now() + 2 * 3600e3 + 14 * 60e3 + 9e3);
  const pad = (n) => String(n).padStart(2, '0');
  time.dateTime = target.toISOString();
  el('[data-local]').textContent = target.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
  const band = (ms) => ms <= 0 ? 'end' : ms < 60e3 ? 'm1' : ms < 600e3 ? 'm10' : ms < 3600e3 ? 'h1' : 'far';
  const say = { far: '', h1: 'Less than one hour left to apply.', m10: 'Ten minutes left to apply.', m1: 'One minute left to apply.', end: 'Enrollment for Cohort 12 is closed.' };
  let seen = null, id = 0;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.floor(ms / 1000);
    const h = Math.floor(s / 3600), m = Math.floor(s / 60) % 60;
    el('[data-h]').textContent = pad(h);
    el('[data-m]').textContent = pad(m);
    el('[data-s]').textContent = pad(s % 60);
    sentence.textContent = ms > 0 ? h + ' hours ' + m + ' minutes remaining' : 'Enrollment closed';
    const b = band(ms);
    if (b !== seen) {
      seen = b;
      root.dataset.band = b;
      live.toggleAttribute('data-expired', b === 'end');
      live.textContent = say[b];
    }
    if (ms > 0) id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  tick();
  root.cleanup = () => clearTimeout(id);
})();
```
