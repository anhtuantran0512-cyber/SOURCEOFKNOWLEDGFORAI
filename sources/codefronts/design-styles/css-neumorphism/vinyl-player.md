---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/vinyl-player/"
title: "Neumorphic Range Slider with Inset Track"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Range inputs styled as carved tracks with raised pucks — soft UI's most convincing component, because a groove with a knob in it is a real object people…"
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Range Slider with Inset Track
Source: https://codefronts.com/design-styles/css-neumorphism/vinyl-player/

Range inputs styled as carved tracks with raised pucks — soft UI's most convincing component, because a groove with a knob in it is a real object people already know how to use. Horizontal and vertical sliders plus a stepped one, all on native input[type=range], with the WebKit and Firefox pseudo-element pairs written out and the fill-before-thumb technique that neither engine supports natively.
## HTML
```html
<section class="nm-13" aria-labelledby="nm-13-heading">
      <input type="checkbox" id="nm-13-theme" class="nm-13__themeinput">
      <label for="nm-13-theme" class="nm-13__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-13__stage">
    <header class="nm-13__head">
      <p class="nm-13__kicker">Component · range</p>
      <h2 class="nm-13__heading" id="nm-13-heading">A groove with a knob in it</h2>
      <p class="nm-13__sub">The component soft UI was made for — and two engines that need two rule sets to build it.</p>
    </header>

    <div class="nm-13__panel">
      <div class="nm-13__slider">
        <div class="nm-13__labelrow">
          <label class="nm-13__label" for="nm-13-vol">Output level</label>
          <span class="nm-13__value">72%</span>
        </div>
        <input class="nm-13__range" type="range" id="nm-13-vol" min="0" max="100" value="72" style="--nm-13-value:72%">
      </div>

      <div class="nm-13__slider">
        <div class="nm-13__labelrow">
          <label class="nm-13__label" for="nm-13-warm">Warmth</label>
          <span class="nm-13__value">−3 dB</span>
        </div>
        <input class="nm-13__range" type="range" id="nm-13-warm" min="-12" max="12" value="-3" style="--nm-13-value:37.5%">
      </div>

      <div class="nm-13__slider">
        <div class="nm-13__labelrow">
          <label class="nm-13__label" for="nm-13-step">Quality preset</label>
          <span class="nm-13__value">Step 3 of 5</span>
        </div>
        <input class="nm-13__range nm-13__range--nm-13-stepped" type="range" id="nm-13-step" min="1" max="5" step="1" value="3" style="--nm-13-value:50%">
      </div>
    </div>

    <div class="nm-13__mixer">
      <div class="nm-13__fader">
        <input class="nm-13__vrange" type="range" id="nm-13-lo" min="0" max="100" value="64" aria-label="Low band" style="--nm-13-value:64%">
        <span class="nm-13__faderlabel">Low<em>+4</em></span>
      </div>
      <div class="nm-13__fader">
        <input class="nm-13__vrange" type="range" id="nm-13-mid" min="0" max="100" value="48" aria-label="Mid band" style="--nm-13-value:48%">
        <span class="nm-13__faderlabel">Mid<em>−1</em></span>
      </div>
      <div class="nm-13__fader">
        <input class="nm-13__vrange" type="range" id="nm-13-hi" min="0" max="100" value="80" aria-label="High band" style="--nm-13-value:80%">
        <span class="nm-13__faderlabel">High<em>+7</em></span>
      </div>
      <p class="nm-13__mixernote">Vertical faders use <code>writing-mode: vertical-lr</code> with the older <code>-webkit-appearance: slider-vertical</code> declared before it.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-13 {
  position: relative;
  --nm-13-surface: #e4e5e8;
  --nm-13-dark: rgba(167,170,178,0.64);
  --nm-13-light: rgba(255,255,255,0.94);
  --nm-13-ink: #24262b;
  --nm-13-muted: #575b64;
  --nm-13-border: #969aa4;
  --nm-13-fill: #5b52a8;
  --nm-13-track: 14px;
  --nm-13-thumb: 28px;
  --nm-13-font-display: "IBM Plex Sans", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-13-surface);
  color: var(--nm-13-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 280)) {
  .nm-13 {
    --nm-13-surface: oklch(0.918 0.005 280);
    --nm-13-ink: oklch(0.26 0.013 285);
    --nm-13-muted: oklch(0.45 0.016 285);
    --nm-13-fill: oklch(0.48 0.13 292);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-13 {
    --nm-13-dark: color-mix(in oklab, var(--nm-13-surface), #000 20%);
    --nm-13-light: color-mix(in oklab, var(--nm-13-surface), #fff 92%);
    --nm-13-border: color-mix(in oklab, var(--nm-13-surface), var(--nm-13-ink) 33%);
  }
}

.nm-13 *,
.nm-13 *::before,
.nm-13 *::after {
  box-sizing: border-box;
}

.nm-13__stage {
  max-width: 900px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(20px, 3.2vw, 32px);
}

.nm-13__head {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-13__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-13-muted);
}

.nm-13__heading {
  margin: 0;
  font-family: var(--nm-13-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-13__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-13-muted);
  text-wrap: pretty;
}

.nm-13__panel {
  border-radius: 24px;
  padding: clamp(20px, 3.4vw, 30px);
  display: flex;
  flex-direction: column;
  gap: clamp(20px, 3vw, 28px);
  background: var(--nm-13-surface);
  border: 1px solid var(--nm-13-border);
  box-shadow: 10px 10px 22px var(--nm-13-dark), -10px -10px 22px var(--nm-13-light);
}

.nm-13__slider {
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-inline-size: 0;
}

.nm-13__labelrow {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  align-items: baseline;
  min-inline-size: 0;
}

.nm-13__label {
  font-family: var(--nm-13-font-display);
  font-size: 0.86rem;
  font-weight: 600;
}

.nm-13__value {
  font-size: 0.8rem;
  color: var(--nm-13-muted);
  font-variant-numeric: tabular-nums;
}

.nm-13__range {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: var(--nm-13-thumb);
  margin: 0;
  background: transparent;
  cursor: pointer;
}

.nm-13__range:focus {
  outline: none;
}

.nm-13__range:focus-visible {
  outline: 2px solid var(--nm-13-fill);
  outline-offset: 4px;
  border-radius: 999px;
}

.nm-13__range::-webkit-slider-runnable-track {
  height: var(--nm-13-track);
  border-radius: 999px;
  background: linear-gradient(90deg, var(--nm-13-fill) 0 var(--nm-13-value), transparent var(--nm-13-value));
  background-color: var(--nm-13-surface);
  box-shadow: inset 4px 4px 8px var(--nm-13-dark), inset -4px -4px 8px var(--nm-13-light);
}

.nm-13__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: var(--nm-13-thumb);
  height: var(--nm-13-thumb);
  margin-top: calc((var(--nm-13-track) - var(--nm-13-thumb)) / 2);
  border-radius: 50%;
  background: var(--nm-13-surface);
  border: 1px solid var(--nm-13-border);
  box-shadow: 4px 4px 9px var(--nm-13-dark), -4px -4px 9px var(--nm-13-light);
}

.nm-13__range::-moz-range-track {
  height: var(--nm-13-track);
  border-radius: 999px;
  background: var(--nm-13-surface);
  box-shadow: inset 4px 4px 8px var(--nm-13-dark), inset -4px -4px 8px var(--nm-13-light);
}

.nm-13__range::-moz-range-progress {
  height: var(--nm-13-track);
  border-radius: 999px;
  background: var(--nm-13-fill);
}

.nm-13__range::-moz-range-thumb {
  width: var(--nm-13-thumb);
  height: var(--nm-13-thumb);
  border-radius: 50%;
  background: var(--nm-13-surface);
  border: 1px solid var(--nm-13-border);
  box-shadow: 4px 4px 9px var(--nm-13-dark), -4px -4px 9px var(--nm-13-light);
}

.nm-13__range--nm-13-stepped::-webkit-slider-runnable-track {
  background-image: linear-gradient(90deg, var(--nm-13-fill) 0 var(--nm-13-value), transparent var(--nm-13-value)), repeating-linear-gradient(90deg, transparent 0 calc(25% - 1px), var(--nm-13-border) calc(25% - 1px), var(--nm-13-border) 25%);
}

.nm-13__mixer {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(18px, 3.4vw, 30px);
  align-items: flex-end;
  justify-content: center;
  border-radius: 24px;
  padding: clamp(20px, 3.4vw, 28px);
  background: var(--nm-13-surface);
  border: 1px solid var(--nm-13-border);
  box-shadow: inset 6px 6px 13px var(--nm-13-dark), inset -6px -6px 13px var(--nm-13-light);
}

.nm-13__fader {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.nm-13__vrange {
  -webkit-appearance: slider-vertical;
  appearance: none;
  writing-mode: vertical-lr;
  direction: rtl;
  width: var(--nm-13-thumb);
  height: 140px;
  margin: 0;
  background: transparent;
  cursor: pointer;
}

.nm-13__vrange:focus-visible {
  outline: 2px solid var(--nm-13-fill);
  outline-offset: 4px;
  border-radius: 999px;
}

.nm-13__vrange::-webkit-slider-runnable-track {
  width: var(--nm-13-track);
  border-radius: 999px;
  background: var(--nm-13-surface);
  box-shadow: inset 4px 4px 8px var(--nm-13-dark), inset -4px -4px 8px var(--nm-13-light);
}

.nm-13__vrange::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: var(--nm-13-thumb);
  height: var(--nm-13-thumb);
  margin-left: calc((var(--nm-13-track) - var(--nm-13-thumb)) / 2);
  border-radius: 50%;
  background: var(--nm-13-surface);
  border: 1px solid var(--nm-13-border);
  box-shadow: 4px 4px 9px var(--nm-13-dark), -4px -4px 9px var(--nm-13-light);
}

.nm-13__vrange::-moz-range-track {
  width: var(--nm-13-track);
  border-radius: 999px;
  background: var(--nm-13-surface);
  box-shadow: inset 4px 4px 8px var(--nm-13-dark), inset -4px -4px 8px var(--nm-13-light);
}

.nm-13__vrange::-moz-range-thumb {
  width: var(--nm-13-thumb);
  height: var(--nm-13-thumb);
  border-radius: 50%;
  background: var(--nm-13-surface);
  border: 1px solid var(--nm-13-border);
  box-shadow: 4px 4px 9px var(--nm-13-dark), -4px -4px 9px var(--nm-13-light);
}

.nm-13__faderlabel {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  font-family: var(--nm-13-font-display);
  font-size: 0.8rem;
  font-weight: 600;
}

.nm-13__faderlabel em {
  font-style: normal;
  font-size: 0.72rem;
  font-weight: 400;
  color: var(--nm-13-muted);
  font-variant-numeric: tabular-nums;
}

.nm-13__mixernote {
  flex: 1 0 100%;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.78rem;
  line-height: 1.6;
  color: var(--nm-13-muted);
  text-wrap: pretty;
}

.nm-13__mixernote code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.9em;
  color: var(--nm-13-ink);
  overflow-wrap: anywhere;
}

@media (prefers-color-scheme: dark) {
  .nm-13 {
    --nm-13-surface: #26282d;
    --nm-13-dark: rgba(11,12,14,0.72);
    --nm-13-light: rgba(88,91,99,0.44);
    --nm-13-ink: #e8e9ee;
    --nm-13-muted: #9b9ea8;
    --nm-13-border: #858893;
    --nm-13-fill: #9b8ef0;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-13 {
      --nm-13-dark: color-mix(in oklab, var(--nm-13-surface), #000 55%);
      --nm-13-light: color-mix(in oklab, var(--nm-13-surface), #fff 14%);
    }
  }
}

.nm-13[data-theme="dark"] {
  --nm-13-surface: #26282d;
  --nm-13-dark: rgba(11,12,14,0.72);
  --nm-13-light: rgba(88,91,99,0.44);
  --nm-13-ink: #e8e9ee;
  --nm-13-muted: #9b9ea8;
  --nm-13-border: #858893;
  --nm-13-fill: #9b8ef0;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-13[data-theme="dark"] {
    --nm-13-dark: color-mix(in oklab, var(--nm-13-surface), #000 55%);
    --nm-13-light: color-mix(in oklab, var(--nm-13-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-13__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-13__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-13-surface);
  color: var(--nm-13-ink);
  border: 1px solid var(--nm-13-line);
  font: 600 11px/1 var(--nm-13-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-13-distance, 6px) var(--nm-13-distance, 6px) var(--nm-13-blur, 14px) var(--nm-13-dark), calc(-1 * var(--nm-13-distance, 6px)) calc(-1 * var(--nm-13-distance, 6px)) var(--nm-13-blur, 14px) var(--nm-13-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-13__themebtn:hover {
  color: var(--nm-13-ink);
}

.nm-13__themeinput:focus-visible + .nm-13__themebtn {
  outline: 2px solid var(--nm-13-ink);
  outline-offset: 3px;
}

.nm-13:has(#nm-13-theme:checked) .nm-13__themebtn {
  box-shadow: inset var(--nm-13-distance, 6px) var(--nm-13-distance, 6px) var(--nm-13-blur, 14px) var(--nm-13-dark), inset calc(-1 * var(--nm-13-distance, 6px)) calc(-1 * var(--nm-13-distance, 6px)) var(--nm-13-blur, 14px) var(--nm-13-light);
}

.nm-13__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-13:has(#nm-13-theme:checked) {
  --nm-13-surface: #26282d;
  --nm-13-dark: rgba(11,12,14,0.72);
  --nm-13-light: rgba(88,91,99,0.44);
  --nm-13-ink: #e8e9ee;
  --nm-13-muted: #9b9ea8;
  --nm-13-border: #858893;
  --nm-13-fill: #9b8ef0;
}

@media (prefers-color-scheme: light) {
  .nm-13:has(#nm-13-theme:checked) {
    --nm-13-surface: #26282d;
    --nm-13-dark: rgba(11,12,14,0.72);
    --nm-13-light: rgba(88,91,99,0.44);
    --nm-13-ink: #e8e9ee;
    --nm-13-muted: #9b9ea8;
    --nm-13-border: #858893;
    --nm-13-fill: #9b8ef0;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-13:has(#nm-13-theme:checked) {
    --nm-13-surface: #e4e5e8;
    --nm-13-dark: rgba(167,170,178,0.64);
    --nm-13-light: rgba(255,255,255,0.94);
    --nm-13-ink: #24262b;
    --nm-13-muted: #575b64;
    --nm-13-border: #969aa4;
    --nm-13-fill: #5b52a8;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-13__themebtn {
    transition: none;
  }
}
```
