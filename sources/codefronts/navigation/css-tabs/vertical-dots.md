---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/vertical-dots/"
title: "Vertical Dots"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Sidebar nav with a connecting timeline rule."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Dots
Source: https://codefronts.com/navigation/css-tabs/vertical-dots/

Sidebar nav with a connecting timeline rule. The active item's dot fills in solid teal with a soft outer glow; inactive dots stay hollow. Vertical layout. Pure CSS.
## HTML
```html
<div class="tt28">
  <nav class="tt28n">
    <input type="radio" name="tt28" id="tt28-r1" checked />
    <label class="tt28b" for="tt28-r1"><span class="tt28dot"></span>Profile</label>
    <input type="radio" name="tt28" id="tt28-r2" />
    <label class="tt28b" for="tt28-r2"><span class="tt28dot"></span>Account</label>
    <input type="radio" name="tt28" id="tt28-r3" />
    <label class="tt28b" for="tt28-r3"><span class="tt28dot"></span>Billing</label>
    <input type="radio" name="tt28" id="tt28-r4" />
    <label class="tt28b" for="tt28-r4"><span class="tt28dot"></span>Logs</label>
  </nav>
</div>
```
## CSS
```css
.tt28 {
  background: #0d1117;
  padding: 18px 22px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}
/* nav padding-left = 30px → that x defines a "rail column" centered at x=15.
   Both the timeline rule and the active dot center on x=15 so they sit on
   the same vertical axis regardless of dot size or label padding. */

.tt28n {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding-left: 30px;
  min-width: 0;
}

.tt28n::before {
  content: "";
  position: absolute;
  left: 14px;
  top: 14px;
  bottom: 14px;
  width: 2px;
  background: rgba(56, 189, 248, 0.18);
  border-radius: 1px;
}

.tt28n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt28b {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 6px 8px;
  font: 600 12px/1 ui-sans-serif, system-ui;
  color: rgba(255, 255, 255, 0.55);
  cursor: pointer;
  border-radius: 4px;
  transition: color 0.22s, background 0.22s;
  white-space: nowrap;
}

.tt28dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 1.5px solid rgba(56, 189, 248, 0.45);
  background: #0d1117;
  flex-shrink: 0;
  /* margin-left = -(button padding-left + dot half-width - line center)
       = -(8 + 6 - 15) = -(-1) ... actually: button starts at nav-padding-left
       (30px). Dot needs left edge at x=9 so center sits at x=15 (line center).
       Button content starts at x=38 (30 + 8 padding). To put dot's left edge
       at x=9, margin-left = 9 - 38 = -29px. */
  margin-left: -29px;
  transition: background 0.25s, border-color 0.25s, box-shadow 0.3s;
  position: relative;
  z-index: 1;
}

.tt28b:hover {
  color: rgba(255, 255, 255, 0.85);
  background: rgba(56, 189, 248, 0.06);
}

.tt28n input:checked + .tt28b {
  color: #7dd3fc;
}

.tt28n input:checked + .tt28b .tt28dot {
  background: #38bdf8;
  border-color: #38bdf8;
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.55);
}

.tt28n input:focus-visible + .tt28b {
  outline: 1px dashed #38bdf8;
  outline-offset: 3px;
}
```
