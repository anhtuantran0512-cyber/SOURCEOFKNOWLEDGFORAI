---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/stencil-cut/"
title: "Stencil Cut"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Active tab is a solid safety-yellow plate stamped on ink."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stencil Cut
Source: https://codefronts.com/navigation/css-tabs/stencil-cut/

Active tab is a solid safety-yellow plate stamped on ink. Pure two-color print — black ink on yellow for the active label, muted yellow on ink for inactive. The 2px upward translate gives the yellow plate a small physical lift over the surrounding stage.
## HTML
```html
<div class="tt08">
  <nav class="tt08n">
    <input type="radio" name="tt08" id="tt08-r1" />
    <label class="tt08b" for="tt08-r1">
      <span>READ</span>
    </label>
    <input type="radio" name="tt08" id="tt08-r2" checked />
    <label class="tt08b" for="tt08-r2">
      <span>WRITE</span>
    </label>
    <input type="radio" name="tt08" id="tt08-r3" />
    <label class="tt08b" for="tt08-r3">
      <span>SHIP</span>
    </label>
  </nav>
  <div class="tt08p">Drafts, archives, and reference material.</div>
  <div class="tt08p">The current notebook in active edit mode.</div>
  <div class="tt08p">Approvals, releases, and publication state.</div>
</div>
```
## CSS
```css
.tt08 {
  min-height: 100vh;
  background: #1a1a1a;
  padding: 22px 22px 18px;
  font-family: ui-monospace, monospace;
  width: 100%;
}

.tt08n {
  display: flex;
  gap: 8px;
}

.tt08n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt08b {
  flex: 1;
  padding: 14px 12px;
  border: 0;
  background: transparent;
  font: 900 14px/1 ui-monospace, monospace;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: rgba(245, 203, 26, 0.45);
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: color 0.25s, background 0.25s, transform 0.25s;
}

.tt08b:hover {
  color: rgba(245, 203, 26, 0.8);
}

.tt08n input:checked + .tt08b {
  color: #1a1a1a;
  background: #f5cb1a;
  transform: translateY(-2px);
  box-shadow: 0 4px 0 -2px rgba(0, 0, 0, 0.4);
}

.tt08p {
  display: none;
  padding-top: 14px;
  font: 11px/1.6 ui-serif, Georgia, serif;
  color: rgba(232, 226, 208, 0.7);
  font-style: italic;
}

.tt08:has(#tt08-r1:checked) .tt08p:nth-of-type(1),
.tt08:has(#tt08-r2:checked) .tt08p:nth-of-type(2),
.tt08:has(#tt08-r3:checked) .tt08p:nth-of-type(3) {
  display: block;
}
```
