---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-usage-page-with-quota-meters/"
title: "Tailwind Usage Page with Quota Meters"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A usage dashboard where limits read at a glance: a conic-gradient ring for API requests that animates in through a registered @property, a 14-day request…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Usage Page with Quota Meters
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-usage-page-with-quota-meters/

A usage dashboard where limits read at a glance: a conic-gradient ring for API requests that animates in through a registered @property, a 14-day request chart with an end-of-cycle forecast, and five linear quota meters that turn amber at 80% and red past the limit — with a page-level overage banner that appears only when a meter is over.
## HTML
```html
<section data-tsp03 class="tsp-03 group/use w-full min-h-svh bg-tsp03-bg px-4 py-10 font-tsp03-sans text-tsp03-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-03-h">
  <div class="mx-auto grid w-full max-w-6xl gap-6">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div><h1 id="tsp-03-h" class="text-3xl font-semibold tracking-tight">Usage</h1><p class="mt-1 text-tsp03-mut">Billing period Oct 1 – Oct 30 · resets in 12 days</p></div>
      <a href="#tsp-03-h" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp03-ink px-4 text-sm font-semibold text-white shadow-sm transition hover:bg-tsp03-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp03-acc">Upgrade plan</a>
    </header>

    <div role="alert" class="hidden items-start gap-3 rounded-2xl border border-rose-200 bg-rose-50 p-4 text-sm text-rose-800 group-has-[[data-level=over]]/use:flex">
      <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mt-0.5 size-5 flex-none"><path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/></svg>
      <p><strong class="font-semibold">You're over a plan limit.</strong> Overage on build minutes is billed at $0.008 / min. Raise the limit or upgrade to avoid throttling.</p>
    </div>

    <div class="grid gap-6 lg:grid-cols-[22rem_minmax(0,1fr)]">
      <article class="grid content-start gap-6 rounded-3xl border border-tsp03-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-7" aria-labelledby="tsp-03-req">
        <div class="flex items-center justify-between"><h2 id="tsp-03-req" class="font-semibold">API requests</h2><span class="rounded-full bg-tsp03-acc/10 px-2.5 py-1 text-xs font-semibold text-tsp03-acc">Pro · 1M / mo</span></div>
        <div data-ring role="meter" aria-labelledby="tsp-03-req" aria-valuemin="0" aria-valuemax="1000000" aria-valuenow="0" data-used="742318" data-limit="1000000" class="relative grid aspect-square w-52 place-items-center justify-self-center rounded-full bg-[conic-gradient(var(--color-tsp03-acc)_calc(var(--tsp03-p)*1%),var(--color-tsp03-track)_0)] transition-[--tsp03-p] duration-[1400ms] ease-out motion-reduce:transition-none">
          <span class="absolute inset-3.5 rounded-full bg-white shadow-[inset_0_2px_6px_rgb(0_0_0/0.06)]"></span>
          <span class="relative grid justify-items-center"><span data-ring-pct class="text-4xl font-semibold tabular-nums tracking-tight">0%</span><span class="text-xs text-tsp03-mut">742,318 of 1,000,000</span></span>
        </div>
        <div>
          <div class="flex items-end gap-1 h-16" aria-hidden="true">
            <i class="h-[38%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[44%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[40%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[52%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[48%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[30%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[26%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[58%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[64%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[61%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[72%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[68%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-[86%] flex-1 rounded-sm bg-tsp03-acc/25"></i><i class="h-full flex-1 rounded-sm bg-tsp03-acc"></i>
          </div>
          <div class="mt-2 flex justify-between text-[11px] text-tsp03-mut"><span>Sep 24</span><span>Today</span></div>
        </div>
        <p class="flex items-start gap-2 rounded-2xl bg-amber-50 p-3 text-sm text-amber-900"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mt-0.5 size-4 flex-none"><path d="M3 17 9 11l4 4 8-8M15 7h6v6"/></svg><span>At this pace you'll reach <strong class="font-semibold">1.24M</strong> by Oct 30 — 24% over.</span></p>
      </article>

      <article class="rounded-3xl border border-tsp03-line bg-white p-6 shadow-[0_1px_2px_rgb(0_0_0/0.04)] sm:p-7" aria-labelledby="tsp-03-q">
        <h2 id="tsp-03-q" class="font-semibold">Plan quotas</h2>
        <div class="mt-2 grid divide-y divide-tsp03-line">
          <div data-meter data-used="9" data-limit="12" data-unit="seats" class="group/m grid gap-2.5 py-5">
            <div class="flex flex-wrap items-baseline justify-between gap-2"><span id="tsp-03-m1" class="font-medium">Seats</span><span class="text-sm tabular-nums"><strong data-val class="font-semibold"></strong> <span data-of class="text-tsp03-mut"></span></span></div>
            <div role="meter" aria-labelledby="tsp-03-m1" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" class="h-2 overflow-hidden rounded-full bg-tsp03-track"><div class="h-full w-[calc(var(--tsp03-p,0)*1%)] max-w-full rounded-full bg-tsp03-acc transition-[width] duration-1000 ease-out group-data-[level=warn]/m:bg-amber-500 group-data-[level=over]/m:bg-rose-500 motion-reduce:transition-none"></div></div>
            <p data-note class="text-xs text-tsp03-mut group-data-[level=warn]/m:text-amber-700 group-data-[level=over]/m:font-semibold group-data-[level=over]/m:text-rose-700"></p>
          </div>
          <div data-meter data-used="38.2" data-limit="100" data-unit="GB" class="group/m grid gap-2.5 py-5">
            <div class="flex flex-wrap items-baseline justify-between gap-2"><span id="tsp-03-m2" class="font-medium">Storage</span><span class="text-sm tabular-nums"><strong data-val class="font-semibold"></strong> <span data-of class="text-tsp03-mut"></span></span></div>
            <div role="meter" aria-labelledby="tsp-03-m2" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" class="h-2 overflow-hidden rounded-full bg-tsp03-track"><div class="h-full w-[calc(var(--tsp03-p,0)*1%)] max-w-full rounded-full bg-tsp03-acc transition-[width] duration-1000 ease-out group-data-[level=warn]/m:bg-amber-500 group-data-[level=over]/m:bg-rose-500 motion-reduce:transition-none"></div></div>
            <p data-note class="text-xs text-tsp03-mut group-data-[level=warn]/m:text-amber-700 group-data-[level=over]/m:font-semibold group-data-[level=over]/m:text-rose-700"></p>
          </div>
          <div data-meter data-used="612" data-limit="1000" data-unit="GB" class="group/m grid gap-2.5 py-5">
            <div class="flex flex-wrap items-baseline justify-between gap-2"><span id="tsp-03-m3" class="font-medium">Bandwidth</span><span class="text-sm tabular-nums"><strong data-val class="font-semibold"></strong> <span data-of class="text-tsp03-mut"></span></span></div>
            <div role="meter" aria-labelledby="tsp-03-m3" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" class="h-2 overflow-hidden rounded-full bg-tsp03-track"><div class="h-full w-[calc(var(--tsp03-p,0)*1%)] max-w-full rounded-full bg-tsp03-acc transition-[width] duration-1000 ease-out group-data-[level=warn]/m:bg-amber-500 group-data-[level=over]/m:bg-rose-500 motion-reduce:transition-none"></div></div>
            <p data-note class="text-xs text-tsp03-mut group-data-[level=warn]/m:text-amber-700 group-data-[level=over]/m:font-semibold group-data-[level=over]/m:text-rose-700"></p>
          </div>
          <div data-meter data-used="3120" data-limit="3000" data-unit="min" class="group/m grid gap-2.5 py-5">
            <div class="flex flex-wrap items-baseline justify-between gap-2"><span id="tsp-03-m4" class="font-medium">Build minutes</span><span class="text-sm tabular-nums"><strong data-val class="font-semibold"></strong> <span data-of class="text-tsp03-mut"></span></span></div>
            <div role="meter" aria-labelledby="tsp-03-m4" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" class="h-2 overflow-hidden rounded-full bg-tsp03-track"><div class="h-full w-[calc(var(--tsp03-p,0)*1%)] max-w-full rounded-full bg-tsp03-acc transition-[width] duration-1000 ease-out group-data-[level=warn]/m:bg-amber-500 group-data-[level=over]/m:bg-rose-500 motion-reduce:transition-none"></div></div>
            <p data-note class="text-xs text-tsp03-mut group-data-[level=warn]/m:text-amber-700 group-data-[level=over]/m:font-semibold group-data-[level=over]/m:text-rose-700"></p>
          </div>
          <div data-meter data-used="41200" data-limit="50000" data-unit="credits" class="group/m grid gap-2.5 py-5">
            <div class="flex flex-wrap items-baseline justify-between gap-2"><span id="tsp-03-m5" class="font-medium">AI credits</span><span class="text-sm tabular-nums"><strong data-val class="font-semibold"></strong> <span data-of class="text-tsp03-mut"></span></span></div>
            <div role="meter" aria-labelledby="tsp-03-m5" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" class="h-2 overflow-hidden rounded-full bg-tsp03-track"><div class="h-full w-[calc(var(--tsp03-p,0)*1%)] max-w-full rounded-full bg-tsp03-acc transition-[width] duration-1000 ease-out group-data-[level=warn]/m:bg-amber-500 group-data-[level=over]/m:bg-rose-500 motion-reduce:transition-none"></div></div>
            <p data-note class="text-xs text-tsp03-mut group-data-[level=warn]/m:text-amber-700 group-data-[level=over]/m:font-semibold group-data-[level=over]/m:text-rose-700"></p>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp03-bg: #f4f7fa;
  --color-tsp03-bg: oklch(0.975 0.005 240);
  --color-tsp03-ink: #0f1b2a;
  --color-tsp03-ink: oklch(0.215 0.035 250);
  --color-tsp03-mut: #5a6878;
  --color-tsp03-mut: oklch(0.52 0.03 250);
  --color-tsp03-line: #e2e8ef;
  --color-tsp03-line: oklch(0.928 0.011 250);
  --color-tsp03-track: #e9eef4;
  --color-tsp03-track: oklch(0.945 0.01 250);
  --color-tsp03-acc: #0ea5e9;
  --color-tsp03-acc: oklch(0.685 0.148 237);
  --font-tsp03-sans: 'Sora', system-ui, sans-serif;
}
/* A typed number is what lets the conic-gradient ring interpolate — utilities can't register one. */

@property --tsp03-p {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

.tsp-03 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp03]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const fmt = (n) => Number(n).toLocaleString('en-US', { maximumFractionDigits: 1 });
  const level = (p) => (p > 100 ? 'over' : p >= 80 ? 'warn' : 'ok');
  const ring = root.querySelector('[data-ring]');
  const meters = [...root.querySelectorAll('[data-meter]')];
  meters.forEach((m) => {
    const used = +m.dataset.used, limit = +m.dataset.limit, unit = m.dataset.unit;
    const p = (used / limit) * 100;
    m.dataset.level = level(p);
    m.querySelector('[data-val]').textContent = fmt(used) + ' ' + unit;
    m.querySelector('[data-of]').textContent = 'of ' + fmt(limit);
    m.querySelector('[role=meter]').setAttribute('aria-valuenow', Math.round(p));
    const note = m.querySelector('[data-note]');
    if (p > 100) note.textContent = 'Over by ' + fmt(used - limit) + ' ' + unit + ' — overage applies';
    else if (p >= 80) note.textContent = Math.round(p) + '% used — consider raising this limit';
    else note.textContent = fmt(limit - used) + ' ' + unit + ' remaining';
  });
  const ringP = (+ring.dataset.used / +ring.dataset.limit) * 100;
  ring.setAttribute('aria-valuenow', ring.dataset.used);
  setTimeout(() => {
    meters.forEach((m) => m.style.setProperty('--tsp03-p', ((+m.dataset.used / +m.dataset.limit) * 100).toFixed(1)));
    ring.style.setProperty('--tsp03-p', ringP.toFixed(1));
  }, 80);
  const pct = root.querySelector('[data-ring-pct]');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const start = Date.now() + 80, dur = reduce ? 0 : 1400;
  const tick = () => {
    const k = dur ? Math.min(1, Math.max(0, Date.now() - start) / dur) : 1;
    pct.textContent = Math.round(ringP * (1 - Math.pow(1 - k, 3))) + '%';
    if (k < 1) setTimeout(tick, 16);
  };
  tick();
})();
```
