---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-submit-button-success-state/"
title: "CSS Submit Button Success State"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A form submit button that morphs into a checkmark success state with a width collapse animation and icon draw, then resets — all styled with CSS transitions…"
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Submit Button Success State
Source: https://codefronts.com/motion/css-animated-buttons/css-submit-button-success-state/

A form submit button that morphs into a checkmark success state with a width collapse animation and icon draw, then resets — all styled with CSS transitions and driven by a JS class toggle.
## HTML
```html
<div class="ab-12">
  <div class="ab-12__card">
    <h2 class="ab-12__title">Contact Us</h2>
    <p class="ab-12__sub">We'll get back to you within 24 hours.</p>
    <div class="ab-12__field"><input class="ab-12__input" type="text" placeholder="Your name" /></div>
    <div class="ab-12__field"><input class="ab-12__input" type="email" placeholder="Email address" /></div>
    <button class="ab-12__btn" id="ab-12-btn">
      <span class="ab-12__text" id="ab-12-text">Send Message</span>
      <svg class="ab-12__check" id="ab-12-check" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <polyline points="20 6 9 17 4 12" pathLength="30"></polyline>
      </svg>
    </button>
  </div>
</div>
```
## CSS
```css
.ab-12,
.ab-12 *,
.ab-12 *::before,
.ab-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-12 ::selection {
  background: #10b981;
  color: #fff;
}

.ab-12 {
  --success: #10b981;
  --primary: #4f46e5;
  font-family: system-ui,sans-serif;
  background: #f8fafc;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.ab-12__card {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 24px rgba(0,0,0,.08);
  padding: 2rem 2rem 2rem;
  width: 100%;
  max-width: 380px;
}

.ab-12__title {
  font-size: 1.4rem;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: .4rem;
}

.ab-12__sub {
  font-size: .88rem;
  color: #64748b;
  margin-bottom: 1.5rem;
  line-height: 1.5;
}

.ab-12__field {
  margin-bottom: .9rem;
}

.ab-12__input {
  width: 100%;
  padding: .7rem 1rem;
  border: 1.5px solid #e2e8f0;
  border-radius: 8px;
  font-size: .9rem;
  color: #1e293b;
  outline: none;
  transition: border-color .2s;
  background: #f8fafc;
}

.ab-12__input:focus {
  border-color: var(--primary);
}

.ab-12__btn {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 48px;
  padding: 0 1.5rem;
  font-size: 1rem;
  font-weight: 700;
  color: #fff;
  background: var(--primary);
  border: none;
  border-radius: 50px;
  cursor: pointer;
  outline: none;
  overflow: hidden;
  transition: width .4s cubic-bezier(.4,0,.2,1),background .4s,box-shadow .3s;
  box-shadow: 0 4px 16px rgba(79,70,229,.3);
  margin-top: .25rem;
  will-change: width;
}

.ab-12__btn:hover:not(.is-success) {
  filter: brightness(1.08);
}

.ab-12__btn.is-success {
  width: 48px;
  background: var(--success);
  box-shadow: 0 4px 16px rgba(16,185,129,.35);
}

.ab-12__text {
  transition: opacity .2s,transform .2s;
  white-space: nowrap;
}

.ab-12__btn.is-success .ab-12__text {
  opacity: 0;
  transform: scale(.6);
  position: absolute;
}

.ab-12__check {
  position: absolute;
  width: 24px;
  height: 24px;
  opacity: 0;
  transform: scale(.6);
  transition: opacity .2s .35s,transform .3s .35s;
}

.ab-12__check polyline {
  stroke-dasharray: 30;
  stroke-dashoffset: 30;
}

.ab-12__btn.is-success .ab-12__check {
  opacity: 1;
  transform: scale(1);
}

.ab-12__btn.is-success .ab-12__check polyline {
  animation: ab-12-draw .4s ease .4s forwards;
}

@keyframes ab-12-draw {
  to {
    stroke-dashoffset: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ab-12__btn,
    .ab-12__check,
    .ab-12__text {
    transition: none;
  }

  .ab-12__btn.is-success .ab-12__check polyline {
    animation: none;
    stroke-dashoffset: 0;
  }
}
```

## JavaScript
```js
(function(){
  var btn=document.getElementById('ab-12-btn');
  if(!btn)return;
  var timer=null;
  btn.addEventListener('click',function(){
    if(btn.classList.contains('is-success'))return;
    btn.classList.add('is-success');
    btn.disabled=true;
    clearTimeout(timer);
    timer=setTimeout(function(){
      btn.classList.remove('is-success');
      btn.disabled=false;
    },2500);
  });
})();
```
