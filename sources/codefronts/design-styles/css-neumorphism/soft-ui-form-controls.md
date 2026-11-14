---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/soft-ui-form-controls/"
title: "Soft UI Toggle Switch and Checkbox"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Switches, checkboxes and radios in soft UI, built on real form inputs rather than divs."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Soft UI Toggle Switch and Checkbox
Source: https://codefronts.com/design-styles/css-neumorphism/soft-ui-form-controls/

Switches, checkboxes and radios in soft UI, built on real form inputs rather than divs. The track is an inset well, the knob is a raised puck, and the on state changes colour and position and label — never depth alone. Keyboard focus, disabled and indeterminate states are all handled, and the whole set works with the native input hidden but still reachable.
## HTML
```html
<section class="nm-08" aria-labelledby="nm-08-heading">
      <input type="checkbox" id="nm-08-theme" class="nm-08__themeinput">
      <label for="nm-08-theme" class="nm-08__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-08__stage">
    <header class="nm-08__head">
      <p class="nm-08__kicker">Form controls</p>
      <h2 class="nm-08__heading" id="nm-08-heading">Switches built on real inputs</h2>
      <p class="nm-08__sub">Inset track, raised knob, and an on state that changes colour, position and shape — not just shadow direction.</p>
    </header>

    <div class="nm-08__panel">
      <div class="nm-08__row">
        <input class="nm-08__input" type="checkbox" id="nm-08-sw1" checked>
        <label class="nm-08__label" for="nm-08-sw1">
          <span class="nm-08__track"><span class="nm-08__knob"></span></span>
          <span class="nm-08__text"><b>Nightly backups</b><em>Runs at 03:00 in your local time</em></span>
        </label>
      </div>
      <div class="nm-08__row">
        <input class="nm-08__input" type="checkbox" id="nm-08-sw2">
        <label class="nm-08__label" for="nm-08-sw2">
          <span class="nm-08__track"><span class="nm-08__knob"></span></span>
          <span class="nm-08__text"><b>Share usage analytics</b><em>Anonymised, aggregated weekly</em></span>
        </label>
      </div>
      <div class="nm-08__row">
        <input class="nm-08__input" type="checkbox" id="nm-08-sw3" disabled>
        <label class="nm-08__label" for="nm-08-sw3">
          <span class="nm-08__track"><span class="nm-08__knob"></span></span>
          <span class="nm-08__text"><b>Priority sync</b><em>Not available on the Solo plan</em></span>
        </label>
      </div>
    </div>

    <div class="nm-08__panel nm-08__panel--boxes">
      <div class="nm-08__check">
        <input class="nm-08__input" type="checkbox" id="nm-08-cb1" checked>
        <label class="nm-08__clabel" for="nm-08-cb1">
          <span class="nm-08__box">
            <svg viewBox="0 0 20 20" width="13" height="13" aria-hidden="true"><path d="M4 10.5l4 4 8-9" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          Compress before upload
        </label>
      </div>
      <div class="nm-08__check">
        <input class="nm-08__input" type="checkbox" id="nm-08-cb2">
        <label class="nm-08__clabel" for="nm-08-cb2">
          <span class="nm-08__box">
            <svg viewBox="0 0 20 20" width="13" height="13" aria-hidden="true"><path d="M4 10.5l4 4 8-9" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          Keep original filenames
        </label>
      </div>
      <div class="nm-08__check">
        <input class="nm-08__input" type="radio" name="nm-08-plan" id="nm-08-r1" checked>
        <label class="nm-08__clabel" for="nm-08-r1"><span class="nm-08__box nm-08__box--radio"><span class="nm-08__pip"></span></span>Weekly digest</label>
      </div>
      <div class="nm-08__check">
        <input class="nm-08__input" type="radio" name="nm-08-plan" id="nm-08-r2">
        <label class="nm-08__clabel" for="nm-08-r2"><span class="nm-08__box nm-08__box--radio"><span class="nm-08__pip"></span></span>Immediate alerts</label>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-08 {
  position: relative;
  --nm-08-surface: #e4e9ee;
  --nm-08-dark: rgba(166,177,190,0.62);
  --nm-08-light: rgba(255,255,255,0.94);
  --nm-08-ink: #232a33;
  --nm-08-muted: #59616d;
  --nm-08-border: #98a1ad;
  --nm-08-on: #2f7f6f;
  --nm-08-track-w: 62px;
  --nm-08-track-h: 32px;
  --nm-08-knob: 24px;
  --nm-08-knob-lift: 4px;
  --nm-08-speed: 200ms;
  --nm-08-font-display: "Inter Tight", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-08-surface);
  color: var(--nm-08-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 240)) {
  .nm-08 {
    --nm-08-surface: oklch(0.921 0.011 240);
    --nm-08-ink: oklch(0.27 0.019 250);
    --nm-08-muted: oklch(0.47 0.02 250);
    --nm-08-border: oklch(0.66 0.021 246);
    --nm-08-on: oklch(0.52 0.084 178);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-08 {
    --nm-08-dark: color-mix(in oklab, var(--nm-08-surface), #000 19%);
    --nm-08-light: color-mix(in oklab, var(--nm-08-surface), #fff 92%);
  }
}

.nm-08 *,
.nm-08 *::before,
.nm-08 *::after {
  box-sizing: border-box;
}

.nm-08__stage {
  max-width: 780px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 58px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(20px, 3.2vw, 30px);
}

.nm-08__head {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-08__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-08-muted);
}

.nm-08__heading {
  margin: 0;
  font-family: var(--nm-08-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 650;
  letter-spacing: -0.025em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-08__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-08-muted);
  text-wrap: pretty;
}

.nm-08__panel {
  border-radius: 22px;
  padding: clamp(16px, 3vw, 26px);
  background: var(--nm-08-surface);
  border: 1px solid var(--nm-08-border);
  display: flex;
  flex-direction: column;
  gap: 6px;
  box-shadow: 9px 9px 18px var(--nm-08-dark), -9px -9px 18px var(--nm-08-light);
}

.nm-08__panel--boxes {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
}

@media (min-width: 560px) {
  .nm-08__panel--boxes {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-08__row,
.nm-08__check {
  position: relative;
  min-inline-size: 0;
}

.nm-08__input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.nm-08__label {
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: 56px;
  padding: 6px 2px;
  cursor: pointer;
  min-inline-size: 0;
}

.nm-08__track {
  flex: none;
  position: relative;
  width: var(--nm-08-track-w);
  height: var(--nm-08-track-h);
  border-radius: 999px;
  background: var(--nm-08-surface);
  box-shadow: inset 4px 4px 8px var(--nm-08-dark), inset -4px -4px 8px var(--nm-08-light);
  transition: background-color var(--nm-08-speed) ease;
}

.nm-08__knob {
  position: absolute;
  top: 50%;
  left: 4px;
  width: var(--nm-08-knob);
  height: var(--nm-08-knob);
  margin-top: calc(var(--nm-08-knob) / -2);
  border-radius: 50%;
  background: var(--nm-08-surface);
  border: 1px solid var(--nm-08-border);
  box-shadow: var(--nm-08-knob-lift) var(--nm-08-knob-lift) 8px var(--nm-08-dark), calc(var(--nm-08-knob-lift) * -1) calc(var(--nm-08-knob-lift) * -1) 8px var(--nm-08-light);
  transition: transform var(--nm-08-speed) cubic-bezier(0.3, 1.3, 0.5, 1);
}

.nm-08__input:checked + .nm-08__label .nm-08__track {
  background: var(--nm-08-on);
  box-shadow: inset 4px 4px 8px rgba(0,0,0,0.25), inset -3px -3px 7px rgba(255,255,255,0.2);
}

.nm-08__input:checked + .nm-08__label .nm-08__knob {
  transform: translateX(calc(var(--nm-08-track-w) - var(--nm-08-knob) - 8px));
}

.nm-08__input:focus-visible + .nm-08__label .nm-08__track {
  outline: 2px solid var(--nm-08-on);
  outline-offset: 3px;
}

.nm-08__input:disabled + .nm-08__label {
  cursor: not-allowed;
}

.nm-08__input:disabled + .nm-08__label .nm-08__track {
  box-shadow: none;
  border: 1px dotted var(--nm-08-border);
}

.nm-08__input:disabled + .nm-08__label .nm-08__knob {
  box-shadow: none;
  border-style: dotted;
}

.nm-08__input:disabled + .nm-08__label .nm-08__text em {
  color: var(--nm-08-muted);
}

.nm-08__text {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-inline-size: 0;
}

.nm-08__text b {
  font-family: var(--nm-08-font-display);
  font-size: 0.94rem;
  font-weight: 600;
}

.nm-08__text em {
  font-style: normal;
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--nm-08-muted);
}

.nm-08__clabel {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 48px;
  padding: 4px 2px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  min-inline-size: 0;
}

.nm-08__box {
  flex: none;
  width: 26px;
  height: 26px;
  display: grid;
  place-items: center;
  border-radius: 8px;
  border: 1px solid var(--nm-08-border);
  background: var(--nm-08-surface);
  color: transparent;
  box-shadow: inset 3px 3px 6px var(--nm-08-dark), inset -3px -3px 6px var(--nm-08-light);
  transition: color var(--nm-08-speed) ease, background-color var(--nm-08-speed) ease;
}

.nm-08__box--radio {
  border-radius: 50%;
}

.nm-08__pip {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: transparent;
  transition: background-color var(--nm-08-speed) ease, transform var(--nm-08-speed) ease;
  transform: scale(0.4);
}

.nm-08__input:checked + .nm-08__clabel .nm-08__box {
  color: #fff;
  background: var(--nm-08-on);
  border-color: var(--nm-08-on);
  box-shadow: 4px 4px 9px var(--nm-08-dark), -4px -4px 9px var(--nm-08-light);
}

.nm-08__input:checked + .nm-08__clabel .nm-08__pip {
  background: #fff;
  transform: scale(1);
}

.nm-08__input:focus-visible + .nm-08__clabel .nm-08__box {
  outline: 2px solid var(--nm-08-on);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .nm-08__knob,
    .nm-08__box,
    .nm-08__pip,
    .nm-08__track {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-08 {
    --nm-08-surface: #272c33;
    --nm-08-dark: rgba(11,13,16,0.72);
    --nm-08-light: rgba(88,96,108,0.44);
    --nm-08-ink: #e6eaf0;
    --nm-08-muted: #9ba4b0;
    --nm-08-border: #869;
    --nm-08-border: #868f9c;
    --nm-08-on: #62c4ae;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-08 {
      --nm-08-dark: color-mix(in oklab, var(--nm-08-surface), #000 55%);
      --nm-08-light: color-mix(in oklab, var(--nm-08-surface), #fff 14%);
    }
  }

  .nm-08__input:checked + .nm-08__clabel .nm-08__box {
    color: #14201d;
  }
}

.nm-08[data-theme="dark"] {
  --nm-08-surface: #272c33;
  --nm-08-dark: rgba(11,13,16,0.72);
  --nm-08-light: rgba(88,96,108,0.44);
  --nm-08-ink: #e6eaf0;
  --nm-08-muted: #9ba4b0;
  --nm-08-border: #868f9c;
  --nm-08-on: #62c4ae;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-08[data-theme="dark"] {
    --nm-08-dark: color-mix(in oklab, var(--nm-08-surface), #000 55%);
    --nm-08-light: color-mix(in oklab, var(--nm-08-surface), #fff 14%);
  }
}

.nm-08[data-theme="dark"] .nm-08__input:checked + .nm-08__clabel .nm-08__box {
  color: #14201d;
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-08__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-08__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-08-surface);
  color: var(--nm-08-ink);
  border: 1px solid var(--nm-08-line);
  font: 600 11px/1 var(--nm-08-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-08-distance, 6px) var(--nm-08-distance, 6px) var(--nm-08-blur, 14px) var(--nm-08-dark), calc(-1 * var(--nm-08-distance, 6px)) calc(-1 * var(--nm-08-distance, 6px)) var(--nm-08-blur, 14px) var(--nm-08-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-08__themebtn:hover {
  color: var(--nm-08-ink);
}

.nm-08__themeinput:focus-visible + .nm-08__themebtn {
  outline: 2px solid var(--nm-08-ink);
  outline-offset: 3px;
}

.nm-08:has(#nm-08-theme:checked) .nm-08__themebtn {
  box-shadow: inset var(--nm-08-distance, 6px) var(--nm-08-distance, 6px) var(--nm-08-blur, 14px) var(--nm-08-dark), inset calc(-1 * var(--nm-08-distance, 6px)) calc(-1 * var(--nm-08-distance, 6px)) var(--nm-08-blur, 14px) var(--nm-08-light);
}

.nm-08__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-08:has(#nm-08-theme:checked) {
  --nm-08-surface: #272c33;
  --nm-08-dark: rgba(11,13,16,0.72);
  --nm-08-light: rgba(88,96,108,0.44);
  --nm-08-ink: #e6eaf0;
  --nm-08-muted: #9ba4b0;
  --nm-08-border: #868f9c;
  --nm-08-on: #62c4ae;
}

@media (prefers-color-scheme: light) {
  .nm-08:has(#nm-08-theme:checked) {
    --nm-08-surface: #272c33;
    --nm-08-dark: rgba(11,13,16,0.72);
    --nm-08-light: rgba(88,96,108,0.44);
    --nm-08-ink: #e6eaf0;
    --nm-08-muted: #9ba4b0;
    --nm-08-border: #868f9c;
    --nm-08-on: #62c4ae;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-08:has(#nm-08-theme:checked) {
    --nm-08-surface: #e4e9ee;
    --nm-08-dark: rgba(166,177,190,0.62);
    --nm-08-light: rgba(255,255,255,0.94);
    --nm-08-ink: #232a33;
    --nm-08-muted: #59616d;
    --nm-08-border: #98a1ad;
    --nm-08-on: #2f7f6f;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-08__themebtn {
    transition: none;
  }
}
```
