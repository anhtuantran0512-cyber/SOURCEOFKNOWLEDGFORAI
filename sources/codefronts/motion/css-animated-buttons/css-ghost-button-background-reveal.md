---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-ghost-button-background-reveal/"
title: "CSS Ghost Button Background Reveal"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "Transparent ghost buttons that elegantly fill with a solid colour or gradient on hover, with JS-powered ripple origin tracking so the fill emanates from the…"
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Ghost Button Background Reveal
Source: https://codefronts.com/motion/css-animated-buttons/css-ghost-button-background-reveal/

Transparent ghost buttons that elegantly fill with a solid colour or gradient on hover, with JS-powered ripple origin tracking so the fill emanates from the exact cursor position.
## HTML
```html
<div class="ab-20">
  <p class="ab-20__label">Hover from any direction</p>
  <div class="ab-20__row">
    <button class="ab-20__btn ab-20__btn--violet">
      <span class="ab-20__fill"></span>
      <span class="ab-20__label-inner">Get Started</span>
    </button>
    <button class="ab-20__btn ab-20__btn--cyan">
      <span class="ab-20__fill"></span>
      <span class="ab-20__label-inner">View Docs</span>
    </button>
    <button class="ab-20__btn ab-20__btn--rose">
      <span class="ab-20__fill"></span>
      <span class="ab-20__label-inner">Contact Us</span>
    </button>
  </div>
</div>
```
## CSS
```css
.ab-20,
.ab-20 *,
.ab-20 *::before,
.ab-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-20 ::selection {
  background: #7c3aed;
  color: #fff;
}

.ab-20 {
  font-family: system-ui,sans-serif;
  background: #0a0a14;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
}

.ab-20__label {
  font-size: .78rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #475569;
}

.ab-20__row {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.ab-20__btn {
  --fill-color: #7c3aed;
  position: relative;
  overflow: hidden;
  padding: .85rem 2.2rem;
  font-size: .95rem;
  font-weight: 700;
  color: #e2e8f0;
  background: transparent;
  border: 2px solid rgba(255,255,255,.2);
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  transition: color .35s,border-color .35s;
}

.ab-20__btn--violet {
  --fill-color: #7c3aed;
  color: #c4b5fd;
  border-color: #7c3aed;
}

.ab-20__btn--cyan {
  --fill-color: #0891b2;
  color: #67e8f9;
  border-color: #0891b2;
}

.ab-20__btn--rose {
  --fill-color: #e11d48;
  color: #fda4af;
  border-color: #e11d48;
}

.ab-20__btn.is-hovered {
  color: #fff;
  border-color: transparent;
}

.ab-20__fill {
  position: absolute;
  border-radius: 50%;
  background: var(--fill-color);
  left: var(--rx,50%);
  top: var(--ry,50%);
  width: 0;
  height: 0;
  transform: translate(-50%,-50%);
  transition: width .5s cubic-bezier(.4,0,.2,1),height .5s cubic-bezier(.4,0,.2,1);
  pointer-events: none;
  z-index: 0;
}

.ab-20__btn.is-hovered .ab-20__fill {
  width: var(--size,400px);
  height: var(--size,400px);
}

.ab-20__label-inner {
  position: relative;
  z-index: 1;
}

@media (prefers-reduced-motion: reduce) {
  .ab-20__fill {
    transition: none;
  }

  .ab-20__btn.is-hovered .ab-20__fill {
    width: 100%;
    height: 100%;
    border-radius: 0;
  }
}
```

## JavaScript
```js
(function(){
  var btns=document.querySelectorAll('.ab-20__btn');
  btns.forEach(function(btn){
    var fill=btn.querySelector('.ab-20__fill');
    if(!fill)return;
    var diag=Math.sqrt(Math.pow(btn.offsetWidth,2)+Math.pow(btn.offsetHeight,2));
    btn.style.setProperty('--size',diag*3+'px');
    btn.addEventListener('mouseenter',function(e){
      fill.style.setProperty('--rx',e.offsetX+'px');
      fill.style.setProperty('--ry',e.offsetY+'px');
      btn.classList.add('is-hovered');
    });
    btn.addEventListener('mouseleave',function(e){
      fill.style.setProperty('--rx',e.offsetX+'px');
      fill.style.setProperty('--ry',e.offsetY+'px');
      btn.classList.remove('is-hovered');
    });
  });
})();
```
