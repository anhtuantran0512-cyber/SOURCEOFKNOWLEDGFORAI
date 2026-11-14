---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-liquid-drop-ripple-animation/"
title: "Liquid Drop Impact Ripple"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "A drop falls, hits, throws rings outward, and a smaller rebound drop rises from the impact point and lands again."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Drop Impact Ripple
Source: https://codefronts.com/motion/css-ripple-designs/css-liquid-drop-ripple-animation/

A drop falls, hits, throws rings outward, and a smaller rebound drop rises from the impact point and lands again. Three animations sequenced with nothing but delays computed from one cycle token, so the whole event stays in phase, cannot drift apart over successive loops, and can be retimed end to end by changing a single value.
## HTML
```html
<section class="rpl-18" aria-labelledby="rpl-18-title">
  <input class="rpl-18__theme-input" type="checkbox" id="rpl-18-theme">
  <label class="rpl-18__theme" for="rpl-18-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-18__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-18__panel">
    <div class="rpl-18__zone">
      <div class="rpl-18__scene" aria-hidden="true">
        <span class="rpl-18__drop"></span>
        <span class="rpl-18__impact"></span>
        <span class="rpl-18__impact rpl-18__impact--b"></span>
        <span class="rpl-18__rebound"></span>
      </div>
      <h1 class="rpl-18__h1" id="rpl-18-title">Drop files to upload</h1>
      <p class="rpl-18__sub">PNG, JPG or HEIC up to 50 MB each</p>
      <button class="rpl-18__browse" type="button">Browse files</button>
    </div>
    <ul class="rpl-18__queue">
      <li class="rpl-18__item">
        <span class="rpl-18__thumb" data-t="1"></span>
        <span class="rpl-18__meta"><span class="rpl-18__fn">estuary-01.heic</span><span class="rpl-18__fs">8.4 MB &middot; uploaded</span></span>
        <span class="rpl-18__tick">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="m5 13 4 4 10-10"/></svg>
        </span>
      </li>
      <li class="rpl-18__item">
        <span class="rpl-18__thumb" data-t="2"></span>
        <span class="rpl-18__meta"><span class="rpl-18__fn">tidepool-sketch.png</span><span class="rpl-18__fs">2.1 MB &middot; 68%</span></span>
        <span class="rpl-18__prog"><span class="rpl-18__prog-fill"></span></span>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
.rpl-18 {
  --rpl-18-bg: #f4f1ea;
  --rpl-18-bg: oklch(0.958 0.010 88);
  --rpl-18-card: #fffdf8;
  --rpl-18-card: oklch(0.993 0.005 88);
  --rpl-18-line: #e3ddd0;
  --rpl-18-line: oklch(0.895 0.012 88);
  --rpl-18-fg: #1b1813;
  --rpl-18-fg: oklch(0.225 0.010 75);
  --rpl-18-muted: #6f695d;
  --rpl-18-muted: oklch(0.55 0.014 82);
  --rpl-18-accent: #1e5aa8;
  --rpl-18-accent: oklch(0.45 0.13 250);
  --rpl-18-cycle: 3.2s;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: var(--rpl-18-bg);
  color: var(--rpl-18-fg);
  font-family: ui-rounded, "SF Pro Rounded", -apple-system, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-18 *,
.rpl-18 *::before,
.rpl-18 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rpl-18:not(:has(#rpl-18-theme:checked)) {
    --rpl-18-bg: #12110e;
    --rpl-18-bg: oklch(0.185 0.008 82);
    --rpl-18-card: #1b1a16;
    --rpl-18-card: oklch(0.24 0.008 82);
    --rpl-18-line: #2d2b26;
    --rpl-18-line: oklch(0.315 0.008 82);
    --rpl-18-fg: #f4f0e9;
    --rpl-18-fg: oklch(0.96 0.008 88);
    --rpl-18-muted: #a19b90;
    --rpl-18-muted: oklch(0.72 0.012 85);
    --rpl-18-accent: #85b4ff;
    --rpl-18-accent: oklch(0.78 0.12 255);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-18:has(#rpl-18-theme:checked) {
    --rpl-18-bg: #12110e;
    --rpl-18-bg: oklch(0.185 0.008 82);
    --rpl-18-card: #1b1a16;
    --rpl-18-card: oklch(0.24 0.008 82);
    --rpl-18-line: #2d2b26;
    --rpl-18-line: oklch(0.315 0.008 82);
    --rpl-18-fg: #f4f0e9;
    --rpl-18-fg: oklch(0.96 0.008 88);
    --rpl-18-muted: #a19b90;
    --rpl-18-muted: oklch(0.72 0.012 85);
    --rpl-18-accent: #85b4ff;
    --rpl-18-accent: oklch(0.78 0.12 255);
  }
}

.rpl-18__panel {
  inline-size: 100%;
  max-inline-size: 520px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: clamp(18px, 3vw, 26px);
  border: 1px solid var(--rpl-18-line);
  border-radius: 28px;
  background: var(--rpl-18-card);
}

.rpl-18__zone {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: clamp(26px, 5vw, 40px) 24px clamp(24px, 4vw, 32px);
  border: 2px dashed color-mix(in oklab, var(--rpl-18-accent) 40%, var(--rpl-18-line));
  border-radius: 22px;
  text-align: center;
  background: color-mix(in oklab, var(--rpl-18-accent) 4%, transparent);
}

.rpl-18__scene {
  position: relative;
  inline-size: 130px;
  block-size: 104px;
  margin-block-end: 6px;
}

.rpl-18__drop {
  position: absolute;
  inset-inline-start: 50%;
  inline-size: 13px;
  block-size: 17px;
  border-radius: 50% 50% 50% 50% / 62% 62% 38% 38%;
  background: var(--rpl-18-accent);
  animation: rpl-18-fall var(--rpl-18-cycle) cubic-bezier(0.45, 0, 0.75, 0.3) infinite;
}

@keyframes rpl-18-fall {
  0% {
    transform: translate(-50%, -6px) scaleY(0.8);
    opacity: 0;
  }

  6% {
    opacity: 1;
  }

  30% {
    transform: translate(-50%, 66px) scaleY(1.35);
    opacity: 1;
  }

  33% {
    transform: translate(-50%, 74px) scaleY(0.4) scaleX(1.8);
    opacity: 0.5;
  }

  36%,
    100% {
    transform: translate(-50%, 74px) scaleY(0.2) scaleX(2.2);
    opacity: 0;
  }
}
/* Sequence with delays off one cycle: fall → impact rings → rebound bead. No script, no timers. */

.rpl-18__impact {
  position: absolute;
  inset-block-start: 78px;
  inset-inline-start: 50%;
  inline-size: 120px;
  aspect-ratio: 1;
  border: 2px solid var(--rpl-18-accent);
  border-radius: 50%;
  opacity: 0;
  animation: rpl-18-ring var(--rpl-18-cycle) cubic-bezier(0.1, 0.7, 0.3, 1) infinite;
  animation-delay: calc(var(--rpl-18-cycle) * 0.33);
}

.rpl-18__impact--b {
  animation-delay: calc(var(--rpl-18-cycle) * 0.42);
}

@keyframes rpl-18-ring {
  0% {
    transform: translate(-50%, -50%) scale(0.04);
    opacity: 0.75;
  }

  40% {
    opacity: 0.22;
  }

  60%,
    100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

.rpl-18__rebound {
  position: absolute;
  inset-block-start: 78px;
  inset-inline-start: 50%;
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: var(--rpl-18-accent);
  opacity: 0;
  animation: rpl-18-bead var(--rpl-18-cycle) cubic-bezier(0.3, 0, 0.6, 1) infinite;
  animation-delay: calc(var(--rpl-18-cycle) * 0.35);
}

@keyframes rpl-18-bead {
  0% {
    transform: translate(-50%, -50%) scale(0.4);
    opacity: 0;
  }

  15% {
    transform: translate(-50%, -240%) scale(1);
    opacity: 0.9;
  }

  32% {
    transform: translate(-50%, -50%) scale(0.6);
    opacity: 0;
  }

  100% {
    transform: translate(-50%, -50%) scale(0.4);
    opacity: 0;
  }
}

.rpl-18__h1 {
  margin: 0;
  font-size: clamp(20px, 3.4vw, 25px);
  font-weight: 620;
  letter-spacing: -0.022em;
}

.rpl-18__sub {
  margin: 0;
  font-size: 13px;
  color: var(--rpl-18-muted);
}

.rpl-18__browse {
  margin-block-start: 12px;
  min-block-size: 44px;
  padding: 0 20px;
  border: 1px solid var(--rpl-18-line);
  border-radius: 12px;
  background: var(--rpl-18-card);
  color: var(--rpl-18-fg);
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}

.rpl-18__browse:hover {
  border-color: var(--rpl-18-accent);
  color: var(--rpl-18-accent);
}

.rpl-18__browse:focus-visible {
  outline: 2px solid var(--rpl-18-accent);
  outline-offset: 2px;
}

.rpl-18__queue {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rpl-18__item {
  display: grid;
  grid-template-columns: 44px minmax(0, 1fr) auto;
  align-items: center;
  gap: 13px;
  padding: 10px 12px;
  border: 1px solid var(--rpl-18-line);
  border-radius: 16px;
}

.rpl-18__thumb {
  inline-size: 44px;
  block-size: 44px;
  border-radius: 11px;
  background: linear-gradient(140deg, oklch(0.68 0.10 220), oklch(0.48 0.08 250));
}

.rpl-18__thumb[data-t="2"] {
  background: linear-gradient(140deg, oklch(0.72 0.10 150), oklch(0.50 0.08 200));
}

.rpl-18__meta {
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-inline-size: 0;
}

.rpl-18__fn {
  font-size: 13.5px;
  font-weight: 580;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.rpl-18__fs {
  font-size: 12px;
  color: var(--rpl-18-muted);
}

.rpl-18__tick {
  display: grid;
  place-items: center;
  inline-size: 24px;
  block-size: 24px;
  border-radius: 50%;
  background: var(--rpl-18-accent);
  color: var(--rpl-18-card);
}

.rpl-18__tick svg {
  inline-size: 14px;
  block-size: 14px;
}

.rpl-18__prog {
  inline-size: 56px;
  block-size: 5px;
  border-radius: 999px;
  background: color-mix(in oklab, var(--rpl-18-fg) 10%, transparent);
  overflow: hidden;
}

.rpl-18__prog-fill {
  display: block;
  inline-size: 68%;
  block-size: 100%;
  border-radius: 999px;
  background: var(--rpl-18-accent);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-18__drop,
    .rpl-18__impact,
    .rpl-18__rebound {
    animation: none;
  }

  .rpl-18__drop {
    transform: translate(-50%, 40px);
    opacity: 1;
  }

  .rpl-18__impact {
    opacity: 0.2;
    transform: translate(-50%, -50%) scale(0.55);
  }

  .rpl-18__rebound {
    opacity: 0;
  }
}

.rpl-18 {
  position: relative;
}

.rpl-18__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-18__theme {
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

.rpl-18__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-18__theme:active {
  transform: scale(0.94);
}

.rpl-18__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-18__theme-input:checked + .rpl-18__theme svg {
  transform: rotate(180deg);
}

.rpl-18__theme-input:focus-visible + .rpl-18__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-18__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-18__theme,
    .rpl-18__theme svg {
    transition: none;
  }
}
```
