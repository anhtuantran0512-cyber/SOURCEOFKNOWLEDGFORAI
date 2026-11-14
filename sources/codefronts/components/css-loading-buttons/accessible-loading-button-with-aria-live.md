---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/accessible-loading-button-with-aria-live/"
title: "Accessible Loading Button with ARIA Live"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "The contract a spinner alone does not satisfy."
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Loading Button with ARIA Live
Source: https://codefronts.com/components/css-loading-buttons/accessible-loading-button-with-aria-live/

The contract a spinner alone does not satisfy. While the request runs the button carries aria-busy, the state change is announced through a polite live region, and the failure path is announced through role=alert so it interrupts. It also fixes the disabled trap from the previous demo: aria-disabled plus a no-op handler keeps the control focusable while still refusing the work.
## HTML
```html
<div class="lb-04">
  <div class="lb-04__stage">
    <section class="lb-04__card" aria-labelledby="lb-04-h">
      <p class="lb-04__eyebrow">Draft · Autumn field notes</p>
      <h2 class="lb-04__h" id="lb-04-h">Publish post</h2>
      <p class="lb-04__sub">Both buttons do the same work. One is locked with the disabled property, one with aria-disabled. Tab to each, activate with Enter, and watch where focus lands.</p>

      <div class="lb-04__actions">
        <button class="lb-04__btn" type="button" id="lb-04-hard" data-state="idle" aria-busy="false">
          <span class="lb-04__spin" aria-hidden="true"></span>
          <span class="lb-04__label" id="lb-04-hard-label">Publish (disabled)</span>
        </button>
        <button class="lb-04__btn lb-04__btn--soft" type="button" id="lb-04-soft" data-state="idle" aria-busy="false" aria-disabled="false">
          <span class="lb-04__spin" aria-hidden="true"></span>
          <span class="lb-04__label" id="lb-04-soft-label">Publish (aria-disabled)</span>
        </button>
      </div>

      <p class="lb-04__focus">Focus is currently on: <output id="lb-04-focus">nothing</output></p>

      <div class="lb-04__regions">
        <p class="lb-04__polite" id="lb-04-live" role="status" aria-live="polite"></p>
        <p class="lb-04__alert" id="lb-04-alert" role="alert"></p>
      </div>

      <div class="lb-04__log">
        <p class="lb-04__logh">Announcement transcript</p>
        <ul class="lb-04__logl" id="lb-04-log"></ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-04 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #faf4e8;
  --surface: #fffdf7;
  --ink: #2a2118;
  --muted: #7d6b57;
  --rule: #e8dcc6;
  --accent: #b4531f;
  --ok: #3f7d54;
  --bad: #a32d20;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--paper);
  color: var(--ink);
  padding: 40px 18px;
}

.lb-04 *,
.lb-04 *::before,
.lb-04 *::after {
  box-sizing: border-box;
}

.lb-04__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-04__card {
  inline-size: 100%;
  max-inline-size: 34rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 18px;
  padding: 24px 22px;
  box-shadow: 0 14px 30px -22px rgba(42, 33, 24, .5);
}

.lb-04__eyebrow {
  margin: 0;
  font-size: 11px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.lb-04__h {
  margin: 6px 0 0;
  font-size: 22px;
  font-weight: 620;
  letter-spacing: -.02em;
}

.lb-04__sub {
  margin: 10px 0 20px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 52ch;
}

.lb-04__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  min-inline-size: 0;
}

.lb-04__btn {
  appearance: none;
  border: 0;
  background: var(--accent);
  color: #fff8f2;
  border-radius: 14px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  padding: 0 18px;
  min-block-size: 44px;
  min-inline-size: 0;
  display: inline-flex;
  align-items: center;
  gap: 9px;
  cursor: pointer;
  transition: background 180ms ease, opacity 180ms ease;
}

.lb-04__btn--soft {
  background: transparent;
  color: var(--accent);
  box-shadow: inset 0 0 0 1.5px var(--accent);
}

.lb-04__btn:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

.lb-04__btn:disabled {
  opacity: .62;
  cursor: progress;
}

.lb-04__btn[aria-disabled="true"] {
  opacity: .62;
  cursor: progress;
}

.lb-04__btn[data-state="done"] {
  background: var(--ok);
  color: #f4fbf6;
  box-shadow: none;
}

.lb-04__btn[data-state="error"] {
  background: var(--bad);
  color: #fff4f2;
  box-shadow: none;
}

.lb-04__label {
  min-inline-size: 0;
}

.lb-04__spin {
  inline-size: 0;
  block-size: 15px;
  border-radius: 50%;
  border: 2px solid currentColor;
  border-block-start-color: transparent;
  opacity: 0;
  transition: inline-size 160ms ease, opacity 160ms ease;
}

.lb-04__btn[data-state="pending"] .lb-04__spin {
  inline-size: 15px;
  opacity: 1;
  animation: lb-04-spin 700ms linear infinite;
}

@keyframes lb-04-spin {
  to {
    transform: rotate(1turn);
  }
}

.lb-04__focus {
  margin: 16px 0 0;
  font-size: 12.5px;
  color: var(--muted);
}

.lb-04__focus output {
  font-weight: 650;
  color: var(--ink);
}

.lb-04__regions {
  margin: 14px 0 0;
  display: grid;
  gap: 6px;
  min-block-size: 20px;
}

.lb-04__polite {
  margin: 0;
  font-size: 12.5px;
  color: var(--ok);
  min-inline-size: 0;
}

.lb-04__alert {
  margin: 0;
  font-size: 12.5px;
  font-weight: 620;
  color: var(--bad);
  min-inline-size: 0;
}

.lb-04__log {
  margin: 18px 0 0;
  border-top: 1px solid var(--rule);
  padding-top: 12px;
}

.lb-04__logh {
  margin: 0 0 8px;
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.lb-04__logl {
  margin: 0;
  padding-inline-start: 18px;
  display: grid;
  gap: 4px;
  font-size: 12px;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-04__spin {
    animation: none !important;
    transition: none;
  }

  .lb-04__btn[data-state="pending"] .lb-04__spin {
    border-block-start-color: currentColor;
    opacity: .5;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-04 {
    --paper: #171310;
    --surface: #201a15;
    --ink: #f4ece1;
    --muted: #a89584;
    --rule: #33291f;
    --accent: #e0813f;
    --ok: #63bd8b;
    --bad: #ee8272;
  }

  .lb-04__btn {
    color: #1b1410;
  }

  .lb-04__btn--soft {
    color: var(--accent);
  }
}

[data-theme="dark"] .lb-04 {
  --paper: #171310;
  --surface: #201a15;
  --ink: #f4ece1;
  --muted: #a89584;
  --rule: #33291f;
  --accent: #e0813f;
  --ok: #63bd8b;
  --bad: #ee8272;
}
```

