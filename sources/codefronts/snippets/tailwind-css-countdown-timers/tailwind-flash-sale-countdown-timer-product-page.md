---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-flash-sale-countdown-timer-product-page/"
title: "Tailwind Flash Sale Countdown Timer for Product Pages"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A product-page urgency block: sale price over a struck original, a savings chip, the countdown and a stock bar in one frame."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Flash Sale Countdown Timer for Product Pages
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-flash-sale-countdown-timer-product-page/

A product-page urgency block: sale price over a struck original, a savings chip, the countdown and a stock bar in one frame. At zero it doesn't vanish or freeze &mdash; it switches to Sale ended with the full price restored, the honest version of this pattern. New in the port: Add to cart confirms and decrements real stock, the timer turns red inside the last hour via data-urgent:, and a w-(--stock) bar animates on change.
## HTML
```html
<section class="tcd-17 w-full min-h-svh grid place-items-center bg-tcd17-page px-4 py-12 font-tcd17-sans text-tcd17-ink" aria-labelledby="tcd-17-title">
  <article class="grid w-full max-w-[800px] grid-cols-1 border-[2.5px] border-tcd17-ink bg-tcd17-card shadow-[8px_8px_0_0_var(--color-tcd17-ink)] md:grid-cols-[minmax(0,0.9fr)_minmax(0,1.1fr)]">
    <div aria-hidden="true" class="relative min-h-[240px] overflow-hidden border-b-[2.5px] border-tcd17-ink bg-tcd17-shot md:border-r-[2.5px] md:border-b-0">
      <span class="absolute top-3.5 left-3.5 z-10 -rotate-6 border-2 border-tcd17-ink bg-tcd17-acc px-3 py-1 font-tcd17-display text-sm uppercase tracking-[0.06em] shadow-[3px_3px_0_0_var(--color-tcd17-ink)]">Flash −31%</span>
      <div class="absolute inset-[18%_22%] rounded-[14px] border-[2.5px] border-tcd17-ink bg-tcd17-ink shadow-[inset_0_0_0_10px_var(--color-tcd17-shot)]">
        <span class="absolute top-[18%] left-1/2 size-[26%] -translate-x-1/2 rounded-full border-[6px] border-tcd17-shot"></span>
        <span class="absolute bottom-[14%] left-1/2 size-[46%] -translate-x-1/2 rounded-full border-[8px] border-tcd17-shot"></span>
      </div>
    </div>

    <div class="min-w-0 p-[clamp(18px,4vw,30px)]">
      <p class="mb-1.5 text-[11px] font-bold uppercase tracking-[0.16em] text-tcd17-mut">Nova Audio · monitors</p>
      <h2 id="tcd-17-title" class="mb-4 font-tcd17-display text-[clamp(22px,3.8vw,30px)] leading-[1.05] tracking-[-0.01em] text-balance">Basalt M2 studio monitor, pair</h2>

      <div class="mb-4 flex flex-wrap items-baseline gap-x-3 gap-y-2">
        <strong data-now class="font-tcd17-display text-[clamp(34px,6vw,44px)] leading-none tabular-nums">$479</strong>
        <s data-was class="text-lg font-semibold text-tcd17-mut tabular-nums">$690</s>
        <span data-save class="border-2 border-tcd17-ink bg-tcd17-acc px-2 py-0.5 text-xs font-bold">Save $211 · 31%</span>
      </div>

      <div role="timer" data-timer class="group/timer border-[2.5px] border-tcd17-ink bg-tcd17-acc px-4 py-3 transition-colors data-urgent:bg-tcd17-danger data-urgent:text-white data-ended:bg-tcd17-ink data-ended:text-white">
        <p data-tlabel class="mb-1.5 text-[11px] font-bold uppercase tracking-[0.14em]">Spring Sale ends in</p>
        <time datetime="" data-clock aria-hidden="true" class="flex items-start gap-1.5 tabular-nums">
          <span class="grid justify-items-center"><b data-h class="font-tcd17-display text-[clamp(30px,6vw,40px)] font-normal leading-none">05</b><i class="text-[10px] font-bold not-italic uppercase tracking-[0.12em] opacity-80">hrs</i></span><span class="font-tcd17-display text-[clamp(26px,5vw,34px)] leading-none opacity-50">:</span>
          <span class="grid justify-items-center"><b data-m class="font-tcd17-display text-[clamp(30px,6vw,40px)] font-normal leading-none">12</b><i class="text-[10px] font-bold not-italic uppercase tracking-[0.12em] opacity-80">min</i></span><span class="font-tcd17-display text-[clamp(26px,5vw,34px)] leading-none opacity-50">:</span>
          <span class="grid justify-items-center"><b data-s class="font-tcd17-display text-[clamp(30px,6vw,40px)] font-normal leading-none">44</b><i class="text-[10px] font-bold not-italic uppercase tracking-[0.12em] opacity-80">sec</i></span>
        </time>
      </div>

      <div data-stock style="--stock: 22%" class="mt-4">
        <div aria-hidden="true" class="h-3 border-2 border-tcd17-ink bg-tcd17-page"><span class="block h-full w-(--stock) bg-tcd17-danger transition-[width] duration-500"></span></div>
        <p class="mt-1.5 text-[13px] text-tcd17-mut"><strong data-left class="font-bold text-tcd17-ink">7 pairs left</strong> of the 32 allocated to this sale</p>
      </div>

      <button type="button" data-buy class="mt-5 min-h-[52px] w-full cursor-pointer border-[2.5px] border-tcd17-ink bg-tcd17-ink px-5 font-tcd17-display text-[15px] uppercase tracking-[0.04em] text-white shadow-[4px_4px_0_0_var(--color-tcd17-acc)] transition-[transform,box-shadow,background-color] hover:-translate-x-px hover:-translate-y-px hover:shadow-[6px_6px_0_0_var(--color-tcd17-acc)] active:translate-x-1 active:translate-y-1 active:shadow-none focus-visible:outline-[3px] focus-visible:outline-offset-4 focus-visible:outline-tcd17-ink data-added:bg-tcd17-ok disabled:cursor-not-allowed disabled:bg-tcd17-mut disabled:shadow-none">Add to cart · $479</button>
      <p class="mt-2.5 text-[12.5px] text-tcd17-mut">Order before 4pm for dispatch today · free returns for 30 days</p>
      <output data-live aria-live="polite" class="sr-only"></output>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd17-page: #f3f1ea;
  --color-tcd17-page: oklch(0.955 0.01 90);
  --color-tcd17-card: #ffffff;
  --color-tcd17-card: oklch(1 0 0);
  --color-tcd17-shot: #e9e5da;
  --color-tcd17-shot: oklch(0.92 0.014 90);
  --color-tcd17-ink: #0c0c0c;
  --color-tcd17-ink: oklch(0.1 0 0);
  --color-tcd17-mut: #57554f;
  --color-tcd17-mut: oklch(0.44 0.006 80);
  --color-tcd17-acc: #ffcc00;
  --color-tcd17-acc: oklch(0.88 0.17 96);
  --color-tcd17-danger: #d92b1f;
  --color-tcd17-danger: oklch(0.53 0.22 28);
  --color-tcd17-ok: #1f7a46;
  --color-tcd17-ok: oklch(0.5 0.13 152);
  --font-tcd17-display: 'Archivo Black', 'Archivo', sans-serif;
  --font-tcd17-sans: 'Archivo', system-ui, sans-serif;
}

.tcd-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-17');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const clock = q('[data-clock]'), box = q('[data-timer]'), live = q('[data-live]'), buy = q('[data-buy]');
  const pad = (n) => String(n).padStart(2, '0');
  const target = new Date(Date.now() + 5 * 3600e3 + 12 * 60e3 + 44e3), ALLOC = 32;
  let id = 0, seen = null, stock = 7, price = 479, ended = false, aid = 0;
  clock.dateTime = target.toISOString();
  const label = () => stock > 0 ? 'Add to cart · $' + price : 'Sold out';
  const end = () => {
    ended = true; price = 690;
    box.setAttribute('data-ended', ''); box.removeAttribute('data-urgent');
    q('[data-tlabel]').textContent = 'Spring Sale ended';
    clock.innerHTML = '<b class="font-tcd17-display text-[clamp(26px,5vw,34px)] font-normal leading-none">Full price restored</b>';
    q('[data-now]').textContent = '$690'; q('[data-was]').hidden = true;
    q('[data-save]').textContent = 'Sale ended';
    buy.textContent = label();
    live.textContent = 'The Spring Sale has ended. The price shown is now the full price.';
  };
  const tick = () => {
    const ms = target - Date.now();
    if (ms <= 0) return end();
    const s = Math.floor(ms / 1000);
    q('[data-h]').textContent = pad(Math.floor(s / 3600));
    q('[data-m]').textContent = pad(Math.floor(s / 60) % 60);
    q('[data-s]').textContent = pad(s % 60);
    box.toggleAttribute('data-urgent', ms <= 3600e3);
    const b = ms < 60e3 ? 'm1' : ms < 600e3 ? 'm10' : ms < 3600e3 ? 'h1' : 'far';
    if (b !== seen) { seen = b; live.textContent = { far: '', h1: 'Less than one hour left in the Spring Sale.', m10: 'Ten minutes left in the Spring Sale.', m1: 'One minute left in the Spring Sale.' }[b]; }
    id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  buy.addEventListener('click', () => {
    if (stock <= 0) return;
    stock -= 1;
    q('[data-stock]').style.setProperty('--stock', (stock / ALLOC * 100).toFixed(1) + '%');
    q('[data-left]').textContent = stock === 0 ? 'Sold out' : stock + (stock === 1 ? ' pair left' : ' pairs left');
    buy.setAttribute('data-added', ''); buy.textContent = 'Added to cart ✓';
    live.textContent = 'Added to cart. ' + (stock ? stock + ' left at this price.' : 'That was the last pair.');
    clearTimeout(aid);
    aid = setTimeout(() => { buy.removeAttribute('data-added'); buy.textContent = label(); buy.disabled = stock <= 0; }, 1800);
  });
  tick();
  root.cleanup = () => { clearTimeout(id); clearTimeout(aid); };
})();
```
