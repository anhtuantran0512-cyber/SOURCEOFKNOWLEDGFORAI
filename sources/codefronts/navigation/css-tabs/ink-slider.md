---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/ink-slider/"
title: "Ink Slider"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Solid ink-violet bar slides horizontally beneath the active tab."
has_js: "true"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ink Slider
Source: https://codefronts.com/navigation/css-tabs/ink-slider/

Solid ink-violet bar slides horizontally beneath the active tab. JS measures offsetLeft + offsetWidth so the bar matches each tab's exact width — no fixed-width assumption — and re-aligns on viewport resize.
## HTML
```html
<div class="tt21">
  <nav class="tt21n">
    <span class="tt21bar" aria-hidden="true"></span>
    <button class="tt21b active" data-t>Overview</button>
    <button class="tt21b" data-t>Pricing</button>
    <button class="tt21b" data-t>Reviews</button>
    <button class="tt21b" data-t>Support</button>
  </nav>
</div>
```
## CSS
```css
.tt21 {
  background: #faf8f3;
  padding: 32px 18px 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
}

.tt21n {
  position: relative;
  display: flex;
  border-bottom: 1px solid rgba(35, 28, 72, 0.12);
  min-width: 0;
}

.tt21bar {
  position: absolute;
  bottom: -1px;
  left: 0;
  height: 3px;
  width: 0;
  background: #231c48;
  border-radius: 2px 2px 0 0;
  transition: left 0.45s cubic-bezier(0.65, 0, 0.35, 1), width 0.45s cubic-bezier(0.65, 0, 0.35, 1);
  pointer-events: none;
}

.tt21b {
  flex: 1;
  min-width: 0;
  padding: 12px 14px 14px;
  border: 0;
  background: transparent;
  font: 600 13px/1 ui-sans-serif, system-ui;
  color: rgba(35, 28, 72, 0.55);
  cursor: pointer;
  transition: color 0.25s;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tt21b:hover {
  color: rgba(35, 28, 72, 0.85);
}

.tt21b.active {
  color: #231c48;
}

.tt21b:focus-visible {
  outline: 2px solid #231c48;
  outline-offset: -2px;
}

@media (prefers-reduced-motion: reduce) {
  .tt21bar {
    transition: none;
  }
}
```

## JavaScript
```js
/* Ink Slider — toggle .active and slide the ink bar to the active tab.
   Re-positions on viewport resize so the bar stays locked to its button. */
(function () {
  var nav = document.querySelector(".tt21n");
  if (!nav) return;
  var btns = nav.querySelectorAll("[data-t]");
  var bar = nav.querySelector(".tt21bar");
  var current = null;

  function reposition() {
    if (!current || !bar) return;
    bar.style.left = current.offsetLeft + "px";
    bar.style.width = current.offsetWidth + "px";
  }
  function activate(btn) {
    current = btn;
    btns.forEach(function (b) {
      b.classList.toggle("active", b === btn);
    });
    reposition();
  }
  btns.forEach(function (b) {
    b.addEventListener("click", function () {
      activate(b);
    });
  });
  window.addEventListener("resize", reposition);
  var initial = nav.querySelector("[data-t].active") || btns[0];
  if (initial) activate(initial);
})();
```
