---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/minimal-ios-style-toggle-switch/"
title: "Minimal iOS-Style Toggle Switch"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The most searched toggle pattern on earth: a fluid, platform-agnostic iOS-style switch built entirely from a styled checkbox."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal iOS-Style Toggle Switch
Source: https://codefronts.com/components/css-toggles-switches/minimal-ios-style-toggle-switch/

The most searched toggle pattern on earth: a fluid, platform-agnostic iOS-style switch built entirely from a styled checkbox. The track sweeps from neutral gray to Apple green while a crisp white thumb glides across — and pressing it stretches the thumb exactly like the native control.
## HTML
```html
<section class="tgl-01" aria-label="iOS-style toggle switch">
  <label class="tgl-01__row" for="tgl-01-sw">
    <span class="tgl-01__txt"><b>Wi-Fi</b><small>Auto-join known networks</small></span>
    <input type="checkbox" id="tgl-01-sw" class="tgl-01__sw" role="switch" checked>
  </label>
  <p class="tgl-01__cap">Click · or Tab + Space</p>
</section>
```
## CSS
```css
.tgl-01,
.tgl-01 *,
.tgl-01 *::before,
.tgl-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-01 {
  --on: #34c759;
  font-family: -apple-system,'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
  padding: 60px 20px;
  background: #f2f2f7;
}

.tgl-01__row {
  display: flex;
  align-items: center;
  gap: 44px;
  background: #fff;
  padding: 16px 20px;
  border-radius: 14px;
  box-shadow: 0 1px 2px rgba(0,0,0,.06);
  cursor: pointer;
  width: min(340px,100%);
}

.tgl-01__txt {
  display: flex;
  flex-direction: column;
  gap: 2px;
  flex: 1;
}

.tgl-01__txt b {
  font-size: 16px;
  font-weight: 600;
  color: #1c1c1e;
}

.tgl-01__txt small {
  font-size: 12.5px;
  color: #8e8e93;
}

.tgl-01__sw {
  appearance: none;
  -webkit-appearance: none;
  flex: none;
  width: 51px;
  height: 31px;
  border-radius: 16px;
  background: #e9e9eb;
  position: relative;
  cursor: pointer;
  transition: background-color .3s;
}

.tgl-01__sw::before {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  width: 27px;
  height: 27px;
  border-radius: 14px;
  background: #fff;
  box-shadow: 0 3px 8px rgba(0,0,0,.15),0 1px 1px rgba(0,0,0,.16);
  transition: transform .3s cubic-bezier(.2,.9,.25,1.05),width .25s;
}

.tgl-01__sw:checked {
  background: var(--on);
}

.tgl-01__sw:checked::before {
  transform: translateX(20px);
}

.tgl-01__sw:active::before {
  width: 32px;
}

.tgl-01__sw:checked:active::before {
  transform: translateX(15px);
}

.tgl-01__sw:focus-visible {
  outline: 3px solid #0a84ff;
  outline-offset: 3px;
}

.tgl-01__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #a5a5ad;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-01__sw,
    .tgl-01__sw::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — appearance:none turns the checkbox itself into the track; a ::before thumb slides on transform:translateX() and :active reproduces the native iOS thumb stretch. */
```
