---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/skeuomorphic-light-switch/"
title: "Skeuomorphic Light Switch"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A physical rocker light switch — brushed metal bezel, plastic rocker that tilts on toggle, subtle shadow that deepens when pressed."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeuomorphic Light Switch
Source: https://codefronts.com/components/css-toggles-switches/skeuomorphic-light-switch/

A physical rocker light switch — brushed metal bezel, plastic rocker that tilts on toggle, subtle shadow that deepens when pressed. Heavy realism, satisfying click.
## HTML
```html
<label class="tgl-36">
  <input class="tgl-36__input" type="checkbox" checked>
  <span class="tgl-36__bezel" aria-hidden="true">
    <span class="tgl-36__rocker">
      <span class="tgl-36__mark"></span>
    </span>
  </span>
  <span class="tgl-36__label">Power</span>
</label>
```
## CSS
```css
.tgl-36 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  color: #d8d4dc;
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 48px 20px;
  background: #14141e;
  box-sizing: border-box;
}

.tgl-36__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.tgl-36__bezel {
  position: relative;
  width: 56px;
  height: 44px;
  background: linear-gradient(180deg, #4a4a52 0%, #2a2a30 100%);
  border-radius: 6px;
  padding: 4px;
  box-shadow: inset 0 1px 1px rgba(255,255,255,0.18), inset 0 -1px 1px rgba(0,0,0,0.5), 0 2px 4px rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
}

.tgl-36__rocker {
  position: relative;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, #f4f1ec 0%, #d8d2c6 100%);
  border-radius: 3px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.8), inset 0 -1px 0 rgba(0,0,0,0.15);
  transition: transform 0.18s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.18s ease;
  transform-origin: center;
}

.tgl-36__mark {
  position: absolute;
  top: 6px;
  left: 50%;
  width: 14px;
  height: 3px;
  background: #2a2a30;
  border-radius: 2px;
  transform: translateX(-50%);
  transition: top 0.18s ease, bottom 0.18s ease;
}

.tgl-36__input:checked ~ .tgl-36__bezel .tgl-36__rocker {
  transform: rotateX(0deg);
  box-shadow: inset 0 -1px 0 rgba(255,255,255,0.8), inset 0 1px 0 rgba(0,0,0,0.15);
}

.tgl-36__input:checked ~ .tgl-36__bezel .tgl-36__mark {
  top: auto;
  bottom: 6px;
  background: #d04f4f;
}

.tgl-36__input:not(:checked) ~ .tgl-36__bezel .tgl-36__rocker {
  transform: rotateX(180deg);
}

.tgl-36__input:focus-visible ~ .tgl-36__bezel {
  outline: 2px solid #6b9eff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-36__rocker,
    .tgl-36__mark {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the rocker plate flips rotateX(180°→0°) inside a beveled bezel while the position mark swaps ends and turns red. */
```
