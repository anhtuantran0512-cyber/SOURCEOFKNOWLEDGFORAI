---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-copy-button-with-tooltip-feedback/"
title: "CSS Copy Button with Tooltip Feedback"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "A tooltip that does two jobs: it explains the button before the click (Copy to clipboard) and confirms it after (Copied to clipboard!). It opens on hover and…"
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Copy Button with Tooltip Feedback
Source: https://codefronts.com/snippets/css-copy-button/css-copy-button-with-tooltip-feedback/

A tooltip that does two jobs: it explains the button before the click (Copy to clipboard) and confirms it after (Copied to clipboard!). It opens on hover and on :focus-visible, so keyboard users get the same hint, and stays pinned for two seconds after a successful copy even when the pointer has already left.
## HTML
```html
<div class="cpy-03">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-03__sr" type="checkbox" id="cpy-03-dark">
  <label class="cpy-03__theme" for="cpy-03-dark" title="Switch light or dark theme">
    <svg class="cpy-03__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-03__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-03__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-03__stage">
    <div class="cpy-03__card">
      <p class="cpy-03__eyebrow">Tooltip feedback</p>
      <h2 class="cpy-03__title">Hint before, confirmation after</h2>
      <p class="cpy-03__lead">Hover the button &mdash; or <kbd class="cpy-03__kbd">Tab</kbd> to it, which shows the same bubble. After a copy the tooltip pins itself for two seconds, so it still lands if your pointer has already moved on.</p>

      <div class="cpy-03__panel">
        <div class="cpy-03__meta">
          <span class="cpy-03__badge">Build 4181</span>
          <code class="cpy-03__sha" id="cpy-03-value">9f2c41ad</code>
        </div>
        <div class="cpy-03__wrap" data-pin="0" data-state="idle">
          <button class="cpy-03__btn" type="button" aria-label="Copy commit SHA 9f2c41ad" aria-describedby="cpy-03-tip">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </button>
          <span class="cpy-03__tip" id="cpy-03-tip" role="tooltip">
            <span class="cpy-03__t1">Copy to clipboard</span>
            <span class="cpy-03__t2">Copied to clipboard!</span>
          </span>
        </div>
      </div>

      <p class="cpy-03__note">The bubble is one element: both strings sit in a single grid cell, so it never resizes mid-transition.</p>
      <p class="cpy-03__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-03 {
  --bg: #f6f7fb;
  --panel: #ffffff;
  --panel2: #f0f2f7;
  --ink: #0b1020;
  --muted: #5b6474;
  --line: rgba(11,16,32,.11);
  --accent: #4338ca;
  --ok: #0f766e;
  --tip-bg: #0b1020;
  --tip-ink: #f5f6fa;
  --err: #dc2626;
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

.cpy-03 *,
.cpy-03 *::before,
.cpy-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-03 {
    --accent: oklch(.48 .2 277);
    --ok: oklch(.52 .11 183);
  }
}

.cpy-03__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-03__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-03__theme {
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

.cpy-03__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-03__moon {
  display: none;
}

.cpy-03__sr:focus-visible + .cpy-03__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-03__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-03__card {
  inline-size: min(100%,34rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .9rem;
  box-shadow: 0 1px 2px rgba(11,16,32,.05),0 26px 50px -34px rgba(11,16,32,.35);
}

.cpy-03__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-03__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-03__lead {
  margin: 0;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-03__kbd {
  font-family: var(--mono);
  font-size: .74rem;
  padding: .12rem .38rem;
  border: 1px solid var(--line);
  border-block-end-width: 2px;
  border-radius: .35rem;
  background: var(--panel2);
  color: var(--ink);
}

.cpy-03__panel {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-block-start: .3rem;
  padding: clamp(1.1rem,3vw,1.6rem);
  border: 1px solid var(--line);
  border-radius: 1.2rem;
  background: var(--panel2);
}

.cpy-03__meta {
  display: grid;
  gap: .35rem;
}

.cpy-03__badge {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-03__sha {
  font-family: var(--mono);
  font-size: clamp(1.15rem,3vw,1.5rem);
  letter-spacing: -.01em;
}

.cpy-03__wrap {
  position: relative;
  display: inline-grid;
  place-items: center;
}

.cpy-03__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  padding: 0;
  border: 1px solid var(--line);
  border-radius: .8rem;
  background: var(--panel);
  color: var(--ink);
  cursor: pointer;
  transition: background var(--dur),color var(--dur),border-color var(--dur),scale var(--dur);
}

.cpy-03__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-03__btn:hover {
  background: var(--panel2);
}

.cpy-03__btn:active {
  scale: .96;
}

.cpy-03__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpy-03__wrap[data-state="copied"] .cpy-03__btn {
  color: var(--ok);
  border-color: color-mix(in srgb,var(--ok) 40%,transparent);
}

.cpy-03__wrap[data-state="error"] .cpy-03__btn {
  color: var(--err);
  border-color: color-mix(in srgb,var(--err) 40%,transparent);
}

.cpy-03__tip {
  position: absolute;
  inset-block-end: 100%;
  inset-inline-start: 50%;
  z-index: 2;
  translate: -50% .2rem;
  display: grid;
  padding: .5rem .7rem;
  border-radius: .6rem;
  background: var(--tip-bg);
  color: var(--tip-ink);
  font-size: .8rem;
  font-weight: 520;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transition: opacity var(--dur) ease,translate var(--dur) ease,visibility var(--dur) allow-discrete;
}

.cpy-03__tip::after {
  content: "";
  position: absolute;
  inset-block-start: 100%;
  inset-inline-start: 50%;
  inline-size: .5rem;
  block-size: .5rem;
  translate: -50% -60%;
  rotate: 45deg;
  background: var(--tip-bg);
  border-radius: .1rem;
}

.cpy-03__tip span {
  grid-area: 1/1;
  transition: opacity var(--dur) ease;
}

.cpy-03__t2 {
  opacity: 0;
}

.cpy-03__wrap:hover .cpy-03__tip,
.cpy-03__btn:focus-visible + .cpy-03__tip,
.cpy-03__wrap[data-pin="1"] .cpy-03__tip {
  opacity: 1;
  visibility: visible;
  translate: -50% -.5rem;
}

.cpy-03__wrap[data-state="copied"] .cpy-03__t1,
.cpy-03__wrap[data-state="error"] .cpy-03__t1 {
  opacity: 0;
}

.cpy-03__wrap[data-state="copied"] .cpy-03__t2,
.cpy-03__wrap[data-state="error"] .cpy-03__t2 {
  opacity: 1;
}

.cpy-03__wrap[data-state="copied"] .cpy-03__tip {
  background: var(--ok);
}

.cpy-03__wrap[data-state="copied"] .cpy-03__tip::after {
  background: var(--ok);
}

.cpy-03__wrap[data-state="error"] .cpy-03__tip {
  background: var(--err);
}

.cpy-03__wrap[data-state="error"] .cpy-03__tip::after {
  background: var(--err);
}

.cpy-03__note {
  margin: 0;
  font-size: .86rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-03__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

@media not (prefers-color-scheme: dark) {
  .cpy-03:has(#cpy-03-dark:checked) {
    --bg: #070911;
    --panel: #0d111a;
    --panel2: #151a25;
    --ink: #e9edf5;
    --muted: rgba(233,237,245,.62);
    --line: rgba(233,237,245,.14);
    --accent: #a5b4fc;
    --ok: #5eead4;
    --tip-bg: #e9edf5;
    --tip-ink: #0b1020;
  }

  .cpy-03:has(#cpy-03-dark:checked) .cpy-03__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-03:has(#cpy-03-dark:checked) .cpy-03__sun {
    display: none;
  }

  .cpy-03:has(#cpy-03-dark:checked) .cpy-03__moon {
    display: block;
  }

  .cpy-03:has(#cpy-03-dark:checked) .cpy-03__wrap[data-state="copied"] .cpy-03__tip {
    color: #04231f;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-03:not([data-theme="light"]):not(:has(#cpy-03-dark:checked)) {
    --bg: #070911;
    --panel: #0d111a;
    --panel2: #151a25;
    --ink: #e9edf5;
    --muted: rgba(233,237,245,.62);
    --line: rgba(233,237,245,.14);
    --accent: #a5b4fc;
    --ok: #5eead4;
    --tip-bg: #e9edf5;
    --tip-ink: #0b1020;
  }

  .cpy-03__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-03__sun {
    display: none;
  }

  .cpy-03__moon {
    display: block;
  }

  .cpy-03:has(#cpy-03-dark:checked) .cpy-03__sun {
    display: block;
  }

  .cpy-03:has(#cpy-03-dark:checked) .cpy-03__moon {
    display: none;
  }

  .cpy-03__wrap[data-state="copied"] .cpy-03__tip {
    color: #04231f;
  }
}

.cpy-03[data-theme="dark"] {
  --bg: #070911;
  --panel: #0d111a;
  --panel2: #151a25;
  --ink: #e9edf5;
  --muted: rgba(233,237,245,.62);
  --line: rgba(233,237,245,.14);
  --accent: #a5b4fc;
  --ok: #5eead4;
  --tip-bg: #e9edf5;
  --tip-ink: #0b1020;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-03 *,
    .cpy-03 *::before,
    .cpy-03 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-03__card,
    .cpy-03__panel,
    .cpy-03__btn,
    .cpy-03__theme,
    .cpy-03__tip {
    border: 1px solid CanvasText;
    background: Canvas;
    color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .cpy-03__tip::after {
    background: Canvas;
    border: 1px solid CanvasText;
  }
}
```

## JavaScript
```js
const cpy03 = document.querySelector('.cpy-03');
if (cpy03) {
  const wrap = cpy03.querySelector('.cpy-03__wrap');
  const btn = cpy03.querySelector('.cpy-03__btn');
  const live = cpy03.querySelector('.cpy-03__live');
  const value = cpy03.querySelector('.cpy-03__sha');
  const t2 = cpy03.querySelector('.cpy-03__t2');
  let timer;
  const show = (state, tip, message) => {
    wrap.dataset.state = state;
    wrap.dataset.pin = '1';                  // keep it open after the pointer leaves
    t2.textContent = tip;
    live.textContent = message;
    clearTimeout(timer);
    timer = setTimeout(() => { wrap.dataset.pin = '0'; wrap.dataset.state = 'idle'; live.textContent = ''; }, 2000);
  };
  btn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(value.textContent.trim());
      show('copied', 'Copied to clipboard!', 'Commit SHA copied');
    } catch {
      show('error', 'Copy blocked', 'Clipboard permission denied');
    }
  });
}
```
