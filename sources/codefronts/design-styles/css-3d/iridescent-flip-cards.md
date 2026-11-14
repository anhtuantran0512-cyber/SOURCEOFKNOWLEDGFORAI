---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/iridescent-flip-cards/"
title: "Depth Layering with Stacked Z Planes"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "Five parallel planes at different translateZ values, with no rotation anywhere in the scene."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Depth Layering with Stacked Z Planes
Source: https://codefronts.com/design-styles/css-3d/iridescent-flip-cards/

Five parallel planes at different translateZ values, with no rotation anywhere in the scene. Depth alone creates the stack: the camera sits off centre so the planes fan out, and each one is smaller than the one in front of it &mdash; which the last plane corrects with the compensating scale, so the maths is visible rather than asserted.
## HTML
```html
<section class="d3-13" aria-labelledby="d3-13-title">
  <h2 class="d3-13__sr" id="d3-13-title">Depth from stacked Z planes</h2>

  <div class="d3-13__theme">
    <input class="d3-13__theme-input" type="checkbox" id="d3-13-theme">
    <label class="d3-13__theme-label" for="d3-13-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-13__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-13__stage">
    <div class="d3-13__viewport">
      <div class="d3-13__scene">
        <div class="d3-13__deck">
          <div class="d3-13__plane d3-13__plane--sky" aria-hidden="true"><span class="d3-13__sun"></span></div>
          <div class="d3-13__plane d3-13__plane--far" aria-hidden="true"></div>
          <div class="d3-13__plane d3-13__plane--mid" aria-hidden="true"></div>
          <div class="d3-13__plane d3-13__plane--copy">
            <span class="d3-13__kicker">Expedition 04 &middot; Tromsø</span>
            <b class="d3-13__title">Aurora<br>Crossing</b>
            <span class="d3-13__sub">6 nights &middot; departures Jan&ndash;Mar</span>
          </div>
          <div class="d3-13__plane d3-13__plane--near" aria-hidden="true"></div>
          <div class="d3-13__plane d3-13__plane--ui">
            <span class="d3-13__price">from <b>&pound;1,840</b></span>
            <span class="d3-13__cta">Reserve a berth</span>
          </div>
        </div>
      </div>

      <ol class="d3-13__ruler">
        <li><b>sky</b><code>translateZ(-240px)</code></li>
        <li><b>ridge</b><code>translateZ(-180px)</code></li>
        <li><b>hills</b><code>translateZ(-120px)</code></li>
        <li><b>headline</b><code>translateZ(-60px)</code></li>
        <li><b>foreground</b><code>translateZ(0)</code></li>
        <li><b>controls</b><code>translateZ(60px)</code></li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-13 {
  --d3-13-bg: #060c1c;
  --d3-13-surf: #0d1730;
  --d3-13-line: #1e2c4d;
  --d3-13-ink: #eef3ff;
  --d3-13-mut: #93a3c6;
  --d3-13-acc: #ff8a3d;
  --d3-13-acc: oklch(75% 0.17 55);
  --d3-13-acc2: #59d2ff;
  --d3-13-acc2: oklch(82% 0.12 220);
  --d3-13-gap: 60px;
  --d3-13-depth: 900px;
  --d3-13-font-display: "Inter", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(56rem 28rem at 20% -10%, color-mix(in oklab, var(--d3-13-acc2) 20%, transparent), transparent 62%), radial-gradient(44rem 24rem at 96% 106%, color-mix(in oklab, var(--d3-13-acc) 20%, transparent), transparent 60%), var(--d3-13-bg);
  color: var(--d3-13-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-13 *,
.d3-13 *::before,
.d3-13 *::after {
  box-sizing: border-box;
}

.d3-13__sr {
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

.d3-13:has(.d3-13__theme-input:checked) {
  --d3-13-bg: #eef2f9;
  --d3-13-surf: #ffffff;
  --d3-13-line: #d3dceb;
  --d3-13-ink: #0a1122;
  --d3-13-mut: #55627d;
  --d3-13-acc: #b64a00;
  --d3-13-acc: oklch(56% 0.16 55);
  --d3-13-acc2: #0071a6;
  --d3-13-acc2: oklch(52% 0.13 230);
}

@media (prefers-color-scheme: light) {
  .d3-13:has(.d3-13__theme-input:checked) {
    --d3-13-bg: #eef2f9;
    --d3-13-surf: #ffffff;
    --d3-13-line: #d3dceb;
    --d3-13-ink: #0a1122;
    --d3-13-mut: #55627d;
    --d3-13-acc: #b64a00;
    --d3-13-acc: oklch(56% 0.16 55);
    --d3-13-acc2: #0071a6;
    --d3-13-acc2: oklch(52% 0.13 230);
  }
}

@media (prefers-color-scheme: dark) {
  .d3-13:has(.d3-13__theme-input:checked) {
    --d3-13-bg: #eef2f9;
    --d3-13-surf: #ffffff;
    --d3-13-line: #d3dceb;
    --d3-13-ink: #0a1122;
    --d3-13-mut: #55627d;
    --d3-13-acc: #b64a00;
    --d3-13-acc: oklch(56% 0.16 55);
    --d3-13-acc2: #0071a6;
    --d3-13-acc2: oklch(52% 0.13 230);
  }
}

.d3-13__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-13__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-13__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-13-line);
  border-radius: 14px;
  background: color-mix(in oklab, var(--d3-13-surf) 85%, transparent);
  color: var(--d3-13-ink);
  cursor: pointer;
}

.d3-13__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-13__theme-input:focus-visible + .d3-13__theme-label {
  outline: 2px solid var(--d3-13-acc);
  outline-offset: 3px;
}

.d3-13__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-13__viewport {
  inline-size: 100%;
  max-inline-size: 62rem;
  overflow: hidden;
  display: grid;
  gap: clamp(0.9rem, 3vw, 1.5rem);
}

.d3-13__scene {
  perspective: var(--d3-13-depth);
  perspective-origin: 50% 44%;
  block-size: clamp(17rem, 48vw, 25rem);
  display: grid;
  place-items: center;
}

.d3-13__deck {
  position: relative;
  inline-size: min(100%, 40rem);
  block-size: 100%;
  transform-style: preserve-3d;
  transform: rotateX(4deg) rotateY(-9deg);
  border-radius: 24px;
}

.d3-13__plane {
  position: absolute;
  inset: 0;
  border-radius: 24px;
  overflow: hidden;
}

.d3-13__plane--sky {
  transform: translateZ(calc(var(--d3-13-gap) * -4));
  background: linear-gradient(190deg, #0a1c46 0%, #16305e 45%, #2b4a72 100%);
  box-shadow: inset 0 0 120px rgba(0, 0, 0, 0.5);
}

.d3-13__sun {
  position: absolute;
  inset-block-start: 18%;
  inset-inline-start: 62%;
  inline-size: 6rem;
  block-size: 6rem;
  border-radius: 999px;
  background: radial-gradient(closest-side, color-mix(in oklab, var(--d3-13-acc) 90%, #fff), transparent 72%);
  filter: blur(1px);
}

.d3-13__plane--far {
  transform: translateZ(calc(var(--d3-13-gap) * -3));
  background: linear-gradient(180deg, transparent 46%, #12294f 46%);
  clip-path: polygon(0 100%, 0 62%, 14% 48%, 28% 60%, 44% 40%, 62% 58%, 78% 44%, 100% 60%, 100% 100%);
}

.d3-13__plane--mid {
  transform: translateZ(calc(var(--d3-13-gap) * -2));
  background: linear-gradient(180deg, #0e2246, #081733);
  clip-path: polygon(0 100%, 0 74%, 18% 62%, 34% 76%, 52% 58%, 70% 74%, 86% 64%, 100% 76%, 100% 100%);
}

.d3-13__plane--near {
  transform: translateZ(0);
  background: linear-gradient(180deg, #04101f, #020a15);
  clip-path: polygon(0 100%, 0 88%, 22% 80%, 46% 92%, 68% 82%, 88% 90%, 100% 84%, 100% 100%);
}

.d3-13__plane--copy {
  transform: translateZ(calc(var(--d3-13-gap) * -1));
  display: grid;
  align-content: center;
  justify-items: start;
  gap: 0.35rem;
  padding: clamp(1rem, 4vw, 2.4rem);
  overflow: visible;
}

.d3-13__kicker {
  font: 700 0.66rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--d3-13-acc);
}

.d3-13__title {
  font: 800 clamp(2rem, 8vw, 4.2rem)/0.92 var(--d3-13-font-display);
  letter-spacing: -0.04em;
  color: #fff;
  text-shadow: 0 18px 40px rgba(0, 0, 0, 0.55);
}

.d3-13__sub {
  font: 500 clamp(0.72rem, 2vw, 0.85rem)/1.3 system-ui, sans-serif;
  color: rgba(238, 243, 255, 0.78);
}

.d3-13__plane--ui {
  transform: translateZ(var(--d3-13-gap));
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 0.75rem;
  padding: clamp(1rem, 4vw, 2.4rem);
  background: none;
  pointer-events: none;
}

.d3-13__price {
  padding: 0.5rem 0.8rem;
  border-radius: 14px;
  background: rgba(8, 14, 28, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.16);
  font: 500 0.72rem/1.2 ui-monospace, Menlo, monospace;
  color: rgba(255, 255, 255, 0.82);
}

.d3-13__price b {
  display: block;
  font: 800 clamp(1rem, 3vw, 1.3rem)/1.1 var(--d3-13-font-display);
  color: #fff;
}

.d3-13__cta {
  padding: 0.75rem 1.1rem;
  border-radius: 999px;
  background: var(--d3-13-acc);
  color: #24140a;
  font: 700 clamp(0.75rem, 2vw, 0.85rem)/1 var(--d3-13-font-display);
  box-shadow: 0 16px 30px -12px color-mix(in oklab, var(--d3-13-acc) 70%, transparent);
}

.d3-13__ruler {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 10rem), 1fr));
  gap: 0.4rem 0.9rem;
}

.d3-13__ruler li {
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
  font: 500 clamp(0.64rem, 1.8vw, 0.72rem)/1.3 ui-monospace, Menlo, monospace;
  color: var(--d3-13-mut);
}

.d3-13__ruler b {
  color: var(--d3-13-acc2);
  font-weight: 700;
}
```
