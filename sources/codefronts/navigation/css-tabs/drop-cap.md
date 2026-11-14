---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/drop-cap/"
title: "Drop Cap"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Inactive tabs are mono single-letter initials."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Drop Cap
Source: https://codefronts.com/navigation/css-tabs/drop-cap/

Inactive tabs are mono single-letter initials. The active tab unfolds into a rotating-and-scaling serif drop cap followed by the rest of the word; tail unfolds left-to-right.
## HTML
```html
<div class="tt07">
  <nav class="tt07n">
    <input type="radio" name="tt07" id="tt07-r1" checked />
    <label class="tt07b" for="tt07-r1">
      <span class="tt07cap">A</span>
      <span class="tt07rest">rticle</span>
    </label>
    <input type="radio" name="tt07" id="tt07-r2" />
    <label class="tt07b" for="tt07-r2">
      <span class="tt07cap">G</span>
      <span class="tt07rest">allery</span>
    </label>
    <input type="radio" name="tt07" id="tt07-r3" />
    <label class="tt07b" for="tt07-r3">
      <span class="tt07cap">N</span>
      <span class="tt07rest">otes</span>
    </label>
  </nav>
  <div class="tt07p">The body copy of an editorial feature.</div>
  <div class="tt07p">A curated set of plates and engravings.</div>
  <div class="tt07p">Marginalia and footnote annotations.</div>
</div>
```
## CSS
```css
.tt07 {
  min-height: 100vh;
  background: #e8dec8;
  padding: 22px 22px 18px;
  width: 100%;
}

.tt07n {
  display: flex;
  gap: 22px;
  align-items: baseline;
  border-bottom: 1px solid rgba(12, 85, 96, 0.22);
  padding-bottom: 14px;
}

.tt07n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt07b {
  border: 0;
  background: transparent;
  padding: 0;
  cursor: pointer;
  display: inline-flex;
  align-items: baseline;
  color: #0c5560;
  transition: opacity 0.3s;
}

.tt07cap {
  font: 900 26px/1 ui-serif, Georgia, serif;
  color: #0c5560;
  display: inline-block;
  transform-origin: center bottom;
  transition: color 0.35s, transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tt07rest {
  font: italic 16px/1 ui-serif, Georgia, serif;
  color: #0c5560;
  margin-left: 1px;
  max-width: 0;
  overflow: hidden;
  white-space: nowrap;
  transition: max-width 0.5s cubic-bezier(0.65, 0, 0.35, 1) 0.1s;
  opacity: 0.7;
}

.tt07b {
  opacity: 0.4;
}

.tt07b:hover {
  opacity: 0.78;
}

.tt07n input:checked + .tt07b {
  opacity: 1;
}

.tt07n input:checked + .tt07b .tt07cap {
  color: #d44a2a;
  transform: rotate(-4deg) scale(1.15);
}

.tt07n input:checked + .tt07b .tt07rest {
  max-width: 200px;
}

.tt07p {
  display: none;
  padding-top: 14px;
  font: italic 12px/1.6 ui-serif, Georgia, serif;
  color: #3a3a42;
}

.tt07:has(#tt07-r1:checked) .tt07p:nth-of-type(1),
.tt07:has(#tt07-r2:checked) .tt07p:nth-of-type(2),
.tt07:has(#tt07-r3:checked) .tt07p:nth-of-type(3) {
  display: block;
}
```
