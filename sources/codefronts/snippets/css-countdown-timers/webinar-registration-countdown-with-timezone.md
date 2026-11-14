---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/webinar-registration-countdown-with-timezone/"
title: "Webinar Registration Countdown with Timezone"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "A registration card that counts down to the session and states the start time twice: once in the visitor's own timezone, resolved from the browser, and once…"
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Webinar Registration Countdown with Timezone
Source: https://codefronts.com/snippets/css-countdown-timers/webinar-registration-countdown-with-timezone/

A registration card that counts down to the session and states the start time twice: once in the visitor's own timezone, resolved from the browser, and once in the host's. It also explains the parsing bug that silently shifts an event by hours for every visitor who is not in the author's timezone.
## HTML
```html
<section class="cdt-10" aria-labelledby="cdt-10-title">
  <input class="cdt-10__tgl" type="checkbox" id="cdt-10-theme">
  <label class="cdt-10__tglbtn" for="cdt-10-theme">
    <svg class="cdt-10__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-10__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-10__darktext">Dark mode</span><span class="cdt-10__lighttext">Light mode</span>
  </label>
  <div class="cdt-10__stage">
    <article class="cdt-10__card">
      <div class="cdt-10__ribbon">
        <span class="cdt-10__chip">Live session</span>
        <span class="cdt-10__seats">62 of 300 seats left</span>
      </div>

      <h2 class="cdt-10__title" id="cdt-10-title">Shipping schema changes without downtime</h2>
      <p class="cdt-10__host">Alex Chen · Staff engineer at Talon · 45 minutes, live Q&amp;A after</p>

      <div class="cdt-10__timer" role="timer">
        <time class="cdt-10__digits" datetime="" data-clock aria-hidden="true">
          <span><b data-d>01</b><i>days</i></span>
          <span><b data-h>04</b><i>hrs</i></span>
          <span><b data-m>36</b><i>min</i></span>
          <span><b data-s>12</b><i>sec</i></span>
        </time>
        <p class="cdt-10__rel" data-rel>starts in about a day</p>
      </div>

      <dl class="cdt-10__zones">
        <div class="cdt-10__zone"><dt>Your time</dt><dd data-local>—</dd></div>
        <div class="cdt-10__zone"><dt>Host time</dt><dd data-host>—</dd></div>
      </dl>

      <div class="cdt-10__actions">
        <button class="cdt-10__btn" type="button">Save my seat</button>
        <button class="cdt-10__btn cdt-10__btn--ghost" type="button">
          <svg viewBox="0 0 18 18" width="15" height="15" aria-hidden="true"><rect x="2.5" y="4" width="13" height="11.5" rx="2" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M2.5 7.6h13M6.2 2.6v2.6M11.8 2.6v2.6" stroke="currentColor" stroke-width="1.4"/></svg>
          Add to calendar
        </button>
      </div>

      <p class="cdt-10__foot">Stored as one UTC instant and rendered twice. A wall-clock string such as <code>2026-09-01 14:00</code> would be parsed in each visitor's own zone and shift the session by hours.</p>
      <output class="cdt-10__live" aria-live="polite" data-live></output>
    </article>
  </div>
</section>
```
## CSS
```css
.cdt-10 {
  --page: #f4f5f7;
  --card: #ffffff;
  --ink: #17191f;
  --muted: #63676f;
  --rule: #e3e5e9;
  --accent: #2563d8;
  --soft: #eef3fd;
  --font-display: "Geist", "Inter", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-10 {
    --page: oklch(96.5% 0.004 265);
    --card: oklch(100% 0 0);
    --ink: oklch(22% 0.012 265);
    --muted: oklch(52% 0.012 265);
    --rule: oklch(91% 0.006 265);
    --accent: oklch(52% 0.19 262);
    --soft: oklch(96% 0.026 262);
  }
}

.cdt-10 *,
.cdt-10 *::before,
.cdt-10 *::after {
  box-sizing: border-box;
}

.cdt-10__stage {
  display: grid;
  place-content: center;
  justify-items: center;
  min-height: 100vh;
  padding: clamp(16px, 4vw, 48px);
}

.cdt-10__card {
  inline-size: min(620px, 100%);
  padding: clamp(20px, 4.4vw, 34px);
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 14px;
  box-shadow: 0 10px 26px -20px rgba(23, 25, 31, 0.4);
}

.cdt-10__ribbon {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px 12px;
  margin-block-end: 18px;
}

.cdt-10__chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 10px;
  border-radius: 99px;
  background: var(--soft);
  color: var(--accent);
  font: 600 11px/1 var(--font-display);
  letter-spacing: 0.04em;
}

.cdt-10__chip::before {
  content: "";
  inline-size: 6px;
  block-size: 6px;
  border-radius: 50%;
  background: var(--accent);
}

.cdt-10__seats {
  font-size: 12px;
  color: var(--muted);
}

.cdt-10__title {
  margin: 0 0 8px;
  font: 600 clamp(20px, 3.6vw, 27px)/1.22 var(--font-display);
  letter-spacing: -0.022em;
  text-wrap: balance;
}

.cdt-10__host {
  margin: 0 0 22px;
  font-size: 13px;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-10__timer {
  padding: 18px;
  border: 1px solid var(--rule);
  border-radius: 12px;
  background: var(--page);
}

.cdt-10__digits {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 6px;
  font-variant-numeric: tabular-nums;
}

.cdt-10__digits > span {
  display: grid;
  gap: 5px;
  justify-items: center;
  min-inline-size: 0;
}

.cdt-10__digits b {
  font: 600 clamp(24px, 7vw, 38px)/1 var(--font-display);
  letter-spacing: -0.03em;
  font-variant-numeric: tabular-nums;
}

.cdt-10__digits i {
  font: 600 9.5px/1 var(--font-display);
  font-style: normal;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-10__rel {
  margin: 14px 0 0;
  padding-block-start: 12px;
  border-block-start: 1px solid var(--rule);
  font-size: 12.5px;
  color: var(--muted);
  text-align: center;
}

.cdt-10__zones {
  display: grid;
  gap: 1px;
  margin: 18px 0 0;
  background: var(--rule);
  border: 1px solid var(--rule);
  border-radius: 12px;
  overflow: hidden;
}

@media (min-width: 520px) {
  .cdt-10__zones {
    grid-template-columns: 1fr 1fr;
  }
}

.cdt-10__zone {
  min-inline-size: 0;
  padding: 12px 14px;
  background: var(--card);
}

.cdt-10__zone dt {
  font: 600 10px/1 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.cdt-10__zone dd {
  margin: 6px 0 0;
  font-size: 13.5px;
  line-height: 1.4;
  font-variant-numeric: tabular-nums;
  overflow-wrap: anywhere;
}

.cdt-10__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-block-start: 20px;
}

.cdt-10__btn {
  flex: 1 1 160px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  min-block-size: 46px;
  min-inline-size: 44px;
  padding: 12px 18px;
  border: 1px solid transparent;
  border-radius: 10px;
  background: var(--accent);
  color: #fff;
  font: 600 14px/1 var(--font-display);
  cursor: pointer;
}

.cdt-10__btn--ghost {
  background: var(--card);
  color: var(--ink);
  border-color: var(--rule);
}

.cdt-10__btn:hover {
  filter: brightness(1.05);
}

.cdt-10__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.cdt-10__foot {
  margin: 18px 0 0;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cdt-10__foot code {
  padding: 1px 5px;
  border-radius: 4px;
  background: var(--soft);
  font: 500 11px/1.4 ui-monospace, Menlo, monospace;
  color: var(--accent);
  overflow-wrap: anywhere;
}

.cdt-10__live {
  display: block;
  min-block-size: 1.1em;
  margin-block-start: 8px;
  font: 600 12px/1.3 var(--font-display);
  color: var(--accent);
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-10 {
  position: relative;
}

.cdt-10__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-10__tglbtn {
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

.cdt-10__tglbtn:hover {
  opacity: 1;
}

.cdt-10__tgl:focus-visible + .cdt-10__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-10__tglbtn svg {
  flex: none;
}

.cdt-10__sun,
.cdt-10__lighttext {
  display: none;
}

.cdt-10:has(.cdt-10__tgl:checked) .cdt-10__moon,
.cdt-10:has(.cdt-10__tgl:checked) .cdt-10__darktext {
  display: none;
}

.cdt-10:has(.cdt-10__tgl:checked) .cdt-10__sun {
  display: block;
}

.cdt-10:has(.cdt-10__tgl:checked) .cdt-10__lighttext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-10__tglbtn {
    padding: 12px;
  }

  .cdt-10__darktext,
    .cdt-10__lighttext,
    .cdt-10:has(.cdt-10__tgl:checked) .cdt-10__darktext,
    .cdt-10:has(.cdt-10__tgl:checked) .cdt-10__lighttext {
    display: none;
  }
}
/* toggle in the system-light case */

@media (prefers-color-scheme: light) {
  .cdt-10:has(.cdt-10__tgl:checked) {
    --page: #0e1014;
    --card: #171a20;
    --ink: #eef0f4;
    --muted: #969ba5;
    --rule: #262a33;
    --accent: #6f9dff;
    --soft: #1b2436;
  }

  .cdt-10:has(.cdt-10__tgl:checked) .cdt-10__btn {
    color: #0e1014;
  }

  .cdt-10:has(.cdt-10__tgl:checked) .cdt-10__btn--ghost {
    color: #eef0f4;
  }
}

@media (prefers-color-scheme: dark) {
  .cdt-10 {
    --page: #0e1014;
    --card: #171a20;
    --ink: #eef0f4;
    --muted: #969ba5;
    --rule: #262a33;
    --accent: #6f9dff;
    --soft: #1b2436;
  }

  .cdt-10__btn {
    color: #0e1014;
  }

  .cdt-10__btn--ghost {
    color: #eef0f4;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-10:has(.cdt-10__tgl:checked) {
    --page: oklch(96.5% 0.004 265);
    --card: oklch(100% 0 0);
    --ink: oklch(22% 0.012 265);
    --muted: oklch(52% 0.012 265);
    --rule: oklch(91% 0.006 265);
    --accent: oklch(52% 0.19 262);
    --soft: oklch(96% 0.026 262);
  }

  .cdt-10:has(.cdt-10__tgl:checked) .cdt-10__btn {
    color: #fff;
  }

  .cdt-10:has(.cdt-10__tgl:checked) .cdt-10__btn--ghost {
    color: var(--ink);
  }
}

[data-theme="dark"] .cdt-10 {
  --page: #0e1014;
  --card: #171a20;
  --ink: #eef0f4;
  --muted: #969ba5;
  --rule: #262a33;
  --accent: #6f9dff;
  --soft: #1b2436;
}

[data-theme="dark"] .cdt-10 .cdt-10__btn {
  color: #0e1014;
}

[data-theme="dark"] .cdt-10 .cdt-10__btn--ghost {
  color: #eef0f4;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-10');
if (root) {
  const q = (s) => root.querySelector(s);
  const HOST = 'Europe/Berlin', clock = q('[data-clock]'), live = q('[data-live]');
  const target = new Date(Date.now() + 28 * 3600e3 + 36 * 60e3 + 12e3);
  const zone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  const fmt = (tz) => new Intl.DateTimeFormat([], { dateStyle: 'medium', timeStyle: 'short', timeZone: tz }).format(target);
  const rel = new Intl.RelativeTimeFormat([], { numeric: 'auto' });
  const pad = (n) => String(n).padStart(2, '0');
  clock.dateTime = target.toISOString();
  q('[data-local]').textContent = fmt(zone) + ' · ' + zone;
  q('[data-host]').textContent = fmt(HOST) + ' · ' + HOST;
  let seen = null, id = 0;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.floor(ms / 1000);
    q('[data-d]').textContent = pad(Math.floor(s / 86400));
    q('[data-h]').textContent = pad(Math.floor(s / 3600) % 24);
    q('[data-m]').textContent = pad(Math.floor(s / 60) % 60);
    q('[data-s]').textContent = pad(s % 60);
    q('[data-rel]').textContent = ms <= 0 ? 'The room is open — join now' : s >= 86400 ? 'starts ' + rel.format(Math.round(s / 86400), 'day') : s >= 3600 ? 'starts ' + rel.format(Math.round(s / 3600), 'hour') : 'starts ' + rel.format(Math.ceil(s / 60), 'minute');
    const b = ms <= 0 ? 'end' : ms < 600e3 ? 'm10' : ms < 3600e3 ? 'h1' : ms < 86400e3 ? 'd1' : 'far';
    if (b !== seen) { seen = b; live.textContent = { far: '', d1: 'Session starts within a day.', h1: 'Session starts within the hour.', m10: 'Session starts in ten minutes.', end: 'The session room is open.' }[b]; }
    if (ms > 0) id = setTimeout(tick, 1000 - (Date.now() % 1000));
  };
  tick();
  root.cleanup = () => clearTimeout(id);
}
```
