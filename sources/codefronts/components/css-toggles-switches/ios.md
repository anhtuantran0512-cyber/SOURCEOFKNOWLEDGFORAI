---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/ios/"
title: "iOS"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "The reference iOS-style pill toggle — translucent track, white thumb with a subtle drop shadow, smooth slide on toggle. Honors prefers-reduced-motion."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS
Source: https://codefronts.com/components/css-toggles-switches/ios/

The reference iOS-style pill toggle — translucent track, white thumb with a subtle drop shadow, smooth slide on toggle. Honors prefers-reduced-motion.
## HTML
```html
<label class="tgl-34">
  <input class="tgl-34__input" type="checkbox" checked>
  <span class="tgl-34__track" aria-hidden="true">
    <span class="tgl-34__thumb"></span>
  </span>
  <span class="tgl-34__label">Wi-Fi</span>
</label>
```
## CSS
```css
.tgl-34 {
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
  font-size: 15px;
  color: #f0eeff;
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

.tgl-34__input {
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

.tgl-34__track {
  position: relative;
  width: 51px;
  height: 31px;
  background: rgba(120,120,128,0.32);
  border-radius: 999px;
  transition: background 0.25s ease;
}

.tgl-34__thumb {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 27px;
  height: 27px;
  border-radius: 50%;
  background: #ffffff;
  /* Tighter shadow than real iOS — on iOS the shadow casts onto the
       screen background; here the toggle sits on a card and a softer
       shadow keeps the thumb visually contained within the track. */
  box-shadow: 0 1px 2px rgba(0,0,0,0.18), 0 0 1px rgba(0,0,0,0.08);
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.tgl-34__input:checked ~ .tgl-34__track {
  background: #34c759;
}

.tgl-34__input:checked ~ .tgl-34__track .tgl-34__thumb {
  transform: translateX(20px);
}

.tgl-34__input:focus-visible ~ .tgl-34__track {
  outline: 2px solid #0a84ff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-34__track,
    .tgl-34__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — sr-only checkbox drives track color and a 20px transform:translateX thumb slide via :checked ~ rules. */
```
