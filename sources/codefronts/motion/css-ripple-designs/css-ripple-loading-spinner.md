---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-ripple-loading-spinner/"
title: "Ripple Loading Spinner"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Four rings leave the same centre on a fixed interval, producing a continuous outward flow with nothing rotating."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple Loading Spinner
Source: https://codefronts.com/motion/css-ripple-designs/css-ripple-loading-spinner/

Four rings leave the same centre on a fixed interval, producing a continuous outward flow with nothing rotating. The interesting part is the arithmetic: the delay per ring is the cycle divided by the ring count, so adding a fifth ring keeps the rhythm even instead of bunching it. Paired with a live region, because a spinner alone announces nothing.
## HTML
```html
<section class="rpl-13" aria-labelledby="rpl-13-title">
  <input class="rpl-13__theme-input" type="checkbox" id="rpl-13-theme">
  <label class="rpl-13__theme" for="rpl-13-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-13__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-13__card" role="status" aria-live="polite">
    <div class="rpl-13__loader" aria-hidden="true">
      <span class="rpl-13__ring"></span>
      <span class="rpl-13__ring"></span>
      <span class="rpl-13__ring"></span>
      <span class="rpl-13__ring"></span>
      <span class="rpl-13__core"></span>
    </div>
    <h1 class="rpl-13__h1" id="rpl-13-title">Restoring your workspace</h1>
    <p class="rpl-13__sub">Rebuilding 1,248 files from the last snapshot</p>
    <div class="rpl-13__bar" aria-hidden="true"><span class="rpl-13__fill"></span></div>
    <ul class="rpl-13__steps">
      <li class="rpl-13__step rpl-13__step--done">Snapshot verified</li>
      <li class="rpl-13__step rpl-13__step--done">Index rebuilt</li>
      <li class="rpl-13__step rpl-13__step--now">Copying assets</li>
      <li class="rpl-13__step">Reconnecting integrations</li>
    </ul>
  </div>
</section>
```
## CSS
```css
.rpl-13 {
  --rpl-13-bg: #f3f5f8;
  --rpl-13-bg: oklch(0.958 0.005 250);
  --rpl-13-card: #ffffff;
  --rpl-13-card: oklch(1 0 0);
  --rpl-13-line: #e4e8ee;
  --rpl-13-line: oklch(0.918 0.007 250);
  --rpl-13-fg: #131720;
  --rpl-13-fg: oklch(0.205 0.012 255);
  --rpl-13-muted: #69717f;
  --rpl-13-muted: oklch(0.565 0.014 255);
  --rpl-13-accent: #2563d8;
  --rpl-13-accent: oklch(0.55 0.18 260);
  --rpl-13-cycle: 2.4s;
  --rpl-13-rings: 4;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: var(--rpl-13-bg);
  color: var(--rpl-13-fg);
  font-family: "Helvetica Neue", -apple-system, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-13 *,
.rpl-13 *::before,
.rpl-13 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rpl-13:not(:has(#rpl-13-theme:checked)) {
    --rpl-13-bg: #0a0c11;
    --rpl-13-bg: oklch(0.16 0.010 255);
    --rpl-13-card: #12161e;
    --rpl-13-card: oklch(0.21 0.012 255);
    --rpl-13-line: #232833;
    --rpl-13-line: oklch(0.29 0.014 255);
    --rpl-13-fg: #edf0f5;
    --rpl-13-fg: oklch(0.955 0.005 255);
    --rpl-13-muted: #949cab;
    --rpl-13-muted: oklch(0.70 0.014 255);
    --rpl-13-accent: #7ea6ff;
    --rpl-13-accent: oklch(0.76 0.135 262);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-13:has(#rpl-13-theme:checked) {
    --rpl-13-bg: #0a0c11;
    --rpl-13-bg: oklch(0.16 0.010 255);
    --rpl-13-card: #12161e;
    --rpl-13-card: oklch(0.21 0.012 255);
    --rpl-13-line: #232833;
    --rpl-13-line: oklch(0.29 0.014 255);
    --rpl-13-fg: #edf0f5;
    --rpl-13-fg: oklch(0.955 0.005 255);
    --rpl-13-muted: #949cab;
    --rpl-13-muted: oklch(0.70 0.014 255);
    --rpl-13-accent: #7ea6ff;
    --rpl-13-accent: oklch(0.76 0.135 262);
  }
}

.rpl-13__card {
  inline-size: 100%;
  max-inline-size: 420px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: clamp(30px, 5vw, 44px) clamp(22px, 4vw, 34px);
  border: 1px solid var(--rpl-13-line);
  border-radius: 26px;
  background: var(--rpl-13-card);
  text-align: center;
}

.rpl-13__loader {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 116px;
  block-size: 116px;
  margin-block-end: 8px;
}

.rpl-13__core {
  inline-size: 12px;
  block-size: 12px;
  border-radius: 50%;
  background: var(--rpl-13-accent);
}

.rpl-13__ring {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 116px;
  aspect-ratio: 1;
  border: 2px solid var(--rpl-13-accent);
  border-radius: 50%;
  animation: rpl-13-pulse var(--rpl-13-cycle) cubic-bezier(0.12, 0.7, 0.3, 1) infinite;
}
/* stagger = cycle / ring count, so the gap between rings stays even if you add one */

.rpl-13__ring:nth-child(1) {
  animation-delay: calc(var(--rpl-13-cycle) / var(--rpl-13-rings) * 0);
}

.rpl-13__ring:nth-child(2) {
  animation-delay: calc(var(--rpl-13-cycle) / var(--rpl-13-rings) * -1);
}

.rpl-13__ring:nth-child(3) {
  animation-delay: calc(var(--rpl-13-cycle) / var(--rpl-13-rings) * -2);
}

.rpl-13__ring:nth-child(4) {
  animation-delay: calc(var(--rpl-13-cycle) / var(--rpl-13-rings) * -3);
}

@keyframes rpl-13-pulse {
  from {
    transform: translate(-50%, -50%) scale(0.1);
    opacity: 0.85;
  }

  70% {
    opacity: 0.15;
  }

  to {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

.rpl-13__h1 {
  margin: 0;
  font-size: clamp(20px, 3.2vw, 25px);
  font-weight: 600;
  letter-spacing: -0.022em;
}

.rpl-13__sub {
  margin: 0;
  font-size: 13.5px;
  color: var(--rpl-13-muted);
  font-variant-numeric: tabular-nums;
}

.rpl-13__bar {
  inline-size: 100%;
  block-size: 6px;
  margin-block: 10px 4px;
  border-radius: 999px;
  background: color-mix(in oklab, var(--rpl-13-fg) 9%, transparent);
  overflow: hidden;
}

.rpl-13__fill {
  display: block;
  inline-size: 64%;
  block-size: 100%;
  border-radius: 999px;
  background: var(--rpl-13-accent);
}

.rpl-13__steps {
  margin: 6px 0 0;
  padding: 0;
  list-style: none;
  inline-size: 100%;
  display: flex;
  flex-direction: column;
  gap: 9px;
  text-align: start;
}

.rpl-13__step {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--rpl-13-muted);
}

.rpl-13__step::before {
  content: "";
  inline-size: 15px;
  block-size: 15px;
  flex: none;
  border: 1.5px solid var(--rpl-13-line);
  border-radius: 50%;
}

.rpl-13__step--done {
  color: var(--rpl-13-fg);
}

.rpl-13__step--done::before {
  border-color: var(--rpl-13-accent);
  background: var(--rpl-13-accent);
}

.rpl-13__step--now {
  color: var(--rpl-13-fg);
  font-weight: 560;
}

.rpl-13__step--now::before {
  border-color: var(--rpl-13-accent);
  box-shadow: inset 0 0 0 3px var(--rpl-13-card), inset 0 0 0 9px var(--rpl-13-accent);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-13__ring {
    animation: none;
    opacity: 0.2;
  }

  .rpl-13__ring:nth-child(1) {
    transform: translate(-50%, -50%) scale(0.3);
  }

  .rpl-13__ring:nth-child(2) {
    transform: translate(-50%, -50%) scale(0.5);
  }

  .rpl-13__ring:nth-child(3) {
    transform: translate(-50%, -50%) scale(0.7);
  }

  .rpl-13__ring:nth-child(4) {
    transform: translate(-50%, -50%) scale(0.9);
  }
}

.rpl-13 {
  position: relative;
}

.rpl-13__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-13__theme {
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

.rpl-13__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-13__theme:active {
  transform: scale(0.94);
}

.rpl-13__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-13__theme-input:checked + .rpl-13__theme svg {
  transform: rotate(180deg);
}

.rpl-13__theme-input:focus-visible + .rpl-13__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-13__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-13__theme,
    .rpl-13__theme svg {
    transition: none;
  }
}
```
