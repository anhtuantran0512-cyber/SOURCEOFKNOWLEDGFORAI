---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/plasma-pill/"
title: "CSS Pill Button Group with Rotating Conic Plasma Border (Animated Gradient Ring)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "Pill buttons wrapped in a living plasma ring — a conic-gradient border that rotates continuously around each pill, glowing hotter on the active one."
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pill Button Group with Rotating Conic Plasma Border (Animated Gradient Ring)
Source: https://codefronts.com/components/css-button-groups/plasma-pill/

Pill buttons wrapped in a living plasma ring — a conic-gradient border that rotates continuously around each pill, glowing hotter on the active one. The mesmerizing 'CSS rotating conic plasma border button group' powered by an @property angle, using the border-box gradient trick so the animated ring never bleeds into the label.
## HTML
```html
<section class="btn-23" aria-label="Rotating conic plasma pill group demo">
  <div class="btn-23__wrap">
    <p class="btn-23__label">Energy plan</p>
    <div class="btn-23__pills" role="radiogroup" aria-label="Energy plan">
      <input type="radio" name="btn-23" id="btn-23-1" class="btn-23__in" checked>
      <label for="btn-23-1" class="btn-23__pill">Solar</label>
      <input type="radio" name="btn-23" id="btn-23-2" class="btn-23__in">
      <label for="btn-23-2" class="btn-23__pill">Fusion</label>
      <input type="radio" name="btn-23" id="btn-23-3" class="btn-23__in">
      <label for="btn-23-3" class="btn-23__pill">Hybrid</label>
    </div>
  </div>
</section>
```
## CSS
```css
@property --btn-23-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.btn-23,
.btn-23 *,
.btn-23 *::before,
.btn-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-23 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(120% 120% at 50% 0%,#160b1e,#08040c);
  padding: 44px 20px;
}

.btn-23__wrap {
  width: min(520px,100%);
}

.btn-23__label {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #d59bff;
  margin: 0 0 16px 2px;
}

.btn-23__pills {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.btn-23__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-23__pill {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 50px;
  padding: 0 30px;
  font-size: 15px;
  font-weight: 750;
  color: #b9a8cf;
  cursor: pointer;
  border-radius: 999px;
  border: 2px solid transparent;
  background: linear-gradient(#160c1f,#160c1f) padding-box,conic-gradient(from var(--btn-23-a),#5b3a8a,#8a5bd6,#3a5b8a,#5b3a8a) border-box;
  animation: btn-23-spin 7s linear infinite;
  transition: color .25s;
}

@keyframes btn-23-spin {
  to {
    --btn-23-a: 360deg;
  }
}

.btn-23__pill:hover {
  color: #e6d6ff;
}

.btn-23__in:checked + .btn-23__pill {
  color: #fff;
  background: linear-gradient(#1a0e12,#1a0e12) padding-box,conic-gradient(from var(--btn-23-a),#ff7a18,#ff2bd0,#ffd24c,#ff7a18) border-box;
  animation: btn-23-spin 3s linear infinite;
  text-shadow: 0 0 10px rgba(255,120,60,.6);
}

.btn-23__in:checked + .btn-23__pill::before {
  content: "";
  position: absolute;
  inset: -4px;
  border-radius: 999px;
  background: conic-gradient(from var(--btn-23-a),#ff7a18,#ff2bd0,#ffd24c,#ff7a18);
  filter: blur(11px);
  opacity: .55;
  z-index: -1;
  animation: btn-23-spin 3s linear infinite;
}

.btn-23__in:focus-visible + .btn-23__pill {
  outline: 3px solid #ffd24c;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .btn-23__pill,
    .btn-23__in:checked + .btn-23__pill,
    .btn-23__in:checked + .btn-23__pill::before {
    animation: none;
  }
}
```
