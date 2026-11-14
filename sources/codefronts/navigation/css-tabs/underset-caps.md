---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/underset-caps/"
title: "Underset Caps"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Tiny uppercase mono labels above a single thick rule. The rule slides under the active label — measured live, like a sliding bookmark on a typecase shelf."
has_js: "true"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Underset Caps
Source: https://codefronts.com/navigation/css-tabs/underset-caps/

Tiny uppercase mono labels above a single thick rule. The rule slides under the active label — measured live, like a sliding bookmark on a typecase shelf.
## HTML
```html
<div class="tt06">
  <nav class="tt06n">
    <button class="tt06b active" data-t>Volume I</button>
    <button class="tt06b" data-t>Volume II</button>
    <button class="tt06b" data-t>Volume III</button>
    <button class="tt06b" data-t>Volume IV</button>
    <span class="tt06rule"> </span>
  </nav>
  <div class="tt06p active" data-p>The Origins, 1450–1600.</div>
  <div class="tt06p" data-p>The Reformation, 1600–1750.</div>
  <div class="tt06p" data-p>The Industrial Cut, 1750–1900.</div>
  <div class="tt06p" data-p>The Digital Era, 1980 onward.</div>
</div>
```
## CSS
```css
.tt06 {
  min-height: 100vh;
  background: #1a1a1a;
  padding: 28px 22px 22px;
  font-family: ui-monospace, monospace;
  width: 100%;
}

.tt06n {
  position: relative;
  display: flex;
  gap: 24px;
  padding-bottom: 14px;
}

.tt06b {
  border: 0;
  background: transparent;
  padding: 0;
  font: 700 9px/1 ui-monospace, monospace;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: rgba(232, 226, 208, 0.5);
  cursor: pointer;
  transition: color 0.25s;
}

.tt06b:hover {
  color: rgba(232, 226, 208, 0.85);
}

.tt06b.active {
  color: #e8e2d0;
}

.tt06rule {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 6px;
  background: #c43a32;
  transition: left 0.45s cubic-bezier(0.65, 0, 0.35, 1), width 0.45s cubic-bezier(0.65, 0, 0.35, 1);
}

.tt06p {
  display: none;
  padding-top: 18px;
  font: italic 12px/1.6 ui-serif, Georgia, serif;
  color: rgba(232, 226, 208, 0.7);
}

.tt06p.active {
  display: block;
}
```

## JavaScript
```js
/* Underset Caps — toggle .active and slide horizontal rule under active.
   Re-positions the sliding rule on viewport resize. */
(function () {
  var nav = document.querySelector(".tt06n");
  if (!nav) return;
  var btns = nav.querySelectorAll("[data-t]");
  var rule = nav.querySelector(".tt06rule");
  var pnls = document.querySelectorAll(".tt06p");
  var current = null;

  function reposition() {
    if (!current || !rule) return;
    rule.style.left = current.offsetLeft + "px";
    rule.style.width = current.offsetWidth + "px";
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
