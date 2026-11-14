---
source: "codefronts"
url: "https://codefronts.com/snippets/css-countdown-timers/rate-limit-cooldown-button-with-retry-timer/"
title: "Rate Limit Cooldown Button with Retry Timer"
section: "snippets"
category: "css-countdown-timers"
category_name: "CSS Countdown Timers"
description: "What a 429 should look like in a UI: the action returns Too Many Requests, the button enters a cooldown derived from the Retry-After header, and a tinted…"
has_js: "true"
---

Here's a working CSS Countdown Timer from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rate Limit Cooldown Button with Retry Timer
Source: https://codefronts.com/snippets/css-countdown-timers/rate-limit-cooldown-button-with-retry-timer/

What a 429 should look like in a UI: the action returns Too Many Requests, the button enters a cooldown derived from the Retry-After header, and a tinted fill drains across the label as the seconds tick away. The response headers sit beside it so the number on the button is traceable to the value the server sent.
## HTML
```html
<section class="cdt-06" aria-labelledby="cdt-06-title">
  <input class="cdt-06__tgl" type="checkbox" id="cdt-06-theme">
  <label class="cdt-06__tglbtn" for="cdt-06-theme">
    <svg class="cdt-06__moon" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><path d="M15.7 12.8A6.5 6.5 0 0 1 7.2 4.3a6.6 6.6 0 1 0 8.5 8.5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>
    <svg class="cdt-06__sun" viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><circle cx="10" cy="10" r="3.7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 1.8v2.1M10 16.1v2.1M1.8 10h2.1M16.1 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    <span class="cdt-06__darktext">Dark mode</span><span class="cdt-06__lighttext">Light mode</span>
  </label>
  <div class="cdt-06__stage">
    <div class="cdt-06__panel">
      <header class="cdt-06__head">
        <span class="cdt-06__dot" aria-hidden="true"></span>
        <h2 class="cdt-06__title" id="cdt-06-title">POST /v2/exports</h2>
        <span class="cdt-06__env">talon-api · staging</span>
      </header>

      <div class="cdt-06__row">
        <button class="cdt-06__go" type="button" data-go>
          <span data-label>Run request</span>
        </button>
        <p class="cdt-06__state" role="timer" data-state>Ready · 5 requests per minute</p>
      </div>

      <dl class="cdt-06__headers">
        <div><dt>status</dt><dd data-status>—</dd></div>
        <div><dt>retry-after</dt><dd><time datetime="" data-retry>—</time></dd></div>
        <div><dt>x-ratelimit-remaining</dt><dd data-left>5</dd></div>
        <div><dt>x-ratelimit-reset</dt><dd data-reset>—</dd></div>
      </dl>

      <pre class="cdt-06__log" data-log aria-label="Request log">$ waiting for first run</pre>
      <output class="cdt-06__sr" aria-live="polite" data-live></output>
      <p class="cdt-06__foot">Retry-After may arrive as delta-seconds or an HTTP-date. Both are parsed; a missing header falls back to a fixed 15s wait.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cdt-06 {
  --page: #000000;
  --panel: #0a0a0b;
  --ink: #f4f4f5;
  --muted: #7d7d86;
  --rule: #1e1e22;
  --accent: #ffb224;
  --danger: #ff5c5c;
  --ok: #4ade80;
  --mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--mono);
}

@supports (color: oklch(50% 0.1 20)) {
  .cdt-06 {
    --page: oklch(0% 0 0);
    --panel: oklch(15% 0.004 280);
    --ink: oklch(96% 0.003 280);
    --muted: oklch(61% 0.01 280);
    --rule: oklch(25% 0.006 280);
    --accent: oklch(81% 0.16 78);
    --danger: oklch(69% 0.19 25);
    --ok: oklch(82% 0.17 148);
  }
}

.cdt-06 *,
.cdt-06 *::before,
.cdt-06 *::after {
  box-sizing: border-box;
}

.cdt-06__stage {
  display: grid;
  place-content: center;
  justify-items: center;
  min-height: 100vh;
  padding: clamp(12px, 4vw, 40px);
}

.cdt-06__panel {
  inline-size: min(620px, 100%);
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 6px;
}

.cdt-06__head {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  border-block-end: 1px solid var(--rule);
  min-inline-size: 0;
}

.cdt-06__dot {
  flex: none;
  inline-size: 7px;
  block-size: 7px;
  border-radius: 50%;
  background: var(--ok);
}

.cdt-06__title {
  flex: 1 1 auto;
  min-inline-size: 0;
  margin: 0;
  font: 500 12.5px/1.3 var(--mono);
  letter-spacing: -0.01em;
  overflow-wrap: anywhere;
}

.cdt-06__env {
  flex: none;
  font-size: 10.5px;
  color: var(--muted);
}

.cdt-06__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px;
  padding: 12px;
  border-block-end: 1px solid var(--rule);
}

.cdt-06__go {
  min-block-size: 44px;
  min-inline-size: 150px;
  padding: 11px 16px;
  border: 1px solid var(--rule);
  border-radius: 4px;
  background-color: transparent;
  background-image: linear-gradient(to right, rgba(255, 178, 36, 0.22), rgba(255, 178, 36, 0.22));
  background-repeat: no-repeat;
  background-size: 0% 100%;
  color: var(--ink);
  font: 500 12.5px/1 var(--mono);
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background-size 1s linear, border-color 0.2s;
}

.cdt-06__go:not([disabled]):hover {
  border-color: var(--accent);
}

.cdt-06__go:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cdt-06__go[disabled] {
  color: var(--accent);
  cursor: not-allowed;
  border-color: color-mix(in oklab, var(--accent) 45%, var(--rule));
}

.cdt-06__go[data-cool] {
  background-size: var(--fill, 100%) 100%;
}

.cdt-06__state {
  flex: 1 1 160px;
  min-inline-size: 0;
  margin: 0;
  font-size: 11.5px;
  color: var(--muted);
}

.cdt-06__state[data-limited] {
  color: var(--danger);
}

.cdt-06__headers {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1px;
  margin: 0;
  background: var(--rule);
}

.cdt-06__headers > div {
  min-inline-size: 0;
  padding: 9px 12px;
  background: var(--panel);
}

.cdt-06__headers dt {
  font-size: 10px;
  letter-spacing: 0.04em;
  color: var(--muted);
  overflow-wrap: anywhere;
}

.cdt-06__headers dd {
  margin: 3px 0 0;
  font-size: 12.5px;
  font-variant-numeric: tabular-nums;
}

.cdt-06__headers dd[data-status="429"] {
  color: var(--danger);
}

.cdt-06__log {
  margin: 0;
  padding: 12px;
  min-block-size: 76px;
  border-block-start: 1px solid var(--rule);
  font: 400 11.5px/1.7 var(--mono);
  color: var(--muted);
  white-space: pre-wrap;
  overflow-wrap: anywhere;
}

.cdt-06__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-06__foot {
  margin: 0;
  padding: 10px 12px;
  border-block-start: 1px solid var(--rule);
  font-size: 10.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .cdt-06__go {
    transition: none;
  }
}
/* --- pure-CSS theme toggle ------------------------------------------- */

.cdt-06 {
  position: relative;
}

.cdt-06__tgl {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cdt-06__tglbtn {
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

.cdt-06__tglbtn:hover {
  opacity: 1;
}

.cdt-06__tgl:focus-visible + .cdt-06__tglbtn {
  outline: 2px solid currentColor;
  outline-offset: 2px;
  opacity: 1;
}

.cdt-06__tglbtn svg {
  flex: none;
}

.cdt-06__moon,
.cdt-06__darktext {
  display: none;
}

.cdt-06:has(.cdt-06__tgl:checked) .cdt-06__sun,
.cdt-06:has(.cdt-06__tgl:checked) .cdt-06__lighttext {
  display: none;
}

.cdt-06:has(.cdt-06__tgl:checked) .cdt-06__moon {
  display: block;
}

.cdt-06:has(.cdt-06__tgl:checked) .cdt-06__darktext {
  display: inline;
}

@media (max-width: 460px) {
  .cdt-06__tglbtn {
    padding: 12px;
  }

  .cdt-06__darktext,
    .cdt-06__lighttext,
    .cdt-06:has(.cdt-06__tgl:checked) .cdt-06__darktext,
    .cdt-06:has(.cdt-06__tgl:checked) .cdt-06__lighttext {
    display: none;
  }
}
/* toggle in the system-dark case */

@media (prefers-color-scheme: dark) {
  .cdt-06:has(.cdt-06__tgl:checked) {
    --page: #f4f4f5;
    --panel: #ffffff;
    --ink: #101012;
    --muted: #6c6c75;
    --rule: #e2e2e6;
    --accent: #a15c00;
    --danger: #c02626;
    --ok: #157f3c;
  }
}

@media (prefers-color-scheme: light) {
  .cdt-06 {
    --page: #f4f4f5;
    --panel: #ffffff;
    --ink: #101012;
    --muted: #6c6c75;
    --rule: #e2e2e6;
    --accent: #a15c00;
    --danger: #c02626;
    --ok: #157f3c;
  }
  /* mirror flip-back: checked means the opposite of the system preference */

  .cdt-06:has(.cdt-06__tgl:checked) {
    --page: oklch(0% 0 0);
    --panel: oklch(15% 0.004 280);
    --ink: oklch(96% 0.003 280);
    --muted: oklch(61% 0.01 280);
    --rule: oklch(25% 0.006 280);
    --accent: oklch(81% 0.16 78);
    --danger: oklch(69% 0.19 25);
    --ok: oklch(82% 0.17 148);
  }
}

[data-theme="dark"] .cdt-06 {
  --page: #000000;
  --panel: #0a0a0b;
  --ink: #f4f4f5;
  --muted: #7d7d86;
  --rule: #1e1e22;
  --accent: #ffb224;
  --danger: #ff5c5c;
  --ok: #4ade80;
}
```

