---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-clipboard-api-copy-button-with-fallback/"
title: "CSS Clipboard API Copy Button with Fallback"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "The demo that answers the single most-searched failure in this topic: why is navigator.clipboard undefined? A live environment probe reports secure context,…"
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Clipboard API Copy Button with Fallback
Source: https://codefronts.com/snippets/css-copy-button/css-clipboard-api-copy-button-with-fallback/

The demo that answers the single most-searched failure in this topic: why is navigator.clipboard undefined? A live environment probe reports secure context, API availability and permission result, the button copies through writeText() and silently falls back to a hidden <textarea> plus execCommand('copy') when it cannot, then tells you which path actually did the work.
## HTML
```html
<div class="cpy-05">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-05__sr" type="checkbox" id="cpy-05-dark">
  <label class="cpy-05__theme" for="cpy-05-dark" title="Switch light or dark theme">
    <svg class="cpy-05__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-05__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-05__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-05__stage">
    <div class="cpy-05__card">
      <p class="cpy-05__eyebrow">Clipboard API &middot; with fallback</p>
      <h2 class="cpy-05__title">Copy that survives an insecure origin</h2>

      <div class="cpy-05__row">
        <code class="cpy-05__value">pnpm dlx codefronts@latest init</code>
        <button class="cpy-05__btn" type="button" data-state="idle">
          <span class="cpy-05__icons">
            <svg class="cpy-05__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-05__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <span class="cpy-05__labels"><span class="cpy-05__l1">Copy</span><span class="cpy-05__l2">Copied</span></span>
        </button>
      </div>

      <dl class="cpy-05__probe">
        <div><dt>Secure context</dt><dd id="cpy-05-secure">checking</dd></div>
        <div><dt>navigator.clipboard</dt><dd id="cpy-05-api">checking</dd></div>
        <div><dt>Path used</dt><dd id="cpy-05-path">not run yet</dd></div>
      </dl>

      <p class="cpy-05__live" role="status" aria-live="polite">Press Copy to see which path this browser takes.</p>
      <p class="cpy-05__note"><code>writeText()</code> first; on rejection a hidden <code>&lt;textarea&gt;</code> plus <code>execCommand('copy')</code>. If both fail the button says so instead of pretending.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-05 {
  --bg: #f5f7f6;
  --panel: #ffffff;
  --panel2: #eef1f0;
  --ink: #0a0f0d;
  --muted: #586360;
  --line: rgba(10,15,13,.11);
  --accent: #0d9488;
  --ok: #15803d;
  --ok-bg: rgba(21,128,61,.1);
  --warn: #b45309;
  --err: #dc2626;
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

.cpy-05 *,
.cpy-05 *::before,
.cpy-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-05 {
    --accent: oklch(.6 .12 183);
    --ok: oklch(.55 .15 149);
    --ok-bg: oklch(.55 .15 149/.12);
    --warn: oklch(.56 .14 62);
    --err: oklch(.58 .21 25);
  }
}

.cpy-05__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-05__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-05__theme {
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

.cpy-05__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-05__moon {
  display: none;
}

.cpy-05__sr:focus-visible + .cpy-05__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-05__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-05__card {
  inline-size: min(100%,36rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .95rem;
  box-shadow: 0 1px 2px rgba(10,15,13,.05),0 26px 50px -34px rgba(10,15,13,.32);
}
/* Grid/flex children default to min-width:auto, so the long copied
   value forced the card past the stage and took the document sideways
   at 320px. */

.cpy-05__card {
  min-inline-size: 0;
}

.cpy-05__card > * {
  min-inline-size: 0;
}

.cpy-05__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-05__title {
  margin: 0 0 .2rem;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-05__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .6rem;
  padding: .6rem .6rem .6rem .9rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--panel2);
}

.cpy-05__value {
  flex: 1 1 12rem;
  min-inline-size: 0;
  font-family: var(--mono);
  font-size: clamp(.8rem,1.6vw,.9rem);
  white-space: nowrap;
  overflow-x: auto;
  scrollbar-width: none;
}

.cpy-05__value::-webkit-scrollbar {
  display: none;
}

.cpy-05__btn {
  flex: none;
  min-block-size: 2.75rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  padding-inline: 1rem;
  border: 1px solid transparent;
  border-radius: .8rem;
  background: var(--ink);
  color: var(--panel);
  font: inherit;
  font-size: .9rem;
  font-weight: 560;
  cursor: pointer;
  transition: background var(--dur),color var(--dur),scale var(--dur);
}

.cpy-05__btn:active {
  scale: .975;
}

.cpy-05__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-05__btn[data-state="copied"] {
  background: var(--ok);
  color: #fff;
}

.cpy-05__btn[data-state="fallback"] {
  background: var(--warn);
  color: #fff;
}

.cpy-05__btn[data-state="error"] {
  background: var(--err);
  color: #fff;
}

.cpy-05__icons {
  position: relative;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  flex: none;
}

.cpy-05__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-05__i2 {
  opacity: 0;
  scale: .5;
}

.cpy-05__btn:not([data-state="idle"]) .cpy-05__i1 {
  opacity: 0;
  scale: .5;
}

.cpy-05__btn:not([data-state="idle"]) .cpy-05__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-05__labels {
  display: grid;
}

.cpy-05__labels span {
  grid-area: 1/1;
  transition: opacity var(--dur),translate var(--dur);
}

.cpy-05__l2 {
  opacity: 0;
  translate: 0 .4rem;
}

.cpy-05__btn:not([data-state="idle"]) .cpy-05__l1 {
  opacity: 0;
  translate: 0 -.4rem;
}

.cpy-05__btn:not([data-state="idle"]) .cpy-05__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-05__probe {
  display: grid;
  gap: 0;
  margin: 0;
  border: 1px solid var(--line);
  border-radius: 1rem;
  overflow: hidden;
}

.cpy-05__probe > div {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 1rem;
  align-items: center;
  padding: .7rem 1rem;
  border-block-start: 1px solid var(--line);
}

.cpy-05__probe > div:first-child {
  border-block-start: 0;
}

.cpy-05__probe dt {
  font-family: var(--mono);
  font-size: .8rem;
  color: var(--muted);
}

.cpy-05__probe dd {
  margin: 0;
  font-family: var(--mono);
  font-size: .8rem;
  font-weight: 520;
}

.cpy-05__probe dd[data-ok="yes"] {
  color: var(--ok);
}

.cpy-05__probe dd[data-ok="no"] {
  color: var(--err);
}

.cpy-05__probe dd[data-ok="warn"] {
  color: var(--warn);
}

.cpy-05__live {
  margin: 0;
  min-block-size: 1.3rem;
  font-family: var(--mono);
  font-size: .8rem;
  color: var(--accent);
}

.cpy-05__note {
  margin: 0;
  font-size: .86rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-05__note code {
  font-family: var(--mono);
  font-size: .78rem;
  padding: .1rem .3rem;
  border-radius: .3rem;
  background: var(--panel2);
}

@media not (prefers-color-scheme: dark) {
  .cpy-05:has(#cpy-05-dark:checked) {
    --bg: #060a09;
    --panel: #0c1211;
    --panel2: #141b1a;
    --ink: #e8efec;
    --muted: rgba(232,239,236,.62);
    --line: rgba(232,239,236,.14);
    --accent: #5eead4;
    --ok: #6ee7a8;
    --ok-bg: rgba(110,231,168,.13);
    --warn: #fbbf24;
    --err: #fda4af;
  }

  .cpy-05:has(#cpy-05-dark:checked) .cpy-05__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-05:has(#cpy-05-dark:checked) .cpy-05__sun {
    display: none;
  }

  .cpy-05:has(#cpy-05-dark:checked) .cpy-05__moon {
    display: block;
  }

  .cpy-05:has(#cpy-05-dark:checked) .cpy-05__btn:not([data-state="idle"]) {
    color: #04231f;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-05:not([data-theme="light"]):not(:has(#cpy-05-dark:checked)) {
    --bg: #060a09;
    --panel: #0c1211;
    --panel2: #141b1a;
    --ink: #e8efec;
    --muted: rgba(232,239,236,.62);
    --line: rgba(232,239,236,.14);
    --accent: #5eead4;
    --ok: #6ee7a8;
    --ok-bg: rgba(110,231,168,.13);
    --warn: #fbbf24;
    --err: #fda4af;
  }

  .cpy-05__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-05__sun {
    display: none;
  }

  .cpy-05__moon {
    display: block;
  }

  .cpy-05:has(#cpy-05-dark:checked) .cpy-05__sun {
    display: block;
  }

  .cpy-05:has(#cpy-05-dark:checked) .cpy-05__moon {
    display: none;
  }

  .cpy-05__btn:not([data-state="idle"]) {
    color: #04231f;
  }
}

.cpy-05[data-theme="dark"] {
  --bg: #060a09;
  --panel: #0c1211;
  --panel2: #141b1a;
  --ink: #e8efec;
  --muted: rgba(232,239,236,.62);
  --line: rgba(232,239,236,.14);
  --accent: #5eead4;
  --ok: #6ee7a8;
  --ok-bg: rgba(110,231,168,.13);
  --warn: #fbbf24;
  --err: #fda4af;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-05 *,
    .cpy-05 *::before,
    .cpy-05 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-05__card,
    .cpy-05__row,
    .cpy-05__btn,
    .cpy-05__theme,
    .cpy-05__probe {
    border-color: CanvasText;
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
const cpy05 = document.querySelector('.cpy-05');
if (cpy05) {
  const q = (s) => cpy05.querySelector(s);
  const btn = q('.cpy-05__btn'), live = q('.cpy-05__live'), pathOut = q('#cpy-05-path');
  const flag = (el, ok, text) => { el.dataset.ok = ok; el.textContent = text; };
  flag(q('#cpy-05-secure'), window.isSecureContext ? 'yes' : 'no', window.isSecureContext ? 'true (https or localhost)' : 'false (http:// or file://)');
  flag(q('#cpy-05-api'), navigator.clipboard ? 'yes' : 'no', navigator.clipboard ? 'available' : 'undefined');
  const legacy = (text) => {                       // deprecated, still the safety net
    const ta = document.createElement('textarea');
    ta.value = text; ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;top:0;left:-9999px;opacity:0';
    document.body.append(ta); ta.select();
    let ok = false;
    try { ok = document.execCommand('copy'); } catch { ok = false; }
    ta.remove();
    return ok;
  };
  let timer;
  btn.addEventListener('click', async () => {
    const text = q('.cpy-05__value').textContent.trim();
    let how = 'failed';
    try { await navigator.clipboard.writeText(text); how = 'async'; }
    catch { how = legacy(text) ? 'fallback' : 'failed'; }
    const map = { async: ['copied', 'yes', 'navigator.clipboard.writeText()'], fallback: ['fallback', 'warn', 'execCommand fallback'], failed: ['error', 'no', 'blocked - press Ctrl C'] };
    const [state, ok, label] = map[how];
    btn.dataset.state = state; flag(pathOut, ok, label);
    live.textContent = how === 'failed' ? 'Both paths blocked here - select the command and press Ctrl C.' : 'Copied via ' + label;
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; }, 2000);
  });
}
```
