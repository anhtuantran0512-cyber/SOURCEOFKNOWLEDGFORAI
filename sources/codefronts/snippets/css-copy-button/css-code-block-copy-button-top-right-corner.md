---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-code-block-copy-button-top-right-corner/"
title: "CSS Code Block Copy Button Top Right Corner"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "Placement, offset and hit area &mdash; the three things that actually decide whether a code-block copy button feels right."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Code Block Copy Button Top Right Corner
Source: https://codefronts.com/snippets/css-copy-button/css-code-block-copy-button-top-right-corner/

Placement, offset and hit area &mdash; the three things that actually decide whether a code-block copy button feels right. The block here is deliberately plain so the button is the subject: it sits in the top-right corner, the <pre> reserves padding so no line ever runs under it, and a toggle draws the invisible 44&nbsp;&times;&nbsp;44&nbsp;px target so you can see the difference between a 32&nbsp;px icon and a real touch target.
## HTML
```html
<div class="cpy-06">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-06__sr" type="checkbox" id="cpy-06-dark">
  <label class="cpy-06__theme" for="cpy-06-dark" title="Switch light or dark theme">
    <svg class="cpy-06__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-06__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-06__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-06__stage">
    <div class="cpy-06__wrap">
      <p class="cpy-06__eyebrow">Placement &middot; top-right corner</p>
      <h2 class="cpy-06__title">The corner button, measured properly</h2>

      <div class="cpy-06__block">
        <button class="cpy-06__btn" type="button" data-state="idle" aria-label="Copy code to clipboard">
          <span class="cpy-06__icons">
            <svg class="cpy-06__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-06__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
        </button>
        <pre class="cpy-06__pre"><code id="cpy-06-code">export const copy = async (text) =&gt; {
  try { await navigator.clipboard.writeText(text); return true; }
  catch { return false; }
};</code></pre>
      </div>

      <div class="cpy-06__tools">
        <input class="cpy-06__sr" type="checkbox" id="cpy-06-guide">
        <label class="cpy-06__toggle" for="cpy-06-guide">Show 44&times;44 hit area</label>
        <p class="cpy-06__live" role="status" aria-live="polite"></p>
      </div>
      <p class="cpy-06__note">The <code>&lt;pre&gt;</code> reserves <code>calc(2.75rem + var(--off) * 2)</code> of end padding, so the last line above never slides under the button.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-06 {
  --bg: #f6f7f9;
  --panel: #ffffff;
  --code: #0f1420;
  --code-ink: #dfe5f2;
  --ink: #0b0f1a;
  --muted: #5b6474;
  --line: rgba(11,15,26,.11);
  --accent: #4f46e5;
  --ok: #34d399;
  --dur: 200ms;
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

.cpy-06 *,
.cpy-06 *::before,
.cpy-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-06 {
    --accent: oklch(.53 .21 274);
    --ok: oklch(.78 .15 162);
  }
}

.cpy-06__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-06__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-06__theme {
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

.cpy-06__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-06__moon {
  display: none;
}

.cpy-06__sr:focus-visible + .cpy-06__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-06__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-06__wrap {
  inline-size: min(100%,42rem);
  min-inline-size: 0;
  display: grid;
  gap: .85rem;
}
/* Grid items default to min-width:auto, so the code block inside forced
   this wrapper past its own 100% and took the document sideways at 390px. */

.cpy-06__wrap > * {
  min-inline-size: 0;
}

.cpy-06__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-06__title {
  margin: 0 0 .3rem;
  font-size: clamp(1.4rem,3.4vw,1.95rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-06__block {
  position: relative;
  border-radius: 1.1rem;
  background: var(--code);
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 24px 46px -32px rgba(11,15,26,.55);
}

.cpy-06__pre {
  margin: 0;
  padding: 1.15rem 1.2rem;
  padding-inline-end: calc(2.75rem + var(--off) * 2);
  overflow-x: auto;
  border-radius: inherit;
}

.cpy-06__pre code {
  font-family: var(--mono);
  font-size: clamp(.76rem,1.5vw,.88rem);
  line-height: 1.75;
  color: var(--code-ink);
  white-space: pre;
}

.cpy-06__btn {
  position: absolute;
  inset-block-start: var(--off);
  inset-inline-end: var(--off);
  z-index: 2;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  padding: 0;
  border: 1px solid rgba(255,255,255,.14);
  border-radius: .7rem;
  background: rgba(255,255,255,.07);
  color: var(--code-ink);
  cursor: pointer;
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  transition: background var(--dur),color var(--dur),border-color var(--dur),scale var(--dur);
}

.cpy-06__btn:hover {
  background: rgba(255,255,255,.14);
}

.cpy-06__btn:active {
  scale: .94;
}

.cpy-06__btn:focus-visible {
  outline: 2px solid var(--ok);
  outline-offset: 2px;
}

.cpy-06__btn[data-state="copied"] {
  color: var(--ok);
  border-color: color-mix(in srgb,var(--ok) 45%,transparent);
}

.cpy-06__icons {
  position: relative;
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.cpy-06__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur),rotate var(--dur);
}

.cpy-06__i2 {
  opacity: 0;
  scale: .5;
  rotate: -20deg;
}

.cpy-06__btn[data-state="copied"] .cpy-06__i1 {
  opacity: 0;
  scale: .5;
  rotate: 16deg;
}

.cpy-06__btn[data-state="copied"] .cpy-06__i2 {
  opacity: 1;
  scale: 1;
  rotate: 0deg;
}

.cpy-06__tools {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem;
}

.cpy-06__toggle {
  min-block-size: 44px;
  display: inline-flex;
  align-items: center;
  padding-inline: .9rem;
  border: 1px solid var(--line);
  border-radius: .7rem;
  background: var(--panel);
  font-family: var(--mono);
  font-size: .78rem;
  cursor: pointer;
  transition: border-color var(--dur),color var(--dur);
}

#cpy-06-guide:checked + .cpy-06__toggle {
  border-color: var(--accent);
  color: var(--accent);
}

#cpy-06-guide:focus-visible + .cpy-06__toggle {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpy-06:has(#cpy-06-guide:checked) .cpy-06__btn {
  outline: 1px dashed color-mix(in srgb,var(--ok) 75%,transparent);
  outline-offset: 0;
}

.cpy-06:has(#cpy-06-guide:checked) .cpy-06__icons {
  outline: 1px dashed color-mix(in srgb,#f97316 80%,transparent);
}

.cpy-06__live {
  margin: 0;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--accent);
}

.cpy-06__note {
  margin: 0;
  font-size: .86rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-06__note code {
  font-family: var(--mono);
  font-size: .77rem;
}

@media (hover: none) {
  .cpy-06__btn {
    background: rgba(255,255,255,.14);
  }
}

@media not (prefers-color-scheme: dark) {
  .cpy-06:has(#cpy-06-dark:checked) {
    --bg: #08090e;
    --panel: #0e1017;
    --code: #12151f;
    --ink: #e9ecf5;
    --muted: rgba(233,236,245,.62);
    --line: rgba(233,236,245,.14);
    --accent: #a5b4fc;
  }

  .cpy-06:has(#cpy-06-dark:checked) .cpy-06__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-06:has(#cpy-06-dark:checked) .cpy-06__sun {
    display: none;
  }

  .cpy-06:has(#cpy-06-dark:checked) .cpy-06__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-06:not([data-theme="light"]):not(:has(#cpy-06-dark:checked)) {
    --bg: #08090e;
    --panel: #0e1017;
    --code: #12151f;
    --ink: #e9ecf5;
    --muted: rgba(233,236,245,.62);
    --line: rgba(233,236,245,.14);
    --accent: #a5b4fc;
  }

  .cpy-06__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-06__sun {
    display: none;
  }

  .cpy-06__moon {
    display: block;
  }

  .cpy-06:has(#cpy-06-dark:checked) .cpy-06__sun {
    display: block;
  }

  .cpy-06:has(#cpy-06-dark:checked) .cpy-06__moon {
    display: none;
  }
}

.cpy-06[data-theme="dark"] {
  --bg: #08090e;
  --panel: #0e1017;
  --code: #12151f;
  --ink: #e9ecf5;
  --muted: rgba(233,236,245,.62);
  --line: rgba(233,236,245,.14);
  --accent: #a5b4fc;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-06 *,
    .cpy-06 *::before,
    .cpy-06 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-06__block,
    .cpy-06__btn,
    .cpy-06__theme,
    .cpy-06__toggle {
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
const cpy06 = document.querySelector('.cpy-06');
if (cpy06) {
  const btn = cpy06.querySelector('.cpy-06__btn');
  const code = cpy06.querySelector('#cpy-06-code');
  const live = cpy06.querySelector('.cpy-06__live');
  let timer;
  btn.addEventListener('click', async () => {
    let ok = true;
    try { await navigator.clipboard.writeText(code.textContent); } catch { ok = false; }
    btn.dataset.state = ok ? 'copied' : 'idle';
    btn.setAttribute('aria-label', ok ? 'Code copied to clipboard' : 'Copy code to clipboard');
    live.textContent = ok ? 'Copied 4 lines' : 'Clipboard blocked - select the code and press Ctrl C';
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; btn.setAttribute('aria-label', 'Copy code to clipboard'); }, 2000);
  });
}
```
