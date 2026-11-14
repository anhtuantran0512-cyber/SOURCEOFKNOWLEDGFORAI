---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/dark-mode-sun-moon-theme-switcher/"
title: "Dark Mode Sun / Moon Theme Switcher"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The classic 'day night switch': the sliding thumb is a glowing sun that morphs into a crescent moon as the track deepens from daylight blue to midnight navy…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Sun / Moon Theme Switcher
Source: https://codefronts.com/components/css-toggles-switches/dark-mode-sun-moon-theme-switcher/

The classic 'day night switch': the sliding thumb is a glowing sun that morphs into a crescent moon as the track deepens from daylight blue to midnight navy — stars fade in, a cloud drifts out, and the entire panel re-themes via :has(). Zero JavaScript.
## HTML
```html
<section class="tgl-02" aria-label="Dark mode sun and moon theme switcher">
  <label class="tgl-02__row" for="tgl-02-sw">
    <span class="tgl-02__lbl">Appearance</span>
    <span class="tgl-02__scene">
      <input type="checkbox" id="tgl-02-sw" class="tgl-02__sw" role="switch">
      <span class="tgl-02__stars" aria-hidden="true"></span>
      <span class="tgl-02__cloud" aria-hidden="true"></span>
    </span>
  </label>
  <p class="tgl-02__cap">Sun ↔ moon · pure CSS morph</p>
</section>
```
## CSS
```css
.tgl-02,
.tgl-02 *,
.tgl-02 *::before,
.tgl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-02 {
  --day: #7ecbf5;
  --night: #1c2a4a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
  padding: 60px 20px;
  background: #eaf4fb;
  color: #27313f;
  transition: background-color .5s,color .5s;
}

.tgl-02:has(.tgl-02__sw:checked) {
  background: #0d1526;
  color: #c7d2e8;
}

.tgl-02__row {
  display: flex;
  align-items: center;
  gap: 26px;
  cursor: pointer;
}

.tgl-02__lbl {
  font-size: 16px;
  font-weight: 600;
}

.tgl-02__scene {
  position: relative;
  display: inline-block;
}

.tgl-02__sw {
  appearance: none;
  -webkit-appearance: none;
  display: block;
  width: 70px;
  height: 36px;
  border-radius: 20px;
  background: linear-gradient(var(--day),#b3e0f9);
  position: relative;
  cursor: pointer;
  transition: background-color .45s;
  box-shadow: inset 0 2px 5px rgba(0,40,80,.25);
}

.tgl-02__sw:checked {
  background: linear-gradient(var(--night),#0f1830);
}

.tgl-02__sw::before {
  content: "";
  position: absolute;
  top: 4px;
  left: 4px;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: transparent;
  box-shadow: inset 0 0 0 14px #ffd54f,0 0 12px rgba(255,200,60,.8);
  transition: transform .45s cubic-bezier(.3,1.2,.4,1),box-shadow .45s;
  z-index: 1;
}

.tgl-02__sw:checked::before {
  transform: translateX(34px);
  box-shadow: inset -8px -4px 0 1px #f4f1de,0 0 10px rgba(220,225,255,.45);
}

.tgl-02__stars {
  position: absolute;
  top: 9px;
  left: 12px;
  width: 2px;
  height: 2px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 10px 4px 0 #fff,4px 14px 0 0 #dfe8ff,16px 16px 0 #fff,24px 7px 0 0 #dfe8ff;
  opacity: 0;
  transition: opacity .45s;
  pointer-events: none;
}

.tgl-02__sw:checked ~ .tgl-02__stars {
  opacity: .95;
}

.tgl-02__cloud {
  position: absolute;
  top: 19px;
  right: 12px;
  width: 18px;
  height: 7px;
  border-radius: 8px;
  background: #fff;
  box-shadow: -7px -4px 0 -1px #fff,6px -3px 0 -2px #fff;
  opacity: .95;
  transition: opacity .45s,transform .45s;
  pointer-events: none;
}

.tgl-02__sw:checked ~ .tgl-02__cloud {
  opacity: 0;
  transform: translateX(8px);
}

.tgl-02__sw:focus-visible {
  outline: 3px solid #4d9fff;
  outline-offset: 3px;
}

.tgl-02__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  opacity: .55;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-02,
    .tgl-02__sw,
    .tgl-02__sw::before,
    .tgl-02__sw::after,
    .tgl-02__stars,
    .tgl-02__cloud {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the thumb slides on transform, an inset box-shadow morphs its fill from solid sun to crescent moon, and the section re-themes itself with :has(:checked). */
```
