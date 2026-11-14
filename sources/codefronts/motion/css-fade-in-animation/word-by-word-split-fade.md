---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/word-by-word-split-fade/"
title: "Word-by-Word Split Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "A headline is split word-by-word into spans via JavaScript, each assigned an animation-delay, creating a sequential typewriter-style word cascade with…"
has_js: "true"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Word-by-Word Split Fade
Source: https://codefronts.com/motion/css-fade-in-animation/word-by-word-split-fade/

A headline is split word-by-word into spans via JavaScript, each assigned an animation-delay, creating a sequential typewriter-style word cascade with translateY spring bounce.
## HTML
```html
<div class="fi-10" id="fi-10-root">
  <div class="fi-10__output">
    <div class="fi-10__label" id="fi-10-label">Word-by-word fade</div>
    <div class="fi-10__text" id="fi-10-text">Words appear one by one creating a cinematic reading experience</div>
    <div class="fi-10__sub" id="fi-10-sub">JavaScript splits text into spans, staggering animation-delay per word index.</div>
    <div class="fi-10__replay" id="fi-10-replay">↺ Replay</div>
  </div>
</div>
```
## CSS
```css
.fi-10 {
  --bg: #0a0f0a;
  --green: #4ade80;
  --lime: #a3e635;
  --text: #f0fdf4;
  font-family: 'Plus Jakarta Sans',sans-serif;
  min-height: 320px;
  border-radius: 20px;
  display: grid;
  place-items: center;
  padding: 40px;
  overflow: hidden;
}

.fi-10 *,
.fi-10 *::before,
.fi-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-10 ::selection {
  background: var(--green);
  color: #000;
}

.fi-10__output {
  text-align: center;
  max-width: 560px;
}

.fi-10__label {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--green);
  margin-bottom: 20px;
  opacity: 0;
  animation: fi-10-word-fade .5s ease forwards .1s;
}

.fi-10__text {
  font-size: clamp(1.4rem,3.5vw,2.2rem);
  font-weight: 800;
  line-height: 1.4;
  color: var(--text);
  margin-bottom: 24px;
}
/* JS injects spans; each span animates individually */

.fi-10__word {
  display: inline-block;
  margin-right: .3em;
  opacity: 0;
  transform: translateY(12px);
  animation: fi-10-word-up .5s cubic-bezier(.16,1,.3,1) forwards;
}

.fi-10__sub {
  font-size: .9rem;
  color: rgba(240,253,244,.45);
  line-height: 1.6;
  opacity: 0;
  animation: fi-10-word-fade .5s ease forwards;
}

.fi-10__replay {
  margin-top: 20px;
  display: inline-block;
  font-size: .75rem;
  font-weight: 600;
  color: var(--green);
  cursor: pointer;
  border: 1px solid rgba(74,222,128,.2);
  border-radius: 20px;
  padding: 6px 16px;
  background: rgba(74,222,128,.08);
  transition: background .2s;
}

.fi-10__replay:hover {
  background: rgba(74,222,128,.15);
}

@keyframes fi-10-word-up {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fi-10-word-fade {
  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-10 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  const textEl = document.getElementById('fi-10-text');
  const subEl  = document.getElementById('fi-10-sub');
  const replay = document.getElementById('fi-10-replay');
  const BASE_DELAY = 0.3;
  const STEP = 0.09;

  function splitAndAnimate(el, startDelay){
    const words = el.textContent.trim().split(/\s+/);
    el.innerHTML = '';
    words.forEach((w,i)=>{
      const span = document.createElement('span');
      span.className='fi-10__word';
      span.textContent = w;
      span.style.animationDelay = (startDelay + i * STEP)+'s';
      el.appendChild(span);
    });
    return startDelay + words.length * STEP;
  }

  function run(){
    const subDelay = splitAndAnimate(textEl, BASE_DELAY);
    subEl.style.animationDelay = (subDelay + 0.1)+'s';
    subEl.style.animation='none';
    void subEl.offsetWidth;
    subEl.style.animation='fi-10-word-fade .5s ease forwards';
  }

  run();

  replay.addEventListener('click',()=>{
    // Reset and re-animate
    textEl.querySelectorAll('.fi-10__word').forEach(s=>{
      s.style.animation='none';
      void s.offsetWidth;
      s.style.animation='fi-10-word-up .5s cubic-bezier(.16,1,.3,1) forwards';
    });
    subEl.style.animation='none';
    void subEl.offsetWidth;
    subEl.style.animation='fi-10-word-fade .5s ease forwards';
  });
})();
```
