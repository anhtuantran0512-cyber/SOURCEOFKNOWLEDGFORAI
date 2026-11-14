---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/inset-type/"
title: "Inset Type"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Active label sits inside a chiseled negative-space well."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inset Type
Source: https://codefronts.com/navigation/css-tabs/inset-type/

Active label sits inside a chiseled negative-space well. Inset shadow stack on a darker rectangle gives the impression letters are carved into brass-tinted slate. Pure CSS box-shadow, no images.
## HTML
```html
<div class="tt20">
  <nav class="tt20n">
    <input type="radio" name="tt20" id="tt20-r1" checked />
    <label class="tt20b" for="tt20-r1">Etch</label>
    <input type="radio" name="tt20" id="tt20-r2" />
    <label class="tt20b" for="tt20-r2">Engrave</label>
    <input type="radio" name="tt20" id="tt20-r3" />
    <label class="tt20b" for="tt20-r3">Emboss</label>
  </nav>
  <div class="tt20p">Acid bites the plate to print recessed lines.</div>
  <div class="tt20p">A burin cuts directly into the metal surface.</div>
  <div class="tt20p">Pressure raises the paper into a relief.</div>
</div>
```
## CSS
```css
.tt20 {
  min-height: 100vh;
  background: #3a3a42;
  padding: 22px 22px 18px;
  font-family: ui-monospace, monospace;
  width: 100%;
}

.tt20n {
  display: flex;
  gap: 8px;
  padding: 8px;
  background: #2a2a30;
  border-radius: 4px;
}

.tt20n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt20b {
  flex: 1;
  padding: 14px 12px;
  border: 0;
  background: transparent;
  font: 800 12px/1 ui-monospace, monospace;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: rgba(201, 161, 94, 0.6);
  cursor: pointer;
  border-radius: 3px;
  transition: color 0.25s, background 0.3s, box-shadow 0.3s;
}

.tt20b:hover {
  color: rgba(201, 161, 94, 0.95);
}

.tt20n input:checked + .tt20b {
  background: #1f1f24;
  color: #c9a15e;
  box-shadow: inset 2px 2px 4px rgba(0, 0, 0, 0.55), inset -1px -1px 2px rgba(255, 255, 255, 0.08);
  text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.55);
}

.tt20p {
  display: none;
  padding-top: 14px;
  font: italic 11px/1.6 ui-serif, Georgia, serif;
  color: rgba(201, 161, 94, 0.8);
}

.tt20:has(#tt20-r1:checked) .tt20p:nth-of-type(1),
.tt20:has(#tt20-r2:checked) .tt20p:nth-of-type(2),
.tt20:has(#tt20-r3:checked) .tt20p:nth-of-type(3) {
  display: block;
}
```
