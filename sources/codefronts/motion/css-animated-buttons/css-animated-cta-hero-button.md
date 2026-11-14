---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-animated-cta-hero-button/"
title: "CSS Animated CTA Hero Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A hero-section CTA button with a pulsing ring beacon, gradient text label, and particle burst on click — combining CSS animations with a lightweight JS…"
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated CTA Hero Button
Source: https://codefronts.com/motion/css-animated-buttons/css-animated-cta-hero-button/

A hero-section CTA button with a pulsing ring beacon, gradient text label, and particle burst on click — combining CSS animations with a lightweight JS particle emitter.
## HTML
```html
<div class="ab-11">
  <div class="ab-11__hero">
    <p class="ab-11__eyebrow">✦ Now in public beta</p>
    <h1 class="ab-11__title">The dev platform<br>built for speed.</h1>
    <p class="ab-11__sub">Deploy anywhere. Scale effortlessly. Ship today.</p>
    <div class="ab-11__wrap" id="ab-11-wrap">
      <button class="ab-11__btn" id="ab-11-btn">Start Building Free</button>
    </div>
    <p class="ab-11__note">No credit card · 50k free API calls included</p>
  </div>
</div>
```
## CSS
```css
.ab-11,
.ab-11 *,
.ab-11 *::before,
.ab-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-11 ::selection {
  background: #7c3aed;
  color: #fff;
}

.ab-11 {
  --beacon: #a78bfa;
  font-family: system-ui,sans-serif;
  background: #050510;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.ab-11__hero {
  text-align: center;
  max-width: 520px;
}

.ab-11__eyebrow {
  font-size: .8rem;
  letter-spacing: .16em;
  color: #a78bfa;
  margin-bottom: 1rem;
  text-transform: uppercase;
}

.ab-11__title {
  font-size: clamp(2rem,5vw,3rem);
  font-weight: 900;
  color: #fff;
  line-height: 1.1;
  margin-bottom: 1rem;
}

.ab-11__sub {
  font-size: 1rem;
  color: #94a3b8;
  margin-bottom: 2rem;
  line-height: 1.6;
}

.ab-11__wrap {
  position: relative;
  display: inline-block;
  margin-bottom: 1rem;
}

.ab-11__wrap::before,
.ab-11__wrap::after {
  content: '';
  position: absolute;
  inset: -6px;
  border-radius: 16px;
  border: 2px solid var(--beacon);
  opacity: 0;
  animation: ab-11-beacon 2s ease-out infinite;
}

.ab-11__wrap::after {
  animation-delay: .7s;
}

.ab-11__btn {
  position: relative;
  z-index: 1;
  padding: .95rem 2.6rem;
  font-size: 1.05rem;
  font-weight: 800;
  color: #fff;
  background: linear-gradient(135deg,#7c3aed,#2563eb);
  border: none;
  border-radius: 12px;
  cursor: pointer;
  outline: none;
  letter-spacing: .03em;
  box-shadow: 0 4px 24px rgba(124,58,237,.45);
  transition: filter .2s,transform .15s;
}

.ab-11__btn:hover {
  filter: brightness(1.12);
  transform: translateY(-2px);
}

.ab-11__btn:active {
  transform: translateY(0);
}

.ab-11__note {
  font-size: .75rem;
  color: #475569;
  margin-top: .5rem;
}

@keyframes ab-11-beacon {
  0% {
    transform: scale(1);
    opacity: .7;
  }

  100% {
    transform: scale(1.5);
    opacity: 0;
  }
}

.ab-11__particle {
  position: absolute;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  pointer-events: none;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  animation: ab-11-burst .7s ease-out forwards;
  will-change: transform,opacity;
}

@keyframes ab-11-burst {
  0% {
    transform: translate(-50%,-50%) translate(0,0) scale(1);
    opacity: 1;
  }

  100% {
    transform: translate(-50%,-50%) translate(var(--dx),var(--dy)) scale(0);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ab-11__wrap::before,
    .ab-11__wrap::after {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var wrap=document.getElementById('ab-11-wrap');
  var btn=document.getElementById('ab-11-btn');
  if(!btn||!wrap)return;
  var colours=['#a78bfa','#60a5fa','#34d399','#f472b6','#fbbf24','#fff'];
  var COUNT=12;
  btn.addEventListener('click',function(e){
    for(var i=0;i<COUNT;i++){
      var p=document.createElement('span');
      p.className='ab-11__particle';
      var angle=Math.random()*Math.PI*2;
      var dist=40+Math.random()*40;
      p.style.setProperty('--dx',Math.cos(angle)*dist+'px');
      p.style.setProperty('--dy',Math.sin(angle)*dist+'px');
      p.style.background=colours[Math.floor(Math.random()*colours.length)];
      p.style.left=e.offsetX+'px';
      p.style.top=e.offsetY+'px';
      wrap.appendChild(p);
      p.addEventListener('animationend',function(){this.remove()});
    }
  });
})();
```
