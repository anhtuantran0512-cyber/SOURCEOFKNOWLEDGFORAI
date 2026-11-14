---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-add-to-cart-button-animation/"
title: "CSS Add To Cart Button Animation"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "An e-commerce add-to-cart button that animates a product dot flying into a cart icon badge on click, with a count increment and brief success flash."
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Add To Cart Button Animation
Source: https://codefronts.com/motion/css-animated-buttons/css-add-to-cart-button-animation/

An e-commerce add-to-cart button that animates a product dot flying into a cart icon badge on click, with a count increment and brief success flash.
## HTML
```html
<div class="ab-15">
  <div class="ab-15__card">
    <div class="ab-15__product">
      <div class="ab-15__img"></div>
      <div class="ab-15__info">
        <p class="ab-15__name">Mechanical Keyboard Pro</p>
        <p class="ab-15__price">$149.00</p>
      </div>
    </div>
    <div class="ab-15__actions">
      <button class="ab-15__btn" id="ab-15-btn">
        <svg class="ab-15__cart-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
          <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
        </svg>
        <span>Add to Cart</span>
        <span class="ab-15__badge" id="ab-15-badge">0</span>
      </button>
    </div>
  </div>
</div>
```
## CSS
```css
.ab-15,
.ab-15 *,
.ab-15 *::before,
.ab-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-15 ::selection {
  background: #f59e0b;
  color: #fff;
}

.ab-15 {
  --dot-color: #f59e0b;
  font-family: system-ui,sans-serif;
  background: #fff7ed;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.ab-15__card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(0,0,0,.08);
  padding: 1.5rem;
  width: 100%;
  max-width: 360px;
}

.ab-15__product {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.25rem;
  align-items: center;
}

.ab-15__img {
  width: 72px;
  height: 72px;
  flex-shrink: 0;
  background: linear-gradient(135deg,#fde68a,#f59e0b);
  border-radius: 10px;
}

.ab-15__name {
  font-size: .95rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: .35rem;
}

.ab-15__price {
  font-size: 1.15rem;
  font-weight: 800;
  color: #f59e0b;
}

.ab-15__actions {
  position: relative;
}

.ab-15__btn {
  position: relative;
  display: flex;
  align-items: center;
  gap: .6rem;
  width: 100%;
  padding: .85rem 1.5rem;
  font-size: .95rem;
  font-weight: 700;
  color: #fff;
  background: #1e293b;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  transition: background .3s,transform .15s;
  overflow: visible;
}

.ab-15__btn:hover {
  background: #334155;
  transform: translateY(-1px);
}

.ab-15__btn.is-added {
  background: #059669;
}

.ab-15__btn:active {
  transform: translateY(0);
}

.ab-15__cart-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.ab-15__badge {
  position: absolute;
  top: -8px;
  right: -8px;
  min-width: 20px;
  height: 20px;
  padding: 0 5px;
  background: #f59e0b;
  color: #fff;
  font-size: .72rem;
  font-weight: 800;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #fff;
}

.ab-15__badge.pop {
  animation: ab-15-pop .3s ease both;
}

@keyframes ab-15-pop {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.5);
  }

  100% {
    transform: scale(1);
  }
}

.ab-15__dot {
  position: fixed;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--dot-color,#f59e0b);
  pointer-events: none;
  z-index: 9999;
  animation: ab-15-fly .65s cubic-bezier(.4,0,.2,1) forwards;
  will-change: transform,opacity;
}

@keyframes ab-15-fly {
  0% {
    transform: translate(0,0) scale(1);
    opacity: 1;
  }

  50% {
    transform: translate(calc(var(--tx)*.5),calc(var(--ty)*.5 - 40px)) scale(.8);
    opacity: .9;
  }

  100% {
    transform: translate(var(--tx),var(--ty)) scale(0);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ab-15__dot {
    animation: none;
    opacity: 0;
  }

  .ab-15__badge.pop {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var btn=document.getElementById('ab-15-btn');
  var badge=document.getElementById('ab-15-badge');
  if(!btn||!badge)return;
  var count=0;
  function flyDot(e){
    var br=btn.getBoundingClientRect();
    var bbr=badge.getBoundingClientRect();
    var startX=e.clientX-5;
    var startY=e.clientY-5;
    var endX=bbr.left+bbr.width/2-5;
    var endY=bbr.top+bbr.height/2-5;
    var dot=document.createElement('div');
    dot.className='ab-15__dot';
    dot.style.left=startX+'px';
    dot.style.top=startY+'px';
    dot.style.setProperty('--tx',(endX-startX)+'px');
    dot.style.setProperty('--ty',(endY-startY)+'px');
    document.body.appendChild(dot);
    dot.addEventListener('animationend',function(){
      dot.remove();
      count++;
      badge.textContent=count;
      badge.classList.remove('pop');
      void badge.offsetWidth;
      badge.classList.add('pop');
    });
  }
  btn.addEventListener('click',function(e){
    btn.classList.add('is-added');
    setTimeout(function(){btn.classList.remove('is-added')},800);
    flyDot(e);
  });
})();
```
