---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/sliding-pill/"
title: "Sliding Pill"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Icon + label tabs on cream stock. A solid indigo pill is the indicator; it physically slides between tabs on click, with the active label inverting to cream."
has_js: "true"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliding Pill
Source: https://codefronts.com/navigation/css-tabs/sliding-pill/

Icon + label tabs on cream stock. A solid indigo pill is the indicator; it physically slides between tabs on click, with the active label inverting to cream.
## HTML
```html
<div class="tt17">
  <nav class="tt17n">
    <span class="tt17pill" aria-hidden="true"> </span>
    <button class="tt17b active" data-t>
      <svg class="tt17i" viewBox="0 0 24 24" aria-hidden="true">
        <rect x="3" y="3" width="7" height="7" />
        <rect x="14" y="3" width="7" height="7" />
        <rect x="3" y="14" width="7" height="7" />
        <rect x="14" y="14" width="7" height="7" />
      </svg>
      <span class="tt17l">Grid</span>
    </button>
    <button class="tt17b" data-t>
      <svg class="tt17i" viewBox="0 0 24 24" aria-hidden="true">
        <line x1="8" y1="6" x2="21" y2="6" />
        <line x1="8" y1="12" x2="21" y2="12" />
        <line x1="8" y1="18" x2="21" y2="18" />
        <circle cx="4" cy="6" r="1" />
        <circle cx="4" cy="12" r="1" />
        <circle cx="4" cy="18" r="1" />
      </svg>
      <span class="tt17l">List</span>
    </button>
    <button class="tt17b" data-t>
      <svg class="tt17i" viewBox="0 0 24 24" aria-hidden="true">
        <rect x="3" y="4" width="18" height="6" rx="1" />
        <rect x="3" y="14" width="18" height="6" rx="1" />
      </svg>
      <span class="tt17l">Cards</span>
    </button>
  </nav>
</div>
```
## CSS
```css
.tt17 {
  background: #f4f3ee;
  padding: 28px 22px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  width: 100%;
}

.tt17n {
  position: relative;
  display: flex;
  gap: 0;
  padding: 6px;
  background: rgba(59, 58, 140, 0.06);
  border-radius: 999px;
  flex: 1;
}

.tt17pill {
  position: absolute;
  top: 6px;
  left: 6px;
  height: calc(100% - 12px);
  width: 0;
  background: #3b3a8c;
  border-radius: 999px;
  transition: left 0.5s cubic-bezier(0.65, 0, 0.35, 1), width 0.5s cubic-bezier(0.65, 0, 0.35, 1);
  z-index: 0;
}

.tt17b {
  position: relative;
  z-index: 1;
  flex: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 11px 14px;
  border: 0;
  background: transparent;
  font: 600 13px/1 ui-sans-serif, system-ui;
  letter-spacing: 0.02em;
  color: rgba(59, 58, 140, 0.65);
  cursor: pointer;
  transition: color 0.3s 0.05s;
}

.tt17b:hover {
  color: rgba(59, 58, 140, 0.95);
}

.tt17b.active {
  color: #f4f3ee;
}

.tt17i {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}
```

## JavaScript
```js
/* Sliding Pill — toggle .active and slide solid pill between tabs.
   Re-positions the pill on viewport resize. */
(function () {
  var nav = document.querySelector(".tt17n");
  if (!nav) return;
  var btns = nav.querySelectorAll("[data-t]");
  var pill = nav.querySelector(".tt17pill");
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
