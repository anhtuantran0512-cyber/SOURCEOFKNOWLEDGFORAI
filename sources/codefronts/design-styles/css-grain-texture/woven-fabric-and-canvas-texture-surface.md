---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/woven-fabric-and-canvas-texture-surface/"
title: "Woven Fabric and Canvas Texture Surface"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Weave is two sets of threads crossing at right angles, and that is exactly what two repeating-linear-gradients are."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Woven Fabric and Canvas Texture Surface
Source: https://codefronts.com/design-styles/css-grain-texture/woven-fabric-and-canvas-texture-surface/

Weave is two sets of threads crossing at right angles, and that is exactly what two repeating-linear-gradients are. Add turbulence for thread irregularity and you get linen, canvas, hessian and denim as pure CSS — no images, resolution-independent, and themeable. Shown as a real fabric swatch catalogue.
## HTML
```html
<section class="grn-18" aria-labelledby="grn-18-title">
  <div class="grn-18__theme">
    <input class="grn-18__theme-input" type="checkbox" id="grn-18-theme">
    <label class="grn-18__theme-label" for="grn-18-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-18__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-18__shell">
    <header class="grn-18__head">
      <p class="grn-18__kicker">Material library · upholstery</p>
      <h1 class="grn-18__h1" id="grn-18-title">Four fabrics, three numbers, no photography</h1>
      <p class="grn-18__lede">Warp and weft as two crossed <code>repeating-linear-gradient</code>s, irregularity from turbulence, and every swatch recolourable because none of it is an image.</p>
    </header>

    <ul class="grn-18__swatches">
      <li class="grn-18__swatch" style="--grn-18-pitch: 3px; --grn-18-thread: 1.2px; --grn-18-depth: 0.1; --grn-18-col: #c9b79a">
        <span class="grn-18__cloth" aria-hidden="true"><span class="grn-18__slub"></span></span>
        <div class="grn-18__meta">
          <div class="grn-18__row"><h2 class="grn-18__name">Belgian linen</h2><span class="grn-18__sku">LN-04</span></div>
          <p class="grn-18__desc">Fine pitch, low contrast. The closest weave to a plain surface — use it where texture should be felt rather than seen.</p>
          <dl class="grn-18__nums"><div><dt>pitch</dt><dd>3px</dd></div><div><dt>thread</dt><dd>1.2px</dd></div><div><dt>depth</dt><dd>0.10</dd></div></dl>
        </div>
      </li>

      <li class="grn-18__swatch" style="--grn-18-pitch: 6px; --grn-18-thread: 2.4px; --grn-18-depth: 0.16; --grn-18-col: #d9cfb8">
        <span class="grn-18__cloth" aria-hidden="true"><span class="grn-18__slub"></span></span>
        <div class="grn-18__meta">
          <div class="grn-18__row"><h2 class="grn-18__name">Cotton canvas</h2><span class="grn-18__sku">CV-12</span></div>
          <p class="grn-18__desc">Medium pitch, heavier thread. The default upholstery weight, and the one that photographs worst — so build it in CSS.</p>
          <dl class="grn-18__nums"><div><dt>pitch</dt><dd>6px</dd></div><div><dt>thread</dt><dd>2.4px</dd></div><div><dt>depth</dt><dd>0.16</dd></div></dl>
        </div>
      </li>

      <li class="grn-18__swatch" style="--grn-18-pitch: 11px; --grn-18-thread: 4.5px; --grn-18-depth: 0.26; --grn-18-col: #b1935f">
        <span class="grn-18__cloth" aria-hidden="true"><span class="grn-18__slub grn-18__slub--heavy"></span></span>
        <div class="grn-18__meta">
          <div class="grn-18__row"><h2 class="grn-18__name">Jute hessian</h2><span class="grn-18__sku">HS-01</span></div>
          <p class="grn-18__desc">Wide pitch, high contrast, heavy slub. Open enough that the backing colour reads through the gaps.</p>
          <dl class="grn-18__nums"><div><dt>pitch</dt><dd>11px</dd></div><div><dt>thread</dt><dd>4.5px</dd></div><div><dt>depth</dt><dd>0.26</dd></div></dl>
        </div>
      </li>

      <li class="grn-18__swatch grn-18__swatch--denim" style="--grn-18-pitch: 4px; --grn-18-thread: 1.8px; --grn-18-depth: 0.2; --grn-18-col: #3f5878">
        <span class="grn-18__cloth" aria-hidden="true"><span class="grn-18__slub grn-18__slub--nap"></span></span>
        <div class="grn-18__meta">
          <div class="grn-18__row"><h2 class="grn-18__name">Indigo denim</h2><span class="grn-18__sku">DN-08</span></div>
          <p class="grn-18__desc">Plain weave plus an anisotropic nap layer, which gives the surface a direction the way real twill does.</p>
          <dl class="grn-18__nums"><div><dt>pitch</dt><dd>4px</dd></div><div><dt>nap</dt><dd>0.02 0.9</dd></div><div><dt>depth</dt><dd>0.20</dd></div></dl>
        </div>
      </li>
    </ul>

    <aside class="grn-18__why">
      <h2 class="grn-18__h2">Why not a photograph</h2>
      <p class="grn-18__why-b">A fabric photo is 80–300KB, tiles visibly, and cannot be recoloured. This is under 500 bytes, tiles perfectly by construction, and takes its colour from your tokens — which is the only version that works in a configurator where the customer picks the colour.</p>
    </aside>
  </main>
</section>
```
## CSS
```css
.grn-18 {
  --grn-18-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='grn18n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23grn18n)'/%3E%3C/svg%3E");
  --grn-18-nap: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='grn18p'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.02 0.9' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23grn18p)'/%3E%3C/svg%3E");
  --grn-18-bg: #f1ebe0;
  --grn-18-surf: #fbf7ef;
  --grn-18-line: #dcd2bf;
  --grn-18-ink: #241f17;
  --grn-18-mut: #6b6252;
  --grn-18-acc: #7a5a2e;
  --grn-18-acc: oklch(48% 0.09 66);
  --grn-18-pitch: 5px;
  --grn-18-thread: 2px;
  --grn-18-depth: 0.16;
  --grn-18-col: #d0c0a4;
  --grn-18-slub: 0.08;
  --grn-18-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-18-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-18-bg);
  color: var(--grn-18-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-18 *,
.grn-18 *::before,
.grn-18 *::after {
  box-sizing: border-box;
}

.grn-18 :focus-visible {
  outline: 2px solid var(--grn-18-acc);
  outline-offset: 3px;
}

.grn-18 code {
  font-family: var(--grn-18-font-mono);
  font-size: 0.9em;
}

.grn-18__sr {
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

.grn-18:has(.grn-18__theme-input:checked) {
  --grn-18-bg: #16130e;
  --grn-18-surf: #1f1b15;
  --grn-18-line: #342d22;
  --grn-18-ink: #f2ece0;
  --grn-18-mut: #a49a86;
  --grn-18-acc: #d7a75d;
  --grn-18-acc: oklch(77% 0.11 72);
  --grn-18-slub: 0.12;
}

@media (prefers-color-scheme: dark) {
  .grn-18 {
    --grn-18-bg: #16130e;
    --grn-18-surf: #1f1b15;
    --grn-18-line: #342d22;
    --grn-18-ink: #f2ece0;
    --grn-18-mut: #a49a86;
    --grn-18-acc: #d7a75d;
    --grn-18-acc: oklch(77% 0.11 72);
    --grn-18-slub: 0.12;
  }

  .grn-18:has(.grn-18__theme-input:checked) {
    --grn-18-bg: #f1ebe0;
    --grn-18-surf: #fbf7ef;
    --grn-18-line: #dcd2bf;
    --grn-18-ink: #241f17;
    --grn-18-mut: #6b6252;
    --grn-18-acc: #7a5a2e;
    --grn-18-acc: oklch(48% 0.09 66);
    --grn-18-slub: 0.08;
  }
}

@media (prefers-color-scheme: light) {
  .grn-18:has(.grn-18__theme-input:checked) {
    --grn-18-bg: #16130e;
    --grn-18-surf: #1f1b15;
    --grn-18-line: #342d22;
    --grn-18-ink: #f2ece0;
    --grn-18-mut: #a49a86;
    --grn-18-acc: #d7a75d;
    --grn-18-acc: oklch(77% 0.11 72);
    --grn-18-slub: 0.12;
  }
}

.grn-18__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-18__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-18__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-18-line);
  border-radius: 999px;
  background: var(--grn-18-surf);
  color: var(--grn-18-ink);
  cursor: pointer;
}

.grn-18__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-18__shell {
  inline-size: min(76rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3rem);
}

.grn-18__head {
  max-inline-size: 46rem;
  display: grid;
  gap: 0.6rem;
}

.grn-18__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-18-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-18-acc);
}

.grn-18__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.2vw, 3.3rem)/1.04 var(--grn-18-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-18__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--grn-18-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.07rem);
  text-wrap: pretty;
}

.grn-18__swatches {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(1rem, 2.4vw, 1.5rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
}

.grn-18__swatch {
  display: grid;
  grid-template-rows: auto 1fr;
  overflow: hidden;
  border: 1px solid var(--grn-18-line);
  border-radius: 14px;
  background: var(--grn-18-surf);
  min-inline-size: 0;
}

.grn-18__cloth {
  position: relative;
  display: block;
  block-size: clamp(9rem, 20vw, 12rem);
  isolation: isolate;
  background-color: var(--grn-18-col);
  background-image: repeating-linear-gradient(90deg, rgba(0, 0, 0, var(--grn-18-depth)) 0 var(--grn-18-thread), transparent var(--grn-18-thread) var(--grn-18-pitch)), repeating-linear-gradient(0deg, rgba(0, 0, 0, var(--grn-18-depth)) 0 var(--grn-18-thread), transparent var(--grn-18-thread) var(--grn-18-pitch)), repeating-linear-gradient(90deg, rgba(255, 255, 255, calc(var(--grn-18-depth) * 0.55)) 0 1px, transparent 1px var(--grn-18-pitch));
  background-blend-mode: multiply, multiply, screen;
}

.grn-18__slub {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: var(--grn-18-noise);
  opacity: var(--grn-18-slub);
  mix-blend-mode: multiply;
}

.grn-18__slub--heavy {
  opacity: calc(var(--grn-18-slub) * 1.8);
}

.grn-18__slub--nap {
  background-image: var(--grn-18-nap);
  opacity: calc(var(--grn-18-slub) * 1.5);
  mix-blend-mode: overlay;
}

.grn-18__meta {
  display: grid;
  align-content: start;
  gap: 0.5rem;
  padding: clamp(1rem, 2.4vw, 1.4rem);
}

.grn-18__row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.6rem;
}

.grn-18__name {
  margin: 0;
  font: 600 1.05rem/1.2 var(--grn-18-font-display);
  letter-spacing: -0.02em;
}

.grn-18__sku {
  font: 400 0.72rem/1 var(--grn-18-font-mono);
  letter-spacing: 0.1em;
  color: var(--grn-18-mut);
}

.grn-18__desc {
  margin: 0;
  color: var(--grn-18-mut);
  font-size: 0.87rem;
  text-wrap: pretty;
}

.grn-18__nums {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem 1.2rem;
  margin: 0.2rem 0 0;
  padding-block-start: 0.7rem;
  border-block-start: 1px solid var(--grn-18-line);
}

.grn-18__nums > div {
  display: grid;
  gap: 0.05rem;
}

.grn-18__nums dt {
  margin: 0;
  font: 400 0.64rem/1 var(--grn-18-font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--grn-18-mut);
}

.grn-18__nums dd {
  margin: 0;
  font: 500 0.85rem/1 var(--grn-18-font-mono);
}

.grn-18__why {
  display: grid;
  gap: 0.5rem;
  padding: clamp(1.2rem, 3vw, 1.8rem);
  border: 1px solid var(--grn-18-line);
  border-radius: 14px;
  background: var(--grn-18-surf);
}

.grn-18__h2 {
  margin: 0;
  font: 600 clamp(1.1rem, 2.6vw, 1.35rem)/1.2 var(--grn-18-font-display);
}

.grn-18__why-b {
  margin: 0;
  max-inline-size: 52rem;
  color: var(--grn-18-mut);
  font-size: 0.92rem;
  text-wrap: pretty;
}

@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 2dppx) {
  .grn-18__cloth {
    background-size: auto;
  }

  .grn-18__slub {
    opacity: calc(var(--grn-18-slub) * 1.15);
  }
}

.grn-18__swatch {
  transition: transform 300ms cubic-bezier(0.22, 1, 0.36, 1), border-color 240ms ease;
}

@media (hover: hover) and (pointer: fine) {
  .grn-18__swatch:hover {
    transform: translateY(-4px);
    border-color: var(--grn-18-acc);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-18__swatch {
    transition-duration: 1ms;
    transform: none;
  }
}
```
