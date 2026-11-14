---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-loading-spinner-inside-button/"
title: "CSS Loading Spinner Inside Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A button that reveals a micro-spinner overlay and transitions to a disabled loading state on click, then resolves to success — all using CSS transitions and…"
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Loading Spinner Inside Button
Source: https://codefronts.com/motion/css-animated-buttons/css-loading-spinner-inside-button/

A button that reveals a micro-spinner overlay and transitions to a disabled loading state on click, then resolves to success — all using CSS transitions and a JS state machine.
## HTML
```html
<div class="ab-18">
  <p class="ab-18__label">Click to simulate a request</p>
  <div class="ab-18__group">
    <button class="ab-18__btn" id="ab-18-btn">
      <span class="ab-18__text" id="ab-18-text">Save Changes</span>
      <svg class="ab-18__check" viewBox="0 0 20 20" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <polyline points="16 5 8 14 4 10" pathLength="24"/>
      </svg>
    </button>
    <button class="ab-18__btn ab-18__btn--outline" id="ab-18-btn2">
      <span class="ab-18__text" id="ab-18-text2">Subscribe</span>
      <svg class="ab-18__check" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <polyline points="16 5 8 14 4 10" pathLength="24"/>
      </svg>
    </button>
  </div>
</div>
```
## CSS
```css
.ab-18,
.ab-18 *,
.ab-18 *::before,
.ab-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-18 ::selection {
  background: #4f46e5;
  color: #fff;
}

.ab-18 {
  font-family: system-ui,sans-serif;
  background: #f1f5f9;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
}

.ab-18__label {
  font-size: .78rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #64748b;
}

.ab-18__group {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.ab-18__btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: .85rem 2rem;
  min-width: 160px;
  font-size: .95rem;
  font-weight: 700;
  color: #fff;
  background: #4f46e5;
  border: 2px solid #4f46e5;
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  transition: background .3s,border-color .3s,transform .15s;
  overflow: hidden;
}

.ab-18__btn--outline {
  background: transparent;
  color: #4f46e5;
}

.ab-18__btn:hover:not([disabled]) {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.ab-18__btn:active:not([disabled]) {
  transform: translateY(0);
}

.ab-18__btn[disabled] {
  cursor: not-allowed;
  opacity: .85;
}

.ab-18__text {
  transition: opacity .25s;
  display: block;
}

.ab-18__check {
  position: absolute;
  width: 20px;
  height: 20px;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .3s .2s,transform .3s .2s;
}

.ab-18__check polyline {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
}
/* spinner */

.ab-18__btn::after {
  content: '';
  position: absolute;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: 2px solid rgba(255,255,255,.3);
  border-top-color: #fff;
  opacity: 0;
  transform: scale(0);
  transition: opacity .2s,transform .2s;
  pointer-events: none;
}

.ab-18__btn--outline::after {
  border: 2px solid rgba(79,70,229,.3);
  border-top-color: #4f46e5;
}
/* loading state */

.ab-18__btn.is-loading .ab-18__text {
  opacity: 0;
}

.ab-18__btn.is-loading::after {
  opacity: 1;
  transform: scale(1);
  animation: ab-18-spin .8s linear infinite;
}
/* success state */

.ab-18__btn.is-success {
  background: #059669;
  border-color: #059669;
}

.ab-18__btn.is-success .ab-18__text {
  opacity: 0;
}

.ab-18__btn.is-success .ab-18__check {
  opacity: 1;
  transform: scale(1);
}

.ab-18__btn.is-success .ab-18__check polyline {
  animation: ab-18-draw .4s ease .1s forwards;
}

@keyframes ab-18-spin {
  to {
    transform: scale(1) rotate(360deg);
  }
}

@keyframes ab-18-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ab-18__btn.is-loading::after {
    animation: none;
  }

  .ab-18__btn.is-success .ab-18__check polyline {
    animation: none;
    stroke-dashoffset: 0;
  }

  .ab-18__text,
    .ab-18__check {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  function makeBtn(id,txtId){
    var btn=document.getElementById(id);
    var txt=document.getElementById(txtId);
    if(!btn||!txt)return;
    var orig=txt.textContent;
    var busy=false;
    btn.style.width=btn.offsetWidth+'px';
    btn.addEventListener('click',function(){
      if(busy)return;busy=true;
      btn.classList.add('is-loading');
      btn.disabled=true;
      setTimeout(function(){
        btn.classList.remove('is-loading');
        btn.classList.add('is-success');
        setTimeout(function(){
          btn.classList.remove('is-success');
          btn.disabled=false;
          busy=false;
        },1800);
      },2000);
    });
  }
  makeBtn('ab-18-btn','ab-18-text');
  makeBtn('ab-18-btn2','ab-18-text2');
})();
```
