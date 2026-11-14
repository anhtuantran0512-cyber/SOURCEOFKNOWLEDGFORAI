---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-slider-calculator-per-seat/"
title: "Tailwind Pricing Slider Calculator for Per-Seat Pricing"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "The usage-based calculator SaaS teams actually ship: drag a team-size slider and every tier's monthly total recalculates, the per-seat maths updates and the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Slider Calculator for Per-Seat Pricing
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-slider-calculator-per-seat/

The usage-based calculator SaaS teams actually ship: drag a team-size slider and every tier's monthly total recalculates, the per-seat maths updates and the &ldquo;Best value&rdquo; badge jumps to whichever plan is now cheapest. The range thumb and track are styled with arbitrary pseudo-element variants ([&::-webkit-slider-thumb]:), and the script marks the winner with a data-best attribute that data-best: utilities restyle.
## HTML
```html
<section class="tpt-11 w-full min-h-svh grid place-items-center bg-tpt11-bg bg-[radial-gradient(70%_50%_at_50%_0%,var(--color-tpt11-glow),transparent)] px-5 py-16 font-tpt11-sans text-tpt11-ink antialiased" aria-label="Per-seat pricing calculator" data-tpt11-root>
  <div class="grid w-full max-w-5xl justify-items-center gap-10">
    <header class="grid w-full max-w-md justify-items-center gap-6 text-center">
      <h2 class="text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em]">How big is your team?</h2>
      <label for="tpt11-range" class="text-sm font-medium text-tpt11-mut"><output data-out class="mr-1 font-tpt11-mono text-2xl font-semibold text-tpt11-acc tabular-nums">10</output> seats</label>
      <div class="grid w-full gap-2">
        <input type="range" id="tpt11-range" min="1" max="100" step="1" value="10" list="tpt11-ticks" data-range class="h-2 w-full cursor-pointer appearance-none rounded-full bg-[linear-gradient(to_right,var(--color-tpt11-acc)_var(--pct),var(--color-tpt11-track)_var(--pct))] [--pct:9%] focus-visible:outline-3 focus-visible:outline-offset-8 focus-visible:outline-tpt11-acc [&::-moz-range-thumb]:size-6 [&::-moz-range-thumb]:rounded-full [&::-moz-range-thumb]:border-[5px] [&::-moz-range-thumb]:border-tpt11-acc [&::-moz-range-thumb]:bg-white [&::-webkit-slider-thumb]:size-6 [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:border-[5px] [&::-webkit-slider-thumb]:border-tpt11-acc [&::-webkit-slider-thumb]:bg-white [&::-webkit-slider-thumb]:shadow-[0_4px_12px_oklch(0_0_0/0.45)] [&::-webkit-slider-thumb]:transition-transform hover:[&::-webkit-slider-thumb]:scale-115 active:[&::-webkit-slider-thumb]:scale-125">
        <datalist id="tpt11-ticks"><option value="1"></option><option value="25"></option><option value="50"></option><option value="75"></option><option value="100"></option></datalist>
        <div aria-hidden="true" class="flex justify-between font-tpt11-mono text-[11px] text-tpt11-mut"><span>1</span><span>25</span><span>50</span><span>75</span><span>100</span></div>
      </div>
    </header>
    <div class="grid w-full gap-5 md:grid-cols-3">
      <article data-card class="group/card relative flex flex-col gap-2 rounded-[20px] border-[1.5px] border-tpt11-line bg-tpt11-card p-7 transition-[border-color,box-shadow] duration-350 data-best:border-tpt11-acc data-best:shadow-[0_18px_44px_-26px_var(--color-tpt11-acc)]">
        <span class="absolute -top-3 right-5 translate-y-1 rounded-full bg-tpt11-acc px-3 py-1 text-[10.5px] font-bold tracking-[0.08em] text-tpt11-on-acc uppercase opacity-0 transition duration-350 group-data-best/card:translate-y-0 group-data-best/card:opacity-100">Best value</span>
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt11-mut uppercase">Starter</h3>
        <p class="text-[42px] leading-tight font-bold tracking-[-0.035em] tabular-nums"><span data-amount>$70</span><small class="text-[15px] font-medium tracking-normal text-tpt11-mut">/mo</small></p>
        <p data-math class="min-h-4 font-tpt11-mono text-xs text-tpt11-mut tabular-nums">$7 × 10 seats</p>
        <ul class="mt-4 mb-6 grid flex-1 content-start gap-2.5 text-sm text-tpt11-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt11-acc *:before:content-['✓']"><li>Core features</li><li>Standard support</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border border-tpt11-line text-sm font-semibold text-tpt11-ink no-underline transition hover:border-tpt11-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt11-acc group-data-best/card:border-tpt11-acc group-data-best/card:bg-tpt11-acc group-data-best/card:text-tpt11-on-acc">Choose Starter</a>
      </article>
      <article data-card class="group/card relative flex flex-col gap-2 rounded-[20px] border-[1.5px] border-tpt11-line bg-tpt11-card p-7 transition-[border-color,box-shadow] duration-350 data-best:border-tpt11-acc data-best:shadow-[0_18px_44px_-26px_var(--color-tpt11-acc)]">
        <span class="absolute -top-3 right-5 translate-y-1 rounded-full bg-tpt11-acc px-3 py-1 text-[10.5px] font-bold tracking-[0.08em] text-tpt11-on-acc uppercase opacity-0 transition duration-350 group-data-best/card:translate-y-0 group-data-best/card:opacity-100">Best value</span>
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt11-mut uppercase">Team</h3>
        <p class="text-[42px] leading-tight font-bold tracking-[-0.035em] tabular-nums"><span data-amount>$99</span><small class="text-[15px] font-medium tracking-normal text-tpt11-mut">/mo</small></p>
        <p data-math class="min-h-4 font-tpt11-mono text-xs text-tpt11-mut tabular-nums">$49 base + $5 × 10 seats</p>
        <ul class="mt-4 mb-6 grid flex-1 content-start gap-2.5 text-sm text-tpt11-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt11-acc *:before:content-['✓']"><li>Everything in Starter</li><li>Roles &amp; permissions</li><li>Priority support</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border border-tpt11-line text-sm font-semibold text-tpt11-ink no-underline transition hover:border-tpt11-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt11-acc group-data-best/card:border-tpt11-acc group-data-best/card:bg-tpt11-acc group-data-best/card:text-tpt11-on-acc">Choose Team</a>
      </article>
      <article data-card class="group/card relative flex flex-col gap-2 rounded-[20px] border-[1.5px] border-tpt11-line bg-tpt11-card p-7 transition-[border-color,box-shadow] duration-350 data-best:border-tpt11-acc data-best:shadow-[0_18px_44px_-26px_var(--color-tpt11-acc)]">
        <span class="absolute -top-3 right-5 translate-y-1 rounded-full bg-tpt11-acc px-3 py-1 text-[10.5px] font-bold tracking-[0.08em] text-tpt11-on-acc uppercase opacity-0 transition duration-350 group-data-best/card:translate-y-0 group-data-best/card:opacity-100">Best value</span>
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt11-mut uppercase">Business</h3>
        <p class="text-[42px] leading-tight font-bold tracking-[-0.035em] tabular-nums"><span data-amount>$184</span><small class="text-[15px] font-medium tracking-normal text-tpt11-mut">/mo</small></p>
        <p data-math class="min-h-4 font-tpt11-mono text-xs text-tpt11-mut tabular-nums">$149 base + $3.5 × 10 seats</p>
        <ul class="mt-4 mb-6 grid flex-1 content-start gap-2.5 text-sm text-tpt11-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt11-acc *:before:content-['✓']"><li>Everything in Team</li><li>SSO &amp; audit log</li><li>99.9% uptime SLA</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border border-tpt11-line text-sm font-semibold text-tpt11-ink no-underline transition hover:border-tpt11-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt11-acc group-data-best/card:border-tpt11-acc group-data-best/card:bg-tpt11-acc group-data-best/card:text-tpt11-on-acc">Choose Business</a>
      </article>
    </div>
    <p data-live aria-live="polite" class="sr-only"></p>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tpt11-mono text-[11.5px] text-tpt11-mut ring-1 ring-white/10">[&amp;::-webkit-slider-thumb]: · data-best: · group-data-best/card:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt11-bg: #0f1410;
  --color-tpt11-bg: oklch(0.18 0.012 150);
  --color-tpt11-glow: #16301c99;
  --color-tpt11-glow: oklch(0.29 0.05 150 / 0.6);
  --color-tpt11-card: #161d17;
  --color-tpt11-card: oklch(0.22 0.015 150);
  --color-tpt11-line: #2a352c;
  --color-tpt11-line: oklch(0.31 0.02 150);
  --color-tpt11-track: #2a342c;
  --color-tpt11-track: oklch(0.31 0.018 150);
  --color-tpt11-ink: #e9efe9;
  --color-tpt11-ink: oklch(0.94 0.01 150);
  --color-tpt11-body: #c3cfc3;
  --color-tpt11-body: oklch(0.84 0.02 150);
  --color-tpt11-mut: #98a699;
  --color-tpt11-mut: oklch(0.7 0.02 150);
  --color-tpt11-acc: #3fc16a;
  --color-tpt11-acc: oklch(0.72 0.17 148);
  --color-tpt11-on-acc: #07140b;
  --color-tpt11-on-acc: oklch(0.17 0.03 150);
  --font-tpt11-sans: 'Geist', system-ui, sans-serif;
  --font-tpt11-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-11 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tpt11-root]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const range = root.querySelector('[data-range]');
    const out = root.querySelector('[data-out]');
    const live = root.querySelector('[data-live]');
    const cards = [...root.querySelectorAll('[data-card]')];
    const TIERS = [
      { name: 'Starter', base: 0, seat: 7 },
      { name: 'Team', base: 49, seat: 5 },
      { name: 'Business', base: 149, seat: 3.5 },
    ];
    const ANNOUNCE_MS = 600;
    let announce = 0;
    const update = () => {
      const seats = +range.value;
      out.textContent = seats;
      range.style.setProperty('--pct', ((seats - range.min) / (range.max - range.min)) * 100 + '%');
      let best = 0, bestPrice = Infinity;
      TIERS.forEach((t, i) => {
        const total = Math.round(t.base + t.seat * seats);
        cards[i].querySelector('[data-amount]').textContent = '$' + total;
        cards[i].querySelector('[data-math]').textContent = (t.base ? '$' + t.base + ' base + ' : '') + '$' + t.seat + ' × ' + seats + (seats === 1 ? ' seat' : ' seats');
        if (total < bestPrice) { bestPrice = total; best = i; }
      });
      cards.forEach((c, i) => c.toggleAttribute('data-best', i === best));
      clearTimeout(announce);
      announce = setTimeout(() => {
        live.textContent = seats + ' seats: best value is ' + TIERS[best].name + ' at $' + bestPrice + ' per month.';
      }, ANNOUNCE_MS);
    };
    range.addEventListener('input', update);
    update();
  });
})();
```
