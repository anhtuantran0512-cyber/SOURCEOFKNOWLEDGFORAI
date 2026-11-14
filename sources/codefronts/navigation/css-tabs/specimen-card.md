---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/specimen-card/"
title: "Specimen Card"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "The whole bar reads as a foundry specimen card."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Specimen Card
Source: https://codefronts.com/navigation/css-tabs/specimen-card/

The whole bar reads as a foundry specimen card. Foundry name on the left in tiny mono; tabs on the right are large display glyph specimens. On activation the foundry name pulses a single beat.
## HTML
```html
<div class="tt16">
  <nav class="tt16n">
    <div class="tt16meta">
      <div class="tt16name">
        CodeFronts
        <br />Foundry
      </div>
      <div class="tt16id">SPEC · 2026</div>
    </div>
    <div class="tt16tabs">
      <input type="radio" name="tt16" id="tt16-r1" checked />
      <label class="tt16b" for="tt16-r1">Aa</label>
      <input type="radio" name="tt16" id="tt16-r2" />
      <label class="tt16b" for="tt16-r2">Bb</label>
      <input type="radio" name="tt16" id="tt16-r3" />
      <label class="tt16b" for="tt16-r3">Cc</label>
    </div>
  </nav>
  <div class="tt16p">Specimen of the upright Roman cut.</div>
  <div class="tt16p">Specimen of the bold cut.</div>
  <div class="tt16p">Specimen of the small caps cut.</div>
</div>
```
## CSS
```css
.tt16 {
  min-height: 100vh;
  background: #1a1a1a;
  padding: 16px 22px;
  font-family: ui-serif, Georgia, serif;
  width: 100%;
}

.tt16n {
  display: flex;
  align-items: stretch;
  gap: 22px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(232, 226, 208, 0.18);
}

.tt16n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt16meta {
  padding-right: 22px;
  border-right: 1px solid rgba(232, 226, 208, 0.18);
  transition: opacity 0.4s;
}

.tt16name {
  font: 800 11px/1.3 ui-monospace, monospace;
  color: #e8e2d0;
  letter-spacing: 0.2em;
  text-transform: uppercase;
}

.tt16id {
  font: 600 9px/1 ui-monospace, monospace;
  color: rgba(232, 226, 208, 0.5);
  margin-top: 6px;
  letter-spacing: 0.2em;
}

.tt16tabs {
  display: flex;
  gap: 18px;
  align-items: baseline;
}

.tt16b {
  border: 0;
  background: transparent;
  padding: 0;
  font: 700 28px/1 ui-serif, Georgia, serif;
  color: rgba(232, 226, 208, 0.4);
  cursor: pointer;
  transition: color 0.3s, transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tt16b:hover {
  color: rgba(232, 226, 208, 0.8);
}

.tt16n input:checked + .tt16b {
  color: #c43a32;
  transform: scale(1.15);
}

.tt16p {
  display: none;
  padding-top: 12px;
  font: italic 11px/1.6 ui-serif, Georgia, serif;
  color: rgba(232, 226, 208, 0.7);
}

.tt16:has(#tt16-r1:checked) .tt16p:nth-of-type(1),
.tt16:has(#tt16-r2:checked) .tt16p:nth-of-type(2),
.tt16:has(#tt16-r3:checked) .tt16p:nth-of-type(3) {
  display: block;
}
```
