---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/preserve-3d-and-what-flattens-a-scene/"
title: "Preserve 3D and What Flattens a Scene"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "The most common 3D bug in CSS, catalogued."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Preserve 3D and What Flattens a Scene
Source: https://codefronts.com/design-styles/css-3d/preserve-3d-and-what-flattens-a-scene/

The most common 3D bug in CSS, catalogued. transform-style: preserve-3d lets children hold their own Z position, but a grouping property on an ancestor silently forces flattening: overflow, filter, opacity below 1, mask, clip-path and contain: paint. One correct scene, then the same scene broken six ways, each labelled with its culprit.
## HTML
```html
<section class="d3-06" aria-labelledby="d3-06-title">
  <h2 class="d3-06__sr" id="d3-06-title">What flattens a preserve-3d scene</h2>

  <div class="d3-06__theme">
    <input class="d3-06__theme-input" type="checkbox" id="d3-06-theme">
    <label class="d3-06__theme-label" for="d3-06-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-06__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-06__stage">
    <div class="d3-06__viewport">
      <header class="d3-06__head">
        <div>
          <span class="d3-06__kicker">Scene diagnostics</span>
          <strong>Six properties that quietly flatten your 3D</strong>
        </div>
        <span class="d3-06__score"><b>1</b> / 7 scenes still have depth</span>
      </header>

      <ul class="d3-06__grid">
        <li class="d3-06__cell d3-06__cell--ok">
          <div class="d3-06__mini">
            <span class="d3-06__plate d3-06__plate--back"></span>
            <span class="d3-06__plate d3-06__plate--front">Z</span>
          </div>
          <code class="d3-06__code">preserve-3d only</code>
          <span class="d3-06__note">Reference &mdash; two plates, real depth</span>
        </li>
        <li class="d3-06__cell">
          <div class="d3-06__mini d3-06__mini--overflow">
            <span class="d3-06__plate d3-06__plate--back"></span>
            <span class="d3-06__plate d3-06__plate--front">Z</span>
          </div>
          <code class="d3-06__code">overflow: hidden</code>
          <span class="d3-06__note">Clipping forces a flattened group</span>
        </li>
        <li class="d3-06__cell">
          <div class="d3-06__mini d3-06__mini--filter">
            <span class="d3-06__plate d3-06__plate--back"></span>
            <span class="d3-06__plate d3-06__plate--front">Z</span>
          </div>
          <code class="d3-06__code">filter: blur(2px)</code>
          <span class="d3-06__note">Any filter, including a no-op value</span>
        </li>
        <li class="d3-06__cell">
          <div class="d3-06__mini d3-06__mini--opacity">
            <span class="d3-06__plate d3-06__plate--back"></span>
            <span class="d3-06__plate d3-06__plate--front">Z</span>
          </div>
          <code class="d3-06__code">opacity: 0.85</code>
          <span class="d3-06__note">Below 1 creates a group</span>
        </li>
        <li class="d3-06__cell">
          <div class="d3-06__mini d3-06__mini--mask">
            <span class="d3-06__plate d3-06__plate--back"></span>
            <span class="d3-06__plate d3-06__plate--front">Z</span>
          </div>
          <code class="d3-06__code">mask-image: linear-gradient(...)</code>
          <span class="d3-06__note">Masking groups the subtree</span>
        </li>
        <li class="d3-06__cell">
          <div class="d3-06__mini d3-06__mini--contain">
            <span class="d3-06__plate d3-06__plate--back"></span>
            <span class="d3-06__plate d3-06__plate--front">Z</span>
          </div>
          <code class="d3-06__code">contain: paint</code>
          <span class="d3-06__note">Paint containment flattens</span>
        </li>
        <li class="d3-06__cell">
          <div class="d3-06__mini d3-06__mini--flat">
            <span class="d3-06__plate d3-06__plate--back"></span>
            <span class="d3-06__plate d3-06__plate--front">Z</span>
          </div>
          <code class="d3-06__code">transform-style: flat</code>
          <span class="d3-06__note">The direct override</span>
        </li>
      </ul>

      <p class="d3-06__note d3-06__note--foot">Every red tile has the same markup as the reference. One extra declaration on the parent is the only difference &mdash; and nothing in DevTools warns you.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-06 {
  --d3-06-bg: #f3f5f8;
  --d3-06-surf: #ffffff;
  --d3-06-line: #dbe1ea;
  --d3-06-grid: #e7ecf3;
  --d3-06-ink: #101620;
  --d3-06-mut: #5b6577;
  --d3-06-acc: #e0342a;
  --d3-06-acc: oklch(58% 0.21 27);
  --d3-06-ok: #0f9d58;
  --d3-06-ok: oklch(62% 0.15 156);
  --d3-06-z: 34px;
  --d3-06-font-display: "Segoe UI", "Noto Sans", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--d3-06-bg);
  background-image: radial-gradient(50rem 26rem at 92% -10%, color-mix(in oklab, var(--d3-06-acc) 12%, transparent), transparent 60%), linear-gradient(var(--d3-06-grid) 1px, transparent 1px), linear-gradient(90deg, var(--d3-06-grid) 1px, transparent 1px);
  background-size: auto, 24px 24px, 24px 24px;
  color: var(--d3-06-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-06 *,
.d3-06 *::before,
.d3-06 *::after {
  box-sizing: border-box;
}

.d3-06__sr {
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

.d3-06:has(.d3-06__theme-input:checked) {
  --d3-06-bg: #0a0e15;
  --d3-06-surf: #131a25;
  --d3-06-line: #26313f;
  --d3-06-grid: #121924;
  --d3-06-ink: #eef2f8;
  --d3-06-mut: #98a4b6;
  --d3-06-acc: #ff7a6d;
  --d3-06-acc: oklch(73% 0.17 27);
  --d3-06-ok: #45d68d;
  --d3-06-ok: oklch(80% 0.15 156);
}

@media (prefers-color-scheme: dark) {
  .d3-06 {
    --d3-06-bg: #0a0e15;
    --d3-06-surf: #131a25;
    --d3-06-line: #26313f;
    --d3-06-grid: #121924;
    --d3-06-ink: #eef2f8;
    --d3-06-mut: #98a4b6;
    --d3-06-acc: #ff7a6d;
    --d3-06-acc: oklch(73% 0.17 27);
    --d3-06-ok: #45d68d;
    --d3-06-ok: oklch(80% 0.15 156);
  }

  .d3-06:has(.d3-06__theme-input:checked) {
    --d3-06-bg: #f3f5f8;
    --d3-06-surf: #ffffff;
    --d3-06-line: #dbe1ea;
    --d3-06-grid: #e7ecf3;
    --d3-06-ink: #101620;
    --d3-06-mut: #5b6577;
    --d3-06-acc: #e0342a;
    --d3-06-acc: oklch(58% 0.21 27);
    --d3-06-ok: #0f9d58;
    --d3-06-ok: oklch(62% 0.15 156);
  }
}

@media (prefers-color-scheme: light) {
  .d3-06:has(.d3-06__theme-input:checked) {
    --d3-06-bg: #0a0e15;
    --d3-06-surf: #131a25;
    --d3-06-line: #26313f;
    --d3-06-grid: #121924;
    --d3-06-ink: #eef2f8;
    --d3-06-mut: #98a4b6;
    --d3-06-acc: #ff7a6d;
    --d3-06-acc: oklch(73% 0.17 27);
    --d3-06-ok: #45d68d;
    --d3-06-ok: oklch(80% 0.15 156);
  }
}

.d3-06__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-06__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-06__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-06-line);
  border-radius: 12px;
  background: var(--d3-06-surf);
  color: var(--d3-06-ink);
  cursor: pointer;
}

.d3-06__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-06__theme-input:focus-visible + .d3-06__theme-label {
  outline: 2px solid var(--d3-06-acc);
  outline-offset: 3px;
}

.d3-06__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-06__viewport {
  inline-size: 100%;
  max-inline-size: 66rem;
  overflow: hidden;
  display: grid;
  gap: clamp(1rem, 3vw, 1.6rem);
  padding: clamp(1rem, 3.5vw, 2rem);
  border: 1px solid var(--d3-06-line);
  border-radius: 22px;
  background: color-mix(in oklab, var(--d3-06-surf) 82%, transparent);
  box-shadow: 0 30px 70px -40px rgba(16, 22, 32, 0.7);
}

.d3-06__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 0.75rem;
}

.d3-06__kicker {
  display: block;
  font: 700 0.64rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--d3-06-acc);
}

.d3-06__head strong {
  font: 700 clamp(1.15rem, 3.8vw, 1.85rem)/1.1 var(--d3-06-font-display);
  letter-spacing: -0.02em;
}

.d3-06__score {
  padding: 0.35rem 0.7rem;
  border-radius: 999px;
  border: 1px solid var(--d3-06-line);
  background: var(--d3-06-surf);
  font: 500 0.72rem/1.2 ui-monospace, Menlo, monospace;
  color: var(--d3-06-mut);
}

.d3-06__score b {
  color: var(--d3-06-ok);
}

.d3-06__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
  gap: clamp(0.6rem, 2.2vw, 1rem);
}

.d3-06__cell {
  display: grid;
  gap: 0.45rem;
  padding: clamp(0.7rem, 2.2vw, 0.95rem);
  border: 1px solid var(--d3-06-line);
  border-radius: 16px;
  background: var(--d3-06-surf);
  box-shadow: 0 10px 24px -18px rgba(16, 22, 32, 0.8);
}

.d3-06__cell--ok {
  border-color: color-mix(in oklab, var(--d3-06-ok) 55%, var(--d3-06-line));
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--d3-06-ok) 14%, transparent);
}

.d3-06__mini {
  position: relative;
  block-size: 5.5rem;
  border-radius: 10px;
  background: color-mix(in oklab, var(--d3-06-ink) 5%, transparent);
  perspective: 560px;
  perspective-origin: 50% 40%;
  display: grid;
  place-items: center;
}

.d3-06__mini::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 10px;
  background-image: linear-gradient(color-mix(in oklab, var(--d3-06-mut) 18%, transparent) 1px, transparent 1px);
  background-size: 100% 12px;
  pointer-events: none;
}

.d3-06__plate {
  position: absolute;
  inline-size: 54%;
  block-size: 54%;
  border-radius: 8px;
  display: grid;
  place-items: center;
  font: 700 0.72rem/1 ui-monospace, Menlo, monospace;
}

.d3-06__plate--back {
  background: color-mix(in oklab, var(--d3-06-mut) 30%, transparent);
  border: 1px solid var(--d3-06-line);
}

.d3-06__plate--front {
  background: linear-gradient(150deg, var(--d3-06-ok), color-mix(in oklab, var(--d3-06-ok) 55%, #04241a));
  color: #fff;
}

.d3-06__cell--ok .d3-06__mini,
.d3-06__mini--overflow,
.d3-06__mini--filter,
.d3-06__mini--opacity,
.d3-06__mini--mask,
.d3-06__mini--contain,
.d3-06__mini--flat {
  transform-style: preserve-3d;
}

.d3-06__cell .d3-06__plate--front {
  transform: translateZ(var(--d3-06-z)) rotateY(-22deg);
}

.d3-06__cell .d3-06__plate--back {
  transform: translateZ(calc(var(--d3-06-z) * -1)) rotateY(-22deg);
}

.d3-06__mini--overflow {
  overflow: hidden;
}

.d3-06__mini--filter {
  filter: blur(0.4px);
}

.d3-06__mini--opacity {
  opacity: 0.85;
}

.d3-06__mini--mask {
  -webkit-mask-image: linear-gradient(#000, #000);
  mask-image: linear-gradient(#000, #000);
}

.d3-06__mini--contain {
  contain: paint;
}

.d3-06__mini--flat {
  transform-style: flat;
}

.d3-06__mini--overflow .d3-06__plate--front,
.d3-06__mini--filter .d3-06__plate--front,
.d3-06__mini--opacity .d3-06__plate--front,
.d3-06__mini--mask .d3-06__plate--front,
.d3-06__mini--contain .d3-06__plate--front,
.d3-06__mini--flat .d3-06__plate--front {
  background: linear-gradient(150deg, var(--d3-06-acc), color-mix(in oklab, var(--d3-06-acc) 55%, #2a0605));
}

.d3-06__code {
  font: 600 clamp(0.66rem, 1.9vw, 0.76rem)/1.3 ui-monospace, Menlo, monospace;
  color: var(--d3-06-ink);
  overflow-wrap: anywhere;
}

.d3-06__cell--ok .d3-06__code {
  color: var(--d3-06-ok);
}

.d3-06__note {
  font: 500 clamp(0.66rem, 1.8vw, 0.74rem)/1.35 system-ui, sans-serif;
  color: var(--d3-06-mut);
}

.d3-06__note--foot {
  max-inline-size: 60ch;
  text-wrap: pretty;
}
```
