---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/slab-serif-swash/"
title: "Slab Serif Swash"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Italic slab-serif labels on warm-cream stock."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slab Serif Swash
Source: https://codefronts.com/navigation/css-tabs/slab-serif-swash/

Italic slab-serif labels on warm-cream stock. The active tab gets a deep-emerald swash underline — a curved SVG stroke beneath the word, like a calligrapher's flourish on letterpress vellum.
## HTML
```html
<div class="tt15">
  <nav class="tt15n">
    <input type="radio" name="tt15" id="tt15-r1" checked />
    <label class="tt15b" for="tt15-r1">
      Manifesto
      <svg class="tt15s" viewBox="0 0 80 12" aria-hidden="true">
        <path
          d="M 2 8 Q 20 2 40 6 T 78 8"
          fill="none"
          stroke="#0f4f3d"
          stroke-width="1.6"
          stroke-linecap="round"
        />
      </svg>
    </label>
    <input type="radio" name="tt15" id="tt15-r2" />
    <label class="tt15b" for="tt15-r2">
      Colophon
      <svg class="tt15s" viewBox="0 0 80 12" aria-hidden="true">
        <path
          d="M 2 8 Q 20 2 40 6 T 78 8"
          fill="none"
          stroke="#0f4f3d"
          stroke-width="1.6"
          stroke-linecap="round"
        />
      </svg>
    </label>
    <input type="radio" name="tt15" id="tt15-r3" />
    <label class="tt15b" for="tt15-r3">
      Errata
      <svg class="tt15s" viewBox="0 0 80 12" aria-hidden="true">
        <path
          d="M 2 8 Q 20 2 40 6 T 78 8"
          fill="none"
          stroke="#0f4f3d"
          stroke-width="1.6"
          stroke-linecap="round"
        />
      </svg>
    </label>
  </nav>
  <div class="tt15p">The founding statement of intent.</div>
  <div class="tt15p">The closing inscription, type & paper notes.</div>
  <div class="tt15p">Corrections issued after the first printing.</div>
</div>
```
## CSS
```css
.tt15 {
  min-height: 100vh;
  background: #fdf4d6;
  padding: 22px 22px 26px;
  font-family: ui-serif, "Times New Roman", serif;
  width: 100%;
}

.tt15n {
  display: flex;
  gap: 28px;
  align-items: flex-end;
}

.tt15n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt15b {
  position: relative;
  border: 0;
  background: transparent;
  padding: 0 0 4px;
  font: italic 700 18px/1 ui-serif, "Times New Roman", serif;
  color: rgba(15, 79, 61, 0.55);
  cursor: pointer;
  transition: color 0.25s;
}

.tt15b:hover {
  color: rgba(15, 79, 61, 0.9);
}

.tt15n input:checked + .tt15b {
  color: #0f4f3d;
}

.tt15s {
  position: absolute;
  bottom: -8px;
  left: 0;
  right: 0;
  width: 100%;
  height: 12px;
  opacity: 0;
  stroke-dasharray: 100;
  stroke-dashoffset: 100;
  transition: opacity 0.2s, stroke-dashoffset 0.6s cubic-bezier(0.65, 0, 0.35, 1);
}

.tt15n input:checked + .tt15b .tt15s {
  opacity: 1;
  stroke-dashoffset: 0;
}

.tt15p {
  display: none;
  padding-top: 18px;
  font: italic 12px/1.6 ui-serif, Georgia;
  color: #3a3a42;
}

.tt15:has(#tt15-r1:checked) .tt15p:nth-of-type(1),
.tt15:has(#tt15-r2:checked) .tt15p:nth-of-type(2),
.tt15:has(#tt15-r3:checked) .tt15p:nth-of-type(3) {
  display: block;
}
```
