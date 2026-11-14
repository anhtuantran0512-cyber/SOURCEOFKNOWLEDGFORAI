---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/keeping-ripples-circular-in-any-box/"
title: "Keeping Ripples Circular in Any Box"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "A ring sized in percentages goes oval the instant its container stops being square, and almost no container is square."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Keeping Ripples Circular in Any Box
Source: https://codefronts.com/motion/css-ripple-designs/keeping-ripples-circular-in-any-box/

A ring sized in percentages goes oval the instant its container stops being square, and almost no container is square. The failure sits beside three fixes: a square pseudo-element driven by aspect-ratio, an absolute size taken from the container diagonal, and the padding-top percentage trick for engines that predate aspect-ratio. All three are labelled.
## HTML
```html
<section class="rpl-02" aria-labelledby="rpl-02-title">
  <input class="rpl-02__theme-input" type="checkbox" id="rpl-02-theme">
  <label class="rpl-02__theme" for="rpl-02-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-02__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-02__card">
    <div class="rpl-02__head">
      <p class="rpl-02__step">Step 3 of 3</p>
      <h1 class="rpl-02__h1" id="rpl-02-title">Confirm your order</h1>
      <p class="rpl-02__lede">Nordwell Chore Coat &middot; Ecru &middot; Medium</p>
    </div>
    <dl class="rpl-02__sum">
      <div class="rpl-02__line"><dt>Subtotal</dt><dd>$248.00</dd></div>
      <div class="rpl-02__line"><dt>Shipping</dt><dd>Free</dd></div>
      <div class="rpl-02__line rpl-02__line--total"><dt>Total</dt><dd>$248.00</dd></div>
    </dl>
    <div class="rpl-02__actions">
      <button class="rpl-02__btn rpl-02__btn--wide" type="button">Pay $248.00</button>
      <div class="rpl-02__row">
        <button class="rpl-02__btn rpl-02__btn--ghost" type="button">Edit cart</button>
        <button class="rpl-02__btn rpl-02__btn--icon" type="button" aria-label="Apply gift card">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="8" width="18" height="12" rx="2"/><path d="M3 12h18M12 8v12M12 8c-2.5-4-6-2.5-4 0m4 0c2.5-4 6-2.5 4 0"/></svg>
        </button>
      </div>
      <button class="rpl-02__btn rpl-02__btn--tall" type="button">
        <span class="rpl-02__btn-title">Pay in 4</span>
        <span class="rpl-02__btn-note">$62.00 today, then 3 payments</span>
      </button>
    </div>
    <p class="rpl-02__fine">Every control is a different aspect ratio. The ripple stays round in all of them.</p>
  </div>
</section>
```
## CSS
```css
.rpl-02 {
  --rpl-02-bg: #f2efe9;
  --rpl-02-bg: oklch(0.955 0.010 85);
  --rpl-02-card: #fffdf9;
  --rpl-02-card: oklch(0.995 0.004 85);
  --rpl-02-fg: #1a1814;
  --rpl-02-fg: oklch(0.22 0.010 70);
  --rpl-02-muted: #6d675e;
  --rpl-02-muted: oklch(0.545 0.012 78);
  --rpl-02-line: #e2ddd3;
  --rpl-02-line: oklch(0.895 0.010 85);
  --rpl-02-accent: #1f4b3f;
  --rpl-02-accent: oklch(0.38 0.065 165);
  --rpl-02-ink: rgba(255, 255, 255, 0.42);
  --rpl-02-ink-dark: rgba(31, 75, 63, 0.20);
  --rpl-02-ink-dark: oklch(0.38 0.065 165 / 0.20);
  --rpl-02-dur: 620ms;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: var(--rpl-02-bg);
  color: var(--rpl-02-fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-02 *,
.rpl-02 *::before,
.rpl-02 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rpl-02:not(:has(#rpl-02-theme:checked)) {
    --rpl-02-bg: #12110f;
    --rpl-02-bg: oklch(0.18 0.008 78);
    --rpl-02-card: #1a1917;
    --rpl-02-card: oklch(0.235 0.008 78);
    --rpl-02-fg: #f2efe9;
    --rpl-02-fg: oklch(0.955 0.008 85);
    --rpl-02-muted: #a09a90;
    --rpl-02-muted: oklch(0.72 0.012 82);
    --rpl-02-line: #2c2a27;
    --rpl-02-line: oklch(0.31 0.008 78);
    --rpl-02-accent: #79d8b6;
    --rpl-02-accent: oklch(0.82 0.10 165);
    --rpl-02-ink: rgba(10, 22, 18, 0.35);
    --rpl-02-ink-dark: rgba(121, 216, 182, 0.20);
    --rpl-02-ink-dark: oklch(0.82 0.10 165 / 0.20);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-02:has(#rpl-02-theme:checked) {
    --rpl-02-bg: #12110f;
    --rpl-02-bg: oklch(0.18 0.008 78);
    --rpl-02-card: #1a1917;
    --rpl-02-card: oklch(0.235 0.008 78);
    --rpl-02-fg: #f2efe9;
    --rpl-02-fg: oklch(0.955 0.008 85);
    --rpl-02-muted: #a09a90;
    --rpl-02-muted: oklch(0.72 0.012 82);
    --rpl-02-line: #2c2a27;
    --rpl-02-line: oklch(0.31 0.008 78);
    --rpl-02-accent: #79d8b6;
    --rpl-02-accent: oklch(0.82 0.10 165);
    --rpl-02-ink: rgba(10, 22, 18, 0.35);
    --rpl-02-ink-dark: rgba(121, 216, 182, 0.20);
    --rpl-02-ink-dark: oklch(0.82 0.10 165 / 0.20);
  }
}

.rpl-02__card {
  inline-size: 100%;
  max-inline-size: 480px;
  display: flex;
  flex-direction: column;
  gap: 26px;
  padding: clamp(22px, 4vw, 36px);
  border: 1px solid var(--rpl-02-line);
  border-radius: 26px;
  background: var(--rpl-02-card);
}

.rpl-02__head {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rpl-02__step {
  margin: 0;
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--rpl-02-accent);
  font-weight: 600;
}

.rpl-02__h1 {
  margin: 0;
  font-size: clamp(26px, 4vw, 34px);
  font-weight: 600;
  letter-spacing: -0.025em;
  line-height: 1.1;
}

.rpl-02__lede {
  margin: 0;
  font-size: 14px;
  color: var(--rpl-02-muted);
}

.rpl-02__sum {
  margin: 0;
  display: flex;
  flex-direction: column;
}

.rpl-02__line {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  padding: 11px 0;
  border-block-end: 1px solid var(--rpl-02-line);
  font-size: 14px;
}

.rpl-02__line dt {
  color: var(--rpl-02-muted);
}

.rpl-02__line dd {
  margin: 0;
  font-variant-numeric: tabular-nums;
}

.rpl-02__line--total {
  border-block-end: 0;
  padding-block-end: 0;
  font-size: 17px;
  font-weight: 620;
}

.rpl-02__line--total dt {
  color: var(--rpl-02-fg);
}

.rpl-02__actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.rpl-02__row {
  display: flex;
  gap: 10px;
}

.rpl-02__btn {
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 52px;
  padding: 14px 20px;
  border: 1px solid transparent;
  border-radius: 14px;
  background: var(--rpl-02-accent);
  color: var(--rpl-02-card);
  font: inherit;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  -webkit-tap-highlight-color: transparent;
}

.rpl-02__btn:focus-visible {
  outline: 2px solid var(--rpl-02-accent);
  outline-offset: 3px;
}

.rpl-02__btn--wide {
  inline-size: 100%;
}

.rpl-02__btn--ghost {
  flex: 1;
  background: transparent;
  color: var(--rpl-02-fg);
  border-color: var(--rpl-02-line);
}

.rpl-02__btn--icon {
  inline-size: 52px;
  padding: 0;
  flex: none;
  background: transparent;
  color: var(--rpl-02-fg);
  border-color: var(--rpl-02-line);
}

.rpl-02__btn--icon svg {
  inline-size: 20px;
  block-size: 20px;
}

.rpl-02__btn--tall {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 4px;
  min-block-size: 78px;
  background: transparent;
  color: var(--rpl-02-fg);
  border-color: var(--rpl-02-line);
}

.rpl-02__btn-title {
  font-size: 15px;
  font-weight: 600;
}

.rpl-02__btn-note {
  font-size: 12.5px;
  font-weight: 400;
  color: var(--rpl-02-muted);
}
/* The square ripple layer: aspect-ratio keeps it circular whatever the button shape. */

.rpl-02__btn::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 150%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--rpl-02-ink);
  opacity: 0;
  transform: translate(-50%, -50%) scale(0);
  transition: transform var(--rpl-02-dur) cubic-bezier(0.12, 0.72, 0.28, 1), opacity var(--rpl-02-dur) linear;
  pointer-events: none;
  z-index: -1;
}

.rpl-02__btn--ghost::after,
.rpl-02__btn--icon::after,
.rpl-02__btn--tall::after {
  background: var(--rpl-02-ink-dark);
}

.rpl-02__btn:active::after {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  transition: none;
}

@supports not (aspect-ratio: 1) {
  .rpl-02__btn::after {
    inline-size: 150%;
    block-size: 0;
    padding-block-end: 150%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rpl-02__btn::after {
    display: none;
  }

  .rpl-02__btn:active {
    filter: brightness(0.94);
  }
}

.rpl-02__fine {
  margin: 0;
  font-size: 12px;
  line-height: 1.5;
  color: var(--rpl-02-muted);
  text-wrap: pretty;
}

.rpl-02 {
  position: relative;
}

.rpl-02__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-02__theme {
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

.rpl-02__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-02__theme:active {
  transform: scale(0.94);
}

.rpl-02__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-02__theme-input:checked + .rpl-02__theme svg {
  transform: rotate(180deg);
}

.rpl-02__theme-input:focus-visible + .rpl-02__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-02__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-02__theme,
    .rpl-02__theme svg {
    transition: none;
  }
}
```
