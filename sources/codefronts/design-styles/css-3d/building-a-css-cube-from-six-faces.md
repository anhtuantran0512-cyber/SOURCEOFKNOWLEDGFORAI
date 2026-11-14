---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/building-a-css-cube-from-six-faces/"
title: "Building a CSS Cube from Six Faces"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "The canonical construction, derived rather than hardcoded: six absolutely positioned faces, each rotated into place and pushed out by half the edge length."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Building a CSS Cube from Six Faces
Source: https://codefronts.com/design-styles/css-3d/building-a-css-cube-from-six-faces/

The canonical construction, derived rather than hardcoded: six absolutely positioned faces, each rotated into place and pushed out by half the edge length. One custom property sets the cube's size and every translateZ follows from it through calc(), so resizing is a single edit instead of six.
## HTML
```html
<section class="d3-07" aria-labelledby="d3-07-title">
  <h2 class="d3-07__sr" id="d3-07-title">Cube built from six faces</h2>

  <div class="d3-07__theme">
    <input class="d3-07__theme-input" type="checkbox" id="d3-07-theme">
    <label class="d3-07__theme-label" for="d3-07-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-07__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-07__stage">
    <div class="d3-07__viewport">
      <header class="d3-07__head">
        <span class="d3-07__kicker">Ostfeld Roasters &mdash; packaging</span>
        <strong>Six faces, one&nbsp;box</strong>
      </header>

      <div class="d3-07__scene">
        <div class="d3-07__cube">
          <article class="d3-07__face d3-07__face--front"><span class="d3-07__eyebrow">Single origin</span><b>Kaffee<br>No.&nbsp;04</b><span class="d3-07__foot">250 g &middot; whole bean</span></article>
          <article class="d3-07__face d3-07__face--right"><span class="d3-07__eyebrow">Roast</span><b>Dark</b><span class="d3-07__foot">Agtron 42</span></article>
          <article class="d3-07__face d3-07__face--back"><span class="d3-07__eyebrow">Notes</span><b>Cocoa<br>Fig</b><span class="d3-07__foot">Ethiopia &middot; 1900m</span></article>
          <article class="d3-07__face d3-07__face--left"><span class="d3-07__eyebrow">Batch</span><b>04&nbsp;/&nbsp;26</b><span class="d3-07__foot">Roasted 12 Aug</span></article>
          <article class="d3-07__face d3-07__face--top"><b class="d3-07__mark">O</b></article>
          <article class="d3-07__face d3-07__face--bottom"><span class="d3-07__foot">EAN 5 012345 678900</span></article>
        </div>
      </div>

      <ol class="d3-07__net">
        <li><span class="d3-07__swatch d3-07__swatch--f"></span>front <code>translateZ(s/2)</code></li>
        <li><span class="d3-07__swatch d3-07__swatch--r"></span>right <code>rotateY(90deg)</code></li>
        <li><span class="d3-07__swatch d3-07__swatch--b"></span>back <code>rotateY(180deg)</code></li>
        <li><span class="d3-07__swatch d3-07__swatch--l"></span>left <code>rotateY(-90deg)</code></li>
        <li><span class="d3-07__swatch d3-07__swatch--t"></span>top <code>rotateX(90deg)</code></li>
        <li><span class="d3-07__swatch d3-07__swatch--u"></span>bottom <code>rotateX(-90deg)</code></li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-07 {
  --d3-07-bg: #f4f2ec;
  --d3-07-surf: #ffffff;
  --d3-07-line: #1a1815;
  --d3-07-ink: #14120f;
  --d3-07-mut: #6a6358;
  --d3-07-red: #e03a24;
  --d3-07-red: oklch(58% 0.2 32);
  --d3-07-blue: #1b48d8;
  --d3-07-blue: oklch(48% 0.21 264);
  --d3-07-yellow: #f2bd12;
  --d3-07-yellow: oklch(84% 0.16 92);
  --d3-07-green: #17795a;
  --d3-07-green: oklch(50% 0.11 165);
  --d3-07-size: clamp(9rem, 30vw, 14rem);
  --d3-07-spin: 26s;
  --d3-07-font-display: "Futura", "Century Gothic", "Avenir Next", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(46rem 24rem at 82% -8%, color-mix(in oklab, var(--d3-07-yellow) 30%, transparent), transparent 62%), var(--d3-07-bg);
  color: var(--d3-07-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-07 *,
.d3-07 *::before,
.d3-07 *::after {
  box-sizing: border-box;
}

.d3-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.d3-07:has(.d3-07__theme-input:checked) {
  --d3-07-bg: #100f0d;
  --d3-07-surf: #191714;
  --d3-07-line: #efece5;
  --d3-07-ink: #f4f1ea;
  --d3-07-mut: #a49c8e;
  --d3-07-red: #ff7a5e;
  --d3-07-red: oklch(74% 0.16 32);
  --d3-07-blue: #7f9dff;
  --d3-07-blue: oklch(76% 0.14 264);
  --d3-07-yellow: #f8d95c;
  --d3-07-yellow: oklch(89% 0.14 92);
  --d3-07-green: #55c79c;
  --d3-07-green: oklch(76% 0.11 165);
}

@media (prefers-color-scheme: dark) {
  .d3-07 {
    --d3-07-bg: #100f0d;
    --d3-07-surf: #191714;
    --d3-07-line: #efece5;
    --d3-07-ink: #f4f1ea;
    --d3-07-mut: #a49c8e;
    --d3-07-red: #ff7a5e;
    --d3-07-red: oklch(74% 0.16 32);
    --d3-07-blue: #7f9dff;
    --d3-07-blue: oklch(76% 0.14 264);
    --d3-07-yellow: #f8d95c;
    --d3-07-yellow: oklch(89% 0.14 92);
    --d3-07-green: #55c79c;
    --d3-07-green: oklch(76% 0.11 165);
  }

  .d3-07:has(.d3-07__theme-input:checked) {
    --d3-07-bg: #f4f2ec;
    --d3-07-surf: #ffffff;
    --d3-07-line: #1a1815;
    --d3-07-ink: #14120f;
    --d3-07-mut: #6a6358;
    --d3-07-red: #e03a24;
    --d3-07-red: oklch(58% 0.2 32);
    --d3-07-blue: #1b48d8;
    --d3-07-blue: oklch(48% 0.21 264);
    --d3-07-yellow: #f2bd12;
    --d3-07-yellow: oklch(84% 0.16 92);
    --d3-07-green: #17795a;
    --d3-07-green: oklch(50% 0.11 165);
  }
}

@media (prefers-color-scheme: light) {
  .d3-07:has(.d3-07__theme-input:checked) {
    --d3-07-bg: #100f0d;
    --d3-07-surf: #191714;
    --d3-07-line: #efece5;
    --d3-07-ink: #f4f1ea;
    --d3-07-mut: #a49c8e;
    --d3-07-red: #ff7a5e;
    --d3-07-red: oklch(74% 0.16 32);
    --d3-07-blue: #7f9dff;
    --d3-07-blue: oklch(76% 0.14 264);
    --d3-07-yellow: #f8d95c;
    --d3-07-yellow: oklch(89% 0.14 92);
    --d3-07-green: #55c79c;
    --d3-07-green: oklch(76% 0.11 165);
  }
}

.d3-07__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-07__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-07__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 2px solid var(--d3-07-line);
  background: var(--d3-07-surf);
  color: var(--d3-07-ink);
  cursor: pointer;
}

.d3-07__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-07__theme-input:focus-visible + .d3-07__theme-label {
  outline: 2px solid var(--d3-07-blue);
  outline-offset: 3px;
}

.d3-07__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-07__viewport {
  inline-size: 100%;
  max-inline-size: 54rem;
  overflow: hidden;
  display: grid;
  gap: clamp(1rem, 3vw, 1.6rem);
}

.d3-07__head {
  display: grid;
  gap: 0.1rem;
}

.d3-07__kicker {
  font: 700 0.66rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--d3-07-red);
}

.d3-07__head strong {
  font: 700 clamp(1.6rem, 6vw, 3.1rem)/0.95 var(--d3-07-font-display);
  letter-spacing: -0.02em;
}

.d3-07__scene {
  perspective: clamp(700px, 92vw, 1400px);
  perspective-origin: 50% 40%;
  block-size: calc(var(--d3-07-size) * 1.9);
  display: grid;
  place-items: center;
}

.d3-07__cube {
  position: relative;
  inline-size: var(--d3-07-size);
  block-size: var(--d3-07-size);
  transform-style: preserve-3d;
  animation: d3-07-spin var(--d3-07-spin) linear infinite;
}

@keyframes d3-07-spin {
  from {
    transform: rotateX(-16deg) rotateY(0deg);
  }

  to {
    transform: rotateX(-16deg) rotateY(360deg);
  }
}

.d3-07__face {
  position: absolute;
  inset: 0;
  padding: clamp(0.7rem, 2.4vw, 1.1rem);
  display: grid;
  align-content: space-between;
  border: 2px solid var(--d3-07-line);
  backface-visibility: hidden;
  overflow: hidden;
}

.d3-07__face b {
  font: 700 clamp(1.05rem, 3.6vw, 1.7rem)/0.98 var(--d3-07-font-display);
  letter-spacing: -0.02em;
}

.d3-07__eyebrow {
  font: 700 0.6rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  opacity: 0.75;
}

.d3-07__foot {
  font: 500 0.62rem/1.3 ui-monospace, Menlo, monospace;
  opacity: 0.75;
}

.d3-07__face--front {
  transform: translateZ(calc(var(--d3-07-size) / 2));
  background: var(--d3-07-red);
  color: #fff;
}

.d3-07__face--right {
  transform: rotateY(90deg) translateZ(calc(var(--d3-07-size) / 2));
  background: var(--d3-07-yellow);
  color: #14120f;
}

.d3-07__face--back {
  transform: rotateY(180deg) translateZ(calc(var(--d3-07-size) / 2));
  background: var(--d3-07-blue);
  color: #fff;
}

.d3-07__face--left {
  transform: rotateY(-90deg) translateZ(calc(var(--d3-07-size) / 2));
  background: var(--d3-07-green);
  color: #fff;
}

.d3-07__face--top {
  transform: rotateX(90deg) translateZ(calc(var(--d3-07-size) / 2));
  background: var(--d3-07-ink);
  color: var(--d3-07-bg);
  place-content: center;
  place-items: center;
}

.d3-07__face--bottom {
  transform: rotateX(-90deg) translateZ(calc(var(--d3-07-size) / 2));
  background: var(--d3-07-surf);
  color: var(--d3-07-ink);
  align-content: end;
}

.d3-07__mark {
  font-size: clamp(2.5rem, 9vw, 4.5rem) !important;
  line-height: 0.8;
}

.d3-07__net {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: 0.4rem 0.9rem;
}

.d3-07__net li {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font: 500 clamp(0.66rem, 1.8vw, 0.74rem)/1.3 ui-monospace, Menlo, monospace;
  color: var(--d3-07-mut);
}

.d3-07__net code {
  color: var(--d3-07-ink);
}

.d3-07__swatch {
  inline-size: 0.85rem;
  block-size: 0.85rem;
  border: 1px solid var(--d3-07-line);
  flex: none;
}

.d3-07__swatch--f {
  background: var(--d3-07-red);
}

.d3-07__swatch--r {
  background: var(--d3-07-yellow);
}

.d3-07__swatch--b {
  background: var(--d3-07-blue);
}

.d3-07__swatch--l {
  background: var(--d3-07-green);
}

.d3-07__swatch--t {
  background: var(--d3-07-ink);
}

.d3-07__swatch--u {
  background: var(--d3-07-surf);
}

@media (prefers-reduced-motion: reduce) {
  .d3-07__cube {
    animation: none;
    transform: rotateX(-16deg) rotateY(-32deg);
  }
}
```
