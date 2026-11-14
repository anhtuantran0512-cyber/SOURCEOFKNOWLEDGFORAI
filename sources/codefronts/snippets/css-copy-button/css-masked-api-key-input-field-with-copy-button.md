---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-masked-api-key-input-field-with-copy-button/"
title: "CSS Masked API Key Input Field with Copy Button"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "The real dashboard pattern: a secret shown as sk_live_&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;4a2f, an eye toggle to reveal it, and a copy button…"
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masked API Key Input Field with Copy Button
Source: https://codefronts.com/snippets/css-copy-button/css-masked-api-key-input-field-with-copy-button/

The real dashboard pattern: a secret shown as sk_live_&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;4a2f, an eye toggle to reveal it, and a copy button that always copies the full key &mdash; never the masked display string. The mask is presentation; the value lives in one place and the two controls read from it.
## HTML
```html
<div class="cpy-11">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-11__sr" type="checkbox" id="cpy-11-dark">
  <label class="cpy-11__theme" for="cpy-11-dark" title="Switch light or dark theme">
    <svg class="cpy-11__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-11__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-11__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-11__stage">
    <div class="cpy-11__card">
      <div class="cpy-11__head">
        <p class="cpy-11__eyebrow">API keys</p>
        <span class="cpy-11__env">Live mode</span>
      </div>
      <h2 class="cpy-11__title">Secret key</h2>
      <p class="cpy-11__lead">Reveal it if you must, but the copy button always sends the full 32-character key &mdash; not the dots you can see.</p>

      <div class="cpy-11__shell">
        <input class="cpy-11__field" id="cpy-11-field" type="text" value="sk_live_" readonly spellcheck="false" autocomplete="off" inputmode="none" aria-label="Secret API key, masked">
        <div class="cpy-11__actions">
          <button class="cpy-11__icon" id="cpy-11-toggle" type="button" aria-pressed="false" aria-label="Reveal API key">
            <svg class="cpy-11__eye" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M2.6 12S6 5.9 12 5.9 21.4 12 21.4 12 18 18.1 12 18.1 2.6 12 2.6 12Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="12" cy="12" r="2.9" stroke="currentColor" stroke-width="1.7"/></svg>
            <svg class="cpy-11__eyeoff" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.2 4.2 19.8 19.8M9.6 6.3A9.8 9.8 0 0 1 12 6c6 0 9.4 6 9.4 6a16 16 0 0 1-2.7 3.3M6.2 8.3A15.6 15.6 0 0 0 2.6 12S6 18 12 18a9.7 9.7 0 0 0 3-.45" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          </button>
          <button class="cpy-11__copy" id="cpy-11-copy" type="button" data-state="idle">
            <span class="cpy-11__icons">
              <svg class="cpy-11__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
              <svg class="cpy-11__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <span class="cpy-11__labels"><span class="cpy-11__l1">Copy key</span><span class="cpy-11__l2">Copied</span></span>
          </button>
        </div>
      </div>

      <p class="cpy-11__meta">Created 4 Mar 2027 by Priya Sharma &middot; last used 6 minutes ago</p>
      <p class="cpy-11__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-11 {
  --bg: #f6f7fa;
  --panel: #ffffff;
  --panel2: #f0f2f6;
  --ink: #0a0e18;
  --muted: #59606e;
  --line: rgba(10,14,24,.12);
  --accent: #4f46e5;
  --ok: #15803d;
  --warn: #b45309;
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

.cpy-11 *,
.cpy-11 *::before,
.cpy-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-11 {
    --accent: oklch(.53 .21 274);
    --ok: oklch(.55 .15 149);
    --warn: oklch(.56 .14 62);
  }
}

.cpy-11__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-11__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-11__theme {
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

.cpy-11__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-11__moon {
  display: none;
}

.cpy-11__sr:focus-visible + .cpy-11__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-11__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-11__card {
  inline-size: min(100%,36rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .6rem;
  box-shadow: 0 1px 2px rgba(10,14,24,.05),0 26px 50px -34px rgba(10,14,24,.32);
}

.cpy-11__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.cpy-11__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-11__env {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: .25rem .55rem;
  border-radius: 999px;
  color: var(--warn);
  background: color-mix(in srgb,var(--warn) 12%,transparent);
  border: 1px solid color-mix(in srgb,var(--warn) 30%,transparent);
}

.cpy-11__title {
  margin: 0;
  font-size: clamp(1.35rem,3.2vw,1.75rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-11__lead {
  margin: 0 0 .7rem;
  font-size: .94rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-11__shell {
  display: flex;
  align-items: center;
  gap: .4rem;
  padding: .4rem .4rem .4rem .95rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--panel2);
  transition: border-color var(--dur),box-shadow var(--dur);
}

.cpy-11__shell:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in srgb,var(--accent) 16%,transparent);
}

.cpy-11__field {
  flex: 1 1 8rem;
  min-inline-size: 0;
  padding: .55rem 0;
  border: 0;
  background: transparent;
  color: var(--ink);
  font-family: var(--mono);
  font-size: clamp(.82rem,1.7vw,.95rem);
  letter-spacing: .02em;
  outline: none;
  text-overflow: ellipsis;
}

.cpy-11__actions {
  display: flex;
  align-items: center;
  gap: .35rem;
  flex: none;
}

.cpy-11__icon {
  inline-size: 2.6rem;
  block-size: 2.6rem;
  display: grid;
  place-items: center;
  padding: 0;
  border: 1px solid transparent;
  border-radius: .7rem;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background var(--dur),color var(--dur);
}

.cpy-11__icon svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-11__icon:hover {
  background: var(--panel);
  color: var(--ink);
}

.cpy-11__icon:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.cpy-11__eyeoff {
  display: none;
}

.cpy-11__icon[aria-pressed="true"] {
  color: var(--accent);
}

.cpy-11__icon[aria-pressed="true"] .cpy-11__eye {
  display: none;
}

.cpy-11__icon[aria-pressed="true"] .cpy-11__eyeoff {
  display: block;
}

.cpy-11__copy {
  min-block-size: 2.6rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  padding-inline: .9rem;
  border: 1px solid transparent;
  border-radius: .7rem;
  background: var(--ink);
  color: var(--panel);
  font: inherit;
  font-size: .85rem;
  font-weight: 560;
  cursor: pointer;
  transition: background var(--dur),color var(--dur),scale var(--dur);
}

.cpy-11__copy:active {
  scale: .97;
}

.cpy-11__copy:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpy-11__copy[data-state="copied"] {
  background: var(--ok);
  color: #fff;
}

.cpy-11__icons {
  position: relative;
  inline-size: 1.05rem;
  block-size: 1.05rem;
  flex: none;
}

.cpy-11__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-11__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-11__copy[data-state="copied"] .cpy-11__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-11__copy[data-state="copied"] .cpy-11__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-11__labels {
  display: grid;
}

.cpy-11__labels span {
  grid-area: 1/1;
  transition: opacity var(--dur),translate var(--dur);
}

.cpy-11__l2 {
  opacity: 0;
  translate: 0 .35rem;
}

.cpy-11__copy[data-state="copied"] .cpy-11__l1 {
  opacity: 0;
  translate: 0 -.35rem;
}

.cpy-11__copy[data-state="copied"] .cpy-11__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-11__meta {
  margin: .6rem 0 0;
  font-size: .82rem;
  color: var(--muted);
}

.cpy-11__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

@media (max-width: 26rem) {
  .cpy-11__shell {
    flex-wrap: wrap;
    padding: .7rem;
  }

  .cpy-11__field {
    flex-basis: 100%;
    padding-inline: .3rem;
  }

  .cpy-11__actions {
    inline-size: 100%;
    justify-content: flex-end;
  }
}

@media not (prefers-color-scheme: dark) {
  .cpy-11:has(#cpy-11-dark:checked) {
    --bg: #07080f;
    --panel: #0d1018;
    --panel2: #151924;
    --ink: #e9ebf3;
    --muted: rgba(233,235,243,.6);
    --line: rgba(233,235,243,.14);
    --accent: #a5b4fc;
    --ok: #6ee7a8;
    --warn: #fbbf24;
  }

  .cpy-11:has(#cpy-11-dark:checked) .cpy-11__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-11:has(#cpy-11-dark:checked) .cpy-11__sun {
    display: none;
  }

  .cpy-11:has(#cpy-11-dark:checked) .cpy-11__moon {
    display: block;
  }

  .cpy-11:has(#cpy-11-dark:checked) .cpy-11__copy[data-state="copied"] {
    color: #04231a;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-11:not([data-theme="light"]):not(:has(#cpy-11-dark:checked)) {
    --bg: #07080f;
    --panel: #0d1018;
    --panel2: #151924;
    --ink: #e9ebf3;
    --muted: rgba(233,235,243,.6);
    --line: rgba(233,235,243,.14);
    --accent: #a5b4fc;
    --ok: #6ee7a8;
    --warn: #fbbf24;
  }

  .cpy-11__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-11__sun {
    display: none;
  }

  .cpy-11__moon {
    display: block;
  }

  .cpy-11:has(#cpy-11-dark:checked) .cpy-11__sun {
    display: block;
  }

  .cpy-11:has(#cpy-11-dark:checked) .cpy-11__moon {
    display: none;
  }

  .cpy-11__copy[data-state="copied"] {
    color: #04231a;
  }
}

.cpy-11[data-theme="dark"] {
  --bg: #07080f;
  --panel: #0d1018;
  --panel2: #151924;
  --ink: #e9ebf3;
  --muted: rgba(233,235,243,.6);
  --line: rgba(233,235,243,.14);
  --accent: #a5b4fc;
  --ok: #6ee7a8;
  --warn: #fbbf24;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-11 *,
    .cpy-11 *::before,
    .cpy-11 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-11__card,
    .cpy-11__shell,
    .cpy-11__copy,
    .cpy-11__icon,
    .cpy-11__theme {
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
const cpy11 = document.querySelector('.cpy-11');
if (cpy11) {
  const KEY = 'sk-demo-REDACTED';   // the only place the real value lives
  const mask = (k) => k.slice(0, 8) + '\u2022'.repeat(12) + k.slice(-4);
  const field = cpy11.querySelector('#cpy-11-field');
  const toggle = cpy11.querySelector('#cpy-11-toggle');
  const copy = cpy11.querySelector('#cpy-11-copy');
  const live = cpy11.querySelector('.cpy-11__live');
  let shown = false, timer;
  field.value = mask(KEY);
  toggle.addEventListener('click', () => {
    shown = !shown;
    toggle.setAttribute('aria-pressed', String(shown));
    toggle.setAttribute('aria-label', shown ? 'Hide API key' : 'Reveal API key');
    field.value = shown ? KEY : mask(KEY);
    field.setAttribute('aria-label', shown ? 'Secret API key, revealed' : 'Secret API key, masked');
  });
  copy.addEventListener('click', async () => {
    let ok = true;
    try { await navigator.clipboard.writeText(KEY); } catch { ok = false; }   // full key, never the mask
    copy.dataset.state = ok ? 'copied' : 'idle';
    live.textContent = ok ? 'Full key copied (' + KEY.length + ' characters)' : 'Clipboard blocked - reveal the key and press Ctrl C';
    clearTimeout(timer);
    timer = setTimeout(() => { copy.dataset.state = 'idle'; live.textContent = ''; }, 2200);
  });
}
```
