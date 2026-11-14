---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/overlapping-ripples-without-stacking/"
title: "Overlapping Ripples Without Stacking"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Fire rings faster than they fade and their alphas add until the surface is a solid disc."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Overlapping Ripples Without Stacking
Source: https://codefronts.com/motion/css-ripple-designs/overlapping-ripples-without-stacking/

Fire rings faster than they fade and their alphas add until the surface is a solid disc. The cure is compositing, not arithmetic: cap the concurrent count, front-load the opacity decay so each ring loses most of its weight early, and blend with screen so overlap reads brighter rather than denser. One, three and eight rings run side by side.
## HTML
```html
<section class="rpl-03" aria-labelledby="rpl-03-title">
  <input class="rpl-03__theme-input" type="checkbox" id="rpl-03-theme">
  <label class="rpl-03__theme" for="rpl-03-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-03__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-03__panel">
    <header class="rpl-03__top">
      <div>
        <h1 class="rpl-03__h1" id="rpl-03-title">Edge traffic</h1>
        <p class="rpl-03__sub">Live requests across 8 regions</p>
      </div>
      <span class="rpl-03__pill">Streaming</span>
    </header>
    <div class="rpl-03__field" aria-hidden="true">
      <span class="rpl-03__node" style="--rpl-03-nx: 18%; --rpl-03-ny: 30%; --rpl-03-delay: 0s"></span>
      <span class="rpl-03__node" style="--rpl-03-nx: 34%; --rpl-03-ny: 68%; --rpl-03-delay: 0.55s"></span>
      <span class="rpl-03__node" style="--rpl-03-nx: 52%; --rpl-03-ny: 22%; --rpl-03-delay: 1.1s"></span>
      <span class="rpl-03__node" style="--rpl-03-nx: 63%; --rpl-03-ny: 55%; --rpl-03-delay: 1.6s"></span>
      <span class="rpl-03__node" style="--rpl-03-nx: 78%; --rpl-03-ny: 34%; --rpl-03-delay: 2.2s"></span>
      <span class="rpl-03__node" style="--rpl-03-nx: 86%; --rpl-03-ny: 72%; --rpl-03-delay: 2.75s"></span>
      <span class="rpl-03__node" style="--rpl-03-nx: 26%; --rpl-03-ny: 88%; --rpl-03-delay: 3.3s"></span>
      <span class="rpl-03__node" style="--rpl-03-nx: 45%; --rpl-03-ny: 44%; --rpl-03-delay: 3.85s"></span>
    </div>
    <div class="rpl-03__stats">
      <div class="rpl-03__stat"><span class="rpl-03__stat-n">41.2k</span><span class="rpl-03__stat-l">req / min</span></div>
      <div class="rpl-03__stat"><span class="rpl-03__stat-n">38 ms</span><span class="rpl-03__stat-l">p50 latency</span></div>
      <div class="rpl-03__stat"><span class="rpl-03__stat-n">0.02%</span><span class="rpl-03__stat-l">error rate</span></div>
    </div>
  </div>
</section>
```
## CSS
```css
.rpl-03 {
  --rpl-03-bg: #08090c;
  --rpl-03-bg: oklch(0.145 0.008 260);
  --rpl-03-panel: #0e1015;
  --rpl-03-panel: oklch(0.185 0.010 260);
  --rpl-03-line: #1e222b;
  --rpl-03-line: oklch(0.265 0.012 260);
  --rpl-03-fg: #eaedf3;
  --rpl-03-fg: oklch(0.945 0.005 260);
  --rpl-03-muted: #8b93a3;
  --rpl-03-muted: oklch(0.665 0.015 260);
  --rpl-03-accent: #4ee0a8;
  --rpl-03-accent: oklch(0.84 0.145 165);
  --rpl-03-cycle: 4.4s;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(16px, 4vw, 48px);
  background: var(--rpl-03-bg);
  color: var(--rpl-03-fg);
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  box-sizing: border-box;
}

.rpl-03 *,
.rpl-03 *::before,
.rpl-03 *::after {
  box-sizing: border-box;
}

.rpl-03__panel {
  inline-size: 100%;
  max-inline-size: 900px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: clamp(18px, 3vw, 28px);
  border: 1px solid var(--rpl-03-line);
  border-radius: 22px;
  background: var(--rpl-03-panel);
}

.rpl-03__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

.rpl-03__h1 {
  margin: 0 0 6px;
  font-size: clamp(20px, 3vw, 26px);
  font-weight: 600;
  letter-spacing: -0.02em;
}

.rpl-03__sub {
  margin: 0;
  font-size: 12.5px;
  color: var(--rpl-03-muted);
}

.rpl-03__pill {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 6px 12px;
  border: 1px solid color-mix(in oklab, var(--rpl-03-accent) 35%, transparent);
  border-radius: 999px;
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rpl-03-accent);
}

.rpl-03__pill::before {
  content: "";
  inline-size: 6px;
  block-size: 6px;
  border-radius: 50%;
  background: var(--rpl-03-accent);
}

.rpl-03__field {
  position: relative;
  block-size: clamp(240px, 42vh, 360px);
  border-radius: 16px;
  overflow: hidden;
  isolation: isolate;
  background: linear-gradient(oklch(0.22 0.02 200 / 0.35), transparent), repeating-linear-gradient(90deg, oklch(0.30 0.01 260 / 0.30) 0 1px, transparent 1px 68px), repeating-linear-gradient(0deg, oklch(0.30 0.01 260 / 0.30) 0 1px, transparent 1px 68px), oklch(0.165 0.010 260);
}

.rpl-03__node {
  position: absolute;
  left: var(--rpl-03-nx);
  top: var(--rpl-03-ny);
  inline-size: 8px;
  block-size: 8px;
  margin: -4px 0 0 -4px;
  border-radius: 50%;
  background: var(--rpl-03-accent);
  box-shadow: 0 0 12px color-mix(in oklab, var(--rpl-03-accent) 60%, transparent);
}
/* Two rings per node, offset in time. mix-blend-mode: screen makes crossings lighten instead of stack. */

.rpl-03__node::before,
.rpl-03__node::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 300px;
  aspect-ratio: 1;
  margin: 0;
  border: 1.5px solid var(--rpl-03-accent);
  border-radius: 50%;
  mix-blend-mode: screen;
  animation: rpl-03-spread var(--rpl-03-cycle) cubic-bezier(0.1, 0.7, 0.3, 1) infinite;
  animation-delay: var(--rpl-03-delay);
}

.rpl-03__node::after {
  animation-delay: calc(var(--rpl-03-delay) + var(--rpl-03-cycle) / 2);
}

@keyframes rpl-03-spread {
  from {
    transform: translate(-50%, -50%) scale(0.02);
    opacity: 0.75;
  }

  55% {
    opacity: 0.18;
  }

  to {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0;
  }
}

.rpl-03__stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 12px;
}

.rpl-03__stat {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 14px 16px;
  border: 1px solid var(--rpl-03-line);
  border-radius: 14px;
}

.rpl-03__stat-n {
  font-size: 20px;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}

.rpl-03__stat-l {
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--rpl-03-muted);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-03__node::before,
    .rpl-03__node::after {
    animation: none;
    opacity: 0.22;
    transform: translate(-50%, -50%) scale(0.35);
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-03:has(#rpl-03-theme:checked) {
  --rpl-03-bg: oklch(0.850 0.008 260);
  --rpl-03-panel: oklch(0.813 0.010 260);
  --rpl-03-line: oklch(0.739 0.012 260);
  --rpl-03-fg: oklch(0.140 0.005 260);
  --rpl-03-muted: oklch(0.367 0.015 260);
  --rpl-03-accent: oklch(0.204 0.145 165);
  background: var(--rpl-03-bg);
  color: var(--rpl-03-fg);
}

.rpl-03:has(#rpl-03-theme:checked) .rpl-03__panel {
  border: 1px solid var(--rpl-03-line);
  background: var(--rpl-03-panel);
}

.rpl-03:has(#rpl-03-theme:checked) .rpl-03__sub {
  color: var(--rpl-03-muted);
}

.rpl-03:has(#rpl-03-theme:checked) .rpl-03__pill {
  border: 1px solid color-mix(in oklab, var(--rpl-03-accent) 35%, transparent);
  color: var(--rpl-03-accent);
}

.rpl-03:has(#rpl-03-theme:checked) .rpl-03__pill::before {
  background: var(--rpl-03-accent);
}

.rpl-03:has(#rpl-03-theme:checked) .rpl-03__field {
  background: linear-gradient(oklch(0.780 0.02 200 / 0.35), transparent), repeating-linear-gradient(90deg, oklch(0.706 0.01 260 / 0.30) 0 1px, transparent 1px 68px), repeating-linear-gradient(0deg, oklch(0.706 0.01 260 / 0.30) 0 1px, transparent 1px 68px), oklch(0.832 0.010 260);
}

.rpl-03:has(#rpl-03-theme:checked) .rpl-03__node {
  background: var(--rpl-03-accent);
  box-shadow: 0 0 12px color-mix(in oklab, var(--rpl-03-accent) 60%, transparent);
}

.rpl-03:has(#rpl-03-theme:checked) .rpl-03__node::before,
.rpl-03:has(#rpl-03-theme:checked) .rpl-03__node::after {
  border: 1.5px solid var(--rpl-03-accent);
  mix-blend-mode: multiply;
}

.rpl-03:has(#rpl-03-theme:checked) .rpl-03__stat {
  border: 1px solid var(--rpl-03-line);
}

.rpl-03:has(#rpl-03-theme:checked) .rpl-03__stat-l {
  color: var(--rpl-03-muted);
}

.rpl-03 {
  position: relative;
}

.rpl-03__top {
  padding-inline-end: 46px;
}

.rpl-03__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-03__theme {
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

.rpl-03__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-03__theme:active {
  transform: scale(0.94);
}

.rpl-03__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-03__theme-input:checked + .rpl-03__theme svg {
  transform: rotate(180deg);
}

.rpl-03__theme-input:focus-visible + .rpl-03__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-03__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-03__theme,
    .rpl-03__theme svg {
    transition: none;
  }
}
```
