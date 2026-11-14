---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/bracket-marks/"
title: "Bracket Marks"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "The active tab is framed by typographic brackets — `[` on the left, `]` on the right — that physically slide between tabs."
has_js: "true"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bracket Marks
Source: https://codefronts.com/navigation/css-tabs/bracket-marks/

The active tab is framed by typographic brackets — `[` on the left, `]` on the right — that physically slide between tabs. A single shared pair of pseudo-elements does the work.
## HTML
```html
<div class="tt09">
  <nav class="tt09n" data-tt09>
    <button class="tt09b active" data-t>One</button>
    <button class="tt09b" data-t>Two</button>
    <button class="tt09b" data-t>Three</button>
    <span class="tt09bL">[</span>
    <span class="tt09bR">]</span>
  </nav>
  <div class="tt09p active" data-p>The first marker.</div>
  <div class="tt09p" data-p>The second marker.</div>
  <div class="tt09p" data-p>The third marker.</div>
</div>
```
## CSS
```css
.tt09 {
  min-height: 100vh;
  background: #25222e;
  padding: 24px 22px 18px;
  font-family: ui-serif, Georgia, serif;
  width: 100%;
}

.tt09n {
  position: relative;
  display: flex;
  gap: 18px;
  justify-content: center;
}

.tt09b {
  border: 0;
  background: transparent;
  padding: 6px 8px;
  font: 600 16px/1 ui-serif, Georgia, serif;
  color: rgba(232, 226, 208, 0.5);
  cursor: pointer;
  transition: color 0.3s;
}

.tt09b:hover {
  color: rgba(232, 226, 208, 0.85);
}

.tt09b.active {
  color: #e8e2d0;
}

.tt09bL,
.tt09bR {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  font: 200 36px/1 ui-serif, Georgia, serif;
  color: #dc1e3a;
  pointer-events: none;
  transition: left 0.5s cubic-bezier(0.65, 0, 0.35, 1);
}

.tt09bL {
  left: 0;
}

.tt09bR {
  left: 0;
}

.tt09p {
  display: none;
  padding-top: 16px;
  font: italic 12px/1.6 ui-serif, Georgia, serif;
  color: rgba(232, 226, 208, 0.7);
  text-align: center;
}

.tt09p.active {
  display: block;
}
```

## JavaScript
```js
/* Bracket Marks — toggle .active and slide [ ] frame around active button.
   Re-positions the brackets on viewport resize. */
(function () {
  var nav = document.querySelector(".tt09n");
  if (!nav) return;
  var btns = nav.querySelectorAll("[data-t]");
  var bL = nav.querySelector(".tt09bL");
  var bR = nav.querySelector(".tt09bR");
  var pnls = document.querySelectorAll(".tt09p");
  var current = null;

  function reposition() {
    if (!current || !bL || !bR) return;
    bL.style.left = current.offsetLeft - 20 + "px";
    bR.style.left = current.offsetLeft + current.offsetWidth + 4 + "px";
  }
  function activate(btn) {
    current = btn;
    btns.forEach(function (b) {
      b.classList.toggle("active", b === btn);
    });
    var i = Array.prototype.indexOf.call(btns, btn);
    pnls.forEach(function (p, j) {
      p.classList.toggle("active", j === i);
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
