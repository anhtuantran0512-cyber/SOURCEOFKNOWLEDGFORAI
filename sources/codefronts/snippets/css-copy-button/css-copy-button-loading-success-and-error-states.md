---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-copy-button-loading-success-and-error-states/"
title: "CSS Copy Button Loading, Success, and Error States"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "Almost every copy button ships two states."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Copy Button Loading, Success, and Error States
Source: https://codefronts.com/snippets/css-copy-button/css-copy-button-loading-success-and-error-states/

Almost every copy button ships two states. This one ships three, including the error case nobody builds: the value has to be fetched before it can be copied, so there is a real loading state, and the write can fail with permission denied, insecure context or nothing to copy. Switch the scenario and watch each path resolve honestly.
## HTML
```html
<div class="cpy-17">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-17__sr" type="checkbox" id="cpy-17-dark">
  <label class="cpy-17__theme" for="cpy-17-dark" title="Switch light or dark theme">
    <svg class="cpy-17__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-17__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-17__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-17__stage">
    <div class="cpy-17__card">
      <p class="cpy-17__eyebrow">State machine &middot; loading / success / error</p>
      <h2 class="cpy-17__title">Mint a one-time invite token</h2>
      <p class="cpy-17__lead">The value does not exist until you ask for it, so this button loads before it copies &mdash; and tells you exactly what went wrong when it cannot.</p>

      <button class="cpy-17__btn" type="button" data-state="idle" aria-disabled="false">
        <span class="cpy-17__slot">
          <span class="cpy-17__spinner" aria-hidden="true"></span>
          <svg class="cpy-17__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <svg class="cpy-17__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <svg class="cpy-17__i3" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 7.4v6M12 16.4v.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/></svg>
        </span>
        <span class="cpy-17__labels">
          <span class="cpy-17__lb cpy-17__lb--idle">Generate &amp; copy token</span>
          <span class="cpy-17__lb cpy-17__lb--load">Generating&hellip;</span>
          <span class="cpy-17__lb cpy-17__lb--ok">Token copied</span>
          <span class="cpy-17__lb cpy-17__lb--err">Copy failed</span>
        </span>
      </button>

      <p class="cpy-17__msg" id="cpy-17-msg" role="status" aria-live="polite">Idle &mdash; nothing minted yet.</p>
      <p class="cpy-17__alert" id="cpy-17-alert" role="alert"></p>

      <fieldset class="cpy-17__modes">
        <legend>Scenario</legend>
        <input class="cpy-17__sr" type="radio" name="cpy-17-mode" id="cpy-17-m1" value="ok" checked>
        <label for="cpy-17-m1">Normal</label>
        <input class="cpy-17__sr" type="radio" name="cpy-17-mode" id="cpy-17-m2" value="denied">
        <label for="cpy-17-m2">Permission denied</label>
        <input class="cpy-17__sr" type="radio" name="cpy-17-mode" id="cpy-17-m3" value="empty">
        <label for="cpy-17-m3">Empty value</label>
      </fieldset>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-17 {
  --bg: #f6f7f9;
  --panel: #ffffff;
  --panel2: #f0f2f6;
  --ink: #0b0e16;
  --muted: #5a6170;
  --line: rgba(11,14,22,.12);
  --accent: #4f46e5;
  --ok: #15803d;
  --ok-bg: rgba(21,128,61,.1);
  --err: #dc2626;
  --err-bg: rgba(220,38,38,.1);
  --dur: 190ms;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cpy-17 *,
.cpy-17 *::before,
.cpy-17 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-17 {
    --accent: oklch(.53 .21 274);
    --ok: oklch(.55 .15 149);
    --ok-bg: oklch(.55 .15 149/.12);
    --err: oklch(.58 .21 25);
    --err-bg: oklch(.58 .21 25/.12);
  }
}

.cpy-17__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-17__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-17__theme {
  position: absolute;
  inset-block-start: clamp(1rem,3vw,1.75rem);
  inset-inline-end: clamp(1rem,3vw,1.75rem);
  z-index: 3;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.6);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  color: var(--ink);
  cursor: pointer;
}

.cpy-17__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-17__moon {
  display: none;
}

.cpy-17__sr:focus-visible + .cpy-17__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-17__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-17__card {
  inline-size: min(100%,34rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .8rem;
  justify-items: start;
  box-shadow: 0 1px 2px rgba(11,14,22,.05),0 28px 55px -36px rgba(11,14,22,.34);
}

.cpy-17__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-17__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-17__lead {
  margin: 0 0 .4rem;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-17__btn {
  min-block-size: 3rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  padding-inline: 1.2rem;
  border: 1px solid transparent;
  border-radius: .85rem;
  background: var(--ink);
  color: var(--panel);
  font: inherit;
  font-size: .93rem;
  font-weight: 560;
  cursor: pointer;
  transition: background var(--dur),color var(--dur),scale var(--dur);
}

.cpy-17__btn:active {
  scale: .98;
}

.cpy-17__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-17__btn[data-state="loading"] {
  cursor: progress;
  background: color-mix(in srgb,var(--ink) 78%,var(--panel));
}

.cpy-17__btn[data-state="copied"] {
  background: var(--ok);
  color: #fff;
}

.cpy-17__btn[data-state="error"] {
  background: var(--err);
  color: #fff;
}

.cpy-17__slot {
  position: relative;
  inline-size: 1.2rem;
  block-size: 1.2rem;
  flex: none;
}

.cpy-17__slot svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  opacity: 0;
  scale: .6;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-17__btn[data-state="idle"] .cpy-17__i1,
.cpy-17__btn[data-state="copied"] .cpy-17__i2,
.cpy-17__btn[data-state="error"] .cpy-17__i3 {
  opacity: 1;
  scale: 1;
}

.cpy-17__spinner {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  opacity: 0;
  background: conic-gradient(from 0deg,transparent 0 25%,currentColor 100%);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(100% - 2.5px),#000 calc(100% - 2px));
  mask: radial-gradient(farthest-side,transparent calc(100% - 2.5px),#000 calc(100% - 2px));
  transition: opacity var(--dur);
}

.cpy-17__btn[data-state="loading"] .cpy-17__spinner {
  opacity: 1;
  animation: cpy-17-spin 700ms linear infinite;
}

@keyframes cpy-17-spin {
  to {
    rotate: 360deg;
  }
}

.cpy-17__labels {
  display: grid;
}

.cpy-17__lb {
  grid-area: 1/1;
  opacity: 0;
  transition: opacity var(--dur);
}

.cpy-17__btn[data-state="idle"] .cpy-17__lb--idle,
.cpy-17__btn[data-state="loading"] .cpy-17__lb--load,
.cpy-17__btn[data-state="copied"] .cpy-17__lb--ok,
.cpy-17__btn[data-state="error"] .cpy-17__lb--err {
  opacity: 1;
}

.cpy-17__msg {
  margin: 0;
  min-block-size: 1.3rem;
  font-family: var(--mono);
  font-size: .8rem;
  color: var(--muted);
}

.cpy-17__msg[data-kind="ok"] {
  color: var(--ok);
}

.cpy-17__alert {
  margin: 0;
  min-block-size: 1.3rem;
  font-size: .85rem;
  font-weight: 540;
  color: var(--err);
}

.cpy-17__modes {
  display: flex;
  flex-wrap: wrap;
  gap: .45rem;
  margin: .4rem 0 0;
  padding: 0;
  border: 0;
}

.cpy-17__modes legend {
  padding: 0 0 .45rem;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-17__modes label {
  min-block-size: 44px;
  display: inline-flex;
  align-items: center;
  padding-inline: .85rem;
  border: 1px solid var(--line);
  border-radius: .7rem;
  font-size: .82rem;
  cursor: pointer;
  transition: border-color var(--dur),background var(--dur),color var(--dur);
}

.cpy-17__modes label:hover {
  background: var(--panel2);
}

.cpy-17__modes input:checked + label {
  border-color: var(--accent);
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 8%,transparent);
}

.cpy-17__modes input:focus-visible + label {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media not (prefers-color-scheme: dark) {
  .cpy-17:has(#cpy-17-dark:checked) {
    --bg: #07080f;
    --panel: #0d1017;
    --panel2: #161a24;
    --ink: #e9ebf3;
    --muted: rgba(233,235,243,.6);
    --line: rgba(233,235,243,.14);
    --accent: #a5b4fc;
    --ok: #6ee7a8;
    --ok-bg: rgba(110,231,168,.13);
    --err: #fda4af;
    --err-bg: rgba(253,164,175,.13);
  }

  .cpy-17:has(#cpy-17-dark:checked) .cpy-17__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-17:has(#cpy-17-dark:checked) .cpy-17__sun {
    display: none;
  }

  .cpy-17:has(#cpy-17-dark:checked) .cpy-17__moon {
    display: block;
  }

  .cpy-17:has(#cpy-17-dark:checked) .cpy-17__btn[data-state="copied"],
    .cpy-17:has(#cpy-17-dark:checked) .cpy-17__btn[data-state="error"] {
    color: #0a0f14;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-17:not([data-theme="light"]):not(:has(#cpy-17-dark:checked)) {
    --bg: #07080f;
    --panel: #0d1017;
    --panel2: #161a24;
    --ink: #e9ebf3;
    --muted: rgba(233,235,243,.6);
    --line: rgba(233,235,243,.14);
    --accent: #a5b4fc;
    --ok: #6ee7a8;
    --ok-bg: rgba(110,231,168,.13);
    --err: #fda4af;
    --err-bg: rgba(253,164,175,.13);
  }

  .cpy-17__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-17__sun {
    display: none;
  }

  .cpy-17__moon {
    display: block;
  }

  .cpy-17:has(#cpy-17-dark:checked) .cpy-17__sun {
    display: block;
  }

  .cpy-17:has(#cpy-17-dark:checked) .cpy-17__moon {
    display: none;
  }

  .cpy-17__btn[data-state="copied"],
    .cpy-17__btn[data-state="error"] {
    color: #0a0f14;
  }
}

.cpy-17[data-theme="dark"] {
  --bg: #07080f;
  --panel: #0d1017;
  --panel2: #161a24;
  --ink: #e9ebf3;
  --muted: rgba(233,235,243,.6);
  --line: rgba(233,235,243,.14);
  --accent: #a5b4fc;
  --ok: #6ee7a8;
  --ok-bg: rgba(110,231,168,.13);
  --err: #fda4af;
  --err-bg: rgba(253,164,175,.13);
}

@media (prefers-reduced-motion: reduce) {
  .cpy-17 *,
    .cpy-17 *::before,
    .cpy-17 *::after {
    transition: none !important;
  }

  .cpy-17__btn[data-state="loading"] .cpy-17__spinner {
    animation-duration: 1600ms;
  }
}

@media (forced-colors: active) {
  .cpy-17__card,
    .cpy-17__btn,
    .cpy-17__theme,
    .cpy-17__modes label {
    border: 1px solid CanvasText;
    background: Canvas;
    color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```

