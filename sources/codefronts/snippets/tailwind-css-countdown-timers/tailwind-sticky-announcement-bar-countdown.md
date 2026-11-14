---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-sticky-announcement-bar-countdown/"
title: "Tailwind Sticky Announcement Bar with Countdown Timer"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "A site-wide sticky bar where the timer, not the message, is the dominant element: oversized tabular digits, one line of offer copy, a compact CTA and a real…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Announcement Bar with Countdown Timer
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-sticky-announcement-bar-countdown/

A site-wide sticky bar where the timer, not the message, is the dominant element: oversized tabular digits, one line of offer copy, a compact CTA and a real dismiss button. It sticks inside its scroll container and reflows to two lines on phones. New in the port: dismiss animates closed via data-dismissed:grid-rows-[0fr] and moves focus to the page heading, and the final ten minutes pulse via data-urgent:.
## HTML
```html
<section class="tcd-18 w-full min-h-svh bg-tcd18-page font-tcd18-sans text-tcd18-ink antialiased" aria-labelledby="tcd-18-title">
  <div class="h-svh overflow-y-auto">
    <div data-bar role="timer" class="sticky top-0 z-10 grid grid-rows-[1fr] transition-[grid-template-rows] duration-300 ease-out data-dismissed:grid-rows-[0fr] motion-reduce:transition-none">
      <div class="min-h-0 overflow-hidden">
        <div data-inner class="group/bar grid grid-cols-[auto_minmax(0,1fr)_auto_auto] items-center gap-x-4 gap-y-2 bg-tcd18-bar px-[clamp(12px,3vw,24px)] py-2.5 text-tcd18-barink max-sm:grid-cols-[auto_minmax(0,1fr)_auto]">
          <time datetime="" data-clock aria-hidden="true" class="flex items-baseline gap-0.5 font-tcd18-mono text-[clamp(22px,4vw,30px)] font-bold leading-none tabular-nums group-data-urgent/bar:animate-pulse group-data-urgent/bar:text-tcd18-acc motion-reduce:animate-none"><b data-h>01</b><span class="opacity-40">:</span><b data-m>59</b><span class="opacity-40">:</span><b data-s class="text-tcd18-acc">07</b></time>
          <p data-copy class="min-w-0 text-[13.5px] leading-snug font-medium text-pretty max-sm:col-span-full max-sm:row-start-2">Free next-day shipping on everything — ends when the clock does.</p>
          <button type="button" data-cta class="min-h-10 cursor-pointer rounded-full bg-tcd18-acc px-4 text-[13px] font-bold whitespace-nowrap text-tcd18-bar transition hover:brightness-105 active:scale-[0.97] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd18-acc max-sm:col-start-2 max-sm:row-start-1 max-sm:justify-self-end">Shop the drop</button>
          <button type="button" data-close class="grid size-11 cursor-pointer place-items-center rounded-full text-tcd18-barink/70 transition hover:bg-white/10 hover:text-tcd18-barink focus-visible:outline-2 focus-visible:outline-tcd18-acc max-sm:col-start-3 max-sm:row-start-1"><span class="sr-only">Dismiss the offer bar</span><svg viewBox="0 0 14 14" width="13" height="13" aria-hidden="true"><path d="M2.5 2.5l9 9M11.5 2.5l-9 9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>
        </div>
      </div>
    </div>

    <div class="mx-auto max-w-[920px] px-[clamp(16px,4vw,40px)] pt-6 pb-16">
      <header aria-hidden="true" class="mb-10 flex flex-wrap items-center gap-x-6 gap-y-2 border-b border-tcd18-rule pb-4 text-sm text-tcd18-mut"><strong class="mr-auto text-base font-extrabold text-tcd18-ink">Fern Supply</strong><span>New</span><span>Workshop</span><span>Journal</span><span class="rounded-full bg-tcd18-ink px-3 py-1 text-xs font-bold text-white">Cart · 2</span></header>
      <h2 id="tcd-18-title" tabindex="-1" class="mb-3 text-[clamp(26px,4.6vw,40px)] font-extrabold leading-[1.05] tracking-[-0.025em] text-balance focus:outline-none">Scroll — the bar stays, the timer keeps counting</h2>
      <p class="mb-8 max-w-[60ch] text-[15px] leading-relaxed text-tcd18-mut text-pretty">The bar is sticky inside this scroll container, which is where the pattern usually breaks: an <code class="rounded bg-tcd18-rule px-1 py-0.5 font-tcd18-mono text-[12.5px] text-tcd18-ink">overflow: hidden</code> ancestor between the bar and the scroll root disables sticky entirely.</p>
      <div aria-hidden="true" class="grid grid-cols-2 gap-4 sm:grid-cols-3">
        <div class="grid gap-2"><span class="aspect-[4/5] rounded-2xl bg-tcd18-tile"></span><span class="h-3 w-3/4 rounded bg-tcd18-rule"></span><span class="h-3 w-1/3 rounded bg-tcd18-rule"></span></div>
        <div class="grid gap-2"><span class="aspect-[4/5] rounded-2xl bg-tcd18-tile"></span><span class="h-3 w-2/3 rounded bg-tcd18-rule"></span><span class="h-3 w-1/4 rounded bg-tcd18-rule"></span></div>
        <div class="grid gap-2"><span class="aspect-[4/5] rounded-2xl bg-tcd18-tile"></span><span class="h-3 w-3/5 rounded bg-tcd18-rule"></span><span class="h-3 w-1/3 rounded bg-tcd18-rule"></span></div>
        <div class="grid gap-2"><span class="aspect-[4/5] rounded-2xl bg-tcd18-tile"></span><span class="h-3 w-3/4 rounded bg-tcd18-rule"></span><span class="h-3 w-1/4 rounded bg-tcd18-rule"></span></div>
        <div class="grid gap-2"><span class="aspect-[4/5] rounded-2xl bg-tcd18-tile"></span><span class="h-3 w-1/2 rounded bg-tcd18-rule"></span><span class="h-3 w-1/3 rounded bg-tcd18-rule"></span></div>
        <div class="grid gap-2"><span class="aspect-[4/5] rounded-2xl bg-tcd18-tile"></span><span class="h-3 w-2/3 rounded bg-tcd18-rule"></span><span class="h-3 w-1/4 rounded bg-tcd18-rule"></span></div>
      </div>
      <p class="mt-10 text-[13px] text-tcd18-mut">At zero the bar swaps to a closed state in place rather than disappearing and shifting the page under you.</p>
      <output data-live aria-live="polite" class="sr-only"></output>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd18-page: #f5f5f2;
  --color-tcd18-page: oklch(0.965 0.004 100);
  --color-tcd18-bar: #17181a;
  --color-tcd18-bar: oklch(0.19 0.006 260);
  --color-tcd18-barink: #f7f8f4;
  --color-tcd18-barink: oklch(0.97 0.008 100);
  --color-tcd18-ink: #17181a;
  --color-tcd18-ink: oklch(0.2 0.006 260);
  --color-tcd18-mut: #5d5f63;
  --color-tcd18-mut: oklch(0.47 0.008 260);
  --color-tcd18-rule: #e2e2dd;
  --color-tcd18-rule: oklch(0.91 0.006 100);
  --color-tcd18-tile: #e8e8e2;
  --color-tcd18-tile: oklch(0.925 0.008 100);
  --color-tcd18-acc: #c8f52e;
  --color-tcd18-acc: oklch(0.9 0.19 120);
  --font-tcd18-sans: 'Archivo', system-ui, sans-serif;
  --font-tcd18-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tcd-18 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-18');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const bar = q('[data-bar]'), inner = q('[data-inner]'), clock = q('[data-clock]'), live = q('[data-live]');
  const pad = (n) => String(n).padStart(2, '0');
  const target = new Date(Date.now() + 3600e3 + 59 * 60e3 + 7e3);
  let id = 0, seen = null;
  clock.dateTime = target.toISOString();
  const tick = () => {
    const ms = target - Date.now();
    if (ms <= 0) {
      inner.removeAttribute('data-urgent');
      clock.innerHTML = '<b>Closed</b>';
      q('[data-copy]').textContent = 'Free shipping has ended — standard rates apply.';
      q('[data-cta]').textContent = 'Browse the range';
      live.textContent = 'The free shipping offer has closed.';
      return;
    }
    const s = Math.floor(ms / 1000);
    q('[data-h]').textContent = pad(Math.floor(s / 3600));
    q('[data-m]').textContent = pad(Math.floor(s / 60) % 60);
    q('[data-s]').textContent = pad(s % 60);
    inner.toggleAttribute('data-urgent', ms <= 600e3);
    const b = ms < 60e3 ? 'm1' : ms < 600e3 ? 'm10' : 'far';
    if (b !== seen) { seen = b; live.textContent = { far: '', m10: 'Ten minutes left for free next-day shipping.', m1: 'One minute left for free next-day shipping.' }[b]; }
    id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  q('[data-close]').addEventListener('click', () => {
    clearTimeout(id);
    bar.setAttribute('data-dismissed', '');
    bar.setAttribute('aria-hidden', 'true');
    q('#tcd-18-title').focus({ preventScroll: true });
    live.textContent = 'Offer bar dismissed.';
  });
  tick();
  root.cleanup = () => clearTimeout(id);
})();
```
