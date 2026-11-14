---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/riso-misregistration/"
title: "Riso Misregistration"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Two-color riso print on charcoal stock."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Riso Misregistration
Source: https://codefronts.com/navigation/css-tabs/riso-misregistration/

Two-color riso print on charcoal stock. Active tab is a solid orange block with a cyan plate misregistered 4px below-left, like a zine pulled with the cyan plate slightly off the orange. No swashes, no icons; just two color plates and a typographic punch.
## HTML
```html
<div class="tt14">
  <nav class="tt14n">
    <input type="radio" name="tt14" id="tt14-r1" checked />
    <label class="tt14b" for="tt14-r1">
      <span class="tt14plate" aria-hidden="true"> </span>
      <span class="tt14lbl">Issue 01</span>
    </label>
    <input type="radio" name="tt14" id="tt14-r2" />
    <label class="tt14b" for="tt14-r2">
      <span class="tt14plate" aria-hidden="true"> </span>
      <span class="tt14lbl">Issue 02</span>
    </label>
    <input type="radio" name="tt14" id="tt14-r3" />
    <label class="tt14b" for="tt14-r3">
      <span class="tt14plate" aria-hidden="true"> </span>
      <span class="tt14lbl">Issue 03</span>
    </label>
    <input type="radio" name="tt14" id="tt14-r4" />
    <label class="tt14b" for="tt14-r4">
      <span class="tt14plate" aria-hidden="true"> </span>
      <span class="tt14lbl">Issue 04</span>
    </label>
  </nav>
</div>
```
## CSS
```css
.tt14 {
  background: #0e0f12;
  padding: 28px 22px;
  font-family: ui-monospace, monospace;
  min-height: 100vh;
  display: flex;
  align-items: center;
  width: 100%;
}

.tt14n {
  display: flex;
  gap: 12px;
  flex: 1;
}

.tt14n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt14b {
  position: relative;
  flex: 1;
  border: 0;
  background: transparent;
  padding: 18px 16px;
  font: 800 12px/1 ui-monospace, monospace;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: rgba(232, 226, 208, 0.55);
  cursor: pointer;
  isolation: isolate;
  transition: color 0.2s;
}

.tt14b:hover {
  color: rgba(232, 226, 208, 0.92);
}

.tt14n input:checked + .tt14b {
  color: #fdf6e9;
  text-shadow: 0 1px 0 rgba(0, 0, 0, 0.35);
}

.tt14plate {
  position: absolute;
  inset: 0;
  background: #ff5e3a;
  z-index: -1;
  opacity: 0;
  transition: opacity 0.05s steps(1, end);
}

.tt14plate::before {
  content: "";
  position: absolute;
  inset: 0;
  background: #00a8c8;
  transform: translate(-4px, 4px);
  mix-blend-mode: multiply;
  opacity: 0;
}

.tt14n input:checked + .tt14b .tt14plate {
  opacity: 1;
}

.tt14n input:checked + .tt14b .tt14plate::before {
  opacity: 0.92;
  animation: tt14-plate-shift 0.32s cubic-bezier(0.65, 0, 0.35, 1);
}

@keyframes tt14-plate-shift {
  0% {
    transform: translate(0, 0);
    opacity: 0;
  }

  55% {
    transform: translate(-7px, 7px);
    opacity: 0.92;
  }

  100% {
    transform: translate(-4px, 4px);
    opacity: 0.92;
  }
}

.tt14lbl {
  position: relative;
  z-index: 1;
}

@media (prefers-reduced-motion: reduce) {
  .tt14n input:checked + .tt14b .tt14plate::before {
    animation: none;
  }
}
```
