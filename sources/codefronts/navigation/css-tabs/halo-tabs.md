---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/halo-tabs/"
title: "Halo Tabs"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Mobile-style nav-bar tabs in a soft white pill."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Halo Tabs
Source: https://codefronts.com/navigation/css-tabs/halo-tabs/

Mobile-style nav-bar tabs in a soft white pill. Inactive icons are line-only grey. Activating a tab tints the icon mint, blooms a soft pink halo behind it, and slides the label in to the right of the icon — no underline, just the color shift and the label appearance.
## HTML
```html
<div class="tt04">
  <nav class="tt04n">
    <input type="radio" name="tt04" id="tt04-r1" checked />
    <label class="tt04b" for="tt04-r1">
      <span class="tt04halo" aria-hidden="true"> </span>
      <svg class="tt04i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M3 11l9-8 9 8v10a2 2 0 0 1-2 2h-4v-7H9v7H5a2 2 0 0 1-2-2z" />
      </svg>
      <span class="tt04l">Home</span>
    </label>
    <input type="radio" name="tt04" id="tt04-r2" />
    <label class="tt04b" for="tt04-r2">
      <span class="tt04halo" aria-hidden="true"> </span>
      <svg class="tt04i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M5 8l7-5 7 5v3H5z" />
        <path d="M9 11h6v8H9z" />
        <path d="M3 19h18" />
      </svg>
      <span class="tt04l">Strategy</span>
    </label>
    <input type="radio" name="tt04" id="tt04-r3" />
    <label class="tt04b" for="tt04-r3">
      <span class="tt04halo" aria-hidden="true"> </span>
      <svg class="tt04i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M7 3h10v4l-3 5 3 5v4H7v-4l3-5-3-5z" />
        <line x1="9" y1="3" x2="9" y2="3" />
      </svg>
      <span class="tt04l">Period</span>
    </label>
    <input type="radio" name="tt04" id="tt04-r4" />
    <label class="tt04b" for="tt04-r4">
      <span class="tt04halo" aria-hidden="true"> </span>
      <svg class="tt04i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M12 2L4 6v6c0 5 3.5 9.5 8 10 4.5-.5 8-5 8-10V6z" />
        <polyline points="9 12 11 14 15 10" />
      </svg>
      <span class="tt04l">Security</span>
    </label>
    <input type="radio" name="tt04" id="tt04-r5" />
    <label class="tt04b" for="tt04-r5">
      <span class="tt04halo" aria-hidden="true"> </span>
      <svg class="tt04i" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="3" />
        <path
          d="M19 12a7 7 0 0 0-.1-1.2l2-1.6-2-3.4-2.5 1a7 7 0 0 0-2.1-1.2L14 3h-4l-.3 2.6a7 7 0 0 0-2.1 1.2l-2.5-1-2 3.4 2 1.6A7 7 0 0 0 5 12c0 .4 0 .8.1 1.2l-2 1.6 2 3.4 2.5-1a7 7 0 0 0 2.1 1.2L10 21h4l.3-2.6a7 7 0 0 0 2.1-1.2l2.5 1 2-3.4-2-1.6c.1-.4.1-.8.1-1.2z"
        />
      </svg>
      <span class="tt04l">Settings</span>
    </label>
  </nav>
</div>
```
## CSS
```css
.tt04 {
  background: #f0f1f1;
  padding: 0;
  font-family: "Nunito", ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.tt04n {
  position: relative;
  display: flex;
  gap: 4px;
  padding: 18px 22px;
  background: #fefefe;
  border-radius: 999px;
  margin: 14px;
  flex: 1;
  max-width: 480px;
  box-shadow: 0 6px 22px -8px rgba(0, 0, 0, 0.12);
  font-size: 1em;
}

.tt04n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt04b {
  position: relative;
  flex: 1 1 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 6px 4px;
  border: 0;
  background: transparent;
  cursor: pointer;
  overflow: hidden;
  color: #d5dadd;
  transition: flex 0.45s cubic-bezier(0.4, 0, 0.2, 1), color 0.3s;
}

.tt04b:hover {
  color: #9aa0a4;
}
/* Soft pink halo behind the active icon, top-left offset like the reference */

.tt04halo {
  position: absolute;
  top: 14%;
  left: 22%;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #fde4ec;
  transform: scale(0);
  transform-origin: center;
  transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 0;
  pointer-events: none;
}

.tt04i {
  width: 26px;
  height: 26px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.6;
  stroke-linecap: round;
  stroke-linejoin: round;
  position: relative;
  z-index: 2;
  flex-shrink: 0;
  transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1);
}

.tt04l {
  position: relative;
  z-index: 2;
  font: 800 15px/1 "Nunito", ui-sans-serif, system-ui;
  letter-spacing: 0.01em;
  white-space: nowrap;
  color: #2dd4bf;
  /* Hidden until active — slides in to the right of the icon */
  max-width: 0;
  overflow: hidden;
  opacity: 0;
  transform: translateX(-8px);
  transition: max-width 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s 0.1s, transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.tt04n input:checked + .tt04b {
  flex: 2.6;
  color: #2dd4bf;
}

.tt04n input:checked + .tt04b .tt04halo {
  transform: scale(1);
}

.tt04n input:checked + .tt04b .tt04l {
  max-width: 200px;
  opacity: 1;
  transform: translateX(0);
}

@media (prefers-reduced-motion: reduce) {
  .tt04halo,
    .tt04l,
    .tt04b {
    transition: none;
  }
}
```
