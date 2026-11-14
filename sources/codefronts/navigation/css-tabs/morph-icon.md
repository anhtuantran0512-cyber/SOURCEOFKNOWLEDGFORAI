---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/morph-icon/"
title: "Morph Icon"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Compact icon-only tabs that expand on activation: the label morphs in via a max-width transition, smoothly widening the active tab inline."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Morph Icon
Source: https://codefronts.com/navigation/css-tabs/morph-icon/

Compact icon-only tabs that expand on activation: the label morphs in via a max-width transition, smoothly widening the active tab inline. Pure CSS, no positional JS.
## HTML
```html
<div class="tt30">
  <nav class="tt30n">
    <input type="radio" name="tt30" id="tt30-r1" checked />
    <label class="tt30b" for="tt30-r1">
      <svg class="tt30i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M3 12l9-9 9 9M5 10v10h14V10" />
      </svg>
      <span class="tt30l">Home</span>
    </label>
    <input type="radio" name="tt30" id="tt30-r2" />
    <label class="tt30b" for="tt30-r2">
      <svg class="tt30i" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="11" cy="11" r="7" />
        <path d="M21 21l-5-5" />
      </svg>
      <span class="tt30l">Search</span>
    </label>
    <input type="radio" name="tt30" id="tt30-r3" />
    <label class="tt30b" for="tt30-r3">
      <svg class="tt30i" viewBox="0 0 24 24" aria-hidden="true">
        <path
          d="M3 8h18M3 14h18M5 4h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"
        />
      </svg>
      <span class="tt30l">Inbox</span>
    </label>
    <input type="radio" name="tt30" id="tt30-r4" />
    <label class="tt30b" for="tt30-r4">
      <svg class="tt30i" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="8" r="4" />
        <path d="M3 21v-2a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2" />
      </svg>
      <span class="tt30l">Profile</span>
    </label>
  </nav>
</div>
```
## CSS
```css
.tt30 {
  background: #fdf6e9;
  padding: 32px 18px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tt30n {
  display: flex;
  gap: 6px;
  background: #fff;
  border-radius: 999px;
  padding: 6px;
  box-shadow: 0 4px 14px rgba(212, 67, 127, 0.12);
  min-width: 0;
}

.tt30n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt30b {
  display: flex;
  align-items: center;
  gap: 0;
  padding: 10px 12px;
  border-radius: 999px;
  cursor: pointer;
  color: #94748a;
  transition: background 0.3s, color 0.3s, gap 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  white-space: nowrap;
  overflow: hidden;
}

.tt30b:hover {
  color: #d4437f;
}

.tt30i {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.tt30l {
  font: 700 12px/1 ui-sans-serif, system-ui;
  max-width: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-width 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s;
}

.tt30n input:checked + .tt30b {
  background: #d4437f;
  color: #fff;
  gap: 8px;
}

.tt30n input:checked + .tt30b .tt30l {
  max-width: 120px;
  opacity: 1;
}

.tt30n input:focus-visible + .tt30b {
  outline: 2px dashed #d4437f;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .tt30b,
    .tt30l {
    transition: none;
  }
}
```
