---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-sound-wave-ripple-visualizer/"
title: "Sound Wave Ripple Visualizer"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Rings leave a centre point at different amplitudes, each band driven by its own custom property, so the field reads as radial displacement rather than a row…"
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sound Wave Ripple Visualizer
Source: https://codefronts.com/motion/css-ripple-designs/css-sound-wave-ripple-visualizer/

Rings leave a centre point at different amplitudes, each band driven by its own custom property, so the field reads as radial displacement rather than a row of bars. It is decorative and says so: nothing here is connected to Web Audio, and a visualiser that is not synced to real audio should never be presented as if it were.
## HTML
```html
<section class="rpl-17" aria-label="Sound Wave Ripple Visualizer">
  <input class="rpl-17__theme-input" type="checkbox" id="rpl-17-theme">
  <label class="rpl-17__theme" for="rpl-17-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-17__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-17__shell">
    <p class="rpl-17__label">Listening</p>
    <div class="rpl-17__stage" aria-hidden="true">
      <span class="rpl-17__ring" style="--rpl-17-i: 0; --rpl-17-amp: 0.92"></span>
      <span class="rpl-17__ring" style="--rpl-17-i: 1; --rpl-17-amp: 0.68"></span>
      <span class="rpl-17__ring" style="--rpl-17-i: 2; --rpl-17-amp: 1"></span>
      <span class="rpl-17__ring" style="--rpl-17-i: 3; --rpl-17-amp: 0.55"></span>
      <span class="rpl-17__ring" style="--rpl-17-i: 4; --rpl-17-amp: 0.8"></span>
      <span class="rpl-17__ticks"></span>
      <span class="rpl-17__mic">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11.5a6.5 6.5 0 0 0 13 0M12 18v3"/></svg>
      </span>
    </div>
    <p class="rpl-17__transcript">&ldquo;Add oat milk and cardamom to the shopping list&rdquo;</p>
    <div class="rpl-17__meters">
      <div class="rpl-17__meter"><span class="rpl-17__mn">-12 dB</span><span class="rpl-17__ml">input</span></div>
      <div class="rpl-17__meter"><span class="rpl-17__mn">0.4 s</span><span class="rpl-17__ml">latency</span></div>
      <div class="rpl-17__meter"><span class="rpl-17__mn">on-device</span><span class="rpl-17__ml">model</span></div>
    </div>
    <button class="rpl-17__stop" type="button">Stop listening</button>
  </div>
</section>
```
## CSS
```css
.rpl-17 {
  --rpl-17-bg: #06070b;
  --rpl-17-bg: oklch(0.135 0.010 265);
  --rpl-17-fg: #e9ecf5;
  --rpl-17-fg: oklch(0.945 0.008 265);
  --rpl-17-muted: #7f879b;
  --rpl-17-muted: oklch(0.635 0.022 265);
  --rpl-17-line: #1a1d27;
  --rpl-17-line: oklch(0.245 0.014 265);
  --rpl-17-accent: #9d7cff;
  --rpl-17-accent: oklch(0.72 0.17 292);
  --rpl-17-accent2: #4fd6ff;
  --rpl-17-accent2: oklch(0.84 0.13 215);
  --rpl-17-cycle: 2.8s;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(18px, 4vw, 48px);
  background: radial-gradient(60% 50% at 50% 42%, oklch(0.28 0.10 292 / 0.45), transparent 70%), var(--rpl-17-bg);
  color: var(--rpl-17-fg);
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  box-sizing: border-box;
}

.rpl-17 *,
.rpl-17 *::before,
.rpl-17 *::after {
  box-sizing: border-box;
}

.rpl-17__shell {
  inline-size: 100%;
  max-inline-size: 480px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 22px;
  text-align: center;
}

.rpl-17__label {
  margin: 0;
  font-size: 11px;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--rpl-17-accent);
}

.rpl-17__stage {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: min(340px, 78vw);
  aspect-ratio: 1;
}

.rpl-17__ticks {
  position: absolute;
  inset: 12%;
  border-radius: 50%;
  background: conic-gradient(from 0deg, oklch(0.72 0.17 292 / 0.55) 0 1deg, transparent 1deg 6deg);
  mask: radial-gradient(circle, transparent 62%, #000 63%, #000 70%, transparent 71%);
  opacity: 0.6;
}

.rpl-17__mic {
  position: relative;
  z-index: 2;
  display: grid;
  place-items: center;
  inline-size: 78px;
  block-size: 78px;
  border-radius: 50%;
  background: linear-gradient(150deg, var(--rpl-17-accent), oklch(0.55 0.16 300));
  color: oklch(0.16 0.02 292);
  box-shadow: 0 0 50px oklch(0.72 0.17 292 / 0.4);
}

.rpl-17__mic svg {
  inline-size: 30px;
  block-size: 30px;
}
/* One keyframe, five rings: --rpl-17-i shifts the delay, --rpl-17-amp shifts the reach. */

.rpl-17__ring {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 100%;
  aspect-ratio: 1;
  border: 1.5px solid var(--rpl-17-accent2);
  border-radius: 50%;
  mix-blend-mode: screen;
  animation: rpl-17-wave var(--rpl-17-cycle) cubic-bezier(0.1, 0.68, 0.3, 1) infinite;
  animation-delay: calc(var(--rpl-17-cycle) / 5 * var(--rpl-17-i) * -1);
}

@keyframes rpl-17-wave {
  from {
    transform: translate(-50%, -50%) scale(0.22);
    opacity: calc(0.62 * var(--rpl-17-amp, 1));
  }

  70% {
    opacity: calc(0.12 * var(--rpl-17-amp, 1));
  }

  to {
    transform: translate(-50%, -50%) scale(var(--rpl-17-amp, 1));
    opacity: 0;
  }
}

.rpl-17__transcript {
  margin: 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: clamp(16px, 2.6vw, 20px);
  line-height: 1.45;
  letter-spacing: -0.01em;
  max-inline-size: 32ch;
  text-wrap: balance;
}

.rpl-17__meters {
  display: flex;
  gap: 10px;
  inline-size: 100%;
}

.rpl-17__meter {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 12px 10px;
  border: 1px solid var(--rpl-17-line);
  border-radius: 14px;
}

.rpl-17__mn {
  font-size: 13px;
  font-variant-numeric: tabular-nums;
}

.rpl-17__ml {
  font-size: 9.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--rpl-17-muted);
}

.rpl-17__stop {
  min-block-size: 46px;
  padding: 0 22px;
  border: 1px solid var(--rpl-17-line);
  border-radius: 999px;
  background: transparent;
  color: var(--rpl-17-fg);
  font: inherit;
  font-size: 12px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  cursor: pointer;
  transition: border-color 160ms ease, color 160ms ease;
}

.rpl-17__stop:hover {
  border-color: var(--rpl-17-accent);
  color: var(--rpl-17-accent);
}

.rpl-17__stop:focus-visible {
  outline: 2px solid var(--rpl-17-accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-17__ring {
    animation: none;
    opacity: 0.18;
    transform: translate(-50%, -50%) scale(calc(0.3 + 0.15 * var(--rpl-17-i)));
  }

  .rpl-17__stop {
    transition: none;
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-17:has(#rpl-17-theme:checked) {
  --rpl-17-bg: oklch(0.859 0.010 265);
  --rpl-17-fg: oklch(0.140 0.008 265);
  --rpl-17-muted: oklch(0.394 0.022 265);
  --rpl-17-line: oklch(0.757 0.014 265);
  --rpl-17-accent: oklch(0.315 0.17 292);
  --rpl-17-accent2: oklch(0.204 0.13 215);
  background: radial-gradient(60% 50% at 50% 42%, oklch(0.725 0.10 292 / 0.45), transparent 70%), var(--rpl-17-bg);
  color: var(--rpl-17-fg);
}

.rpl-17:has(#rpl-17-theme:checked) .rpl-17__label {
  color: var(--rpl-17-accent);
}

.rpl-17:has(#rpl-17-theme:checked) .rpl-17__ticks {
  background: conic-gradient(from 0deg, oklch(0.315 0.17 292 / 0.55) 0 1deg, transparent 1deg 6deg);
}

.rpl-17:has(#rpl-17-theme:checked) .rpl-17__mic {
  background: linear-gradient(150deg, var(--rpl-17-accent), oklch(0.473 0.16 300));
  color: oklch(0.836 0.02 292);
  box-shadow: 0 0 50px oklch(0.315 0.17 292 / 0.4);
}

.rpl-17:has(#rpl-17-theme:checked) .rpl-17__ring {
  border: 1.5px solid var(--rpl-17-accent2);
  mix-blend-mode: multiply;
}

.rpl-17:has(#rpl-17-theme:checked) .rpl-17__meter {
  border: 1px solid var(--rpl-17-line);
}

.rpl-17:has(#rpl-17-theme:checked) .rpl-17__ml {
  color: var(--rpl-17-muted);
}

.rpl-17:has(#rpl-17-theme:checked) .rpl-17__stop {
  border: 1px solid var(--rpl-17-line);
  color: var(--rpl-17-fg);
}

.rpl-17:has(#rpl-17-theme:checked) .rpl-17__stop:hover {
  border-color: var(--rpl-17-accent);
  color: var(--rpl-17-accent);
}

.rpl-17:has(#rpl-17-theme:checked) .rpl-17__stop:focus-visible {
  outline: 2px solid var(--rpl-17-accent);
}

.rpl-17 {
  position: relative;
}

.rpl-17__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-17__theme {
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

.rpl-17__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-17__theme:active {
  transform: scale(0.94);
}

.rpl-17__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-17__theme-input:checked + .rpl-17__theme svg {
  transform: rotate(180deg);
}

.rpl-17__theme-input:focus-visible + .rpl-17__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-17__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-17__theme,
    .rpl-17__theme svg {
    transition: none;
  }
}
```
