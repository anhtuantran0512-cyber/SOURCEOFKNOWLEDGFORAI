---
source: "codefronts"
url: "https://codefronts.com/components/css-button-groups/subgrid-beam/"
title: "CSS Button Group with Subgrid Underline Beam (Perfectly Aligned Tab Indicator)"
section: "components"
category: "css-button-groups"
category_name: "CSS Button Groups"
description: "A tab-style button group where a glowing underline beam snaps beneath the active button — and, crucially, aligns to the exact button column using CSS…"
has_js: "false"
---

Here's a working CSS Button Group from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Button Group with Subgrid Underline Beam (Perfectly Aligned Tab Indicator)
Source: https://codefronts.com/components/css-button-groups/subgrid-beam/

A tab-style button group where a glowing underline beam snaps beneath the active button — and, crucially, aligns to the exact button column using CSS subgrid, so the beam is never a pixel off no matter the label lengths. The modern 'CSS subgrid underline beam tab indicator' pattern that finally kills manual offset math.
## HTML
```html
<section class="btn-13" aria-label="Subgrid underline beam button group demo">
  <div class="btn-13__wrap">
    <div class="btn-13__group" role="group" aria-label="Dashboard sections">
      <input type="radio" name="btn-13" id="btn-13-1" class="btn-13__in" checked>
      <label for="btn-13-1" class="btn-13__tab">Overview</label>
      <input type="radio" name="btn-13" id="btn-13-2" class="btn-13__in">
      <label for="btn-13-2" class="btn-13__tab">Analytics</label>
      <input type="radio" name="btn-13" id="btn-13-3" class="btn-13__in">
      <label for="btn-13-3" class="btn-13__tab">Reports</label>
      <input type="radio" name="btn-13" id="btn-13-4" class="btn-13__in">
      <label for="btn-13-4" class="btn-13__tab">Settings</label>
      <div class="btn-13__track"><span class="btn-13__beam" aria-hidden="true"></span></div>
    </div>
  </div>
</section>
```
## CSS
```css
.btn-13,
.btn-13 *,
.btn-13 *::before,
.btn-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.btn-13 {
  --accent: oklch(0.72 0.19 45);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,#12100e,#191510);
  padding: 44px 20px;
}

.btn-13__wrap {
  width: min(600px,100%);
}

.btn-13__group {
  display: grid;
  grid-template-columns: repeat(4,auto);
  justify-content: start;
  gap: 0 6px;
  position: relative;
}

.btn-13__in {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.btn-13__tab {
  grid-row: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 20px;
  font-size: 15.5px;
  font-weight: 700;
  color: #8f857a;
  cursor: pointer;
  transition: color .25s;
  border-radius: 9px;
}

.btn-13__tab:hover {
  color: #d9cfc2;
}

.btn-13__in:checked + .btn-13__tab {
  color: #fff;
}

.btn-13__track {
  grid-row: 2;
  grid-column: 1/-1;
  display: grid;
  grid-template-columns: subgrid;
  height: 5px;
  margin-top: 6px;
}

.btn-13__beam {
  grid-column: 1;
  justify-self: stretch;
  height: 5px;
  border-radius: 3px;
  background: var(--accent);
  box-shadow: 0 0 16px 1px var(--accent),0 0 40px 2px color-mix(in oklab,var(--accent) 60%,transparent);
  transition: grid-column .05s;
  position: relative;
}

.btn-13__group:has(#btn-13-1:checked) .btn-13__beam {
  grid-column: 1;
}

.btn-13__group:has(#btn-13-2:checked) .btn-13__beam {
  grid-column: 2;
}

.btn-13__group:has(#btn-13-3:checked) .btn-13__beam {
  grid-column: 3;
}

.btn-13__group:has(#btn-13-4:checked) .btn-13__beam {
  grid-column: 4;
}

.btn-13__in:focus-visible + .btn-13__tab {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@supports not (grid-template-columns: subgrid) {
  .btn-13__track {
    grid-template-columns: repeat(4,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .btn-13__tab {
    transition: none;
  }
}
```
