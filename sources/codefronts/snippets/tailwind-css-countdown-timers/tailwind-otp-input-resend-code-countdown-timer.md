---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-otp-input-resend-code-countdown-timer/"
title: "Tailwind OTP Input with Resend Code Countdown Timer"
section: "snippets"
category: "tailwind-css-countdown-timers"
category_name: "Tailwind CSS Countdown Timers"
description: "The verification screen every auth flow needs: six code cells with autocomplete=\"one-time-code\", a resend control that stays disabled behind an inline…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind OTP Input with Resend Code Countdown Timer
Source: https://codefronts.com/snippets/tailwind-css-countdown-timers/tailwind-otp-input-resend-code-countdown-timer/

The verification screen every auth flow needs: six code cells with autocomplete="one-time-code", a resend control that stays disabled behind an inline countdown and backs off exponentially, and a live region that speaks once &mdash; when resend is usable again. New in the port: paste-to-fill, Backspace navigation, a verify button that only enables at six digits, and attempt pips showing the next wait.
## HTML
```html
<section class="tcd-05 group/root w-full min-h-svh grid place-items-center bg-tcd05-page bg-[radial-gradient(70%_60%_at_50%_0%,var(--color-tcd05-glow),transparent_70%)] px-4 py-12 font-tcd05-sans text-tcd05-ink antialiased" data-tries="1" aria-labelledby="tcd-05-title">
  <article class="w-full max-w-[440px] rounded-3xl border border-tcd05-rule bg-tcd05-card p-[clamp(22px,5vw,36px)] shadow-tcd05-card transition duration-500 starting:translate-y-2 starting:opacity-0">
    <div class="mb-6 flex items-center gap-2 font-tcd05-display text-[13px] font-bold tracking-[0.02em] text-tcd05-acc">
      <span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-tcd05-acc/10"><svg viewBox="0 0 24 24" width="18" height="18"><rect x="4" y="10" width="16" height="10.5" rx="2.4" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8.2 10V7.6a3.8 3.8 0 0 1 7.6 0V10" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></span>
      Sable ID
    </div>
    <h2 id="tcd-05-title" class="mb-2 font-tcd05-display text-[clamp(22px,4vw,28px)] font-bold leading-tight tracking-[-0.02em] text-balance">Enter your verification code</h2>
    <p class="mb-6 text-[14px] leading-relaxed text-tcd05-mut text-pretty">We sent a six-digit code to <strong class="font-semibold text-tcd05-ink">a•••@meridian.co</strong>. It expires in ten minutes.</p>

    <div role="group" aria-label="Six digit verification code" class="grid grid-cols-6 gap-[clamp(5px,1.6vw,9px)]">
      <input data-cell type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" placeholder=" " aria-label="Digit 1" value="4" class="aspect-[3/4] w-full min-w-0 rounded-xl border-[1.5px] border-tcd05-rule bg-transparent p-0 text-center font-tcd05-display text-[clamp(20px,5.4vw,26px)] font-bold tabular-nums transition caret-tcd05-acc not-placeholder-shown:border-tcd05-acc not-placeholder-shown:bg-tcd05-acc/5 focus-visible:border-tcd05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc/40">
      <input data-cell type="text" inputmode="numeric" maxlength="1" placeholder=" " aria-label="Digit 2" value="1" class="aspect-[3/4] w-full min-w-0 rounded-xl border-[1.5px] border-tcd05-rule bg-transparent p-0 text-center font-tcd05-display text-[clamp(20px,5.4vw,26px)] font-bold tabular-nums transition caret-tcd05-acc not-placeholder-shown:border-tcd05-acc not-placeholder-shown:bg-tcd05-acc/5 focus-visible:border-tcd05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc/40">
      <input data-cell type="text" inputmode="numeric" maxlength="1" placeholder=" " aria-label="Digit 3" value="9" class="aspect-[3/4] w-full min-w-0 rounded-xl border-[1.5px] border-tcd05-rule bg-transparent p-0 text-center font-tcd05-display text-[clamp(20px,5.4vw,26px)] font-bold tabular-nums transition caret-tcd05-acc not-placeholder-shown:border-tcd05-acc not-placeholder-shown:bg-tcd05-acc/5 focus-visible:border-tcd05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc/40">
      <input data-cell type="text" inputmode="numeric" maxlength="1" placeholder=" " aria-label="Digit 4" class="aspect-[3/4] w-full min-w-0 rounded-xl border-[1.5px] border-tcd05-rule bg-transparent p-0 text-center font-tcd05-display text-[clamp(20px,5.4vw,26px)] font-bold tabular-nums transition caret-tcd05-acc not-placeholder-shown:border-tcd05-acc not-placeholder-shown:bg-tcd05-acc/5 focus-visible:border-tcd05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc/40">
      <input data-cell type="text" inputmode="numeric" maxlength="1" placeholder=" " aria-label="Digit 5" class="aspect-[3/4] w-full min-w-0 rounded-xl border-[1.5px] border-tcd05-rule bg-transparent p-0 text-center font-tcd05-display text-[clamp(20px,5.4vw,26px)] font-bold tabular-nums transition caret-tcd05-acc not-placeholder-shown:border-tcd05-acc not-placeholder-shown:bg-tcd05-acc/5 focus-visible:border-tcd05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc/40">
      <input data-cell type="text" inputmode="numeric" maxlength="1" placeholder=" " aria-label="Digit 6" class="aspect-[3/4] w-full min-w-0 rounded-xl border-[1.5px] border-tcd05-rule bg-transparent p-0 text-center font-tcd05-display text-[clamp(20px,5.4vw,26px)] font-bold tabular-nums transition caret-tcd05-acc not-placeholder-shown:border-tcd05-acc not-placeholder-shown:bg-tcd05-acc/5 focus-visible:border-tcd05-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-acc/40">
    </div>

    <button type="button" data-verify disabled class="mt-5 min-h-12 w-full cursor-pointer rounded-xl bg-tcd05-acc px-4 font-tcd05-display text-[15px] font-bold text-white shadow-[0_10px_22px_-12px_var(--color-tcd05-acc)] transition hover:brightness-110 active:scale-[0.99] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tcd05-ink disabled:cursor-not-allowed disabled:bg-tcd05-rule disabled:text-tcd05-mut disabled:shadow-none">Verify and continue</button>

    <div role="timer" class="mt-5 grid gap-2 border-t border-tcd05-rule pt-5">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <button type="button" data-resend disabled class="-mx-2 inline-flex min-h-11 cursor-pointer items-center gap-1.5 rounded-lg px-2 text-sm font-semibold tabular-nums text-tcd05-acc underline-offset-4 transition enabled:hover:underline focus-visible:outline-2 focus-visible:outline-tcd05-acc disabled:cursor-not-allowed disabled:text-tcd05-mut">Resend code in <time datetime="" data-clock>0:29</time></button>
        <span aria-hidden="true" class="flex items-center gap-1.5 text-[11px] font-medium text-tcd05-mut">
          <span class="size-1.5 rounded-full bg-tcd05-acc"></span>
          <span class="size-1.5 rounded-full bg-tcd05-rule group-data-[tries=2]/root:bg-tcd05-acc group-data-[tries=3]/root:bg-tcd05-acc"></span>
          <span class="size-1.5 rounded-full bg-tcd05-rule group-data-[tries=3]/root:bg-tcd05-acc"></span>
          <span data-next class="ml-1">next wait 1:00</span>
        </span>
      </div>
      <p class="text-[12.5px] leading-relaxed text-tcd05-mut text-pretty">Didn't arrive? Check spam before requesting another — each request waits longer.</p>
    </div>
    <output data-live aria-live="polite" class="mt-1 block min-h-[1.2em] text-[13px] font-semibold text-tcd05-ok"></output>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcd05-page: #f6f1e9;
  --color-tcd05-page: oklch(0.96 0.018 80);
  --color-tcd05-glow: #efe6ff;
  --color-tcd05-glow: oklch(0.94 0.04 300);
  --color-tcd05-card: #fffdf9;
  --color-tcd05-card: oklch(0.99 0.008 85);
  --color-tcd05-ink: #241f2e;
  --color-tcd05-ink: oklch(0.25 0.03 300);
  --color-tcd05-mut: #615a72;
  --color-tcd05-mut: oklch(0.48 0.03 300);
  --color-tcd05-rule: #e6dfd3;
  --color-tcd05-rule: oklch(0.9 0.016 80);
  --color-tcd05-acc: #6b3df0;
  --color-tcd05-acc: oklch(0.52 0.24 292);
  --color-tcd05-ok: #2f7d54;
  --color-tcd05-ok: oklch(0.52 0.11 155);
  --font-tcd05-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tcd05-sans: 'Figtree', system-ui, sans-serif;
  --shadow-tcd05-card: 0 1px 2px rgb(36 31 46 / 0.04), 0 26px 50px -30px rgb(36 31 46 / 0.45);
}

.tcd-05 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tcd-05');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const q = (s) => root.querySelector(s);
  const btn = q('[data-resend]'), live = q('[data-live]'), verify = q('[data-verify]'), next = q('[data-next]');
  const cells = [...root.querySelectorAll('[data-cell]')];
  const fmt = (s) => Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
  let wait = 29e3, target = Date.now() + wait, id = 0, tries = 1;
  const sync = () => { verify.disabled = cells.some((c) => !c.value); };
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    const clock = btn.querySelector('[data-clock]');
    if (clock) { clock.textContent = fmt(s); clock.dateTime = new Date(target).toISOString(); }
    if (ms > 0) { id = setTimeout(tick, 1000 - (Date.now() % 1000)); return; }
    btn.disabled = false;
    btn.textContent = 'Resend code';
    live.textContent = 'You can request a new code now.';
  };
  const start = () => {
    wait = Math.min(Math.max(wait, 30e3) * 2, 120e3); target = Date.now() + wait;
    tries = Math.min(tries + 1, 3); root.dataset.tries = String(tries);
    next.textContent = tries >= 3 ? 'max wait 2:00' : 'next wait ' + fmt(Math.min(wait * 2, 120e3) / 1000);
    btn.disabled = true; live.textContent = 'New code sent.';
    btn.innerHTML = 'Resend code in <time data-clock></time>';
    clearTimeout(id); tick();
  };
  btn.addEventListener('click', () => { if (!btn.disabled) start(); });
  cells.forEach((c, i) => {
    c.addEventListener('input', () => {
      const digits = c.value.replace(/\D/g, '');
      if (digits.length > 1) {
        digits.slice(0, cells.length - i).split('').forEach((d, k) => { cells[i + k].value = d; });
        cells[Math.min(i + digits.length, cells.length) - 1].focus();
      } else {
        c.value = digits;
        if (digits && cells[i + 1]) cells[i + 1].focus();
      }
      sync();
    });
    c.addEventListener('keydown', (e) => {
      if (e.key === 'Backspace' && !c.value && cells[i - 1]) { cells[i - 1].focus(); cells[i - 1].value = ''; sync(); e.preventDefault(); }
      if (e.key === 'ArrowLeft' && cells[i - 1]) cells[i - 1].focus();
      if (e.key === 'ArrowRight' && cells[i + 1]) cells[i + 1].focus();
    });
  });
  verify.addEventListener('click', () => { live.textContent = 'Code verified. Signing you in.'; verify.textContent = 'Verified ✓'; });
  sync(); tick();
  root.cleanup = () => clearTimeout(id);
})();
```