## JavaScript
```js
const root = document.querySelector('.cdt-06');
if (root) {
  const q = (s) => root.querySelector(s);
  const go = q('[data-go]'), label = q('[data-label]'), state = q('[data-state]'), log = q('[data-log]');
  const live = q('[data-live]'), FALLBACK = 15;
  let left = 5, id = 0, total = 0, target = 0;
  const parseRetry = (v) => Number.isFinite(+v) ? +v : Number.isFinite(Date.parse(v)) ? Math.ceil((Date.parse(v) - Date.now()) / 1000) : FALLBACK;
  const tick = () => {
    const ms = Math.max(0, target - Date.now()), s = Math.ceil(ms / 1000);
    label.textContent = 'Retry in ' + s + 's';
    go.style.setProperty('--fill', (ms / total * 100).toFixed(1) + '%');
    if (ms > 0) return void (id = setTimeout(tick, 1000 - (Date.now() % 1000)));
    go.disabled = false; go.removeAttribute('aria-disabled'); go.removeAttribute('data-cool');
    label.textContent = 'Run request'; left = 5; q('[data-left]').textContent = left;
    state.removeAttribute('data-limited'); state.textContent = 'Ready · window reset';
    live.textContent = 'Rate limit window reset. You can run the request again.';
  };
  go.addEventListener('click', () => {
    if (go.disabled) return;
    if (left > 0) { left -= 1; q('[data-left]').textContent = left; q('[data-status]').textContent = '202'; q('[data-status]').dataset.status = '202'; log.textContent = '$ 202 accepted · export queued · ' + left + ' left in window'; return; }
    const header = '9';
    const secs = parseRetry(header); total = secs * 1000; target = Date.now() + total;
    q('[data-status]').textContent = '429'; q('[data-status]').dataset.status = '429';
    q('[data-retry]').textContent = header; q('[data-retry]').dateTime = 'PT' + secs + 'S'; q('[data-reset]').textContent = new Date(target).toLocaleTimeString([], { hour12: false });
    state.setAttribute('data-limited', ''); state.textContent = 'Too Many Requests · cooling down';
    log.textContent = '$ 429 too many requests\n  retry-after: ' + header + '  → cooldown ' + secs + 's';
    go.disabled = true; go.setAttribute('aria-disabled', 'true'); go.setAttribute('data-cool', '');
    live.textContent = 'Rate limited. Retry available in ' + secs + ' seconds.';
    clearTimeout(id); tick();
  });
  root.cleanup = () => clearTimeout(id);
}
```
