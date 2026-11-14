---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/cascade-letter-drop-fade/"
title: "Cascade Letter Drop Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "JavaScript splits a headline character-by-character into spans with staggered animation-delay; each letter drops in from above with a spring bounce, creating…"
has_js: "true"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cascade Letter Drop Fade
Source: https://codefronts.com/motion/css-fade-in-animation/cascade-letter-drop-fade/

JavaScript splits a headline character-by-character into spans with staggered animation-delay; each letter drops in from above with a spring bounce, creating a raindrop cascade.
## HTML
```html
<div class="fi-16" id="fi-16-root">
  <div>
    <div class="fi-16__label">Letter cascade</div>
    <span class="fi-16__title" id="fi-16-title">Cascade Letters</span>
    <p class="fi-16__sub" id="fi-16-sub" style="animation-delay:1.4s">JavaScript splits every character into a span with a staggered animation-delay, creating a raindrop-style letter cascade.</p>
    <div class="fi-16__row" id="fi-16-row" style="animation-delay:1.7s">
      <span class="fi-16__chip">JS split</span>
      <span class="fi-16__chip">nth-child delay</span>
      <span class="fi-16__chip">spring bounce</span>
    </div>
    <div class="fi-16__replay" id="fi-16-replay" style="animation-delay:1.9s">↺ replay animation</div>
  </div>
</div>
```
## CSS
```css
.fi-16 {
  --bg: #090b14;
  --gold: #f59e0b;
  --amber: #fbbf24;
  --text: #fffbeb;
  font-family: 'DM Sans',sans-serif;
  min-height: 340px;
  border-radius: 20px;
  display: grid;
  place-items: center;
  padding: 40px;
  overflow: hidden;
  text-align: center;
}

.fi-16 *,
.fi-16 *::before,
.fi-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-16 ::selection {
  background: var(--gold);
  color: #000;
}

.fi-16__label {
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(255,251,235,.35);
  margin-bottom: 20px;
}

.fi-16__title {
  font-family: 'Syne',sans-serif;
  font-size: clamp(1.8rem,4vw,3rem);
  font-weight: 800;
  color: var(--text);
  line-height: 1.2;
  margin-bottom: 16px;
  display: block;
}
/* JS injects letter spans */

.fi-16__letter {
  display: inline-block;
  opacity: 0;
  transform: translateY(-20px) rotate(-8deg);
  animation: fi-16-letter-drop .5s cubic-bezier(.34,1.56,.64,1) forwards;
}

.fi-16__letter.fi-16--space {
  margin-right: .35em;
}

.fi-16__sub {
  font-size: .95rem;
  color: rgba(255,251,235,.45);
  line-height: 1.6;
  max-width: 400px;
  margin-bottom: 28px;
  opacity: 0;
  animation: fi-16-fade-up .6s ease forwards;
}

.fi-16__row {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
  opacity: 0;
  animation: fi-16-fade-up .5s ease forwards;
}

.fi-16__chip {
  padding: 7px 16px;
  border-radius: 20px;
  font-size: .75rem;
  font-weight: 700;
  background: rgba(245,158,11,.12);
  border: 1px solid rgba(245,158,11,.25);
  color: var(--gold);
  transition: background .2s,transform .2s;
  cursor: default;
}

.fi-16__chip:hover {
  background: rgba(245,158,11,.22);
  transform: translateY(-2px);
}

.fi-16__replay {
  margin-top: 18px;
  display: inline-block;
  font-size: .72rem;
  font-weight: 600;
  color: rgba(255,251,235,.35);
  cursor: pointer;
  border-bottom: 1px dashed rgba(255,255,255,.15);
  padding-bottom: 2px;
  transition: color .2s;
  opacity: 0;
  animation: fi-16-fade-up .5s ease forwards;
}

.fi-16__replay:hover {
  color: var(--gold);
}

@keyframes fi-16-letter-drop {
  to {
    opacity: 1;
    transform: translateY(0) rotate(0deg);
  }
}

@keyframes fi-16-fade-up {
  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-16 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  const titleEl = document.getElementById('fi-16-title');
  const replay  = document.getElementById('fi-16-replay');
  const STEP = 0.05;

  function animate(){
    const text = 'Cascade Letters';
    titleEl.innerHTML = '';
    [...text].forEach((ch, i)=>{
      const span = document.createElement('span');
      span.className = 'fi-16__letter' + (ch === ' ' ? ' fi-16--space' : '');
      span.textContent = ch === ' ' ? '\u00a0' : ch;
      span.style.animationDelay = (0.1 + i * STEP)+'s';
      titleEl.appendChild(span);
    });
  }

  animate();

  replay.addEventListener('click',()=>{
    titleEl.querySelectorAll('.fi-16__letter').forEach(s=>{
      s.style.animation='none';void s.offsetWidth;
      s.style.animation='fi-16-letter-drop .5s cubic-bezier(.34,1.56,.64,1) forwards';
    });
  });
})();
```
