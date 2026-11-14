---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/specimen-no/"
title: "Specimen No."
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Tab labels read as letterpress specimen slugs."
has_js: "true"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Specimen No.
Source: https://codefronts.com/navigation/css-tabs/specimen-no/

Tab labels read as letterpress specimen slugs. The active tab is announced by a 4-digit serial that flips digits on activation, and a mint underline draws under the active label.
## HTML
```html
<div class="tt01">
  <div class="tt01serial" data-tt01-serial>0317</div>
  <nav class="tt01n">
    <button class="tt01b active" data-t data-tt01="0317">Helvetica</button>
    <button class="tt01b" data-t data-tt01="0211">Bodoni</button>
    <button class="tt01b" data-t data-tt01="0489">Futura</button>
    <span class="tt01rule"> </span>
  </nav>
  <div class="tt01p active" data-p>Cut by Max Miedinger, 1957. Neo-grotesque sans.</div>
  <div class="tt01p" data-p>Cut by Giambattista Bodoni, 1798. Modern serif.</div>
  <div class="tt01p" data-p>Cut by Paul Renner, 1927. Geometric sans.</div>
</div>
```
## CSS
```css
.tt01 {
  min-height: 100vh;
  background: #1f2326;
  padding: 18px 22px 16px;
  font-family: ui-monospace, monospace;
  width: 100%;
}

.tt01serial {
  font: 800 36px/1 ui-monospace, monospace;
  color: #51d5c2;
  letter-spacing: 0.04em;
  margin-bottom: 6px;
  transition: opacity 0.15s;
}

.tt01serial.fade {
  opacity: 0.2;
}

.tt01n {
  position: relative;
  display: flex;
  gap: 0;
  border-top: 1.5px solid rgba(81, 213, 194, 0.25);
  border-bottom: 1px solid rgba(81, 213, 194, 0.12);
}

.tt01b {
  flex: 1;
  padding: 12px 8px;
  border: 0;
  background: transparent;
  font: 700 11px/1 ui-monospace, monospace;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: rgba(232, 226, 208, 0.45);
  cursor: pointer;
  border-right: 1px solid rgba(81, 213, 194, 0.1);
  transition: color 0.25s, transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tt01b:last-child {
  border-right: 0;
}

.tt01b:hover {
  color: rgba(232, 226, 208, 0.75);
}

.tt01b.active {
  color: #51d5c2;
  transform: translateY(-1px);
}

.tt01rule {
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 0;
  height: 2px;
  background: #51d5c2;
  transition: left 0.4s cubic-bezier(0.65, 0, 0.35, 1), width 0.4s cubic-bezier(0.65, 0, 0.35, 1);
}

.tt01p {
  display: none;
  padding-top: 12px;
  font: italic 11px/1.6 ui-serif, Georgia;
  color: rgba(232, 226, 208, 0.7);
}

.tt01p.active {
  display: block;
}
```

## JavaScript
```js
/* Specimen No. — toggle .active and update sliding rule + flip serial.
   Re-positions the sliding rule on viewport resize. */
(function () {
  var nav = document.querySelector(".tt01n");
  if (!nav) return;
  var btns = nav.querySelectorAll("[data-t]");
  var serial = document.querySelector("[data-tt01-serial]");
  var rule = document.querySelector(".tt01rule");
  var pnls = document.querySelectorAll(".tt01p");
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
    if (serial && btn.dataset.tt01) {
      serial.classList.add("fade");
      setTimeout(function () {
        serial.textContent = btn.dataset.tt01;
        serial.classList.remove("fade");
      }, 150);
    }
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
