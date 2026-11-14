---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/ripple-easing-that-feels-like-water/"
title: "Ripple Easing That Feels Like Water"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Real displacement decelerates hard: fast at impact, then trailing away."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple Easing That Feels Like Water
Source: https://codefronts.com/motion/css-ripple-designs/ripple-easing-that-feels-like-water/

Real displacement decelerates hard: fast at impact, then trailing away. A linear ripple reads as a machine and ease-in-out reads as a slide transition. The same ring runs under three curves with each curve drawn beside it, plus the detail most builds miss — scale and opacity want different timing, so the ring is still growing after it has almost gone.
## HTML
```html
<section class="rpl-04" aria-labelledby="rpl-04-title">
  <input class="rpl-04__theme-input" type="checkbox" id="rpl-04-theme">
  <label class="rpl-04__theme" for="rpl-04-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-04__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-04__player">
    <div class="rpl-04__art" aria-hidden="true">
      <span class="rpl-04__wave"></span>
      <span class="rpl-04__wave rpl-04__wave--b"></span>
      <span class="rpl-04__wave rpl-04__wave--c"></span>
      <span class="rpl-04__disc"></span>
    </div>
    <div class="rpl-04__meta">
      <p class="rpl-04__eyebrow">Now playing</p>
      <h1 class="rpl-04__track" id="rpl-04-title">Shallow Water</h1>
      <p class="rpl-04__artist">Hana Ito &middot; Tidal Rooms</p>
    </div>
    <div class="rpl-04__scrub" aria-hidden="true"><span class="rpl-04__scrub-fill"></span></div>
    <div class="rpl-04__times" aria-hidden="true"><span>2:14</span><span>5:38</span></div>
    <div class="rpl-04__transport">
      <button class="rpl-04__btn" type="button" aria-label="Previous track">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 6h2v12H7zM19 6v12l-9-6z"/></svg>
      </button>
      <button class="rpl-04__btn rpl-04__btn--play" type="button" aria-label="Pause">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9 5h3v14H9zM14 5h3v14h-3z"/></svg>
      </button>
      <button class="rpl-04__btn" type="button" aria-label="Next track">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M15 6h2v12h-2zM5 6l9 6-9 6z"/></svg>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
.rpl-04 {
  --rpl-04-bg: #061417;
  --rpl-04-bg: oklch(0.20 0.030 205);
  --rpl-04-card: #0b2126;
  --rpl-04-card: oklch(0.26 0.036 205);
  --rpl-04-line: #16353c;
  --rpl-04-line: oklch(0.33 0.038 205);
  --rpl-04-fg: #eaf6f6;
  --rpl-04-fg: oklch(0.965 0.012 195);
  --rpl-04-muted: #8fb3b6;
  --rpl-04-muted: oklch(0.755 0.030 197);
  --rpl-04-accent: #5fe3d0;
  --rpl-04-accent: oklch(0.855 0.115 182);
  --rpl-04-dur: 5.2s;
  --rpl-04-ease: cubic-bezier(0.06, 0.72, 0.24, 1);
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: radial-gradient(90% 70% at 50% 0%, oklch(0.30 0.055 195 / 0.8), transparent 70%), var(--rpl-04-bg);
  color: var(--rpl-04-fg);
  font-family: ui-serif, Georgia, "Times New Roman", serif;
  box-sizing: border-box;
}

.rpl-04 *,
.rpl-04 *::before,
.rpl-04 *::after {
  box-sizing: border-box;
}

.rpl-04__player {
  inline-size: 100%;
  max-inline-size: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  padding: clamp(22px, 4vw, 32px);
  border: 1px solid var(--rpl-04-line);
  border-radius: 30px;
  background: oklch(0.26 0.036 205 / 0.75);
  backdrop-filter: blur(14px);
}

.rpl-04__art {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: min(260px, 62vw);
  aspect-ratio: 1;
  margin-block-end: 4px;
}

.rpl-04__disc {
  inline-size: 58%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: conic-gradient(from 210deg, oklch(0.55 0.12 200), oklch(0.80 0.11 175), oklch(0.45 0.13 250), oklch(0.55 0.12 200));
  box-shadow: inset 0 0 40px oklch(0.15 0.03 210 / 0.6);
}

.rpl-04__disc::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  inline-size: 12%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--rpl-04-card);
}
/* Water easing: scale decelerates hard, opacity leaves early — the ring keeps growing after it has gone. */

.rpl-04__wave {
  position: absolute;
  inline-size: 58%;
  aspect-ratio: 1;
  border: 1.5px solid var(--rpl-04-accent);
  border-radius: 50%;
  animation: rpl-04-scale var(--rpl-04-dur) var(--rpl-04-ease) infinite, rpl-04-fade var(--rpl-04-dur) cubic-bezier(0.3, 0.05, 0.6, 1) infinite;
}

.rpl-04__wave--b {
  animation-delay: calc(var(--rpl-04-dur) / -3), calc(var(--rpl-04-dur) / -3);
}

.rpl-04__wave--c {
  animation-delay: calc(var(--rpl-04-dur) / -1.5), calc(var(--rpl-04-dur) / -1.5);
}

@keyframes rpl-04-scale {
  from {
    transform: scale(1);
  }

  to {
    transform: scale(1.72);
  }
}

@keyframes rpl-04-fade {
  from {
    opacity: 0.65;
  }

  to {
    opacity: 0;
  }
}

.rpl-04__meta {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  text-align: center;
}

.rpl-04__eyebrow {
  margin: 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 10.5px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--rpl-04-accent);
}

.rpl-04__track {
  margin: 0;
  font-size: clamp(26px, 5vw, 34px);
  font-weight: 500;
  letter-spacing: -0.01em;
}

.rpl-04__artist {
  margin: 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 13px;
  color: var(--rpl-04-muted);
}

.rpl-04__scrub {
  inline-size: 100%;
  block-size: 4px;
  border-radius: 999px;
  background: color-mix(in oklab, var(--rpl-04-fg) 14%, transparent);
  overflow: hidden;
}

.rpl-04__scrub-fill {
  display: block;
  inline-size: 39%;
  block-size: 100%;
  border-radius: 999px;
  background: var(--rpl-04-accent);
}

.rpl-04__times {
  inline-size: 100%;
  display: flex;
  justify-content: space-between;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  color: var(--rpl-04-muted);
  font-variant-numeric: tabular-nums;
  margin-block-start: -10px;
}

.rpl-04__transport {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-block-start: 6px;
}

.rpl-04__btn {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 52px;
  block-size: 52px;
  border: 1px solid var(--rpl-04-line);
  border-radius: 50%;
  background: transparent;
  color: var(--rpl-04-fg);
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  -webkit-tap-highlight-color: transparent;
}

.rpl-04__btn svg {
  inline-size: 20px;
  block-size: 20px;
}

.rpl-04__btn:focus-visible {
  outline: 2px solid var(--rpl-04-accent);
  outline-offset: 3px;
}

.rpl-04__btn--play {
  inline-size: 68px;
  block-size: 68px;
  border-color: transparent;
  background: var(--rpl-04-accent);
  color: oklch(0.22 0.04 200);
}

.rpl-04__btn--play svg {
  inline-size: 26px;
  block-size: 26px;
}

.rpl-04__btn::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 160%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: color-mix(in oklab, var(--rpl-04-accent) 30%, transparent);
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  transition: transform 900ms var(--rpl-04-ease), opacity 900ms cubic-bezier(0.3, 0.05, 0.6, 1);
  pointer-events: none;
  z-index: -1;
}

.rpl-04__btn--play::after {
  background: oklch(0.22 0.04 200 / 0.28);
}

.rpl-04__btn:active::after {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  transition: none;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-04__wave {
    animation: none;
    opacity: 0.25;
    transform: scale(1.3);
  }

  .rpl-04__btn::after {
    display: none;
  }

  .rpl-04__btn:active {
    filter: brightness(1.2);
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-04:has(#rpl-04-theme:checked) {
  --rpl-04-bg: oklch(0.799 0.030 205);
  --rpl-04-card: oklch(0.743 0.036 205);
  --rpl-04-line: oklch(0.678 0.038 205);
  --rpl-04-fg: oklch(0.140 0.012 195);
  --rpl-04-muted: oklch(0.283 0.030 197);
  --rpl-04-accent: oklch(0.190 0.115 182);
  background: radial-gradient(90% 70% at 50% 0%, oklch(0.706 0.055 195 / 0.8), transparent 70%), var(--rpl-04-bg);
  color: var(--rpl-04-fg);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__player {
  border: 1px solid var(--rpl-04-line);
  background: oklch(0.743 0.036 205 / 0.75);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__disc {
  background: conic-gradient(from 210deg, oklch(0.473 0.12 200), oklch(0.241 0.11 175), oklch(0.567 0.13 250), oklch(0.473 0.12 200));
  box-shadow: inset 0 0 40px oklch(0.845 0.03 210 / 0.6);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__disc::after {
  background: var(--rpl-04-card);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__wave {
  border: 1.5px solid var(--rpl-04-accent);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__eyebrow {
  color: var(--rpl-04-accent);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__artist {
  color: var(--rpl-04-muted);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__scrub {
  background: color-mix(in oklab, var(--rpl-04-fg) 14%, transparent);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__scrub-fill {
  background: var(--rpl-04-accent);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__times {
  color: var(--rpl-04-muted);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__btn {
  border: 1px solid var(--rpl-04-line);
  color: var(--rpl-04-fg);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__btn:focus-visible {
  outline: 2px solid var(--rpl-04-accent);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__btn--play {
  background: var(--rpl-04-accent);
  color: oklch(0.780 0.04 200);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__btn::after {
  background: color-mix(in oklab, var(--rpl-04-accent) 30%, transparent);
}

.rpl-04:has(#rpl-04-theme:checked) .rpl-04__btn--play::after {
  background: oklch(0.780 0.04 200 / 0.28);
}

.rpl-04 {
  position: relative;
}

.rpl-04__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-04__theme {
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

.rpl-04__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-04__theme:active {
  transform: scale(0.94);
}

.rpl-04__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-04__theme-input:checked + .rpl-04__theme svg {
  transform: rotate(180deg);
}

.rpl-04__theme-input:focus-visible + .rpl-04__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-04__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-04__theme,
    .rpl-04__theme svg {
    transition: none;
  }
}
```
