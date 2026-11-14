---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/pill-nav/"
title: "Pill Nav"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Mobile-style bottom-nav with hot-pink active pill that grows around the active icon and label."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pill Nav
Source: https://codefronts.com/navigation/css-tabs/pill-nav/

Mobile-style bottom-nav with hot-pink active pill that grows around the active icon and label. Inactive items show only icons; activation adds the label inside the pill.
## HTML
```html
<div class="tt13">
  <nav class="tt13n">
    <input type="radio" name="tt13" id="tt13-r1" checked />
    <label class="tt13b" for="tt13-r1">
      <svg class="tt13i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M3 11l9-8 9 8v10a2 2 0 0 1-2 2h-4v-7H9v7H5a2 2 0 0 1-2-2z" />
      </svg>
      <span class="tt13l">Home</span>
    </label>
    <input type="radio" name="tt13" id="tt13-r2" />
    <label class="tt13b" for="tt13-r2">
      <svg class="tt13i" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="11" cy="11" r="7" />
        <line x1="21" y1="21" x2="16" y2="16" />
      </svg>
      <span class="tt13l">Search</span>
    </label>
    <input type="radio" name="tt13" id="tt13-r3" />
    <label class="tt13b" for="tt13-r3">
      <svg class="tt13i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M20 8h-3V5a3 3 0 0 0-3-3h-4a3 3 0 0 0-3 3v3H4l1 12h14z" />
      </svg>
      <span class="tt13l">Saved</span>
    </label>
    <input type="radio" name="tt13" id="tt13-r4" />
    <label class="tt13b" for="tt13-r4">
      <svg class="tt13i" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="8" r="4" />
        <path d="M3 21v-2a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2" />
      </svg>
      <span class="tt13l">Profile</span>
    </label>
  </nav>
</div>
```
## CSS
```css
.tt13 {
  background: #1f2326;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 28px 22px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  width: 100%;
}

.tt13n {
  flex: 1;
  display: flex;
  gap: 6px;
  padding: 6px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 999px;
}

.tt13n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt13b {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 14px;
  border: 0;
  background: transparent;
  font: 700 12px/1 ui-sans-serif, system-ui;
  letter-spacing: 0.04em;
  color: rgba(232, 226, 208, 0.55);
  cursor: pointer;
  border-radius: 999px;
  flex: 1;
  transition: flex 0.45s cubic-bezier(0.34, 1.4, 0.5, 1), background 0.25s, color 0.25s;
}

.tt13b:hover {
  color: rgba(232, 226, 208, 0.85);
}

.tt13i {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform 0.4s cubic-bezier(0.34, 1.4, 0.5, 1);
}

.tt13l {
  max-width: 0;
  white-space: nowrap;
  overflow: hidden;
  transition: max-width 0.45s cubic-bezier(0.65, 0, 0.35, 1) 0.05s;
}

.tt13n input:checked + .tt13b {
  background: #ec4899;
  color: #1a1a1a;
  flex: 2.4;
}

.tt13n input:checked + .tt13b .tt13i {
  transform: scale(1.1);
}

.tt13n input:checked + .tt13b .tt13l {
  max-width: 120px;
}
```
