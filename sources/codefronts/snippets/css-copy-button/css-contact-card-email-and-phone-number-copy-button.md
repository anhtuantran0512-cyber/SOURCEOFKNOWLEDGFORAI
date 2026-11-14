---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-contact-card-email-and-phone-number-copy-button/"
title: "CSS Contact Card Email & Phone Number Copy Button"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "A compact profile card where the email and the phone number each carry their own copy control, plus the links themselves &mdash; because some people want to…"
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Contact Card Email & Phone Number Copy Button
Source: https://codefronts.com/snippets/css-copy-button/css-contact-card-email-and-phone-number-copy-button/

A compact profile card where the email and the phone number each carry their own copy control, plus the links themselves &mdash; because some people want to copy, and some want mailto:. Two icon buttons, distinct aria-labels, one delegated handler, and a per-row success tick that never disturbs the card's rhythm.
## HTML
```html
<div class="cpy-14">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-14__sr" type="checkbox" id="cpy-14-dark">
  <label class="cpy-14__theme" for="cpy-14-dark" title="Switch light or dark theme">
    <svg class="cpy-14__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-14__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-14__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-14__stage">
    <article class="cpy-14__card">
      <header class="cpy-14__head">
        <img class="cpy-14__avatar" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=facearea&facepad=2.6&w=240&h=240&q=70" alt="Portrait of Alex Chen" width="240" height="240" loading="lazy" decoding="async">
        <div class="cpy-14__who">
          <h2 class="cpy-14__name">Alex Chen</h2>
          <p class="cpy-14__role">Staff Engineer &middot; Platform</p>
        </div>
      </header>

      <ul class="cpy-14__rows">
        <li class="cpy-14__row">
          <svg class="cpy-14__glyph" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="3" y="5.2" width="18" height="13.6" rx="2.6" stroke="currentColor" stroke-width="1.7"/><path d="m3.9 7 7.2 5.2a1.6 1.6 0 0 0 1.8 0L20.1 7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <div class="cpy-14__pair">
            <span class="cpy-14__key">Email</span>
            <a class="cpy-14__value" href="mailto:[email protected]">[email protected]</a>
          </div>
          <button class="cpy-14__copy" type="button" data-state="idle" data-copy="[email protected]" aria-label="Copy email address">
            <span class="cpy-14__icons">
              <svg class="cpy-14__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
              <svg class="cpy-14__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
          </button>
        </li>
        <li class="cpy-14__row">
          <svg class="cpy-14__glyph" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7.2 3.8h2.4l1.5 3.6-1.9 1.4a10.6 10.6 0 0 0 5 5l1.4-1.9 3.6 1.5v2.4a2.4 2.4 0 0 1-2.6 2.4A15.4 15.4 0 0 1 4.8 6.4 2.4 2.4 0 0 1 7.2 3.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <div class="cpy-14__pair">
            <span class="cpy-14__key">Direct line</span>
            <a class="cpy-14__value" href="tel:+14155550148">+1 (415) 555-0148</a>
          </div>
          <button class="cpy-14__copy" type="button" data-state="idle" data-copy="+14155550148" aria-label="Copy phone number">
            <span class="cpy-14__icons">
              <svg class="cpy-14__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
              <svg class="cpy-14__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
          </button>
        </li>
      </ul>

      <p class="cpy-14__live" role="status" aria-live="polite"></p>
      <p class="cpy-14__foot">The link acts, the button copies. Phone numbers copy as <code>+14155550148</code>, not as they are displayed.</p>
    </article>
  </div>
</div>
```
## CSS
```css
.cpy-14 {
  --bg: #f6f7f7;
  --panel: #ffffff;
  --panel2: #f0f2f2;
  --ink: #0b100f;
  --muted: #586261;
  --line: rgba(11,16,15,.12);
  --accent: #0f766e;
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

.cpy-14 *,
.cpy-14 *::before,
.cpy-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-14 {
    --accent: oklch(.52 .11 183);
    --ok: oklch(.55 .15 149);
  }
}

.cpy-14__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-14__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-14__theme {
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

.cpy-14__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-14__moon {
  display: none;
}

.cpy-14__sr:focus-visible + .cpy-14__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-14__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-14__card {
  inline-size: min(100%,32rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.3rem,4vw,2rem);
  display: grid;
  gap: 1rem;
  box-shadow: 0 1px 2px rgba(11,16,15,.05),0 28px 55px -36px rgba(11,16,15,.34);
}

.cpy-14__head {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.cpy-14__avatar {
  inline-size: 3.75rem;
  block-size: 3.75rem;
  border-radius: 999px;
  object-fit: cover;
  background: var(--panel2);
  flex: none;
}

.cpy-14__who {
  display: grid;
  gap: .15rem;
}

.cpy-14__name {
  margin: 0;
  font-size: clamp(1.2rem,3vw,1.45rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-14__role {
  margin: 0;
  font-size: .86rem;
  color: var(--muted);
}

.cpy-14__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .5rem;
}

.cpy-14__row {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .85rem;
  padding: .7rem .75rem .7rem .9rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--panel);
  transition: background var(--dur),border-color var(--dur);
}

.cpy-14__row:hover,
.cpy-14__row:focus-within {
  background: var(--panel2);
}

.cpy-14__row:has([data-state="copied"]) {
  border-color: color-mix(in srgb,var(--ok) 40%,transparent);
}

.cpy-14__glyph {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  color: var(--accent);
}

.cpy-14__pair {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
}

.cpy-14__key {
  font-family: var(--mono);
  font-size: .65rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-14__value {
  font-size: .92rem;
  color: var(--ink);
  text-decoration: none;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  border-block-end: 1px solid transparent;
}

.cpy-14__value:hover {
  border-block-end-color: var(--accent);
  color: var(--accent);
}

.cpy-14__value:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .2rem;
}

.cpy-14__copy {
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

.cpy-14__copy:hover {
  background: var(--panel);
  border-color: var(--line);
  color: var(--ink);
}

.cpy-14__copy:active {
  scale: .94;
}

.cpy-14__copy:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpy-14__copy[data-state="copied"] {
  color: var(--ok);
}

.cpy-14__icons {
  position: relative;
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.cpy-14__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-14__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-14__copy[data-state="copied"] .cpy-14__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-14__copy[data-state="copied"] .cpy-14__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-14__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

.cpy-14__foot {
  margin: 0;
  font-size: .8rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-14__foot code {
  font-family: var(--mono);
  font-size: .75rem;
}

@media not (prefers-color-scheme: dark) {
  .cpy-14:has(#cpy-14-dark:checked) {
    --bg: #060a09;
    --panel: #0c1211;
    --panel2: #151b1a;
    --ink: #e8efed;
    --muted: rgba(232,239,237,.6);
    --line: rgba(232,239,237,.14);
    --accent: #5eead4;
    --ok: #6ee7a8;
  }

  .cpy-14:has(#cpy-14-dark:checked) .cpy-14__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-14:has(#cpy-14-dark:checked) .cpy-14__sun {
    display: none;
  }

  .cpy-14:has(#cpy-14-dark:checked) .cpy-14__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-14:not([data-theme="light"]):not(:has(#cpy-14-dark:checked)) {
    --bg: #060a09;
    --panel: #0c1211;
    --panel2: #151b1a;
    --ink: #e8efed;
    --muted: rgba(232,239,237,.6);
    --line: rgba(232,239,237,.14);
    --accent: #5eead4;
    --ok: #6ee7a8;
  }

  .cpy-14__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-14__sun {
    display: none;
  }

  .cpy-14__moon {
    display: block;
  }

  .cpy-14:has(#cpy-14-dark:checked) .cpy-14__sun {
    display: block;
  }

  .cpy-14:has(#cpy-14-dark:checked) .cpy-14__moon {
    display: none;
  }
}

.cpy-14[data-theme="dark"] {
  --bg: #060a09;
  --panel: #0c1211;
  --panel2: #151b1a;
  --ink: #e8efed;
  --muted: rgba(232,239,237,.6);
  --line: rgba(232,239,237,.14);
  --accent: #5eead4;
  --ok: #6ee7a8;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-14 *,
    .cpy-14 *::before,
    .cpy-14 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-14__card,
    .cpy-14__row,
    .cpy-14__copy,
    .cpy-14__theme {
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
const cpy14 = document.querySelector('.cpy-14');
if (cpy14) {
  const live = cpy14.querySelector('.cpy-14__live');
  const timers = new WeakMap();                       // one timer per button
  cpy14.addEventListener('click', async (event) => {
    const btn = event.target.closest('.cpy-14__copy');
    if (!btn) return;
    const value = btn.dataset.copy;
    let ok = true;
    try { await navigator.clipboard.writeText(value); } catch { ok = false; }
    btn.dataset.state = ok ? 'copied' : 'idle';
    const what = btn.getAttribute('aria-label').replace('Copy ', '');
    live.textContent = ok ? what + ' copied: ' + value : 'Clipboard blocked - select the ' + what + ' and press Ctrl C';
    clearTimeout(timers.get(btn));
    timers.set(btn, setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, 2000));
  });
}
```
