---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/button-with-inline-spinner-swap/"
title: "Button with Inline Spinner Swap"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "The reference build the rest of the collection reuses: the label crossfades into a spinner that sits exactly where the text was, both stacked in one grid…"
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Button with Inline Spinner Swap
Source: https://codefronts.com/components/css-loading-buttons/button-with-inline-spinner-swap/

The reference build the rest of the collection reuses: the label crossfades into a spinner that sits exactly where the text was, both stacked in one grid cell so nothing reflows. One data-state attribute on the button carries idle, pending, done and error, and attribute selectors do all the styling. Reach for it whenever a click starts work the user has to wait for.
## HTML
```html
<div class="lb-01">
  <div class="lb-01__stage">
    <section class="lb-01__card" aria-labelledby="lb-01-h">
      <header class="lb-01__head">
        <p class="lb-01__eyebrow">Account</p>
        <h2 class="lb-01__h" id="lb-01-h">Profile</h2>
      </header>

      <div class="lb-01__row">
        <div class="lb-01__field">
          <span class="lb-01__flabel">Display name</span>
          <span class="lb-01__fvalue">Alex Chen</span>
        </div>
        <div class="lb-01__field">
          <span class="lb-01__flabel">Role</span>
          <span class="lb-01__fvalue">Engineering, Platform</span>
        </div>
      </div>

      <footer class="lb-01__foot">
        <div class="lb-01__mode" role="group" aria-label="Simulated response">
          <label class="lb-01__radio"><input type="radio" name="lb-01-mode" value="ok" checked> Succeeds</label>
          <label class="lb-01__radio"><input type="radio" name="lb-01-mode" value="fail"> Fails</label>
        </div>

        <button class="lb-01__btn" type="button" id="lb-01-btn" data-state="idle" aria-busy="false">
          <span class="lb-01__faces">
            <span class="lb-01__face lb-01__face--idle">Save changes</span>
            <span class="lb-01__face lb-01__face--pending">
              <svg class="lb-01__spin" viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><circle cx="10" cy="10" r="7.5" stroke-opacity=".28"/><path d="M17.5 10A7.5 7.5 0 0 0 10 2.5"/></svg>
              Saving
            </span>
            <span class="lb-01__face lb-01__face--done">
              <svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4.5 10.5l3.5 3.5 7.5-8"/></svg>
              Saved
            </span>
            <span class="lb-01__face lb-01__face--error">
              <svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M10 5.5v5.5"/><circle cx="10" cy="14.6" r=".9" fill="currentColor" stroke="none"/></svg>
              Retry
            </span>
          </span>
        </button>
      </footer>

      <p class="lb-01__status" id="lb-01-live" role="status" aria-live="polite">Ready</p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-01 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #f7f6f2;
  --surface: #ffffff;
  --ink: #17161a;
  --muted: #6e6c74;
  --rule: #e5e3dc;
  --accent: #17161a;
  --on-accent: #ffffff;
  --ok: #1c7a55;
  --bad: #b4342a;
  --dur: 220ms;
  --hold: 1500ms;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--paper);
  color: var(--ink);
  padding: 40px 18px;
}

.lb-01 *,
.lb-01 *::before,
.lb-01 *::after {
  box-sizing: border-box;
}

.lb-01__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-01__card {
  inline-size: 100%;
  max-inline-size: 30rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 6px;
  padding: 22px 22px 18px;
}

.lb-01__eyebrow {
  margin: 0;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.lb-01__h {
  margin: 4px 0 0;
  font-size: 20px;
  font-weight: 640;
  letter-spacing: -.015em;
}

.lb-01__row {
  display: grid;
  gap: 14px;
  margin: 18px 0;
  padding: 16px 0;
  border-block: 1px solid var(--rule);
}

.lb-01__field {
  display: flex;
  flex-wrap: wrap;
  gap: 4px 14px;
  justify-content: space-between;
  min-inline-size: 0;
}

.lb-01__flabel {
  font-size: 12.5px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-01__fvalue {
  font-size: 13px;
  font-weight: 560;
  min-inline-size: 0;
}

.lb-01__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
  justify-content: space-between;
  min-inline-size: 0;
}

.lb-01__mode {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  min-inline-size: 0;
}

.lb-01__radio {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
}

.lb-01__radio input {
  accent-color: var(--accent);
  inline-size: 15px;
  block-size: 15px;
}

.lb-01__btn {
  appearance: none;
  border: 1px solid var(--accent);
  background: var(--accent);
  color: var(--on-accent);
  border-radius: 6px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 560;
  padding: 0 18px;
  min-block-size: 44px;
  min-inline-size: 0;
  cursor: pointer;
  transition: background var(--dur) ease, border-color var(--dur) ease, transform 120ms ease;
}

.lb-01__btn:active {
  transform: translateY(1px);
}

.lb-01__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.lb-01__btn[data-state="pending"] {
  cursor: progress;
}

.lb-01__btn[data-state="done"] {
  background: var(--ok);
  border-color: var(--ok);
}

.lb-01__btn[data-state="error"] {
  background: var(--bad);
  border-color: var(--bad);
}

.lb-01__faces {
  display: grid;
  place-items: center;
}

.lb-01__face {
  grid-area: 1 / 1;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  white-space: nowrap;
  opacity: 0;
  visibility: hidden;
  transform: scale(.92);
  transition: opacity var(--dur) ease, transform var(--dur) ease, visibility var(--dur);
}

.lb-01__btn[data-state="idle"] .lb-01__face--idle,
.lb-01__btn[data-state="pending"] .lb-01__face--pending,
.lb-01__btn[data-state="done"] .lb-01__face--done,
.lb-01__btn[data-state="error"] .lb-01__face--error {
  opacity: 1;
  visibility: visible;
  transform: none;
}

.lb-01__spin {
  animation: lb-01-spin 720ms linear infinite;
}

@keyframes lb-01-spin {
  to {
    transform: rotate(1turn);
  }
}

.lb-01__status {
  margin: 14px 0 0;
  font-size: 12px;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-01__spin {
    animation: none;
  }

  .lb-01__face {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-01 {
    --paper: #131316;
    --surface: #1b1b20;
    --ink: #edecf1;
    --muted: #9b99a4;
    --rule: #2b2b33;
    --accent: #edecf1;
    --on-accent: #131316;
    --ok: #4fbd90;
    --bad: #f0857a;
  }
}

[data-theme="dark"] .lb-01 {
  --paper: #131316;
  --surface: #1b1b20;
  --ink: #edecf1;
  --muted: #9b99a4;
  --rule: #2b2b33;
  --accent: #edecf1;
  --on-accent: #131316;
  --ok: #4fbd90;
  --bad: #f0857a;
}
```

## JavaScript
```js
const btn = document.getElementById('lb-01-btn');
const live = document.getElementById('lb-01-live');
let timer;

const set = (state, message) => {
  btn.dataset.state = state;
  btn.setAttribute('aria-busy', String(state === 'pending'));
  live.textContent = message;
};

btn.addEventListener('click', () => {
  if (btn.dataset.state === 'pending') return;
  clearTimeout(timer);
  set('pending', 'Saving profile changes');
  const fails = document.querySelector('input[name="lb-01-mode"]:checked').value === 'fail';
  timer = setTimeout(() => {
    if (fails) {
      set('error', 'Could not save. Press the button to retry.');
    } else {
      set('done', 'Profile saved');
    }
    timer = setTimeout(() => set('idle', 'Ready'), 1500);
  }, 1400);
});
```
