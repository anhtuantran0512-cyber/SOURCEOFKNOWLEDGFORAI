---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/folio-fold/"
title: "Folio Fold"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Inactive tabs are flat sand-colored rectangles on charcoal."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Folio Fold
Source: https://codefronts.com/navigation/css-tabs/folio-fold/

Inactive tabs are flat sand-colored rectangles on charcoal. The active tab's top-right corner physically folds down 18px via clip-path with a darker fold-underside triangle, lifts 4px above its siblings, and shows a small fold preview on hover. Inactive tabs preview an 8px fold on hover so the mechanic is discoverable.
## HTML
```html
<div class="tt18">
  <nav class="tt18n">
    <input type="radio" name="tt18" id="tt18-r1" checked />
    <label class="tt18b" for="tt18-r1">
      Page 1
      <span class="tt18fold" aria-hidden="true"> </span>
    </label>
    <input type="radio" name="tt18" id="tt18-r2" />
    <label class="tt18b" for="tt18-r2">
      Page 2
      <span class="tt18fold" aria-hidden="true"> </span>
    </label>
    <input type="radio" name="tt18" id="tt18-r3" />
    <label class="tt18b" for="tt18-r3">
      Page 3
      <span class="tt18fold" aria-hidden="true"> </span>
    </label>
  </nav>
  <div class="tt18p">The opening recto.</div>
  <div class="tt18p">The continuation.</div>
  <div class="tt18p">The closing leaf.</div>
</div>
```
## CSS
```css
.tt18 {
  min-height: 100vh;
  background: #25222e;
  padding: 26px 22px 22px;
  font-family: ui-serif, Georgia, serif;
  width: 100%;
}

.tt18n {
  display: flex;
  gap: 6px;
  align-items: stretch;
}

.tt18n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt18b {
  position: relative;
  flex: 1;
  padding: 16px 18px;
  border: 0;
  background: #d4a574;
  font: 600 13px/1 ui-serif, Georgia, serif;
  color: rgba(26, 26, 26, 0.55);
  cursor: pointer;
  text-align: left;
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  transition: clip-path 0.45s cubic-bezier(0.65, 0, 0.35, 1), color 0.25s, transform 0.3s, box-shadow 0.4s, background 0.25s;
}

.tt18b:hover {
  color: rgba(26, 26, 26, 0.9);
  background: #dcb084;
  clip-path: polygon(0 0, calc(100% - 8px) 0, 100% 8px, 100% 100%, 0 100%);
}

.tt18n input:checked + .tt18b {
  color: #1a1a1a;
  background: #e6c39c;
  clip-path: polygon(0 0, calc(100% - 18px) 0, 100% 18px, 100% 100%, 0 100%);
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.45), 0 -2px 0 rgba(255, 255, 255, 0.18) inset;
}

.tt18fold {
  position: absolute;
  top: 0;
  right: 0;
  width: 18px;
  height: 18px;
  background: #1c1a24;
  clip-path: polygon(100% 0, 100% 100%, 0 100%);
  opacity: 0;
  transition: opacity 0.25s 0.2s, width 0.4s cubic-bezier(0.65, 0, 0.35, 1), height 0.4s cubic-bezier(0.65, 0, 0.35, 1);
}

.tt18b:hover .tt18fold {
  opacity: 0.85;
  width: 8px;
  height: 8px;
}

.tt18n input:checked + .tt18b .tt18fold {
  opacity: 1;
  width: 18px;
  height: 18px;
}

.tt18p {
  display: none;
  padding-top: 14px;
  font: italic 12px/1.6 ui-serif, Georgia;
  color: rgba(212, 165, 116, 0.85);
}

.tt18:has(#tt18-r1:checked) .tt18p:nth-of-type(1),
.tt18:has(#tt18-r2:checked) .tt18p:nth-of-type(2),
.tt18:has(#tt18-r3:checked) .tt18p:nth-of-type(3) {
  display: block;
}
```
