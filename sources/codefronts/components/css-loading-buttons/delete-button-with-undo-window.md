---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/delete-button-with-undo-window/"
title: "Delete Button with Undo Window"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "Destructive actions done the modern way: act immediately, then offer a timed undo with a visible countdown, instead of blocking the user on a confirm dialog…"
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Delete Button with Undo Window
Source: https://codefronts.com/components/css-loading-buttons/delete-button-with-undo-window/

Destructive actions done the modern way: act immediately, then offer a timed undo with a visible countdown, instead of blocking the user on a confirm dialog first. The row leaves at once, a five-second window drains in view, and the commit only happens when the window closes. If that commit fails, the row comes back with an explanation.
## HTML
```html
<div class="lb-15">
  <div class="lb-15__stage">
    <section class="lb-15__panel" aria-labelledby="lb-15-h">
      <h2 class="lb-15__h" id="lb-15-h">API keys</h2>

      <div class="lb-15__table">
        <div class="lb-15__row" data-key="staging">
          <div class="lb-15__cell">
            <p class="lb-15__name">staging-writer</p>
            <p class="lb-15__meta">Created 12 Mar · last used 3 days ago</p>
          </div>
          <button class="lb-15__del" type="button" data-state="idle" aria-label="Delete key staging-writer">
            <svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4.5 6.5h11M8 6.5V4.8h4V6.5M6.2 6.5l.7 9h6.2l.7-9"/></svg>
          </button>
        </div>
        <div class="lb-15__row" data-key="ci">
          <div class="lb-15__cell">
            <p class="lb-15__name">ci-deploy</p>
            <p class="lb-15__meta">Created 2 Feb · last used 4 minutes ago</p>
          </div>
          <button class="lb-15__del" type="button" data-state="idle" aria-label="Delete key ci-deploy">
            <svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4.5 6.5h11M8 6.5V4.8h4V6.5M6.2 6.5l.7 9h6.2l.7-9"/></svg>
          </button>
        </div>
        <div class="lb-15__row" data-key="legacy">
          <div class="lb-15__cell">
            <p class="lb-15__name">legacy-import</p>
            <p class="lb-15__meta">Created 8 Nov · never used</p>
          </div>
          <button class="lb-15__del" type="button" data-state="idle" aria-label="Delete key legacy-import">
            <svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4.5 6.5h11M8 6.5V4.8h4V6.5M6.2 6.5l.7 9h6.2l.7-9"/></svg>
          </button>
        </div>
      </div>

      <div class="lb-15__undo" id="lb-15-undo" hidden>
        <span class="lb-15__utext" id="lb-15-utext">Key deleted</span>
        <span class="lb-15__timer" id="lb-15-timer">5</span>
        <button class="lb-15__ubtn" type="button" id="lb-15-undo-btn">Undo</button>
        <span class="lb-15__bar" id="lb-15-bar" aria-hidden="true"></span>
      </div>

      <label class="lb-15__toggle"><input type="checkbox" id="lb-15-fail"> Make the delete request fail</label>
      <p class="lb-15__live" id="lb-15-live" role="status" aria-live="polite"></p>
      <p class="lb-15__alert" id="lb-15-alert" role="alert"></p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-15 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #201d1a;
  --surface: #2a2622;
  --ink: #f3ede4;
  --muted: #a2988a;
  --rule: #3b352e;
  --amber: #f0a12e;
  --bad: #e5674b;
  --window: 5s;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-15 *,
.lb-15 *::before,
.lb-15 *::after {
  box-sizing: border-box;
}

.lb-15__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-15__panel {
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
}

.lb-15__h {
  margin: 0 0 14px;
  font-size: 19px;
  font-weight: 640;
  letter-spacing: -.015em;
}

.lb-15__table {
  display: grid;
  gap: 8px;
}

.lb-15__row {
  display: flex;
  gap: 12px;
  align-items: center;
  justify-content: space-between;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 6px;
  padding: 12px 14px;
  min-inline-size: 0;
}

.lb-15__cell {
  min-inline-size: 0;
}

.lb-15__name {
  margin: 0;
  font-size: 13.5px;
  font-weight: 600;
  font-family: ui-monospace, Menlo, monospace;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.lb-15__meta {
  margin: 4px 0 0;
  font-size: 11.5px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-15__del {
  appearance: none;
  flex: none;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 50%;
  border: 1px solid var(--rule);
  background: transparent;
  color: var(--muted);
  display: grid;
  place-items: center;
  cursor: pointer;
  transition: color 150ms ease, border-color 150ms ease, background 150ms ease;
}

.lb-15__del:hover {
  color: var(--bad);
  border-color: var(--bad);
}

.lb-15__del:focus-visible {
  outline: 3px solid var(--amber);
  outline-offset: 2px;
}

.lb-15__undo {
  position: relative;
  overflow: hidden;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin: 14px 0 0;
  padding: 12px 14px;
  background: var(--surface);
  border: 1px solid var(--amber);
  border-radius: 6px;
  min-inline-size: 0;
}

.lb-15__undo[hidden] {
  display: none;
}

.lb-15__utext {
  font-size: 13px;
  min-inline-size: 0;
}

.lb-15__timer {
  font-size: 12px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.lb-15__ubtn {
  appearance: none;
  margin-inline-start: auto;
  border: 0;
  background: var(--amber);
  color: #241804;
  border-radius: 4px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 700;
  padding: 0 16px;
  min-block-size: 44px;
  cursor: pointer;
}

.lb-15__ubtn:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 2px;
}

.lb-15__bar {
  position: absolute;
  inset-block-end: 0;
  inset-inline: 0;
  block-size: 3px;
  background: var(--amber);
  transform-origin: left center;
  transform: scaleX(1);
}

.lb-15__undo[data-running="true"] .lb-15__bar {
  transition: transform var(--window) linear;
  transform: scaleX(0);
}

.lb-15__toggle {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 12px 0 0;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
}

.lb-15__toggle input {
  accent-color: var(--amber);
  inline-size: 15px;
  block-size: 15px;
}

.lb-15__live {
  margin: 4px 0 0;
  min-block-size: 17px;
  font-size: 12px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-15__alert {
  margin: 2px 0 0;
  min-block-size: 17px;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--bad);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-15__undo[data-running="true"] .lb-15__bar {
    transition: none;
    transform: scaleX(1);
    opacity: .4;
  }

  .lb-15__del {
    transition: none;
  }
}

@media (prefers-color-scheme: light) {
  .lb-15 {
    --bg: #f6f2ea;
    --surface: #ffffff;
    --ink: #241f19;
    --muted: #756b5d;
    --rule: #e4ddd0;
    --amber: #a86a09;
    --bad: #b23f26;
  }

  .lb-15__ubtn {
    color: #fff8ea;
  }
}

[data-theme="light"] .lb-15 {
  --bg: #f6f2ea;
  --surface: #ffffff;
  --ink: #241f19;
  --muted: #756b5d;
  --rule: #e4ddd0;
  --amber: #a86a09;
  --bad: #b23f26;
}
```

