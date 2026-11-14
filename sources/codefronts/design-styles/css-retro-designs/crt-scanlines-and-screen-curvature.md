---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/crt-scanlines-and-screen-curvature/"
title: "CRT Scanlines and Screen Curvature"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A CRT look is not one effect, it is four: scanlines, curvature, phosphor bloom and mains flicker."
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CRT Scanlines and Screen Curvature
Source: https://codefronts.com/design-styles/css-retro-designs/crt-scanlines-and-screen-curvature/

A CRT look is not one effect, it is four: scanlines, curvature, phosphor bloom and mains flicker. Each one is a separate layer here with its own switch, so you can stack them one at a time and see what each contributes. The reference build the rest of the collection borrows from, including the fix for 1px scanlines aliasing on fractional device pixel ratios.
## HTML
```html
<section class="rt-01" aria-labelledby="rt-01-title">
  <h2 class="rt-01__sr" id="rt-01-title">CRT scanline and curvature layer stack</h2>

  <div class="rt-01__theme">
    <input class="rt-01__theme-input" type="checkbox" id="rt-01-theme">
    <label class="rt-01__theme-label" for="rt-01-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-01__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-01__stage">
    <p class="rt-01__badge">Cathode-ray tube &middot; shadow-mask display</p>

    <div class="rt-01__rig">
      <div class="rt-01__bezel">
        <div class="rt-01__screen">
          <div class="rt-01__content">
            <p class="rt-01__line rt-01__line--dim">SYSTEM MONITOR &mdash; VT/CRT COMPOSITE</p>
            <p class="rt-01__big" data-rt-01-text="PHOSPHOR">PHOSPHOR</p>
            <p class="rt-01__line">SCAN 15.734 kHz &nbsp; VERT 59.94 Hz</p>
            <p class="rt-01__line">MASK PITCH 0.28 mm &nbsp; DEFL 90&deg;</p>
            <p class="rt-01__line rt-01__line--dim">READY<span class="rt-01__caret" aria-hidden="true"></span></p>
          </div>
          <div class="rt-01__bloom" aria-hidden="true">
            <p class="rt-01__big">PHOSPHOR</p>
          </div>
          <div class="rt-01__scan" aria-hidden="true"></div>
          <div class="rt-01__vig" aria-hidden="true"></div>
          <div class="rt-01__flick" aria-hidden="true"></div>
        </div>
        <div class="rt-01__chin">
          <span class="rt-01__brand">TRINITRON&nbsp;/&nbsp;14"</span>
          <span class="rt-01__led" aria-hidden="true"></span>
        </div>
      </div>

      <ul class="rt-01__panel">
        <li class="rt-01__switch">
          <input class="rt-01__cb" type="checkbox" id="rt-01-scan" checked>
          <label class="rt-01__lb" for="rt-01-scan">
            <span class="rt-01__lb-n">01</span>
            <span class="rt-01__lb-t">Scanlines</span>
            <span class="rt-01__lb-d">repeating-linear-gradient, 3px period</span>
          </label>
        </li>
        <li class="rt-01__switch">
          <input class="rt-01__cb" type="checkbox" id="rt-01-curve" checked>
          <label class="rt-01__lb" for="rt-01-curve">
            <span class="rt-01__lb-n">02</span>
            <span class="rt-01__lb-t">Curvature</span>
            <span class="rt-01__lb-d">border-radius plus inset corner vignette</span>
          </label>
        </li>
        <li class="rt-01__switch">
          <input class="rt-01__cb" type="checkbox" id="rt-01-bloom" checked>
          <label class="rt-01__lb" for="rt-01-bloom">
            <span class="rt-01__lb-n">03</span>
            <span class="rt-01__lb-t">Phosphor bloom</span>
            <span class="rt-01__lb-d">blurred duplicate, mix-blend-mode: screen</span>
          </label>
        </li>
        <li class="rt-01__switch">
          <input class="rt-01__cb" type="checkbox" id="rt-01-flick" checked>
          <label class="rt-01__lb" for="rt-01-flick">
            <span class="rt-01__lb-n">04</span>
            <span class="rt-01__lb-t">Mains flicker</span>
            <span class="rt-01__lb-d">6s opacity cycle, stops under reduced motion</span>
          </label>
        </li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
.rt-01 {
  --rt-01-scan: 3px;
  --rt-01-curve: 26px;
  --rt-01-bloom: 3px;
  --rt-01-flicker-dur: 6s;
  --rt-01-scan-on: 1;
  --rt-01-curve-on: 1;
  --rt-01-bloom-on: 1;
  --rt-01-flick-on: 1;
  --rt-01-glow: #7cf6b0;
  --rt-01-glow-dim: #4fbf88;
  --rt-01-tube: #04100b;
  --rt-01-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
  --rt-01-bg: #d9dde1;
  --rt-01-bg: oklch(88% 0.006 240);
  --rt-01-surface: #f4f6f7;
  --rt-01-surface: oklch(97% 0.003 240);
  --rt-01-ink: #14181b;
  --rt-01-ink: oklch(19% 0.008 240);
  --rt-01-ink-2: #4a545c;
  --rt-01-ink-2: oklch(43% 0.014 240);
  --rt-01-line: #a9b1b8;
  --rt-01-line: oklch(75% 0.009 240);
  --rt-01-case: #b9beb6;
  --rt-01-case-2: #8f948c;
  --rt-01-acc: #0f6bd8;
  --rt-01-acc: oklch(52% 0.19 252);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-01-bg);
  color: var(--rt-01-ink);
  font-family: var(--rt-01-mono);
  -webkit-text-size-adjust: 100%;
}

.rt-01 *,
.rt-01 *::before,
.rt-01 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-01 {
    --rt-01-bg: #101314;
    --rt-01-bg: oklch(18% 0.005 200);
    --rt-01-surface: #1b2022;
    --rt-01-surface: oklch(24% 0.007 200);
    --rt-01-ink: #eef2f3;
    --rt-01-ink: oklch(96% 0.003 200);
    --rt-01-ink-2: #a2acb1;
    --rt-01-ink-2: oklch(74% 0.009 200);
    --rt-01-line: #394246;
    --rt-01-line: oklch(35% 0.01 200);
    --rt-01-acc: #6fb2ff;
    --rt-01-acc: oklch(76% 0.13 252);
  }
}

.rt-01[data-theme="dark"],
.rt-01:has(.rt-01__theme-input:checked) {
  --rt-01-bg: #101314;
  --rt-01-bg: oklch(18% 0.005 200);
  --rt-01-surface: #1b2022;
  --rt-01-surface: oklch(24% 0.007 200);
  --rt-01-ink: #eef2f3;
  --rt-01-ink: oklch(96% 0.003 200);
  --rt-01-ink-2: #a2acb1;
  --rt-01-ink-2: oklch(74% 0.009 200);
  --rt-01-line: #394246;
  --rt-01-line: oklch(35% 0.01 200);
  --rt-01-acc: #6fb2ff;
  --rt-01-acc: oklch(76% 0.13 252);
}

@media (prefers-color-scheme: light) {
  .rt-01:has(.rt-01__theme-input:checked) {
    --rt-01-bg: #101314;
    --rt-01-bg: oklch(18% 0.005 200);
    --rt-01-surface: #1b2022;
    --rt-01-surface: oklch(24% 0.007 200);
    --rt-01-ink: #eef2f3;
    --rt-01-ink: oklch(96% 0.003 200);
    --rt-01-ink-2: #a2acb1;
    --rt-01-ink-2: oklch(74% 0.009 200);
    --rt-01-line: #394246;
    --rt-01-line: oklch(35% 0.01 200);
    --rt-01-acc: #6fb2ff;
    --rt-01-acc: oklch(76% 0.13 252);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-01:has(.rt-01__theme-input:checked) {
    --rt-01-bg: #d9dde1;
    --rt-01-bg: oklch(88% 0.006 240);
    --rt-01-surface: #f4f6f7;
    --rt-01-surface: oklch(97% 0.003 240);
    --rt-01-ink: #14181b;
    --rt-01-ink: oklch(19% 0.008 240);
    --rt-01-ink-2: #4a545c;
    --rt-01-ink-2: oklch(43% 0.014 240);
    --rt-01-line: #a9b1b8;
    --rt-01-line: oklch(75% 0.009 240);
    --rt-01-acc: #0f6bd8;
    --rt-01-acc: oklch(52% 0.19 252);
  }
}

.rt-01:has(#rt-01-scan:not(:checked)) {
  --rt-01-scan-on: 0;
}

.rt-01:has(#rt-01-curve:not(:checked)) {
  --rt-01-curve-on: 0;
  --rt-01-curve: 2px;
}

.rt-01:has(#rt-01-bloom:not(:checked)) {
  --rt-01-bloom-on: 0;
}

.rt-01:has(#rt-01-flick:not(:checked)) {
  --rt-01-flick-on: 0;
}

.rt-01__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-01__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-01__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-01__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-01-line);
  border-radius: 50%;
  background: var(--rt-01-surface);
  color: var(--rt-01-ink-2);
  cursor: pointer;
}

.rt-01__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-01__theme-input:focus-visible + .rt-01__theme-label {
  outline: 2px solid var(--rt-01-acc);
  outline-offset: 2px;
}

.rt-01__stage {
  max-inline-size: 74rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.85rem, 0.5rem + 2vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.rt-01__badge {
  margin: 0;
  justify-self: start;
  min-inline-size: 0;
  font-size: 0.7rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--rt-01-ink-2);
  border: 1px solid var(--rt-01-line);
  padding: 0.35rem 0.7rem;
  border-radius: 2px;
  background: var(--rt-01-surface);
}

.rt-01__rig {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
  align-items: start;
}

.rt-01__bezel {
  min-inline-size: 0;
  position: relative;
  background: linear-gradient(180deg, var(--rt-01-case) 0%, var(--rt-01-case-2) 100%);
  border-radius: calc(var(--rt-01-curve) + 18px);
  padding: clamp(0.9rem, 0.6rem + 1.4vw, 1.6rem);
  box-shadow: inset 0 2px 0 rgba(255, 255, 255, 0.55), inset 0 -2px 0 rgba(0, 0, 0, 0.35), 0 18px 40px -18px rgba(0, 0, 0, 0.65);
}

.rt-01__screen {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  border-radius: var(--rt-01-curve);
  background: radial-gradient(120% 100% at 50% 45%, #0a2018 0%, var(--rt-01-tube) 72%);
  aspect-ratio: 4 / 3;
  display: grid;
  place-items: center;
  box-shadow: inset 0 0 0 2px #06120d, inset 0 0 30px 6px rgba(0, 0, 0, 0.75);
  transition: border-radius 240ms ease;
}

.rt-01__content {
  position: relative;
  z-index: 2;
  min-inline-size: 0;
  padding: clamp(0.75rem, 0.4rem + 2vw, 2rem);
  text-align: center;
  color: var(--rt-01-glow);
  display: grid;
  gap: 0.55rem;
  justify-items: center;
}

.rt-01__line {
  margin: 0;
  font-size: clamp(0.6rem, 0.45rem + 0.7vw, 0.85rem);
  letter-spacing: 0.1em;
  color: var(--rt-01-glow);
}

.rt-01__line--dim {
  color: var(--rt-01-glow-dim);
}

.rt-01__big {
  margin: 0;
  font-size: clamp(1.6rem, 0.6rem + 6.5vw, 4rem);
  letter-spacing: 0.14em;
  font-weight: 700;
  line-height: 1;
  color: var(--rt-01-glow);
}

.rt-01__caret {
  display: inline-block;
  inline-size: 0.6em;
  block-size: 1em;
  margin-inline-start: 0.3em;
  background: var(--rt-01-glow);
  vertical-align: -0.15em;
  animation: rt-01-blink 1.2s steps(1, end) infinite;
}

.rt-01__bloom {
  position: absolute;
  inset: 0;
  z-index: 3;
  display: grid;
  place-items: center;
  pointer-events: none;
  mix-blend-mode: screen;
  filter: blur(var(--rt-01-bloom));
  opacity: calc(0.85 * var(--rt-01-bloom-on));
  transition: opacity 200ms ease;
}

.rt-01__bloom .rt-01__big {
  color: var(--rt-01-glow);
}

.rt-01__scan {
  position: absolute;
  inset: 0;
  z-index: 4;
  pointer-events: none;
  opacity: calc(0.55 * var(--rt-01-scan-on));
  background: repeating-linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0) 0,
      rgba(0, 0, 0, 0) calc(var(--rt-01-scan) - 1px),
      rgba(0, 0, 0, 0.72) calc(var(--rt-01-scan) - 1px),
      rgba(0, 0, 0, 0.72) var(--rt-01-scan)
    );
  transition: opacity 200ms ease;
}

@media (min-resolution: 1.5dppx) {
  .rt-01__scan {
    background: repeating-linear-gradient(
          to bottom,
          rgba(0, 0, 0, 0) 0,
          rgba(0, 0, 0, 0.62) calc(var(--rt-01-scan) * 0.5),
          rgba(0, 0, 0, 0) calc(var(--rt-01-scan) * 1.34)
        );
  }
}

.rt-01__vig {
  position: absolute;
  inset: -1px;
  z-index: 5;
  pointer-events: none;
  opacity: var(--rt-01-curve-on);
  background: radial-gradient(115% 105% at 50% 50%, rgba(0, 0, 0, 0) 52%, rgba(0, 0, 0, 0.55) 84%, rgba(0, 0, 0, 0.9) 100%), linear-gradient(90deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0) 18% 82%, rgba(255, 255, 255, 0.05));
  transition: opacity 200ms ease;
}

.rt-01__flick {
  position: absolute;
  inset: 0;
  z-index: 6;
  pointer-events: none;
  background: rgba(120, 255, 190, 0.05);
  opacity: 0;
  animation: rt-01-flicker var(--rt-01-flicker-dur) ease-in-out infinite;
  animation-play-state: running;
}

.rt-01:has(#rt-01-flick:not(:checked)) .rt-01__flick {
  animation: none;
  opacity: 0;
}

.rt-01__chin {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.75rem 0.35rem 0.1rem;
  min-inline-size: 0;
}

.rt-01__brand {
  font-size: 0.62rem;
  letter-spacing: 0.22em;
  color: #3c4038;
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.45);
  min-inline-size: 0;
}

.rt-01__led {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  flex: none;
  background: #63f0a0;
  box-shadow: 0 0 8px 2px rgba(99, 240, 160, 0.7), inset 0 0 2px #0a3a22;
}

.rt-01__panel {
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.5rem;
  align-content: start;
}

.rt-01__switch {
  position: relative;
  min-inline-size: 0;
}

.rt-01__cb {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 44px;
  block-size: 44px;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.rt-01__lb {
  display: grid;
  grid-template-columns: 44px minmax(0, 1fr);
  gap: 0 0.7rem;
  align-items: center;
  min-block-size: 56px;
  cursor: pointer;
  background: var(--rt-01-surface);
  border: 1px solid var(--rt-01-line);
  border-radius: 3px;
  padding: 0.5rem 0.75rem 0.5rem 0.5rem;
}

.rt-01__lb-n {
  grid-row: 1 / 3;
  display: grid;
  place-items: center;
  inline-size: 34px;
  block-size: 34px;
  margin-inline-start: 5px;
  border: 2px solid var(--rt-01-ink-2);
  border-radius: 2px;
  font-size: 0.72rem;
  color: var(--rt-01-ink-2);
  font-variant-numeric: tabular-nums;
}

.rt-01__cb:checked + .rt-01__lb .rt-01__lb-n {
  background: var(--rt-01-ink);
  border-color: var(--rt-01-ink);
  color: var(--rt-01-surface);
}

.rt-01__lb-t {
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  min-inline-size: 0;
}

.rt-01__lb-d {
  font-size: 0.68rem;
  color: var(--rt-01-ink-2);
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.rt-01__cb:focus-visible + .rt-01__lb {
  outline: 2px solid var(--rt-01-acc);
  outline-offset: 2px;
}

.rt-01__cb:checked + .rt-01__lb {
  border-color: var(--rt-01-ink-2);
}

@keyframes rt-01-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

@keyframes rt-01-flicker {
  0%,
    96%,
    100% {
    opacity: 0;
  }

  97% {
    opacity: 0.5;
  }

  98% {
    opacity: 0.12;
  }

  99% {
    opacity: 0.38;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rt-01__flick,
    .rt-01__caret {
    animation: none;
  }

  .rt-01__caret {
    opacity: 1;
  }

  .rt-01__screen {
    transition: none;
  }
}

@media (min-width: 62rem) {
  .rt-01__rig {
    grid-template-columns: minmax(0, 1.55fr) minmax(0, 1fr);
    gap: 2rem;
  }

  .rt-01__panel {
    gap: 0.65rem;
  }
}
```
