---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/accessible-ripples-and-reduced-motion/"
title: "Accessible Ripples and Reduced Motion"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "A ripple is decorative feedback, so under reduced motion the answer is not a slower ripple — it is an instant state change that says the same thing without…"
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Ripples and Reduced Motion
Source: https://codefronts.com/motion/css-ripple-designs/accessible-ripples-and-reduced-motion/

A ripple is decorative feedback, so under reduced motion the answer is not a slower ripple — it is an instant state change that says the same thing without movement. Both versions sit side by side. Alongside them: why the ring must be aria-hidden, why it can never be the only sign a control fired, and why it is not a focus indicator.
## HTML
```html
<section class="rpl-08" aria-labelledby="rpl-08-title">
  <input class="rpl-08__theme-input" type="checkbox" id="rpl-08-theme">
  <label class="rpl-08__theme" for="rpl-08-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-08__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-08__sheet">
    <header class="rpl-08__head">
      <h1 class="rpl-08__h1" id="rpl-08-title">Accessibility</h1>
      <p class="rpl-08__sub">Changes apply across every device on this account.</p>
    </header>
    <div class="rpl-08__group">
      <p class="rpl-08__group-t">Motion</p>
      <label class="rpl-08__row">
        <span class="rpl-08__txt"><span class="rpl-08__name">Reduce motion</span><span class="rpl-08__desc">Replace transitions with instant state changes</span></span>
        <input class="rpl-08__sw" type="checkbox" role="switch" checked>
      </label>
      <label class="rpl-08__row">
        <span class="rpl-08__txt"><span class="rpl-08__name">Auto-play previews</span><span class="rpl-08__desc">Play video thumbnails on hover</span></span>
        <input class="rpl-08__sw" type="checkbox" role="switch">
      </label>
    </div>
    <div class="rpl-08__group">
      <p class="rpl-08__group-t">Display</p>
      <label class="rpl-08__row">
        <span class="rpl-08__txt"><span class="rpl-08__name">Increase contrast</span><span class="rpl-08__desc">Stronger borders and text weight</span></span>
        <input class="rpl-08__sw" type="checkbox" role="switch" checked>
      </label>
      <label class="rpl-08__row">
        <span class="rpl-08__txt"><span class="rpl-08__name">Larger text</span><span class="rpl-08__desc">Scale interface type to 120%</span></span>
        <input class="rpl-08__sw" type="checkbox" role="switch">
      </label>
    </div>
    <div class="rpl-08__foot">
      <button class="rpl-08__btn rpl-08__btn--ghost" type="button">Reset</button>
      <button class="rpl-08__btn" type="button">Save changes</button>
    </div>
  </div>
</section>
```
## CSS
```css
.rpl-08 {
  --rpl-08-bg: #faf7f2;
  --rpl-08-bg: oklch(0.975 0.008 85);
  --rpl-08-card: #ffffff;
  --rpl-08-card: oklch(1 0 0);
  --rpl-08-line: #e6e1d8;
  --rpl-08-line: oklch(0.905 0.010 85);
  --rpl-08-fg: #191712;
  --rpl-08-fg: oklch(0.215 0.010 75);
  --rpl-08-muted: #6f6a60;
  --rpl-08-muted: oklch(0.555 0.012 80);
  --rpl-08-accent: #6d4bd8;
  --rpl-08-accent: oklch(0.52 0.20 292);
  --rpl-08-ink: rgba(109, 75, 216, 0.16);
  --rpl-08-ink: oklch(0.52 0.20 292 / 0.16);
  --rpl-08-dur: 560ms;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: var(--rpl-08-bg);
  color: var(--rpl-08-fg);
  font-family: ui-rounded, "SF Pro Rounded", -apple-system, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-08 *,
.rpl-08 *::before,
.rpl-08 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rpl-08:not(:has(#rpl-08-theme:checked)) {
    --rpl-08-bg: #12100d;
    --rpl-08-bg: oklch(0.185 0.008 78);
    --rpl-08-card: #1b1917;
    --rpl-08-card: oklch(0.24 0.008 78);
    --rpl-08-line: #2d2a26;
    --rpl-08-line: oklch(0.315 0.008 78);
    --rpl-08-fg: #f6f2ec;
    --rpl-08-fg: oklch(0.965 0.008 85);
    --rpl-08-muted: #a29c92;
    --rpl-08-muted: oklch(0.725 0.012 82);
    --rpl-08-accent: #b9a0ff;
    --rpl-08-accent: oklch(0.79 0.13 292);
    --rpl-08-ink: rgba(185, 160, 255, 0.18);
    --rpl-08-ink: oklch(0.79 0.13 292 / 0.18);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-08:has(#rpl-08-theme:checked) {
    --rpl-08-bg: #12100d;
    --rpl-08-bg: oklch(0.185 0.008 78);
    --rpl-08-card: #1b1917;
    --rpl-08-card: oklch(0.24 0.008 78);
    --rpl-08-line: #2d2a26;
    --rpl-08-line: oklch(0.315 0.008 78);
    --rpl-08-fg: #f6f2ec;
    --rpl-08-fg: oklch(0.965 0.008 85);
    --rpl-08-muted: #a29c92;
    --rpl-08-muted: oklch(0.725 0.012 82);
    --rpl-08-accent: #b9a0ff;
    --rpl-08-accent: oklch(0.79 0.13 292);
    --rpl-08-ink: rgba(185, 160, 255, 0.18);
    --rpl-08-ink: oklch(0.79 0.13 292 / 0.18);
  }
}

.rpl-08__sheet {
  inline-size: 100%;
  max-inline-size: 540px;
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding: clamp(22px, 4vw, 34px);
  border: 1px solid var(--rpl-08-line);
  border-radius: 28px;
  background: var(--rpl-08-card);
}

.rpl-08__head {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.rpl-08__h1 {
  margin: 0;
  font-size: clamp(26px, 4vw, 32px);
  font-weight: 620;
  letter-spacing: -0.025em;
}

.rpl-08__sub {
  margin: 0;
  font-size: 14px;
  color: var(--rpl-08-muted);
  text-wrap: pretty;
}

.rpl-08__group {
  display: flex;
  flex-direction: column;
}

.rpl-08__group-t {
  margin: 0 0 6px;
  font-size: 11px;
  letter-spacing: 0.13em;
  text-transform: uppercase;
  color: var(--rpl-08-muted);
  font-weight: 600;
}

.rpl-08__row {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  min-block-size: 68px;
  padding: 14px 16px;
  margin-inline: -4px;
  border-radius: 16px;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  -webkit-tap-highlight-color: transparent;
}

.rpl-08__row + .rpl-08__row {
  box-shadow: inset 0 1px 0 var(--rpl-08-line);
}

.rpl-08__txt {
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-inline-size: 0;
}

.rpl-08__name {
  font-size: 15px;
  font-weight: 580;
  letter-spacing: -0.01em;
}

.rpl-08__desc {
  font-size: 12.5px;
  color: var(--rpl-08-muted);
  text-wrap: pretty;
}

.rpl-08__sw {
  inline-size: 50px;
  block-size: 30px;
  flex: none;
  margin: 0;
  accent-color: var(--rpl-08-accent);
  cursor: pointer;
}

.rpl-08__sw:focus-visible {
  outline: 2px solid var(--rpl-08-accent);
  outline-offset: 3px;
}
/* The ripple is decoration on top of a real state change — the switch is the feedback that matters. */

.rpl-08__row::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 130%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--rpl-08-ink);
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  transition: transform var(--rpl-08-dur) cubic-bezier(0.14, 0.7, 0.3, 1), opacity var(--rpl-08-dur) linear;
  pointer-events: none;
  z-index: -1;
}

.rpl-08__row:active::after {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  transition: none;
}

.rpl-08__foot {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

.rpl-08__btn {
  position: relative;
  min-block-size: 46px;
  padding: 0 20px;
  border: 1px solid transparent;
  border-radius: 13px;
  background: var(--rpl-08-accent);
  color: var(--rpl-08-card);
  font: inherit;
  font-size: 14.5px;
  font-weight: 600;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
}

.rpl-08__btn--ghost {
  background: transparent;
  color: var(--rpl-08-fg);
  border-color: var(--rpl-08-line);
}

.rpl-08__btn:focus-visible {
  outline: 2px solid var(--rpl-08-accent);
  outline-offset: 3px;
}

.rpl-08__btn::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 160%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: oklch(1 0 0 / 0.35);
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  transition: transform var(--rpl-08-dur) cubic-bezier(0.14, 0.7, 0.3, 1), opacity var(--rpl-08-dur) linear;
  pointer-events: none;
  z-index: -1;
}

.rpl-08__btn--ghost::after {
  background: var(--rpl-08-ink);
}

.rpl-08__btn:active::after {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  transition: none;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-08__row::after,
    .rpl-08__btn::after {
    display: none;
  }

  .rpl-08__row:active {
    background: color-mix(in oklab, var(--rpl-08-accent) 12%, transparent);
  }

  .rpl-08__btn:active {
    filter: brightness(0.93);
  }
}

.rpl-08 {
  position: relative;
}

.rpl-08__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-08__theme {
  position: absolute;
  z-index: 60;
  inset-block-start: 14px;
  inset-inline-end: 14px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background 160ms ease, border-color 160ms ease, transform 160ms ease;
}

.rpl-08__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-08__theme:active {
  transform: scale(0.94);
}

.rpl-08__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-08__theme-input:checked + .rpl-08__theme svg {
  transform: rotate(180deg);
}

.rpl-08__theme-input:focus-visible + .rpl-08__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-08__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-08__theme,
    .rpl-08__theme svg {
    transition: none;
  }
}
```
