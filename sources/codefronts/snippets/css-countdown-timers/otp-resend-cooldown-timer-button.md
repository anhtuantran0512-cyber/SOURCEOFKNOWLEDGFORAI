---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/otp-resend-cooldown-timer-button/"
title: "OTP Resend Cooldown Timer Button"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "The resend cooldown every auth flow needs: after a one-time code is sent the resend control goes disabled with an inline countdown, then re-enables itself."
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: OTP Resend Cooldown Timer Button
Source: https://codefronts.com/snippets/css-countdown-timers/otp-resend-cooldown-timer-button/

The resend cooldown every auth flow needs: after a one-time code is sent the resend control goes disabled with an inline countdown, then re-enables itself. The live region stays silent through the count and speaks once when the button becomes usable again, which is the only moment a screen-reader user needs to hear about.
## HTML
```html
<section class="cdt-05" aria-labelledby="cdt-05-title">
  <input class="cdt-05__tgl" type="checkbox" id="cdt-05-theme">
  <label class="cdt-05__tglbtn" for="cdt-05-theme">
    <svg class="cdt-05__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-05__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-05__darktext">Dark mode</span><span class="cdt-05__lighttext">Light mode</span>
  </label>
  <div class="cdt-05__stage">
    <article class="cdt-05__card">
      <div class="cdt-05__mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="20" height="20"><rect x="4" y="10" width="16" height="10.5" rx="2.4" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8.2 10V7.6a3.8 3.8 0 0 1 7.6 0V10" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>
        Sable ID
      </div>
      <h2 class="cdt-05__title" id="cdt-05-title">Enter your verification code</h2>
      <p class="cdt-05__sub">We sent a six-digit code to <strong>a•••@meridian.co</strong>. It expires in ten minutes.</p>

      <div class="cdt-05__cells" role="group" aria-label="Six digit verification code">
        <input class="cdt-05__cell" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="1" aria-label="Digit 1" value="4">
        <input class="cdt-05__cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 2" value="1">
        <input class="cdt-05__cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 3" value="9">
        <input class="cdt-05__cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 4">
        <input class="cdt-05__cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 5">
        <input class="cdt-05__cell" type="text" inputmode="numeric" maxlength="1" aria-label="Digit 6">
      </div>

      <button class="cdt-05__verify" type="button">Verify and continue</button>

      <div class="cdt-05__resend" role="timer">
        <button class="cdt-05__link" type="button" data-resend disabled aria-disabled="true">
          Resend code in <time datetime="" data-clock>0:29</time>
        </button>
        <p class="cdt-05__hint" data-hint>Didn't arrive? Check spam before requesting another — each request waits longer.</p>
      </div>
      <output class="cdt-05__live" aria-live="polite" data-live></output>
    </article>
  </div>
</section>
```
## CSS
```css
.cdt-05 {
  --page: #f6f1e9;
  --card: #fffdf9;
  --ink: #241f2e;
  --muted: #6f6880;
  --rule: #e6dfd3;
  --accent: #6b3df0;
  --ok: #2f7d54;
  --font-display: "Optima", "Gill Sans", "Segoe UI", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, sans-serif;
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-05 {
    --page: oklch(96% 0.018 80);
    --card: oklch(99% 0.008 85);
    --ink: oklch(25% 0.03 300);
    --muted: oklch(52% 0.03 300);
    --rule: oklch(90% 0.016 80);
    --accent: oklch(52% 0.24 292);
    --ok: oklch(52% 0.11 155);
  }
}

.cdt-05 *,
.cdt-05 *::before,
.cdt-05 *::after {
  box-sizing: border-box;
}

.cdt-05__stage {
  display: grid;
  place-content: center;
  justify-items: center;
  min-height: 100vh;
  padding: clamp(16px, 5vw, 48px);
}

.cdt-05__card {
  inline-size: min(440px, 100%);
  padding: clamp(22px, 5vw, 36px);
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 18px;
  box-shadow: 0 18px 40px -28px rgba(36, 31, 46, 0.45);
}

.cdt-05__mark {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-block-end: 20px;
  font: 600 13px/1 var(--font-display);
  letter-spacing: 0.02em;
  color: var(--accent);
}

.cdt-05__title {
  margin: 0 0 8px;
  font: 600 clamp(21px, 4vw, 27px)/1.2 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.cdt-05__sub {
  margin: 0 0 24px;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-05__sub strong {
  color: var(--ink);
  font-weight: 600;
}

.cdt-05__cells {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: clamp(5px, 1.6vw, 9px);
}

.cdt-05__cell {
  min-inline-size: 0;
  inline-size: 100%;
  aspect-ratio: 3 / 4;
  padding: 0;
  text-align: center;
  border: 1.5px solid var(--rule);
  border-radius: 10px;
  background: transparent;
  color: var(--ink);
  font: 600 clamp(19px, 5.4vw, 25px)/1 var(--font-display);
  font-variant-numeric: tabular-nums;
}

.cdt-05__cell:not(:placeholder-shown),
.cdt-05__cell[value]:not([value=""]) {
  border-color: var(--accent);
}

.cdt-05__cell:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-color: var(--accent);
}

.cdt-05__verify {
  inline-size: 100%;
  min-block-size: 48px;
  margin-block-start: 20px;
  padding: 13px 18px;
  border: 0;
  border-radius: 11px;
  background: var(--accent);
  color: #fff;
  font: 600 14.5px/1 var(--font-display);
  cursor: pointer;
}

.cdt-05__verify:hover {
  filter: brightness(1.07);
}

.cdt-05__verify:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.cdt-05__resend {
  margin-block-start: 20px;
  padding-block-start: 18px;
  border-block-start: 1px solid var(--rule);
  text-align: center;
}

.cdt-05__link {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 10px 14px;
  border: 1px solid transparent;
  border-radius: 10px;
  background: transparent;
  color: var(--accent);
  font: 600 13.5px/1.3 var(--font-display);
  cursor: pointer;
}

.cdt-05__link time {
  font-variant-numeric: tabular-nums;
}

.cdt-05__link[disabled] {
  color: var(--muted);
  cursor: not-allowed;
}

.cdt-05__link:not([disabled]) {
  border-color: var(--accent);
}

.cdt-05__link:not([disabled]):hover {
  background: rgba(107, 61, 240, 0.08);
}

.cdt-05__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdt-05__hint {
  margin: 8px 0 0;
  font-size: 11.5px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-05__live {
  display: block;
  min-block-size: 1.1em;
  margin-block-start: 8px;
  font: 600 12px/1.3 var(--font-display);
  color: var(--ok);
  text-align: center;
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-05 {
  position: relative;
}

.cdt-05__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-05__tglbtn {
  position: absolute;
  inset-block-end: 14px;
  inset-inline-end: 14px;
  z-index: 20;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-block-size: 44px;
  min-inline-size: 44px;
  padding: 12px 14px;
  border: 1px solid currentColor;
  border-radius: 10px;
  background: transparent;
  color: inherit;
  font: 600 11px/1 system-ui, sans-serif;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: 0.62;
}

.cdt-05__tglbtn:hover {
  opacity: 1;
}

.cdt-05__tgl:focus-visible + .cdt-05__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-05__tglbtn svg {
  flex: none;
}

.cdt-05__sun,
.cdt-05__lighttext {
  display: none;
}

.cdt-05:has(.cdt-05__tgl:checked) .cdt-05__moon,
.cdt-05:has(.cdt-05__tgl:checked) .cdt-05__darktext {
  display: none;
}

.cdt-05:has(.cdt-05__tgl:checked) .cdt-05__sun {
  display: block;
}

.cdt-05:has(.cdt-05__tgl:checked) .cdt-05__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-05__tglbtn {
    padding: 12px;
  }

  .cdt-05__darktext,
    .cdt-05__lighttext,
    .cdt-05:has(.cdt-05__tgl:checked) .cdt-05__darktext,
    .cdt-05:has(.cdt-05__tgl:checked) .cdt-05__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-05:has(.cdt-05__tgl:checked) {
    --page: #17141c;
    --card: #201c28;
    --ink: #f2eefa;
    --muted: #a49bb5;
    --rule: #302a3b;
    --accent: #b79bff;
    --ok: #6ad39a;
  }

  .cdt-05:has(.cdt-05__tgl:checked) .cdt-05__verify {
    color: #17141c;
  }

  .cdt-05:has(.cdt-05__tgl:checked) .cdt-05__link:not([disabled]):hover {
    background: rgba(183, 155, 255, 0.14);
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-05 {
    --page: #17141c;
    --card: #201c28;
    --ink: #f2eefa;
    --muted: #a49bb5;
    --rule: #302a3b;
    --accent: #b79bff;
    --ok: #6ad39a;
  }

  .cdt-05__verify {
    color: #17141c;
  }

  .cdt-05__link:not([disabled]):hover {
    background: rgba(183, 155, 255, 0.14);
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-05:has(.cdt-05__tgl:checked) {
    --page: oklch(96% 0.018 80);
    --card: oklch(99% 0.008 85);
    --ink: oklch(25% 0.03 300);
    --muted: oklch(52% 0.03 300);
    --rule: oklch(90% 0.016 80);
    --accent: oklch(52% 0.24 292);
    --ok: oklch(52% 0.11 155);
  }

  .cdt-05:has(.cdt-05__tgl:checked) .cdt-05__verify {
    color: #fff;
  }

  .cdt-05:has(.cdt-05__tgl:checked) .cdt-05__link:not([disabled]):hover {
    background: rgba(107, 61, 240, 0.08);
  }
}

[data-theme="dark"] .cdt-05 {
  --page: #17141c;
  --card: #201c28;
  --ink: #f2eefa;
  --muted: #a49bb5;
  --rule: #302a3b;
  --accent: #b79bff;
  --ok: #6ad39a;
}

[data-theme="dark"] .cdt-05 .cdt-05__verify {
  color: #17141c;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-05');
if (root) {
  const btn = root.querySelector('[data-resend]');
  const clock = root.querySelector('[data-clock]'), live = root.querySelector('[data-live]');
  const cells = [...root.querySelectorAll('.cdt-05__cell')];
  let wait = 29e3, target = Date.now() + wait, id = 0;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    clock.textContent = Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
    clock.dateTime = new Date(target).toISOString();
    if (ms > 0) return void (id = setTimeout(tick, 1000 - (Date.now() % 1000)));
    btn.disabled = false; btn.setAttribute('aria-disabled', 'false');
    btn.innerHTML = 'Resend code';
    live.textContent = 'You can request a new code now.';
  };
  const start = () => {
    wait = Math.min(wait * 2, 120e3); target = Date.now() + wait;
    btn.disabled = true; btn.setAttribute('aria-disabled', 'true'); live.textContent = '';
    btn.innerHTML = 'Resend code in <time data-clock></time>';
    clearTimeout(id); tick();
  };
  btn.addEventListener('click', () => { if (!btn.disabled) start(); });
  cells.forEach((c, i) => c.addEventListener('input', () => {
    c.value = c.value.replace(/\D/g, '').slice(-1);
    if (c.value && cells[i + 1]) cells[i + 1].focus();
  }));
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