## JavaScript
```js
const cpy17 = document.querySelector('.cpy-17');
if (cpy17) {
  const btn = cpy17.querySelector('.cpy-17__btn');
  const msg = cpy17.querySelector('#cpy-17-msg');
  const alert = cpy17.querySelector('#cpy-17-alert');
  const wait = (ms) => new Promise((r) => setTimeout(r, ms));
  const mode = () => cpy17.querySelector('input[name="cpy-17-mode"]:checked').value;
  let timer;
  const set = (state, note, problem) => {
    btn.dataset.state = state;
    btn.setAttribute('aria-busy', String(state === 'loading'));
    btn.setAttribute('aria-disabled', String(state === 'loading'));
    msg.textContent = note; msg.dataset.kind = state === 'copied' ? 'ok' : '';
    alert.textContent = problem || '';
  };
  btn.addEventListener('click', async () => {
    if (btn.getAttribute('aria-disabled') === 'true') return;      // guard, not disabled
    clearTimeout(timer);
    set('loading', 'Minting a one-time token...');
    await wait(560);                                               // floor so the spinner reads
    const token = mode() === 'empty' ? '' : 'inv_' + Math.random().toString(36).slice(2, 12);
    try {
      if (mode() === 'denied') throw new DOMException('denied', 'NotAllowedError');
      if (!token) throw new DOMException('empty', 'DataError');
      await navigator.clipboard.writeText(token);
      set('copied', 'Copied ' + token);
    } catch (err) {
      const why = err.name === 'DataError' ? 'Nothing to copy - the token came back empty.'
        : window.isSecureContext ? 'Clipboard permission denied by the browser.'
        : 'Clipboard needs https - this page is not a secure context.';
      set('error', 'Write rejected: ' + err.name, why);
    }
    timer = setTimeout(() => set('idle', 'Idle - nothing minted yet.'), 2600);
  });
}
```
