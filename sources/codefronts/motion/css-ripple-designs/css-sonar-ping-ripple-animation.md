---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-sonar-ping-ripple-animation/"
title: "Sonar Ping Status Ripple"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "A ping leaves a status dot and travels outward, twice per cycle."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sonar Ping Status Ripple
Source: https://codefronts.com/motion/css-ripple-designs/css-sonar-ping-ripple-animation/

A ping leaves a status dot and travels outward, twice per cycle. Built as a monitoring panel where every row carries a text state as well as a colour and a motion, because a green dot next to a red dot is the textbook failure of SC 1.4.1 — colour and animation are decoration, the word is the information.
## HTML
```html
<section class="rpl-14" aria-labelledby="rpl-14-title">
  <input class="rpl-14__theme-input" type="checkbox" id="rpl-14-theme">
  <label class="rpl-14__theme" for="rpl-14-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-14__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-14__panel">
    <header class="rpl-14__top">
      <div>
        <h1 class="rpl-14__h1" id="rpl-14-title">Fleet status</h1>
        <p class="rpl-14__sub">us-east &middot; eu-west &middot; ap-south</p>
      </div>
      <p class="rpl-14__clock">Checked 14:22:07 UTC</p>
    </header>
    <ul class="rpl-14__list">
      <li class="rpl-14__row">
        <span class="rpl-14__dot rpl-14__dot--live" aria-hidden="true"></span>
        <span class="rpl-14__svc">api-gateway</span>
        <span class="rpl-14__num">42 ms</span>
        <span class="rpl-14__state rpl-14__state--ok">Operational</span>
      </li>
      <li class="rpl-14__row">
        <span class="rpl-14__dot rpl-14__dot--live" aria-hidden="true"></span>
        <span class="rpl-14__svc">auth-service</span>
        <span class="rpl-14__num">55 ms</span>
        <span class="rpl-14__state rpl-14__state--ok">Operational</span>
      </li>
      <li class="rpl-14__row">
        <span class="rpl-14__dot rpl-14__dot--warn" aria-hidden="true"></span>
        <span class="rpl-14__svc">media-encoder</span>
        <span class="rpl-14__num">312 ms</span>
        <span class="rpl-14__state rpl-14__state--warn">Degraded</span>
      </li>
      <li class="rpl-14__row">
        <span class="rpl-14__dot" aria-hidden="true"></span>
        <span class="rpl-14__svc">batch-reporter</span>
        <span class="rpl-14__num">&mdash;</span>
        <span class="rpl-14__state">Paused</span>
      </li>
      <li class="rpl-14__row">
        <span class="rpl-14__dot rpl-14__dot--live" aria-hidden="true"></span>
        <span class="rpl-14__svc">webhook-relay</span>
        <span class="rpl-14__num">88 ms</span>
        <span class="rpl-14__state rpl-14__state--ok">Operational</span>
      </li>
    </ul>
    <footer class="rpl-14__foot">
      <span class="rpl-14__legend"><i class="rpl-14__key rpl-14__key--ok"></i>Operational</span>
      <span class="rpl-14__legend"><i class="rpl-14__key rpl-14__key--warn"></i>Degraded</span>
      <span class="rpl-14__legend"><i class="rpl-14__key"></i>Paused</span>
    </footer>
  </div>
</section>
```
## CSS
```css
.rpl-14 {
  --rpl-14-bg: #0d1117;
  --rpl-14-bg: oklch(0.195 0.014 255);
  --rpl-14-panel: #141a23;
  --rpl-14-panel: oklch(0.24 0.016 255);
  --rpl-14-line: #232c38;
  --rpl-14-line: oklch(0.305 0.018 255);
  --rpl-14-fg: #e9eef5;
  --rpl-14-fg: oklch(0.945 0.006 255);
  --rpl-14-muted: #8794a5;
  --rpl-14-muted: oklch(0.665 0.018 255);
  --rpl-14-ok: #35d69a;
  --rpl-14-ok: oklch(0.80 0.145 165);
  --rpl-14-warn: #ffb02e;
  --rpl-14-warn: oklch(0.81 0.155 78);
  --rpl-14-cycle: 2.2s;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: var(--rpl-14-bg);
  color: var(--rpl-14-fg);
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  box-sizing: border-box;
}

.rpl-14 *,
.rpl-14 *::before,
.rpl-14 *::after {
  box-sizing: border-box;
}

.rpl-14__panel {
  inline-size: 100%;
  max-inline-size: 760px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  padding: clamp(20px, 3vw, 30px);
  border: 1px solid var(--rpl-14-line);
  border-radius: 22px;
  background: var(--rpl-14-panel);
}

.rpl-14__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 18px;
  flex-wrap: wrap;
}

.rpl-14__h1 {
  margin: 0 0 6px;
  font-size: clamp(19px, 2.8vw, 24px);
  font-weight: 600;
  letter-spacing: -0.02em;
}

.rpl-14__sub {
  margin: 0;
  font-size: 12px;
  color: var(--rpl-14-muted);
  letter-spacing: 0.04em;
}

.rpl-14__clock {
  margin: 0;
  font-size: 11.5px;
  color: var(--rpl-14-muted);
  font-variant-numeric: tabular-nums;
}

.rpl-14__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
}

.rpl-14__row {
  display: grid;
  grid-template-columns: 22px minmax(0, 1fr) auto auto;
  align-items: center;
  gap: 14px;
  padding: 15px 4px;
  border-block-end: 1px solid var(--rpl-14-line);
}

.rpl-14__row:last-child {
  border-block-end: 0;
}

.rpl-14__dot {
  position: relative;
  justify-self: center;
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: color-mix(in oklab, var(--rpl-14-muted) 55%, transparent);
}

.rpl-14__dot--live {
  background: var(--rpl-14-ok);
}

.rpl-14__dot--warn {
  background: var(--rpl-14-warn);
}
/* The ping is decorative; the word next to it carries the state for anyone who can't see colour or motion. */

.rpl-14__dot--live::after,
.rpl-14__dot--warn::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 34px;
  aspect-ratio: 1;
  border-radius: 50%;
  background: currentColor;
  animation: rpl-14-ping var(--rpl-14-cycle) cubic-bezier(0.1, 0.7, 0.3, 1) infinite;
}

.rpl-14__dot--live::after {
  color: var(--rpl-14-ok);
}

.rpl-14__dot--warn::after {
  color: var(--rpl-14-warn);
  animation-duration: 1.4s;
}

@keyframes rpl-14-ping {
  from {
    transform: translate(-50%, -50%) scale(0.22);
    opacity: 0.55;
  }

  to {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

.rpl-14__svc {
  font-size: 14px;
  letter-spacing: -0.005em;
}

.rpl-14__num {
  font-size: 13px;
  color: var(--rpl-14-muted);
  font-variant-numeric: tabular-nums;
}

.rpl-14__state {
  min-inline-size: 108px;
  text-align: end;
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--rpl-14-muted);
}

.rpl-14__state--ok {
  color: var(--rpl-14-ok);
}

.rpl-14__state--warn {
  color: var(--rpl-14-warn);
}

.rpl-14__foot {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  padding-block-start: 4px;
}

.rpl-14__legend {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rpl-14-muted);
}

.rpl-14__key {
  inline-size: 8px;
  block-size: 8px;
  border-radius: 50%;
  background: color-mix(in oklab, var(--rpl-14-muted) 55%, transparent);
}

.rpl-14__key--ok {
  background: var(--rpl-14-ok);
}

.rpl-14__key--warn {
  background: var(--rpl-14-warn);
}

@media (max-width: 560px) {
  .rpl-14__row {
    grid-template-columns: 22px minmax(0, 1fr) auto;
  }

  .rpl-14__num {
    grid-column: 2;
    font-size: 12px;
  }

  .rpl-14__state {
    grid-row: 1;
    grid-column: 3;
    min-inline-size: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rpl-14__dot--live::after,
    .rpl-14__dot--warn::after {
    animation: none;
    opacity: 0.22;
    transform: translate(-50%, -50%) scale(0.5);
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-14:has(#rpl-14-theme:checked) {
  --rpl-14-bg: oklch(0.804 0.014 255);
  --rpl-14-panel: oklch(0.762 0.016 255);
  --rpl-14-line: oklch(0.701 0.018 255);
  --rpl-14-fg: oklch(0.140 0.006 255);
  --rpl-14-muted: oklch(0.367 0.018 255);
  --rpl-14-ok: oklch(0.241 0.145 165);
  --rpl-14-warn: oklch(0.232 0.155 78);
  background: var(--rpl-14-bg);
  color: var(--rpl-14-fg);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__panel {
  border: 1px solid var(--rpl-14-line);
  background: var(--rpl-14-panel);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__sub {
  color: var(--rpl-14-muted);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__clock {
  color: var(--rpl-14-muted);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__dot {
  background: color-mix(in oklab, var(--rpl-14-muted) 55%, transparent);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__dot--live {
  background: var(--rpl-14-ok);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__dot--warn {
  background: var(--rpl-14-warn);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__dot--live::after,
.rpl-14:has(#rpl-14-theme:checked) .rpl-14__dot--warn::after {
  background: currentColor;
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__dot--live::after {
  color: var(--rpl-14-ok);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__dot--warn::after {
  color: var(--rpl-14-warn);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__num {
  color: var(--rpl-14-muted);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__state {
  color: var(--rpl-14-muted);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__state--ok {
  color: var(--rpl-14-ok);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__state--warn {
  color: var(--rpl-14-warn);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__legend {
  color: var(--rpl-14-muted);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__key {
  background: color-mix(in oklab, var(--rpl-14-muted) 55%, transparent);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__key--ok {
  background: var(--rpl-14-ok);
}

.rpl-14:has(#rpl-14-theme:checked) .rpl-14__key--warn {
  background: var(--rpl-14-warn);
}

.rpl-14 {
  position: relative;
}

.rpl-14__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-14__theme {
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

.rpl-14__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-14__theme:active {
  transform: scale(0.94);
}

.rpl-14__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-14__theme-input:checked + .rpl-14__theme svg {
  transform: rotate(180deg);
}

.rpl-14__theme-input:focus-visible + .rpl-14__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-14__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-14__theme,
    .rpl-14__theme svg {
    transition: none;
  }
}
```
