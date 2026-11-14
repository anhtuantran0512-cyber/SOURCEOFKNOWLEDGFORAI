---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/sliding-pill-with-label/"
title: "Sliding Pill with Label"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A track containing both labels (ON / OFF) with a thumb that slides over the active one. Common SaaS-dashboard pattern — the label IS the indicator."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliding Pill with Label
Source: https://codefronts.com/components/css-toggles-switches/sliding-pill-with-label/

A track containing both labels (ON / OFF) with a thumb that slides over the active one. Common SaaS-dashboard pattern — the label IS the indicator.
## HTML
```html
<label class="tgl-41">
  <input class="tgl-41__input" type="checkbox" checked>
  <span class="tgl-41__track" aria-hidden="true">
    <span class="tgl-41__text tgl-41__on">ON</span>
    <span class="tgl-41__text tgl-41__off">OFF</span>
    <span class="tgl-41__thumb"></span>
  </span>
  <span class="tgl-41__label">Public profile</span>
</label>
```
## CSS
```css
.tgl-41 {
  font-family: "Inter", "Segoe UI", system-ui, sans-serif;
  font-size: 14px;
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

.tgl-41__input {
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

.tgl-41__track {
  position: relative;
  width: 76px;
  height: 28px;
  background: #2a2a30;
  border-radius: 999px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  transition: background 0.25s ease;
}

.tgl-41__text {
  position: relative;
  z-index: 2;
  text-align: center;
  transition: color 0.25s ease;
  pointer-events: none;
}

.tgl-41__on {
  color: #7c6cff;
}

.tgl-41__off {
  color: #6a6a7a;
}

.tgl-41__thumb {
  position: absolute;
  top: 2px;
  left: 2px;
  width: calc(50% - 2px);
  height: calc(100% - 4px);
  background: #f0eeff;
  border-radius: 999px;
  z-index: 1;
  transition: left 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 1px 2px rgba(0,0,0,0.3);
}

.tgl-41__input:checked ~ .tgl-41__track .tgl-41__on {
  color: #1a1a1a;
}

.tgl-41__input:checked ~ .tgl-41__track .tgl-41__off {
  color: #6a6a7a;
}

.tgl-41__input:not(:checked) ~ .tgl-41__track .tgl-41__on {
  color: #6a6a7a;
}

.tgl-41__input:not(:checked) ~ .tgl-41__track .tgl-41__off {
  color: #1a1a1a;
}

.tgl-41__input:not(:checked) ~ .tgl-41__track .tgl-41__thumb {
  left: 50%;
}

.tgl-41__input:focus-visible ~ .tgl-41__track {
  outline: 2px solid #7c6cff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-41__thumb,
    .tgl-41__text,
    .tgl-41__track {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a half-width pill thumb slides between grid-centered ON/OFF words, recoloring whichever it covers. */
```
