---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/typewriter/"
title: "Typewriter"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Activating a tab triggers a typewriter animation on the panel: text reveals via max-width steps animation, with a blinking cursor at the end."
has_js: "false"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Typewriter
Source: https://codefronts.com/navigation/css-tabs/typewriter/

Activating a tab triggers a typewriter animation on the panel: text reveals via max-width steps animation, with a blinking cursor at the end. Pure CSS via radio inputs and steps() timing.
## HTML
```html
<div class="tt31">
  <nav class="tt31n">
    <input type="radio" name="tt31" id="tt31-r1" checked />
    <label class="tt31b" for="tt31-r1">Greet</label>
    <input type="radio" name="tt31" id="tt31-r2" />
    <label class="tt31b" for="tt31-r2">Status</label>
    <input type="radio" name="tt31" id="tt31-r3" />
    <label class="tt31b" for="tt31-r3">Goodbye</label>
  </nav>
  <div class="tt31body">
    <div class="tt31p"><span class="tt31type">Hello, friend.</span></div>
    <div class="tt31p"><span class="tt31type">Systems nominal.</span></div>
    <div class="tt31p"><span class="tt31type">See you tomorrow.</span></div>
  </div>
</div>
```
## CSS
```css
.tt31 {
  background: #1a1625;
  padding: 22px 22px;
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.tt31n {
  display: flex;
  gap: 4px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  margin-bottom: 18px;
  min-width: 0;
}

.tt31n input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.tt31b {
  flex: 1;
  min-width: 0;
  padding: 9px 12px;
  font: 600 11px/1 ui-monospace, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.45);
  cursor: pointer;
  text-align: center;
  border-bottom: 2px solid transparent;
  margin-bottom: -1px;
  transition: color 0.2s, border-color 0.2s;
  white-space: nowrap;
}

.tt31b:hover {
  color: rgba(255, 255, 255, 0.85);
}

.tt31n input:checked + .tt31b {
  color: #fbbf24;
  border-bottom-color: #fbbf24;
}

.tt31n input:focus-visible + .tt31b {
  outline: 1px dashed #fbbf24;
  outline-offset: -3px;
}

.tt31body {
  padding: 6px 0;
}

.tt31p {
  display: none;
}

.tt31:has(#tt31-r1:checked) .tt31p:nth-of-type(1),
.tt31:has(#tt31-r2:checked) .tt31p:nth-of-type(2),
.tt31:has(#tt31-r3:checked) .tt31p:nth-of-type(3) {
  display: block;
}

.tt31type {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  font: 14px/1.6 ui-monospace, monospace;
  color: #fbbf24;
  border-right: 2px solid #fbbf24;
  width: 0;
  animation: tt31-type 1.4s steps(20) forwards, tt31-blink 0.8s step-end infinite 1.4s;
}

@keyframes tt31-type {
  to {
    width: 100%;
  }
}

@keyframes tt31-blink {
  50% {
    border-right-color: transparent;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tt31type {
    animation: none;
    width: 100%;
    border-right-color: transparent;
  }
}
```
