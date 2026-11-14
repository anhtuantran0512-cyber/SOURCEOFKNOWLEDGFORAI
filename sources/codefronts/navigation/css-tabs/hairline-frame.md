---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/hairline-frame/"
title: "Hairline Frame"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Hairline-framed tabs in warm-white stock."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hairline Frame
Source: https://codefronts.com/navigation/css-tabs/hairline-frame/

Hairline-framed tabs in warm-white stock. Active tab's top edge thickens to 4px deep-navy AND four corner dots materialize at the frame's extremes — a Bodoni stroke-contrast move with editorial restraint.
## HTML
```html
<div class="tt12">
  <nav class="tt12n">
    <input type="radio" name="tt12" id="tt12-r1" checked />
    <label class="tt12b" for="tt12-r1">
      Drafts
      <span class="tt12tk tt12tk-1" aria-hidden="true"> </span>
      <span class="tt12tk tt12tk-2" aria-hidden="true"> </span>
      <span class="tt12tk tt12tk-3" aria-hidden="true"> </span>
      <span class="tt12tk tt12tk-4" aria-hidden="true"> </span>
    </label>
    <input type="radio" name="tt12" id="tt12-r2" />
    <label class="tt12b" for="tt12-r2">
      Proofs
      <span class="tt12tk tt12tk-1" aria-hidden="true"> </span>
      <span class="tt12tk tt12tk-2" aria-hidden="true"> </span>
      <span class="tt12tk tt12tk-3" aria-hidden="true"> </span>
      <span class="tt12tk tt12tk-4" aria-hidden="true"> </span>
    </label>
    <input type="radio" name="tt12" id="tt12-r3" />
    <label class="tt12b" for="tt12-r3">
      Final
      <span class="tt12tk tt12tk-1" aria-hidden="true"> </span>
      <span class="tt12tk tt12tk-2" aria-hidden="true"> </span>
      <span class="tt12tk tt12tk-3" aria-hidden="true"> </span>
      <span class="tt12tk tt12tk-4" aria-hidden="true"> </span>
    </label>
  </nav>
  <div class="tt12p">Working files in progress.</div>
  <div class="tt12p">Galleys ready for review.</div>
  <div class="tt12p">Approved and locked.</div>
</div>
```
## CSS
```css
.tt12 {
  min-height: 100vh;
  background: #f5f1ea;
  padding: 26px 22px 22px;
  font-family: ui-serif, Georgia, serif;
  width: 100%;
}

.tt12n {
  display: flex;
  gap: 14px;
}

.tt12n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt12b {
  position: relative;
  padding: 14px 24px 11px;
  border: 0.5px solid #1a2842;
  border-top: 4px solid transparent;
  background: transparent;
  font: 600 13px/1 ui-serif, Georgia, serif;
  letter-spacing: 0.06em;
  color: rgba(26, 40, 66, 0.5);
  cursor: pointer;
  transition: color 0.3s, border-top-color 0.3s, transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tt12b:hover {
  color: rgba(26, 40, 66, 0.85);
  transform: translateY(-1px);
}

.tt12n input:checked + .tt12b {
  color: #1a2842;
  border-top-color: #1a2842;
}

.tt12tk {
  position: absolute;
  width: 7px;
  height: 7px;
  background: #1a2842;
  border-radius: 50%;
  opacity: 0;
  transition: opacity 0.25s 0.1s, transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1) 0.1s;
}

.tt12tk-1 {
  top: -3.5px;
  left: -3.5px;
  transform: scale(0);
}

.tt12tk-2 {
  top: -3.5px;
  right: -3.5px;
  transform: scale(0);
}

.tt12tk-3 {
  bottom: -3.5px;
  left: -3.5px;
  transform: scale(0);
}

.tt12tk-4 {
  bottom: -3.5px;
  right: -3.5px;
  transform: scale(0);
}

.tt12n input:checked + .tt12b .tt12tk {
  opacity: 1;
  transform: scale(1);
}

.tt12p {
  display: none;
  padding-top: 16px;
  font: italic 12px/1.6 ui-serif, Georgia;
  color: #3a3a42;
}

.tt12:has(#tt12-r1:checked) .tt12p:nth-of-type(1),
.tt12:has(#tt12-r2:checked) .tt12p:nth-of-type(2),
.tt12:has(#tt12-r3:checked) .tt12p:nth-of-type(3) {
  display: block;
}
```
