---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/error-state-with-shake-and-retry/"
title: "Error State with Shake and Retry"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "Failure has to be as legible as success."
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Error State with Shake and Retry
Source: https://codefronts.com/components/css-loading-buttons/error-state-with-shake-and-retry/

Failure has to be as legible as success. The button takes a red surface, a short horizontal shake built purely from transform, and a label that becomes an explicit retry affordance instead of quietly reverting to idle. Under reduced motion the shake is replaced by a colour and label change rather than removed, because the feedback is the message.
## HTML
```html
<div class="lb-07">
  <div class="lb-07__stage">
    <section class="lb-07__sheet" aria-labelledby="lb-07-h">
      <h2 class="lb-07__h" id="lb-07-h">Attachments</h2>

      <ul class="lb-07__files">
        <li class="lb-07__file">
          <span class="lb-07__fic" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M11.5 2.5H5.5v15h9V6z"/><path d="M11.5 2.5V6h3"/></svg>
          </span>
          <span class="lb-07__fname">q3-forecast.xlsx</span>
          <span class="lb-07__fsize">2.4 MB</span>
        </li>
        <li class="lb-07__file">
          <span class="lb-07__fic" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M11.5 2.5H5.5v15h9V6z"/><path d="M11.5 2.5V6h3"/></svg>
          </span>
          <span class="lb-07__fname">handover-notes.md</span>
          <span class="lb-07__fsize">11 KB</span>
        </li>
      </ul>

      <div class="lb-07__foot">
        <button class="lb-07__btn" type="button" id="lb-07-btn" data-state="idle" aria-busy="false">
          <span class="lb-07__ic lb-07__ic--up" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 15.5V4.5M5.5 9 10 4.5 14.5 9"/></svg>
          </span>
          <span class="lb-07__ic lb-07__ic--dots" aria-hidden="true"><i></i><i></i><i></i></span>
          <span class="lb-07__ic lb-07__ic--bad" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 3.2 18 16.8H2z"/><path d="M10 8v3.4"/><circle cx="10" cy="14" r=".9" fill="currentColor" stroke="none"/></svg>
          </span>
          <span class="lb-07__faces">
            <span class="lb-07__face lb-07__face--idle">Upload 2 files</span>
            <span class="lb-07__face lb-07__face--pending">Uploading</span>
            <span class="lb-07__face lb-07__face--error" id="lb-07-retry">Retry upload</span>
          </span>
        </button>
        <p class="lb-07__hint" id="lb-07-alert" role="alert"></p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-07 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #f2f2f1;
  --surface: #ffffff;
  --ink: #121212;
  --muted: #6d6d6d;
  --rule: #1212121f;
  --accent: #121212;
  --bad: #c62f22;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 18px;
}

.lb-07 *,
.lb-07 *::before,
.lb-07 *::after {
  box-sizing: border-box;
}

.lb-07__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-07__sheet {
  inline-size: 100%;
  max-inline-size: 33rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1.5px solid var(--ink);
  border-radius: 6px;
  padding: 22px;
  box-shadow: 6px 6px 0 var(--ink);
}

.lb-07__h {
  margin: 0 0 16px;
  font-size: 19px;
  font-weight: 640;
  letter-spacing: -.015em;
}

.lb-07__files {
  list-style: none;
  margin: 0 0 18px;
  padding: 0;
  display: grid;
  gap: 8px;
}

.lb-07__file {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border: 1px solid var(--rule);
  border-radius: 4px;
  min-inline-size: 0;
}

.lb-07__fic {
  flex: none;
  color: var(--muted);
  display: inline-flex;
}

.lb-07__fname {
  font-size: 13px;
  font-weight: 520;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.lb-07__fsize {
  margin-inline-start: auto;
  flex: none;
  font-size: 11.5px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.lb-07__foot {
  display: grid;
  gap: 10px;
  justify-items: start;
}

.lb-07__btn {
  appearance: none;
  border: 1.5px solid var(--accent);
  background: var(--accent);
  color: #fbfbfb;
  border-radius: 6px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  padding: 0 18px;
  min-block-size: 44px;
  min-inline-size: 0;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  cursor: pointer;
  transition: background 160ms linear, border-color 160ms linear;
}

.lb-07__btn:focus-visible {
  outline: 3px solid var(--bad);
  outline-offset: 3px;
}

.lb-07__btn[data-state="pending"] {
  cursor: progress;
}

.lb-07__btn[data-state="error"] {
  background: var(--bad);
  border-color: var(--bad);
  animation: lb-07-shake 340ms cubic-bezier(.36, .07, .19, .97) both;
}

@keyframes lb-07-shake {
  10%,
    90% {
    transform: translate3d(-2px, 0, 0);
  }

  30%,
    70% {
    transform: translate3d(4px, 0, 0);
  }

  50% {
    transform: translate3d(-4px, 0, 0);
  }

  100% {
    transform: translate3d(0, 0, 0);
  }
}

.lb-07__ic {
  display: none;
  flex: none;
}

.lb-07__btn[data-state="idle"] .lb-07__ic--up,
.lb-07__btn[data-state="pending"] .lb-07__ic--dots,
.lb-07__btn[data-state="error"] .lb-07__ic--bad {
  display: inline-flex;
  align-items: center;
  gap: 3px;
}

.lb-07__ic--dots i {
  inline-size: 4px;
  block-size: 4px;
  border-radius: 50%;
  background: currentColor;
  animation: lb-07-bounce 800ms ease-in-out infinite;
}

.lb-07__ic--dots i:nth-child(2) {
  animation-delay: 130ms;
}

.lb-07__ic--dots i:nth-child(3) {
  animation-delay: 260ms;
}

@keyframes lb-07-bounce {
  0%,
    100% {
    transform: translateY(2px);
    opacity: .45;
  }

  50% {
    transform: translateY(-2px);
    opacity: 1;
  }
}

.lb-07__faces {
  display: grid;
  place-items: center;
}

.lb-07__face {
  grid-area: 1 / 1;
  white-space: nowrap;
  visibility: hidden;
}

.lb-07__btn[data-state="idle"] .lb-07__face--idle,
.lb-07__btn[data-state="pending"] .lb-07__face--pending,
.lb-07__btn[data-state="error"] .lb-07__face--error {
  visibility: visible;
}

.lb-07__hint {
  margin: 0;
  min-block-size: 18px;
  font-size: 12.5px;
  font-weight: 560;
  color: var(--bad);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-07__btn[data-state="error"] {
    animation: none;
    box-shadow: inset 0 0 0 2px #fbfbfb;
  }

  .lb-07__ic--dots i {
    animation: none;
    opacity: .85;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-07 {
    --bg: #121212;
    --surface: #1a1a1a;
    --ink: #f0f0f0;
    --muted: #9a9a9a;
    --rule: #f0f0f024;
    --accent: #f0f0f0;
    --bad: #ef6a5a;
  }

  .lb-07__btn {
    color: #121212;
  }

  .lb-07__sheet {
    box-shadow: 6px 6px 0 #2e2e2e;
  }
}

[data-theme="dark"] .lb-07 {
  --bg: #121212;
  --surface: #1a1a1a;
  --ink: #f0f0f0;
  --muted: #9a9a9a;
  --rule: #f0f0f024;
  --accent: #f0f0f0;
  --bad: #ef6a5a;
}
```

## JavaScript
```js
const btn = document.getElementById('lb-07-btn');
const alertBox = document.getElementById('lb-07-alert');
const retry = document.getElementById('lb-07-retry');
let attempts = 0;
let timer;

btn.addEventListener('click', () => {
  if (btn.dataset.state === 'pending') return;
  clearTimeout(timer);
  btn.dataset.state = 'pending';
  btn.setAttribute('aria-busy', 'true');
  alertBox.textContent = '';
  timer = setTimeout(() => {
    attempts += 1;
    btn.setAttribute('aria-busy', 'false');
    btn.removeAttribute('data-state');
    void btn.offsetWidth;
    btn.dataset.state = 'error';
    if (attempts >= 3) {
      retry.textContent = 'Upload one at a time';
      alertBox.textContent = 'Upload failed ' + attempts + ' times. Try sending the files individually.';
    } else {
      retry.textContent = 'Retry upload';
      alertBox.textContent = 'Upload failed: the connection dropped at 1.8 MB.';
    }
  }, 1400);
});
```
