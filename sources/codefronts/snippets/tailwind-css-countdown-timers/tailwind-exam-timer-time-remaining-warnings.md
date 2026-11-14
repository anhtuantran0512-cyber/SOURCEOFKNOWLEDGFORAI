---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-exam-timer-time-remaining-warnings/"
title: "Tailwind Exam Timer with Time Remaining Warnings"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A proctored-test time chip that changes state at 50%, 10% and 2% remaining &mdash; colour, weight, icon and one announcement per boundary &mdash; plus the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Exam Timer with Time Remaining Warnings
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-exam-timer-time-remaining-warnings/

A proctored-test time chip that changes state at 50%, 10% and 2% remaining &mdash; colour, weight, icon and one announcement per boundary &mdash; plus the affordance most exam timers omit: a documented way to add approved time. In the port, every band is a data-band value read by group-data-[band=warn]/chip:, and new preview buttons let you jump straight to each threshold.
## HTML
```html
<section class="tcd-12 w-full min-h-svh bg-tcd12-page font-tcd12-sans text-tcd12-ink antialiased" aria-labelledby="tcd-12-title">
  <div class="mx-auto grid min-h-svh max-w-[960px] grid-cols-1 content-start gap-6 px-[clamp(16px,4vw,44px)] py-12 lg:grid-cols-[minmax(0,1fr)_284px] lg:content-center">
    <div class="min-w-0">
      <p class="mb-2.5 font-tcd12-display text-[11px] font-semibold uppercase tracking-[0.2em] text-tcd12-mut">Basalt Certification · Section 3 of 4</p>
      <h2 id="tcd-12-title" class="mb-6 font-tcd12-display text-[clamp(24px,4vw,34px)] font-bold leading-tight tracking-[-0.01em] text-balance">Query planning and index selection</h2>
      <ol class="grid gap-5">
        <li class="rounded-xl border border-tcd12-rule p-5"><p class="mb-4 text-[15px] leading-relaxed"><b class="mr-2 font-tcd12-mono text-tcd12-acc">Q7</b>Which access path does the planner choose when the predicate is non-sargable?</p><div class="grid gap-2"><label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-lg border border-tcd12-rule px-3.5 text-sm transition hover:border-tcd12-acc/50 has-checked:border-tcd12-acc has-checked:bg-tcd12-acc/5"><input type="radio" name="tcd12-q7" class="accent-tcd12-acc">Sequential scan</label><label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-lg border border-tcd12-rule px-3.5 text-sm transition hover:border-tcd12-acc/50 has-checked:border-tcd12-acc has-checked:bg-tcd12-acc/5"><input type="radio" name="tcd12-q7" class="accent-tcd12-acc">Index-only scan</label><label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-lg border border-tcd12-rule px-3.5 text-sm transition hover:border-tcd12-acc/50 has-checked:border-tcd12-acc has-checked:bg-tcd12-acc/5"><input type="radio" name="tcd12-q7" class="accent-tcd12-acc">Bitmap heap scan</label></div></li>
        <li class="rounded-xl border border-tcd12-rule p-5"><p class="mb-4 text-[15px] leading-relaxed"><b class="mr-2 font-tcd12-mono text-tcd12-acc">Q8</b>Given a composite index on (tenant_id, created_at), which query cannot use it?</p><div class="grid gap-2"><label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-lg border border-tcd12-rule px-3.5 text-sm transition hover:border-tcd12-acc/50 has-checked:border-tcd12-acc has-checked:bg-tcd12-acc/5"><input type="radio" name="tcd12-q8" class="accent-tcd12-acc">Filter on tenant_id only</label><label class="flex min-h-11 cursor-pointer items-center gap-3 rounded-lg border border-tcd12-rule px-3.5 text-sm transition hover:border-tcd12-acc/50 has-checked:border-tcd12-acc has-checked:bg-tcd12-acc/5"><input type="radio" name="tcd12-q8" class="accent-tcd12-acc">Filter on created_at only</label></div></li>
      </ol>
    </div>

    <aside class="min-w-0 lg:sticky lg:top-6 lg:self-start">
      <div role="timer" data-chip data-band="ok" class="group/chip rounded-2xl border-2 border-tcd12-rule bg-tcd12-page p-4 transition-colors duration-300 data-[band=half]:border-tcd12-acc data-[band=warn]:border-tcd12-warn data-[band=warn]:bg-tcd12-warn/8 data-[band=crit]:border-tcd12-crit data-[band=crit]:bg-tcd12-crit data-[band=crit]:text-white data-[band=end]:border-tcd12-ink data-[band=end]:bg-tcd12-ink data-[band=end]:text-white">
        <div class="flex items-center gap-2.5">
          <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-lg bg-tcd12-acc/10 text-tcd12-acc group-data-[band=warn]/chip:bg-tcd12-warn/15 group-data-[band=warn]/chip:text-tcd12-warn group-data-[band=crit]/chip:bg-white/20 group-data-[band=crit]/chip:text-white group-data-[band=end]/chip:bg-white/15 group-data-[band=end]/chip:text-white">
            <svg viewBox="0 0 18 18" width="16" height="16" class="group-data-[band=warn]/chip:hidden group-data-[band=crit]/chip:hidden"><circle cx="9" cy="9" r="7" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M9 5.4V9l2.6 1.6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            <svg viewBox="0 0 18 18" width="16" height="16" class="hidden group-data-[band=warn]/chip:block group-data-[band=crit]/chip:block group-data-[band=crit]/chip:animate-pulse"><path d="M9 2 1.6 15h14.8L9 2Z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M9 7v3.6M9 12.4v.8" stroke="currentColor" stroke-width="1.6"/></svg>
          </span>
          <time datetime="" data-clock class="font-tcd12-mono text-[30px] font-semibold leading-none tracking-[-0.02em] tabular-nums">44:59</time>
        </div>
        <p data-caption class="mt-2 font-tcd12-display text-[13px] font-semibold uppercase tracking-[0.08em] text-tcd12-mut group-data-[band=warn]/chip:text-tcd12-warn group-data-[band=crit]/chip:text-white group-data-[band=end]/chip:text-white">On track</p>
        <div aria-hidden="true" class="mt-3 h-1.5 overflow-hidden rounded-full bg-tcd12-rule group-data-[band=crit]/chip:bg-white/25 group-data-[band=end]/chip:bg-white/25"><span data-fill class="block h-full rounded-full bg-tcd12-acc transition-[width] duration-1000 ease-linear group-data-[band=warn]/chip:bg-tcd12-warn group-data-[band=crit]/chip:bg-white motion-reduce:transition-none"></span></div>
        <button type="button" data-add class="mt-4 min-h-11 w-full cursor-pointer rounded-xl border border-current/25 px-3 text-[13px] font-semibold transition hover:bg-current/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd12-acc disabled:cursor-default disabled:opacity-60">+ 10 min approved time</button>
        <p class="mt-2.5 text-[11.5px] leading-relaxed opacity-75">Accommodations are granted by the exam office before the session. This control models that flow.</p>
        <output data-live aria-live="polite" class="sr-only"></output>
      </div>
      <div class="mt-3 flex flex-wrap items-center gap-1.5 text-[11.5px] text-tcd12-mut">
        <span class="mr-1">Preview: jump to</span>
        <button type="button" data-jump="0.5" class="min-h-8 cursor-pointer rounded-md border border-tcd12-rule px-2.5 font-tcd12-mono hover:border-tcd12-ink/30">50%</button>
        <button type="button" data-jump="0.1" class="min-h-8 cursor-pointer rounded-md border border-tcd12-rule px-2.5 font-tcd12-mono hover:border-tcd12-ink/30">10%</button>
        <button type="button" data-jump="0.02" class="min-h-8 cursor-pointer rounded-md border border-tcd12-rule px-2.5 font-tcd12-mono hover:border-tcd12-ink/30">2%</button>
      </div>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd12-page: #ffffff;
  --color-tcd12-page: oklch(1 0 0);
  --color-tcd12-ink: #0b0b0c;
  --color-tcd12-ink: oklch(0.12 0.004 280);
  --color-tcd12-mut: #5c5c63;
  --color-tcd12-mut: oklch(0.46 0.008 280);
  --color-tcd12-rule: #e2e2e4;
  --color-tcd12-rule: oklch(0.91 0.003 280);
  --color-tcd12-acc: #3b2ee0;
  --color-tcd12-acc: oklch(0.45 0.24 275);
  --color-tcd12-warn: #9a5c00;
  --color-tcd12-warn: oklch(0.54 0.13 70);
  --color-tcd12-crit: #c22b1d;
  --color-tcd12-crit: oklch(0.52 0.2 27);
  --font-tcd12-display: 'Archivo Narrow', system-ui, sans-serif;
  --font-tcd12-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-tcd12-mono: 'IBM Plex Mono', ui-monospace, monospace;
}

.tcd-12 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-12');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const chip = q('[data-chip]'), clock = q('[data-clock]'), fill = q('[data-fill]');
  const cap = q('[data-caption]'), live = q('[data-live]'), add = q('[data-add]');
  let total = 45 * 60e3, target = Date.now() + total - 1000, id = 0, seen = null;
  const CAPTIONS = { ok: 'On track', half: 'Half the time used', warn: 'Ten percent left', crit: 'Final moments', end: 'Time expired' };
  const SAY = { half: 'Half of your exam time has been used.', warn: 'Ten percent of your exam time remains.', crit: 'Two percent of your time remains. Finish and submit.', end: 'Time expired. Your answers were submitted.' };
  const band = (ms, f) => ms <= 0 ? 'end' : f <= 0.02 ? 'crit' : f <= 0.1 ? 'warn' : f <= 0.5 ? 'half' : 'ok';
  const pad = (n) => String(n).padStart(2, '0');
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), f = ms / total, s = Math.ceil(ms / 1000);
    clock.textContent = pad(Math.floor(s / 60)) + ':' + pad(s % 60);
    clock.dateTime = new Date(target).toISOString();
    fill.style.width = (f * 100).toFixed(2) + '%';
    const b = band(ms, f);
    if (b !== seen) {
      seen = b; chip.dataset.band = b; cap.textContent = CAPTIONS[b];
      if (SAY[b]) live.textContent = SAY[b];
      if (b === 'end') add.disabled = true;
    }
    if (ms > 0) id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  add.addEventListener('click', () => {
    total += 10 * 60e3; target += 10 * 60e3; seen = null;
    add.disabled = true; add.textContent = '✓ 10 min accommodation applied';
    live.textContent = 'Ten minutes of approved time added.';
    clearTimeout(id); tick();
  });
  root.querySelectorAll('[data-jump]').forEach((b) => b.addEventListener('click', () => {
    target = Date.now() + total * parseFloat(b.dataset.jump) - 500; seen = null;
    clearTimeout(id); tick();
  }));
  tick();
  root.cleanup = () => clearTimeout(id);
})();
```
