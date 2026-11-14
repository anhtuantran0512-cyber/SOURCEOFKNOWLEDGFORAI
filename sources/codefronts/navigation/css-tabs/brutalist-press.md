---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/brutalist-press/"
title: "Brutalist Press"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Heavy uppercase tabs with hard 4px black offset shadows."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Press
Source: https://codefronts.com/navigation/css-tabs/brutalist-press/

Heavy uppercase tabs with hard 4px black offset shadows. Active tab presses flush — shadow collapses, button translates 4px down-right, color inverts. Tactile mechanical-keyboard feedback.
## HTML
```html
<div class="tt23">
  <nav class="tt23n">
    <input type="radio" name="tt23" id="tt23-r1" checked />
    <label class="tt23b" for="tt23-r1">Build</label>
    <input type="radio" name="tt23" id="tt23-r2" />
    <label class="tt23b" for="tt23-r2">Ship</label>
    <input type="radio" name="tt23" id="tt23-r3" />
    <label class="tt23b" for="tt23-r3">Iterate</label>
  </nav>
  <div class="tt23p">Build — assemble the parts.</div>
  <div class="tt23p">Ship — push it to production.</div>
  <div class="tt23p">Iterate — measure and refine.</div>
</div>
```
## CSS
```css
.tt23 {
  background: #fef0c7;
  padding: 26px 22px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.tt23n {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  min-width: 0;
}

.tt23n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt23b {
  flex: 1;
  min-width: 0;
  padding: 12px 16px;
  border: 3px solid #0a0a0a;
  background: #fff;
  font: 800 12px/1 ui-sans-serif, system-ui;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #0a0a0a;
  cursor: pointer;
  text-align: center;
  box-shadow: 4px 4px 0 0 #0a0a0a;
  transition: transform 0.12s ease-out, box-shadow 0.12s ease-out, background 0.2s, color 0.2s;
  white-space: nowrap;
}

.tt23b:hover {
  background: #f4e7b3;
}

.tt23n input:checked + .tt23b {
  transform: translate(4px, 4px);
  box-shadow: 0 0 0 0 #0a0a0a;
  background: #0a0a0a;
  color: #fef0c7;
}

.tt23n input:focus-visible + .tt23b {
  outline: 2px dashed #0a0a0a;
  outline-offset: 4px;
}

.tt23p {
  display: none;
  padding-top: 22px;
  font: 600 13px/1.55 ui-sans-serif, system-ui;
  color: #0a0a0a;
}

.tt23:has(#tt23-r1:checked) .tt23p:nth-of-type(1),
.tt23:has(#tt23-r2:checked) .tt23p:nth-of-type(2),
.tt23:has(#tt23-r3:checked) .tt23p:nth-of-type(3) {
  display: block;
}
```
