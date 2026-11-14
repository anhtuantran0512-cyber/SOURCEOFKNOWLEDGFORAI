---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/shockwave/"
title: "Shockwave"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "An energy/tech card that fires concentric ripple rings outward from the exact point where the cursor enters, with staggered colored waves."
has_js: "true"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shockwave
Source: https://codefronts.com/motion/css-card-hover-effects/shockwave/

An energy/tech card that fires concentric ripple rings outward from the exact point where the cursor enters, with staggered colored waves. Best for power, audio, gaming, and CTA cards that should feel reactive and kinetic.
## HTML
```html
<div class="card-29">
  <article class="card-29__card" data-card-29="root">
    <div class="card-29__inner">
      <span class="card-29__tag">// Energy Core</span>
      <h2 class="card-29__title">Pulse<br>Reactor</h2>
      <p class="card-29__desc">Every interaction sends a wave outward. Hover anywhere — the ripple starts where you enter.</p>
      <span class="card-29__btn">Discharge ⚡</span>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;700&family=Inter:wght@400;500&display=swap');

.card-29,
.card-29 *,
.card-29 *::before,
.card-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-29 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #07101a;
  font-family: 'Inter', sans-serif;
  padding: 2rem;
}

.card-29__card {
  --card-29-x: 50%;
  --card-29-y: 50%;
  position: relative;
  width: 340px;
  height: 440px;
  border-radius: 18px;
  cursor: pointer;
  overflow: hidden;
  background: radial-gradient(circle at 50% 40%, #0e2236, #060d16);
  border: 1px solid rgba(60,180,255,0.18);
}

.card-29__card::before {
  content: "";
  position: absolute;
  top: var(--card-29-y);
  left: var(--card-29-x);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  transform: translate(-50%, -50%) scale(0);
  border: 2px solid rgba(80,200,255,0.7);
  box-shadow: 0 0 30px rgba(80,200,255,0.5);
  z-index: 1;
}

.card-29__card:hover::before {
  animation: card-29-ring 0.9s cubic-bezier(0.2,0.6,0.3,1) forwards;
}

@keyframes card-29-ring {
  0% {
    transform: translate(-50%,-50%) scale(0);
    opacity: 0.9;
  }

  100% {
    transform: translate(-50%,-50%) scale(60);
    opacity: 0;
  }
}

.card-29__card::after {
  content: "";
  position: absolute;
  top: var(--card-29-y);
  left: var(--card-29-x);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  transform: translate(-50%, -50%) scale(0);
  border: 1px solid rgba(160,90,255,0.6);
  z-index: 1;
}

.card-29__card:hover::after {
  animation: card-29-ring 1.1s cubic-bezier(0.2,0.6,0.3,1) 0.12s forwards;
}

.card-29__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #dceaf7;
}

.card-29__tag {
  font-family: 'Chakra Petch', sans-serif;
  font-size: 0.72rem;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: #4fc3ff;
}

.card-29__title {
  font-family: 'Chakra Petch', sans-serif;
  font-weight: 700;
  font-size: 2.6rem;
  line-height: 0.95;
}

.card-29__desc {
  font-size: 0.86rem;
  line-height: 1.6;
  color: #8fa6bb;
}

.card-29__btn {
  align-self: flex-start;
  font-family: 'Chakra Petch', sans-serif;
  font-size: 0.85rem;
  letter-spacing: 0.06em;
  padding: 0.7rem 1.5rem;
  border-radius: 8px;
  border: 1px solid rgba(80,200,255,0.4);
  color: #4fc3ff;
  background: rgba(80,200,255,0.08);
  transition: background 0.3s ease;
}

.card-29__card:hover .card-29__btn {
  background: rgba(80,200,255,0.18);
}

@media (prefers-reduced-motion: reduce) {
  .card-29__card::before,
    .card-29__card::after {
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.card-29');
  if (!root) return;
  const c = root.querySelector('[data-card-29="root"]');
  if (!c) return;
  c.addEventListener('mouseenter', (e) => {
    const r = c.getBoundingClientRect();
    c.style.setProperty('--card-29-x', `${e.clientX - r.left}px`);
    c.style.setProperty('--card-29-y', `${e.clientY - r.top}px`);
  });
})();
```
