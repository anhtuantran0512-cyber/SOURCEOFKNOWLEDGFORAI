---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-toggle-switch-gradient-text-colour-picker/"
title: "CSS Toggle Switch Gradient Text Colour Picker"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Three checkbox-driven toggle switches independently enable gradient fills on individual words, demonstrating CSS state-driven gradient text with zero…"
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Toggle Switch Gradient Text Colour Picker
Source: https://codefronts.com/design-styles/css-gradient-text/css-toggle-switch-gradient-text-colour-picker/

Three checkbox-driven toggle switches independently enable gradient fills on individual words, demonstrating CSS state-driven gradient text with zero JavaScript.
## HTML
```html
<div class="gt-14">
  <input type="checkbox" id="gt-14-chk-a" class="gt-14__chk-a">
  <input type="checkbox" id="gt-14-chk-b" class="gt-14__chk-b">
  <input type="checkbox" id="gt-14-chk-c" class="gt-14__chk-c">
  <span class="gt-14__label">Toggle gradient fills</span>
  <div class="gt-14__controls">
    <div class="gt-14__toggle-row">
      <label class="gt-14__toggle-label" for="gt-14-chk-a">
        <div class="gt-14__track gt-14__track-a"></div>
        <span class="gt-14__name">Pink gradient</span>
      </label>
    </div>
    <div class="gt-14__toggle-row">
      <label class="gt-14__toggle-label" for="gt-14-chk-b">
        <div class="gt-14__track gt-14__track-b"></div>
        <span class="gt-14__name">Green gradient</span>
      </label>
    </div>
    <div class="gt-14__toggle-row">
      <label class="gt-14__toggle-label" for="gt-14-chk-c">
        <div class="gt-14__track gt-14__track-c"></div>
        <span class="gt-14__name">Blue gradient</span>
      </label>
    </div>
  </div>
  <div class="gt-14__stage">
    <div class="gt-14__word gt-14__word-a">VIVID</div>
    <div class="gt-14__word gt-14__word-b">COLOUR</div>
    <div class="gt-14__word gt-14__word-c">CONTROL</div>
  </div>
</div>
```
## CSS
```css
.gt-14,
.gt-14 *,
.gt-14 *::before,
.gt-14 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-14 {
  --bg: #f0ede8;
  font-family: 'Manrope', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 3rem 2rem;
}

.gt-14__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #bbb;
}
/* Hidden checkboxes drive the toggling */

.gt-14__chk-a {
  display: none;
}

.gt-14__chk-b {
  display: none;
}

.gt-14__chk-c {
  display: none;
}
/* Toggle switch UI */

.gt-14__controls {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  align-items: flex-start;
}

.gt-14__toggle-row {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.gt-14__toggle-label {
  display: flex;
  align-items: center;
  gap: .6rem;
  cursor: pointer;
  user-select: none;
}

.gt-14__track {
  width: 44px;
  height: 24px;
  border-radius: 12px;
  background: #ddd;
  position: relative;
  transition: background .3s;
}

.gt-14__track::after {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: white;
  transition: transform .3s;
  box-shadow: 0 1px 4px rgba(0,0,0,.2);
}
/* Checked states */

#gt-14-chk-a:checked ~ .gt-14__stage .gt-14__track-a {
  background: #f093fb;
}

#gt-14-chk-a:checked ~ .gt-14__stage .gt-14__track-a::after {
  transform: translateX(20px);
}

#gt-14-chk-b:checked ~ .gt-14__stage .gt-14__track-b {
  background: #43e97b;
}

#gt-14-chk-b:checked ~ .gt-14__stage .gt-14__track-b::after {
  transform: translateX(20px);
}

#gt-14-chk-c:checked ~ .gt-14__stage .gt-14__track-c {
  background: #4facfe;
}

#gt-14-chk-c:checked ~ .gt-14__stage .gt-14__track-c::after {
  transform: translateX(20px);
}

.gt-14__name {
  font-size: .75rem;
  font-weight: 700;
  color: #888;
}
/* Main text — default plain */

.gt-14__stage {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .5rem;
}

.gt-14__word {
  font-size: clamp(3rem, 10vw, 6rem);
  font-weight: 800;
  line-height: 1;
  color: #ccc;
  transition: color .4s;
  -webkit-text-fill-color: currentColor;
}

.gt-14__word-a {
  -webkit-text-fill-color: #ccc;
  background: linear-gradient(90deg, #f093fb, #f5576c);
  -webkit-background-clip: text;
  background-clip: text;
  transition: -webkit-text-fill-color .4s;
}

.gt-14__word-b {
  -webkit-text-fill-color: #ccc;
  background: linear-gradient(90deg, #43e97b, #38f9d7);
  -webkit-background-clip: text;
  background-clip: text;
}

.gt-14__word-c {
  -webkit-text-fill-color: #ccc;
  background: linear-gradient(90deg, #4facfe, #00f2fe);
  -webkit-background-clip: text;
  background-clip: text;
}

#gt-14-chk-a:checked ~ .gt-14__stage .gt-14__word-a {
  -webkit-text-fill-color: transparent;
}

#gt-14-chk-b:checked ~ .gt-14__stage .gt-14__word-b {
  -webkit-text-fill-color: transparent;
}

#gt-14-chk-c:checked ~ .gt-14__stage .gt-14__word-c {
  -webkit-text-fill-color: transparent;
}

@media (prefers-reduced-motion: reduce) {
  .gt-14__track,
    .gt-14__track::after {
    transition: none;
  }
}
```
