---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-copy-button-icon-morphing-animation-copy-to-checkmark/"
title: "CSS Copy Button Icon Morphing Animation (Copy to Checkmark)"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "The icon itself is the feedback."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Copy Button Icon Morphing Animation (Copy to Checkmark)
Source: https://codefronts.com/snippets/css-copy-button/css-copy-button-icon-morphing-animation-copy-to-checkmark/

The icon itself is the feedback. On copy, the clipboard glyph shrinks and rotates out while a checkmark draws itself with stroke-dashoffset, then the whole thing rewinds on reset. A duration switcher (150 / 220 / 380&nbsp;ms) lets you feel exactly where a micro-interaction stops reading as instant &mdash; and it is pure CSS, driven by :has() on three radios.
## HTML
```html
<div class="cpy-02">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-02__sr" type="checkbox" id="cpy-02-dark">
  <label class="cpy-02__theme" for="cpy-02-dark" title="Switch light or dark theme">
    <svg class="cpy-02__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-02__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-02__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-02__stage">
    <div class="cpy-02__card">
      <p class="cpy-02__eyebrow">Icon morph &middot; copy &rarr; check</p>
      <h2 class="cpy-02__title">Watch the glyph become the tick</h2>

      <div class="cpy-02__demo">
        <button class="cpy-02__btn" type="button" data-state="idle" data-copy="git clone [email protected]:codefronts/clipboard.git">
          <span class="cpy-02__icons">
            <svg class="cpy-02__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-02__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path class="cpy-02__tick" pathLength="1" d="M5 12.6 9.7 17.3 19.4 7.1" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <span class="cpy-02__labels">
            <span class="cpy-02__l1">Copy clone URL</span>
            <span class="cpy-02__l2">Copied</span>
          </span>
        </button>
        <p class="cpy-02__snip"><code>git clone [email protected]:codefronts/clipboard.git</code></p>
      </div>

      <fieldset class="cpy-02__speed">
        <legend>Morph duration</legend>
        <input class="cpy-02__sr" type="radio" name="cpy-02-dur" id="cpy-02-fast">
        <label for="cpy-02-fast">150ms<span>snappy</span></label>
        <input class="cpy-02__sr" type="radio" name="cpy-02-dur" id="cpy-02-base" checked>
        <label for="cpy-02-base">220ms<span>house default</span></label>
        <input class="cpy-02__sr" type="radio" name="cpy-02-dur" id="cpy-02-slow">
        <label for="cpy-02-slow">380ms<span>too slow, on purpose</span></label>
      </fieldset>

      <p class="cpy-02__note">The tick is one <code>&lt;path&gt;</code> with <code>pathLength=&quot;1&quot;</code>, drawn by transitioning <code>stroke-dashoffset</code> from <code>1</code> to <code>0</code>.</p>
      <p class="cpy-02__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-02 {
  --bg: #f7f7f8;
  --panel: #ffffff;
  --panel2: #f1f2f5;
  --ink: #0c0d12;
  --muted: #616572;
  --line: rgba(12,13,18,.11);
  --accent: #0f766e;
  --ok: #0f766e;
  --ok-bg: rgba(15,118,110,.1);
  --err: #dc2626;
  --dur: 220ms;
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

.cpy-02 *,
.cpy-02 *::before,
.cpy-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-02 {
    --accent: oklch(.52 .11 183);
    --ok: oklch(.52 .11 183);
    --ok-bg: oklch(.52 .11 183/.12);
  }
}

.cpy-02__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-02__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-02__theme {
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

.cpy-02__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-02__moon {
  display: none;
}

.cpy-02__sr:focus-visible + .cpy-02__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-02__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-02__card {
  inline-size: min(100%,36rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.6rem;
  padding: clamp(1.4rem,4vw,2.3rem);
  display: grid;
  gap: 1rem;
  box-shadow: 0 1px 2px rgba(12,13,18,.05),0 26px 50px -34px rgba(12,13,18,.35);
}

.cpy-02__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-02__title {
  margin: 0;
  font-size: clamp(1.4rem,3.4vw,1.85rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-02__demo {
  display: grid;
  gap: .75rem;
  justify-items: start;
  padding: clamp(1rem,2.6vw,1.4rem);
  border: 1px solid var(--line);
  border-radius: 1.2rem;
  background: var(--panel2);
}

.cpy-02__snip {
  margin: 0;
  inline-size: 100%;
  overflow-x: auto;
  white-space: nowrap;
  scrollbar-width: none;
}

.cpy-02__snip code {
  font-family: var(--mono);
  font-size: .8rem;
  color: var(--muted);
}

.cpy-02__snip::-webkit-scrollbar {
  display: none;
}

.cpy-02__btn {
  min-block-size: 2.9rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  padding-inline: 1.1rem;
  border: 1px solid transparent;
  border-radius: .85rem;
  background: var(--ink);
  color: var(--panel);
  font: inherit;
  font-size: .92rem;
  font-weight: 560;
  cursor: pointer;
  transition: background var(--dur),color var(--dur),scale var(--dur);
}

.cpy-02__btn:active {
  scale: .975;
}

.cpy-02__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-02__btn[data-state="copied"] {
  background: var(--ok);
  color: #fff;
}

.cpy-02__btn[data-state="error"] {
  background: var(--err);
  color: #fff;
}

.cpy-02__icons {
  position: relative;
  inline-size: 1.25rem;
  block-size: 1.25rem;
  flex: none;
}

.cpy-02__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
}

.cpy-02__i1 {
  transition: opacity calc(var(--dur)*.65) ease,scale calc(var(--dur)*.65) ease,rotate calc(var(--dur)*.65) ease;
}

.cpy-02__btn[data-state="copied"] .cpy-02__i1 {
  opacity: 0;
  scale: .35;
  rotate: -28deg;
}

.cpy-02__tick {
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset var(--dur) cubic-bezier(.22,1,.36,1) calc(var(--dur)*.35);
}

.cpy-02__btn[data-state="copied"] .cpy-02__tick {
  stroke-dashoffset: 0;
}

.cpy-02__labels {
  display: grid;
}

.cpy-02__labels span {
  grid-area: 1/1;
  transition: opacity var(--dur) ease,translate var(--dur) ease;
}

.cpy-02__l2 {
  opacity: 0;
  translate: 0 .4rem;
}

.cpy-02__btn[data-state="copied"] .cpy-02__l1 {
  opacity: 0;
  translate: 0 -.4rem;
}

.cpy-02__btn[data-state="copied"] .cpy-02__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-02__speed {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  margin: 0;
  padding: 0;
  border: 0;
}

.cpy-02__speed legend {
  padding: 0 0 .5rem;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-02__speed label {
  display: grid;
  gap: .1rem;
  min-block-size: 44px;
  align-content: center;
  padding: .4rem .8rem;
  border: 1px solid var(--line);
  border-radius: .7rem;
  font-family: var(--mono);
  font-size: .8rem;
  cursor: pointer;
  transition: background var(--dur),border-color var(--dur);
}

.cpy-02__speed label span {
  font-family: var(--sans);
  font-size: .72rem;
  color: var(--muted);
}

.cpy-02__speed label:hover {
  background: var(--panel2);
}

.cpy-02__speed input:checked + label {
  border-color: var(--accent);
  background: var(--ok-bg);
  color: var(--accent);
}

.cpy-02__speed input:focus-visible + label {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpy-02:has(#cpy-02-fast:checked) {
  --dur: 150ms;
}

.cpy-02:has(#cpy-02-slow:checked) {
  --dur: 380ms;
}

.cpy-02__note {
  margin: 0;
  font-size: .86rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-02__note code {
  font-family: var(--mono);
  font-size: .78rem;
  padding: .1rem .3rem;
  border-radius: .3rem;
  background: var(--panel2);
}

.cpy-02__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

@media not (prefers-color-scheme: dark) {
  .cpy-02:has(#cpy-02-dark:checked) {
    --bg: #08090c;
    --panel: #0e1015;
    --panel2: #171a21;
    --ink: #eceef3;
    --muted: rgba(236,238,243,.62);
    --line: rgba(236,238,243,.14);
    --accent: #5eead4;
    --ok: #5eead4;
    --ok-bg: rgba(94,234,212,.14);
  }

  .cpy-02:has(#cpy-02-dark:checked) .cpy-02__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-02:has(#cpy-02-dark:checked) .cpy-02__sun {
    display: none;
  }

  .cpy-02:has(#cpy-02-dark:checked) .cpy-02__moon {
    display: block;
  }

  .cpy-02:has(#cpy-02-dark:checked) .cpy-02__btn[data-state="copied"] {
    color: #04231f;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-02:not([data-theme="light"]):not(:has(#cpy-02-dark:checked)) {
    --bg: #08090c;
    --panel: #0e1015;
    --panel2: #171a21;
    --ink: #eceef3;
    --muted: rgba(236,238,243,.62);
    --line: rgba(236,238,243,.14);
    --accent: #5eead4;
    --ok: #5eead4;
    --ok-bg: rgba(94,234,212,.14);
  }

  .cpy-02__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-02__sun {
    display: none;
  }

  .cpy-02__moon {
    display: block;
  }

  .cpy-02:has(#cpy-02-dark:checked) .cpy-02__sun {
    display: block;
  }

  .cpy-02:has(#cpy-02-dark:checked) .cpy-02__moon {
    display: none;
  }

  .cpy-02__btn[data-state="copied"] {
    color: #04231f;
  }
}

.cpy-02[data-theme="dark"] {
  --bg: #08090c;
  --panel: #0e1015;
  --panel2: #171a21;
  --ink: #eceef3;
  --muted: rgba(236,238,243,.62);
  --line: rgba(236,238,243,.14);
  --accent: #5eead4;
  --ok: #5eead4;
  --ok-bg: rgba(94,234,212,.14);
}

@media (prefers-reduced-motion: reduce) {
  .cpy-02 *,
    .cpy-02 *::before,
    .cpy-02 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-02__card,
    .cpy-02__demo,
    .cpy-02__btn,
    .cpy-02__theme,
    .cpy-02__speed label {
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
const cpy02 = document.querySelector('.cpy-02');
if (cpy02) {
  const btn = cpy02.querySelector('.cpy-02__btn');
  const live = cpy02.querySelector('.cpy-02__live');
  let timer;
  const set = (state, message, hold) => {
    btn.dataset.state = state;
    live.textContent = message;
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, hold);
  };
  btn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(btn.dataset.copy);
      set('copied', 'Clone URL copied', 2200);   // long enough to watch the tick draw
    } catch {
      set('error', 'Clipboard unavailable here', 2600);
    }
  });
}
```
