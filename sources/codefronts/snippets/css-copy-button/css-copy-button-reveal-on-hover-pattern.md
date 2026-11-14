---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-copy-button-reveal-on-hover-pattern/"
title: "CSS Copy Button Reveal on Hover Pattern"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "The pattern that keeps a docs page calm: the copy button is invisible until you approach the block, then fades and slides into place in 180&nbsp;ms."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Copy Button Reveal on Hover Pattern
Source: https://codefronts.com/snippets/css-copy-button/css-copy-button-reveal-on-hover-pattern/

The pattern that keeps a docs page calm: the copy button is invisible until you approach the block, then fades and slides into place in 180&nbsp;ms. The part almost every implementation gets wrong is the keyboard &mdash; a hover-only reveal is a button a keyboard user can focus but never see. Here :focus-within reveals it too, and touch devices get it permanently.
## HTML
```html
<div class="cpy-09">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-09__sr" type="checkbox" id="cpy-09-dark">
  <label class="cpy-09__theme" for="cpy-09-dark" title="Switch light or dark theme">
    <svg class="cpy-09__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-09__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-09__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-09__stage">
    <div class="cpy-09__wrap">
      <p class="cpy-09__eyebrow">Reveal &middot; hover and focus-within</p>
      <h2 class="cpy-09__title">Quiet until you need it</h2>
      <p class="cpy-09__lead">Hover the block below &mdash; or press <kbd class="cpy-09__kbd">Tab</kbd>, which reveals it exactly the same way.</p>

      <div class="cpy-09__block">
        <button class="cpy-09__btn" type="button" data-state="idle" aria-label="Copy configuration to clipboard">
          <span class="cpy-09__icons">
            <svg class="cpy-09__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-09__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <span class="cpy-09__label">Copy</span>
        </button>
        <pre class="cpy-09__pre"><code id="cpy-09-code">{
  "theme": "codefronts-dark",
  "copyButton": { "reveal": "hover", "focusWithin": true }
}</code></pre>
      </div>

      <div class="cpy-09__rules">
        <p><span>Pointer</span>reveals on <code>:hover</code></p>
        <p><span>Keyboard</span>reveals on <code>:focus-within</code></p>
        <p><span>Touch</span>always visible via <code>@media (hover:none)</code></p>
      </div>
      <p class="cpy-09__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-09 {
  --bg: #f6f7f8;
  --panel: #ffffff;
  --code: #101418;
  --code-ink: #dde3ea;
  --ink: #0b0e12;
  --muted: #5a626d;
  --line: rgba(11,14,18,.11);
  --accent: #0ea5e9;
  --ok: #34d399;
  --dur: 180ms;
  --off: .65rem;
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

.cpy-09 *,
.cpy-09 *::before,
.cpy-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-09 {
    --accent: oklch(.7 .14 232);
    --ok: oklch(.78 .15 162);
  }
}

.cpy-09__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-09__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-09__theme {
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

.cpy-09__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-09__moon {
  display: none;
}

.cpy-09__sr:focus-visible + .cpy-09__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-09__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-09__wrap {
  inline-size: min(100%,40rem);
  min-inline-size: 0;
  display: grid;
  gap: .8rem;
}
/* Same min-width:auto guard as demo 06. */

.cpy-09__wrap > * {
  min-inline-size: 0;
}

.cpy-09__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-09__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.95rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-09__lead {
  margin: 0 0 .3rem;
  font-size: .95rem;
  line-height: 1.6;
  color: var(--muted);
}

.cpy-09__kbd {
  font-family: var(--mono);
  font-size: .74rem;
  padding: .12rem .38rem;
  border: 1px solid var(--line);
  border-block-end-width: 2px;
  border-radius: .35rem;
  background: var(--panel);
  color: var(--ink);
}

.cpy-09__block {
  position: relative;
  border-radius: 1.1rem;
  background: var(--code);
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 24px 46px -32px rgba(11,14,18,.5);
}

.cpy-09__pre {
  margin: 0;
  padding: 1.2rem 1.25rem;
  padding-inline-end: calc(6rem + var(--off));
  overflow-x: auto;
  border-radius: inherit;
}

.cpy-09__pre code {
  font-family: var(--mono);
  font-size: clamp(.76rem,1.5vw,.87rem);
  line-height: 1.8;
  color: var(--code-ink);
  white-space: pre;
}

.cpy-09__btn {
  position: absolute;
  inset-block-start: var(--off);
  inset-inline-end: var(--off);
  z-index: 2;
  min-block-size: 2.4rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding-inline: .7rem;
  border: 1px solid rgba(255,255,255,.16);
  border-radius: .65rem;
  background: rgba(255,255,255,.09);
  color: var(--code-ink);
  font: inherit;
  font-size: .8rem;
  font-weight: 540;
  cursor: pointer;
  opacity: 0;
  visibility: hidden;
  translate: 0 -.3rem;
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  transition: opacity var(--dur) ease,translate var(--dur) ease,background var(--dur),color var(--dur),visibility var(--dur) allow-discrete;
}

.cpy-09__block:hover .cpy-09__btn,
.cpy-09__block:focus-within .cpy-09__btn {
  opacity: 1;
  visibility: visible;
  translate: 0 0;
}

.cpy-09__btn:hover {
  background: rgba(255,255,255,.16);
}

.cpy-09__btn:focus-visible {
  outline: 2px solid var(--ok);
  outline-offset: 2px;
}

.cpy-09__btn[data-state="copied"] {
  color: var(--ok);
  border-color: color-mix(in srgb,var(--ok) 45%,transparent);
}

.cpy-09__icons {
  position: relative;
  inline-size: 1rem;
  block-size: 1rem;
  flex: none;
}

.cpy-09__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-09__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-09__btn[data-state="copied"] .cpy-09__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-09__btn[data-state="copied"] .cpy-09__i2 {
  opacity: 1;
  scale: 1;
}

@media (hover: none) {
  .cpy-09__btn {
    opacity: 1;
    visibility: visible;
    translate: 0 0;
  }
}

.cpy-09__rules {
  display: grid;
  gap: .4rem;
  margin-block-start: .3rem;
}

.cpy-09__rules p {
  display: grid;
  grid-template-columns: 5.5rem 1fr;
  gap: .75rem;
  margin: 0;
  font-size: .86rem;
  color: var(--muted);
}

.cpy-09__rules span {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--accent);
}

.cpy-09__rules code {
  font-family: var(--mono);
  font-size: .78rem;
}

.cpy-09__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--accent);
}

@media not (prefers-color-scheme: dark) {
  .cpy-09:has(#cpy-09-dark:checked) {
    --bg: #07090b;
    --panel: #0d1114;
    --code: #12161b;
    --ink: #e8ecf2;
    --muted: rgba(232,236,242,.62);
    --line: rgba(232,236,242,.14);
    --accent: #7dd3fc;
  }

  .cpy-09:has(#cpy-09-dark:checked) .cpy-09__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-09:has(#cpy-09-dark:checked) .cpy-09__sun {
    display: none;
  }

  .cpy-09:has(#cpy-09-dark:checked) .cpy-09__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-09:not([data-theme="light"]):not(:has(#cpy-09-dark:checked)) {
    --bg: #07090b;
    --panel: #0d1114;
    --code: #12161b;
    --ink: #e8ecf2;
    --muted: rgba(232,236,242,.62);
    --line: rgba(232,236,242,.14);
    --accent: #7dd3fc;
  }

  .cpy-09__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-09__sun {
    display: none;
  }

  .cpy-09__moon {
    display: block;
  }

  .cpy-09:has(#cpy-09-dark:checked) .cpy-09__sun {
    display: block;
  }

  .cpy-09:has(#cpy-09-dark:checked) .cpy-09__moon {
    display: none;
  }
}

.cpy-09[data-theme="dark"] {
  --bg: #07090b;
  --panel: #0d1114;
  --code: #12161b;
  --ink: #e8ecf2;
  --muted: rgba(232,236,242,.62);
  --line: rgba(232,236,242,.14);
  --accent: #7dd3fc;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-09 *,
    .cpy-09 *::before,
    .cpy-09 *::after {
    transition: none !important;
    animation: none !important;
  }

  .cpy-09__btn {
    translate: 0 0;
  }
}

@media (forced-colors: active) {
  .cpy-09__block,
    .cpy-09__btn,
    .cpy-09__theme {
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
const cpy09 = document.querySelector('.cpy-09');
if (cpy09) {
  const btn = cpy09.querySelector('.cpy-09__btn');
  const code = cpy09.querySelector('#cpy-09-code');
  const live = cpy09.querySelector('.cpy-09__live');
  const label = cpy09.querySelector('.cpy-09__label');
  let timer;
  btn.addEventListener('click', async () => {
    let ok = true;
    try { await navigator.clipboard.writeText(code.textContent); } catch { ok = false; }
    btn.dataset.state = ok ? 'copied' : 'idle';
    label.textContent = ok ? 'Copied' : 'Blocked';
    live.textContent = ok ? 'Configuration copied' : 'Clipboard blocked - press Ctrl C';
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; label.textContent = 'Copy'; live.textContent = ''; }, 2000);
  });
}
```
