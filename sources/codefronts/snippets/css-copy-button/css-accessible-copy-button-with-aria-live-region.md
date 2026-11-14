---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-accessible-copy-button-with-aria-live-region/"
title: "CSS Accessible Copy Button with ARIA Live Region"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "A copy button that a screen reader user can actually use: aria-label on the icon-only control, a polite live region that announces Copied to clipboard, a…"
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Accessible Copy Button with ARIA Live Region
Source: https://codefronts.com/snippets/css-copy-button/css-accessible-copy-button-with-aria-live-region/

A copy button that a screen reader user can actually use: aria-label on the icon-only control, a polite live region that announces Copied to clipboard, a 2&nbsp;px focus ring you cannot miss, and a 44&nbsp;&times;&nbsp;44&nbsp;px target. The panel beside it transcribes every announcement as it happens, so you can see exactly what assistive tech hears.
## HTML
```html
<div class="cpy-19">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-19__sr" type="checkbox" id="cpy-19-dark">
  <label class="cpy-19__theme" for="cpy-19-dark" title="Switch light or dark theme">
    <svg class="cpy-19__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-19__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-19__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-19__stage">
    <div class="cpy-19__card">
      <p class="cpy-19__eyebrow">WCAG 2.2 AA &middot; announced, not just shown</p>
      <h2 class="cpy-19__title">What the screen reader hears</h2>

      <div class="cpy-19__panel">
        <div class="cpy-19__pair">
          <span class="cpy-19__key">Account number</span>
          <code class="cpy-19__value" id="cpy-19-value">4471 8829 0416</code>
        </div>
        <button class="cpy-19__btn" type="button" data-state="idle" aria-label="Copy account number 4471 8829 0416">
          <span class="cpy-19__icons">
            <svg class="cpy-19__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-19__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
        </button>
      </div>

      <p class="cpy-19__live" role="status" aria-live="polite"></p>
      <p class="cpy-19__alert" role="alert"></p>

      <section class="cpy-19__log" aria-label="Announcement transcript">
        <h3 class="cpy-19__lh">Announcement transcript</h3>
        <ol class="cpy-19__list" id="cpy-19-list">
          <li class="cpy-19__empty">Nothing announced yet &mdash; press the button, or Tab to it and press Enter.</li>
        </ol>
      </section>

      <ul class="cpy-19__checks">
        <li><strong>44 &times; 44</strong>hit area, 20&nbsp;px glyph</li>
        <li><strong>2px</strong>focus-visible ring, offset 3&nbsp;px</li>
        <li><strong>polite</strong>status for success, alert for failure</li>
        <li><strong>label</strong>names the value, not just the verb</li>
      </ul>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-19 {
  --bg: #f6f7fa;
  --panel: #ffffff;
  --panel2: #eff1f6;
  --ink: #0a0d16;
  --muted: #585f6d;
  --line: rgba(10,13,22,.12);
  --accent: #1d4ed8;
  --ok: #15803d;
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

.cpy-19 *,
.cpy-19 *::before,
.cpy-19 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-19 {
    --accent: oklch(.48 .22 264);
    --ok: oklch(.55 .15 149);
    --err: oklch(.58 .21 25);
  }
}

.cpy-19__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-19__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-19__theme {
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

.cpy-19__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-19__moon {
  display: none;
}

.cpy-19__sr:focus-visible + .cpy-19__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-19__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-19__card {
  inline-size: min(100%,35rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .8rem;
  box-shadow: 0 1px 2px rgba(10,13,22,.05),0 28px 55px -36px rgba(10,13,22,.34);
}

.cpy-19__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-19__title {
  margin: 0 0 .3rem;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-19__panel {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1rem 1.05rem;
  border: 1px solid var(--line);
  border-radius: 1.1rem;
  background: var(--panel2);
}

.cpy-19__pair {
  display: grid;
  gap: .2rem;
}

.cpy-19__key {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-19__value {
  font-family: var(--mono);
  font-size: clamp(1rem,2.6vw,1.25rem);
  letter-spacing: .04em;
}

.cpy-19__btn {
  flex: none;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  padding: 0;
  border: 1px solid var(--line);
  border-radius: .75rem;
  background: var(--panel);
  color: var(--ink);
  cursor: pointer;
  transition: background var(--dur),color var(--dur),border-color var(--dur),scale var(--dur);
}

.cpy-19__btn:hover {
  background: color-mix(in srgb,var(--accent) 8%,var(--panel));
}

.cpy-19__btn:active {
  scale: .94;
}

.cpy-19__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-19__btn[data-state="copied"] {
  color: var(--ok);
  border-color: color-mix(in srgb,var(--ok) 42%,transparent);
}

.cpy-19__icons {
  position: relative;
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.cpy-19__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-19__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-19__btn[data-state="copied"] .cpy-19__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-19__btn[data-state="copied"] .cpy-19__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-19__live {
  margin: 0;
  min-block-size: 1.25rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

.cpy-19__alert {
  margin: 0;
  min-block-size: 1.1rem;
  font-size: .83rem;
  font-weight: 540;
  color: var(--err);
}

.cpy-19__log {
  padding: 1rem 1.1rem;
  border: 1px dashed var(--line);
  border-radius: 1rem;
  background: color-mix(in srgb,var(--accent) 4%,transparent);
}

.cpy-19__lh {
  margin: 0 0 .5rem;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
}

.cpy-19__list {
  margin: 0;
  padding: 0 0 0 1.1rem;
  display: grid;
  gap: .3rem;
}

.cpy-19__list li {
  font-family: var(--mono);
  font-size: .78rem;
  line-height: 1.55;
  color: var(--ink);
}

.cpy-19__empty {
  list-style: none;
  margin-inline-start: -1.1rem;
  color: var(--muted) !important;
}

.cpy-19__checks {
  list-style: none;
  margin: .2rem 0 0;
  padding: 0;
  display: grid;
  gap: .35rem;
}

.cpy-19__checks li {
  display: grid;
  grid-template-columns: 5.5rem 1fr;
  gap: .75rem;
  font-size: .84rem;
  color: var(--muted);
  align-items: baseline;
}

.cpy-19__checks strong {
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--accent);
}

@media not (prefers-color-scheme: dark) {
  .cpy-19:has(#cpy-19-dark:checked) {
    --bg: #06080f;
    --panel: #0c1017;
    --panel2: #151924;
    --ink: #e8ebf3;
    --muted: rgba(232,235,243,.6);
    --line: rgba(232,235,243,.15);
    --accent: #93c5fd;
    --ok: #6ee7a8;
    --err: #fda4af;
  }

  .cpy-19:has(#cpy-19-dark:checked) .cpy-19__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-19:has(#cpy-19-dark:checked) .cpy-19__sun {
    display: none;
  }

  .cpy-19:has(#cpy-19-dark:checked) .cpy-19__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-19:not([data-theme="light"]):not(:has(#cpy-19-dark:checked)) {
    --bg: #06080f;
    --panel: #0c1017;
    --panel2: #151924;
    --ink: #e8ebf3;
    --muted: rgba(232,235,243,.6);
    --line: rgba(232,235,243,.15);
    --accent: #93c5fd;
    --ok: #6ee7a8;
    --err: #fda4af;
  }

  .cpy-19__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-19__sun {
    display: none;
  }

  .cpy-19__moon {
    display: block;
  }

  .cpy-19:has(#cpy-19-dark:checked) .cpy-19__sun {
    display: block;
  }

  .cpy-19:has(#cpy-19-dark:checked) .cpy-19__moon {
    display: none;
  }
}

.cpy-19[data-theme="dark"] {
  --bg: #06080f;
  --panel: #0c1017;
  --panel2: #151924;
  --ink: #e8ebf3;
  --muted: rgba(232,235,243,.6);
  --line: rgba(232,235,243,.15);
  --accent: #93c5fd;
  --ok: #6ee7a8;
  --err: #fda4af;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-19 *,
    .cpy-19 *::before,
    .cpy-19 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-19__card,
    .cpy-19__panel,
    .cpy-19__btn,
    .cpy-19__theme,
    .cpy-19__log {
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
const cpy19 = document.querySelector('.cpy-19');
if (cpy19) {
  const btn = cpy19.querySelector('.cpy-19__btn');
  const value = cpy19.querySelector('#cpy-19-value');
  const live = cpy19.querySelector('.cpy-19__live');      // pre-existing, never injected
  const alertBox = cpy19.querySelector('.cpy-19__alert');
  const list = cpy19.querySelector('#cpy-19-list');
  let timer;
  const log = (role, message) => {
    cpy19.querySelector('.cpy-19__empty')?.remove();
    const li = document.createElement('li');
    li.textContent = new Date().toLocaleTimeString() + '  [' + role + '] ' + message;
    list.append(li);
  };
  btn.addEventListener('click', async () => {
    const text = value.textContent.trim();
    live.textContent = ''; alertBox.textContent = '';     // clear so a repeat re-announces
    let ok = true;
    try { await navigator.clipboard.writeText(text); } catch { ok = false; }
    btn.dataset.state = ok ? 'copied' : 'idle';
    requestAnimationFrame(() => {
      if (ok) { live.textContent = 'Copied to clipboard: ' + text; log('status, polite', 'Copied to clipboard: ' + text); }
      else { alertBox.textContent = 'Copy failed. Select the number and press Control C.'; log('alert, assertive', 'Copy failed. Select the number and press Control C.'); }
    });
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, 2200);
  });
}
```
