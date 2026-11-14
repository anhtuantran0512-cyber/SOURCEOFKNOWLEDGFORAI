---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-copy-button-feedback-countdown-reset-timer/"
title: "CSS Copy Button Feedback Countdown Reset Timer"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "Most copy buttons revert on an invisible timer, so the user cannot tell whether the state is sticky or about to vanish."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Copy Button Feedback Countdown Reset Timer
Source: https://codefronts.com/snippets/css-copy-button/css-copy-button-feedback-countdown-reset-timer/

Most copy buttons revert on an invisible timer, so the user cannot tell whether the state is sticky or about to vanish. This one draws the wait: a countdown ring sweeps around the tick over two seconds, the button ignores clicks while it runs, and the ring restarts cleanly &mdash; no stacked timers, no flicker.
## HTML
```html
<div class="cpy-18">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-18__sr" type="checkbox" id="cpy-18-dark">
  <label class="cpy-18__theme" for="cpy-18-dark" title="Switch light or dark theme">
    <svg class="cpy-18__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-18__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-18__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-18__stage">
    <div class="cpy-18__card">
      <p class="cpy-18__eyebrow">Countdown reset &middot; 2 seconds, visible</p>
      <h2 class="cpy-18__title">Show the wait, guard the click</h2>
      <p class="cpy-18__lead">Copy it, then try clicking again immediately &mdash; the button holds its state, the ring runs down, and no second timer is created.</p>

      <div class="cpy-18__row">
        <code class="cpy-18__value" id="cpy-18-value">docker run -p 4173:4173 codefronts/preview:2027</code>
        <button class="cpy-18__btn" type="button" data-state="idle" aria-disabled="false">
          <span class="cpy-18__slot">
            <span class="cpy-18__ring" aria-hidden="true"></span>
            <svg class="cpy-18__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-18__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5.4 12.6 9.6 16.8 18.6 7.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <span class="cpy-18__labels"><span class="cpy-18__l1">Copy command</span><span class="cpy-18__l2">Copied!</span></span>
        </button>
      </div>

      <p class="cpy-18__live" role="status" aria-live="polite"></p>
      <p class="cpy-18__note">The ring is a <code>conic-gradient</code> whose angle animates because <code>--cpy-18-p</code> is registered with <code>@property</code> as a <code>&lt;number&gt;</code>. Without that registration the value would jump instead of sweeping.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-18 {
  --bg: #f7f7f8;
  --panel: #ffffff;
  --panel2: #f0f1f4;
  --ink: #0c0d11;
  --muted: #5c606b;
  --line: rgba(12,13,17,.12);
  --accent: #0f766e;
  --ok: #0f766e;
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

.cpy-18 *,
.cpy-18 *::before,
.cpy-18 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-18 {
    --accent: oklch(.52 .11 183);
    --ok: oklch(.52 .11 183);
  }
}

@property --cpy-18-p {
  syntax: '<number>';
  inherits: false;
  initial-value: 100;
}

.cpy-18__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-18__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-18__theme {
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

.cpy-18__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-18__moon {
  display: none;
}

.cpy-18__sr:focus-visible + .cpy-18__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-18__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-18__card {
  min-inline-size: 0;
  inline-size: min(100%,35rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .85rem;
  box-shadow: 0 1px 2px rgba(12,13,17,.05),0 28px 55px -36px rgba(12,13,17,.32);
}
/* Grid items default to min-width:auto, so the countdown row and the long
   value string forced these children past the card's content box and took
   the document sideways at 320-390px. */

.cpy-18__card > * {
  min-inline-size: 0;
}

.cpy-18__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-18__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-18__lead {
  margin: 0 0 .3rem;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-18__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
  padding: .65rem .65rem .65rem .95rem;
  border: 1px solid var(--line);
  border-radius: 1.05rem;
  background: var(--panel2);
}

.cpy-18__value {
  flex: 1 1 12rem;
  min-inline-size: 0;
  font-family: var(--mono);
  font-size: clamp(.76rem,1.6vw,.86rem);
  white-space: nowrap;
  overflow-x: auto;
  scrollbar-width: none;
}

.cpy-18__value::-webkit-scrollbar {
  display: none;
}

.cpy-18__btn {
  flex: none;
  min-block-size: 2.85rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  padding-inline: 1.05rem;
  border: 1px solid var(--line);
  border-radius: .85rem;
  background: var(--panel);
  color: var(--ink);
  font: inherit;
  font-size: .9rem;
  font-weight: 560;
  cursor: pointer;
  transition: background var(--dur),color var(--dur),border-color var(--dur),scale var(--dur);
}

.cpy-18__btn:hover {
  background: var(--panel2);
}

.cpy-18__btn:active {
  scale: .975;
}

.cpy-18__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpy-18__btn[data-state="copied"] {
  color: var(--ok);
  border-color: color-mix(in srgb,var(--ok) 40%,transparent);
  cursor: default;
}

.cpy-18__slot {
  position: relative;
  inline-size: 1.35rem;
  block-size: 1.35rem;
  flex: none;
  display: grid;
  place-items: center;
}

.cpy-18__slot svg {
  position: absolute;
  inline-size: .95rem;
  block-size: .95rem;
  opacity: 0;
  scale: .6;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-18__btn[data-state="idle"] .cpy-18__i1 {
  opacity: 1;
  scale: 1;
}

.cpy-18__btn[data-state="copied"] .cpy-18__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-18__ring {
  position: absolute;
  inset: 0;
  border-radius: 999px;
  opacity: 0;
  color: var(--ok);
  border: 2px solid currentColor;
  transition: opacity var(--dur);
}

.cpy-18__btn[data-state="copied"] .cpy-18__ring {
  opacity: 1;
}

@supports (background: conic-gradient(currentColor 50%,transparent 0)) {
  .cpy-18__ring {
    border: 0;
    background: conic-gradient(currentColor calc(var(--cpy-18-p,100) * 1%),transparent 0);
    -webkit-mask: radial-gradient(farthest-side,transparent 66%,#000 68%);
    mask: radial-gradient(farthest-side,transparent 66%,#000 68%);
  }

  .cpy-18__btn[data-state="copied"] .cpy-18__ring {
    animation: cpy-18-drain 2s linear forwards;
  }
}

@keyframes cpy-18-drain {
  from {
    --cpy-18-p: 100;
  }

  to {
    --cpy-18-p: 0;
  }
}

.cpy-18__labels {
  display: grid;
}

.cpy-18__labels span {
  grid-area: 1/1;
  transition: opacity var(--dur),translate var(--dur);
}

.cpy-18__l2 {
  opacity: 0;
  translate: 0 .4rem;
}

.cpy-18__btn[data-state="copied"] .cpy-18__l1 {
  opacity: 0;
  translate: 0 -.4rem;
}

.cpy-18__btn[data-state="copied"] .cpy-18__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-18__live {
  margin: 0;
  min-block-size: 1.25rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

.cpy-18__note {
  margin: 0;
  font-size: .85rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-18__note code {
  font-family: var(--mono);
  font-size: .77rem;
  padding: .08rem .28rem;
  border-radius: .3rem;
  background: var(--panel2);
}

@media not (prefers-color-scheme: dark) {
  .cpy-18:has(#cpy-18-dark:checked) {
    --bg: #08090c;
    --panel: #0e1014;
    --panel2: #171a1f;
    --ink: #eceef2;
    --muted: rgba(236,238,242,.62);
    --line: rgba(236,238,242,.14);
    --accent: #5eead4;
    --ok: #5eead4;
  }

  .cpy-18:has(#cpy-18-dark:checked) .cpy-18__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-18:has(#cpy-18-dark:checked) .cpy-18__sun {
    display: none;
  }

  .cpy-18:has(#cpy-18-dark:checked) .cpy-18__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-18:not([data-theme="light"]):not(:has(#cpy-18-dark:checked)) {
    --bg: #08090c;
    --panel: #0e1014;
    --panel2: #171a1f;
    --ink: #eceef2;
    --muted: rgba(236,238,242,.62);
    --line: rgba(236,238,242,.14);
    --accent: #5eead4;
    --ok: #5eead4;
  }

  .cpy-18__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-18__sun {
    display: none;
  }

  .cpy-18__moon {
    display: block;
  }

  .cpy-18:has(#cpy-18-dark:checked) .cpy-18__sun {
    display: block;
  }

  .cpy-18:has(#cpy-18-dark:checked) .cpy-18__moon {
    display: none;
  }
}

.cpy-18[data-theme="dark"] {
  --bg: #08090c;
  --panel: #0e1014;
  --panel2: #171a1f;
  --ink: #eceef2;
  --muted: rgba(236,238,242,.62);
  --line: rgba(236,238,242,.14);
  --accent: #5eead4;
  --ok: #5eead4;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-18 *,
    .cpy-18 *::before,
    .cpy-18 *::after {
    transition: none !important;
  }

  .cpy-18__btn[data-state="copied"] .cpy-18__ring {
    animation: none;
    background: conic-gradient(currentColor 100%,transparent 0);
  }
}

@media (forced-colors: active) {
  .cpy-18__card,
    .cpy-18__row,
    .cpy-18__btn,
    .cpy-18__theme {
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
const cpy18 = document.querySelector('.cpy-18');
if (cpy18) {
  const btn = cpy18.querySelector('.cpy-18__btn');
  const value = cpy18.querySelector('#cpy-18-value');
  const live = cpy18.querySelector('.cpy-18__live');
  const HOLD = 2000;                                  // must match the ring animation
  let timer;
  btn.addEventListener('click', async () => {
    if (btn.getAttribute('aria-disabled') === 'true') return;   // cooldown guard
    let ok = true;
    try { await navigator.clipboard.writeText(value.textContent.trim()); } catch { ok = false; }
    btn.dataset.state = 'idle';
    void btn.offsetWidth;                             // flush so the ring restarts from full
    btn.dataset.state = ok ? 'copied' : 'idle';
    btn.setAttribute('aria-disabled', String(ok));
    live.textContent = ok ? 'Copied - reverting in 2 seconds' : 'Clipboard blocked - press Ctrl C';
    clearTimeout(timer);                              // one timer, always
    timer = setTimeout(() => {
      btn.dataset.state = 'idle';
      btn.setAttribute('aria-disabled', 'false');
      live.textContent = '';
    }, HOLD);
  });
}
```
