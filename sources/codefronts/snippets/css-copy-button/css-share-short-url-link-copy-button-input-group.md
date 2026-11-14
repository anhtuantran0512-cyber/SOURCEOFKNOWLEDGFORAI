---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-share-short-url-link-copy-button-input-group/"
title: "CSS Share Short URL Link Copy Button Input Group"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "The share-sheet pattern: a read-only field and a copy button welded into one unit, sharing a border and splitting the radius so it reads as a single control…"
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Share Short URL Link Copy Button Input Group
Source: https://codefronts.com/snippets/css-copy-button/css-share-short-url-link-copy-button-input-group/

The share-sheet pattern: a read-only field and a copy button welded into one unit, sharing a border and splitting the radius so it reads as a single control rather than two components pushed together. Focus the field and the whole link selects; press Enter and it copies &mdash; no form submit involved.
## HTML
```html
<div class="cpy-13">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-13__sr" type="checkbox" id="cpy-13-dark">
  <label class="cpy-13__theme" for="cpy-13-dark" title="Switch light or dark theme">
    <svg class="cpy-13__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-13__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-13__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-13__stage">
    <div class="cpy-13__sheet">
      <div class="cpy-13__head">
        <h2 class="cpy-13__title">Share this collection</h2>
        <p class="cpy-13__sub">Anyone with the link can view the 20 demos.</p>
      </div>

      <label class="cpy-13__label" for="cpy-13-input">Short link</label>
      <div class="cpy-13__group">
        <input class="cpy-13__input" id="cpy-13-input" type="text" value="https://cfr.to/copy-button" readonly spellcheck="false">
        <button class="cpy-13__btn" type="button" data-state="idle">
          <span class="cpy-13__icons">
            <svg class="cpy-13__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M10.4 13.6a4 4 0 0 0 5.66 0l2.83-2.83a4 4 0 1 0-5.66-5.66l-1.1 1.1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M13.6 10.4a4 4 0 0 0-5.66 0L5.11 13.2a4 4 0 1 0 5.66 5.66l1.1-1.1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <svg class="cpy-13__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <span class="cpy-13__labels"><span class="cpy-13__l1">Copy link</span><span class="cpy-13__l2">Copied</span></span>
        </button>
      </div>

      <p class="cpy-13__hint">Focus the field to select the whole link, or press <kbd class="cpy-13__kbd">Enter</kbd> to copy it.</p>
      <p class="cpy-13__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-13 {
  --bg: #f5f6f8;
  --panel: #ffffff;
  --panel2: #eff1f5;
  --ink: #0a0d15;
  --muted: #59616e;
  --line: rgba(10,13,21,.13);
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

.cpy-13 *,
.cpy-13 *::before,
.cpy-13 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-13 {
    --accent: oklch(.55 .21 262);
    --ok: oklch(.55 .15 149);
  }
}

.cpy-13__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-13__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-13__theme {
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

.cpy-13__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-13__moon {
  display: none;
}

.cpy-13__sr:focus-visible + .cpy-13__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-13__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-13__sheet {
  inline-size: min(100%,33rem);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  padding: clamp(1.4rem,4vw,2.25rem);
  display: grid;
  gap: .5rem;
  box-shadow: 0 1px 2px rgba(10,13,21,.05),0 28px 55px -36px rgba(10,13,21,.34);
}

.cpy-13__head {
  display: grid;
  gap: .3rem;
  margin-block-end: .9rem;
}

.cpy-13__title {
  margin: 0;
  font-size: clamp(1.3rem,3.2vw,1.7rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-13__sub {
  margin: 0;
  font-size: .92rem;
  line-height: 1.55;
  color: var(--muted);
}

.cpy-13__label {
  font-size: .8rem;
  font-weight: 560;
  color: var(--muted);
}

.cpy-13__group {
  display: flex;
  align-items: stretch;
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--panel);
  overflow: hidden;
  transition: border-color var(--dur),box-shadow var(--dur);
}

.cpy-13__group:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in srgb,var(--accent) 16%,transparent);
}

.cpy-13__input {
  flex: 1 1 8rem;
  min-inline-size: 0;
  padding: .9rem 1rem;
  border: 0;
  background: transparent;
  color: var(--ink);
  font-family: var(--mono);
  font-size: .88rem;
  outline: none;
}

.cpy-13__btn {
  flex: none;
  min-block-size: 2.9rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  padding-inline: 1rem;
  border: 0;
  border-inline-start: 1px solid var(--line);
  background: var(--panel2);
  color: var(--ink);
  font: inherit;
  font-size: .88rem;
  font-weight: 560;
  cursor: pointer;
  transition: background var(--dur),color var(--dur);
}

.cpy-13__btn:hover {
  background: color-mix(in srgb,var(--ink) 8%,var(--panel2));
}

.cpy-13__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.cpy-13__btn[data-state="copied"] {
  background: var(--ok);
  color: #fff;
  border-inline-start-color: var(--ok);
}

.cpy-13__icons {
  position: relative;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  flex: none;
}

.cpy-13__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-13__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-13__btn[data-state="copied"] .cpy-13__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-13__btn[data-state="copied"] .cpy-13__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-13__labels {
  display: grid;
}

.cpy-13__labels span {
  grid-area: 1/1;
  transition: opacity var(--dur),translate var(--dur);
}

.cpy-13__l2 {
  opacity: 0;
  translate: 0 .35rem;
}

.cpy-13__btn[data-state="copied"] .cpy-13__l1 {
  opacity: 0;
  translate: 0 -.35rem;
}

.cpy-13__btn[data-state="copied"] .cpy-13__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-13__hint {
  margin: .5rem 0 0;
  font-size: .82rem;
  line-height: 1.5;
  color: var(--muted);
}

.cpy-13__kbd {
  font-family: var(--mono);
  font-size: .72rem;
  padding: .1rem .35rem;
  border: 1px solid var(--line);
  border-block-end-width: 2px;
  border-radius: .3rem;
  background: var(--panel2);
  color: var(--ink);
}

.cpy-13__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ok);
}

@media (max-width: 24rem) {
  .cpy-13__group {
    flex-wrap: wrap;
  }

  .cpy-13__btn {
    inline-size: 100%;
    justify-content: center;
    border-inline-start: 0;
    border-block-start: 1px solid var(--line);
  }
}

@media not (prefers-color-scheme: dark) {
  .cpy-13:has(#cpy-13-dark:checked) {
    --bg: #06080e;
    --panel: #0c1017;
    --panel2: #161a24;
    --ink: #e8ebf3;
    --muted: rgba(232,235,243,.6);
    --line: rgba(232,235,243,.15);
    --accent: #93c5fd;
    --ok: #6ee7a8;
  }

  .cpy-13:has(#cpy-13-dark:checked) .cpy-13__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-13:has(#cpy-13-dark:checked) .cpy-13__sun {
    display: none;
  }

  .cpy-13:has(#cpy-13-dark:checked) .cpy-13__moon {
    display: block;
  }

  .cpy-13:has(#cpy-13-dark:checked) .cpy-13__btn[data-state="copied"] {
    color: #04231a;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-13:not([data-theme="light"]):not(:has(#cpy-13-dark:checked)) {
    --bg: #06080e;
    --panel: #0c1017;
    --panel2: #161a24;
    --ink: #e8ebf3;
    --muted: rgba(232,235,243,.6);
    --line: rgba(232,235,243,.15);
    --accent: #93c5fd;
    --ok: #6ee7a8;
  }

  .cpy-13__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-13__sun {
    display: none;
  }

  .cpy-13__moon {
    display: block;
  }

  .cpy-13:has(#cpy-13-dark:checked) .cpy-13__sun {
    display: block;
  }

  .cpy-13:has(#cpy-13-dark:checked) .cpy-13__moon {
    display: none;
  }

  .cpy-13__btn[data-state="copied"] {
    color: #04231a;
  }
}

.cpy-13[data-theme="dark"] {
  --bg: #06080e;
  --panel: #0c1017;
  --panel2: #161a24;
  --ink: #e8ebf3;
  --muted: rgba(232,235,243,.6);
  --line: rgba(232,235,243,.15);
  --accent: #93c5fd;
  --ok: #6ee7a8;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-13 *,
    .cpy-13 *::before,
    .cpy-13 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cpy-13__sheet,
    .cpy-13__group,
    .cpy-13__btn,
    .cpy-13__theme {
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
const cpy13 = document.querySelector('.cpy-13');
if (cpy13) {
  const input = cpy13.querySelector('.cpy-13__input');
  const btn = cpy13.querySelector('.cpy-13__btn');
  const live = cpy13.querySelector('.cpy-13__live');
  let timer;
  const selectAll = () => input.select();
  input.addEventListener('focus', selectAll);
  input.addEventListener('click', selectAll);
  input.addEventListener('keydown', (event) => {          // no form submit anywhere
    if (event.key === 'Enter') { event.preventDefault(); btn.click(); }
  });
  btn.addEventListener('click', async () => {
    let ok = true;
    try { await navigator.clipboard.writeText(input.value); } catch { ok = false; input.select(); }
    btn.dataset.state = ok ? 'copied' : 'idle';
    live.textContent = ok ? 'Link copied' : 'Clipboard blocked - the link is selected, press Ctrl C';
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, 2000);
  });
}
```
