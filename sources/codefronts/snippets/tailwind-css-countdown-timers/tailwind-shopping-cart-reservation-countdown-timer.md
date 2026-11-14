---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-shopping-cart-reservation-countdown-timer/"
title: "Tailwind Shopping Cart Reservation Countdown Timer"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A cart-page reservation timer: items held for a fixed window, a per-line list of what's reserved, a warning state under two minutes and an extend control."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shopping Cart Reservation Countdown Timer
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-shopping-cart-reservation-countdown-timer/

A cart-page reservation timer: items held for a fixed window, a per-line list of what's reserved, a warning state under two minutes and an extend control. The rule it demonstrates: never silently empty a cart &mdash; warn, offer more time, say what happens. New in the port: a depleting pathLength ring around the clock icon, a Start a new hold path after expiry, and every state driven by one data-state attribute.
## HTML
```html
<section class="tcd-19 w-full min-h-svh grid place-items-center bg-tcd19-page px-4 py-12 font-tcd19-sans text-tcd19-ink antialiased" aria-labelledby="tcd-19-title">
  <article data-panel data-state="ok" class="group/panel w-full max-w-[560px] border-2 border-tcd19-ink bg-tcd19-panel p-[clamp(18px,4.4vw,32px)] shadow-[6px_6px_0_0_var(--color-tcd19-ink)] transition-colors data-[state=warn]:border-tcd19-crit data-[state=warn]:shadow-[6px_6px_0_0_var(--color-tcd19-crit)]">
    <header class="mb-5">
      <p class="mb-1.5 text-[11px] font-bold uppercase tracking-[0.16em] text-tcd19-mut">Quill Press · checkout</p>
      <h2 id="tcd-19-title" class="font-tcd19-serif text-[clamp(24px,4.4vw,32px)] font-medium leading-tight tracking-[-0.015em]"><span class="group-data-[state=expired]/panel:hidden">Your items are reserved</span><span class="hidden group-data-[state=expired]/panel:inline">Your hold was released</span></h2>
    </header>

    <div role="timer" class="grid grid-cols-[auto_minmax(0,1fr)] items-center gap-x-4 gap-y-1 rounded-xl bg-tcd19-acc/8 p-4 group-data-[state=warn]/panel:bg-tcd19-crit/10 group-data-[state=expired]/panel:bg-tcd19-ink/5">
      <span data-ring style="--off: 0" aria-hidden="true" class="relative row-span-2 grid size-12 place-items-center text-tcd19-acc group-data-[state=warn]/panel:text-tcd19-crit group-data-[state=expired]/panel:text-tcd19-mut">
        <svg viewBox="0 0 48 48" class="absolute inset-0 -rotate-90"><circle cx="24" cy="24" r="21" pathLength="100" class="fill-none stroke-current opacity-20 [stroke-width:3]"/><circle cx="24" cy="24" r="21" pathLength="100" class="fill-none stroke-current [stroke-dasharray:100] [stroke-dashoffset:var(--off)] [stroke-linecap:round] [stroke-width:3] transition-[stroke-dashoffset] duration-1000 ease-linear motion-reduce:transition-none"/></svg>
        <svg viewBox="0 0 20 20" width="18" height="18"><circle cx="10" cy="10" r="7.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 5.9V10l2.8 1.8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </span>
      <p class="text-[15px] font-semibold">Held for <time datetime="" data-clock class="font-tcd19-serif text-[26px] font-semibold tabular-nums text-tcd19-acc group-data-[state=warn]/panel:text-tcd19-crit group-data-[state=expired]/panel:text-tcd19-mut">9:47</time></p>
      <p data-note class="text-[13px] leading-relaxed text-tcd19-mut text-pretty group-data-[state=warn]/panel:font-semibold group-data-[state=warn]/panel:text-tcd19-crit">Checkout completes the sale. Nothing is charged until you confirm.</p>
    </div>

    <ul class="mt-5 divide-y divide-tcd19-ink/12 border-y border-tcd19-ink/12">
      <li class="grid grid-cols-[minmax(0,1fr)_auto] gap-x-4 gap-y-0.5 py-3"><span class="text-[14.5px] font-semibold">Basalt letterpress set, A5</span><span class="row-span-2 self-center font-tcd19-serif text-lg font-medium tabular-nums">$64</span><span class="text-xs text-tcd19-mut">Held firmly · 12 in stock</span></li>
      <li class="grid grid-cols-[minmax(0,1fr)_auto] gap-x-4 gap-y-0.5 py-3"><span class="text-[14.5px] font-semibold">Meridian ink, oxide black</span><span class="row-span-2 self-center font-tcd19-serif text-lg font-medium tabular-nums">$18</span><span class="text-xs text-tcd19-mut">Held firmly · 40 in stock</span></li>
      <li data-low class="group/line grid grid-cols-[minmax(0,1fr)_auto] gap-x-4 gap-y-0.5 py-3"><span class="text-[14.5px] font-semibold">Fern cotton paper, 250gsm</span><span class="row-span-2 self-center font-tcd19-serif text-lg font-medium tabular-nums">$39</span><span class="flex items-center gap-1.5 text-xs text-tcd19-mut group-data-low/line:font-semibold group-data-low/line:text-tcd19-crit"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Low stock · hold cannot be extended</span></li>
    </ul>

    <div class="mt-5 flex flex-wrap gap-2.5">
      <button type="button" class="min-h-12 flex-[1_1_180px] cursor-pointer border-2 border-tcd19-ink bg-tcd19-ink px-5 font-semibold text-tcd19-panel transition hover:bg-tcd19-ink/90 active:translate-y-px focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcd19-acc">Checkout · $121</button>
      <button type="button" data-extend class="min-h-12 flex-[1_1_160px] cursor-pointer border-2 border-tcd19-ink px-5 font-semibold transition hover:bg-tcd19-ink/5 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcd19-acc disabled:cursor-default disabled:border-tcd19-ink/25 disabled:text-tcd19-mut group-data-[state=warn]/panel:border-tcd19-crit group-data-[state=warn]/panel:bg-tcd19-crit group-data-[state=warn]/panel:text-white">Give me more time</button>
    </div>

    <p class="mt-5 text-[12.5px] leading-relaxed text-tcd19-mut text-pretty">If the hold expires the items stay in your basket — the reservation is released, so stock is no longer guaranteed. Nothing is deleted without telling you.</p>
    <output data-live aria-live="polite" class="sr-only"></output>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd19-page: #f0e9df;
  --color-tcd19-page: oklch(0.935 0.018 75);
  --color-tcd19-panel: #fdfaf5;
  --color-tcd19-panel: oklch(0.985 0.01 80);
  --color-tcd19-ink: #2a2018;
  --color-tcd19-ink: oklch(0.26 0.02 55);
  --color-tcd19-mut: #66574a;
  --color-tcd19-mut: oklch(0.46 0.03 55);
  --color-tcd19-acc: #b4531f;
  --color-tcd19-acc: oklch(0.53 0.15 45);
  --color-tcd19-warn: #b4531f;
  --color-tcd19-warn: oklch(0.53 0.15 45);
  --color-tcd19-crit: #a01f14;
  --color-tcd19-crit: oklch(0.45 0.2 28);
  --font-tcd19-serif: 'Newsreader', Georgia, serif;
  --font-tcd19-sans: 'Instrument Sans', system-ui, sans-serif;
}

.tcd-19 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-19');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const panel = q('[data-panel]'), clock = q('[data-clock]'), note = q('[data-note]'), live = q('[data-live]');
  const ring = q('[data-ring]'), ext = q('[data-extend]');
  const HOLD = 9 * 60e3 + 47e3, MORE = 5 * 60e3, FULL = 10 * 60e3;
  let target = Date.now() + HOLD, total = FULL, id = 0, seen = null;
  const NOTE = { ok: 'Checkout completes the sale. Nothing is charged until you confirm.', soon: 'Five minutes left on this hold. You can extend it once.', warn: 'Under two minutes — extend the hold or complete checkout now.', expired: 'The hold was released. Your items are still listed; stock is no longer guaranteed.' };
  const SAY = { soon: 'Five minutes left on your cart reservation.', warn: 'Under two minutes left. Extend the hold or check out.', expired: 'Your cart reservation expired. The items are still in your basket.' };
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    clock.textContent = ms > 0 ? Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0') : 'released';
    clock.dateTime = new Date(target).toISOString();
    ring.style.setProperty('--off', (100 - ms / total * 100).toFixed(2));
    const b = ms <= 0 ? 'expired' : ms <= 120e3 ? 'warn' : ms <= 300e3 ? 'soon' : 'ok';
    if (b !== seen) {
      seen = b;
      panel.dataset.state = b === 'soon' ? 'ok' : b;
      note.textContent = NOTE[b];
      if (SAY[b]) live.textContent = SAY[b];
      if (b === 'expired') { ext.disabled = false; ext.textContent = 'Start a new hold'; }
    }
    if (ms > 0) id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  ext.addEventListener('click', () => {
    const expired = panel.dataset.state === 'expired';
    total = expired ? FULL : MORE;
    target = Date.now() + total; seen = null;
    ext.disabled = true; ext.textContent = expired ? 'New hold started' : 'Extended once';
    live.textContent = expired ? 'A new ten-minute hold has started. Stock is re-checked.' : 'Five more minutes added to your reservation.';
    clearTimeout(id); tick();
  });
  tick();
  root.cleanup = () => clearTimeout(id);
})();
```
