---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/cropped-letter/"
title: "Cropped Letter"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "The active tab's first letter scales 14→32px, baseline-shifts down, and crops at the tab's right edge. Inactive labels stay at compact display size."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cropped Letter
Source: https://codefronts.com/navigation/css-tabs/cropped-letter/

The active tab's first letter scales 14→32px, baseline-shifts down, and crops at the tab's right edge. Inactive labels stay at compact display size.
## HTML
```html
<div class="tt02">
  <nav class="tt02n">
    <input type="radio" name="tt02" id="tt02-r1" checked />
    <label class="tt02b" for="tt02-r1">
      <span class="tt02hd">Design</span>
    </label>
    <input type="radio" name="tt02" id="tt02-r2" />
    <label class="tt02b" for="tt02-r2">
      <span class="tt02hd">Code</span>
    </label>
    <input type="radio" name="tt02" id="tt02-r3" />
    <label class="tt02b" for="tt02-r3">
      <span class="tt02hd">Preview</span>
    </label>
  </nav>
  <div class="tt02p">Tokens, components, motion.</div>
  <div class="tt02p">Modern CSS, zero deps.</div>
  <div class="tt02p">Live with all states.</div>
</div>
```
## CSS
```css
.tt02 {
  min-height: 100vh;
  background: #1a1a1a;
  padding: 14px 0 16px;
  font-family: ui-serif, Georgia, serif;
  width: 100%;
}

.tt02n {
  display: flex;
  gap: 0;
  border-top: 1px solid rgba(232, 226, 208, 0.18);
  border-bottom: 1px solid rgba(232, 226, 208, 0.18);
}

.tt02n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt02b {
  flex: 1 1 0;
  min-width: 0;
  height: 64px;
  padding: 0;
  border: 0;
  background: transparent;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  border-right: 1px solid rgba(232, 226, 208, 0.12);
  display: block;
}

.tt02n label.tt02b:last-of-type {
  border-right: 0;
}

.tt02hd {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: block;
  font: 600 14px/1 ui-serif, Georgia, serif;
  color: rgba(232, 226, 208, 0.5);
  letter-spacing: 0.02em;
  white-space: nowrap;
  transition: color 0.25s, font-size 0.5s cubic-bezier(0.65, 0, 0.35, 1), transform 0.5s cubic-bezier(0.65, 0, 0.35, 1);
}

.tt02b:hover .tt02hd {
  color: rgba(232, 226, 208, 0.85);
}

.tt02n input:checked + .tt02b .tt02hd {
  color: #e8e2d0;
  font-size: 28px;
  transform: translate(-50%, -50%);
}

.tt02p {
  display: none;
  padding: 10px 18px 0;
  font: 11px/1.55 ui-monospace, monospace;
  color: rgba(232, 226, 208, 0.65);
  letter-spacing: 0.04em;
}

.tt02:has(#tt02-r1:checked) .tt02p:nth-of-type(1),
.tt02:has(#tt02-r2:checked) .tt02p:nth-of-type(2),
.tt02:has(#tt02-r3:checked) .tt02p:nth-of-type(3) {
  display: block;
}
```