## JavaScript
```js
const live = document.getElementById('lb-04-live');
const alertBox = document.getElementById('lb-04-alert');
const log = document.getElementById('lb-04-log');
const focusOut = document.getElementById('lb-04-focus');
const timers = {};

const note = (text) => {
  const li = document.createElement('li');
  li.textContent = text;
  log.prepend(li);
};

const run = (btn, soft, fails) => {
  if (btn.disabled || btn.getAttribute('aria-disabled') === 'true') return;
  clearTimeout(timers[btn.id]);
  btn.dataset.state = 'pending';
  btn.setAttribute('aria-busy', 'true');
  if (soft) btn.setAttribute('aria-disabled', 'true'); else btn.disabled = true;
  alertBox.textContent = '';
  live.textContent = 'Publishing post';
  note('polite: Publishing post');
  timers[btn.id] = setTimeout(() => {
    btn.dataset.state = fails ? 'error' : 'done';
    btn.setAttribute('aria-busy', 'false');
    if (soft) btn.setAttribute('aria-disabled', 'false'); else btn.disabled = false;
    if (fails) { alertBox.textContent = 'Publish failed: the draft has unsaved conflicts.'; note('alert: Publish failed'); }
    else { live.textContent = 'Post published'; note('polite: Post published'); }
    timers[btn.id] = setTimeout(() => { btn.dataset.state = 'idle'; }, 2000);
  }, 1500);
};

const hard = document.getElementById('lb-04-hard');
const soft = document.getElementById('lb-04-soft');
hard.addEventListener('click', () => run(hard, false, false));
soft.addEventListener('click', () => run(soft, true, true));
document.addEventListener('focusin', () => {
  const el = document.activeElement;
  focusOut.textContent = el && el.id ? el.id : el ? el.tagName.toLowerCase() : 'nothing';
});
document.addEventListener('focusout', () => setTimeout(() => {
  focusOut.textContent = document.activeElement && document.activeElement.id ? document.activeElement.id : 'body (focus was dropped)';
}, 0));
```
