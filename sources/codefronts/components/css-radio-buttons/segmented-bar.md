---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/segmented-bar/"
title: "Segmented Control Bar Radio"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "Tab-style view switching done as a radio group: a flat toolbar of icon+label segments with a crisp underline indicator that slides beneath the active view."
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Segmented Control Bar Radio
Source: https://codefronts.com/components/css-radio-buttons/segmented-bar/

Tab-style view switching done as a radio group: a flat toolbar of icon+label segments with a crisp underline indicator that slides beneath the active view. The pattern behind List/Grid/Board toggles in every modern project-management tool — pure CSS slide included.
## HTML
```html
<div class="crb-15-group">
<section class="crb-15a" aria-label="Segmented control bar radio">
  <fieldset class="crb-15a__group">
    <legend class="crb-15a__legend">Project view</legend>
    <div class="crb-15a__bar">
      <label class="crb-15a__seg"><input class="crb-15a__input" type="radio" name="crb-15a" value="list" checked><svg class="crb-15a__ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/></svg><span class="crb-15a__text">List</span></label>
      <label class="crb-15a__seg"><input class="crb-15a__input" type="radio" name="crb-15a" value="grid"><svg class="crb-15a__ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.5"/></svg><span class="crb-15a__text">Grid</span></label>
      <label class="crb-15a__seg"><input class="crb-15a__input" type="radio" name="crb-15a" value="board"><svg class="crb-15a__ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3.5" y="3.5" width="5" height="17" rx="1.5"/><rect x="11" y="3.5" width="5" height="11" rx="1.5"/><rect x="18.5" y="3.5" width="2" height="7" rx="1"/></svg><span class="crb-15a__text">Board</span></label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-15-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-15-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-15a,
.crb-15a *,
.crb-15a *::before,
.crb-15a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-15a {
  --accent: oklch(0.5 0.19 262);
  --ink: #1c2130;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f7f8fa;
}

.crb-15a__group {
  border: none;
  display: grid;
  justify-items: center;
  gap: 18px;
}

.crb-15a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
  text-align: center;
  margin-bottom: 2px;
}

.crb-15a__bar {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  background: #fff;
  border: 1px solid #e4e6ee;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(25,30,50,.06);
  overflow: hidden;
}

.crb-15a__bar::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 33.333%;
  height: 3px;
  border-radius: 3px 3px 0 0;
  background: var(--accent);
  transition: transform .3s cubic-bezier(.22,1,.36,1);
}

.crb-15a__bar:has(.crb-15a__seg:nth-child(2) .crb-15a__input:checked)::after {
  transform: translateX(100%);
}

.crb-15a__bar:has(.crb-15a__seg:nth-child(3) .crb-15a__input:checked)::after {
  transform: translateX(200%);
}

.crb-15a__seg {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-width: 118px;
  min-height: 48px;
  padding: 0 20px;
  cursor: pointer;
  transition: background .2s;
}

.crb-15a__seg:hover {
  background: #f4f5f9;
}

.crb-15a__seg + .crb-15a__seg {
  border-left: 1px solid #eef0f5;
}

.crb-15a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-15a__ic {
  width: 18px;
  height: 18px;
  color: #8a90a5;
  transition: color .25s;
}

.crb-15a__text {
  font-size: 14px;
  font-weight: 650;
  color: #69708a;
  transition: color .25s;
}

.crb-15a__seg:has(.crb-15a__input:checked) .crb-15a__ic,
.crb-15a__seg:has(.crb-15a__input:checked) .crb-15a__text {
  color: var(--accent);
}

.crb-15a__seg:has(.crb-15a__input:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-15a__bar::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the underline is a ::after sized to one segment, translated 0/100%/200% by :has(nth-child) rules; icons and text recolour from the same state. */
```
