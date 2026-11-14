---
source: "codefronts"
url: "https://codefronts.com/snippets/css-badges/dice-face/"
title: "Dice Face"
section: "snippets"
category: "css-badges"
category_name: "CSS Badges"
description: "A fair die with six possible states."
has_js: "true"
---

Here's a working CSS Badge from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dice Face
Source: https://codefronts.com/snippets/css-badges/dice-face/

A fair die with six possible states. Click to roll — the pip positions are correct, the animation is physical, the number updates. One honest square doing exactly one honest job.
## HTML
```html
<div class="bdg-18-stage">
  <div class="bdg-18-wrap">
    <div class="bdg-18-cube" id="bdg-18-cube">
      <div class="bdg-18-pip" data-pos="tl"></div>
      <div class="bdg-18-pip" data-pos="tc"></div>
      <div class="bdg-18-pip" data-pos="tr"></div>
      <div class="bdg-18-pip" data-pos="ml"></div>
      <div class="bdg-18-pip" data-pos="mc"></div>
      <div class="bdg-18-pip" data-pos="mr"></div>
      <div class="bdg-18-pip" data-pos="bl"></div>
      <div class="bdg-18-pip" data-pos="bc"></div>
      <div class="bdg-18-pip" data-pos="br"></div>
    </div>
  </div>
  <div class="bdg-18-face-num" id="bdg-18-face-num">—</div>
  <div class="bdg-18-caption">click the die to roll</div>
</div>
```
## CSS
```css
.bdg-18-stage {
  background: #fff;
  padding: 60px 48px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  width: 100%;
  min-height: 100vh;
}

.bdg-18-wrap {
  perspective: 600px;
}

.bdg-18-cube {
  width: 110px;
  height: 110px;
  background: #fff;
  border: 2.5px solid #1a1612;
  border-radius: 18px;
  display: grid;
  grid-template-areas: "tl tc tr" "ml mc mr" "bl bc br";
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  padding: 14px;
  cursor: pointer;
  box-shadow: 4px 4px 0 #1a1612, 5px 5px 8px rgba(0,0,0,0.12);
  transition: transform 0.15s, box-shadow 0.15s;
  position: relative;
  overflow: hidden;
}

.bdg-18-cube:active {
  transform: translate(3px, 3px);
  box-shadow: 1px 1px 0 #1a1612, 2px 2px 4px rgba(0,0,0,0.1);
}

.bdg-18-cube.is-rolling {
  animation: bdg-18-roll 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97);
}

@keyframes bdg-18-roll {
  0% {
    transform: rotate(0deg) scale(1);
  }

  20% {
    transform: rotate(-8deg) scale(0.95);
  }

  50% {
    transform: rotate(12deg) scale(0.92);
  }

  75% {
    transform: rotate(-5deg) scale(0.97);
  }

  100% {
    transform: rotate(0deg) scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bdg-18-cube.is-rolling {
    animation: none;
  }
}

.bdg-18-pip {
  display: flex;
  align-items: center;
  justify-content: center;
}

.bdg-18-pip::after {
  content: '';
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: transparent;
  transition: background 0.2s;
}

.bdg-18-pip.is-on::after {
  background: #1a1612;
}

.bdg-18-pip[data-pos="tl"] {
  grid-area: tl;
}

.bdg-18-pip[data-pos="tc"] {
  grid-area: tc;
}

.bdg-18-pip[data-pos="tr"] {
  grid-area: tr;
}

.bdg-18-pip[data-pos="ml"] {
  grid-area: ml;
}

.bdg-18-pip[data-pos="mc"] {
  grid-area: mc;
}

.bdg-18-pip[data-pos="mr"] {
  grid-area: mr;
}

.bdg-18-pip[data-pos="bl"] {
  grid-area: bl;
}

.bdg-18-pip[data-pos="bc"] {
  grid-area: bc;
}

.bdg-18-pip[data-pos="br"] {
  grid-area: br;
}

.bdg-18-caption {
  font-family: system-ui, "Bricolage Grotesque", sans-serif;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #aaa;
  text-align: center;
}

.bdg-18-face-num {
  font-family: Georgia, "Fraunces", serif;
  font-size: 48px;
  font-style: italic;
  font-weight: 300;
  color: #1a1612;
  line-height: 1;
  text-align: center;
}
```

## JavaScript
```js
// Click the die to roll. Pip positions per face are encoded as
// arrays of grid-area names; the .is-on class lights up matching pips.
var dieFaces = {
  1: ['mc'],
  2: ['tr', 'bl'],
  3: ['tr', 'mc', 'bl'],
  4: ['tl', 'tr', 'bl', 'br'],
  5: ['tl', 'tr', 'mc', 'bl', 'br'],
  6: ['tl', 'tr', 'ml', 'mr', 'bl', 'br']
};
var dieCube    = document.getElementById('bdg-18-cube');
var dieFaceNum = document.getElementById('bdg-18-face-num');
var dieRolling = false;

function dieSetFace(n) {
  var pips = dieFaces[n];
  dieCube.querySelectorAll('.bdg-18-pip').forEach(function (p) {
    p.classList.toggle('is-on', pips.indexOf(p.dataset.pos) !== -1);
  });
  dieFaceNum.textContent = n;
}

if (dieCube) {
  dieCube.addEventListener('click', function () {
    if (dieRolling) return;
    dieRolling = true;
    dieCube.classList.add('is-rolling');
    setTimeout(function () {
      var n = Math.floor(Math.random() * 6) + 1;
      dieSetFace(n);
      dieCube.classList.remove('is-rolling');
      dieRolling = false;
    }, 280);
  });
}
```
