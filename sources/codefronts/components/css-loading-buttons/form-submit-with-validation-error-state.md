---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/form-submit-with-validation-error-state/"
title: "Form Submit with Validation Error State"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "The round trip that is not a network failure: the spinner runs, the server rejects the value, and the button returns to interactive while the offending field…"
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Form Submit with Validation Error State
Source: https://codefronts.com/components/css-loading-buttons/form-submit-with-validation-error-state/

The round trip that is not a network failure: the spinner runs, the server rejects the value, and the button returns to interactive while the offending field is marked and described. The button's error state and the field's error state are two different messages — one says the request finished, the other says which value has to change.
## HTML
```html
<div class="lb-13">
  <div class="lb-13__stage">
    <section class="lb-13__card" aria-labelledby="lb-13-h">
      <h2 class="lb-13__h" id="lb-13-h">Create your account</h2>
      <p class="lb-13__sub">Try the address below as-is — the server already has it.</p>

      <div class="lb-13__field">
        <label class="lb-13__label" for="lb-13-email">Work email</label>
        <input class="lb-13__input" id="lb-13-email" type="email" value="[email protected]" aria-invalid="false" aria-describedby="lb-13-hint">
        <p class="lb-13__hint" id="lb-13-hint">We will send a confirmation link.</p>
        <p class="lb-13__ferr" id="lb-13-ferr" hidden></p>
      </div>

      <button class="lb-13__btn" type="button" id="lb-13-btn" data-state="idle" aria-busy="false">
        <span class="lb-13__spin" aria-hidden="true"></span>
        <span class="lb-13__blabel" id="lb-13-label">Create account</span>
      </button>

      <p class="lb-13__summary" id="lb-13-summary" role="alert"></p>
      <p class="lb-13__live" id="lb-13-live" role="status" aria-live="polite"></p>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-13 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #f7f2e7;
  --surface: #fffdf6;
  --ink: #26211a;
  --muted: #7a6d5c;
  --rule: #e5dbc6;
  --accent: #8a5a2b;
  --ok: #3d7a52;
  --bad: #a83226;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--paper);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-13 *,
.lb-13 *::before,
.lb-13 *::after {
  box-sizing: border-box;
}

.lb-13__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-13__card {
  inline-size: 100%;
  max-inline-size: 26rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 24px 22px;
  box-shadow: inset 0 -3px 0 var(--rule);
}

.lb-13__h {
  margin: 0;
  font-size: 20px;
  font-weight: 640;
  letter-spacing: -.015em;
}

.lb-13__sub {
  margin: 8px 0 20px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

.lb-13__field {
  display: grid;
  gap: 6px;
  margin-block-end: 18px;
  min-inline-size: 0;
}

.lb-13__label {
  font-size: 12px;
  font-weight: 620;
  letter-spacing: .01em;
}

.lb-13__input {
  font: inherit;
  font-size: 14px;
  color: var(--ink);
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 12px 13px;
  min-block-size: 46px;
  min-inline-size: 0;
  inline-size: 100%;
}

.lb-13__input:focus {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.lb-13__input:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 1px;
}

.lb-13__input[aria-invalid="true"] {
  border-color: var(--bad);
  box-shadow: inset 0 -2px 0 var(--bad);
  background: #fff7f5;
}

.lb-13__hint {
  margin: 0;
  font-size: 11.5px;
  color: var(--muted);
}

.lb-13__ferr {
  margin: 0;
  font-size: 12px;
  font-weight: 620;
  color: var(--bad);
  min-inline-size: 0;
}

.lb-13__btn {
  appearance: none;
  inline-size: 100%;
  border: 0;
  background: var(--accent);
  color: #fff9f2;
  border-radius: 4px;
  font: inherit;
  font-size: 14px;
  font-weight: 620;
  padding: 0 18px;
  min-block-size: 48px;
  min-inline-size: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  cursor: pointer;
}

.lb-13__btn:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 2px;
}

.lb-13__btn:disabled {
  cursor: progress;
  opacity: .85;
}

.lb-13__btn[data-state="done"] {
  background: var(--ok);
}

.lb-13__blabel {
  min-inline-size: 0;
}

.lb-13__spin {
  inline-size: 0;
  block-size: 15px;
  border-radius: 50%;
  border: 2px solid currentColor;
  border-block-end-color: transparent;
  opacity: 0;
  transition: inline-size 150ms ease, opacity 150ms ease;
}

.lb-13__btn[data-state="pending"] .lb-13__spin {
  inline-size: 15px;
  opacity: 1;
  animation: lb-13-spin 660ms linear infinite;
}

@keyframes lb-13-spin {
  to {
    transform: rotate(1turn);
  }
}

.lb-13__summary {
  margin: 12px 0 0;
  min-block-size: 17px;
  font-size: 12.5px;
  font-weight: 620;
  color: var(--bad);
  min-inline-size: 0;
}

.lb-13__live {
  margin: 2px 0 0;
  min-block-size: 17px;
  font-size: 12px;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .lb-13__spin {
    animation: none !important;
    transition: none;
  }

  .lb-13__btn[data-state="pending"] .lb-13__spin {
    border-block-end-color: currentColor;
    opacity: .55;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-13 {
    --paper: #18140f;
    --surface: #201b15;
    --ink: #f2ece1;
    --muted: #a4957f;
    --rule: #342c22;
    --accent: #cf9057;
    --ok: #56b47f;
    --bad: #ef7f6e;
  }

  .lb-13__btn {
    color: #1a1510;
  }

  .lb-13__input[aria-invalid="true"] {
    background: #251713;
  }
}

[data-theme="dark"] .lb-13 {
  --paper: #18140f;
  --surface: #201b15;
  --ink: #f2ece1;
  --muted: #a4957f;
  --rule: #342c22;
  --accent: #cf9057;
  --ok: #56b47f;
  --bad: #ef7f6e;
}
```

## JavaScript
```js
const btn = document.getElementById('lb-13-btn');
const input = document.getElementById('lb-13-email');
const ferr = document.getElementById('lb-13-ferr');
const summary = document.getElementById('lb-13-summary');
const label = document.getElementById('lb-13-label');
const live = document.getElementById('lb-13-live');
const taken = '[email protected]';
let timer;

const submit = () => {
  if (btn.disabled) return;
  clearTimeout(timer);
  input.setAttribute('aria-invalid', 'false');
  input.setAttribute('aria-describedby', 'lb-13-hint');
  ferr.hidden = true;
  summary.textContent = '';
  btn.disabled = true;
  btn.dataset.state = 'pending';
  btn.setAttribute('aria-busy', 'true');
  label.textContent = 'Creating account';
  timer = setTimeout(() => {
    btn.disabled = false;
    btn.setAttribute('aria-busy', 'false');
    if (input.value.trim().toLowerCase() === taken) {
      btn.dataset.state = 'idle';
      label.textContent = 'Create account';
      ferr.textContent = 'That address is already registered. Sign in instead, or use another address.';
      ferr.hidden = false;
      input.setAttribute('aria-invalid', 'true');
      input.setAttribute('aria-describedby', 'lb-13-ferr');
      summary.textContent = 'We could not create the account — one field needs attention.';
      input.focus();
    } else {
      btn.dataset.state = 'done';
      label.textContent = 'Account created';
      live.textContent = 'Account created. Check your inbox for the confirmation link.';
    }
  }, 1300);
};

btn.addEventListener('click', submit);
input.addEventListener('keydown', (event) => { if (event.key === 'Enter') { event.preventDefault(); submit(); } });
```
