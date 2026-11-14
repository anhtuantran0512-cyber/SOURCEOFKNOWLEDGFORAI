---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/css-segmented-control-with-motion-path-comet-thumb-offset-path-arc-travel/"
title: "CSS Segmented Control with Motion-Path Comet Thumb (offset-path Arc Travel)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A segmented control whose selection thumb doesn't slide in a straight line — it arcs along a curved CSS motion path like a comet, trailing an aurora glow…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Segmented Control with Motion-Path Comet Thumb (offset-path Arc Travel)
Source: https://codefronts.com/components/css-button-groups/css-segmented-control-with-motion-path-comet-thumb-offset-path-arc-travel/

A segmented control whose selection thumb doesn't slide in a straight line — it arcs along a curved CSS motion path like a comet, trailing an aurora glow that lags behind and catches up. A never-seen 'CSS offset-path segmented control' that swaps the tired linear thumb for real motion-path travel, on accessible radio inputs.
## HTML
```html
<section class="btn-02" aria-label="Motion-path comet segmented control demo">
  <div class="btn-02__wrap">
    <p class="btn-02__label">Signal mode</p>
    <div class="btn-02__seg" role="radiogroup" aria-label="Signal mode">
      <input type="radio" name="btn-02" id="btn-02-1" class="btn-02__in" checked>
      <label for="btn-02-1" class="btn-02__opt">Live</label>
      <input type="radio" name="btn-02" id="btn-02-2" class="btn-02__in">
      <label for="btn-02-2" class="btn-02__opt">Pulse</label>
      <input type="radio" name="btn-02" id="btn-02-3" class="btn-02__in">
      <label for="btn-02-3" class="btn-02__opt">Wave</label>
      <input type="radio" name="btn-02" id="btn-02-4" class="btn-02__in">
      <label for="btn-02-4" class="btn-02__opt">Idle</label>
      <span class="btn-02__tail" aria-hidden="true"></span>
      <span class="btn-02__thumb" aria-hidden="true"></span>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-02,
.btn-02 *,
.btn-02 *::before,
.btn-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-02 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 50% 0%,#0d1024,#06070f);
  padding: 44px 20px;
}

.btn-02__wrap {
  width: min(420px,100%);
}

.btn-02__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #7fe3c4;
  margin: 0 0 14px 4px;
}

.btn-02__seg {
  --d: 0%;
  position: relative;
  display: grid;
  grid-template-columns: repeat(4,80px);
  width: calc(80px*4 + 12px);
  padding: 6px;
  background: #12142a;
  border: 1px solid #222647;
  border-radius: 16px;
  box-shadow: inset 0 2px 8px rgba(0,0,0,.5);
}

.btn-02__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-02__opt {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  font-size: 14.5px;
  font-weight: 700;
  color: #8891bd;
  cursor: pointer;
  transition: color .3s;
}

.btn-02__thumb,
.btn-02__tail {
  position: absolute;
  left: 0;
  top: 0;
  width: 74px;
  height: 44px;
  border-radius: 11px;
  offset-path: path("M43 28 C 123 6, 203 6, 283 28");
  offset-rotate: 0deg;
  offset-distance: var(--d);
}

.btn-02__thumb {
  z-index: 1;
  background: linear-gradient(120deg,#38f2c0,#3aa0ff);
  box-shadow: 0 4px 18px -4px #38f2c0;
  transition: offset-distance .5s cubic-bezier(.5,0,.2,1);
}

.btn-02__tail {
  z-index: 0;
  background: linear-gradient(120deg,#38f2c0,#8a5bff);
  filter: blur(9px);
  opacity: .6;
  transition: offset-distance .8s cubic-bezier(.5,0,.2,1);
}

.btn-02__seg:has(#btn-02-2:checked) {
  --d: 33.3%;
}

.btn-02__seg:has(#btn-02-3:checked) {
  --d: 66.6%;
}

.btn-02__seg:has(#btn-02-4:checked) {
  --d: 100%;
}

.btn-02__in:checked + .btn-02__opt {
  color: #04121c;
}

.btn-02__in:focus-visible + .btn-02__opt {
  outline: 3px solid #7fe3c4;
  outline-offset: 3px;
  border-radius: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-02__thumb,
    .btn-02__tail {
    offset-path: path("M43 28 L 283 28");
    transition: offset-distance .2s;
  }
}
```