## JavaScript
```js
const strip = document.getElementById('lb-15-undo');
const utext = document.getElementById('lb-15-utext');
const timerOut = document.getElementById('lb-15-timer');
const undoBtn = document.getElementById('lb-15-undo-btn');
const live = document.getElementById('lb-15-live');
const alertBox = document.getElementById('lb-15-alert');
const failBox = document.getElementById('lb-15-fail');
const WINDOW = 5000;
let commit;
let ticker;
let pending = null;

const closeStrip = () => {
  clearTimeout(commit);
  clearInterval(ticker);
  strip.hidden = true;
  strip.dataset.running = 'false';
};

document.querySelectorAll('.lb-15__del').forEach((btn) => {
  btn.addEventListener('click', () => {
    const row = btn.closest('.lb-15__row');
    const parent = row.parentNode;
    if (pending) closeStrip();
    pending = { row, parent, index: [...parent.children].indexOf(row), name: row.querySelector('.lb-15__name').textContent };
    row.remove();
    alertBox.textContent = '';
    utext.textContent = 'Deleted ' + pending.name;
    strip.hidden = false;
    strip.dataset.running = 'false';
    void strip.offsetWidth;
    strip.dataset.running = 'true';
    let left = WINDOW / 1000;
    timerOut.textContent = String(left);
    live.textContent = pending.name + ' deleted. Undo available for ' + left + ' seconds.';
    ticker = setInterval(() => { left -= 1; timerOut.textContent = String(Math.max(0, left)); }, 1000);
    const item = pending;
    commit = setTimeout(() => {
      clearInterval(ticker);
      strip.hidden = true;
      if (failBox.checked) {
        item.parent.insertBefore(item.row, item.parent.children[item.index] || null);
        alertBox.textContent = 'Delete failed on the server — ' + item.name + ' has been restored.';
      } else {
        live.textContent = item.name + ' permanently deleted.';
      }
      pending = null;
    }, WINDOW);
  });
});

undoBtn.addEventListener('click', () => {
  if (!pending) return;
  const item = pending;
  closeStrip();
  item.parent.insertBefore(item.row, item.parent.children[item.index] || null);
  live.textContent = item.name + ' restored.';
  pending = null;
});
```
