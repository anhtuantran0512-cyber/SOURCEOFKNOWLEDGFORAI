---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-copy-button-reusable-class-for-multiple-code-blocks/"
title: "CSS Copy Button Reusable Class for Multiple Code Blocks"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "The last bug everyone hits: three copy buttons, and every one of them copies the first block."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Copy Button Reusable Class for Multiple Code Blocks
Source: https://codefronts.com/snippets/css-copy-button/css-copy-button-reusable-class-for-multiple-code-blocks/

The last bug everyone hits: three copy buttons, and every one of them copies the first block. The fix is not three handlers &mdash; it is one delegated listener that finds the pressed button with closest() and reads that button's own target from a data-* attribute. Add a fourth row and it works with no new JavaScript.
## HTML
```html
<div class="cpy-20">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-20__sr" type="checkbox" id="cpy-20-dark">
  <label class="cpy-20__theme" for="cpy-20-dark" title="Switch light or dark theme">
    <svg class="cpy-20__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-20__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-20__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-20__stage">
    <div class="cpy-20__wrap">
      <p class="cpy-20__eyebrow">One handler &middot; four buttons</p>
      <h2 class="cpy-20__title">Reusable, not repeated</h2>
      <p class="cpy-20__lead">Every button below is served by a single delegated listener. Each reads its own target from <code>data-copy-target</code>, so no button can copy its neighbour&rsquo;s value.</p>

      <div class="cpy-20__list" id="cpy-20-list">
        <div class="cpy-20__block">
          <span class="cpy-20__tag">npm</span>
          <code class="cpy-20__code" id="cpy-20-npm">npm i @codefronts/clipboard</code>
          <button class="cpy-20__btn" type="button" data-state="idle" data-copy-target="#cpy-20-npm" data-copy-label="npm command" aria-label="Copy npm command">
            <span class="cpy-20__icons"><svg class="cpy-20__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><svg class="cpy-20__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </button>
        </div>
        <div class="cpy-20__block">
          <span class="cpy-20__tag">pnpm</span>
          <code class="cpy-20__code" id="cpy-20-pnpm">pnpm add @codefronts/clipboard</code>
          <button class="cpy-20__btn" type="button" data-state="idle" data-copy-target="#cpy-20-pnpm" data-copy-label="pnpm command" aria-label="Copy pnpm command">
            <span class="cpy-20__icons"><svg class="cpy-20__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><svg class="cpy-20__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </button>
        </div>
        <div class="cpy-20__block">
          <span class="cpy-20__tag">yarn</span>
          <code class="cpy-20__code" id="cpy-20-yarn">yarn add @codefronts/clipboard</code>
          <button class="cpy-20__btn" type="button" data-state="idle" data-copy-target="#cpy-20-yarn" data-copy-label="yarn command" aria-label="Copy yarn command">
            <span class="cpy-20__icons"><svg class="cpy-20__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><svg class="cpy-20__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </button>
        </div>
        <div class="cpy-20__block">
          <span class="cpy-20__tag">deno</span>
          <code class="cpy-20__code" id="cpy-20-deno">deno add npm:@codefronts/clipboard</code>
          <button class="cpy-20__btn" type="button" data-state="idle" data-copy-target="#cpy-20-deno" data-copy-label="deno command" aria-label="Copy deno command">
            <span class="cpy-20__icons"><svg class="cpy-20__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><svg class="cpy-20__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          </button>
        </div>
      </div>

      <p class="cpy-20__live" role="status" aria-live="polite"></p>
      <p class="cpy-20__note">Listeners bound: <strong>1</strong> &middot; buttons served: <strong id="cpy-20-count">4</strong>. Add a fifth row and the count changes; the JavaScript does not.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-20 {
  --bg: #f7f7f9;
  --panel: #ffffff;
  --panel2: #f0f1f5;
  --ink: #0b0d14;
  --muted: #5a5f6c;
  --line: rgba(11,13,20,.12);
  --accent: #4f46e5;
  --ok: #15803d;
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

.cpy-20 *,
.cpy-20 *::before,
.cpy-20 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-20 {
    --accent: oklch(.53 .21 274);
    --ok: oklch(.55 .15 149);
  }
}

.cpy-20__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-20__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-20__theme {
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

.cpy-20__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-20__moon {
  display: none;
}

.cpy-20__sr:focus-visible + .cpy-20__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-20__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-20__wrap {
  inline-size: min(100%,38rem);
  display: grid;
  gap: .8rem;
}

.cpy-20__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-20__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.95rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-20__lead {
  margin: 0 0 .3rem;
  font-size: .94rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-20__lead code {
  font-family: var(--mono);
  font-size: .8rem;
  padding: .1rem .3rem;
  border-radius: .3rem;
  background: var(--panel2);
}

.cpy-20__list {
  display: grid;
  gap: .5rem;
}

.cpy-20__block {
  display: grid;
  grid-template-columns: 3.6rem minmax(0,1fr) auto;
  align-items: center;
  gap: .8rem;
  padding: .6rem .6rem .6rem .9rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--panel);
  transition: border-color var(--dur),background var(--dur);
}

.cpy-20__block:hover {
  background: var(--panel2);
}

.cpy-20__block:has([data-state="copied"]) {
  border-color: color-mix(in srgb,var(--ok) 42%,transparent);
}

.cpy-20__tag {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-20__code {
  font-family: var(--mono);
  font-size: clamp(.76rem,1.6vw,.86rem);
  white-space: nowrap;
  overflow-x: auto;
  scrollbar-width: none;
}

.cpy-20__code::-webkit-scrollbar {
  display: none;
}

.cpy-20__btn {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  padding: 0;
  border: 1px solid transparent;
  border-radius: .7rem;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background var(--dur),color var(--dur),border-color var(--dur),scale var(--dur);
}

.cpy-20__btn:hover {
  background: var(--panel);
  border-color: var(--line);
  color: var(--ink);
}

.cpy-20__btn:active {
  scale: .94;
}

.cpy-20__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpy-20__btn[data-state="copied"] {
  color: var(--ok);
}

.cpy-20__icons {
  position: relative;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  pointer-events: none;
}

.cpy-20__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-20__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-20__btn[data-state="copied"] .cpy-20__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-20__btn[data-state="copied"] .cpy-20__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-20__live {
  margin: 0;
  min-block-size: 1.25rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

.cpy-20__note {
  margin: 0;
  font-size: .84rem;
  line-height: 1.6;
  color: var(--muted);
}

.cpy-20__note strong {
  font-family: var(--mono);
  color: var(--accent);
}

@media (max-width: 28rem) {
  .cpy-20__block {
    grid-template-columns: minmax(0,1fr) auto;
  }

  .cpy-20__tag {
    grid-column: 1/-1;
  }
}

@media not (prefers-color-scheme: dark) {
  .cpy-20:has(#cpy-20-dark:checked) {
    --bg: #07080e;
    --panel: #0d1016;
    --panel2: #161922;
    --ink: #e9eaf2;
    --muted: rgba(233,234,242,.6);
    --line: rgba(233,234,242,.14);
    --accent: #a5b4fc;
    --ok: #6ee7a8;
  }

  .cpy-20:has(#cpy-20-dark:checked) .cpy-20__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-20:has(#cpy-20-dark:checked) .cpy-20__sun {
    display: none;
  }

  .cpy-20:has(#cpy-20-dark:checked) .cpy-20__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-20:not([data-theme="light"]):not(:has(#cpy-20-dark:checked)) {
    --bg: #07080e;
    --panel: #0d1016;
    --panel2: #161922;
    --ink: #e9eaf2;
    --muted: rgba(233,234,242,.6);
    --line: rgba(233,234,242,.14);
    --accent: #a5b4fc;
    --ok: #6ee7a8;
  }

  .cpy-20__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-20__sun {
    display: none;
  }

  .cpy-20__moon {
    display: block;
  }

  .cpy-20:has(#cpy-20-dark:checked) .cpy-20__sun {
    display: block;
  }

  .cpy-20:has(#cpy-20-dark:checked) .cpy-20__moon {
    display: none;
  }
}

.cpy-20[data-theme="dark"] {
  --bg: #07080e;
  --panel: #0d1016;
  --panel2: #161922;
  --ink: #e9eaf2;
  --muted: rgba(233,234,242,.6);
  --line: rgba(233,234,242,.14);
  --accent: #a5b4fc;
  --ok: #6ee7a8;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-20 *,
    .cpy-20 *::before,
    .cpy-20 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-20__wrap,
    .cpy-20__block,
    .cpy-20__btn,
    .cpy-20__theme {
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
const cpy20 = document.querySelector('.cpy-20');
if (cpy20) {
  const list = cpy20.querySelector('#cpy-20-list');
  const live = cpy20.querySelector('.cpy-20__live');
  const timers = new WeakMap();                       // independent countdown per button
  cpy20.querySelector('#cpy-20-count').textContent = list.querySelectorAll('.cpy-20__btn').length;
  const legacy = (text) => {                          // keeps insecure origins working
    const ta = document.createElement('textarea');
    ta.value = text; ta.style.cssText = 'position:fixed;top:0;left:-9999px;opacity:0';
    document.body.append(ta); ta.select();
    let ok = false;
    try { ok = document.execCommand('copy'); } catch { ok = false; }
    ta.remove();
    return ok;
  };
  list.addEventListener('click', async (event) => {
    const btn = event.target.closest('.cpy-20__btn');  // the icon is often the target
    if (!btn) return;
    const target = cpy20.querySelector(btn.dataset.copyTarget);
    const text = target.textContent.trim();
    let ok = true;
    try { await navigator.clipboard.writeText(text); } catch { ok = legacy(text); }
    btn.dataset.state = ok ? 'copied' : 'idle';
    live.textContent = (ok ? 'Copied ' : 'Could not copy ') + btn.dataset.copyLabel + ': ' + text;
    clearTimeout(timers.get(btn));
    timers.set(btn, setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, 2000));
  });
}
```
