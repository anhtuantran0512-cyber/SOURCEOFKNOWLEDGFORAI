---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/minimal-dot-navigation/"
title: "Minimal Dot Navigation"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A swipeable five-slide carousel with dot indicators that expand into a pill on the active slide."
has_js: "true"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Dot Navigation
Source: https://codefronts.com/navigation/css-mobile-navigation/minimal-dot-navigation/

A swipeable five-slide carousel with dot indicators that expand into a pill on the active slide. Supports arrow buttons, dot click, touch swipe, and auto-advance — with CSS transitions handling all visual motion.
## HTML
```html
<div class="mn-12" id="mn-12-root">
  <div class="mn-12__track" id="mn-12-track">
    <div class="mn-12__slide">
      <div class="mn-12__slide-emoji">🚀</div>
      <h2>Launch Your Ideas</h2>
      <p>Build and ship products 10x faster with our streamlined platform.</p>
      <a href="#" class="mn-12__slide-cta">Get Started →</a>
    </div>
    <div class="mn-12__slide">
      <div class="mn-12__slide-emoji">🔐</div>
      <h2>Security First</h2>
      <p>Enterprise-grade encryption and compliance built into every layer.</p>
      <a href="#" class="mn-12__slide-cta">Learn More →</a>
    </div>
    <div class="mn-12__slide">
      <div class="mn-12__slide-emoji">⚡</div>
      <h2>Lightning Fast</h2>
      <p>Sub-100ms response times globally with our edge network.</p>
      <a href="#" class="mn-12__slide-cta">See Benchmarks →</a>
    </div>
    <div class="mn-12__slide">
      <div class="mn-12__slide-emoji">🌍</div>
      <h2>Global Scale</h2>
      <p>Deploy to 32 regions worldwide in a single click.</p>
      <a href="#" class="mn-12__slide-cta">Explore Regions →</a>
    </div>
    <div class="mn-12__slide">
      <div class="mn-12__slide-emoji">💎</div>
      <h2>Premium Support</h2>
      <p>24/7 expert support with guaranteed 1-hour response time.</p>
      <a href="#" class="mn-12__slide-cta">Talk to Us →</a>
    </div>
  </div>

  <div class="mn-12__label">Discover</div>
  <div class="mn-12__counter"><span id="mn-12-curr">1</span> / 5</div>

  <button class="mn-12__arrow mn-12__arrow--prev" id="mn-12-prev">‹</button>
  <button class="mn-12__arrow mn-12__arrow--next" id="mn-12-next">›</button>

  <div class="mn-12__dots" id="mn-12-dots">
    <button class="mn-12__dot is-active" data-i="0"></button>
    <button class="mn-12__dot" data-i="1"></button>
    <button class="mn-12__dot" data-i="2"></button>
    <button class="mn-12__dot" data-i="3"></button>
    <button class="mn-12__dot" data-i="4"></button>
  </div>
</div>

```
## CSS
```css
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #0f0f13;
  font-family: 'Segoe UI', sans-serif;
}

.mn-12 {
  --accent: #6366f1;
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.7);
}
/* Slides */

.mn-12__track {
  display: flex;
  width: 500%;
  height: 100%;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform;
}

.mn-12__slide {
  width: 20%;
  height: 100%;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 40px 36px;
  text-align: center;
  position: relative;
}

.mn-12__slide:nth-child(1) {
  background: linear-gradient(160deg, #1e1b4b 0%, #312e81 100%);
}

.mn-12__slide:nth-child(2) {
  background: linear-gradient(160deg, #0c1446 0%, #1e3a5f 100%);
}

.mn-12__slide:nth-child(3) {
  background: linear-gradient(160deg, #1a0533 0%, #3b0764 100%);
}

.mn-12__slide:nth-child(4) {
  background: linear-gradient(160deg, #0a2e1a 0%, #14532d 100%);
}

.mn-12__slide:nth-child(5) {
  background: linear-gradient(160deg, #2d1606 0%, #7c2d12 100%);
}

.mn-12__slide-emoji {
  font-size: 72px;
  margin-bottom: 24px;
  filter: drop-shadow(0 8px 24px rgba(0,0,0,0.3));
}

.mn-12__slide h2 {
  font-size: 28px;
  font-weight: 700;
  color: #fff;
  letter-spacing: -0.5px;
  margin-bottom: 12px;
  line-height: 1.2;
}

.mn-12__slide p {
  font-size: 14px;
  color: rgba(255,255,255,0.6);
  line-height: 1.7;
  max-width: 280px;
}
/* CTA button */

.mn-12__slide-cta {
  display: inline-block;
  margin-top: 28px;
  background: rgba(255,255,255,0.15);
  color: #fff;
  font-size: 13px;
  font-weight: 600;
  padding: 12px 28px;
  border-radius: 100px;
  text-decoration: none;
  border: 1px solid rgba(255,255,255,0.25);
  transition: background 0.2s;
}

.mn-12__slide-cta:hover {
  background: rgba(255,255,255,0.22);
}
/* Dot navigation */

.mn-12__dots {
  position: absolute;
  bottom: 32px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 8px;
  z-index: 10;
}

.mn-12__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,0.3);
  border: none;
  cursor: pointer;
  padding: 0;
  transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.mn-12__dot.is-active {
  width: 28px;
  border-radius: 4px;
  background: #fff;
}
/* Arrow nav */

.mn-12__arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #fff;
  font-size: 16px;
  transition: background 0.2s;
}

.mn-12__arrow:hover {
  background: rgba(255,255,255,0.22);
}

.mn-12__arrow--prev {
  left: 16px;
}

.mn-12__arrow--next {
  right: 16px;
}
/* Slide counter */

.mn-12__counter {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,0.5);
  letter-spacing: 1px;
}

.mn-12__counter span {
  color: rgba(255,255,255,0.9);
}
/* Top label */

.mn-12__label {
  position: absolute;
  top: 20px;
  left: 20px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.3);
}

@media (prefers-reduced-motion: reduce) {
  .mn-12__track {
    transition: none;
  }

  .mn-12__dot {
    transition: none;
  }
}
```

## JavaScript
```js
(function() {
  const track = document.getElementById('mn-12-track');
  const dots = document.querySelectorAll('.mn-12__dot');
  const counter = document.getElementById('mn-12-curr');
  const total = 5;
  let current = 0;

  function goTo(idx) {
    current = (idx + total) % total;
    track.style.transform = `translateX(-${current * 20}%)`;
    dots.forEach((d, i) => d.classList.toggle('is-active', i === current));
    counter.textContent = current + 1;
  }

  document.getElementById('mn-12-prev').addEventListener('click', () => goTo(current - 1));
  document.getElementById('mn-12-next').addEventListener('click', () => goTo(current + 1));
  dots.forEach(d => d.addEventListener('click', () => goTo(+d.dataset.i)));

  // Touch swipe
  let startX = 0;
  track.addEventListener('touchstart', e => { startX = e.touches[0].clientX; }, { passive: true });
  track.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 50) goTo(current + (dx < 0 ? 1 : -1));
  });

  // Auto-advance
  let timer = setInterval(() => goTo(current + 1), 4000);
  document.getElementById('mn-12-root').addEventListener('touchstart', () => clearInterval(timer));
})();
```
