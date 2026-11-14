---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-web3-wallet-address-copy-button-with-text-truncation/"
title: "CSS Web3 Wallet Address Copy Button with Text Truncation"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "A wallet chip showing 0x71C7&hellip;976F &mdash; truncated by CSS, not by JavaScript &mdash; that copies all 42 characters."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Web3 Wallet Address Copy Button with Text Truncation
Source: https://codefronts.com/snippets/css-copy-button/css-web3-wallet-address-copy-button-with-text-truncation/

A wallet chip showing 0x71C7&hellip;976F &mdash; truncated by CSS, not by JavaScript &mdash; that copies all 42 characters. The full address is in the DOM the whole time, split into a flexible head and a fixed tail so the ellipsis lands in the middle; the clipboard receives the real string, because pasting a shortened address means losing funds.
## HTML
```html
<div class="cpy-15">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-15__sr" type="checkbox" id="cpy-15-dark">
  <label class="cpy-15__theme" for="cpy-15-dark" title="Switch light or dark theme">
    <svg class="cpy-15__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-15__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-15__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-15__stage">
    <div class="cpy-15__card">
      <div class="cpy-15__head">
        <span class="cpy-15__chain"><span class="cpy-15__pip"></span>Ethereum</span>
        <span class="cpy-15__ens">codefronts.eth</span>
      </div>

      <div class="cpy-15__chip">
        <span class="cpy-15__addr" id="cpy-15-addr">
          <span class="cpy-15__start">0x71C7656EC7ab88b098defB751B7401B5f6d</span><span class="cpy-15__tail">8976F</span>
        </span>
        <button class="cpy-15__btn" type="button" data-state="idle" aria-label="Copy full wallet address">
          <span class="cpy-15__icons">
            <svg class="cpy-15__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-15__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
        </button>
      </div>

      <p class="cpy-15__live" role="status" aria-live="polite">Truncation is visual only &mdash; the clipboard gets all 42 characters.</p>
      <div class="cpy-15__split">
        <p><span>Displayed</span><code>0x71C7&hellip;976F</code></p>
        <p><span>Copied</span><code class="cpy-15__full">0x71C7656EC7ab88b098defB751B7401B5f6d8976F</code></p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-15 {
  --bg: #f6f6fa;
  --panel: #ffffff;
  --panel2: #eff0f6;
  --ink: #0a0b14;
  --muted: #5a5d70;
  --line: rgba(10,11,20,.12);
  --accent: #6d28d9;
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

.cpy-15 *,
.cpy-15 *::before,
.cpy-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-15 {
    --accent: oklch(.48 .24 295);
    --ok: oklch(.55 .15 149);
  }
}

.cpy-15__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-15__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-15__theme {
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

.cpy-15__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-15__moon {
  display: none;
}

.cpy-15__sr:focus-visible + .cpy-15__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-15__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-15__card {
  inline-size: min(100%,32rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.3rem,4vw,2rem);
  display: grid;
  gap: .9rem;
  box-shadow: 0 1px 2px rgba(10,11,20,.05),0 28px 55px -36px rgba(10,11,20,.34);
}

.cpy-15__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.cpy-15__chain {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-15__pip {
  inline-size: .45rem;
  block-size: .45rem;
  border-radius: 999px;
  background: var(--accent);
}

.cpy-15__ens {
  font-family: var(--mono);
  font-size: .78rem;
  padding: .25rem .55rem;
  border-radius: 999px;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 10%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 28%,transparent);
}

.cpy-15__chip {
  display: flex;
  align-items: center;
  gap: .5rem;
  min-inline-size: 0;
  padding: .5rem .5rem .5rem 1rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--panel2);
}

.cpy-15__addr {
  display: flex;
  min-inline-size: 0;
  flex: 1 1 auto;
  font-family: var(--mono);
  font-size: clamp(.85rem,2.4vw,1.05rem);
  letter-spacing: .01em;
  user-select: all;
}

.cpy-15__start {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.cpy-15__tail {
  flex: none;
}

.cpy-15__btn {
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

.cpy-15__btn:hover {
  background: color-mix(in srgb,var(--accent) 8%,var(--panel));
}

.cpy-15__btn:active {
  scale: .94;
}

.cpy-15__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpy-15__btn[data-state="copied"] {
  color: var(--ok);
  border-color: color-mix(in srgb,var(--ok) 42%,transparent);
}

.cpy-15__icons {
  position: relative;
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.cpy-15__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-15__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-15__btn[data-state="copied"] .cpy-15__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-15__btn[data-state="copied"] .cpy-15__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-15__live {
  margin: 0;
  min-block-size: 1.25rem;
  font-size: .84rem;
  color: var(--muted);
}

.cpy-15__card:has([data-state="copied"]) .cpy-15__live {
  color: var(--ok);
  font-weight: 540;
}

.cpy-15__split {
  display: grid;
  gap: .35rem;
  padding-block-start: .6rem;
  border-block-start: 1px solid var(--line);
}

.cpy-15__split p {
  display: grid;
  grid-template-columns: 5.5rem 1fr;
  gap: .6rem;
  margin: 0;
  align-items: baseline;
}

.cpy-15__split span {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-15__split code {
  font-family: var(--mono);
  font-size: .76rem;
  word-break: break-all;
  color: var(--ink);
}

.cpy-15__full {
  color: var(--accent);
}

@media not (prefers-color-scheme: dark) {
  .cpy-15:has(#cpy-15-dark:checked) {
    --bg: #08070f;
    --panel: #0e0d17;
    --panel2: #171623;
    --ink: #eae9f3;
    --muted: rgba(234,233,243,.6);
    --line: rgba(234,233,243,.14);
    --accent: #c4b5fd;
    --ok: #6ee7a8;
  }

  .cpy-15:has(#cpy-15-dark:checked) .cpy-15__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-15:has(#cpy-15-dark:checked) .cpy-15__sun {
    display: none;
  }

  .cpy-15:has(#cpy-15-dark:checked) .cpy-15__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-15:not([data-theme="light"]):not(:has(#cpy-15-dark:checked)) {
    --bg: #08070f;
    --panel: #0e0d17;
    --panel2: #171623;
    --ink: #eae9f3;
    --muted: rgba(234,233,243,.6);
    --line: rgba(234,233,243,.14);
    --accent: #c4b5fd;
    --ok: #6ee7a8;
  }

  .cpy-15__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-15__sun {
    display: none;
  }

  .cpy-15__moon {
    display: block;
  }

  .cpy-15:has(#cpy-15-dark:checked) .cpy-15__sun {
    display: block;
  }

  .cpy-15:has(#cpy-15-dark:checked) .cpy-15__moon {
    display: none;
  }
}

.cpy-15[data-theme="dark"] {
  --bg: #08070f;
  --panel: #0e0d17;
  --panel2: #171623;
  --ink: #eae9f3;
  --muted: rgba(234,233,243,.6);
  --line: rgba(234,233,243,.14);
  --accent: #c4b5fd;
  --ok: #6ee7a8;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-15 *,
    .cpy-15 *::before,
    .cpy-15 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-15__card,
    .cpy-15__chip,
    .cpy-15__btn,
    .cpy-15__theme {
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
const cpy15 = document.querySelector('.cpy-15');
if (cpy15) {
  const ADDRESS = '0x71C7656EC7ab88b098defB751B7401B5f6d8976F';  // canonical, EIP-55 casing
  const btn = cpy15.querySelector('.cpy-15__btn');
  const live = cpy15.querySelector('.cpy-15__live');
  const rest = 'Truncation is visual only - the clipboard gets all 42 characters.';
  let timer;
  btn.addEventListener('click', async () => {
    let ok = true;
    try { await navigator.clipboard.writeText(ADDRESS); } catch { ok = false; }  // never the elided text
    btn.dataset.state = ok ? 'copied' : 'idle';
    live.textContent = ok
      ? 'Full address copied - ' + ADDRESS.length + ' characters, ending 8976F'
      : 'Clipboard blocked - the address is selectable, press Ctrl C';
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = rest; }, 2600);
  });
}
```
