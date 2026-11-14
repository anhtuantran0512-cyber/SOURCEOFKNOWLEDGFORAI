---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/neon-lattice/"
title: "Perspective Floor Grid Geometry"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "The geometry of a ground plane: a grid rotated flat with rotateX, spacing chosen so the lines converge legibly, and a horizon placed by the camera rather…"
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Perspective Floor Grid Geometry
Source: https://codefronts.com/design-styles/css-3d/neon-lattice/

The geometry of a ground plane: a grid rotated flat with rotateX, spacing chosen so the lines converge legibly, and a horizon placed by the camera rather than drawn by hand. The vanishing point is marked, the scroll is a single background-position animation, and there is no glow anywhere &mdash; the subject is where the lines go.
## HTML
```html
<section class="d3-18" aria-labelledby="d3-18-title">
  <h2 class="d3-18__sr" id="d3-18-title">Perspective floor grid</h2>

  <div class="d3-18__theme">
    <input class="d3-18__theme-input" type="checkbox" id="d3-18-theme">
    <label class="d3-18__theme-label" for="d3-18-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-18__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-18__stage">
    <div class="d3-18__viewport">
      <div class="d3-18__world">
        <span class="d3-18__sky" aria-hidden="true"></span>
        <span class="d3-18__sun" aria-hidden="true"></span>
        <span class="d3-18__horizon" aria-hidden="true"></span>
        <div class="d3-18__floorbox" aria-hidden="true">
          <div class="d3-18__floor"></div>
        </div>

        <div class="d3-18__hud">
          <div class="d3-18__hud-top">
            <span class="d3-18__tag">Sector 3</span>
            <span class="d3-18__tag d3-18__tag--alt">Dry &middot; 24&deg;C</span>
          </div>
          <div class="d3-18__gauge">
            <b>238</b><em>km/h</em>
          </div>
          <dl class="d3-18__strip">
            <div><dt>Lap</dt><dd>1:24.06</dd></div>
            <div><dt>Delta</dt><dd class="d3-18__good">&minus;0.42</dd></div>
            <div><dt>Gear</dt><dd>6</dd></div>
          </dl>
        </div>
      </div>

      <p class="d3-18__note">The floor is one element: a wide plane rotated <code>90deg</code> on X, pushed back in Z, with a repeating gradient for the grid. The horizon is where the plane meets the vanishing point &mdash; not a drawn line.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-18 {
  --d3-18-bg: #150b22;
  --d3-18-surf: #1e1030;
  --d3-18-line: #3a2154;
  --d3-18-ink: #f3ecff;
  --d3-18-mut: #a795c2;
  --d3-18-acc: #39e8ff;
  --d3-18-acc: oklch(85% 0.14 205);
  --d3-18-acc2: #ff4d9d;
  --d3-18-acc2: oklch(68% 0.22 355);
  --d3-18-speed: 2.6s;
  --d3-18-font-display: "Oswald", "Barlow Condensed", "Arial Narrow", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--d3-18-bg);
  color: var(--d3-18-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-18 *,
.d3-18 *::before,
.d3-18 *::after {
  box-sizing: border-box;
}

.d3-18__sr {
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

.d3-18:has(.d3-18__theme-input:checked) {
  --d3-18-bg: #f4f1f8;
  --d3-18-surf: #ffffff;
  --d3-18-line: #ddd4e8;
  --d3-18-ink: #170d24;
  --d3-18-mut: #61527a;
  --d3-18-acc: #0075a3;
  --d3-18-acc: oklch(52% 0.12 225);
  --d3-18-acc2: #c00b62;
  --d3-18-acc2: oklch(50% 0.21 355);
}

@media (prefers-color-scheme: light) {
  .d3-18:has(.d3-18__theme-input:checked) {
    --d3-18-bg: #f4f1f8;
    --d3-18-surf: #ffffff;
    --d3-18-line: #ddd4e8;
    --d3-18-ink: #170d24;
    --d3-18-mut: #61527a;
    --d3-18-acc: #0075a3;
    --d3-18-acc: oklch(52% 0.12 225);
    --d3-18-acc2: #c00b62;
    --d3-18-acc2: oklch(50% 0.21 355);
  }
}

@media (prefers-color-scheme: dark) {
  .d3-18:has(.d3-18__theme-input:checked) {
    --d3-18-bg: #f4f1f8;
    --d3-18-surf: #ffffff;
    --d3-18-line: #ddd4e8;
    --d3-18-ink: #170d24;
    --d3-18-mut: #61527a;
    --d3-18-acc: #0075a3;
    --d3-18-acc: oklch(52% 0.12 225);
    --d3-18-acc2: #c00b62;
    --d3-18-acc2: oklch(50% 0.21 355);
  }
}

.d3-18__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-18__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-18__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-18-line);
  border-radius: 10px;
  background: color-mix(in oklab, var(--d3-18-surf) 80%, transparent);
  color: var(--d3-18-ink);
  cursor: pointer;
}

.d3-18__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-18__theme-input:focus-visible + .d3-18__theme-label {
  outline: 2px solid var(--d3-18-acc);
  outline-offset: 3px;
}

.d3-18__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-18__viewport {
  inline-size: 100%;
  max-inline-size: 58rem;
  overflow: hidden;
  display: grid;
  gap: clamp(0.8rem, 3vw, 1.3rem);
}

.d3-18__world {
  position: relative;
  block-size: clamp(17rem, 48vw, 24rem);
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid var(--d3-18-line);
  background: linear-gradient(180deg, color-mix(in oklab, var(--d3-18-surf) 90%, transparent) 0 52%, color-mix(in oklab, var(--d3-18-bg) 92%, transparent) 52%);
}

.d3-18__sky {
  position: absolute;
  inset: 0 0 48% 0;
  background: linear-gradient(180deg, color-mix(in oklab, var(--d3-18-acc2) 30%, transparent), transparent 78%);
}

.d3-18__sun {
  position: absolute;
  inset-block-start: 12%;
  inset-inline-start: 50%;
  inline-size: clamp(6rem, 18vw, 9rem);
  aspect-ratio: 1;
  margin-inline-start: calc(clamp(6rem, 18vw, 9rem) / -2);
  border-radius: 999px;
  background: linear-gradient(180deg, var(--d3-18-acc2), color-mix(in oklab, var(--d3-18-acc) 70%, transparent));
  opacity: 0.85;
}

.d3-18__horizon {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 52%;
  block-size: 1px;
  background: linear-gradient(90deg, transparent, var(--d3-18-acc), transparent);
}

.d3-18__floorbox {
  position: absolute;
  inset: 52% 0 0 0;
  perspective: 320px;
  perspective-origin: 50% 0%;
  overflow: hidden;
}

.d3-18__floor {
  position: absolute;
  inset: -60% -30% -40%;
  transform: rotateX(78deg);
  transform-origin: 50% 0%;
  background-image: repeating-linear-gradient(90deg, color-mix(in oklab, var(--d3-18-acc) 55%, transparent) 0 1px, transparent 1px 48px), repeating-linear-gradient(180deg, color-mix(in oklab, var(--d3-18-acc) 45%, transparent) 0 1px, transparent 1px 48px);
  animation: d3-18-run var(--d3-18-speed) linear infinite;
}

@keyframes d3-18-run {
  from {
    background-position: 0 0, 0 0;
  }

  to {
    background-position: 0 0, 0 48px;
  }
}

.d3-18__hud {
  position: absolute;
  inset: 0;
  padding: clamp(0.8rem, 3vw, 1.4rem);
  display: grid;
  align-content: space-between;
}

.d3-18__hud-top {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.d3-18__tag {
  padding: 0.25rem 0.6rem;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, var(--d3-18-acc) 45%, transparent);
  background: color-mix(in oklab, var(--d3-18-bg) 55%, transparent);
  font: 700 0.62rem/1.5 ui-monospace, Menlo, monospace;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--d3-18-acc);
}

.d3-18__tag--alt {
  color: var(--d3-18-acc2);
  border-color: color-mix(in oklab, var(--d3-18-acc2) 45%, transparent);
}

.d3-18__gauge {
  justify-self: center;
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
}

.d3-18__gauge b {
  font: 700 clamp(3rem, 14vw, 6rem)/0.85 var(--d3-18-font-display);
  letter-spacing: -0.02em;
  color: #fff;
  text-shadow: 0 0 26px color-mix(in oklab, var(--d3-18-acc) 70%, transparent);
}

.d3-18__gauge em {
  font: 700 clamp(0.8rem, 2.4vw, 1rem)/1 ui-monospace, Menlo, monospace;
  font-style: normal;
  letter-spacing: 0.2em;
  color: var(--d3-18-acc);
}

.d3-18__strip {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.d3-18__strip div {
  padding: 0.4rem 0.7rem;
  border-radius: 10px;
  background: color-mix(in oklab, var(--d3-18-bg) 62%, transparent);
  border: 1px solid var(--d3-18-line);
}

.d3-18__strip dt {
  font: 700 0.56rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--d3-18-mut);
}

.d3-18__strip dd {
  margin: 0;
  font: 600 clamp(0.8rem, 2.2vw, 0.95rem)/1.1 ui-monospace, Menlo, monospace;
  color: var(--d3-18-ink);
}

.d3-18__good {
  color: var(--d3-18-acc) !important;
}

.d3-18__note {
  margin: 0;
  max-inline-size: 62ch;
  font: 500 clamp(0.72rem, 1.95vw, 0.82rem)/1.5 system-ui, sans-serif;
  color: var(--d3-18-mut);
  text-wrap: pretty;
}

.d3-18__note code {
  font: 600 0.95em/1 ui-monospace, Menlo, monospace;
  color: var(--d3-18-acc);
}

@media (prefers-reduced-motion: reduce) {
  .d3-18__floor {
    animation: none;
  }
}
```
