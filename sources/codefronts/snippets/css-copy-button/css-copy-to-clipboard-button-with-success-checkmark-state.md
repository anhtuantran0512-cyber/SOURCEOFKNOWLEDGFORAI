---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-copy-to-clipboard-button-with-success-checkmark-state/"
title: "CSS Copy to Clipboard Button with Success Checkmark State"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "The reference build for the whole collection: a copy button that reads Copy, flips to Copied!"
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Copy to Clipboard Button with Success Checkmark State
Source: https://codefronts.com/snippets/css-copy-button/css-copy-to-clipboard-button-with-success-checkmark-state/

The reference build for the whole collection: a copy button that reads Copy, flips to Copied! with a checkmark, and reverts after two seconds. Icon and label crossfade in the same 200&nbsp;ms, the width never jumps because both labels are stacked in one grid cell, and the success is announced to screen readers as well as shown. Every other demo is a variation on this state machine.
## HTML
```html
<div class="cpy-01">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-01__sr" type="checkbox" id="cpy-01-dark">
  <label class="cpy-01__theme" for="cpy-01-dark" title="Switch light or dark theme">
    <svg class="cpy-01__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-01__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-01__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-01__stage">
    <div class="cpy-01__card">
      <p class="cpy-01__eyebrow"><span class="cpy-01__dot"></span>Install</p>
      <h2 class="cpy-01__title">Add the package</h2>
      <p class="cpy-01__lead">One command, one button, three states. Click it &mdash; the label and the icon change together, then hand themselves back after two seconds.</p>

      <div class="cpy-01__row">
        <code class="cpy-01__value" id="cpy-01-value">npm i @codefronts/clipboard</code>
        <button class="cpy-01__btn" type="button" data-state="idle" aria-describedby="cpy-01-hint">
          <span class="cpy-01__icons">
            <svg class="cpy-01__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-01__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <span class="cpy-01__labels">
            <span class="cpy-01__l1">Copy</span>
            <span class="cpy-01__l2">Copied!</span>
          </span>
        </button>
      </div>

      <p class="cpy-01__hint" id="cpy-01-hint">Tab to the button and press <kbd class="cpy-01__kbd">Enter</kbd> &mdash; keyboard and pointer run the identical path.</p>
      <p class="cpy-01__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-01 {
  --bg: #f6f7f9;
  --panel: #ffffff;
  --panel2: #f1f3f7;
  --ink: #0b1020;
  --muted: #5a6373;
  --line: rgba(11,16,32,.11);
  --accent: #4f46e5;
  --ok: #15803d;
  --ok-bg: rgba(21,128,61,.1);
  --err: #dc2626;
  --err-bg: rgba(220,38,38,.1);
  --dur: 200ms;
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

.cpy-01 *,
.cpy-01 *::before,
.cpy-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-01 {
    --accent: oklch(.53 .21 274);
    --ok: oklch(.55 .15 149);
    --ok-bg: oklch(.55 .15 149/.12);
    --err: oklch(.58 .21 25);
    --err-bg: oklch(.58 .21 25/.12);
  }
}

.cpy-01__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-01__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-01__theme {
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
  transition: background var(--dur),color var(--dur);
}

.cpy-01__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-01__moon {
  display: none;
}

.cpy-01__sr:focus-visible + .cpy-01__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-01__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-01__card {
  inline-size: min(100%,34rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .85rem;
  box-shadow: 0 1px 2px rgba(11,16,32,.05),0 26px 50px -34px rgba(11,16,32,.35);
}

.cpy-01__eyebrow {
  display: flex;
  align-items: center;
  gap: .5rem;
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-01__dot {
  inline-size: .4rem;
  block-size: .4rem;
  border-radius: 999px;
  background: var(--accent);
}

.cpy-01__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-01__lead {
  margin: 0 0 .35rem;
  font-size: .96rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-01__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .6rem;
  padding: .65rem .65rem .65rem .9rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--panel2);
}

.cpy-01__value {
  flex: 1 1 12rem;
  min-inline-size: 0;
  font-family: var(--mono);
  font-size: clamp(.8rem,1.6vw,.92rem);
  overflow-x: auto;
  white-space: nowrap;
  scrollbar-width: none;
}

.cpy-01__value::-webkit-scrollbar {
  display: none;
}

.cpy-01__btn {
  flex: none;
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  padding-inline: 1rem;
  border: 1px solid var(--line);
  border-radius: .8rem;
  background: var(--panel);
  color: var(--ink);
  font: inherit;
  font-size: .9rem;
  font-weight: 560;
  cursor: pointer;
  transition: background var(--dur),border-color var(--dur),color var(--dur),scale var(--dur);
}

.cpy-01__btn:hover {
  background: var(--panel2);
  border-color: color-mix(in srgb,var(--ink) 22%,transparent);
}

.cpy-01__btn:active {
  scale: .975;
}

.cpy-01__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpy-01__btn[data-state="copied"] {
  color: var(--ok);
  background: var(--ok-bg);
  border-color: color-mix(in srgb,var(--ok) 35%,transparent);
}

.cpy-01__btn[data-state="error"] {
  color: var(--err);
  background: var(--err-bg);
  border-color: color-mix(in srgb,var(--err) 35%,transparent);
}

.cpy-01__icons {
  position: relative;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  flex: none;
}

.cpy-01__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur),rotate var(--dur);
}

.cpy-01__i2 {
  opacity: 0;
  scale: .5;
  rotate: -22deg;
}

.cpy-01__btn[data-state="copied"] .cpy-01__i1 {
  opacity: 0;
  scale: .5;
  rotate: 18deg;
}

.cpy-01__btn[data-state="copied"] .cpy-01__i2 {
  opacity: 1;
  scale: 1;
  rotate: 0deg;
}

.cpy-01__labels {
  display: grid;
}

.cpy-01__labels span {
  grid-area: 1/1;
  transition: opacity var(--dur),translate var(--dur);
}

.cpy-01__l2 {
  opacity: 0;
  translate: 0 .45rem;
}

.cpy-01__btn[data-state="copied"] .cpy-01__l1 {
  opacity: 0;
  translate: 0 -.45rem;
}

.cpy-01__btn[data-state="copied"] .cpy-01__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-01__btn[data-state="error"] .cpy-01__l1 {
  opacity: 0;
}

.cpy-01__btn[data-state="error"] .cpy-01__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-01__hint {
  margin: 0;
  font-size: .86rem;
  line-height: 1.55;
  color: var(--muted);
}

.cpy-01__kbd {
  font-family: var(--mono);
  font-size: .76rem;
  padding: .15rem .4rem;
  border: 1px solid var(--line);
  border-block-end-width: 2px;
  border-radius: .35rem;
  background: var(--panel2);
}

.cpy-01__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

.cpy-01__btn[data-state="error"] ~ .cpy-01__live,
.cpy-01__card:has([data-state="error"]) .cpy-01__live {
  color: var(--err);
}

@media not (prefers-color-scheme: dark) {
  .cpy-01:has(#cpy-01-dark:checked) {
    --bg: #070910;
    --panel: #0d1119;
    --panel2: #151b26;
    --ink: #e9edf5;
    --muted: rgba(233,237,245,.62);
    --line: rgba(233,237,245,.14);
    --accent: #a5b4fc;
    --ok: #6ee7a8;
    --ok-bg: rgba(110,231,168,.14);
    --err: #fda4af;
    --err-bg: rgba(253,164,175,.14);
  }

  .cpy-01:has(#cpy-01-dark:checked) .cpy-01__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-01:has(#cpy-01-dark:checked) .cpy-01__sun {
    display: none;
  }

  .cpy-01:has(#cpy-01-dark:checked) .cpy-01__moon {
    display: block;
  }

  .cpy-01:has(#cpy-01-dark:checked) .cpy-01__card {
    box-shadow: 0 1px 2px rgba(0,0,0,.5),0 26px 50px -34px rgba(0,0,0,.8);
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-01:not([data-theme="light"]):not(:has(#cpy-01-dark:checked)) {
    --bg: #070910;
    --panel: #0d1119;
    --panel2: #151b26;
    --ink: #e9edf5;
    --muted: rgba(233,237,245,.62);
    --line: rgba(233,237,245,.14);
    --accent: #a5b4fc;
    --ok: #6ee7a8;
    --ok-bg: rgba(110,231,168,.14);
    --err: #fda4af;
    --err-bg: rgba(253,164,175,.14);
  }

  .cpy-01__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-01__sun {
    display: none;
  }

  .cpy-01__moon {
    display: block;
  }

  .cpy-01:has(#cpy-01-dark:checked) .cpy-01__sun {
    display: block;
  }

  .cpy-01:has(#cpy-01-dark:checked) .cpy-01__moon {
    display: none;
  }
}

.cpy-01[data-theme="dark"] {
  --bg: #070910;
  --panel: #0d1119;
  --panel2: #151b26;
  --ink: #e9edf5;
  --muted: rgba(233,237,245,.62);
  --line: rgba(233,237,245,.14);
  --accent: #a5b4fc;
  --ok: #6ee7a8;
  --ok-bg: rgba(110,231,168,.14);
  --err: #fda4af;
  --err-bg: rgba(253,164,175,.14);
}

@media (prefers-reduced-motion: reduce) {
  .cpy-01 *,
    .cpy-01 *::before,
    .cpy-01 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-01__card,
    .cpy-01__row,
    .cpy-01__btn,
    .cpy-01__theme {
    border-color: CanvasText;
    background: Canvas;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .cpy-01__btn[data-state="copied"] {
    color: CanvasText;
  }
}
```

## JavaScript
```js
const cpy01 = document.querySelector('.cpy-01');
if (cpy01) {
  const btn = cpy01.querySelector('.cpy-01__btn');
  const live = cpy01.querySelector('.cpy-01__live');
  const value = cpy01.querySelector('.cpy-01__value');
  let timer;
  const set = (state, message) => {
    btn.dataset.state = state;
    live.textContent = message;
    clearTimeout(timer);                       // never let two reverts race
    timer = setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, 2000);
  };
  btn.addEventListener('click', async () => {
    const text = value.textContent.trim();
    try {
      await navigator.clipboard.writeText(text); // rejects outside a secure context
      set('copied', 'Copied to clipboard');
    } catch {
      set('error', 'Copy blocked \u2014 select the text and press Ctrl C');
    }
  });
}
```
