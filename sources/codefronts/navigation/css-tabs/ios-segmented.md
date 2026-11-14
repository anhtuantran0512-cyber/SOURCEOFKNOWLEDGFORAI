---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/ios-segmented/"
title: "iOS Segmented"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Apple-style segmented control: gray track, white pill that physically slides between segments."
has_js: "true"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: iOS Segmented
Source: https://codefronts.com/navigation/css-tabs/ios-segmented/

Apple-style segmented control: gray track, white pill that physically slides between segments. JS measures positions live; resize-listener keeps the pill aligned at any width.
## HTML
```html
<div class="tt26">
  <nav class="tt26n">
    <span class="tt26pill" aria-hidden="true"></span>
    <button class="tt26b active" data-t>Day</button>
    <button class="tt26b" data-t>Week</button>
    <button class="tt26b" data-t>Month</button>
  </nav>
</div>
```
## CSS
```css
.tt26 {
  background: #f2f2f7;
  padding: 32px 24px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tt26n {
  position: relative;
  display: flex;
  background: rgba(120, 120, 128, 0.16);
  border-radius: 9px;
  padding: 2px;
  width: 100%;
  max-width: 380px;
  min-width: 0;
}

.tt26pill {
  position: absolute;
  top: 2px;
  left: 2px;
  height: calc(100% - 4px);
  background: #fff;
  border-radius: 7px;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.06);
  transition: left 0.34s cubic-bezier(0.4, 0, 0.2, 1), width 0.34s cubic-bezier(0.4, 0, 0.2, 1);
  pointer-events: none;
}

.tt26b {
  flex: 1;
  min-width: 0;
  padding: 8px 14px;
  border: 0;
  background: transparent;
  font: 600 13px/1 inherit;
  color: #1c1c1e;
  cursor: pointer;
  position: relative;
  z-index: 1;
  transition: color 0.2s;
  white-space: nowrap;
}

.tt26b:focus-visible {
  outline: 2px solid #007aff;
  outline-offset: 2px;
  border-radius: 7px;
}

@media (prefers-reduced-motion: reduce) {
  .tt26pill {
    transition: none;
  }
}
```

## JavaScript
```js
/* iOS Segmented — toggle .active and slide white pill between tabs.
   Re-positions on viewport resize so the pill stays locked to its segment. */
(function () {
  var nav = document.querySelector(".tt26n");
  if (!nav) return;
  var btns = nav.querySelectorAll("[data-t]");
  var pill = nav.querySelector(".tt26pill");
  var current = null;

  function reposition() {
    if (!current || !pill) return;
    pill.style.left = current.offsetLeft + "px";
    pill.style.width = current.offsetWidth + "px";
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
