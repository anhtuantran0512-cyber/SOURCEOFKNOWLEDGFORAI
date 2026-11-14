---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-auction-countdown-timer-anti-snipe/"
title: "Tailwind Auction Countdown Timer with Anti-Snipe Extension"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A brutalist lot card whose countdown turns red in the final minute and, when a bid lands in those seconds, visibly extends by two minutes with an Extended…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Auction Countdown Timer with Anti-Snipe Extension
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-auction-countdown-timer-anti-snipe/

A brutalist lot card whose countdown turns red in the final minute and, when a bid lands in those seconds, visibly extends by two minutes with an Extended +2:00 flash &mdash; the soft-close rule that stops snipers. Ported to a hard offset shadow-[7px_7px_0_0_…], group-data-urgent/timer: state and starting: entries for every new bid row.
## HTML
```html
<section class="tcd-07 w-full min-h-svh grid place-items-center bg-tcd07-page bg-[radial-gradient(var(--color-tcd07-dot)_1px,transparent_1px)] bg-[length:18px_18px] px-4 py-12 font-tcd07-sans text-tcd07-ink" aria-labelledby="tcd-07-title">
  <article class="grid w-full max-w-[780px] grid-cols-1 border-2 border-tcd07-ink bg-tcd07-card shadow-[7px_7px_0_0_var(--color-tcd07-ink)] md:grid-cols-[250px_minmax(0,1fr)]">
    <div aria-hidden="true" class="relative min-h-[200px] min-w-0 overflow-hidden border-b-2 border-tcd07-ink bg-tcd07-thumb p-3.5 md:border-r-2 md:border-b-0">
      <span class="relative z-10 bg-tcd07-ink px-2 py-1 font-tcd07-mono text-[10.5px] font-bold uppercase tracking-[0.2em] text-tcd07-card">Lot 214</span>
      <div class="absolute inset-[44px_24px_20px] border-2 border-tcd07-ink bg-[repeating-linear-gradient(90deg,var(--color-tcd07-wood-a)_0_12px,var(--color-tcd07-wood-b)_12px_24px)] after:absolute after:inset-x-3.5 after:top-[22%] after:h-[34%] after:border-2 after:border-tcd07-ink after:bg-tcd07-card after:content-['']"></div>
    </div>

    <div class="min-w-0 p-[clamp(16px,3.4vw,28px)]">
      <p class="mb-3 inline-flex items-center gap-2 bg-tcd07-ink px-2.5 py-1 font-tcd07-mono text-[10px] font-bold uppercase tracking-[0.18em] text-tcd07-card"><span aria-hidden="true" class="size-1.5 rounded-full bg-tcd07-danger animate-pulse motion-reduce:animate-none"></span>Live · soft close</p>
      <h2 id="tcd-07-title" class="mb-1.5 text-[clamp(20px,3.4vw,27px)] font-extrabold leading-[1.12] tracking-[-0.01em] [font-stretch:85%] text-balance">Basalt No. 4 letterpress cabinet, 1948</h2>
      <p class="mb-5 text-[13px] text-tcd07-mut">Ranger Auction House · <span data-count>32</span> bids · reserve met</p>

      <div class="mb-4 flex flex-wrap items-baseline gap-x-3 gap-y-1 border-b-2 border-tcd07-ink pb-4">
        <span class="font-tcd07-mono text-[11px] font-bold uppercase tracking-[0.14em] text-tcd07-mut">Current bid</span>
        <strong data-val class="text-[clamp(30px,6vw,42px)] font-extrabold leading-none tracking-[-0.02em] tabular-nums [font-stretch:80%]">$4,150</strong>
      </div>

      <div role="timer" data-timer class="group/timer flex flex-wrap items-center gap-x-3 gap-y-1 border-2 border-tcd07-ink bg-tcd07-chip px-3.5 py-3 transition-colors data-urgent:bg-tcd07-danger data-urgent:text-white">
        <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" class="flex-none group-data-urgent/timer:animate-pulse motion-reduce:animate-none"><circle cx="10" cy="10" r="7.6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10 6.2V10l2.6 1.7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <time datetime="" data-clock class="font-tcd07-mono text-[clamp(24px,5vw,30px)] font-bold leading-none tabular-nums">00:58</time>
        <span data-cap class="text-[12.5px] font-semibold">until bidding closes</span>
      </div>

      <p data-flash class="mt-3 hidden border-2 border-tcd07-ink bg-tcd07-hi px-3 py-2 font-tcd07-mono text-[12px] font-bold data-show:block data-show:animate-tcd07-flash motion-reduce:animate-none">Extended +2:00 — a bid landed in the final minute</p>

      <div class="mt-4 flex flex-wrap gap-2.5">
        <button type="button" data-bid class="min-h-12 flex-[1_1_160px] cursor-pointer border-2 border-tcd07-ink bg-tcd07-ink px-5 font-extrabold text-tcd07-card shadow-[3px_3px_0_0_var(--color-tcd07-danger)] transition-[transform,box-shadow] hover:-translate-x-px hover:-translate-y-px hover:shadow-[5px_5px_0_0_var(--color-tcd07-danger)] active:translate-x-0.5 active:translate-y-0.5 active:shadow-none focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcd07-danger disabled:cursor-not-allowed disabled:bg-tcd07-mut disabled:shadow-none">Bid $4,200</button>
        <button type="button" aria-pressed="false" data-watch class="min-h-12 flex-[1_1_120px] cursor-pointer border-2 border-tcd07-ink bg-tcd07-card px-5 font-extrabold transition hover:bg-tcd07-chip aria-pressed:bg-tcd07-hi focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tcd07-danger">Watch lot</button>
      </div>

      <ul data-log aria-label="Recent bids" class="mt-5 grid gap-1.5 font-tcd07-mono text-[12px]">
        <li class="flex justify-between gap-3 border-b border-dashed border-tcd07-ink/30 pb-1.5"><span><b>$4,150</b> Jordan Lee</span><span class="text-tcd07-mut">41s ago</span></li>
        <li class="flex justify-between gap-3 border-b border-dashed border-tcd07-ink/30 pb-1.5"><span><b>$4,050</b> Sam Rivera</span><span class="text-tcd07-mut">2m ago</span></li>
      </ul>
      <p class="mt-4 text-[12px] leading-relaxed text-tcd07-mut text-pretty">Any bid in the final minute moves the close two minutes out. Auctions are a real-time event, so the clock is the same for every bidder and cannot be extended on request.</p>
      <output data-live aria-live="polite" class="sr-only"></output>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd07-page: #f4f1ea;
  --color-tcd07-page: oklch(0.95 0.014 85);
  --color-tcd07-dot: #d9d2c4;
  --color-tcd07-dot: oklch(0.86 0.02 85);
  --color-tcd07-card: #fffefb;
  --color-tcd07-card: oklch(0.99 0.006 85);
  --color-tcd07-ink: #14100c;
  --color-tcd07-ink: oklch(0.17 0.014 60);
  --color-tcd07-mut: #5e554b;
  --color-tcd07-mut: oklch(0.45 0.018 65);
  --color-tcd07-chip: #f1ece1;
  --color-tcd07-chip: oklch(0.94 0.014 82);
  --color-tcd07-thumb: #e8e2d5;
  --color-tcd07-thumb: oklch(0.91 0.018 85);
  --color-tcd07-wood-a: #cfc6b2;
  --color-tcd07-wood-a: oklch(0.83 0.03 85);
  --color-tcd07-wood-b: #ded6c6;
  --color-tcd07-wood-b: oklch(0.88 0.024 85);
  --color-tcd07-danger: #cc2115;
  --color-tcd07-danger: oklch(0.52 0.22 28);
  --color-tcd07-hi: #ffe14d;
  --color-tcd07-hi: oklch(0.91 0.17 98);
  --font-tcd07-sans: 'Archivo', 'Helvetica Neue', sans-serif;
  --font-tcd07-mono: 'Space Mono', ui-monospace, monospace;
  --animate-tcd07-flash: tcd07-flash 0.9s cubic-bezier(0.2, 0.9, 0.3, 1.2);

  @keyframes tcd07-flash {
    0% {
      transform: translateY(-6px) scale(0.97);
      opacity: 0;
    }

    60% {
      transform: translateY(0) scale(1.02);
      opacity: 1;
    }

    100% {
      transform: none;
    }
  }
}

.tcd-07 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-07');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const clock = q('[data-clock]'), cap = q('[data-cap]'), box = q('[data-timer]');
  const flash = q('[data-flash]'), live = q('[data-live]'), log = q('[data-log]'), bidBtn = q('[data-bid]');
  const SOFT = 60e3, BUMP = 120e3, pad = (n) => String(n).padStart(2, '0');
  let target = Date.now() + 58e3, id = 0, seen = null, bid = 4150, count = 32;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    clock.textContent = pad(Math.floor(s / 60)) + ':' + pad(s % 60);
    clock.dateTime = new Date(target).toISOString();
    const urgent = ms > 0 && ms <= SOFT;
    box.toggleAttribute('data-urgent', urgent);
    if (ms > 0) cap.textContent = urgent ? 'Final minute · bids extend the close' : 'until bidding closes';
    const b = ms <= 0 ? 'end' : urgent ? 'urgent' : 'open';
    if (b !== seen) { seen = b; live.textContent = b === 'end' ? 'Bidding closed at ' + bid.toLocaleString() + ' dollars.' : b === 'urgent' ? 'Final minute of bidding.' : ''; }
    if (ms > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); return; }
    clock.textContent = 'Closed'; cap.textContent = 'Bidding closed · lot sold'; bidBtn.disabled = true; bidBtn.textContent = 'Sold';
  };
  bidBtn.addEventListener('click', () => {
    if (bidBtn.disabled || target <= Date.now()) return;
    bid += 50; count += 1;
    q('[data-val]').textContent = '$' + bid.toLocaleString();
    q('[data-count]').textContent = count;
    bidBtn.textContent = 'Bid $' + (bid + 50).toLocaleString();
    const li = document.createElement('li');
    li.className = 'flex justify-between gap-3 border-b border-dashed border-tcd07-ink/30 pb-1.5 transition duration-500 starting:-translate-y-1 starting:opacity-0';
    li.innerHTML = '<span><b>$' + bid.toLocaleString() + '</b> You</span><span class="text-tcd07-mut">just now</span>';
    log.prepend(li);
    if (target - Date.now() <= SOFT) {
      target = Date.now() + BUMP; seen = null;
      flash.removeAttribute('data-show'); void flash.offsetWidth; flash.setAttribute('data-show', '');
      live.textContent = 'Bid accepted. Closing time extended by two minutes.';
      clearTimeout(id); tick();
    } else live.textContent = 'Bid accepted.';
  });
  const watch = q('[data-watch]');
  watch.addEventListener('click', () => { const on = watch.getAttribute('aria-pressed') !== 'true'; watch.setAttribute('aria-pressed', String(on)); watch.textContent = on ? 'Watching ✓' : 'Watch lot'; });
  tick();
  root.cleanup = () => clearTimeout(id);
})();
```
