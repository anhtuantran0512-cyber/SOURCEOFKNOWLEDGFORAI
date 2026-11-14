---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/ripple-effect-on-click/"
title: "Data Attribute State Machine Transitions"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "One element moving through idle, loading, success and error, driven entirely by a single data-state attribute, with every visual difference expressed as a…"
has_js: "true"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data Attribute State Machine Transitions
Source: https://codefronts.com/motion/css-transition-designs/ripple-effect-on-click/

One element moving through idle, loading, success and error, driven entirely by a single data-state attribute, with every visual difference expressed as a transition between attribute selectors. Argues against class juggling: one attribute is one source of truth and cannot land in an impossible combined state the way four independent booleans can.
## HTML
```html
<section class="trn-13" aria-labelledby="trn-13-heading">
  <div class="trn-13__stage">
    <div class="trn-13__theme">
      <input class="trn-13__themecb" type="checkbox" id="trn-13-theme">
      <label class="trn-13__themebtn" for="trn-13-theme">
        <span class="trn-13__themeico" aria-hidden="true">
          <svg class="trn-13__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-13__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-13__head">
      <p class="trn-13__kicker">[data-state]</p>
      <h2 class="trn-13__heading" id="trn-13-heading">One attribute, four states, zero impossible combinations</h2>
      <p class="trn-13__sub">Every transition below is a change of one attribute value. No classes are added or removed.</p>
    </header>

    <div class="trn-13__machine" id="trn-13-machine" data-state="idle">
      <div class="trn-13__chip">
        <span class="trn-13__glyph" aria-hidden="true">
          <svg class="trn-13__ico trn-13__ico--idle" viewBox="0 0 20 20" width="18" height="18"><circle cx="10" cy="10" r="7.2" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
          <svg class="trn-13__ico trn-13__ico--load" viewBox="0 0 20 20" width="18" height="18"><path d="M10 2.8a7.2 7.2 0 1 1-7.1 8.4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <svg class="trn-13__ico trn-13__ico--ok" viewBox="0 0 20 20" width="18" height="18"><path d="m4.6 10.4 3.3 3.3 7.5-7.6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          <svg class="trn-13__ico trn-13__ico--err" viewBox="0 0 20 20" width="18" height="18"><path d="M5.4 5.4l9.2 9.2M14.6 5.4l-9.2 9.2" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        </span>
        <span class="trn-13__label" id="trn-13-label" role="status">Ready to deploy</span>
        <code class="trn-13__value" id="trn-13-value">data-state="idle"</code>
      </div>
      <div class="trn-13__meter"><span class="trn-13__fill"></span></div>
    </div>

    <div class="trn-13__controls">
      <button class="trn-13__btn" type="button" data-trn-13-set="idle">idle</button>
      <button class="trn-13__btn" type="button" data-trn-13-set="loading">loading</button>
      <button class="trn-13__btn" type="button" data-trn-13-set="success">success</button>
      <button class="trn-13__btn" type="button" data-trn-13-set="error">error</button>
    </div>

    <pre class="trn-13__snippet">.trn-13__chip { transition: color 260ms ease, border-color 260ms ease, background-color 260ms ease; }
[data-state="loading"] .trn-13__chip { color: var(--amber); border-color: var(--amber); }
[data-state="success"] .trn-13__chip { color: var(--green); border-color: var(--green); }
[data-state="error"]   .trn-13__chip { color: var(--red);   border-color: var(--red); }</pre>
  </div>
</section>
```
## CSS
```css
.trn-13 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #05080a;
  --grid: #0d1418;
  --ink: #d6f5df;
  --ink: oklch(0.93 0.05 155);
  --muted: #6d8878;
  --muted: oklch(0.58 0.03 158);
  --rule: #16211c;
  --green: #3ff58a;
  --green: oklch(0.87 0.2 150);
  --amber: #ffc857;
  --amber: oklch(0.85 0.14 82);
  --red: #ff6b6b;
  --red: oklch(0.71 0.18 22);
  --radius: 4px;
  --font-display: ui-monospace, "IBM Plex Mono", "JetBrains Mono", Menlo, monospace;
  background: linear-gradient(var(--grid) 1px, transparent 1px) 0 0 / 100% 22px, linear-gradient(90deg, var(--grid) 1px, transparent 1px) 0 0 / 22px 100%, var(--page);
  color: var(--ink);
  font-family: var(--font-display);
}

.trn-13 *,
.trn-13 *::before,
.trn-13 *::after {
  box-sizing: border-box;
}

.trn-13__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(22px, 5vw, 52px) 14px;
}

.trn-13__head {
  inline-size: 100%;
  max-inline-size: 50rem;
  min-inline-size: 0;
  margin: 0 0 20px;
}

.trn-13__kicker {
  margin: 0 0 8px;
  font: 400 11px/1 var(--font-display);
  letter-spacing: 0.14em;
  color: var(--green);
}

.trn-13__heading {
  margin: 0 0 8px;
  font: 400 clamp(20px, 4vw, 29px)/1.2 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.trn-13__sub {
  margin: 0;
  max-inline-size: 54ch;
  font: 400 13px/1.6 system-ui, sans-serif;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-13__machine {
  inline-size: 100%;
  max-inline-size: 50rem;
  min-inline-size: 0;
}

.trn-13__chip {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 12px;
  align-items: center;
  min-inline-size: 0;
  padding: 10px 12px;
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  background: rgba(63, 245, 138, 0.04);
  color: var(--muted);
  transition: color 260ms ease, border-color 260ms ease, background-color 260ms ease;
}

.trn-13__glyph {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 20px;
  block-size: 20px;
}

.trn-13__ico {
  grid-area: 1 / 1;
  opacity: 0;
  transition: opacity 200ms ease;
}

.trn-13__label {
  font: 400 13px/1 var(--font-display);
  color: var(--ink);
}

.trn-13__value {
  margin-inline-start: auto;
  font: 400 11.5px/1 var(--font-display);
  color: var(--muted);
}

.trn-13__meter {
  margin-block-start: 10px;
  block-size: 4px;
  background: var(--rule);
  border-radius: 2px;
  overflow: hidden;
}

.trn-13__fill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  background: var(--muted);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 420ms cubic-bezier(.3, .8, .3, 1), background-color 260ms ease;
}

.trn-13__machine[data-state="idle"] .trn-13__ico--idle {
  opacity: 1;
}

.trn-13__machine[data-state="loading"] .trn-13__ico--load {
  opacity: 1;
  animation: trn-13-spin 900ms linear infinite;
}

.trn-13__machine[data-state="success"] .trn-13__ico--ok {
  opacity: 1;
}

.trn-13__machine[data-state="error"] .trn-13__ico--err {
  opacity: 1;
}

.trn-13__machine[data-state="loading"] .trn-13__chip {
  color: var(--amber);
  border-color: var(--amber);
  background: rgba(255, 200, 87, 0.06);
}

.trn-13__machine[data-state="success"] .trn-13__chip {
  color: var(--green);
  border-color: var(--green);
  background: rgba(63, 245, 138, 0.07);
}

.trn-13__machine[data-state="error"] .trn-13__chip {
  color: var(--red);
  border-color: var(--red);
  background: rgba(255, 107, 107, 0.07);
}

.trn-13__machine[data-state="loading"] .trn-13__fill {
  transform: scaleX(0.62);
  background: var(--amber);
}

.trn-13__machine[data-state="success"] .trn-13__fill {
  transform: scaleX(1);
  background: var(--green);
}

.trn-13__machine[data-state="error"] .trn-13__fill {
  transform: scaleX(0.34);
  background: var(--red);
}

@keyframes trn-13-spin {
  to {
    transform: rotate(360deg);
  }
}

.trn-13__controls {
  inline-size: 100%;
  max-inline-size: 50rem;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-block-start: 16px;
}

.trn-13__btn {
  min-height: 44px;
  padding: 0 14px;
  background: transparent;
  color: var(--ink);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  cursor: pointer;
  font: 400 12.5px/1 var(--font-display);
  transition: border-color 180ms ease, color 180ms ease, background-color 180ms ease;
}

.trn-13__btn:hover {
  border-color: var(--green);
  color: var(--green);
  background: rgba(63, 245, 138, 0.06);
}

.trn-13__btn:focus-visible {
  outline: 2px solid var(--green);
  outline-offset: 2px;
}

.trn-13__btn[aria-pressed="true"] {
  border-color: var(--green);
  color: var(--page);
  background: var(--green);
}

.trn-13__snippet {
  inline-size: 100%;
  max-inline-size: 50rem;
  margin: 18px 0 0;
  padding: 12px;
  background: rgba(63, 245, 138, 0.04);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  font: 400 11px/1.65 var(--font-display);
  color: var(--muted);
  overflow-x: auto;
}

@media (prefers-reduced-motion: reduce) {
  .trn-13__chip {
    transition-duration: 140ms;
  }

  .trn-13__fill {
    transition: background-color 140ms ease;
    transform: scaleX(1);
  }

  .trn-13__machine[data-state="loading"] .trn-13__fill,
    .trn-13__machine[data-state="success"] .trn-13__fill,
    .trn-13__machine[data-state="error"] .trn-13__fill {
    transform: scaleX(1);
  }

  .trn-13__machine[data-state="loading"] .trn-13__ico--load {
    animation: none;
  }
}

@media (prefers-color-scheme: light) {
  .trn-13 {
    --page: #f4f9f5;
    --grid: #e2ece5;
    --ink: #0c1a12;
    --muted: #4c6355;
    --rule: #cddbd2;
    --green: #10763f;
    --amber: #8a5b06;
    --red: #b02a2a;
  }

  .trn-13__btn[aria-pressed="true"] {
    color: #f4f9f5;
  }
}

[data-theme="dark"] .trn-13 {
  --page: #05080a;
  --grid: #0d1418;
  --ink: #d6f5df;
  --muted: #6d8878;
  --rule: #16211c;
  --green: #3ff58a;
  --amber: #ffc857;
  --red: #ff6b6b;
}

[data-theme="dark"] .trn-13__btn[aria-pressed="true"] {
  color: #05080a;
}

.trn-13__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-13__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-13__themebtn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid currentColor;
  border-radius: 999px;
  cursor: pointer;
  color: var(--muted);
  font: 500 11px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: color 200ms ease, opacity 200ms ease;
}

.trn-13__themebtn:hover {
  color: var(--ink);
}

.trn-13__themecb:focus-visible + .trn-13__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-13__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-13__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-13__sun {
  opacity: 0.34;
}

.trn-13__moon {
  opacity: 1;
}

.trn-13:has(#trn-13-theme:checked) .trn-13__sun {
  opacity: 1;
}

.trn-13:has(#trn-13-theme:checked) .trn-13__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-13:has(#trn-13-theme:checked) {
    --page: #f4f9f5;
    --grid: #e2ece5;
    --ink: #0c1a12;
    --muted: #4c6355;
    --rule: #cddbd2;
    --green: #10763f;
    --amber: #8a5b06;
    --red: #b02a2a;
  }

  .trn-13:has(#trn-13-theme:checked) .trn-13__btn[aria-pressed="true"] {
    color: #f4f9f5;
  }
}

@media (prefers-color-scheme: light) {
  .trn-13:has(#trn-13-theme:checked) {
    --page: #05080a;
    --grid: #0d1418;
    --ink: #d6f5df;
    --ink: oklch(0.93 0.05 155);
    --muted: #6d8878;
    --muted: oklch(0.58 0.03 158);
    --rule: #16211c;
    --green: #3ff58a;
    --green: oklch(0.87 0.2 150);
    --amber: #ffc857;
    --amber: oklch(0.85 0.14 82);
    --red: #ff6b6b;
    --red: oklch(0.71 0.18 22);
    --radius: 4px;
    --font-display: ui-monospace, "IBM Plex Mono", "JetBrains Mono", Menlo, monospace;
    background: linear-gradient(var(--grid) 1px, transparent 1px) 0 0 / 100% 22px, linear-gradient(90deg, var(--grid) 1px, transparent 1px) 0 0 / 22px 100%, var(--page);
  }

  .trn-13:has(#trn-13-theme:checked) .trn-13__btn[aria-pressed="true"] {
    border-color: var(--green);
    color: var(--page);
    background: var(--green);
  }

  .trn-13:has(#trn-13-theme:checked) .trn-13__sun {
    opacity: 0.34;
  }

  .trn-13:has(#trn-13-theme:checked) .trn-13__moon {
    opacity: 1;
  }
}
```

## JavaScript
```js
const trn13 = document.querySelector('.trn-13');
if (trn13) {
  const machine = trn13.querySelector('#trn-13-machine');
  const label = trn13.querySelector('#trn-13-label');
  const value = trn13.querySelector('#trn-13-value');
  const copy = { idle: 'Ready to deploy', loading: 'Deploying to production…', success: 'Deployed — build 4192 live', error: 'Failed — migration 0041 rejected' };
  const buttons = [...trn13.querySelectorAll('[data-trn-13-set]')];
  const apply = (state) => {
    machine.setAttribute('data-state', state);
    label.textContent = copy[state];
    value.textContent = 'data-state="' + state + '"';
    for (const b of buttons) b.setAttribute('aria-pressed', String(b.getAttribute('data-trn-13-set') === state));
  };
  for (const b of buttons) b.addEventListener('click', () => apply(b.getAttribute('data-trn-13-set')));
  apply('idle');
}
```
