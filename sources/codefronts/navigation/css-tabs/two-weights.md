---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/two-weights/"
title: "Two Weights"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Pure type-weight contrast. Inactive sits at 200 hairline, active jumps to 900 black with a subtle scale lift. The brand violet underlines the active label."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Two Weights
Source: https://codefronts.com/navigation/css-tabs/two-weights/

Pure type-weight contrast. Inactive sits at 200 hairline, active jumps to 900 black with a subtle scale lift. The brand violet underlines the active label.
## HTML
```html
<div class="tt05">
  <nav class="tt05n">
    <input type="radio" name="tt05" id="tt05-r1" checked />
    <label class="tt05b" for="tt05-r1">Overview</label>
    <input type="radio" name="tt05" id="tt05-r2" />
    <label class="tt05b" for="tt05-r2">Activity</label>
    <input type="radio" name="tt05" id="tt05-r3" />
    <label class="tt05b" for="tt05-r3">Settings</label>
  </nav>
  <div class="tt05p">A summary of the project, members, and recent decisions.</div>
  <div class="tt05p">Edits, comments, and team mentions over the last seven days.</div>
  <div class="tt05p">Permissions, integrations, and billing controls.</div>
</div>
```
## CSS
```css
.tt05 {
  min-height: 100vh;
  background: #15151d;
  padding: 26px 22px 22px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  width: 100%;
}

.tt05n {
  display: flex;
  gap: 28px;
}

.tt05n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt05b {
  position: relative;
  border: 0;
  background: transparent;
  padding: 0 0 8px;
  font: 200 26px/1 ui-sans-serif, system-ui;
  color: #e8e2d0;
  cursor: pointer;
  letter-spacing: -0.02em;
  font-variation-settings: "wght" 200;
  transform: scale(0.96);
  transform-origin: bottom left;
  transition: font-weight 0.45s, font-variation-settings 0.45s, transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tt05b::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 2px;
  background: #7c5cff;
  transform-origin: left;
  transform: scaleX(0);
  transition: transform 0.5s cubic-bezier(0.65, 0, 0.35, 1);
}

.tt05b:hover {
  font-variation-settings: "wght" 400;
}

.tt05n input:checked + .tt05b {
  font-weight: 900;
  font-variation-settings: "wght" 900;
  transform: scale(1);
}

.tt05n input:checked + .tt05b::after {
  transform: scaleX(1);
}

.tt05p {
  display: none;
  padding-top: 16px;
  font: 12px/1.6 ui-serif, Georgia, serif;
  color: rgba(232, 226, 208, 0.7);
  max-width: 360px;
}

.tt05:has(#tt05-r1:checked) .tt05p:nth-of-type(1),
.tt05:has(#tt05-r2:checked) .tt05p:nth-of-type(2),
.tt05:has(#tt05-r3:checked) .tt05p:nth-of-type(3) {
  display: block;
}
```
