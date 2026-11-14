---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/focus-visible-stroke-outline-for-keyboard-users/"
title: "Focus Visible Stroke Outline for Keyboard Users"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A payment confirmation screen with its tab order made visible: every focusable control carries its stop number, and as focus lands the drawn stroke arrives…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Focus Visible Stroke Outline for Keyboard Users
Source: https://codefronts.com/components/css-svg-stroke-buttons/focus-visible-stroke-outline-for-keyboard-users/

A payment confirmation screen with its tab order made visible: every focusable control carries its stop number, and as focus lands the drawn stroke arrives on top of a real two-tone outline that is never animated. Press Tab in the preview — nothing here relies on the animation to tell you where you are, which is the whole point of the pattern.
## HTML
```html
<section class="svgb-09">
  <input class="svgb-09__ti" type="checkbox" id="svgb-09-theme">
  <label class="svgb-09__toggle" for="svgb-09-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-09__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-09__stage">
    <div class="svgb-09__sheet">
      <div class="svgb-09__top">
        <span class="svgb-09__brand">Meridian</span>
        <span class="svgb-09__hint"><kbd class="svgb-09__kbd">Tab</kbd> walks the order</span>
      </div>
      <p class="svgb-09__amount">&pound;1,480.00</p>
      <p class="svgb-09__to">to <strong>Halden Studio Ltd</strong> &middot; sort 20-45-11 &middot; acct &bull;&bull;&bull;&bull;8842</p>

      <ol class="svgb-09__list">
        <li class="svgb-09__li">
          <span class="svgb-09__step" aria-hidden="true">1</span>
          <button class="svgb-09__btn svgb-09__btn--primary" type="button">
            <svg class="svgb-09__frame" viewBox="0 0 340 60" aria-hidden="true">
              <rect class="svgb-09__base" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
              <rect class="svgb-09__ink" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
            </svg>
            <span class="svgb-09__label">Confirm payment</span>
          </button>
        </li>
        <li class="svgb-09__li">
          <span class="svgb-09__step" aria-hidden="true">2</span>
          <button class="svgb-09__btn" type="button">
            <svg class="svgb-09__frame" viewBox="0 0 340 60" aria-hidden="true">
              <rect class="svgb-09__base" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
              <rect class="svgb-09__ink" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
            </svg>
            <span class="svgb-09__label">Schedule for 1 October</span>
          </button>
        </li>
        <li class="svgb-09__li">
          <span class="svgb-09__step" aria-hidden="true">3</span>
          <button class="svgb-09__btn" type="button">
            <svg class="svgb-09__frame" viewBox="0 0 340 60" aria-hidden="true">
              <rect class="svgb-09__base" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
              <rect class="svgb-09__ink" x="1.5" y="1.5" width="337" height="57" rx="8" vector-effect="non-scaling-stroke"/>
            </svg>
            <span class="svgb-09__label">Edit reference</span>
          </button>
        </li>
        <li class="svgb-09__li">
          <span class="svgb-09__step" aria-hidden="true">4</span>
          <a class="svgb-09__link" href="#svgb-09-terms">Payment limits and cut-off times</a>
        </li>
      </ol>

      <div class="svgb-09__foot">
        <span class="svgb-09__pair"><span class="svgb-09__sw svgb-09__sw--h"></span>hover &middot; 2px stroke only</span>
        <span class="svgb-09__pair"><span class="svgb-09__sw svgb-09__sw--f"></span>focus-visible &middot; outline + stroke</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap');

.svgb-09 {
  --svgb-09-bg: #eceef2;
  --svgb-09-bg: oklch(0.945 0.005 265);
  --svgb-09-fg: #0e1116;
  --svgb-09-fg: oklch(0.175 0.008 265);
  --svgb-09-muted: #545a66;
  --svgb-09-muted: oklch(0.485 0.013 265);
  --svgb-09-card: #ffffff;
  --svgb-09-card: oklch(1 0 0);
  --svgb-09-rest: rgba(14, 17, 22, 0.18);
  --svgb-09-rest: oklch(0.175 0.008 265 / 0.18);
  --svgb-09-stroke: #0b5cd6;
  --svgb-09-stroke: oklch(0.47 0.20 260);
  --svgb-09-ring: #0b0e14;
  --svgb-09-ring: oklch(0.17 0.01 265);
  --svgb-09-ring2: #ffffff;
  --svgb-09-ring2: oklch(1 0 0);
  --svgb-09-peri: 780;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-09-bg);
  position: relative;
  color: var(--svgb-09-fg);
  font-family: 'Public Sans', system-ui, sans-serif;
}

.svgb-09 *,
.svgb-09 *::before,
.svgb-09 *::after {
  box-sizing: border-box;
}

.svgb-09__stage {
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px, 5vw, 64px);
}

.svgb-09__sheet {
  width: 100%;
  max-width: 560px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: clamp(22px, 4vw, 40px);
  border-radius: 10px;
  background: var(--svgb-09-card);
  border: 1px solid var(--svgb-09-rest);
}

.svgb-09__top {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
  flex-wrap: wrap;
}

.svgb-09__brand {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.svgb-09__hint {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  color: var(--svgb-09-muted);
}

.svgb-09__kbd {
  font-family: inherit;
  font-size: 10.5px;
  padding: 4px 8px;
  border-radius: 5px;
  border: 1px solid var(--svgb-09-rest);
  box-shadow: 0 1.5px 0 var(--svgb-09-rest);
}

.svgb-09__amount {
  margin: 8px 0 0;
  font-size: clamp(34px, 6vw, 52px);
  font-weight: 700;
  letter-spacing: -0.03em;
  font-variant-numeric: tabular-nums;
}

.svgb-09__to {
  margin: 0 0 10px;
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--svgb-09-muted);
}

.svgb-09__to strong {
  color: var(--svgb-09-fg);
  font-weight: 600;
}

.svgb-09__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.svgb-09__li {
  display: flex;
  align-items: center;
  gap: 14px;
}

.svgb-09__step {
  flex: none;
  inline-size: 22px;
  block-size: 22px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  border: 1px solid var(--svgb-09-rest);
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  color: var(--svgb-09-muted);
}

.svgb-09__btn {
  position: relative;
  inline-size: min(340px, 100%);
  block-size: 60px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 8px;
  background: color-mix(in oklab, var(--svgb-09-fg) 3.5%, transparent);
  color: inherit;
  font: inherit;
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-09__btn--primary {
  background: color-mix(in oklab, var(--svgb-09-stroke) 12%, transparent);
  font-weight: 600;
}

.svgb-09__label {
  position: relative;
  z-index: 1;
}

.svgb-09__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-09__frame rect {
  fill: none;
  stroke-linecap: round;
}

.svgb-09__base {
  stroke: var(--svgb-09-rest);
  stroke-width: 1.4px;
}

.svgb-09__ink {
  stroke: var(--svgb-09-stroke);
  stroke-width: 2px;
  stroke-dasharray: var(--svgb-09-peri);
  stroke-dashoffset: var(--svgb-09-peri);
  transition: stroke-dashoffset 560ms cubic-bezier(0.22, 1, 0.36, 1), stroke-width 160ms ease;
}

.svgb-09__btn:hover .svgb-09__ink {
  stroke-dashoffset: 0;
}

.svgb-09__btn:focus-visible .svgb-09__ink {
  stroke-dashoffset: 0;
  stroke-width: 2.8px;
  transition-duration: 240ms;
}

.svgb-09__btn:focus-visible,
.svgb-09__link:focus-visible {
  outline: 2px solid var(--svgb-09-ring);
  outline-offset: 3px;
  box-shadow: 0 0 0 5px var(--svgb-09-ring2);
}

.svgb-09__btn:focus:not(:focus-visible) {
  outline: none;
  box-shadow: none;
}

.svgb-09__link {
  color: var(--svgb-09-stroke);
  font-size: 14px;
  font-weight: 500;
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
  border-radius: 4px;
}

.svgb-09__link:hover {
  text-decoration-thickness: 2px;
}

.svgb-09__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  padding-block-start: 14px;
  margin-block-start: 4px;
  border-block-start: 1px solid var(--svgb-09-rest);
}

.svgb-09__pair {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  color: var(--svgb-09-muted);
}

.svgb-09__sw {
  inline-size: 22px;
  block-size: 12px;
  border-radius: 3px;
}

.svgb-09__sw--h {
  border: 2px solid var(--svgb-09-stroke);
}

.svgb-09__sw--f {
  border: 2px solid var(--svgb-09-stroke);
  outline: 2px solid var(--svgb-09-ring);
  outline-offset: 2px;
}

.svgb-09__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-09__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 8px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 6%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-09__toggle:hover {
  background: color-mix(in oklab, currentColor 13%, transparent);
}

.svgb-09__toggle:active {
  transform: scale(0.94);
}

.svgb-09__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-09__ti:checked + .svgb-09__toggle svg {
  transform: rotate(180deg);
}

.svgb-09__ti:focus-visible + .svgb-09__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-09__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-09:has(#svgb-09-theme:checked) {
  --svgb-09-bg: #0c0f14;
  --svgb-09-bg: oklch(0.17 0.008 265);
  --svgb-09-fg: #edeff4;
  --svgb-09-fg: oklch(0.955 0.005 265);
  --svgb-09-muted: #8b91a0;
  --svgb-09-muted: oklch(0.67 0.013 265);
  --svgb-09-card: #14171e;
  --svgb-09-card: oklch(0.215 0.01 265);
  --svgb-09-rest: rgba(237, 239, 244, 0.18);
  --svgb-09-rest: oklch(0.955 0.005 265 / 0.18);
  --svgb-09-stroke: #7fb2ff;
  --svgb-09-stroke: oklch(0.78 0.13 260);
  --svgb-09-ring: #ffffff;
  --svgb-09-ring: oklch(1 0 0);
  --svgb-09-ring2: #00080f;
  --svgb-09-ring2: oklch(0.14 0.02 250);
}

@media (forced-colors: active) {
  .svgb-09__ink {
    stroke: transparent;
  }

  .svgb-09__btn {
    border: 1px solid ButtonBorder;
  }

  .svgb-09__btn:focus-visible,
    .svgb-09__link:focus-visible {
    outline: 3px solid Highlight;
    outline-offset: 3px;
    box-shadow: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .svgb-09__ink {
    transition: none;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-09__btn:hover .svgb-09__ink,
    .svgb-09__btn:focus-visible .svgb-09__ink {
    opacity: 1;
  }

  .svgb-09__toggle,
    .svgb-09__toggle svg {
    transition: none;
  }
}
```
