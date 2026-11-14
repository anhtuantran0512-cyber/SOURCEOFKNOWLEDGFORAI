---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/ios-light-mode-settings-list/"
title: "iOS Light Mode Settings List"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The full iOS Settings context, not just the switch: a light grouped list with hairline separators, colored glyph tiles, and three native-feel toggles — the…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS Light Mode Settings List
Source: https://codefronts.com/components/css-toggles-switches/ios-light-mode-settings-list/

The full iOS Settings context, not just the switch: a light grouped list with hairline separators, colored glyph tiles, and three native-feel toggles — the pattern to copy when you need a whole preferences screen, complete with section header and footnote.
## HTML
```html
<section class="tgl-23" aria-label="iOS settings list with toggles">
  <div class="tgl-23__screen">
    <p class="tgl-23__sect">Notifications</p>
    <div class="tgl-23__group">
      <label class="tgl-23__row"><span class="tgl-23__glyph" style="--g:#ff3b30">◗</span><span class="tgl-23__name">Allow Notifications</span><input type="checkbox" class="tgl-23__sw" role="switch" checked></label>
      <label class="tgl-23__row"><span class="tgl-23__glyph" style="--g:#007aff">◍</span><span class="tgl-23__name">Time Sensitive</span><input type="checkbox" class="tgl-23__sw" role="switch" checked></label>
      <label class="tgl-23__row"><span class="tgl-23__glyph" style="--g:#af52de">◔</span><span class="tgl-23__name">Scheduled Summary</span><input type="checkbox" class="tgl-23__sw" role="switch"></label>
    </div>
    <p class="tgl-23__foot">Time Sensitive notifications are delivered immediately and stay on the Lock Screen for an hour.</p>
  </div>
</section>
```
## CSS
```css
.tgl-23,
.tgl-23 *,
.tgl-23 *::before,
.tgl-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-23 {
  --row-h: 52px;
  font-family: -apple-system,'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #f2f2f7;
}

.tgl-23__screen {
  width: min(360px,100%);
}

.tgl-23__sect {
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: .05em;
  color: #6d6d72;
  margin: 0 16px 7px;
}

.tgl-23__group {
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
}

.tgl-23__row {
  display: flex;
  align-items: center;
  gap: 12px;
  height: var(--row-h);
  padding: 0 16px;
  cursor: pointer;
}

.tgl-23__row:not(:last-child) {
  position: relative;
}

.tgl-23__row:not(:last-child)::after {
  content: "";
  position: absolute;
  left: 58px;
  right: 0;
  bottom: 0;
  height: 0.5px;
  background: #c6c6c8;
}

.tgl-23__glyph {
  flex: none;
  width: 30px;
  height: 30px;
  border-radius: 7px;
  background: var(--g);
  color: #fff;
  display: grid;
  place-items: center;
  font-size: 15px;
}

.tgl-23__name {
  flex: 1;
  font-size: 16px;
  color: #000;
}

.tgl-23__sw {
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

.tgl-23__sw::before {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  width: 27px;
  height: 27px;
  border-radius: 14px;
  background: #fff;
  box-shadow: 0 3px 8px rgba(0,0,0,.15),0 1px 1px rgba(0,0,0,.16);
  transition: transform .3s cubic-bezier(.2,.9,.25,1.05);
}

.tgl-23__sw:checked {
  background: #34c759;
}

.tgl-23__sw:checked::before {
  transform: translateX(20px);
}

.tgl-23__sw:focus-visible {
  outline: 3px solid #007aff;
  outline-offset: 2px;
}

.tgl-23__foot {
  font-size: 13px;
  line-height: 1.4;
  color: #6d6d72;
  margin: 7px 16px 0;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-23__sw,
    .tgl-23__sw::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — grouped iOS list built from whole-row labels; inset hairlines start after the glyph column and each switch is a bare appearance:none checkbox. */
```
