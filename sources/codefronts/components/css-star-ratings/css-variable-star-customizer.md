---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/css-variable-star-customizer/"
title: "CSS Variable Star Customizer"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A dark control panel with live color-swatch and size-toggle radios that drive the star rating display purely via CSS custom properties — five palettes and…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Variable Star Customizer
Source: https://codefronts.com/components/css-star-ratings/css-variable-star-customizer/

A dark control panel with live color-swatch and size-toggle radios that drive the star rating display purely via CSS custom properties — five palettes and three sizes, zero JavaScript.
## HTML
```html
<div class="sr-09">
  <div class="sr-09__card">
    <div class="sr-09__header">
      <div class="sr-09__badge">CSS Variables</div>
      <div class="sr-09__title">Live Customizer</div>
      <div class="sr-09__sub">Change color &amp; size — pure CSS, zero JS</div>
    </div>

    <!-- Color & size pickers INSIDE the card for :has() scoping -->
    <div class="sr-09__controls">
      <div class="sr-09__control-row">
        <span class="sr-09__ctrl-label">Color Theme</span>
        <div class="sr-09__swatches">
          <input type="radio" id="sr-09-teal" name="sr-09-color" checked>
          <label for="sr-09-teal" class="sr-09__swatch-label" style="background:#0d9488; color:#0d9488" title="Teal"></label>

          <input type="radio" id="sr-09-pink" name="sr-09-color">
          <label for="sr-09-pink" class="sr-09__swatch-label" style="background:#ec4899; color:#ec4899" title="Pink"></label>

          <input type="radio" id="sr-09-orange" name="sr-09-color">
          <label for="sr-09-orange" class="sr-09__swatch-label" style="background:#f97316; color:#f97316" title="Orange"></label>

          <input type="radio" id="sr-09-violet" name="sr-09-color">
          <label for="sr-09-violet" class="sr-09__swatch-label" style="background:#8b5cf6; color:#8b5cf6" title="Violet"></label>

          <input type="radio" id="sr-09-lime" name="sr-09-color">
          <label for="sr-09-lime" class="sr-09__swatch-label" style="background:#84cc16; color:#84cc16" title="Lime"></label>
        </div>
      </div>

      <div class="sr-09__control-row">
        <span class="sr-09__ctrl-label">Star Size</span>
        <div class="sr-09__sizes">
          <input type="radio" id="sr-09-sm" name="sr-09-size">
          <label for="sr-09-sm" class="sr-09__size-btn">Small</label>

          <input type="radio" id="sr-09-md" name="sr-09-size" checked>
          <label for="sr-09-md" class="sr-09__size-btn">Medium</label>

          <input type="radio" id="sr-09-lg" name="sr-09-size">
          <label for="sr-09-lg" class="sr-09__size-btn">Large</label>
        </div>
      </div>
    </div>

    <div class="sr-09__preview">
      <div class="sr-09__stars">
        <input type="radio" id="sr-09-r5" name="sr-09-rate" value="5">
        <label for="sr-09-r5">5</label>
        <input type="radio" id="sr-09-r4" name="sr-09-rate" value="4">
        <label for="sr-09-r4">4</label>
        <input type="radio" id="sr-09-r3" name="sr-09-rate" value="3">
        <label for="sr-09-r3">3</label>
        <input type="radio" id="sr-09-r2" name="sr-09-rate" value="2">
        <label for="sr-09-r2">2</label>
        <input type="radio" id="sr-09-r1" name="sr-09-rate" value="1">
        <label for="sr-09-r1">1</label>
      </div>
      <div class="sr-09__live-val">Driven by <code>--star-color</code> &amp; <code>--star-size</code></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sr-09,
.sr-09 *,
.sr-09 *::before,
.sr-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-09 ::selection {
  background: #0d9488;
  color: #fff;
}

.sr-09 {
  --bg-page: #18181b;
  --bg-card: #27272a;
  --bg-panel: #1f1f22;
  --border: #3f3f46;
  --text: #fafafa;
  --text-muted: #a1a1aa;
  /* User-customizable properties */
  --star-color: #0d9488;
  --star-size: 48px;
  --star-gap: 8px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-page);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-09__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 32px;
  max-width: 480px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}

.sr-09__header {
  margin-bottom: 28px;
}

.sr-09__badge {
  font-size: 0.72rem;
  font-weight: 700;
  background: rgba(13,148,136,0.15);
  color: var(--star-color);
  border: 1px solid rgba(13,148,136,0.3);
  border-radius: 50px;
  padding: 3px 10px;
  letter-spacing: 0.5px;
  display: inline-block;
  margin-bottom: 10px;
  transition: background 0.3s, color 0.3s, border-color 0.3s;
}

.sr-09__title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
}

.sr-09__sub {
  font-size: 0.82rem;
  color: var(--text-muted);
}
/* Star preview */

.sr-09__preview {
  background: var(--bg-panel);
  border-radius: 16px;
  border: 1px solid var(--border);
  padding: 28px 20px;
  margin-bottom: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.sr-09__stars {
  display: flex;
  flex-direction: row-reverse;
  gap: var(--star-gap);
}

.sr-09__stars input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-09__stars label {
  display: block;
  width: var(--star-size);
  height: var(--star-size);
  cursor: pointer;
  position: relative;
  transition: transform 0.2s cubic-bezier(.34,1.56,.64,1);
  /* Hide the digit text content — star shape is drawn via ::before. */
  font-size: 0;
}

.sr-09__stars label::before {
  content: '';
  display: block;
  width: var(--star-size);
  height: var(--star-size);
  background: rgba(255,255,255,0.1);
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  transition: background 0.25s ease, filter 0.25s ease;
}

.sr-09__stars label:hover::before,
.sr-09__stars label:hover ~ label::before {
  background: var(--star-color);
  filter: drop-shadow(0 0 calc(var(--star-size) * 0.2) color-mix(in srgb, var(--star-color), transparent 50%));
}

.sr-09__stars input:checked ~ label::before {
  background: var(--star-color);
  filter: drop-shadow(0 0 calc(var(--star-size) * 0.15) color-mix(in srgb, var(--star-color), transparent 40%));
}

.sr-09__stars label:hover {
  transform: scale(1.15);
}

.sr-09__live-val {
  font-size: 0.78rem;
  color: var(--text-muted);
  text-align: center;
}

.sr-09__live-val code {
  background: rgba(255,255,255,0.08);
  border-radius: 5px;
  padding: 2px 7px;
  font-family: 'SF Mono', 'Fira Code', monospace;
  color: var(--star-color);
  font-size: 0.8rem;
  transition: color 0.3s;
}
/* Control panel */

.sr-09__controls {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.sr-09__control-row {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sr-09__ctrl-label {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.6px;
}
/* Color swatches */

.sr-09__swatches {
  display: flex;
  gap: 10px;
}

.sr-09__swatches input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-09__swatch-label {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.15s, box-shadow 0.15s;
  position: relative;
}

.sr-09__swatch-label:hover {
  transform: scale(1.1);
}

.sr-09__swatches input:checked + .sr-09__swatch-label {
  box-shadow: 0 0 0 2px var(--bg-card), 0 0 0 4px currentColor;
  transform: scale(1.1);
}
/* Apply colors via :has() on the card */

.sr-09__card:has(#sr-09-teal:checked) {
  --star-color: #0d9488;
}

.sr-09__card:has(#sr-09-pink:checked) {
  --star-color: #ec4899;
}

.sr-09__card:has(#sr-09-orange:checked) {
  --star-color: #f97316;
}

.sr-09__card:has(#sr-09-violet:checked) {
  --star-color: #8b5cf6;
}

.sr-09__card:has(#sr-09-lime:checked) {
  --star-color: #84cc16;
}
/* Size options */

.sr-09__sizes {
  display: flex;
  gap: 8px;
}

.sr-09__sizes input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-09__size-btn {
  padding: 6px 16px;
  border-radius: 8px;
  background: rgba(255,255,255,0.06);
  border: 1px solid var(--border);
  color: var(--text-muted);
  font-size: 0.78rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, border-color 0.2s;
}

.sr-09__sizes input:checked + .sr-09__size-btn {
  background: rgba(255,255,255,0.12);
  color: var(--star-color);
  border-color: var(--star-color);
}
/* Apply sizes */

.sr-09__card:has(#sr-09-sm:checked) {
  --star-size: 32px;
  --star-gap: 6px;
}

.sr-09__card:has(#sr-09-md:checked) {
  --star-size: 48px;
  --star-gap: 8px;
}

.sr-09__card:has(#sr-09-lg:checked) {
  --star-size: 64px;
  --star-gap: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .sr-09__stars label,
    .sr-09__stars label::before,
    .sr-09__swatch-label {
    transition: none;
  }
}
```
