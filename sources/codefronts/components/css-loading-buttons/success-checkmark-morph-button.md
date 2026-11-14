---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/success-checkmark-morph-button/"
title: "Success Checkmark Morph Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "The spinner's own stroke becomes the checkmark: one SVG path, animated with stroke-dasharray and stroke-dashoffset, so there is no spinner element swapped…"
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Success Checkmark Morph Button
Source: https://codefronts.com/components/css-loading-buttons/success-checkmark-morph-button/

The spinner's own stroke becomes the checkmark: one SVG path, animated with stroke-dasharray and stroke-dashoffset, so there is no spinner element swapped out for a tick element. The ring shortens, rotates into place and draws the check, holds for a readable beat, then reverts to idle. The failure branch draws a cross along the same path budget.
## HTML
```html
<div class="lb-06">
  <div class="lb-06__stage">
    <section class="lb-06__card" aria-labelledby="lb-06-h">
      <h2 class="lb-06__h" id="lb-06-h">Weekly digest</h2>
      <p class="lb-06__sub">Sent Fridays. Written by Jordan Lee. One click to confirm — the spinner becomes the tick.</p>

      <div class="lb-06__form">
        <span class="lb-06__input" aria-hidden="true">[email protected]</span>
        <button class="lb-06__btn" type="button" id="lb-06-btn" data-state="idle" aria-busy="false">
          <span class="lb-06__mark" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round">
              <circle class="lb-06__ring" cx="10" cy="10" r="7.4"/>
              <path class="lb-06__check" d="M5.4 10.4 8.6 13.6 14.8 6.8"/>
              <path class="lb-06__cross" d="M6.4 6.4l7.2 7.2M13.6 6.4l-7.2 7.2"/>
            </svg>
          </span>
          <span class="lb-06__faces">
            <span class="lb-06__face lb-06__face--idle">Subscribe</span>
            <span class="lb-06__face lb-06__face--pending">Confirming</span>
            <span class="lb-06__face lb-06__face--done">Subscribed</span>
            <span class="lb-06__face lb-06__face--error">Try again</span>
          </span>
        </button>
      </div>

      <label class="lb-06__toggle"><input type="checkbox" id="lb-06-fail"> Make the next attempt fail</label>
      <p class="lb-06__live" id="lb-06-live" role="status" aria-live="polite">Not subscribed yet.</p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-06 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #eef2ec;
  --surface: #ffffff;
  --ink: #1d2a22;
  --muted: #63776a;
  --rule: #d5e0d6;
  --accent: #2f6b4f;
  --mark: #ffffff;
  --bad: #a63b2c;
  --draw: 260ms;
  --hold: 1400ms;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 18px;
}

.lb-06 *,
.lb-06 *::before,
.lb-06 *::after {
  box-sizing: border-box;
}

.lb-06__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-06__card {
  inline-size: 100%;
  max-inline-size: 32rem;
  min-inline-size: 0;
  background: var(--surface);
  border-radius: 20px;
  padding: 26px 24px;
  box-shadow: 0 20px 40px -28px rgba(29, 42, 34, .55), 0 1px 0 var(--rule);
}

.lb-06__h {
  margin: 0;
  font-size: 21px;
  font-weight: 620;
  letter-spacing: -.02em;
}

.lb-06__sub {
  margin: 8px 0 20px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 46ch;
}

.lb-06__form {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  min-inline-size: 0;
}

.lb-06__input {
  flex: 1 1 12rem;
  min-inline-size: 0;
  font-size: 13px;
  color: var(--muted);
  background: var(--bg);
  border: 1px solid var(--rule);
  border-radius: 999px;
  padding: 12px 16px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.lb-06__btn {
  appearance: none;
  flex: none;
  border: 0;
  background: var(--accent);
  color: var(--mark);
  border-radius: 999px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  padding: 0 20px 0 16px;
  min-block-size: 44px;
  min-inline-size: 0;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  cursor: pointer;
  transition: background 240ms ease;
}

.lb-06__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.lb-06__btn[data-state="pending"] {
  cursor: progress;
}

.lb-06__btn[data-state="error"] {
  background: var(--bad);
}

.lb-06__mark {
  display: inline-flex;
  flex: none;
}

.lb-06__ring,
.lb-06__check,
.lb-06__cross {
  transition: stroke-dashoffset var(--draw) ease, opacity 160ms linear;
}

.lb-06__ring {
  stroke-dasharray: 12 46;
  stroke-dashoffset: 0;
  transform-box: fill-box;
  transform-origin: 50% 50%;
}

.lb-06__check {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
}

.lb-06__cross {
  stroke-dasharray: 22;
  stroke-dashoffset: 22;
}

.lb-06__btn[data-state="idle"] .lb-06__ring {
  stroke-dasharray: 47 0;
}

.lb-06__btn[data-state="pending"] .lb-06__ring {
  animation: lb-06-spin 700ms linear infinite;
}

.lb-06__btn[data-state="done"] .lb-06__ring {
  opacity: 0;
}

.lb-06__btn[data-state="done"] .lb-06__check {
  stroke-dashoffset: 0;
}

.lb-06__btn[data-state="error"] .lb-06__ring {
  opacity: 0;
}

.lb-06__btn[data-state="error"] .lb-06__cross {
  stroke-dashoffset: 0;
}

@keyframes lb-06-spin {
  to {
    transform: rotate(1turn);
  }
}

.lb-06__faces {
  display: grid;
  place-items: center;
}

.lb-06__face {
  grid-area: 1 / 1;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: opacity 180ms ease, visibility 180ms;
}

.lb-06__btn[data-state="idle"] .lb-06__face--idle,
.lb-06__btn[data-state="pending"] .lb-06__face--pending,
.lb-06__btn[data-state="done"] .lb-06__face--done,
.lb-06__btn[data-state="error"] .lb-06__face--error {
  opacity: 1;
  visibility: visible;
}

.lb-06__toggle {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 18px 0 0;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
}

.lb-06__toggle input {
  accent-color: var(--accent);
  inline-size: 15px;
  block-size: 15px;
}

.lb-06__live {
  margin: 4px 0 0;
  font-size: 12.5px;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-06__ring,
    .lb-06__check,
    .lb-06__cross {
    transition: none;
  }

  .lb-06__btn[data-state="pending"] .lb-06__ring {
    animation: none;
    stroke-dasharray: 24 24;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-06 {
    --bg: #10160f;
    --surface: #18211a;
    --ink: #e7f0e6;
    --muted: #94a798;
    --rule: #263226;
    --accent: #4fa87a;
    --mark: #0e150f;
    --bad: #e07a68;
  }
}

[data-theme="dark"] .lb-06 {
  --bg: #10160f;
  --surface: #18211a;
  --ink: #e7f0e6;
  --muted: #94a798;
  --rule: #263226;
  --accent: #4fa87a;
  --mark: #0e150f;
  --bad: #e07a68;
}
```

## JavaScript
```js
const btn = document.getElementById('lb-06-btn');
const live = document.getElementById('lb-06-live');
const failBox = document.getElementById('lb-06-fail');
let timer;

const set = (state, message) => {
  btn.dataset.state = state;
  btn.setAttribute('aria-busy', String(state === 'pending'));
  live.textContent = message;
};

btn.addEventListener('click', () => {
  if (btn.dataset.state === 'pending') return;
  clearTimeout(timer);
  set('pending', 'Confirming subscription');
  timer = setTimeout(() => {
    if (failBox.checked) {
      set('error', 'That address was rejected. Try again.');
    } else {
      set('done', 'Subscribed. Check your inbox to confirm.');
    }
    timer = setTimeout(() => set('idle', failBox.checked ? 'Not subscribed yet.' : 'Subscribed.'), 1400);
  }, 1300);
});
```
