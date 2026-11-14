---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-two-factor-authentication-setup/"
title: "Tailwind Two-Factor Authentication Setup"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A guided 2FA enrolment wizard: choose an authenticator app or SMS, scan a QR code drawn on a canvas (with a copyable setup key fallback) or enter a phone…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Two-Factor Authentication Setup
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-two-factor-authentication-setup/

A guided 2FA enrolment wizard: choose an authenticator app or SMS, scan a QR code drawn on a canvas (with a copyable setup key fallback) or enter a phone number, type a 6-digit code into an OTP input that auto-advances, spreads pasted codes and shakes on a wrong one, then save ten recovery codes before the Finish button unlocks.
## HTML
```html
<section data-tsp10 data-step="1" class="tsp-10 group/wiz w-full min-h-svh bg-tsp10-bg px-4 py-10 font-tsp10-sans text-tsp10-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-10-h">
  <div class="mx-auto grid w-full max-w-2xl gap-8">
    <header class="grid gap-2">
      <p class="flex items-center gap-2 text-sm font-semibold text-tsp10-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/></svg>Security</p>
      <h1 id="tsp-10-h" class="text-3xl font-semibold tracking-tight">Two-factor authentication</h1>
      <p class="text-pretty text-tsp10-mut">Add a second step at sign-in so a stolen password isn't enough.</p>
    </header>

    <ol class="grid grid-cols-3 gap-2 text-sm font-medium group-data-[step=done]/wiz:hidden" aria-label="Setup progress">
      <li class="grid gap-2"><span class="h-1 rounded-full bg-tsp10-acc"></span><span class="text-tsp10-acc">1 · Method</span></li>
      <li class="grid gap-2"><span class="h-1 rounded-full bg-tsp10-line transition group-data-[step=2]/wiz:bg-tsp10-acc group-data-[step=3]/wiz:bg-tsp10-acc"></span><span class="text-tsp10-mut group-data-[step=2]/wiz:text-tsp10-acc group-data-[step=3]/wiz:text-tsp10-acc">2 · Verify</span></li>
      <li class="grid gap-2"><span class="h-1 rounded-full bg-tsp10-line transition group-data-[step=3]/wiz:bg-tsp10-acc"></span><span class="text-tsp10-mut group-data-[step=3]/wiz:text-tsp10-acc">3 · Backup codes</span></li>
    </ol>

    <form data-form class="rounded-3xl border border-tsp10-line bg-white p-6 shadow-[0_24px_60px_-36px_rgb(30_41_90/0.35)] sm:p-8" novalidate>
      <div class="hidden gap-5 group-data-[step=1]/wiz:grid" data-panel="1">
        <h2 class="text-lg font-semibold">How do you want to get codes?</h2>
        <label class="group/m flex cursor-pointer gap-4 rounded-2xl border border-tsp10-line p-5 transition hover:border-tsp10-acc/40 has-checked:border-tsp10-acc has-checked:bg-tsp10-acc/5 has-checked:ring-4 has-checked:ring-tsp10-acc/10 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp10-acc"><input type="radio" name="method" id="tsp-10-app" value="app" class="sr-only" checked><span class="grid size-11 flex-none place-items-center rounded-xl bg-tsp10-acc/10 text-tsp10-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/></svg></span><span class="grid flex-1 gap-1"><span class="flex flex-wrap items-center gap-2 font-semibold">Authenticator app <span class="rounded-full bg-emerald-100 px-2 py-0.5 text-[11px] font-semibold text-emerald-700">Recommended</span></span><span class="text-sm text-tsp10-mut">1Password, Google Authenticator, Authy or any TOTP app. Works offline.</span></span><span class="mt-1 grid size-5 flex-none place-items-center rounded-full border-2 border-tsp10-line group-has-checked/m:border-tsp10-acc group-has-checked/m:bg-tsp10-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/m:opacity-100"></span></span></label>
        <label class="group/m flex cursor-pointer gap-4 rounded-2xl border border-tsp10-line p-5 transition hover:border-tsp10-acc/40 has-checked:border-tsp10-acc has-checked:bg-tsp10-acc/5 has-checked:ring-4 has-checked:ring-tsp10-acc/10 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp10-acc"><input type="radio" name="method" id="tsp-10-sms" value="sms" class="sr-only"><span class="grid size-11 flex-none place-items-center rounded-xl bg-tsp10-bg text-tsp10-mut"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></span><span class="grid flex-1 gap-1"><span class="font-semibold">Text message (SMS)</span><span class="text-sm text-tsp10-mut">We text a code to your phone. Less secure than an app.</span></span><span class="mt-1 grid size-5 flex-none place-items-center rounded-full border-2 border-tsp10-line group-has-checked/m:border-tsp10-acc group-has-checked/m:bg-tsp10-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/m:opacity-100"></span></span></label>
        <div class="flex justify-end"><button type="button" data-next="2" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp10-ink px-5 text-sm font-semibold text-white transition hover:bg-tsp10-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp10-acc">Continue<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button></div>
      </div>

      <div class="hidden gap-6 group-data-[step=2]/wiz:grid" data-panel="2">
        <div class="grid gap-5 sm:grid-cols-[11rem_1fr] sm:items-center group-has-[#tsp-10-sms:checked]/wiz:hidden">
          <div class="grid place-items-center rounded-2xl border border-tsp10-line bg-white p-3 shadow-sm"><canvas data-qr width="290" height="290" class="size-40 [image-rendering:pixelated]" role="img" aria-label="QR code for your authenticator app"></canvas></div>
          <div class="grid gap-3">
            <h2 class="text-lg font-semibold">Scan with your app</h2>
            <p class="text-sm text-tsp10-mut">Can't scan? Enter this setup key instead:</p>
            <div class="flex items-center gap-2 rounded-xl bg-tsp10-bg p-1.5 pl-3"><code data-key class="min-w-0 flex-1 break-all font-tsp10-mono text-sm font-semibold tracking-wider">JBSW Y3DP EHPK 3PXP</code><button type="button" data-copy class="group/cp inline-flex min-h-11 flex-none items-center rounded-lg bg-white px-3 text-sm font-semibold shadow-xs transition hover:bg-white/70 focus-visible:outline-2 focus-visible:outline-tsp10-acc data-copied:text-emerald-700"><span class="group-data-copied/cp:hidden">Copy</span><span class="hidden group-data-copied/cp:inline">Copied</span></button></div>
          </div>
        </div>
        <div class="hidden gap-3 group-has-[#tsp-10-sms:checked]/wiz:grid">
          <h2 class="text-lg font-semibold">Where should we text the code?</h2>
          <div class="flex gap-2"><select aria-label="Country code" class="min-h-11 rounded-xl border border-tsp10-line bg-white px-2 text-sm outline-none focus:ring-4 focus:ring-tsp10-acc/15"><option>🇺🇸 +1</option><option>🇬🇧 +44</option><option>🇦🇺 +61</option><option>🇨🇦 +1</option></select><input type="tel" autocomplete="tel-national" placeholder="(415) 555-0132" aria-label="Phone number" class="min-h-11 min-w-0 flex-1 rounded-xl border border-tsp10-line px-3.5 text-sm outline-none transition focus:border-tsp10-acc focus:ring-4 focus:ring-tsp10-acc/15"><button type="button" data-sms class="min-h-11 rounded-xl border border-tsp10-line bg-white px-4 text-sm font-semibold shadow-xs transition hover:bg-tsp10-bg focus-visible:outline-2 focus-visible:outline-tsp10-acc data-sent:text-emerald-700">Send code</button></div>
        </div>
        <fieldset data-otp class="group/otp grid gap-3">
          <legend class="mb-3 text-sm font-semibold">Enter the 6-digit code</legend>
          <div class="flex gap-2 group-data-error/otp:animate-tsp10-shake sm:gap-3">
            <input inputmode="numeric" autocomplete="one-time-code" maxlength="1" aria-label="Digit 1 of 6" class="h-14 w-full min-w-0 rounded-xl border border-tsp10-line bg-white text-center font-tsp10-mono text-2xl font-semibold caret-tsp10-acc outline-none transition focus:border-tsp10-acc focus:ring-4 focus:ring-tsp10-acc/15 group-data-error/otp:border-rose-500 group-data-error/otp:text-rose-600 sm:h-16">
            <input inputmode="numeric" maxlength="1" aria-label="Digit 2 of 6" class="h-14 w-full min-w-0 rounded-xl border border-tsp10-line bg-white text-center font-tsp10-mono text-2xl font-semibold caret-tsp10-acc outline-none transition focus:border-tsp10-acc focus:ring-4 focus:ring-tsp10-acc/15 group-data-error/otp:border-rose-500 group-data-error/otp:text-rose-600 sm:h-16">
            <input inputmode="numeric" maxlength="1" aria-label="Digit 3 of 6" class="h-14 w-full min-w-0 rounded-xl border border-tsp10-line bg-white text-center font-tsp10-mono text-2xl font-semibold caret-tsp10-acc outline-none transition focus:border-tsp10-acc focus:ring-4 focus:ring-tsp10-acc/15 group-data-error/otp:border-rose-500 group-data-error/otp:text-rose-600 sm:h-16">
            <span aria-hidden="true" class="grid w-3 flex-none place-items-center text-tsp10-mut">–</span>
            <input inputmode="numeric" maxlength="1" aria-label="Digit 4 of 6" class="h-14 w-full min-w-0 rounded-xl border border-tsp10-line bg-white text-center font-tsp10-mono text-2xl font-semibold caret-tsp10-acc outline-none transition focus:border-tsp10-acc focus:ring-4 focus:ring-tsp10-acc/15 group-data-error/otp:border-rose-500 group-data-error/otp:text-rose-600 sm:h-16">
            <input inputmode="numeric" maxlength="1" aria-label="Digit 5 of 6" class="h-14 w-full min-w-0 rounded-xl border border-tsp10-line bg-white text-center font-tsp10-mono text-2xl font-semibold caret-tsp10-acc outline-none transition focus:border-tsp10-acc focus:ring-4 focus:ring-tsp10-acc/15 group-data-error/otp:border-rose-500 group-data-error/otp:text-rose-600 sm:h-16">
            <input inputmode="numeric" maxlength="1" aria-label="Digit 6 of 6" class="h-14 w-full min-w-0 rounded-xl border border-tsp10-line bg-white text-center font-tsp10-mono text-2xl font-semibold caret-tsp10-acc outline-none transition focus:border-tsp10-acc focus:ring-4 focus:ring-tsp10-acc/15 group-data-error/otp:border-rose-500 group-data-error/otp:text-rose-600 sm:h-16">
          </div>
          <p data-otp-msg role="status" aria-live="polite" class="text-sm text-tsp10-mut group-data-error/otp:font-medium group-data-error/otp:text-rose-600">Demo: any code works except 000000.</p>
        </fieldset>
        <div class="flex justify-between gap-3"><button type="button" data-next="1" class="min-h-11 rounded-xl px-4 text-sm font-semibold text-tsp10-mut transition hover:text-tsp10-ink focus-visible:outline-2 focus-visible:outline-tsp10-acc">Back</button><button type="button" data-verify disabled class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp10-ink px-5 text-sm font-semibold text-white transition hover:bg-tsp10-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp10-acc disabled:cursor-not-allowed disabled:opacity-40">Verify</button></div>
      </div>

      <div class="hidden gap-5 group-data-[step=3]/wiz:grid" data-panel="3">
        <div><h2 class="text-lg font-semibold">Save your recovery codes</h2><p class="mt-1 text-sm text-tsp10-mut">If you lose your phone, each code signs you in once. Store them somewhere safe.</p></div>
        <ol data-codes class="grid grid-cols-2 gap-x-6 gap-y-2 rounded-2xl bg-tsp10-bg p-5 font-tsp10-mono text-sm font-semibold tracking-wider sm:grid-cols-2"></ol>
        <div class="flex flex-wrap gap-2"><button type="button" data-download class="inline-flex min-h-11 items-center gap-2 rounded-xl border border-tsp10-line bg-white px-4 text-sm font-semibold shadow-xs transition hover:bg-tsp10-bg focus-visible:outline-2 focus-visible:outline-tsp10-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg>Download .txt</button><button type="button" data-copy-codes class="group/cp inline-flex min-h-11 items-center gap-2 rounded-xl border border-tsp10-line bg-white px-4 text-sm font-semibold shadow-xs transition hover:bg-tsp10-bg focus-visible:outline-2 focus-visible:outline-tsp10-acc data-copied:text-emerald-700"><span class="group-data-copied/cp:hidden">Copy all</span><span class="hidden group-data-copied/cp:inline">Copied</span></button></div>
        <label class="flex min-h-11 cursor-pointer items-center gap-3 text-sm font-medium"><input type="checkbox" data-ack class="size-4 accent-tsp10-acc">I've stored these codes somewhere safe</label>
        <div class="flex justify-end"><button type="button" data-finish disabled class="inline-flex min-h-11 items-center rounded-xl bg-tsp10-acc px-5 text-sm font-semibold text-white transition hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp10-acc disabled:cursor-not-allowed disabled:opacity-40">Finish setup</button></div>
      </div>

      <div class="hidden justify-items-center gap-4 py-6 text-center group-data-[step=done]/wiz:grid" data-panel="done">
        <span class="grid size-16 place-items-center rounded-full bg-emerald-100 text-emerald-600 ring-8 ring-emerald-50"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-7"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg></span>
        <h2 class="text-xl font-semibold">Two-factor is on</h2>
        <p class="max-w-sm text-pretty text-tsp10-mut">Next time you sign in on a new device we'll ask for a code. You have <strong class="font-semibold text-tsp10-ink">10 recovery codes</strong> left.</p>
        <button type="button" data-next="1" class="min-h-11 rounded-xl border border-tsp10-line bg-white px-5 text-sm font-semibold shadow-xs transition hover:bg-tsp10-bg focus-visible:outline-2 focus-visible:outline-tsp10-acc">Run setup again</button>
      </div>
    </form>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp10-bg: #f3f5fb;
  --color-tsp10-bg: oklch(0.968 0.008 270);
  --color-tsp10-ink: #141a33;
  --color-tsp10-ink: oklch(0.22 0.045 272);
  --color-tsp10-mut: #5b6280;
  --color-tsp10-mut: oklch(0.5 0.042 272);
  --color-tsp10-line: #e1e4f0;
  --color-tsp10-line: oklch(0.92 0.015 272);
  --color-tsp10-acc: #3b5bdb;
  --color-tsp10-acc: oklch(0.52 0.19 268);
  --font-tsp10-sans: 'Onest', system-ui, sans-serif;
  --font-tsp10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tsp10-shake: tsp10-shake 0.4s ease-in-out;

  @keyframes tsp10-shake {
    20%,
        60% {
      transform: translateX(-6px);
    }

    40%,
        80% {
      transform: translateX(6px);
    }
  }
}

.tsp-10 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tsp-10 * {
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-tsp10]');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const CODES = 10;
  const go = (step) => {
    root.dataset.step = step;
    const panel = root.querySelector('[data-panel="' + step + '"]');
    const first = panel && panel.querySelector('input:not([type=radio]):not([type=checkbox]), button');
    if (first) setTimeout(() => first.focus({ preventScroll: true }), 30);
  };
  root.querySelectorAll('[data-next]').forEach((b) => b.addEventListener('click', () => go(b.dataset.next)));
  const cv = root.querySelector('[data-qr]'), ctx = cv.getContext('2d'), N = 29, S = 10;
  let seed = 7;
  const rnd = () => ((seed = (seed * 9301 + 49297) % 233280) / 233280);
  ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, N * S, N * S); ctx.fillStyle = '#141a33';
  const finder = (x, y) => { ctx.fillRect(x * S, y * S, 7 * S, 7 * S); ctx.fillStyle = '#fff'; ctx.fillRect((x + 1) * S, (y + 1) * S, 5 * S, 5 * S); ctx.fillStyle = '#141a33'; ctx.fillRect((x + 2) * S, (y + 2) * S, 3 * S, 3 * S); };
  const inFinder = (x, y) => (x < 8 && y < 8) || (x > N - 9 && y < 8) || (x < 8 && y > N - 9);
  for (let y = 0; y < N; y++) for (let x = 0; x < N; x++) if (!inFinder(x, y) && rnd() > 0.52) ctx.fillRect(x * S, y * S, S, S);
  finder(0, 0); finder(N - 7, 0); finder(0, N - 7);
  const copy = async (text, btn) => {
    try { await navigator.clipboard.writeText(text); } catch (e) {}
    btn.dataset.copied = ''; setTimeout(() => delete btn.dataset.copied, 1500);
  };
  root.querySelector('[data-copy]').addEventListener('click', (e) => copy(root.querySelector('[data-key]').textContent.replaceAll(' ', ''), e.currentTarget));
  const sms = root.querySelector('[data-sms]');
  sms.addEventListener('click', () => { sms.dataset.sent = ''; sms.textContent = 'Sent ✓'; });
  const otp = root.querySelector('[data-otp]');
  const boxes = [...otp.querySelectorAll('input')];
  const verify = root.querySelector('[data-verify]');
  const msg = root.querySelector('[data-otp-msg]');
  const code = () => boxes.map((b) => b.value).join('');
  const refresh = () => { verify.disabled = code().length !== 6; delete otp.dataset.error; msg.textContent = 'Demo: any code works except 000000.'; };
  const spread = (from, digits) => { digits.split('').slice(0, 6 - from).forEach((d, i) => { boxes[from + i].value = d; }); boxes[Math.min(from + digits.length, 5)].focus(); refresh(); };
  boxes.forEach((b, i) => {
    b.addEventListener('input', () => { const d = b.value.replace(/[^0-9]/g, ''); b.value = ''; if (d) spread(i, d); else refresh(); });
    b.addEventListener('keydown', (e) => {
      if (e.key === 'Backspace' && !b.value && i > 0) { boxes[i - 1].value = ''; boxes[i - 1].focus(); refresh(); e.preventDefault(); }
      else if (e.key === 'ArrowLeft' && i > 0) boxes[i - 1].focus();
      else if (e.key === 'ArrowRight' && i < 5) boxes[i + 1].focus();
      else if (e.key === 'Enter' && !verify.disabled) verify.click();
    });
    b.addEventListener('paste', (e) => { e.preventDefault(); spread(i, (e.clipboardData.getData('text') || '').replace(/[^0-9]/g, '')); });
    b.addEventListener('focus', () => b.select());
  });
  const ALPHA = 'abcdefghjkmnpqrstuvwxyz23456789';
  const codes = Array.from({ length: CODES }, () => Array.from(crypto.getRandomValues(new Uint8Array(10)), (n) => ALPHA[n % ALPHA.length]).join('').replace(/(.{5})/, '$1-'));
  const list = root.querySelector('[data-codes]');
  codes.forEach((c) => { const li = document.createElement('li'); li.textContent = c; list.appendChild(li); });
  verify.addEventListener('click', () => {
    if (code() === '000000') {
      otp.dataset.error = '';
      msg.textContent = 'That code didn\'t match. Codes refresh every 30 seconds — try the newest one.';
      boxes.forEach((b) => { b.value = ''; }); boxes[0].focus(); verify.disabled = true;
      return;
    }
    go('3');
  });
  root.querySelector('[data-download]').addEventListener('click', () => {
    const url = URL.createObjectURL(new Blob(['Northwind recovery codes\n\n' + codes.join('\n') + '\n'], { type: 'text/plain' }));
    const a = document.createElement('a'); a.href = url; a.download = 'northwind-recovery-codes.txt'; document.body.appendChild(a); a.click(); a.remove();
  });
  root.querySelector('[data-copy-codes]').addEventListener('click', (e) => copy(codes.join('\n'), e.currentTarget));
  const ack = root.querySelector('[data-ack]'), finish = root.querySelector('[data-finish]');
  ack.addEventListener('change', () => { finish.disabled = !ack.checked; });
  finish.addEventListener('click', () => { go('done'); boxes.forEach((b) => { b.value = ''; }); ack.checked = false; finish.disabled = true; verify.disabled = true; });
})();
```
