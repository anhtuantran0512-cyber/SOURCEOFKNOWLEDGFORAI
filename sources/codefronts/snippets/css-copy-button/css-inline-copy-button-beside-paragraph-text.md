---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-inline-copy-button-beside-paragraph-text/"
title: "CSS Inline Copy Button Beside Paragraph Text"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "A copy control small enough to live inside a sentence."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Inline Copy Button Beside Paragraph Text
Source: https://codefronts.com/snippets/css-copy-button/css-inline-copy-button-beside-paragraph-text/

A copy control small enough to live inside a sentence. Two of them sit in this paragraph &mdash; beside a design token and beside a package name &mdash; baseline-aligned so the line height never shifts, hoverable as part of the code span, and each copying its own value. The hard part is not the click handler, it is making a button that does not disturb running text.
## HTML
```html
<div class="cpy-08">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-08__sr" type="checkbox" id="cpy-08-dark">
  <label class="cpy-08__theme" for="cpy-08-dark" title="Switch light or dark theme">
    <svg class="cpy-08__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-08__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-08__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-08__stage">
    <article class="cpy-08__doc">
      <p class="cpy-08__eyebrow">Docs prose &middot; inline control</p>
      <h2 class="cpy-08__title">Tokens you can lift mid-sentence</h2>
      <p class="cpy-08__body">Every accent in this collection resolves from a single token, <span class="cpy-08__unit"><code>--brand-600</code><button class="cpy-08__ib" type="button" data-copy="--brand-600" data-state="idle" aria-label="Copy token name --brand-600"><span class="cpy-08__icons"><svg class="cpy-08__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="2"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><svg class="cpy-08__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span></button></span>, which is defined once on the component root and overridden per theme. Install the tokens with <span class="cpy-08__unit"><code>@codefronts/tokens</code><button class="cpy-08__ib" type="button" data-copy="npm i @codefronts/tokens" data-state="idle" aria-label="Copy install command for the tokens package"><span class="cpy-08__icons"><svg class="cpy-08__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="2"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><svg class="cpy-08__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span></button></span> and the ramp arrives pre-tuned in <code>oklch()</code> with an sRGB fallback for older engines.</p>
      <p class="cpy-08__body cpy-08__body--muted">Notice what does not happen: the line spacing above and below this paragraph is identical to a paragraph with no buttons in it. The control is <code>1.15em</code> square, baseline-aligned, with its hit area extended outside the inline box.</p>
      <p class="cpy-08__live" role="status" aria-live="polite"></p>
    </article>
  </div>
</div>
```
## CSS
```css
.cpy-08 {
  --bg: #fbfaf8;
  --panel: #ffffff;
  --panel2: #f2f1ed;
  --ink: #15140f;
  --muted: #5f5c52;
  --line: rgba(21,20,15,.12);
  --accent: #7c3aed;
  --ok: #15803d;
  --dur: 180ms;
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

.cpy-08 *,
.cpy-08 *::before,
.cpy-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-08 {
    --accent: oklch(.53 .24 292);
    --ok: oklch(.55 .15 149);
  }
}

.cpy-08__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-08__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-08__theme {
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

.cpy-08__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-08__moon {
  display: none;
}

.cpy-08__sr:focus-visible + .cpy-08__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-08__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-08__doc {
  inline-size: min(100%,38rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.5rem,4.5vw,2.6rem);
  display: grid;
  gap: .9rem;
  box-shadow: 0 1px 2px rgba(21,20,15,.04),0 26px 50px -34px rgba(21,20,15,.3);
}

.cpy-08__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-08__title {
  margin: 0 0 .2rem;
  font-size: clamp(1.4rem,3.4vw,1.95rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-08__body {
  margin: 0;
  font-size: 1.02rem;
  line-height: 1.75;
  text-wrap: pretty;
}

.cpy-08__body--muted {
  font-size: .92rem;
  color: var(--muted);
}

.cpy-08__body code {
  font-family: var(--mono);
  font-size: .86em;
  padding: .12em .32em;
  border-radius: .3rem;
  background: var(--panel2);
  transition: background var(--dur);
}

.cpy-08__unit {
  white-space: nowrap;
}

.cpy-08__unit:has([data-state="copied"]) code {
  background: color-mix(in srgb,var(--ok) 18%,transparent);
}

.cpy-08__ib {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  vertical-align: baseline;
  margin-inline-start: .3em;
  inline-size: 1.15em;
  block-size: 1.15em;
  padding: 0;
  border: 0;
  border-radius: .25em;
  background: transparent;
  color: var(--muted);
  font-size: inherit;
  line-height: 1;
  cursor: pointer;
  transition: color var(--dur),scale var(--dur);
}

.cpy-08__ib::after {
  content: "";
  position: absolute;
  inset: -.45em;
}

.cpy-08__ib:hover {
  color: var(--accent);
}

.cpy-08__ib:active {
  scale: .88;
}

.cpy-08__ib:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: .15em;
}

.cpy-08__ib[data-state="copied"] {
  color: var(--ok);
}

.cpy-08__icons {
  position: relative;
  inline-size: 1em;
  block-size: 1em;
}

.cpy-08__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-08__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-08__ib[data-state="copied"] .cpy-08__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-08__ib[data-state="copied"] .cpy-08__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-08__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

@media not (prefers-color-scheme: dark) {
  .cpy-08:has(#cpy-08-dark:checked) {
    --bg: #0a0a09;
    --panel: #111110;
    --panel2: #1b1a18;
    --ink: #f2f0eb;
    --muted: rgba(242,240,235,.6);
    --line: rgba(242,240,235,.14);
    --accent: #c4b5fd;
    --ok: #6ee7a8;
  }

  .cpy-08:has(#cpy-08-dark:checked) .cpy-08__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-08:has(#cpy-08-dark:checked) .cpy-08__sun {
    display: none;
  }

  .cpy-08:has(#cpy-08-dark:checked) .cpy-08__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-08:not([data-theme="light"]):not(:has(#cpy-08-dark:checked)) {
    --bg: #0a0a09;
    --panel: #111110;
    --panel2: #1b1a18;
    --ink: #f2f0eb;
    --muted: rgba(242,240,235,.6);
    --line: rgba(242,240,235,.14);
    --accent: #c4b5fd;
    --ok: #6ee7a8;
  }

  .cpy-08__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-08__sun {
    display: none;
  }

  .cpy-08__moon {
    display: block;
  }

  .cpy-08:has(#cpy-08-dark:checked) .cpy-08__sun {
    display: block;
  }

  .cpy-08:has(#cpy-08-dark:checked) .cpy-08__moon {
    display: none;
  }
}

.cpy-08[data-theme="dark"] {
  --bg: #0a0a09;
  --panel: #111110;
  --panel2: #1b1a18;
  --ink: #f2f0eb;
  --muted: rgba(242,240,235,.6);
  --line: rgba(242,240,235,.14);
  --accent: #c4b5fd;
  --ok: #6ee7a8;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-08 *,
    .cpy-08 *::before,
    .cpy-08 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-08__doc,
    .cpy-08__theme {
    border-color: CanvasText;
    background: Canvas;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .cpy-08__ib {
    color: LinkText;
  }
}
```

## JavaScript
```js
const cpy08 = document.querySelector('.cpy-08');
if (cpy08) {
  const live = cpy08.querySelector('.cpy-08__live');
  const timers = new WeakMap();
  cpy08.addEventListener('click', async (event) => {
    const btn = event.target.closest('.cpy-08__ib');
    if (!btn) return;
    let ok = true;
    try { await navigator.clipboard.writeText(btn.dataset.copy); } catch { ok = false; }
    btn.dataset.state = ok ? 'copied' : 'idle';
    live.textContent = ok ? 'Copied ' + btn.dataset.copy : 'Clipboard blocked - press Ctrl C';
    clearTimeout(timers.get(btn));                  // per-button timer, no cross-talk
    timers.set(btn, setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, 2000));
  });
}
```
