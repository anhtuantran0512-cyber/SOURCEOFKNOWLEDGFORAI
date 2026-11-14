---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-next-prev-arrow-button-hover/"
title: "CSS Next Prev Arrow Button Hover"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "Pagination and slider navigation controls where arrow icons slide subtly forward or backward on hover, with a functional slide counter driven by JS."
has_js: "true"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Next Prev Arrow Button Hover
Source: https://codefronts.com/motion/css-animated-buttons/css-next-prev-arrow-button-hover/

Pagination and slider navigation controls where arrow icons slide subtly forward or backward on hover, with a functional slide counter driven by JS.
## HTML
```html
<div class="ab-19">
  <div class="ab-19__slides">
    <div class="ab-19__slide is-active" id="ab-19-slide">
      <p class="ab-19__slide-label">Slide 1 of 5</p>
      <h3 class="ab-19__slide-title">Effortless Deployment</h3>
      <p class="ab-19__slide-body">Push your code and watch it go live in seconds. Zero config, zero downtime.</p>
    </div>
  </div>
  <div class="ab-19__nav">
    <button class="ab-19__arrow ab-19__arrow--prev is-disabled" id="ab-19-prev" aria-label="Previous slide">
      <span class="ab-19__arrow-inner">
        <svg class="ab-19__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"/></svg>
        <svg class="ab-19__icon ab-19__icon--ghost" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"/></svg>
      </span>
    </button>
    <span class="ab-19__counter" id="ab-19-counter">01 / 05</span>
    <button class="ab-19__arrow ab-19__arrow--next" id="ab-19-next" aria-label="Next slide">
      <span class="ab-19__arrow-inner">
        <svg class="ab-19__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg>
        <svg class="ab-19__icon ab-19__icon--ghost" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
.ab-19,
.ab-19 *,
.ab-19 *::before,
.ab-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-19 ::selection {
  background: #6366f1;
  color: #fff;
}

.ab-19 {
  font-family: system-ui,sans-serif;
  background: #0f172a;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
}

.ab-19__slides {
  width: 100%;
  max-width: 480px;
  background: #1e293b;
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 16px;
  padding: 2rem;
  min-height: 130px;
}

.ab-19__slide-label {
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #475569;
  margin-bottom: .6rem;
}

.ab-19__slide-title {
  font-size: 1.3rem;
  font-weight: 800;
  color: #f1f5f9;
  margin-bottom: .5rem;
}

.ab-19__slide-body {
  font-size: .88rem;
  color: #94a3b8;
  line-height: 1.6;
}

.ab-19__nav {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.ab-19__counter {
  font-size: .85rem;
  font-weight: 700;
  color: #94a3b8;
  letter-spacing: .08em;
  min-width: 60px;
  text-align: center;
  transition: transform .2s;
}

.ab-19__counter.tick {
  animation: ab-19-countup .25s ease both;
}

@keyframes ab-19-countup {
  0% {
    transform: scale(1.3);
  }

  100% {
    transform: scale(1);
  }
}

.ab-19__arrow {
  position: relative;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #1e293b;
  border: 1.5px solid rgba(255,255,255,.1);
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  color: #e2e8f0;
  transition: background .2s,border-color .2s,transform .15s;
  overflow: hidden;
}

.ab-19__arrow:hover:not(.is-disabled) {
  background: #334155;
  border-color: rgba(99,102,241,.5);
  transform: scale(1.06);
}

.ab-19__arrow.is-disabled {
  opacity: .35;
  cursor: not-allowed;
}

.ab-19__arrow-inner {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 24px;
  height: 24px;
  overflow: hidden;
}

.ab-19__icon {
  position: absolute;
  width: 22px;
  height: 22px;
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.ab-19__icon--ghost {
  opacity: 0;
  pointer-events: none;
}
/* next arrow hover */

.ab-19__arrow--next:hover:not(.is-disabled) .ab-19__icon:not(.ab-19__icon--ghost) {
  transform: translateX(120%);
}

.ab-19__arrow--next .ab-19__icon--ghost {
  transform: translateX(-120%);
  opacity: 1;
}

.ab-19__arrow--next:hover:not(.is-disabled) .ab-19__icon--ghost {
  transform: translateX(0);
}
/* prev arrow hover */

.ab-19__arrow--prev:hover:not(.is-disabled) .ab-19__icon:not(.ab-19__icon--ghost) {
  transform: translateX(-120%);
}

.ab-19__arrow--prev .ab-19__icon--ghost {
  transform: translateX(120%);
  opacity: 1;
}

.ab-19__arrow--prev:hover:not(.is-disabled) .ab-19__icon--ghost {
  transform: translateX(0);
}

@media (prefers-reduced-motion: reduce) {
  .ab-19__icon,
    .ab-19__counter {
    transition: none;
  }

  .ab-19__counter.tick {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var prev=document.getElementById('ab-19-prev');
  var next=document.getElementById('ab-19-next');
  var counter=document.getElementById('ab-19-counter');
  var slide=document.getElementById('ab-19-slide');
  if(!prev||!next||!counter||!slide)return;
  var TOTAL=5;
  var idx=0;
  var TITLES=['Effortless Deployment','Instant Scaling','Built-in Observability','Zero Config Security','Global Edge Network'];
  var BODIES=[
    'Push your code and watch it go live in seconds. Zero config, zero downtime.',
    'Handle millions of requests without touching infrastructure settings.',
    'Real-time logs, traces, and metrics out of the box.',
    'Automatic TLS, DDoS protection, and secrets management included.',
    'Your app served from 300+ PoPs worldwide, under 20ms latency.'
  ];
  function pad(n){return n<10?'0'+n:String(n)}
  function update(){
    slide.querySelector('.ab-19__slide-label').textContent='Slide '+(idx+1)+' of '+TOTAL;
    slide.querySelector('.ab-19__slide-title').textContent=TITLES[idx];
    slide.querySelector('.ab-19__slide-body').textContent=BODIES[idx];
    counter.textContent=pad(idx+1)+' / '+pad(TOTAL);
    counter.classList.remove('tick');
    void counter.offsetWidth;
    counter.classList.add('tick');
    prev.classList.toggle('is-disabled',idx===0);
    next.classList.toggle('is-disabled',idx===TOTAL-1);
  }
  prev.addEventListener('click',function(){if(idx>0){idx--;update()}});
  next.addEventListener('click',function(){if(idx<TOTAL-1){idx++;update()}});
})();
```
