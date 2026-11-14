---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-scroll-gradient-text-reveal-on-scroll/"
title: "CSS Scroll Gradient Text Reveal on Scroll"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Each section's headline fades in from below with a gradient fill sliding from washed-out to vivid, triggered by IntersectionObserver as the element enters…"
has_js: "true"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Scroll Gradient Text Reveal on Scroll
Source: https://codefronts.com/design-styles/css-gradient-text/css-scroll-gradient-text-reveal-on-scroll/

Each section's headline fades in from below with a gradient fill sliding from washed-out to vivid, triggered by IntersectionObserver as the element enters the viewport.
## HTML
```html
<div class="gt-15">
  <div class="gt-15__top">
    <p class="gt-15__hint">Scroll to reveal gradient text</p>
    <span class="gt-15__arrow">↓</span>
  </div>
  <div class="gt-15__section">
    <div class="gt-15__reveal">DISCOVER</div>
  </div>
  <div class="gt-15__section">
    <div class="gt-15__reveal">YOUR</div>
  </div>
  <div class="gt-15__section">
    <div class="gt-15__reveal">POTENTIAL</div>
  </div>
  <div class="gt-15__section">
    <div class="gt-15__reveal">THROUGH COLOUR</div>
  </div>
</div>
```
## CSS
```css
.gt-15,
.gt-15 *,
.gt-15 *::before,
.gt-15 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-15 {
  --bg: #0c0c0c;
  font-family: 'Syne', sans-serif;
  background: var(--bg);
  min-height: 300vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 2rem;
}

.gt-15__top {
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.gt-15__hint {
  font-size: .8rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #555;
  animation: gt-15-bounce 2s ease-in-out infinite;
}

.gt-15__arrow {
  font-size: 1.5rem;
  color: #444;
  animation: gt-15-bounce 2s ease-in-out infinite .3s;
}

.gt-15__section {
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 900px;
}

.gt-15__reveal {
  font-size: clamp(3rem, 10vw, 7rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: -.01em;
  color: #2a2a2a;
  background: linear-gradient(90deg, #ff6b6b, #ffd93d, #6bcb77, #4d96ff);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  opacity: 0;
  transform: translateY(40px);
  transition: opacity .8s ease, transform .8s ease;
  background-position: 100% center;
}

.gt-15__reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
  background-position: 0% center;
  transition: opacity .8s ease, transform .8s ease, background-position 1.2s ease;
}

.gt-15__reveal:nth-child(1) {
  transition-delay: 0s;
}

.gt-15__reveal:nth-child(2) {
  transition-delay: .1s;
}

@keyframes gt-15-bounce {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(8px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-15__reveal {
    opacity: 1;
    transform: none;
    transition: none;
    background-position: 0% center;
  }

  .gt-15__hint,
    .gt-15__arrow {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const items = document.querySelectorAll('.gt-15 .gt-15__reveal');
  if (!items.length) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('is-visible');
      }
    });
  }, { threshold: 0.3 });
  items.forEach(el => io.observe(el));
})();
```
