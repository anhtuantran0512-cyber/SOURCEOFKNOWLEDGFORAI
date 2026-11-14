---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/bauhaus-block/"
title: "Bauhaus Block"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Each tab is a distinct primary-color block. Active tab rises 6px and casts a hard offset shadow. Color and geometry as the entire indicator."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bauhaus Block
Source: https://codefronts.com/navigation/css-tabs/bauhaus-block/

Each tab is a distinct primary-color block. Active tab rises 6px and casts a hard offset shadow. Color and geometry as the entire indicator.
## HTML
```html
<div class="tt10">
  <nav class="tt10n">
    <input type="radio" name="tt10" id="tt10-r1" checked />
    <label class="tt10b tt10-1" for="tt10-r1">FORM</label>
    <input type="radio" name="tt10" id="tt10-r2" />
    <label class="tt10b tt10-2" for="tt10-r2">GRID</label>
    <input type="radio" name="tt10" id="tt10-r3" />
    <label class="tt10b tt10-3" for="tt10-r3">TYPE</label>
    <input type="radio" name="tt10" id="tt10-r4" />
    <label class="tt10b tt10-4" for="tt10-r4">HUE</label>
  </nav>
  <div class="tt10p">Composition, weight, balance.</div>
  <div class="tt10p">Modular columns and rows.</div>
  <div class="tt10p">Specimens and pairings.</div>
  <div class="tt10p">Limited primary palette.</div>
</div>
```
## CSS
```css
.tt10 {
  min-height: 100vh;
  background: #f5ead0;
  padding: 22px 18px 16px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  width: 100%;
}

.tt10n {
  display: flex;
  gap: 6px;
}

.tt10n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt10b {
  flex: 1;
  padding: 16px 8px;
  border: 0;
  font: 800 11px/1 ui-monospace, monospace;
  letter-spacing: 0.22em;
  cursor: pointer;
  text-align: center;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s;
}

.tt10-1 {
  background: #c43a32;
  color: #f5ead0;
}

.tt10-2 {
  background: #d4a017;
  color: #1a1a1a;
}

.tt10-3 {
  background: #1a1a1a;
  color: #e8e2d0;
}

.tt10-4 {
  background: #f5ead0;
  color: #1a1a1a;
  box-shadow: inset 0 0 0 1.5px #1a1a1a;
}

.tt10b:hover {
  transform: translateY(-2px);
}

.tt10n input:checked + .tt10b {
  transform: translateY(-6px);
  box-shadow: 0 6px 0 #1a1a1a;
}

.tt10n input:checked + .tt10-4 {
  box-shadow: inset 0 0 0 1.5px #1a1a1a, 0 6px 0 #1a1a1a;
}

.tt10p {
  display: none;
  padding-top: 14px;
  font: 11px/1.6 ui-serif, Georgia, serif;
  color: #3a3a42;
  font-style: italic;
}

.tt10:has(#tt10-r1:checked) .tt10p:nth-of-type(1),
.tt10:has(#tt10-r2:checked) .tt10p:nth-of-type(2),
.tt10:has(#tt10-r3:checked) .tt10p:nth-of-type(3),
.tt10:has(#tt10-r4:checked) .tt10p:nth-of-type(4) {
  display: block;
}
```
