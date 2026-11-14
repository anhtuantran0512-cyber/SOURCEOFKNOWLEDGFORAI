---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-copy-button-inside-input-text-field/"
title: "CSS Copy Button Inside Input Text Field"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "A copy control that lives inside the field's border, on the trailing edge, the way Stripe and Linear do it."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Copy Button Inside Input Text Field
Source: https://codefronts.com/snippets/css-copy-button/css-copy-button-inside-input-text-field/

A copy control that lives inside the field's border, on the trailing edge, the way Stripe and Linear do it. The input keeps its own focus ring, the button never covers the text because the field reserves padding for it, and what gets copied is the live value &mdash; type something and the button copies what you typed, not a hardcoded string.
## HTML
```html
<div class="cpy-07">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-07__sr" type="checkbox" id="cpy-07-dark">
  <label class="cpy-07__theme" for="cpy-07-dark" title="Switch light or dark theme">
    <svg class="cpy-07__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-07__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-07__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-07__stage">
    <div class="cpy-07__card">
      <p class="cpy-07__eyebrow">Trailing action &middot; inside the border</p>
      <h2 class="cpy-07__title">Copy what is in the field</h2>
      <p class="cpy-07__lead">Edit the value &mdash; the button copies whatever is there when you press it. Empty field, disabled button.</p>

      <label class="cpy-07__label" for="cpy-07-input">Webhook endpoint</label>
      <div class="cpy-07__shell">
        <input class="cpy-07__input" id="cpy-07-input" type="text" value="https://api.codefronts.com/hooks/v2/ae91f3" spellcheck="false" autocomplete="off">
        <button class="cpy-07__btn" type="button" data-state="idle" aria-label="Copy webhook endpoint">
          <span class="cpy-07__icons">
            <svg class="cpy-07__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-07__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
        </button>
      </div>
      <p class="cpy-07__help" id="cpy-07-help">Send events here. Rotate the path if it leaks.</p>
      <p class="cpy-07__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-07 {
  --bg: #f7f8fa;
  --panel: #ffffff;
  --panel2: #f1f3f7;
  --ink: #0b1020;
  --muted: #5b6474;
  --line: rgba(11,16,32,.13);
  --accent: #2563eb;
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

.cpy-07 *,
.cpy-07 *::before,
.cpy-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-07 {
    --accent: oklch(.55 .21 262);
    --ok: oklch(.55 .15 149);
  }
}

.cpy-07__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-07__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-07__theme {
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

.cpy-07__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-07__moon {
  display: none;
}

.cpy-07__sr:focus-visible + .cpy-07__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-07__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-07__card {
  inline-size: min(100%,33rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .55rem;
  box-shadow: 0 1px 2px rgba(11,16,32,.05),0 26px 50px -34px rgba(11,16,32,.32);
}

.cpy-07__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-07__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-07__lead {
  margin: 0 0 .8rem;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-07__label {
  font-size: .82rem;
  font-weight: 560;
  color: var(--muted);
}

.cpy-07__shell {
  position: relative;
  display: block;
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--panel);
  transition: border-color var(--dur),box-shadow var(--dur);
}

.cpy-07__shell:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in srgb,var(--accent) 18%,transparent);
}

.cpy-07__input {
  inline-size: 100%;
  padding: .9rem 1rem;
  padding-inline-end: calc(2.5rem + 1rem);
  border: 0;
  border-radius: inherit;
  background: transparent;
  color: var(--ink);
  font-family: var(--mono);
  font-size: .88rem;
  outline: none;
  text-overflow: ellipsis;
}

.cpy-07__btn {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-end: .35rem;
  translate: 0 -50%;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding: 0;
  border: 0;
  border-radius: .65rem;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background var(--dur),color var(--dur),scale var(--dur);
}

.cpy-07__btn::before {
  content: "";
  position: absolute;
  inset-inline-start: -.35rem;
  inset-block: .45rem;
  inline-size: 1px;
  background: var(--line);
}

.cpy-07__btn:hover {
  background: var(--panel2);
  color: var(--ink);
}

.cpy-07__btn:active {
  scale: .93;
}

.cpy-07__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.cpy-07__btn:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.cpy-07__btn[data-state="copied"] {
  color: var(--ok);
}

.cpy-07__icons {
  position: relative;
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.cpy-07__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-07__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-07__btn[data-state="copied"] .cpy-07__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-07__btn[data-state="copied"] .cpy-07__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-07__help {
  margin: .45rem 0 0;
  font-size: .82rem;
  line-height: 1.5;
  color: var(--muted);
}

.cpy-07__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

@media not (prefers-color-scheme: dark) {
  .cpy-07:has(#cpy-07-dark:checked) {
    --bg: #070910;
    --panel: #0d1119;
    --panel2: #161b25;
    --ink: #e9edf5;
    --muted: rgba(233,237,245,.6);
    --line: rgba(233,237,245,.15);
    --accent: #93c5fd;
    --ok: #6ee7a8;
  }

  .cpy-07:has(#cpy-07-dark:checked) .cpy-07__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-07:has(#cpy-07-dark:checked) .cpy-07__sun {
    display: none;
  }

  .cpy-07:has(#cpy-07-dark:checked) .cpy-07__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-07:not([data-theme="light"]):not(:has(#cpy-07-dark:checked)) {
    --bg: #070910;
    --panel: #0d1119;
    --panel2: #161b25;
    --ink: #e9edf5;
    --muted: rgba(233,237,245,.6);
    --line: rgba(233,237,245,.15);
    --accent: #93c5fd;
    --ok: #6ee7a8;
  }

  .cpy-07__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-07__sun {
    display: none;
  }

  .cpy-07__moon {
    display: block;
  }

  .cpy-07:has(#cpy-07-dark:checked) .cpy-07__sun {
    display: block;
  }

  .cpy-07:has(#cpy-07-dark:checked) .cpy-07__moon {
    display: none;
  }
}

.cpy-07[data-theme="dark"] {
  --bg: #070910;
  --panel: #0d1119;
  --panel2: #161b25;
  --ink: #e9edf5;
  --muted: rgba(233,237,245,.6);
  --line: rgba(233,237,245,.15);
  --accent: #93c5fd;
  --ok: #6ee7a8;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-07 *,
    .cpy-07 *::before,
    .cpy-07 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-07__card,
    .cpy-07__shell,
    .cpy-07__btn,
    .cpy-07__theme {
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
const cpy07 = document.querySelector('.cpy-07');
if (cpy07) {
  const input = cpy07.querySelector('.cpy-07__input');
  const btn = cpy07.querySelector('.cpy-07__btn');
  const live = cpy07.querySelector('.cpy-07__live');
  let timer;
  const sync = () => { btn.disabled = input.value.trim() === ''; };
  input.addEventListener('input', sync);
  sync();
  btn.addEventListener('click', async () => {
    const text = input.value.trim();               // live value, never a cached one
    if (!text) return;
    let ok = true;
    try { await navigator.clipboard.writeText(text); } catch { ok = false; }
    btn.dataset.state = ok ? 'copied' : 'idle';
    live.textContent = ok ? 'Endpoint copied (' + text.length + ' characters)' : 'Clipboard blocked - press Ctrl C';
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, 2000);
  });
}
```
