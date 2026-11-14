---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-button-disabled-and-error-states/"
title: "Stroke Draw Button Disabled and Error States"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A prescription review screen, where three states have to be visually and semantically distinct: the dose stepper's minus is genuinely disabled at the floor,…"
has_js: "true"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stroke Draw Button Disabled and Error States
Source: https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-button-disabled-and-error-states/

A prescription review screen, where three states have to be visually and semantically distinct: the dose stepper's minus is genuinely disabled at the floor, the sign-off button is aria-disabled so a keyboard user can still reach it and learn what is missing, and the error frame appears instantly at full weight with an icon, a rewritten message and aria-invalid — never colour alone.
## HTML
```html
<section class="svgb-16" data-state="idle">
  <input class="svgb-16__ti" type="checkbox" id="svgb-16-theme">
  <label class="svgb-16__toggle" for="svgb-16-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-16__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-16__stage">
    <div class="svgb-16__chart">
      <div class="svgb-16__band">
        <span class="svgb-16__bl">Patient</span>
        <span class="svgb-16__bv">R. Okonjo &middot; 42y</span>
        <span class="svgb-16__bl">Ward</span>
        <span class="svgb-16__bv">C4 &middot; bed 11</span>
      </div>

      <h1 class="svgb-16__drug">Amoxicillin <span>500 mg</span></h1>

      <div class="svgb-16__dose">
        <span class="svgb-16__dlabel">Doses per day</span>
        <div class="svgb-16__stepper">
          <button class="svgb-16__step" type="button" disabled aria-label="Decrease doses">
            <svg class="svgb-16__sframe" viewBox="0 0 52 52" aria-hidden="true">
              <rect class="svgb-16__sbase svgb-16__sbase--off" x="1.5" y="1.5" width="49" height="49" rx="10" pathLength="1"/>
            </svg>
            <span class="svgb-16__sg">&minus;</span>
          </button>
          <span class="svgb-16__count">1</span>
          <button class="svgb-16__step" type="button" aria-label="Increase doses">
            <svg class="svgb-16__sframe" viewBox="0 0 52 52" aria-hidden="true">
              <rect class="svgb-16__sbase" x="1.5" y="1.5" width="49" height="49" rx="10" pathLength="1"/>
              <rect class="svgb-16__sink" x="1.5" y="1.5" width="49" height="49" rx="10" pathLength="1"/>
            </svg>
            <span class="svgb-16__sg">+</span>
          </button>
        </div>
        <span class="svgb-16__hint">minimum reached &rarr; truly <code>disabled</code></span>
      </div>

      <label class="svgb-16__flabel" for="svgb-16-field">Prescriber ID</label>
      <input class="svgb-16__field" id="svgb-16-field" type="text" placeholder="GMC 7 digits" autocomplete="off" inputmode="numeric" aria-describedby="svgb-16-msg">
      <p class="svgb-16__msg" id="svgb-16-msg">
        <span class="svgb-16__micon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 8v5"/><circle cx="12" cy="16.4" r="0.9" fill="currentColor" stroke="none"/><path d="M12 3.5 21 19H3Z"/></svg>
        </span>
        <span class="svgb-16__mtext">Sign-off is blocked until a prescriber ID is entered.</span>
      </p>

      <button class="svgb-16__sign" type="button" aria-disabled="true">
        <svg class="svgb-16__frame" viewBox="0 0 380 62" aria-hidden="true">
          <rect class="svgb-16__base" x="2" y="2" width="376" height="58" rx="8" pathLength="1"/>
          <rect class="svgb-16__ink" x="2" y="2" width="376" height="58" rx="8" pathLength="1"/>
        </svg>
        <span class="svgb-16__label">Sign and send to pharmacy</span>
      </button>

      <p class="svgb-16__legend">
        <span class="svgb-16__tag">aria-disabled</span> reachable, explains itself
        <span class="svgb-16__tag svgb-16__tag--off">disabled</span> inert by design
      </p>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');

.svgb-16 {
  --svgb-16-bg: #eef0f1;
  --svgb-16-bg: oklch(0.945 0.004 220);
  --svgb-16-fg: #101316;
  --svgb-16-fg: oklch(0.185 0.006 230);
  --svgb-16-muted: #5a6169;
  --svgb-16-muted: oklch(0.50 0.011 230);
  --svgb-16-card: #ffffff;
  --svgb-16-card: oklch(1 0 0);
  --svgb-16-rest: rgba(16, 19, 22, 0.16);
  --svgb-16-rest: oklch(0.185 0.006 230 / 0.16);
  --svgb-16-stroke: #0c6b8f;
  --svgb-16-stroke: oklch(0.48 0.11 225);
  --svgb-16-err: #b81f1f;
  --svgb-16-err: oklch(0.50 0.20 27);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-16-bg);
  position: relative;
  color: var(--svgb-16-fg);
  font-family: 'IBM Plex Sans', system-ui, sans-serif;
}

.svgb-16 *,
.svgb-16 *::before,
.svgb-16 *::after {
  box-sizing: border-box;
}

.svgb-16__stage {
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px, 5vw, 64px);
}

.svgb-16__chart {
  width: 100%;
  max-width: 500px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: clamp(22px, 4vw, 36px);
  border-radius: 4px;
  background: var(--svgb-16-card);
  border: 1px solid var(--svgb-16-rest);
  border-block-start: 4px solid var(--svgb-16-stroke);
}

.svgb-16__band {
  display: grid;
  grid-template-columns: auto 1fr auto 1fr;
  gap: 4px 12px;
  padding-block-end: 14px;
  border-block-end: 1px solid var(--svgb-16-rest);
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 10.5px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.svgb-16__bl {
  color: var(--svgb-16-muted);
}

.svgb-16__drug {
  margin: 6px 0 4px;
  font-size: clamp(24px, 4vw, 34px);
  font-weight: 600;
  letter-spacing: -0.02em;
}

.svgb-16__drug span {
  color: var(--svgb-16-muted);
  font-weight: 400;
}

.svgb-16__dose {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-block: 8px;
}

.svgb-16__dlabel {
  font-size: 13px;
  font-weight: 500;
}

.svgb-16__stepper {
  display: flex;
  align-items: center;
  gap: 14px;
}

.svgb-16__step {
  position: relative;
  inline-size: 52px;
  block-size: 52px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 10px;
  background: color-mix(in oklab, var(--svgb-16-stroke) 8%, transparent);
  color: inherit;
  font: inherit;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-16__step[disabled] {
  cursor: not-allowed;
  background: color-mix(in oklab, var(--svgb-16-fg) 4%, transparent);
  color: var(--svgb-16-muted);
}

.svgb-16__step:focus-visible {
  outline: 2px solid var(--svgb-16-stroke);
  outline-offset: 3px;
}

.svgb-16__sg {
  position: relative;
  z-index: 1;
  font-size: 22px;
  line-height: 1;
}

.svgb-16__sframe,
.svgb-16__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-16__sframe rect,
.svgb-16__frame rect {
  fill: none;
  stroke-linecap: round;
}

.svgb-16__sbase {
  stroke: var(--svgb-16-rest);
  stroke-width: 1.5px;
}

.svgb-16__sbase--off {
  stroke-dasharray: 0.02 0.02;
}

.svgb-16__sink {
  stroke: var(--svgb-16-stroke);
  stroke-width: 2.2px;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 480ms cubic-bezier(0.22, 1, 0.36, 1);
}

.svgb-16__step:hover .svgb-16__sink,
.svgb-16__step:focus-visible .svgb-16__sink {
  stroke-dashoffset: 0;
}

.svgb-16__count {
  min-inline-size: 2ch;
  text-align: center;
  font-size: 22px;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.svgb-16__hint {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 11px;
  color: var(--svgb-16-muted);
}

.svgb-16__hint code {
  font-size: 11px;
}

.svgb-16__flabel {
  margin-block-start: 6px;
  font-size: 13px;
  font-weight: 500;
}

.svgb-16__field {
  block-size: 52px;
  padding: 0 14px;
  border-radius: 4px;
  border: 1.5px solid var(--svgb-16-rest);
  background: color-mix(in oklab, var(--svgb-16-fg) 2%, transparent);
  color: inherit;
  font: inherit;
  font-size: 15px;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  transition: border-color 200ms ease, box-shadow 200ms ease;
}

.svgb-16__field:focus-visible {
  outline: none;
  border-color: var(--svgb-16-stroke);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--svgb-16-stroke) 22%, transparent);
}

.svgb-16__field[aria-invalid='true'] {
  border-color: var(--svgb-16-err);
}

.svgb-16__msg {
  margin: 0 0 6px;
  display: flex;
  gap: 8px;
  align-items: flex-start;
  font-size: 13px;
  line-height: 1.45;
  color: var(--svgb-16-muted);
}

.svgb-16__micon {
  display: none;
  flex: none;
  color: var(--svgb-16-err);
}

.svgb-16__micon svg {
  inline-size: 16px;
  block-size: 16px;
  display: block;
}

.svgb-16[data-state='error'] .svgb-16__micon {
  display: block;
}

.svgb-16[data-state='error'] .svgb-16__mtext {
  color: var(--svgb-16-err);
  font-weight: 500;
}

.svgb-16__sign {
  position: relative;
  inline-size: 100%;
  block-size: 62px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 8px;
  background: color-mix(in oklab, var(--svgb-16-stroke) 10%, transparent);
  color: inherit;
  font: inherit;
  font-size: 15.5px;
  font-weight: 600;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-16__label {
  position: relative;
  z-index: 1;
}

.svgb-16__sign:focus-visible {
  outline: 2px solid var(--svgb-16-stroke);
  outline-offset: 3px;
}

.svgb-16__base {
  stroke: var(--svgb-16-rest);
  stroke-width: 1.5px;
}

.svgb-16__ink {
  stroke: var(--svgb-16-stroke);
  stroke-width: 2.2px;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 560ms cubic-bezier(0.22, 1, 0.36, 1), stroke 200ms ease;
}

.svgb-16__sign:hover .svgb-16__ink,
.svgb-16__sign:focus-visible .svgb-16__ink {
  stroke-dashoffset: 0;
}

.svgb-16__sign[aria-disabled='true'] {
  cursor: not-allowed;
  background: color-mix(in oklab, var(--svgb-16-stroke) 4%, transparent);
}

.svgb-16__sign[aria-disabled='true'] .svgb-16__ink {
  stroke-dasharray: 0.02 0.014;
  stroke-dashoffset: 0;
  stroke: color-mix(in oklab, var(--svgb-16-stroke) 50%, transparent);
}

@keyframes svgb-16-nudge {
  0%,
    100% {
    translate: 0 0;
  }

  20% {
    translate: -4px 0;
  }

  45% {
    translate: 4px 0;
  }

  70% {
    translate: -2px 0;
  }
}

.svgb-16[data-state='error'] .svgb-16__sign {
  background: color-mix(in oklab, var(--svgb-16-err) 8%, transparent);
  animation: svgb-16-nudge 420ms cubic-bezier(0.36, 0.07, 0.19, 0.97) 1;
}

.svgb-16[data-state='error'] .svgb-16__sign .svgb-16__ink {
  stroke: var(--svgb-16-err);
  stroke-width: 2.6px;
  stroke-dasharray: none;
  stroke-dashoffset: 0;
  transition: none;
}

.svgb-16[data-state='sent'] .svgb-16__sign {
  background: color-mix(in oklab, var(--svgb-16-stroke) 16%, transparent);
}

.svgb-16__legend {
  margin: 2px 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: 8px 12px;
  align-items: center;
  font-size: 12px;
  color: var(--svgb-16-muted);
}

.svgb-16__tag {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 10.5px;
  padding: 3px 7px;
  border-radius: 3px;
  background: color-mix(in oklab, var(--svgb-16-stroke) 12%, transparent);
  color: color-mix(in oklab, var(--svgb-16-stroke) 80%, var(--svgb-16-fg));
}

.svgb-16__tag--off {
  background: color-mix(in oklab, var(--svgb-16-fg) 8%, transparent);
  color: var(--svgb-16-muted);
}

.svgb-16__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-16__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 4px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 6%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-16__toggle:hover {
  background: color-mix(in oklab, currentColor 13%, transparent);
}

.svgb-16__toggle:active {
  transform: scale(0.94);
}

.svgb-16__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-16__ti:checked + .svgb-16__toggle svg {
  transform: rotate(180deg);
}

.svgb-16__ti:focus-visible + .svgb-16__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-16__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-16:has(#svgb-16-theme:checked) {
  --svgb-16-bg: #0d1013;
  --svgb-16-bg: oklch(0.175 0.006 230);
  --svgb-16-fg: #eceff1;
  --svgb-16-fg: oklch(0.95 0.004 230);
  --svgb-16-muted: #8b929a;
  --svgb-16-muted: oklch(0.67 0.011 230);
  --svgb-16-card: #14181c;
  --svgb-16-card: oklch(0.215 0.008 230);
  --svgb-16-rest: rgba(236, 239, 241, 0.18);
  --svgb-16-rest: oklch(0.95 0.004 230 / 0.18);
  --svgb-16-stroke: #6fc6e8;
  --svgb-16-stroke: oklch(0.80 0.10 225);
  --svgb-16-err: #ff8f80;
  --svgb-16-err: oklch(0.78 0.15 30);
}

@media (forced-colors: active) {
  .svgb-16__ink,
    .svgb-16__sink {
    stroke: transparent;
  }

  .svgb-16__sign,
    .svgb-16__step {
    border: 1px solid ButtonBorder;
  }

  .svgb-16[data-state='error'] .svgb-16__mtext {
    color: LinkText;
  }
}

@media (prefers-reduced-motion: reduce) {
  .svgb-16__ink,
    .svgb-16__sink,
    .svgb-16__field {
    transition: none;
  }

  .svgb-16[data-state='error'] .svgb-16__sign {
    animation: none;
  }

  .svgb-16__toggle,
    .svgb-16__toggle svg {
    transition: none;
  }
}
```

## JavaScript
```js
/* aria-disabled keeps the sign-off reachable; the handler declines and explains. */
(function () {
  var root = document.querySelector('.svgb-16');
  if (!root) return;
  var btn = root.querySelector('.svgb-16__sign');
  var field = root.querySelector('.svgb-16__field');
  var text = root.querySelector('.svgb-16__mtext');

  function sync() {
    var ok = field.value.trim().length >= 4;
    btn.setAttribute('aria-disabled', ok ? 'false' : 'true');
    if (ok && root.dataset.state === 'error') {
      root.dataset.state = 'idle';
      field.setAttribute('aria-invalid', 'false');
      text.textContent = 'Prescriber ID accepted. Ready to sign.';
    }
  }

  btn.addEventListener('click', function () {
    if (btn.getAttribute('aria-disabled') === 'true') {
      root.dataset.state = 'error';
      field.setAttribute('aria-invalid', 'true');
      text.textContent = 'Enter your prescriber ID before signing.';
      field.focus();
      return;
    }
    root.dataset.state = 'sent';
    text.textContent = 'Sent to pharmacy queue.';
  });

  field.addEventListener('input', sync);
  sync();
  root.__svgb16Cleanup = function () { field.removeEventListener('input', sync); };
})();
```
