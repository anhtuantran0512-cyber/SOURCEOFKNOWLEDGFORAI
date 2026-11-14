---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/optimistic-ui-save-changes-button/"
title: "Optimistic UI Save Changes Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "Show Saved immediately, sync in the background, and roll back visibly if the write fails."
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Optimistic UI Save Changes Button
Source: https://codefronts.com/components/css-loading-buttons/optimistic-ui-save-changes-button/

Show Saved immediately, sync in the background, and roll back visibly if the write fails. There is no spinner at all in the happy path, which is the point: the interface commits to the user's intent and reconciles afterwards. It suits low-stakes writes like a preference toggle, and it is the wrong pattern for anything you cannot un-say.
## HTML
```html
<div class="lb-12">
  <div class="lb-12__stage">
    <section class="lb-12__panel" aria-labelledby="lb-12-h">
      <h2 class="lb-12__h" id="lb-12-h">Notifications</h2>
      <p class="lb-12__sub">Changes apply straight away and sync in the background. If a sync fails the switch goes back and says so.</p>

      <ul class="lb-12__rows">
        <li class="lb-12__row">
          <span class="lb-12__rl">Weekly summary email</span>
          <label class="lb-12__sw"><input type="checkbox" class="lb-12__cb" data-name="Weekly summary email" checked><span class="lb-12__track" aria-hidden="true"></span></label>
        </li>
        <li class="lb-12__row">
          <span class="lb-12__rl">Mentions and replies</span>
          <label class="lb-12__sw"><input type="checkbox" class="lb-12__cb" data-name="Mentions and replies"><span class="lb-12__track" aria-hidden="true"></span></label>
        </li>
        <li class="lb-12__row">
          <span class="lb-12__rl">Deploy failures</span>
          <label class="lb-12__sw"><input type="checkbox" class="lb-12__cb" data-name="Deploy failures" checked><span class="lb-12__track" aria-hidden="true"></span></label>
        </li>
      </ul>

      <div class="lb-12__foot">
        <button class="lb-12__btn" type="button" id="lb-12-btn" data-state="done" aria-busy="false">
          <span class="lb-12__label" id="lb-12-label">All changes saved</span>
        </button>
        <label class="lb-12__toggle"><input type="checkbox" id="lb-12-fail"> Make the next sync fail</label>
      </div>

      <p class="lb-12__live" id="lb-12-live" role="status" aria-live="polite"></p>
      <p class="lb-12__alert" id="lb-12-alert" role="alert"></p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-12 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #f1f3f5;
  --surface: #ffffff;
  --ink: #191c20;
  --muted: #6d757e;
  --rule: #dfe3e8;
  --accent: #2b3440;
  --ok: #1d7a52;
  --bad: #b23a2b;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-12 *,
.lb-12 *::before,
.lb-12 *::after {
  box-sizing: border-box;
}

.lb-12__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-12__panel {
  inline-size: 100%;
  max-inline-size: 33rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 10px;
  padding: 22px 20px;
}

.lb-12__h {
  margin: 0;
  font-size: 19px;
  font-weight: 640;
  letter-spacing: -.015em;
}

.lb-12__sub {
  margin: 8px 0 16px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 50ch;
}

.lb-12__rows {
  list-style: none;
  margin: 0;
  padding: 0;
}

.lb-12__row {
  display: flex;
  gap: 14px;
  align-items: center;
  justify-content: space-between;
  padding: 13px 0;
  border-block-start: 1px solid var(--rule);
  min-inline-size: 0;
}

.lb-12__rl {
  font-size: 13.5px;
  min-inline-size: 0;
}

.lb-12__sw {
  flex: none;
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  cursor: pointer;
}

.lb-12__cb {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
}

.lb-12__track {
  inline-size: 40px;
  block-size: 22px;
  border-radius: 999px;
  background: var(--rule);
  position: relative;
  transition: background 160ms ease;
}

.lb-12__track::after {
  content: "";
  position: absolute;
  inset-block-start: 3px;
  inset-inline-start: 3px;
  inline-size: 16px;
  block-size: 16px;
  border-radius: 50%;
  background: var(--surface);
  box-shadow: 0 1px 3px rgba(0, 0, 0, .3);
  transition: transform 160ms ease;
}

.lb-12__cb:checked + .lb-12__track {
  background: var(--accent);
}

.lb-12__cb:checked + .lb-12__track::after {
  transform: translateX(18px);
}

.lb-12__cb:focus-visible + .lb-12__track {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.lb-12__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
  margin: 18px 0 0;
  min-inline-size: 0;
}

.lb-12__btn {
  appearance: none;
  border: 1px solid var(--rule);
  background: transparent;
  color: var(--ok);
  border-radius: 999px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 620;
  padding: 0 16px;
  min-block-size: 44px;
  min-inline-size: 0;
  cursor: default;
}

.lb-12__btn[data-state="pending"] {
  color: var(--muted);
}

.lb-12__btn[data-state="error"] {
  color: var(--bad);
  border-color: var(--bad);
  cursor: pointer;
}

.lb-12__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.lb-12__label {
  min-inline-size: 0;
}

.lb-12__toggle {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
  min-inline-size: 0;
}

.lb-12__toggle input {
  accent-color: var(--accent);
  inline-size: 15px;
  block-size: 15px;
}

.lb-12__live {
  margin: 12px 0 0;
  min-block-size: 17px;
  font-size: 12px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-12__alert {
  margin: 2px 0 0;
  min-block-size: 17px;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--bad);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-12__track,
    .lb-12__track::after {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-12 {
    --bg: #14171a;
    --surface: #1b1f24;
    --ink: #e8ebef;
    --muted: #96a0aa;
    --rule: #2a3037;
    --accent: #9fb2c6;
    --ok: #52bd8d;
    --bad: #ee8272;
  }
}

[data-theme="dark"] .lb-12 {
  --bg: #14171a;
  --surface: #1b1f24;
  --ink: #e8ebef;
  --muted: #96a0aa;
  --rule: #2a3037;
  --accent: #9fb2c6;
  --ok: #52bd8d;
  --bad: #ee8272;
}
```

## JavaScript
```js
const btn = document.getElementById('lb-12-btn');
const label = document.getElementById('lb-12-label');
const live = document.getElementById('lb-12-live');
const alertBox = document.getElementById('lb-12-alert');
const failBox = document.getElementById('lb-12-fail');
let outstanding = 0;

const render = () => {
  if (outstanding > 0) {
    btn.dataset.state = 'pending';
    btn.setAttribute('aria-busy', 'true');
    label.textContent = 'Saved · syncing ' + outstanding;
  } else {
    btn.setAttribute('aria-busy', 'false');
    if (btn.dataset.state !== 'error') label.textContent = 'All changes saved';
  }
};

document.querySelectorAll('.lb-12__cb').forEach((cb) => {
  cb.addEventListener('change', () => {
    const snapshot = !cb.checked;
    const name = cb.dataset.name;
    const willFail = failBox.checked;
    outstanding += 1;
    btn.dataset.state = 'pending';
    alertBox.textContent = '';
    live.textContent = name + ' set to ' + (cb.checked ? 'on' : 'off');
    render();
    setTimeout(() => {
      outstanding -= 1;
      if (willFail) {
        cb.checked = snapshot;
        btn.dataset.state = 'error';
        label.textContent = 'Sync failed — reverted';
        alertBox.textContent = name + ' could not be saved and has been put back to ' + (snapshot ? 'on' : 'off') + '.';
      } else if (outstanding === 0) {
        btn.dataset.state = 'done';
      }
      render();
    }, 1300);
  });
});
```
