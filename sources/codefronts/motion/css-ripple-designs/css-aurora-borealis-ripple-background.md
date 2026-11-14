---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-aurora-borealis-ripple-background/"
title: "Aurora Ripple Background"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Very slow colour rings drift across a dusk gradient, overlapping into an aurora."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Ripple Background
Source: https://codefronts.com/motion/css-ripple-designs/css-aurora-borealis-ripple-background/

Very slow colour rings drift across a dusk gradient, overlapping into an aurora. The real problem is not the effect, it is the text: body copy over shifting colour has a contrast ratio that changes frame by frame. Solved with a fixed panel and a scrim measured against the worst frame, not the best one.
## HTML
```html
<section class="rpl-20" aria-labelledby="rpl-20-title">
  <input class="rpl-20__theme-input" type="checkbox" id="rpl-20-theme">
  <label class="rpl-20__theme" for="rpl-20-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-20__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-20__sky" aria-hidden="true">
    <span class="rpl-20__veil"></span>
    <span class="rpl-20__veil rpl-20__veil--b"></span>
    <span class="rpl-20__veil rpl-20__veil--c"></span>
    <span class="rpl-20__grain"></span>
  </div>
  <header class="rpl-20__nav">
    <span class="rpl-20__logo">Boreal</span>
    <nav class="rpl-20__links" aria-label="Primary">
      <span>Platform</span><span>Observatory</span><span>Pricing</span>
    </nav>
    <button class="rpl-20__nav-cta" type="button">Request access</button>
  </header>
  <div class="rpl-20__hero">
    <p class="rpl-20__kicker">Atmospheric data, live</p>
    <h1 class="rpl-20__h1" id="rpl-20-title">Watch the sky change<br>before it does</h1>
    <p class="rpl-20__lede">Boreal streams aurora, ionosphere and magnetometer readings from 240 ground stations into one forecast surface.</p>
    <div class="rpl-20__cta">
      <button class="rpl-20__btn" type="button">Start a forecast</button>
      <button class="rpl-20__btn rpl-20__btn--ghost" type="button">Watch the tour</button>
    </div>
  </div>
  <div class="rpl-20__strip">
    <div class="rpl-20__fact"><span class="rpl-20__fn">240</span><span class="rpl-20__fl">ground stations</span></div>
    <div class="rpl-20__fact"><span class="rpl-20__fn">1.2 s</span><span class="rpl-20__fl">stream latency</span></div>
    <div class="rpl-20__fact"><span class="rpl-20__fn">Kp 6</span><span class="rpl-20__fl">current index</span></div>
  </div>
</section>
```
## CSS
```css
.rpl-20 {
  --rpl-20-base: #070b1c;
  --rpl-20-base: oklch(0.165 0.045 272);
  --rpl-20-fg: #eef1ff;
  --rpl-20-fg: oklch(0.965 0.014 275);
  --rpl-20-muted: #a0a8cc;
  --rpl-20-muted: oklch(0.755 0.038 275);
  --rpl-20-a1: #46f0c0;
  --rpl-20-a1: oklch(0.87 0.145 165);
  --rpl-20-a2: #7b6bff;
  --rpl-20-a2: oklch(0.66 0.19 285);
  --rpl-20-a3: #ff7ac4;
  --rpl-20-a3: oklch(0.76 0.18 340);
  --rpl-20-cycle: 16s;
  position: relative;
  display: flex;
  flex-direction: column;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(18px, 3.5vw, 42px);
  background: var(--rpl-20-base);
  color: var(--rpl-20-fg);
  font-family: ui-serif, Georgia, "Times New Roman", serif;
  overflow: hidden;
  isolation: isolate;
  box-sizing: border-box;
}

.rpl-20 *,
.rpl-20 *::before,
.rpl-20 *::after {
  box-sizing: border-box;
}

.rpl-20__sky {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
}
/* Slow, huge, blurred rings — an ambient ripple field, then a scrim so the type stays legible. */

.rpl-20__veil {
  position: absolute;
  inset-block-start: 12%;
  inset-inline-start: 18%;
  inline-size: min(120vmin, 1200px);
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle, transparent 34%, color-mix(in oklab, var(--rpl-20-a1) 60%, transparent) 46%, transparent 62%);
  filter: blur(46px);
  mix-blend-mode: screen;
  opacity: 0.5;
  animation: rpl-20-swell var(--rpl-20-cycle) cubic-bezier(0.25, 0.6, 0.4, 1) infinite;
}

.rpl-20__veil--b {
  inset-block-start: 46%;
  inset-inline-start: 68%;
  background: radial-gradient(circle, transparent 32%, color-mix(in oklab, var(--rpl-20-a2) 70%, transparent) 44%, transparent 60%);
  animation-delay: calc(var(--rpl-20-cycle) / -3);
}

.rpl-20__veil--c {
  inset-block-start: 78%;
  inset-inline-start: 26%;
  background: radial-gradient(circle, transparent 30%, color-mix(in oklab, var(--rpl-20-a3) 60%, transparent) 42%, transparent 58%);
  animation-delay: calc(var(--rpl-20-cycle) / -1.6);
}

@keyframes rpl-20-swell {
  from {
    transform: translate(-50%, -50%) scale(0.28);
    opacity: 0;
  }

  20% {
    opacity: 0.55;
  }

  to {
    transform: translate(-50%, -50%) scale(1.05);
    opacity: 0;
  }
}

.rpl-20__grain {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, oklch(0.10 0.04 272 / 0.35), oklch(0.10 0.04 272 / 0.82));
}

.rpl-20__nav {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: clamp(14px, 3vw, 34px);
}

.rpl-20__logo {
  font-size: 17px;
  letter-spacing: 0.02em;
}

.rpl-20__links {
  display: flex;
  gap: 22px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 13.5px;
  color: var(--rpl-20-muted);
}

@media (max-width: 640px) {
  .rpl-20__links {
    display: none;
  }
}

.rpl-20__nav-cta {
  margin-inline-start: auto;
  min-block-size: 42px;
  padding: 0 18px;
  border: 1px solid oklch(1 0 0 / 0.22);
  border-radius: 999px;
  background: oklch(1 0 0 / 0.06);
  color: var(--rpl-20-fg);
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 13px;
  font-weight: 550;
  cursor: pointer;
  backdrop-filter: blur(8px);
}

.rpl-20__nav-cta:hover {
  background: oklch(1 0 0 / 0.14);
}

.rpl-20__nav-cta:focus-visible {
  outline: 2px solid var(--rpl-20-a1);
  outline-offset: 3px;
}

.rpl-20__hero {
  position: relative;
  z-index: 2;
  margin-block: auto;
  max-inline-size: min(94%, 720px);
}

.rpl-20__kicker {
  margin: 0 0 18px;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 11px;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--rpl-20-a1);
}

.rpl-20__h1 {
  margin: 0 0 20px;
  max-inline-size: 15ch;
  font-size: clamp(34px, 6.4vw, 72px);
  font-weight: 400;
  line-height: 1.0;
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.rpl-20__lede {
  margin: 0 0 26px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: clamp(14px, 1.7vw, 16.5px);
  line-height: 1.6;
  color: var(--rpl-20-muted);
  max-inline-size: 46ch;
  text-wrap: pretty;
}

.rpl-20__cta {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.rpl-20__btn {
  min-block-size: 52px;
  padding: 0 24px;
  border: 0;
  border-radius: 999px;
  background: var(--rpl-20-fg);
  color: oklch(0.18 0.05 272);
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 15px;
  font-weight: 620;
  cursor: pointer;
}

.rpl-20__btn--ghost {
  background: oklch(1 0 0 / 0.06);
  color: var(--rpl-20-fg);
  border: 1px solid oklch(1 0 0 / 0.22);
  backdrop-filter: blur(8px);
}

.rpl-20__btn:focus-visible {
  outline: 2px solid var(--rpl-20-a1);
  outline-offset: 3px;
}

.rpl-20__strip {
  position: relative;
  z-index: 2;
  display: flex;
  gap: clamp(20px, 5vw, 60px);
  flex-wrap: wrap;
  padding-block-start: 26px;
  border-block-start: 1px solid oklch(1 0 0 / 0.14);
}

.rpl-20__fact {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.rpl-20__fn {
  font-size: clamp(20px, 3vw, 26px);
  letter-spacing: -0.02em;
  font-variant-numeric: tabular-nums;
}

.rpl-20__fl {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 10px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--rpl-20-muted);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-20__veil {
    animation: none;
    opacity: 0.4;
    transform: translate(-50%, -50%) scale(0.8);
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-20:has(#rpl-20-theme:checked) {
  --rpl-20-base: oklch(0.832 0.045 272);
  --rpl-20-fg: oklch(0.140 0.014 275);
  --rpl-20-muted: oklch(0.283 0.038 275);
  --rpl-20-a1: oklch(0.176 0.145 165);
  --rpl-20-a2: oklch(0.371 0.19 285);
  --rpl-20-a3: oklch(0.278 0.18 340);
  background: var(--rpl-20-base);
  color: var(--rpl-20-fg);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__veil {
  background: radial-gradient(circle, transparent 34%, color-mix(in oklab, var(--rpl-20-a1) 60%, transparent) 46%, transparent 62%);
  mix-blend-mode: multiply;
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__veil--b {
  background: radial-gradient(circle, transparent 32%, color-mix(in oklab, var(--rpl-20-a2) 70%, transparent) 44%, transparent 60%);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__veil--c {
  background: radial-gradient(circle, transparent 30%, color-mix(in oklab, var(--rpl-20-a3) 60%, transparent) 42%, transparent 58%);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__grain {
  background: linear-gradient(180deg, oklch(0.892 0.04 272 / 0.35), oklch(0.892 0.04 272 / 0.82));
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__links {
  color: var(--rpl-20-muted);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__nav-cta {
  border: 1px solid oklch(0.140 0 0 / 0.22);
  background: oklch(0.140 0 0 / 0.06);
  color: var(--rpl-20-fg);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__nav-cta:hover {
  background: oklch(0.140 0 0 / 0.14);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__nav-cta:focus-visible {
  outline: 2px solid var(--rpl-20-a1);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__kicker {
  color: var(--rpl-20-a1);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__lede {
  color: var(--rpl-20-muted);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__btn {
  background: var(--rpl-20-fg);
  color: oklch(0.818 0.05 272);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__btn--ghost {
  background: oklch(0.140 0 0 / 0.06);
  color: var(--rpl-20-fg);
  border: 1px solid oklch(0.140 0 0 / 0.22);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__btn:focus-visible {
  outline: 2px solid var(--rpl-20-a1);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__strip {
  border-block-start: 1px solid oklch(0.140 0 0 / 0.14);
}

.rpl-20:has(#rpl-20-theme:checked) .rpl-20__fl {
  color: var(--rpl-20-muted);
}

.rpl-20 {
  position: relative;
}

.rpl-20__nav {
  padding-inline-end: 54px;
}

.rpl-20__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-20__theme {
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

.rpl-20__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-20__theme:active {
  transform: scale(0.94);
}

.rpl-20__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-20__theme-input:checked + .rpl-20__theme svg {
  transform: rotate(180deg);
}

.rpl-20__theme-input:focus-visible + .rpl-20__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-20__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-20__theme,
    .rpl-20__theme svg {
    transition: none;
  }
}
```
