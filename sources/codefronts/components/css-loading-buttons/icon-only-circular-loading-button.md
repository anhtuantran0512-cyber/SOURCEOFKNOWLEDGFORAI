---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/icon-only-circular-loading-button/"
title: "Icon Only Circular Loading Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "A 44px circular control where the icon rotates out and a ring rotates in."
has_js: "false"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Icon Only Circular Loading Button
Source: https://codefronts.com/components/css-loading-buttons/icon-only-circular-loading-button/

A 44px circular control where the icon rotates out and a ring rotates in. The important part is not the animation: an icon-only button has no visible label, so its accessible name must change with the state or a screen reader user has no idea anything happened. Each state ships its own button element with its own name, swapped by CSS.
## HTML
```html
<div class="lb-17">
  <div class="lb-17__stage">
    <section class="lb-17__player" aria-labelledby="lb-17-h">
      <div class="lb-17__meta">
        <p class="lb-17__kicker">Episode 41</p>
        <h2 class="lb-17__h" id="lb-17-h">Rewriting the sync engine</h2>
        <p class="lb-17__by">With Sam Rivera · 48 min</p>
      </div>

      <div class="lb-17__bar">
        <button class="lb-17__ic" type="button" aria-label="Download episode">
          <svg viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M10 3.5v9M6 9l4 4 4-4M4 16.5h12"/></svg>
        </button>
        <button class="lb-17__ic" type="button" aria-label="Refresh feed">
          <svg viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M16 10a6 6 0 1 1-1.9-4.4"/><path d="M16.2 3v3.2H13"/></svg>
        </button>

        <span class="lb-17__slot">
          <button class="lb-17__ic lb-17__ic--mark lb-17__st lb-17__st--idle" type="button" aria-label="Save to bookmarks" aria-busy="false">
            <svg viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5.5 3.5h9v13l-4.5-3.4L5.5 16.5z"/></svg>
          </button>
          <button class="lb-17__ic lb-17__ic--mark lb-17__st lb-17__st--pending" type="button" aria-label="Saving bookmark" aria-busy="true" disabled>
            <svg class="lb-17__ring" viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="10" cy="10" r="7"/></svg>
          </button>
          <button class="lb-17__ic lb-17__ic--mark lb-17__st lb-17__st--done" type="button" aria-label="Saved to bookmarks, remove" aria-busy="false">
            <svg viewBox="0 0 20 20" width="17" height="17" fill="currentColor" stroke="none" aria-hidden="true"><path d="M5.5 3.5h9v13l-4.5-3.4L5.5 16.5z"/></svg>
          </button>
          <button class="lb-17__ic lb-17__ic--mark lb-17__st lb-17__st--error" type="button" aria-label="Saving failed, retry bookmark" aria-busy="false">
            <svg viewBox="0 0 20 20" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M10 3.6 17.6 16.6H2.4z"/><path d="M10 8.2v3.2"/><circle cx="10" cy="13.9" r=".9" fill="currentColor" stroke="none"/></svg>
          </button>
        </span>
      </div>

      <fieldset class="lb-17__states">
        <legend class="lb-17__legend">Bookmark state</legend>
        <label class="lb-17__radio"><input type="radio" name="lb-17-state" value="idle" checked> Idle</label>
        <label class="lb-17__radio"><input type="radio" name="lb-17-state" value="pending" class="lb-17__is-pending"> Pending</label>
        <label class="lb-17__radio"><input type="radio" name="lb-17-state" value="done" class="lb-17__is-done"> Saved</label>
        <label class="lb-17__radio"><input type="radio" name="lb-17-state" value="error" class="lb-17__is-error"> Failed</label>
      </fieldset>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-17 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #eceef1;
  --surface: #ffffff;
  --ink: #1c2126;
  --muted: #6a7480;
  --rule: #dce0e6;
  --accent: #33414f;
  --ok: #1e7a54;
  --bad: #ad3626;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-17 *,
.lb-17 *::before,
.lb-17 *::after {
  box-sizing: border-box;
}

.lb-17__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-17__player {
  inline-size: 100%;
  max-inline-size: 31rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 14px;
  padding: 20px;
  box-shadow: 0 10px 26px -22px rgba(28, 33, 38, .6);
}

.lb-17__kicker {
  margin: 0;
  font-size: 10.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.lb-17__h {
  margin: 6px 0 0;
  font-size: 18px;
  font-weight: 620;
  letter-spacing: -.015em;
  min-inline-size: 0;
}

.lb-17__by {
  margin: 5px 0 0;
  font-size: 12px;
  color: var(--muted);
}

.lb-17__bar {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
  margin: 18px 0 0;
  padding-block-start: 16px;
  border-block-start: 1px solid var(--rule);
  min-inline-size: 0;
}

.lb-17__ic {
  appearance: none;
  inline-size: 44px;
  block-size: 44px;
  flex: none;
  border-radius: 50%;
  border: 1px solid var(--rule);
  background: var(--surface);
  color: var(--muted);
  display: grid;
  place-items: center;
  cursor: pointer;
  transition: color 150ms ease, border-color 150ms ease, background 150ms ease;
}

.lb-17__ic:hover {
  color: var(--ink);
  border-color: var(--accent);
}

.lb-17__ic:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.lb-17__slot {
  display: inline-flex;
}

.lb-17__st {
  display: none;
}

.lb-17:has(input[value="idle"]:checked) .lb-17__st--idle,
.lb-17:has(.lb-17__is-pending:checked) .lb-17__st--pending,
.lb-17:has(.lb-17__is-done:checked) .lb-17__st--done,
.lb-17:has(.lb-17__is-error:checked) .lb-17__st--error {
  display: grid;
}

.lb-17__st--pending {
  color: var(--accent);
  cursor: progress;
}

.lb-17__st--done {
  color: var(--ok);
  border-color: var(--ok);
  background: rgba(30, 122, 84, .08);
}

.lb-17__st--error {
  color: var(--bad);
  border-color: var(--bad);
}

.lb-17__ring {
  transform-box: fill-box;
  transform-origin: 50% 50%;
  stroke-dasharray: 16 30;
  animation: lb-17-spin 760ms linear infinite;
}

@keyframes lb-17-spin {
  to {
    transform: rotate(1turn);
  }
}

.lb-17__states {
  margin: 18px 0 0;
  border: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 4px 14px;
  min-inline-size: 0;
}

.lb-17__legend {
  padding: 0;
  font-size: 10.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.lb-17__radio {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
  cursor: pointer;
}

.lb-17__radio input {
  accent-color: var(--accent);
  inline-size: 15px;
  block-size: 15px;
}

.lb-17__radio input:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lb-17__ring {
    animation: none;
    stroke-dasharray: 23 23;
  }

  .lb-17__ic {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-17 {
    --bg: #15181c;
    --surface: #1d2126;
    --ink: #e8ebef;
    --muted: #939ca8;
    --rule: #2b3138;
    --accent: #b3c1d0;
    --ok: #4fbb8a;
    --bad: #ee8171;
  }

  .lb-17__st--done {
    background: rgba(79, 187, 138, .12);
  }
}

[data-theme="dark"] .lb-17 {
  --bg: #15181c;
  --surface: #1d2126;
  --ink: #e8ebef;
  --muted: #939ca8;
  --rule: #2b3138;
  --accent: #b3c1d0;
  --ok: #4fbb8a;
  --bad: #ee8171;
}
```
