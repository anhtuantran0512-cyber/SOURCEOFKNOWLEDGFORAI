---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/compositor-only-ripples-at-sixty-fps/"
title: "Compositor Only Ripples at Sixty FPS"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Animating width, height or top puts layout on the critical path for every single frame; animating transform and opacity hands the work to the compositor."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Compositor Only Ripples at Sixty FPS
Source: https://codefronts.com/motion/css-ripple-designs/compositor-only-ripples-at-sixty-fps/

Animating width, height or top puts layout on the critical path for every single frame; animating transform and opacity hands the work to the compositor. The two versions run side by side with the properties named and the pipeline stages each one triggers marked, plus an honest account of what will-change actually buys and what it costs.
## HTML
```html
<section class="rpl-05" aria-label="Compositor Only Ripples at Sixty FPS">
  <input class="rpl-05__theme-input" type="checkbox" id="rpl-05-theme">
  <label class="rpl-05__theme" for="rpl-05-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-05__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-05__term">
    <div class="rpl-05__screen">
      <p class="rpl-05__prompt">Enter access code</p>
      <div class="rpl-05__dots" aria-hidden="true">
        <span class="rpl-05__dot rpl-05__dot--on"></span>
        <span class="rpl-05__dot rpl-05__dot--on"></span>
        <span class="rpl-05__dot rpl-05__dot--on"></span>
        <span class="rpl-05__dot"></span>
        <span class="rpl-05__dot"></span>
        <span class="rpl-05__dot"></span>
      </div>
      <p class="rpl-05__hint">Gate 4B &middot; Terminal 21</p>
    </div>
    <div class="rpl-05__pad">
      <button class="rpl-05__key" type="button">1</button>
      <button class="rpl-05__key" type="button">2</button>
      <button class="rpl-05__key" type="button">3</button>
      <button class="rpl-05__key" type="button">4</button>
      <button class="rpl-05__key" type="button">5</button>
      <button class="rpl-05__key" type="button">6</button>
      <button class="rpl-05__key" type="button">7</button>
      <button class="rpl-05__key" type="button">8</button>
      <button class="rpl-05__key" type="button">9</button>
      <button class="rpl-05__key rpl-05__key--alt" type="button" aria-label="Clear">C</button>
      <button class="rpl-05__key" type="button">0</button>
      <button class="rpl-05__key rpl-05__key--go" type="button" aria-label="Confirm">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="m5 13 4 4 10-10"/></svg>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
.rpl-05 {
  --rpl-05-bg: #0c1117;
  --rpl-05-bg: oklch(0.19 0.014 250);
  --rpl-05-card: #131a23;
  --rpl-05-card: oklch(0.235 0.016 250);
  --rpl-05-key: #1b242f;
  --rpl-05-key: oklch(0.285 0.018 250);
  --rpl-05-line: #26313e;
  --rpl-05-line: oklch(0.33 0.018 250);
  --rpl-05-fg: #edf1f6;
  --rpl-05-fg: oklch(0.955 0.006 250);
  --rpl-05-muted: #8d98a7;
  --rpl-05-muted: oklch(0.685 0.016 250);
  --rpl-05-accent: #ffb648;
  --rpl-05-accent: oklch(0.82 0.145 72);
  --rpl-05-dur: 520ms;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: var(--rpl-05-bg);
  color: var(--rpl-05-fg);
  font-family: "Helvetica Neue", -apple-system, system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-05 *,
.rpl-05 *::before,
.rpl-05 *::after {
  box-sizing: border-box;
}

.rpl-05__term {
  inline-size: 100%;
  max-inline-size: 380px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: clamp(18px, 3.5vw, 26px);
  border: 1px solid var(--rpl-05-line);
  border-radius: 28px;
  background: var(--rpl-05-card);
  box-shadow: 0 30px 80px -40px oklch(0 0 0 / 0.9);
}

.rpl-05__screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  padding: 22px 18px;
  border-radius: 18px;
  background: oklch(0.165 0.014 250);
}

.rpl-05__prompt {
  margin: 0;
  font-size: 12px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--rpl-05-muted);
}

.rpl-05__dots {
  display: flex;
  gap: 12px;
}

.rpl-05__dot {
  inline-size: 12px;
  block-size: 12px;
  border-radius: 50%;
  border: 1.5px solid var(--rpl-05-line);
}

.rpl-05__dot--on {
  background: var(--rpl-05-accent);
  border-color: var(--rpl-05-accent);
}

.rpl-05__hint {
  margin: 0;
  font-size: 11.5px;
  letter-spacing: 0.06em;
  color: var(--rpl-05-muted);
}

.rpl-05__pad {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.rpl-05__key {
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 64px;
  border: 1px solid var(--rpl-05-line);
  border-radius: 16px;
  background: var(--rpl-05-key);
  color: var(--rpl-05-fg);
  font: inherit;
  font-size: 22px;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  will-change: transform;
  -webkit-tap-highlight-color: transparent;
}

.rpl-05__key:focus-visible {
  outline: 2px solid var(--rpl-05-accent);
  outline-offset: 2px;
}

.rpl-05__key--alt {
  font-size: 18px;
  color: var(--rpl-05-muted);
}

.rpl-05__key--go {
  background: var(--rpl-05-accent);
  border-color: transparent;
  color: oklch(0.22 0.03 72);
}

.rpl-05__key--go svg {
  inline-size: 24px;
  block-size: 24px;
}
/* transform + opacity only — no width/height/box-shadow in the animation, so it stays on the compositor. */

.rpl-05__key::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 150%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: color-mix(in oklab, var(--rpl-05-accent) 34%, transparent);
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  transition: transform var(--rpl-05-dur) cubic-bezier(0.12, 0.72, 0.28, 1), opacity var(--rpl-05-dur) linear;
  pointer-events: none;
  z-index: -1;
}

.rpl-05__key--go::after {
  background: oklch(0.22 0.03 72 / 0.26);
}

.rpl-05__key:active::after {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  transition: none;
}

.rpl-05__key:active {
  transform: scale(0.97);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-05__key::after {
    display: none;
  }

  .rpl-05__key:active {
    transform: none;
    background: color-mix(in oklab, var(--rpl-05-accent) 22%, var(--rpl-05-key));
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-05:has(#rpl-05-theme:checked) {
  --rpl-05-bg: oklch(0.808 0.014 250);
  --rpl-05-card: oklch(0.766 0.016 250);
  --rpl-05-key: oklch(0.720 0.018 250);
  --rpl-05-line: oklch(0.678 0.018 250);
  --rpl-05-fg: oklch(0.140 0.006 250);
  --rpl-05-muted: oklch(0.348 0.016 250);
  --rpl-05-accent: oklch(0.222 0.145 72);
  background: var(--rpl-05-bg);
  color: var(--rpl-05-fg);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__term {
  border: 1px solid var(--rpl-05-line);
  background: var(--rpl-05-card);
  box-shadow: 0 30px 80px -40px oklch(0.985 0 0 / 0.9);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__screen {
  background: oklch(0.832 0.014 250);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__prompt {
  color: var(--rpl-05-muted);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__dot {
  border: 1.5px solid var(--rpl-05-line);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__dot--on {
  background: var(--rpl-05-accent);
  border-color: var(--rpl-05-accent);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__hint {
  color: var(--rpl-05-muted);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__key {
  border: 1px solid var(--rpl-05-line);
  background: var(--rpl-05-key);
  color: var(--rpl-05-fg);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__key:focus-visible {
  outline: 2px solid var(--rpl-05-accent);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__key--alt {
  color: var(--rpl-05-muted);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__key--go {
  background: var(--rpl-05-accent);
  color: oklch(0.780 0.03 72);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__key::after {
  background: color-mix(in oklab, var(--rpl-05-accent) 34%, transparent);
}

.rpl-05:has(#rpl-05-theme:checked) .rpl-05__key--go::after {
  background: oklch(0.780 0.03 72 / 0.26);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-05:has(#rpl-05-theme:checked) .rpl-05__key:active {
    background: color-mix(in oklab, var(--rpl-05-accent) 22%, var(--rpl-05-key));
  }
}

.rpl-05 {
  position: relative;
}

.rpl-05__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-05__theme {
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

.rpl-05__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-05__theme:active {
  transform: scale(0.94);
}

.rpl-05__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-05__theme-input:checked + .rpl-05__theme svg {
  transform: rotate(180deg);
}

.rpl-05__theme-input:focus-visible + .rpl-05__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-05__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-05__theme,
    .rpl-05__theme svg {
    transition: none;
  }
}
```
