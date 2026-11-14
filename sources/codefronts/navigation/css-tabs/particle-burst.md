---
source: "codefronts"
url: "https://codefronts.com/navigation/css-tabs/particle-burst/"
title: "Particle Burst"
section: "navigation"
category: "css-tabs"
category_name: "CSS Tabs"
description: "Each tab click spawns 8 small color sparks that fly outward and fade."
has_js: "true"
---

Here's a working CSS Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Particle Burst
Source: https://codefronts.com/navigation/css-tabs/particle-burst/

Each tab click spawns 8 small color sparks that fly outward and fade. JS positions each particle at the click point; CSS animates trajectory + fade. The active tab is also highlighted with a coral underline.
## HTML
```html
<div class="tt32">
  <nav class="tt32n">
    <span class="tt32line" aria-hidden="true"></span>
    <button class="tt32b active" data-t>Spark</button>
    <button class="tt32b" data-t>Bloom</button>
    <button class="tt32b" data-t>Burst</button>
    <button class="tt32b" data-t>Flare</button>
  </nav>
</div>
```
## CSS
```css
.tt32 {
  background: #1c1424;
  padding: 36px 18px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  min-height: 100vh;
  box-sizing: border-box;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.tt32n {
  position: relative;
  display: flex;
  gap: 0;
  min-width: 0;
  width: 100%;
  max-width: 420px;
}

.tt32line {
  position: absolute;
  bottom: -2px;
  left: 0;
  height: 2px;
  width: 0;
  background: #ff6b6b;
  border-radius: 2px;
  transition: left 0.4s cubic-bezier(0.65, 0, 0.35, 1), width 0.4s cubic-bezier(0.65, 0, 0.35, 1);
  pointer-events: none;
}

.tt32b {
  flex: 1;
  min-width: 0;
  padding: 10px 12px;
  border: 0;
  background: transparent;
  font: 600 12px/1 ui-sans-serif, system-ui;
  letter-spacing: 0.04em;
  color: rgba(255, 255, 255, 0.55);
  cursor: pointer;
  position: relative;
  transition: color 0.25s;
  white-space: nowrap;
}

.tt32b:hover {
  color: rgba(255, 255, 255, 0.9);
}

.tt32b.active {
  color: #ff6b6b;
}

.tt32b:focus-visible {
  outline: 2px solid #ff6b6b;
  outline-offset: 2px;
  border-radius: 4px;
}

.tt32spark {
  position: absolute;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  pointer-events: none;
  animation: tt32-fly 0.6s cubic-bezier(0.2, 0.6, 0.4, 1) forwards;
}

@keyframes tt32-fly {
  from {
    transform: translate(0, 0) scale(1);
    opacity: 1;
  }

  to {
    transform: translate(var(--dx), var(--dy)) scale(0.3);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tt32line {
    transition: none;
  }

  .tt32spark {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* Particle Burst — toggle .active, slide underline, spawn 8 color sparks
   on click. Re-positions the underline on viewport resize. */
(function () {
  var nav = document.querySelector(".tt32n");
  if (!nav) return;
  var btns = nav.querySelectorAll("[data-t]");
  var line = nav.querySelector(".tt32line");
  var current = null;
  var COLORS = ["#ff6b6b", "#ffd166", "#06d6a0", "#118ab2", "#ef476f"];

  function reposition() {
    if (!current || !line) return;
    line.style.left = current.offsetLeft + "px";
    line.style.width = current.offsetWidth + "px";
  }
  function burst(btn) {
    var rect = btn.getBoundingClientRect();
    var navRect = nav.getBoundingClientRect();
    var cx = rect.left - navRect.left + rect.width / 2;
    var cy = rect.top - navRect.top + rect.height / 2;
    for (var i = 0; i < 8; i++) {
      var s = document.createElement("span");
      s.className = "tt32spark";
      s.style.left = cx + "px";
      s.style.top = cy + "px";
      s.style.background = COLORS[i % COLORS.length];
      var angle = (i / 8) * Math.PI * 2;
      var dist = 32 + Math.random() * 18;
      s.style.setProperty("--dx", Math.cos(angle) * dist + "px");
      s.style.setProperty("--dy", Math.sin(angle) * dist + "px");
      nav.appendChild(s);
      setTimeout(
        (function (n) {
          return function () {
            if (n.parentNode) n.parentNode.removeChild(n);
          };
        })(s),
        700,
      );
    }
  }
  function activate(btn, withBurst) {
    current = btn;
    btns.forEach(function (b) {
      b.classList.toggle("active", b === btn);
    });
    reposition();
    if (withBurst) burst(btn);
  }
  btns.forEach(function (b) {
    b.addEventListener("click", function () {
      activate(b, true);
    });
  });
  window.addEventListener("resize", reposition);
  var initial = nav.querySelector("[data-t].active") || btns[0];
  if (initial) activate(initial, false);
})();
```
