---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-neon-glow-ripple-effect/"
title: "Neon Glow Ripple Ring"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "The glow is a second ring, blurred, sitting behind the sharp one — not a filter applied to the ring itself."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Ripple Ring
Source: https://codefronts.com/motion/css-ripple-designs/css-neon-glow-ripple-effect/

The glow is a second ring, blurred, sitting behind the sharp one — not a filter applied to the ring itself. Filtering the ring blurs the edge you were trying to keep crisp, which is the whole difference between neon and fog. Both versions run side by side so the failure is visible, on a near-black ground where a glow can actually be seen.
## HTML
```html
<section class="rpl-12" aria-labelledby="rpl-12-title">
  <input class="rpl-12__theme-input" type="checkbox" id="rpl-12-theme">
  <label class="rpl-12__theme" for="rpl-12-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-12__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-12__card">
    <div class="rpl-12__badge">
      <span class="rpl-12__ping" aria-hidden="true"></span>
      <span class="rpl-12__badge-t">On air</span>
    </div>
    <div class="rpl-12__mid">
      <h1 class="rpl-12__h1" id="rpl-12-title">Nightshift<br>Radio</h1>
      <p class="rpl-12__set">Live set 042 &middot; Bassline &amp; breaks</p>
    </div>
    <div class="rpl-12__foot">
      <div class="rpl-12__stat"><span class="rpl-12__n">3,418</span><span class="rpl-12__l">listening</span></div>
      <div class="rpl-12__stat"><span class="rpl-12__n">01:12:40</span><span class="rpl-12__l">elapsed</span></div>
      <button class="rpl-12__join" type="button">Tune in</button>
    </div>
  </div>
</section>
```
## CSS
```css
.rpl-12 {
  --rpl-12-bg: #05050a;
  --rpl-12-bg: oklch(0.13 0.014 285);
  --rpl-12-card: #0b0b13;
  --rpl-12-card: oklch(0.17 0.018 285);
  --rpl-12-line: #1d1d2b;
  --rpl-12-line: oklch(0.25 0.024 285);
  --rpl-12-fg: #f2eeff;
  --rpl-12-fg: oklch(0.96 0.016 292);
  --rpl-12-muted: #8f87ab;
  --rpl-12-muted: oklch(0.665 0.045 292);
  --rpl-12-neon: #ff3fa4;
  --rpl-12-neon: oklch(0.68 0.24 350);
  --rpl-12-neon2: #4ad8ff;
  --rpl-12-neon2: oklch(0.83 0.14 220);
  --rpl-12-cycle: 2.6s;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: radial-gradient(70% 50% at 80% 10%, oklch(0.32 0.14 350 / 0.35), transparent 70%), radial-gradient(60% 50% at 10% 90%, oklch(0.32 0.12 220 / 0.3), transparent 70%), var(--rpl-12-bg);
  color: var(--rpl-12-fg);
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  box-sizing: border-box;
}

.rpl-12 *,
.rpl-12 *::before,
.rpl-12 *::after {
  box-sizing: border-box;
}

.rpl-12__card {
  position: relative;
  inline-size: 100%;
  max-inline-size: 460px;
  min-block-size: clamp(400px, 62vh, 520px);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 28px;
  padding: clamp(24px, 4vw, 34px);
  border: 1px solid var(--rpl-12-line);
  border-radius: 28px;
  background: var(--rpl-12-card);
  overflow: hidden;
}

.rpl-12__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg, oklch(1 0 0 / 0.022) 0 1px, transparent 1px 4px);
  pointer-events: none;
}

.rpl-12__badge {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 26px;
  align-self: flex-start;
}

.rpl-12__ping {
  position: relative;
  inline-size: 14px;
  block-size: 14px;
  flex: none;
  border-radius: 50%;
  background: var(--rpl-12-neon);
  box-shadow: 0 0 14px var(--rpl-12-neon), 0 0 40px color-mix(in oklab, var(--rpl-12-neon) 60%, transparent);
}
/* One sharp ring, one blurred twin behind it — the glow comes from the blurred copy, not from animating a shadow. */

.rpl-12__ping::before,
.rpl-12__ping::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 68px;
  aspect-ratio: 1;
  border: 2px solid var(--rpl-12-neon);
  border-radius: 50%;
  animation: rpl-12-ring var(--rpl-12-cycle) cubic-bezier(0.1, 0.7, 0.3, 1) infinite;
}

.rpl-12__ping::after {
  filter: blur(7px);
  border-width: 4px;
  border-color: var(--rpl-12-neon2);
  animation-delay: 120ms;
}

@keyframes rpl-12-ring {
  from {
    transform: translate(-50%, -50%) scale(0.1);
    opacity: 0.9;
  }

  60% {
    opacity: 0.22;
  }

  to {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

.rpl-12__badge-t {
  font-size: 11.5px;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--rpl-12-neon);
}

.rpl-12__mid {
  position: relative;
}

.rpl-12__h1 {
  margin: 0 0 12px;
  font-size: clamp(38px, 8vw, 58px);
  font-weight: 500;
  line-height: 0.98;
  letter-spacing: -0.04em;
  text-transform: uppercase;
}

.rpl-12__set {
  margin: 0;
  font-size: 13px;
  letter-spacing: 0.04em;
  color: var(--rpl-12-muted);
}

.rpl-12__foot {
  position: relative;
  display: flex;
  align-items: flex-end;
  gap: 24px;
}

.rpl-12__stat {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.rpl-12__n {
  font-size: 17px;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
}

.rpl-12__l {
  font-size: 10px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--rpl-12-muted);
}

.rpl-12__join {
  margin-inline-start: auto;
  min-block-size: 46px;
  padding: 0 20px;
  border: 1px solid var(--rpl-12-neon);
  border-radius: 999px;
  background: transparent;
  color: var(--rpl-12-neon);
  font: inherit;
  font-size: 12.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 160ms ease, color 160ms ease, box-shadow 160ms ease;
}

.rpl-12__join:hover {
  background: var(--rpl-12-neon);
  color: oklch(0.15 0.02 350);
  box-shadow: 0 0 26px color-mix(in oklab, var(--rpl-12-neon) 55%, transparent);
}

.rpl-12__join:focus-visible {
  outline: 2px solid var(--rpl-12-neon2);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-12__ping::before,
    .rpl-12__ping::after {
    animation: none;
    opacity: 0.3;
    transform: translate(-50%, -50%) scale(0.28);
  }

  .rpl-12__join {
    transition: none;
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-12:has(#rpl-12-theme:checked) {
  --rpl-12-bg: oklch(0.864 0.014 285);
  --rpl-12-card: oklch(0.827 0.018 285);
  --rpl-12-line: oklch(0.752 0.024 285);
  --rpl-12-fg: oklch(0.140 0.016 292);
  --rpl-12-muted: oklch(0.367 0.045 292);
  --rpl-12-neon: oklch(0.353 0.24 350);
  --rpl-12-neon2: oklch(0.213 0.14 220);
  background: radial-gradient(70% 50% at 80% 10%, oklch(0.687 0.14 350 / 0.35), transparent 70%), radial-gradient(60% 50% at 10% 90%, oklch(0.687 0.12 220 / 0.3), transparent 70%), var(--rpl-12-bg);
  color: var(--rpl-12-fg);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__card {
  border: 1px solid var(--rpl-12-line);
  background: var(--rpl-12-card);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__card::before {
  background: repeating-linear-gradient(0deg, oklch(0.140 0 0 / 0.022) 0 1px, transparent 1px 4px);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__ping {
  background: var(--rpl-12-neon);
  box-shadow: 0 0 14px var(--rpl-12-neon), 0 0 40px color-mix(in oklab, var(--rpl-12-neon) 60%, transparent);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__ping::before,
.rpl-12:has(#rpl-12-theme:checked) .rpl-12__ping::after {
  border: 2px solid var(--rpl-12-neon);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__ping::after {
  border-color: var(--rpl-12-neon2);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__badge-t {
  color: var(--rpl-12-neon);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__set {
  color: var(--rpl-12-muted);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__l {
  color: var(--rpl-12-muted);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__join {
  border: 1px solid var(--rpl-12-neon);
  color: var(--rpl-12-neon);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__join:hover {
  background: var(--rpl-12-neon);
  color: oklch(0.845 0.02 350);
  box-shadow: 0 0 26px color-mix(in oklab, var(--rpl-12-neon) 55%, transparent);
}

.rpl-12:has(#rpl-12-theme:checked) .rpl-12__join:focus-visible {
  outline: 2px solid var(--rpl-12-neon2);
}

.rpl-12 {
  position: relative;
}

.rpl-12__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-12__theme {
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

.rpl-12__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-12__theme:active {
  transform: scale(0.94);
}

.rpl-12__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-12__theme-input:checked + .rpl-12__theme svg {
  transform: rotate(180deg);
}

.rpl-12__theme-input:focus-visible + .rpl-12__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-12__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-12__theme,
    .rpl-12__theme svg {
    transition: none;
  }
}
```
