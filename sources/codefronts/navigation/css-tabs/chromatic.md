---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/chromatic/"
title: "Chromatic"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Four color-coded tabs each with a dedicated tint, border, and active-state glow."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Chromatic
Source: https://codefronts.com/navigation/css-tabs/chromatic/

Four color-coded tabs each with a dedicated tint, border, and active-state glow. Violet, rose, cyan, lime — each tab keeps its identity whether active or inactive. Pure CSS.
## HTML
```html
<div class="tt24">
  <nav class="tt24n">
    <input type="radio" name="tt24" id="tt24-r1" checked />
    <label class="tt24b tt24-v" for="tt24-r1">Violet</label>
    <input type="radio" name="tt24" id="tt24-r2" />
    <label class="tt24b tt24-r" for="tt24-r2">Rose</label>
    <input type="radio" name="tt24" id="tt24-r3" />
    <label class="tt24b tt24-c" for="tt24-r3">Cyan</label>
    <input type="radio" name="tt24" id="tt24-r4" />
    <label class="tt24b tt24-l" for="tt24-r4">Lime</label>
  </nav>
  <div class="tt24p">Violet — deep, contemplative.</div>
  <div class="tt24p">Rose — warm, inviting.</div>
  <div class="tt24p">Cyan — crisp, technical.</div>
  <div class="tt24p">Lime — fresh, urgent.</div>
</div>
```
## CSS
```css
.tt24 {
  background: #0f0f17;
  padding: 24px 20px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.tt24n {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  min-width: 0;
}

.tt24n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt24b {
  flex: 1;
  min-width: 0;
  padding: 11px 14px;
  border-radius: 8px;
  font: 700 12px/1 ui-sans-serif, system-ui;
  letter-spacing: 0.06em;
  cursor: pointer;
  text-align: center;
  transition: background 0.25s, border-color 0.25s, box-shadow 0.3s;
  white-space: nowrap;
  border: 1px solid;
}

.tt24-v {
  color: #c4b5fd;
  border-color: rgba(196, 181, 253, 0.3);
  background: rgba(196, 181, 253, 0.06);
}

.tt24-r {
  color: #fda4af;
  border-color: rgba(253, 164, 175, 0.3);
  background: rgba(253, 164, 175, 0.06);
}

.tt24-c {
  color: #67e8f9;
  border-color: rgba(103, 232, 249, 0.3);
  background: rgba(103, 232, 249, 0.06);
}

.tt24-l {
  color: #bef264;
  border-color: rgba(190, 242, 100, 0.3);
  background: rgba(190, 242, 100, 0.06);
}

.tt24n input:checked + .tt24-v {
  background: rgba(196, 181, 253, 0.18);
  border-color: #c4b5fd;
  box-shadow: 0 0 18px rgba(196, 181, 253, 0.35);
}

.tt24n input:checked + .tt24-r {
  background: rgba(253, 164, 175, 0.18);
  border-color: #fda4af;
  box-shadow: 0 0 18px rgba(253, 164, 175, 0.35);
}

.tt24n input:checked + .tt24-c {
  background: rgba(103, 232, 249, 0.18);
  border-color: #67e8f9;
  box-shadow: 0 0 18px rgba(103, 232, 249, 0.35);
}

.tt24n input:checked + .tt24-l {
  background: rgba(190, 242, 100, 0.18);
  border-color: #bef264;
  box-shadow: 0 0 18px rgba(190, 242, 100, 0.35);
}

.tt24n input:focus-visible + .tt24b {
  outline: 2px dashed currentColor;
  outline-offset: 3px;
}

.tt24p {
  display: none;
  padding-top: 20px;
  font: 13px/1.55 ui-sans-serif, system-ui;
  color: rgba(255, 255, 255, 0.7);
}

.tt24:has(#tt24-r1:checked) .tt24p:nth-of-type(1),
.tt24:has(#tt24-r2:checked) .tt24p:nth-of-type(2),
.tt24:has(#tt24-r3:checked) .tt24p:nth-of-type(3),
.tt24:has(#tt24-r4:checked) .tt24p:nth-of-type(4) {
  display: block;
}
```
