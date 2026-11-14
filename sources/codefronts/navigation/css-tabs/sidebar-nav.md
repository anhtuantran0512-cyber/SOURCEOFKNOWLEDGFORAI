---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/sidebar-nav/"
title: "Sidebar Nav"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Vertical icon-driven nav inspired by hand-built dashboard sidebars."
has_js: "true"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sidebar Nav
Source: https://codefronts.com/navigation/css-tabs/sidebar-nav/

Vertical icon-driven nav inspired by hand-built dashboard sidebars. Dusty olive accent bar slides between rows; the active icon shifts left and a label slides in from behind it.
## HTML
```html
<div class="tt03">
  <nav class="tt03n">
    <button class="tt03b active" data-t>
      <svg class="tt03i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M3 11l9-8 9 8v10a2 2 0 0 1-2 2h-4v-7H9v7H5a2 2 0 0 1-2-2z" />
      </svg>
      <span class="tt03l">Home</span>
    </button>
    <button class="tt03b" data-t>
      <svg class="tt03i" viewBox="0 0 24 24" aria-hidden="true">
        <path d="M2 12h4l3-9 4 18 3-9h6" />
      </svg>
      <span class="tt03l">Activity</span>
    </button>
    <button class="tt03b" data-t>
      <svg class="tt03i" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="8" r="4" />
        <path d="M3 21v-2a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2" />
      </svg>
      <span class="tt03l">People</span>
    </button>
    <button class="tt03b" data-t>
      <svg class="tt03i" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="3" />
        <path
          d="M19 12a7 7 0 0 0-.1-1.2l2-1.6-2-3.4-2.5 1a7 7 0 0 0-2.1-1.2L14 3h-4l-.3 2.6a7 7 0 0 0-2.1 1.2l-2.5-1-2 3.4 2 1.6A7 7 0 0 0 5 12c0 .4 0 .8.1 1.2l-2 1.6 2 3.4 2.5-1a7 7 0 0 0 2.1 1.2L10 21h4l.3-2.6a7 7 0 0 0 2.1-1.2l2.5 1 2-3.4-2-1.6c.1-.4.1-.8.1-1.2z"
        />
      </svg>
      <span class="tt03l">Settings</span>
    </button>
    <span class="tt03acc" aria-hidden="true"> </span>
  </nav>
</div>
```
## CSS
```css
.tt03 {
  background: #e8dac5;
  min-height: 100vh;
  display: flex;
  align-items: stretch;
  padding: 12px 0 12px 12px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  width: 100%;
}

.tt03n {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.tt03b {
  position: relative;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 18px;
  border: 0;
  background: transparent;
  font: 600 13px/1 ui-sans-serif, system-ui;
  color: rgba(58, 46, 30, 0.55);
  cursor: pointer;
  text-align: left;
  transition: color 0.25s, transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), background 0.25s;
}

.tt03b:hover {
  color: rgba(58, 46, 30, 0.85);
  background: rgba(107, 142, 84, 0.08);
}

.tt03i {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
  flex-shrink: 0;
  transition: transform 0.45s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tt03l {
  opacity: 0.7;
  transform: translateX(-4px);
  transition: opacity 0.3s, transform 0.3s cubic-bezier(0.65, 0, 0.35, 1);
}

.tt03b.active {
  color: #4a6a3a;
  transform: translateX(4px);
}

.tt03b.active .tt03i {
  transform: scale(1.12);
}

.tt03b.active .tt03l {
  opacity: 1;
  transform: translateX(0);
}

.tt03acc {
  position: absolute;
  left: -12px;
  top: 0;
  width: 4px;
  height: 0;
  background: #6b8e54;
  border-radius: 0 4px 4px 0;
  transition: top 0.45s cubic-bezier(0.65, 0, 0.35, 1), height 0.45s cubic-bezier(0.65, 0, 0.35, 1);
}
```

## JavaScript
```js
/* Sidebar Nav — toggle .active and slide vertical accent bar.
   Re-positions the accent bar on viewport resize. */
(function () {
  var nav = document.querySelector(".tt03n");
  if (!nav) return;
  var btns = nav.querySelectorAll("[data-t]");
  var acc = nav.querySelector(".tt03acc");
  var current = null;

  function reposition() {
    if (!current || !acc) return;
    acc.style.top = current.offsetTop + "px";
    acc.style.height = current.offsetHeight + "px";
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
