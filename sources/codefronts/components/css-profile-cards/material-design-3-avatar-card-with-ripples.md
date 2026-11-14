---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/material-design-3-avatar-card-with-ripples/"
title: "Material Design 3 Avatar Card with Ripples"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A Material 3 profile card with rounded corners, tonal chips and a floating action button, where taps spawn ink ripples from the exact click point."
has_js: "true"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design 3 Avatar Card with Ripples
Source: https://codefronts.com/components/css-profile-cards/material-design-3-avatar-card-with-ripples/

A Material 3 profile card with rounded corners, tonal chips and a floating action button, where taps spawn ink ripples from the exact click point.
## HTML
```html
<div class="pc-14">
  <div class="pc-14__card" id="pc-14-card">
    <div class="pc-14__pfp">LO<div class="pc-14__ripple-host" id="pc-14-host"></div></div>
    <h3>Liam O'Brien</h3>
    <p class="pc-14__role">Android Developer</p>
    <div class="pc-14__chips">
      <span>Kotlin</span><span>Compose</span><span>Material 3</span>
    </div>
    <div class="pc-14__actions">
      <button class="pc-14__fab" id="pc-14-fab" aria-label="Add">
        <span class="pc-14__plus">+</span>
      </button>
      <button class="pc-14__text">Follow</button>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-14,
.pc-14 *,
.pc-14 *::before,
.pc-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-14 ::selection {
  background: #8ab4f8;
  color: #202124;
}

.pc-14 {
  font-family: 'Google Sans','Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #131316;
  color: #e3e3e3;
}

.pc-14__card {
  width: 300px;
  border-radius: 28px;
  padding: 28px;
  text-align: center;
  background: #1e1f24;
  border: 1px solid #2c2d33;
  box-shadow: 0 8px 24px -10px rgba(0,0,0,.6);
}

.pc-14__pfp {
  position: relative;
  overflow: hidden;
  width: 90px;
  height: 90px;
  border-radius: 28px;
  margin: 0 auto 18px;
  display: grid;
  place-items: center;
  font-weight: 700;
  font-size: 1.6rem;
  color: #131316;
  background: linear-gradient(135deg,#a8c7fa,#d0bcff);
  cursor: pointer;
}

.pc-14__ripple-host {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.pc-14__rip {
  position: absolute;
  border-radius: 50%;
  background: rgba(255,255,255,.5);
  transform: translate(-50%,-50%) scale(0);
  animation: pc-14-rip .6s ease-out forwards;
  pointer-events: none;
}

@keyframes pc-14-rip {
  to {
    transform: translate(-50%,-50%) scale(2.6);
    opacity: 0;
  }
}

.pc-14__card h3 {
  font-size: 1.35rem;
  font-weight: 700;
}

.pc-14__role {
  color: #9aa0a6;
  font-size: .86rem;
  margin-top: 3px;
}

.pc-14__chips {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 18px;
}

.pc-14__chips span {
  font-size: .74rem;
  padding: 6px 12px;
  border-radius: 20px;
  background: #2a2b31;
  border: 1px solid #3a3b42;
  color: #c8cbd1;
}

.pc-14__actions {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  margin-top: 24px;
}

.pc-14__fab {
  width: 56px;
  height: 56px;
  border-radius: 18px;
  border: none;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  background: linear-gradient(135deg,#a8c7fa,#8ab4f8);
  color: #0b1b3a;
  box-shadow: 0 6px 16px -6px #8ab4f8;
  transition: transform .18s,box-shadow .25s;
}

.pc-14__fab:hover {
  box-shadow: 0 10px 24px -6px #8ab4f8;
  transform: translateY(-2px);
}

.pc-14__fab:active {
  transform: scale(.94);
}

.pc-14__plus {
  font-size: 1.8rem;
  font-weight: 400;
  line-height: 1;
}

.pc-14__text {
  padding: 14px 26px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 600;
  font-size: .88rem;
  color: #8ab4f8;
  background: transparent;
  transition: background .25s;
}

.pc-14__text:hover {
  background: rgba(138,180,248,.12);
}

@media (prefers-reduced-motion: reduce) {
  .pc-14 * {
    transition: none!important;
  }

  .pc-14__rip {
    animation-duration: .01s;
  }
}
```

## JavaScript
```js
(function(){
  function ripple(host, x, y){
    var r = document.createElement('span');
    r.className = 'pc-14__rip';
    var rect = host.getBoundingClientRect();
    var size = Math.max(rect.width, rect.height);
    r.style.width = r.style.height = size + 'px';
    r.style.left = (x - rect.left) + 'px';
    r.style.top = (y - rect.top) + 'px';
    host.appendChild(r);
    setTimeout(function(){ r.remove(); }, 620);
  }
  var host = document.getElementById('pc-14-host');
  var pfp = host && host.parentElement;
  if(pfp) pfp.addEventListener('pointerdown', function(e){ ripple(host, e.clientX, e.clientY); });
  var fab = document.getElementById('pc-14-fab');
  if(fab) fab.addEventListener('pointerdown', function(e){ ripple(fab, e.clientX, e.clientY); });
})();
```
