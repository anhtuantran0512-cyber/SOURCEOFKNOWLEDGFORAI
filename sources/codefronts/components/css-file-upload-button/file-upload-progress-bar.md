---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/file-upload-progress-bar/"
title: "File Upload Progress Bar"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "A determinate progress bar that reports like a real transfer: percentage, bytes moved, throughput and a live ETA, all driven from one registered @property so…"
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: File Upload Progress Bar
Source: https://codefronts.com/components/css-file-upload-button/file-upload-progress-bar/

A determinate progress bar that reports like a real transfer: percentage, bytes moved, throughput and a live ETA, all driven from one registered @property so the fill, the sheen and the numeric readout stay in lockstep. It is a proper role="progressbar" with aria-valuenow, and it announces at milestones rather than on every frame — the difference between helpful and unbearable with a screen reader.
## HTML
```html
<div class="fu-14">
  <button class="fu-14__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-14__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-14__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-14__card" aria-labelledby="fu-14-h">
    <header class="fu-14__head">
      <span class="fu-14__ico" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M14.4 3.5H7.8A2.3 2.3 0 0 0 5.5 5.8v12.4A2.3 2.3 0 0 0 7.8 20.5h8.4a2.3 2.3 0 0 0 2.3-2.3V7.4z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M14.3 3.6v3.6h4.1" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
      </span>
      <div class="fu-14__col">
        <h2 class="fu-14__h" id="fu-14-h">quarterly-review-2026.mp4</h2>
        <p class="fu-14__meta" id="fu-14-meta">248.6 MB <span aria-hidden="true">·</span> waiting to start</p>
      </div>
      <span class="fu-14__pct" id="fu-14-pct">0%</span>
    </header>

    <div class="fu-14__bar" id="fu-14-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-labelledby="fu-14-h">
      <span class="fu-14__fill" id="fu-14-fill"></span>
    </div>

    <div class="fu-14__foot">
      <span class="fu-14__rate" id="fu-14-rate">—</span>
      <div class="fu-14__btns">
        <button class="fu-14__ghost" id="fu-14-cancel" type="button" disabled>Cancel</button>
        <button class="fu-14__go" id="fu-14-go" type="button">Start upload</button>
      </div>
    </div>

    <div class="fu-14__pickRow">
      <input class="fu-14__input" id="fu-14-file" type="file">
      <label class="fu-14__pick" for="fu-14-file">Choose a different file</label>
    </div>
    <p class="fu-14__status" id="fu-14-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500&display=swap');

@property --fu-14-p {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

.fu-14 {
  --bg: #070810;
  --surface: #0f1119;
  --raise: #161a24;
  --ink: #eef0f6;
  --muted: #848ca0;
  --line: #222736;
  --acc: #7bf1a8;
  --acc2: #4c8dff;
  --track: #1b202c;
  --fu-14-p: 0%;
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(70% 45% at 50% 0%, color-mix(in oklab,var(--acc2) 16%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-14,
.fu-14 *,
.fu-14 *::before,
.fu-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-14 {
    --acc: oklch(87% .16 155);
    --acc2: oklch(66% .18 262);
  }
}

.fu-14__card {
  inline-size: min(30rem,100%);
  display: grid;
  gap: .9rem;
  padding: clamp(1.1rem,3.5vw,1.5rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  box-shadow: 0 40px 90px -60px #000;
}

.fu-14__head {
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  align-items: center;
  gap: .85rem;
}

.fu-14__ico {
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: .75rem;
  background: color-mix(in oklab,var(--acc2) 16%,transparent);
  color: var(--acc2);
}

.fu-14__ico svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-14__col {
  min-inline-size: 0;
  display: grid;
  gap: .15rem;
}

.fu-14__h {
  margin: 0;
  font-size: .9375rem;
  font-weight: 700;
  letter-spacing: -.015em;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-14__meta {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-14__pct {
  font-family: var(--mono);
  font-size: 1.125rem;
  font-weight: 500;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  color: var(--acc);
}

.fu-14__bar {
  position: relative;
  block-size: .65rem;
  border-radius: 999px;
  overflow: hidden;
  background: var(--track);
  border: 1px solid color-mix(in oklab,var(--ink) 6%,transparent);
}

.fu-14__fill {
  display: block;
  block-size: 100%;
  inline-size: var(--fu-14-p);
  border-radius: 999px;
  background: linear-gradient(90deg, var(--acc2), var(--acc));
  transition: inline-size .22s linear;
  box-shadow: 0 0 18px -2px color-mix(in oklab,var(--acc) 55%,transparent);
}

.fu-14__fill::after {
  content: "";
  position: absolute;
  inset: 0;
  inline-size: var(--fu-14-p);
  border-radius: 999px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.35), transparent);
  background-size: 40% 100%;
  background-repeat: no-repeat;
  animation: fu-14-sheen 1.4s linear infinite;
}

.fu-14__card[data-running="false"] .fu-14__fill::after {
  animation: none;
  opacity: 0;
}

@keyframes fu-14-sheen {
  from {
    background-position: -40% 0;
  }

  to {
    background-position: 140% 0;
  }
}

.fu-14__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.fu-14__rate {
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-14__btns {
  display: flex;
  gap: .5rem;
  margin-inline-start: auto;
}

.fu-14__ghost,
.fu-14__go {
  min-block-size: 2.75rem;
  padding: .6rem 1.1rem;
  cursor: pointer;
  border-radius: .75rem;
  font-family: var(--sans);
  font-size: .875rem;
  font-weight: 700;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1), opacity .2s ease, background .2s ease;
}

.fu-14__ghost {
  border: 1px solid var(--line);
  background: transparent;
  color: var(--muted);
}

.fu-14__ghost:hover:not(:disabled) {
  color: var(--ink);
  border-color: var(--muted);
}

.fu-14__go {
  border: 0;
  background: var(--acc);
  color: #04160c;
}

.fu-14__go:hover:not(:disabled) {
  filter: brightness(1.07);
  transform: translateY(-1px);
}

.fu-14__ghost:disabled,
.fu-14__go:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.fu-14__ghost:focus-visible,
.fu-14__go:focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
}

.fu-14__pickRow {
  display: flex;
}

.fu-14__input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: 0;
  border: 0;
  overflow: hidden;
  opacity: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  white-space: nowrap;
}

.fu-14__pick {
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  min-block-size: 2.5rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--acc2);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.fu-14__pick:hover {
  color: var(--ink);
}

.fu-14__input:focus-visible + .fu-14__pick {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
  border-radius: .3rem;
}

.fu-14__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

@media (prefers-color-scheme: light) {
  .fu-14:not([data-theme="dark"]) {
    --bg: #eef1f6;
    --surface: #ffffff;
    --raise: #f6f8fb;
    --ink: #0b0e15;
    --muted: #5a6376;
    --line: #e2e6ee;
    --acc: #0e9f6e;
    --acc2: #2563eb;
    --track: #e8ecf4;
  }

  .fu-14:not([data-theme="dark"]) .fu-14__go {
    color: #fff;
  }
}

.fu-14[data-theme="light"] {
  --bg: #eef1f6;
  --surface: #ffffff;
  --raise: #f6f8fb;
  --ink: #0b0e15;
  --muted: #5a6376;
  --line: #e2e6ee;
  --acc: #0e9f6e;
  --acc2: #2563eb;
  --track: #e8ecf4;
}

.fu-14[data-theme="light"] .fu-14__go {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .fu-14 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-14__card,
    .fu-14__bar {
    border: 1px solid CanvasText;
  }

  .fu-14__fill {
    background: Highlight;
  }

  .fu-14__go,
    .fu-14__ghost {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-14 {
  position: relative;
}

.fu-14__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.4rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.4rem);
  z-index: 20;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,currentColor 30%,transparent);
  background: color-mix(in oklab,currentColor 12%,transparent);
  color: inherit;
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.fu-14__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-14__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-14__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-14__sun {
  display: none;
}

.fu-14__theme[aria-pressed="true"] .fu-14__sun {
  display: block;
}

.fu-14__theme[aria-pressed="true"] .fu-14__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-14__theme {
    transition: none;
  }

  .fu-14__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-14__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-14');
  if (!root) return;
  const card = root.querySelector('.fu-14__card');
  const bar = root.querySelector('#fu-14-bar');
  const pctEl = root.querySelector('#fu-14-pct');
  const rate = root.querySelector('#fu-14-rate');
  const meta = root.querySelector('#fu-14-meta');
  const title = root.querySelector('#fu-14-h');
  const go = root.querySelector('#fu-14-go');
  const cancel = root.querySelector('#fu-14-cancel');
  const input = root.querySelector('#fu-14-file');
  const status = root.querySelector('#fu-14-status');
  let total = 248.6 * 1024 * 1024, sent = 0, timer = null, milestone = 0;

  const mb = (b) => (b / 1048576).toFixed(1) + ' MB';
  const set = (p) => {
    root.style.setProperty('--fu-14-p', p + '%');
    pctEl.textContent = Math.round(p) + '%';
    bar.setAttribute('aria-valuenow', Math.round(p));
    bar.setAttribute('aria-valuetext', Math.round(p) + ' percent uploaded');
  };

  const stop = (msg) => {
    clearInterval(timer); timer = null;
    card.dataset.running = 'false';
    go.disabled = false; cancel.disabled = true;
    status.textContent = msg;
  };

  go.addEventListener('click', () => {
    sent = 0; milestone = 0; set(0);
    card.dataset.running = 'true';
    go.disabled = true; cancel.disabled = false;
    status.textContent = 'Upload started';
    timer = setInterval(() => {
      const chunk = total * (0.02 + Math.random() * 0.025);
      sent = Math.min(total, sent + chunk);
      const p = (sent / total) * 100;
      set(p);
      const speed = chunk * 5;
      meta.textContent = mb(sent) + ' of ' + mb(total);
      rate.textContent = mb(speed) + '/s · ' + Math.ceil((total - sent) / speed) + 's remaining';
      if (p >= milestone + 25) { milestone += 25; status.textContent = Math.round(p) + '% uploaded'; }
      if (sent >= total) { rate.textContent = 'Transfer complete'; stop('Upload finished — file is now processing'); }
    }, 200);
  });

  cancel.addEventListener('click', () => {
    set(0); sent = 0;
    meta.textContent = mb(total) + ' · cancelled';
    rate.textContent = '—';
    stop('Upload cancelled');
  });

  input.addEventListener('change', () => {
    const f = input.files && input.files[0];
    if (!f) return;
    total = f.size || total; sent = 0; set(0);
    title.textContent = f.name;
    meta.textContent = mb(total) + ' · waiting to start';
    rate.textContent = '—';
    status.textContent = f.name + ' queued';
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-14');
  const btn = root && root.querySelector('.fu-14__theme');
  if (!btn) return;
  const isDark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(isDark()));
    btn.setAttribute('aria-label', isDark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  sync();
})();
```
