---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/velvet-ribbon/"
title: "Velvet Ribbon"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Icon nav on warm-linen stock with a velvet aubergine ribbon trimmed in gilt."
has_js: "true"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Velvet Ribbon
Source: https://codefronts.com/navigation/css-tabs/velvet-ribbon/

Icon nav on warm-linen stock with a velvet aubergine ribbon trimmed in gilt. The ribbon hangs down from the top rail directly above the active icon — measured live so it stays perfectly aligned at any stage width. Jewel-toned, club-bookplate atmosphere.
## HTML
```html
<div class="tt19">
  <nav class="tt19n">
    <span class="tt19rail" aria-hidden="true"> </span>
    <span class="tt19ribbon" aria-hidden="true"> </span>
    <button class="tt19b active" data-t>
      <svg class="tt19i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M3 11l9-8 9 8v10a2 2 0 0 1-2 2h-4v-7H9v7H5a2 2 0 0 1-2-2z" />
      </svg>
      <span class="tt19l">Home</span>
    </button>
    <button class="tt19b" data-t>
      <svg class="tt19i" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="11" cy="11" r="7" />
        <line x1="21" y1="21" x2="16" y2="16" />
      </svg>
      <span class="tt19l">Find</span>
    </button>
    <button class="tt19b" data-t>
      <svg class="tt19i" viewBox="0 0 24 24" aria-hidden="true">
        <path
          d="M9 11h.01M15 11h.01M9.5 15a3.5 3.5 0 0 0 5 0M3 12a9 9 0 1 1 18 0 9 9 0 0 1-18 0z"
        />
      </svg>
      <span class="tt19l">Help</span>
    </button>
    <button class="tt19b" data-t>
      <svg class="tt19i" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="8" r="4" />
        <path d="M3 21v-2a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2" />
      </svg>
      <span class="tt19l">Me</span>
    </button>
  </nav>
</div>
```
## CSS
```css
.tt19 {
  background: #f5efe0;
  padding: 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  width: 100%;
  box-sizing: border-box;
}

.tt19n {
  position: relative;
  flex: 1;
  display: flex;
  padding: 28px 12px 24px;
  box-sizing: border-box;
  min-width: 0;
}
/* Top rail running edge-to-edge — the "shelf" the ribbon hangs from */

.tt19rail {
  position: absolute;
  top: 28px;
  left: 0;
  right: 0;
  height: 3px;
  background: #3d1e4a;
  pointer-events: none;
}
/* The ribbon — JS positions it horizontally to track the active button.
   It hangs from the top rail and overlaps the icon column behind it.
   Height is sized so icon + label both sit comfortably inside it with
   breathing room above the triangular tail. */

.tt19ribbon {
  position: absolute;
  top: 28px;
  width: 56px;
  height: 84px;
  background: #3d1e4a;
  clip-path: polygon(0 0, 100% 0, 100% calc(100% - 10px), 50% 100%, 0 calc(100% - 10px));
  filter: drop-shadow(0 4px 8px rgba(61, 30, 74, 0.4));
  pointer-events: none;
  transition: left 0.5s cubic-bezier(0.65, 0, 0.35, 1);
}
/* Single gilt hem stripe across the ribbon, just below the label.
   Echoes the aubergine rail above and reads as a bookbinder's gilt edge. */

.tt19ribbon::before {
  content: "";
  position: absolute;
  left: 8px;
  right: 8px;
  bottom: 14px;
  height: 1.5px;
  background: #e6c149;
  z-index: 2;
}

.tt19b {
  position: relative;
  z-index: 1;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 14px 4px 12px;
  min-width: 0;
  border: 0;
  background: transparent;
  font: 700 10px/1 ui-sans-serif, system-ui;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(61, 30, 74, 0.5);
  cursor: pointer;
  transition: color 0.3s;
}

.tt19b:hover {
  color: rgba(61, 30, 74, 0.85);
}

.tt19i {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), stroke 0.3s;
}

.tt19l {
  font-weight: 700;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
}
/* Active state: icon + label go cream on aubergine (both sit inside ribbon
   body, with the gilt hem stripe between the label and the triangular tail). */

.tt19b.active {
  color: #f5efe0;
}

.tt19b.active .tt19i {
  stroke: #f5efe0;
}

@media (prefers-reduced-motion: reduce) {
  .tt19ribbon {
    transition: none;
  }
}
```

## JavaScript
```js
/* Velvet Ribbon — toggle .active and slide ribbon centered above active icon.
   Re-measures on viewport resize so the ribbon stays aligned at any width. */
(function () {
  var nav = document.querySelector(".tt19n");
  if (!nav) return;
  var btns = nav.querySelectorAll("[data-t]");
  var ribbon = nav.querySelector(".tt19ribbon");
  var current = null;

  function position(btn) {
    if (!ribbon || !btn) return;
    var w = ribbon.offsetWidth || 56;
    ribbon.style.left = btn.offsetLeft + btn.offsetWidth / 2 - w / 2 + "px";
  }
  function activate(btn) {
    current = btn;
    btns.forEach(function (b) {
      b.classList.toggle("active", b === btn);
    });
    position(btn);
  }
  btns.forEach(function (b) {
    b.addEventListener("click", function () {
      activate(b);
    });
  });
  window.addEventListener("resize", function () {
    position(current);
  });
  var initial = nav.querySelector("[data-t].active") || btns[0];
  if (initial) activate(initial);
})();
```
