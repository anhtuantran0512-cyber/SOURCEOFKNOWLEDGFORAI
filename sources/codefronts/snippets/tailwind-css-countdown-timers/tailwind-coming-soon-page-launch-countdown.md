---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-coming-soon-page-launch-countdown/"
title: "Tailwind Coming Soon Page with Launch Countdown Timer"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "The classic pre-launch splash, rebuilt: a wordmark, one serif headline, four frosted unit tiles for days, hours, minutes and seconds, and a single email field."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Coming Soon Page with Launch Countdown Timer
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-coming-soon-page-launch-countdown/

The classic pre-launch splash, rebuilt: a wordmark, one serif headline, four frosted unit tiles for days, hours, minutes and seconds, and a single email field. Where most versions stall at zero, this one flips the whole page to a live state via data-live. New in the port: Notify me validates and confirms in place via data-subscribed, and the waiting count updates.
## HTML
```html
<section class="tcd-20 group/root w-full min-h-svh bg-[linear-gradient(150deg,var(--color-tcd20-fa),var(--color-tcd20-fb)_70%,var(--color-tcd20-fc))] font-tcd20-sans text-tcd20-ink antialiased" aria-labelledby="tcd-20-title">
  <div class="mx-auto grid min-h-svh max-w-[880px] content-center justify-items-center gap-[clamp(22px,4vw,36px)] px-[clamp(18px,5vw,56px)] py-14 text-center">
    <p class="flex items-center gap-2 text-sm font-bold tracking-[0.28em] uppercase"><span aria-hidden="true" class="size-3 rounded-full border-[3px] border-tcd20-ink"></span>Aperture</p>

    <div class="grid justify-items-center gap-3 transition duration-700 starting:translate-y-2 starting:opacity-0">
      <h2 id="tcd-20-title" class="font-tcd20-serif text-[clamp(40px,8vw,76px)] leading-[0.98] tracking-[-0.02em] text-balance"><span class="group-data-live/root:hidden">The archive opens <em>in</em></span><span class="hidden group-data-live/root:inline">The archive is <em>open</em></span></h2>
      <p class="max-w-[46ch] text-[15.5px] leading-relaxed text-tcd20-mut text-pretty"><span class="group-data-live/root:hidden">Forty years of Meridian's print catalogue, scanned, indexed and free to read.</span><span class="hidden group-data-live/root:inline">Forty years of print, indexed and searchable. Start anywhere.</span></p>
    </div>

    <div role="timer" class="w-full">
      <time datetime="" data-clock class="mx-auto grid max-w-[620px] grid-cols-4 gap-[clamp(6px,2vw,14px)] tabular-nums group-data-live/root:hidden">
        <span class="grid gap-1.5 rounded-2xl border border-tcd20-ink/10 bg-white/70 py-[clamp(12px,3vw,22px)] shadow-[0_20px_40px_-30px_rgb(20_18_26/0.5)] supports-[backdrop-filter:blur(1px)]:bg-white/50 supports-[backdrop-filter:blur(1px)]:backdrop-blur-md"><b data-d class="font-tcd20-serif text-[clamp(38px,10vw,76px)] font-normal leading-none">04</b><i class="text-[10px] font-bold not-italic uppercase tracking-[0.18em] text-tcd20-mut">days</i></span>
        <span class="grid gap-1.5 rounded-2xl border border-tcd20-ink/10 bg-white/70 py-[clamp(12px,3vw,22px)] shadow-[0_20px_40px_-30px_rgb(20_18_26/0.5)] supports-[backdrop-filter:blur(1px)]:bg-white/50 supports-[backdrop-filter:blur(1px)]:backdrop-blur-md"><b data-h class="font-tcd20-serif text-[clamp(38px,10vw,76px)] font-normal leading-none">11</b><i class="text-[10px] font-bold not-italic uppercase tracking-[0.18em] text-tcd20-mut">hours</i></span>
        <span class="grid gap-1.5 rounded-2xl border border-tcd20-ink/10 bg-white/70 py-[clamp(12px,3vw,22px)] shadow-[0_20px_40px_-30px_rgb(20_18_26/0.5)] supports-[backdrop-filter:blur(1px)]:bg-white/50 supports-[backdrop-filter:blur(1px)]:backdrop-blur-md"><b data-m class="font-tcd20-serif text-[clamp(38px,10vw,76px)] font-normal leading-none">28</b><i class="text-[10px] font-bold not-italic uppercase tracking-[0.18em] text-tcd20-mut">minutes</i></span>
        <span class="grid gap-1.5 rounded-2xl border border-tcd20-ink/10 bg-tcd20-ink py-[clamp(12px,3vw,22px)] text-white shadow-[0_20px_40px_-24px_rgb(20_18_26/0.7)]"><b data-s class="font-tcd20-serif text-[clamp(38px,10vw,76px)] font-normal leading-none">05</b><i class="text-[10px] font-bold not-italic uppercase tracking-[0.18em] text-white/70">seconds</i></span>
      </time>
      <p class="hidden items-center justify-center gap-2.5 font-tcd20-serif text-[clamp(26px,5vw,38px)] italic group-data-live/root:flex"><span aria-hidden="true" class="size-3 rounded-full bg-tcd20-ok animate-pulse motion-reduce:animate-none"></span>We're live — start reading</p>
    </div>

    <form data-form novalidate class="group/form grid w-full max-w-[480px] gap-2 text-left">
      <div class="grid gap-2 group-data-subscribed/form:hidden">
        <label for="tcd-20-email" class="text-[13px] font-semibold"><span class="group-data-live/root:hidden">Email me when it opens</span><span class="hidden group-data-live/root:inline">Get the weekly reading list</span></label>
        <div class="flex flex-wrap gap-2.5">
          <input id="tcd-20-email" type="email" inputmode="email" autocomplete="email" required placeholder="[email protected]" class="peer min-h-12 min-w-0 flex-[1_1_220px] rounded-xl border border-tcd20-ink/20 bg-white/80 px-4 text-[15px] placeholder:text-tcd20-mut/70 transition focus-visible:border-tcd20-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd20-ink/30 user-invalid:border-tcd20-danger">
          <button type="submit" class="min-h-12 cursor-pointer rounded-xl bg-tcd20-ink px-5 text-[15px] font-semibold text-white transition hover:bg-tcd20-ink/88 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd20-ink"><span class="group-data-live/root:hidden">Notify me</span><span class="hidden group-data-live/root:inline">Subscribe</span></button>
          <p class="hidden w-full text-[12.5px] font-medium text-tcd20-danger peer-user-invalid:block">Enter a valid email address.</p>
        </div>
      </div>
      <p class="hidden items-center gap-2.5 rounded-xl border border-tcd20-ok/30 bg-tcd20-ok/10 px-4 py-3.5 text-[14px] font-semibold text-tcd20-ok-ink group-data-subscribed/form:flex transition duration-500 starting:opacity-0"><svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M3 8.4 6.4 11.5 13 4.8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span data-thanks>You're on the list — one email on launch day.</span></p>
      <p class="text-center text-[12.5px] text-tcd20-mut">No newsletter, one message on launch day. <b data-count class="font-semibold text-tcd20-ink">2,140</b> people waiting.</p>
    </form>
    <output data-live aria-live="polite" class="sr-only"></output>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd20-fa: #e7e2ff;
  --color-tcd20-fa: oklch(0.91 0.05 295);
  --color-tcd20-fb: #d9f2e6;
  --color-tcd20-fb: oklch(0.93 0.05 160);
  --color-tcd20-fc: #fdfbf6;
  --color-tcd20-fc: oklch(0.99 0.008 90);
  --color-tcd20-ink: #14121a;
  --color-tcd20-ink: oklch(0.17 0.02 290);
  --color-tcd20-mut: #534f68;
  --color-tcd20-mut: oklch(0.43 0.03 290);
  --color-tcd20-ok: #1f8a57;
  --color-tcd20-ok: oklch(0.55 0.13 155);
  --color-tcd20-ok-ink: #14603b;
  --color-tcd20-ok-ink: oklch(0.42 0.1 155);
  --color-tcd20-danger: #b3261e;
  --color-tcd20-danger: oklch(0.5 0.19 27);
  --font-tcd20-serif: 'Instrument Serif', Georgia, serif;
  --font-tcd20-sans: 'Instrument Sans', system-ui, sans-serif;
}

.tcd-20 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-20');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const clock = q('[data-clock]'), live = q('[data-live]'), form = q('[data-form]'), email = q('#tcd-20-email');
  const pad = (n) => String(n).padStart(2, '0');
  const target = new Date(Date.now() + 4 * 86400e3 + 11 * 3600e3 + 28 * 60e3 + 5e3);
  let id = 0, seen = null, count = 2140;
  clock.dateTime = target.toISOString();
  const tick = () => {
    const ms = target - Date.now();
    if (ms <= 0) { root.setAttribute('data-live', ''); live.textContent = 'The archive is now open.'; return; }
    const s = Math.floor(ms / 1000);
    q('[data-d]').textContent = pad(Math.floor(s / 86400));
    q('[data-h]').textContent = pad(Math.floor(s / 3600) % 24);
    q('[data-m]').textContent = pad(Math.floor(s / 60) % 60);
    q('[data-s]').textContent = pad(s % 60);
    const b = ms < 60e3 ? 'm1' : ms < 3600e3 ? 'h1' : ms < 86400e3 ? 'd1' : 'far';
    if (b !== seen) { seen = b; live.textContent = { far: '', d1: 'The archive opens within a day.', h1: 'The archive opens within the hour.', m1: 'The archive opens in one minute.' }[b]; }
    id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!email.value || !email.checkValidity()) { email.focus(); live.textContent = 'Enter a valid email address.'; return; }
    count += 1; q('[data-count]').textContent = count.toLocaleString();
    q('[data-thanks]').textContent = "You're on the list — we'll email " + email.value + ' on launch day.';
    form.setAttribute('data-subscribed', '');
    live.textContent = 'Subscribed. You will get one email on launch day.';
  });
  tick();
  root.cleanup = () => clearTimeout(id);
})();
```
