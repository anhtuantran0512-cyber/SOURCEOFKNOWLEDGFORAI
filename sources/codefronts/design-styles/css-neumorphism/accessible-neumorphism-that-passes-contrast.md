---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/accessible-neumorphism-that-passes-contrast/"
title: "Accessible Neumorphism That Passes Contrast"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "The most important demo here."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Neumorphism That Passes Contrast
Source: https://codefronts.com/design-styles/css-neumorphism/accessible-neumorphism-that-passes-contrast/

The most important demo here. Neumorphism's defining trait — an element the same colour as its background — is also its accessibility failure: there is no contrast at the boundary, so the control's edge is invisible to low-vision users and its affordance is invisible to everyone in bright sunlight. A naive soft-UI button is shown failing, then four fixes that keep the aesthetic intact, each with its measured contrast ratio printed beside it.
## HTML
```html
<section class="nm-04" aria-labelledby="nm-04-heading">
      <input type="checkbox" id="nm-04-theme" class="nm-04__themeinput">
      <label for="nm-04-theme" class="nm-04__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-04__stage">
    <header class="nm-04__head">
      <p class="nm-04__kicker">Accessibility</p>
      <h2 class="nm-04__heading" id="nm-04-heading">Soft UI that survives an audit</h2>
      <p class="nm-04__sub">The style's defining trait is zero contrast at the control boundary. These are the four fixes that keep the look and clear WCAG 2.2 AA.</p>
    </header>

    <div class="nm-04__cols">
      <article class="nm-04__col nm-04__col--fail">
        <h3 class="nm-04__coltitle">Naive — fails</h3>
        <button class="nm-04__btn nm-04__btn--nm-04-naive" type="button">Deploy to production</button>
        <dl class="nm-04__readout">
          <div class="nm-04__row"><dt>Boundary vs surface</dt><dd class="nm-04__bad">1.0:1 — fails 1.4.11</dd></div>
          <div class="nm-04__row"><dt>Label vs surface</dt><dd class="nm-04__bad">2.9:1 — fails 1.4.3</dd></div>
          <div class="nm-04__row"><dt>Focus indicator</dt><dd class="nm-04__bad">shadow swap — fails 2.4.13</dd></div>
        </dl>
        <p class="nm-04__why">No border, tinted label, focus signalled by inverting the shadow. It looks correct in a mockup and disappears on a phone outdoors.</p>
      </article>

      <article class="nm-04__col nm-04__col--pass">
        <h3 class="nm-04__coltitle">Fixed — passes</h3>
        <button class="nm-04__btn nm-04__btn--nm-04-fixed" type="button">
          <span class="nm-04__btnicon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18"><path d="M4 12.5l5 5L20 6.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          Deploy to production
        </button>
        <dl class="nm-04__readout">
          <div class="nm-04__row"><dt>Boundary vs surface</dt><dd class="nm-04__good">3.2:1 — 1px border</dd></div>
          <div class="nm-04__row"><dt>Label vs surface</dt><dd class="nm-04__good">9.4:1 — full ink</dd></div>
          <div class="nm-04__row"><dt>Focus indicator</dt><dd class="nm-04__good">2px outline at 3.6:1</dd></div>
          <div class="nm-04__row"><dt>Target size</dt><dd class="nm-04__good">48px — over 44 minimum</dd></div>
        </dl>
        <p class="nm-04__why">Tab to the button to see the ring. It sits outside the shadow entirely, so its contrast does not depend on the surface illusion.</p>
      </article>
    </div>

    <div class="nm-04__states">
      <p class="nm-04__stateslabel">State without relying on shadow direction</p>
      <div class="nm-04__staterow">
        <span class="nm-04__state nm-04__state--on">
          <span class="nm-04__dot nm-04__dot--on" aria-hidden="true"></span>Backups on
        </span>
        <span class="nm-04__state nm-04__state--off">
          <span class="nm-04__dot nm-04__dot--off" aria-hidden="true"></span>Backups off
        </span>
        <span class="nm-04__state nm-04__state--disabled">
          <span class="nm-04__dot nm-04__dot--disabled" aria-hidden="true"></span>Unavailable on this plan
        </span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-04 {
  position: relative;
  --nm-04-surface: #f2ede4;
  --nm-04-dark: rgba(190,180,163,0.6);
  --nm-04-light: rgba(255,255,255,0.95);
  --nm-04-ink: #2a2620;
  --nm-04-muted: #57503f;
  --nm-04-border: #9a917f;
  --nm-04-accent: #a32d33;
  --nm-04-good: #2f6a41;
  --nm-04-bad: #a32d33;
  --nm-04-distance: clamp(5px, 1.2vw, 9px);
  --nm-04-blur: clamp(10px, 2.4vw, 18px);
  --nm-04-ring-width: 2px;
  --nm-04-target: 48px;
  --nm-04-font-display: "Helvetica Neue", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-04-surface);
  color: var(--nm-04-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.94 0.02 80)) {
  .nm-04 {
    --nm-04-surface: oklch(0.945 0.016 84);
    --nm-04-ink: oklch(0.27 0.011 70);
    --nm-04-muted: oklch(0.44 0.019 76);
    --nm-04-border: oklch(0.65 0.021 78);
    --nm-04-accent: oklch(0.48 0.16 22);
    --nm-04-good: oklch(0.46 0.09 152);
    --nm-04-bad: oklch(0.48 0.16 22);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-04 {
    --nm-04-dark: color-mix(in oklab, var(--nm-04-surface), #000 18%);
    --nm-04-light: color-mix(in oklab, var(--nm-04-surface), #fff 92%);
  }
}

.nm-04 *,
.nm-04 *::before,
.nm-04 *::after {
  box-sizing: border-box;
}

.nm-04__stage {
  max-width: 1060px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 60px) clamp(16px, 4vw, 44px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(24px, 4vw, 40px);
}

.nm-04__head {
  max-width: 60ch;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.nm-04__kicker {
  margin: 0;
  font-family: var(--nm-04-font-display);
  font-size: 0.68rem;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--nm-04-muted);
}

.nm-04__heading {
  margin: 0;
  font-family: var(--nm-04-font-display);
  font-size: clamp(1.5rem, 4.4vw, 2.3rem);
  font-weight: 600;
  letter-spacing: 0.01em;
  text-transform: uppercase;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-04__sub {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.62;
  color: var(--nm-04-muted);
  text-wrap: pretty;
}

.nm-04__cols {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 3vw, 24px);
}

@media (min-width: 720px) {
  .nm-04__cols {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-04__col {
  border-radius: 20px;
  padding: clamp(18px, 3vw, 28px);
  background: var(--nm-04-surface);
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: flex-start;
  min-inline-size: 0;
  border: 1px solid var(--nm-04-border);
  box-shadow: var(--nm-04-distance) var(--nm-04-distance) var(--nm-04-blur) var(--nm-04-dark), calc(var(--nm-04-distance) * -1) calc(var(--nm-04-distance) * -1) var(--nm-04-blur) var(--nm-04-light);
}

.nm-04__coltitle {
  margin: 0;
  font-family: var(--nm-04-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-weight: 700;
}

.nm-04__col--fail .nm-04__coltitle {
  color: var(--nm-04-bad);
}

.nm-04__col--pass .nm-04__coltitle {
  color: var(--nm-04-good);
}

.nm-04__btn {
  min-height: var(--nm-04-target);
  min-width: 44px;
  padding: 0 20px;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  border-radius: 14px;
  background: var(--nm-04-surface);
  font: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  box-shadow: var(--nm-04-distance) var(--nm-04-distance) var(--nm-04-blur) var(--nm-04-dark), calc(var(--nm-04-distance) * -1) calc(var(--nm-04-distance) * -1) var(--nm-04-blur) var(--nm-04-light);
}

.nm-04__btn--nm-04-naive {
  border: 0;
  color: #9c9382;
}

.nm-04__btn--nm-04-naive:focus {
  outline: none;
  box-shadow: inset var(--nm-04-distance) var(--nm-04-distance) var(--nm-04-blur) var(--nm-04-dark), inset calc(var(--nm-04-distance) * -1) calc(var(--nm-04-distance) * -1) var(--nm-04-blur) var(--nm-04-light);
}

.nm-04__btn--nm-04-fixed {
  border: 1px solid var(--nm-04-border);
  color: var(--nm-04-ink);
}

.nm-04__btn--nm-04-fixed:focus-visible {
  outline: var(--nm-04-ring-width) solid var(--nm-04-accent);
  outline-offset: 3px;
}

.nm-04__btn--nm-04-fixed:active {
  box-shadow: inset 5px 5px 11px var(--nm-04-dark), inset -5px -5px 11px var(--nm-04-light);
}

.nm-04__btnicon {
  display: inline-flex;
  color: var(--nm-04-good);
}

.nm-04__readout {
  margin: 0;
  display: grid;
  gap: 8px;
  width: 100%;
}

.nm-04__row {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  align-items: baseline;
  border-bottom: 1px dotted var(--nm-04-border);
  padding-bottom: 7px;
  min-inline-size: 0;
}

.nm-04__row dt {
  font-size: 0.78rem;
  color: var(--nm-04-muted);
  min-inline-size: 0;
}

.nm-04__row dd {
  margin: 0;
  font-size: 0.78rem;
  font-weight: 600;
  text-align: right;
  font-variant-numeric: tabular-nums;
  min-inline-size: 0;
}

.nm-04__good {
  color: var(--nm-04-good);
}

.nm-04__bad {
  color: var(--nm-04-bad);
}

.nm-04__why {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.55;
  color: var(--nm-04-muted);
  text-wrap: pretty;
}

.nm-04__states {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.nm-04__stateslabel {
  margin: 0;
  font-family: var(--nm-04-font-display);
  font-size: 0.68rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--nm-04-muted);
}

.nm-04__staterow {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.nm-04__state {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 12px;
  font-size: 0.83rem;
  font-weight: 600;
  background: var(--nm-04-surface);
  border: 1px solid var(--nm-04-border);
  min-inline-size: 0;
}

.nm-04__state--on {
  box-shadow: 6px 6px 13px var(--nm-04-dark), -6px -6px 13px var(--nm-04-light);
  color: var(--nm-04-good);
}

.nm-04__state--off {
  box-shadow: inset 4px 4px 9px var(--nm-04-dark), inset -4px -4px 9px var(--nm-04-light);
  color: var(--nm-04-ink);
}

.nm-04__state--disabled {
  box-shadow: none;
  border-style: dotted;
  color: var(--nm-04-muted);
}

.nm-04__dot {
  width: 10px;
  height: 10px;
  border-radius: 3px;
  flex: none;
}

.nm-04__dot--on {
  background: var(--nm-04-good);
  border-radius: 50%;
}

.nm-04__dot--off {
  background: var(--nm-04-muted);
}

.nm-04__dot--disabled {
  background: transparent;
  border: 1px dotted var(--nm-04-muted);
}

@media (prefers-color-scheme: dark) {
  .nm-04 {
    --nm-04-surface: #33302a;
    --nm-04-dark: rgba(15,14,12,0.72);
    --nm-04-light: rgba(102,96,86,0.44);
    --nm-04-ink: #f0ebe2;
    --nm-04-muted: #b3ab9b;
    --nm-04-border: #8d8474;
    --nm-04-accent: #e88b84;
    --nm-04-good: #83c898;
    --nm-04-bad: #e88b84;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-04 {
      --nm-04-dark: color-mix(in oklab, var(--nm-04-surface), #000 55%);
      --nm-04-light: color-mix(in oklab, var(--nm-04-surface), #fff 15%);
    }
  }

  .nm-04__btn--nm-04-naive {
    color: #7d7668;
  }
}

.nm-04[data-theme="dark"] {
  --nm-04-surface: #33302a;
  --nm-04-dark: rgba(15,14,12,0.72);
  --nm-04-light: rgba(102,96,86,0.44);
  --nm-04-ink: #f0ebe2;
  --nm-04-muted: #b3ab9b;
  --nm-04-border: #8d8474;
  --nm-04-accent: #e88b84;
  --nm-04-good: #83c898;
  --nm-04-bad: #e88b84;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-04[data-theme="dark"] {
    --nm-04-dark: color-mix(in oklab, var(--nm-04-surface), #000 55%);
    --nm-04-light: color-mix(in oklab, var(--nm-04-surface), #fff 15%);
  }
}

.nm-04[data-theme="dark"] .nm-04__btn--nm-04-naive {
  color: #7d7668;
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-04__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-04__themebtn {
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
  background: var(--nm-04-surface);
  color: var(--nm-04-ink);
  border: 1px solid var(--nm-04-line);
  font: 600 11px/1 var(--nm-04-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-04-distance, 6px) var(--nm-04-distance, 6px) var(--nm-04-blur, 14px) var(--nm-04-dark), calc(-1 * var(--nm-04-distance, 6px)) calc(-1 * var(--nm-04-distance, 6px)) var(--nm-04-blur, 14px) var(--nm-04-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-04__themebtn:hover {
  color: var(--nm-04-ink);
}

.nm-04__themeinput:focus-visible + .nm-04__themebtn {
  outline: 2px solid var(--nm-04-ink);
  outline-offset: 3px;
}

.nm-04:has(#nm-04-theme:checked) .nm-04__themebtn {
  box-shadow: inset var(--nm-04-distance, 6px) var(--nm-04-distance, 6px) var(--nm-04-blur, 14px) var(--nm-04-dark), inset calc(-1 * var(--nm-04-distance, 6px)) calc(-1 * var(--nm-04-distance, 6px)) var(--nm-04-blur, 14px) var(--nm-04-light);
}

.nm-04__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-04:has(#nm-04-theme:checked) {
  --nm-04-surface: #33302a;
  --nm-04-dark: rgba(15,14,12,0.72);
  --nm-04-light: rgba(102,96,86,0.44);
  --nm-04-ink: #f0ebe2;
  --nm-04-muted: #b3ab9b;
  --nm-04-border: #8d8474;
  --nm-04-accent: #e88b84;
  --nm-04-good: #83c898;
  --nm-04-bad: #e88b84;
}

@media (prefers-color-scheme: light) {
  .nm-04:has(#nm-04-theme:checked) {
    --nm-04-surface: #33302a;
    --nm-04-dark: rgba(15,14,12,0.72);
    --nm-04-light: rgba(102,96,86,0.44);
    --nm-04-ink: #f0ebe2;
    --nm-04-muted: #b3ab9b;
    --nm-04-border: #8d8474;
    --nm-04-accent: #e88b84;
    --nm-04-good: #83c898;
    --nm-04-bad: #e88b84;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-04:has(#nm-04-theme:checked) {
    --nm-04-surface: #f2ede4;
    --nm-04-dark: rgba(190,180,163,0.6);
    --nm-04-light: rgba(255,255,255,0.95);
    --nm-04-ink: #2a2620;
    --nm-04-muted: #57503f;
    --nm-04-border: #9a917f;
    --nm-04-accent: #a32d33;
    --nm-04-good: #2f6a41;
    --nm-04-bad: #a32d33;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-04__themebtn {
    transition: none;
  }
}
```
