---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/soft-ui-button-lab/"
title: "Soft UI Button Set with Press Feedback"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "A complete button family in soft UI: primary, secondary, ghost, icon-only and destructive, each at three sizes, each with rest, hover, active, focus and…"
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Soft UI Button Set with Press Feedback
Source: https://codefronts.com/design-styles/css-neumorphism/soft-ui-button-lab/

A complete button family in soft UI: primary, secondary, ghost, icon-only and destructive, each at three sizes, each with rest, hover, active, focus and disabled worked out. The press uses a shallow lift on hover and a genuine inset on active, so the control feels like it travels. Every variant carries a boundary border and a real focus ring, because a button nobody can find is not a button.
## HTML
```html
<section class="nm-05" aria-labelledby="nm-05-heading">
      <input type="checkbox" id="nm-05-theme" class="nm-05__themeinput">
      <label for="nm-05-theme" class="nm-05__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-05__stage">
    <header class="nm-05__head">
      <p class="nm-05__kicker">Component · buttons</p>
      <h2 class="nm-05__heading" id="nm-05-heading">A button family that travels</h2>
      <p class="nm-05__sub">Rest, hover, active, focus, disabled — worked out once on a base class, then tinted per variant.</p>
    </header>

    <div class="nm-05__row">
      <button class="nm-05__btn nm-05__btn--nm-05-primary" type="button">Save changes</button>
      <button class="nm-05__btn" type="button">Preview</button>
      <button class="nm-05__btn nm-05__btn--nm-05-ghost" type="button">Cancel</button>
      <button class="nm-05__btn nm-05__btn--danger" type="button">Delete draft</button>
      <button class="nm-05__btn" type="button" disabled>Publishing…</button>
    </div>

    <div class="nm-05__row">
      <button class="nm-05__btn nm-05__btn--sm" type="button">Small</button>
      <button class="nm-05__btn" type="button">Medium</button>
      <button class="nm-05__btn nm-05__btn--lg" type="button">Large</button>
    </div>

    <div class="nm-05__row">
      <button class="nm-05__icon" type="button" aria-label="Previous track">
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M17 5 8 12l9 7V5zM7 5v14" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
      </button>
      <button class="nm-05__icon nm-05__icon--nm-05-primary" type="button" aria-label="Play">
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M8 5.5 19 12 8 18.5v-13z" fill="currentColor"/></svg>
      </button>
      <button class="nm-05__icon" type="button" aria-label="Next track">
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M7 5l9 7-9 7V5zM17 5v14" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
      </button>
      <button class="nm-05__icon" type="button" aria-label="Shuffle">
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 6h4l8 12h4M4 18h4l2-3M15 7l3-1-1 3M15 17l3 1-1-3" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </div>

    <p class="nm-05__foot">Press and hold any button — the surface inverts to inset and the label drops 1px, so the press survives greyscale and forced-colors mode.</p>
  </div>
</section>
```
## CSS
```css
.nm-05 {
  position: relative;
  --nm-05-surface: #e7e4ef;
  --nm-05-dark: rgba(171,166,190,0.6);
  --nm-05-light: rgba(255,255,255,0.94);
  --nm-05-ink: #2b2836;
  --nm-05-muted: #5d5872;
  --nm-05-border: #9c96b0;
  --nm-05-primary: #6f5bd0;
  --nm-05-danger: #a83a52;
  --nm-05-scale: 1;
  --nm-05-dist: calc(7px * var(--nm-05-scale));
  --nm-05-blur: calc(15px * var(--nm-05-scale));
  --nm-05-lift: 1.45;
  --nm-05-press: 5px;
  --nm-05-radius: 15px;
  --nm-05-font-display: "Avenir Next", "Futura", "Century Gothic", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-05-surface);
  color: var(--nm-05-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.02 300)) {
  .nm-05 {
    --nm-05-surface: oklch(0.911 0.017 300);
    --nm-05-ink: oklch(0.30 0.026 302);
    --nm-05-muted: oklch(0.49 0.032 302);
    --nm-05-border: oklch(0.66 0.028 300);
    --nm-05-primary: oklch(0.52 0.16 292);
    --nm-05-danger: oklch(0.48 0.14 12);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-05 {
    --nm-05-dark: color-mix(in oklab, var(--nm-05-surface), #000 20%);
    --nm-05-light: color-mix(in oklab, var(--nm-05-surface), #fff 90%);
  }
}

.nm-05 *,
.nm-05 *::before,
.nm-05 *::after {
  box-sizing: border-box;
}

.nm-05__stage {
  max-width: 900px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 60px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(20px, 3.4vw, 32px);
}

.nm-05__head {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-05__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--nm-05-muted);
}

.nm-05__heading {
  margin: 0;
  font-family: var(--nm-05-font-display);
  font-size: clamp(1.55rem, 4.4vw, 2.35rem);
  font-weight: 600;
  letter-spacing: -0.015em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-05__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-05-muted);
  text-wrap: pretty;
}

.nm-05__row {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(12px, 2vw, 18px);
  align-items: center;
}

.nm-05__btn {
  min-height: calc(46px * var(--nm-05-scale));
  min-width: 44px;
  padding: 0 calc(22px * var(--nm-05-scale));
  border-radius: var(--nm-05-radius);
  border: 1px solid var(--nm-05-border);
  background: var(--nm-05-surface);
  color: var(--nm-05-ink);
  font: inherit;
  font-family: var(--nm-05-font-display);
  font-size: calc(0.9rem * var(--nm-05-scale));
  font-weight: 600;
  cursor: pointer;
  box-shadow: var(--nm-05-dist) var(--nm-05-dist) var(--nm-05-blur) var(--nm-05-dark), calc(var(--nm-05-dist) * -1) calc(var(--nm-05-dist) * -1) var(--nm-05-blur) var(--nm-05-light);
  transition: box-shadow 170ms ease, transform 120ms ease, color 170ms ease;
}

.nm-05__btn:hover:not(:disabled) {
  box-shadow: calc(var(--nm-05-dist) * var(--nm-05-lift)) calc(var(--nm-05-dist) * var(--nm-05-lift)) calc(var(--nm-05-blur) * var(--nm-05-lift)) var(--nm-05-dark), calc(var(--nm-05-dist) * var(--nm-05-lift) * -1) calc(var(--nm-05-dist) * var(--nm-05-lift) * -1) calc(var(--nm-05-blur) * var(--nm-05-lift)) var(--nm-05-light);
}

.nm-05__btn:active:not(:disabled) {
  transform: translateY(1px);
  box-shadow: inset var(--nm-05-press) var(--nm-05-press) calc(var(--nm-05-blur) * 0.75) var(--nm-05-dark), inset calc(var(--nm-05-press) * -1) calc(var(--nm-05-press) * -1) calc(var(--nm-05-blur) * 0.75) var(--nm-05-light);
}

.nm-05__btn:focus-visible {
  outline: 2px solid var(--nm-05-primary);
  outline-offset: 3px;
}

.nm-05__btn:disabled {
  box-shadow: none;
  border-style: dotted;
  color: var(--nm-05-muted);
  cursor: not-allowed;
}

.nm-05__btn--sm {
  --nm-05-scale: 0.82;
}

.nm-05__btn--lg {
  --nm-05-scale: 1.22;
}

.nm-05__btn--nm-05-primary {
  color: #fff;
  border-color: var(--nm-05-primary);
  background: var(--nm-05-primary);
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-05__btn--nm-05-primary {
    box-shadow: var(--nm-05-dist) var(--nm-05-dist) var(--nm-05-blur) color-mix(in oklab, var(--nm-05-primary), #000 30%), calc(var(--nm-05-dist) * -1) calc(var(--nm-05-dist) * -1) var(--nm-05-blur) color-mix(in oklab, var(--nm-05-primary), #fff 42%);
  }

  .nm-05__btn--nm-05-primary:hover {
    box-shadow: calc(var(--nm-05-dist) * var(--nm-05-lift)) calc(var(--nm-05-dist) * var(--nm-05-lift)) calc(var(--nm-05-blur) * var(--nm-05-lift)) color-mix(in oklab, var(--nm-05-primary), #000 30%), calc(var(--nm-05-dist) * var(--nm-05-lift) * -1) calc(var(--nm-05-dist) * var(--nm-05-lift) * -1) calc(var(--nm-05-blur) * var(--nm-05-lift)) color-mix(in oklab, var(--nm-05-primary), #fff 42%);
  }

  .nm-05__btn--nm-05-primary:active {
    box-shadow: inset var(--nm-05-press) var(--nm-05-press) 11px color-mix(in oklab, var(--nm-05-primary), #000 34%), inset calc(var(--nm-05-press) * -1) calc(var(--nm-05-press) * -1) 11px color-mix(in oklab, var(--nm-05-primary), #fff 34%);
  }
}

.nm-05__btn--nm-05-ghost {
  box-shadow: inset 3px 3px 7px var(--nm-05-dark), inset -3px -3px 7px var(--nm-05-light);
  color: var(--nm-05-muted);
}

.nm-05__btn--nm-05-ghost:hover {
  color: var(--nm-05-ink);
  box-shadow: inset 4px 4px 9px var(--nm-05-dark), inset -4px -4px 9px var(--nm-05-light);
}

.nm-05__btn--danger {
  color: var(--nm-05-danger);
  border-color: var(--nm-05-danger);
}

.nm-05__icon {
  width: 52px;
  height: 52px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  border: 1px solid var(--nm-05-border);
  background: var(--nm-05-surface);
  color: var(--nm-05-ink);
  cursor: pointer;
  box-shadow: var(--nm-05-dist) var(--nm-05-dist) var(--nm-05-blur) var(--nm-05-dark), calc(var(--nm-05-dist) * -1) calc(var(--nm-05-dist) * -1) var(--nm-05-blur) var(--nm-05-light);
  transition: box-shadow 170ms ease, color 170ms ease;
}

.nm-05__icon:hover {
  color: var(--nm-05-primary);
}

.nm-05__icon:active {
  box-shadow: inset var(--nm-05-press) var(--nm-05-press) 11px var(--nm-05-dark), inset calc(var(--nm-05-press) * -1) calc(var(--nm-05-press) * -1) 11px var(--nm-05-light);
}

.nm-05__icon:focus-visible {
  outline: 2px solid var(--nm-05-primary);
  outline-offset: 3px;
}

.nm-05__icon--nm-05-primary {
  width: 62px;
  height: 62px;
  color: var(--nm-05-primary);
}

.nm-05__foot {
  margin: 0;
  max-width: 66ch;
  font-size: 0.84rem;
  line-height: 1.6;
  color: var(--nm-05-muted);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .nm-05__btn,
    .nm-05__icon {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-05 {
    --nm-05-surface: #2c2a35;
    --nm-05-dark: rgba(12,11,16,0.7);
    --nm-05-light: rgba(92,88,110,0.46);
    --nm-05-ink: #e8e5f0;
    --nm-05-muted: #a6a0ba;
    --nm-05-border: #8d87a2;
    --nm-05-primary: #a08ff0;
    --nm-05-danger: #e88ba0;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-05 {
      --nm-05-dark: color-mix(in oklab, var(--nm-05-surface), #000 55%);
      --nm-05-light: color-mix(in oklab, var(--nm-05-surface), #fff 14%);
    }
  }

  .nm-05__btn--nm-05-primary {
    color: #1b1926;
  }
}

.nm-05[data-theme="dark"] {
  --nm-05-surface: #2c2a35;
  --nm-05-dark: rgba(12,11,16,0.7);
  --nm-05-light: rgba(92,88,110,0.46);
  --nm-05-ink: #e8e5f0;
  --nm-05-muted: #a6a0ba;
  --nm-05-border: #8d87a2;
  --nm-05-primary: #a08ff0;
  --nm-05-danger: #e88ba0;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-05[data-theme="dark"] {
    --nm-05-dark: color-mix(in oklab, var(--nm-05-surface), #000 55%);
    --nm-05-light: color-mix(in oklab, var(--nm-05-surface), #fff 14%);
  }
}

.nm-05[data-theme="dark"] .nm-05__btn--nm-05-primary {
  color: #1b1926;
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-05__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-05__themebtn {
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
  background: var(--nm-05-surface);
  color: var(--nm-05-ink);
  border: 1px solid var(--nm-05-line);
  font: 600 11px/1 var(--nm-05-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-05-distance, 6px) var(--nm-05-distance, 6px) var(--nm-05-blur, 14px) var(--nm-05-dark), calc(-1 * var(--nm-05-distance, 6px)) calc(-1 * var(--nm-05-distance, 6px)) var(--nm-05-blur, 14px) var(--nm-05-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-05__themebtn:hover {
  color: var(--nm-05-ink);
}

.nm-05__themeinput:focus-visible + .nm-05__themebtn {
  outline: 2px solid var(--nm-05-ink);
  outline-offset: 3px;
}

.nm-05:has(#nm-05-theme:checked) .nm-05__themebtn {
  box-shadow: inset var(--nm-05-distance, 6px) var(--nm-05-distance, 6px) var(--nm-05-blur, 14px) var(--nm-05-dark), inset calc(-1 * var(--nm-05-distance, 6px)) calc(-1 * var(--nm-05-distance, 6px)) var(--nm-05-blur, 14px) var(--nm-05-light);
}

.nm-05__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-05:has(#nm-05-theme:checked) {
  --nm-05-surface: #2c2a35;
  --nm-05-dark: rgba(12,11,16,0.7);
  --nm-05-light: rgba(92,88,110,0.46);
  --nm-05-ink: #e8e5f0;
  --nm-05-muted: #a6a0ba;
  --nm-05-border: #8d87a2;
  --nm-05-primary: #a08ff0;
  --nm-05-danger: #e88ba0;
}

@media (prefers-color-scheme: light) {
  .nm-05:has(#nm-05-theme:checked) {
    --nm-05-surface: #2c2a35;
    --nm-05-dark: rgba(12,11,16,0.7);
    --nm-05-light: rgba(92,88,110,0.46);
    --nm-05-ink: #e8e5f0;
    --nm-05-muted: #a6a0ba;
    --nm-05-border: #8d87a2;
    --nm-05-primary: #a08ff0;
    --nm-05-danger: #e88ba0;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-05:has(#nm-05-theme:checked) {
    --nm-05-surface: #e7e4ef;
    --nm-05-dark: rgba(171,166,190,0.6);
    --nm-05-light: rgba(255,255,255,0.94);
    --nm-05-ink: #2b2836;
    --nm-05-muted: #5d5872;
    --nm-05-border: #9c96b0;
    --nm-05-primary: #6f5bd0;
    --nm-05-danger: #a83a52;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-05__themebtn {
    transition: none;
  }
}
```
