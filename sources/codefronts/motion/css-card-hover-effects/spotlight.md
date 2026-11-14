---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/spotlight/"
title: "Spotlight"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A minimalist case-study card where a soft light and a matching border highlight follow the cursor across a dark surface."
has_js: "true"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Spotlight
Source: https://codefronts.com/motion/css-card-hover-effects/spotlight/

A minimalist case-study card where a soft light and a matching border highlight follow the cursor across a dark surface. The restraint makes it ideal for design studios, agencies, and premium editorial content that values calm sophistication.
## HTML
```html
<div class="card-16">
  <article class="card-16__card" data-card-16="root">
    <div class="card-16__inner">
      <div class="card-16__row">
        <span>CASE STUDY</span>
        <span>2025</span>
      </div>
      <h2 class="card-16__title">Quiet<br><em>Interfaces</em></h2>
      <p class="card-16__desc">A design system built on restraint. The light follows you because attention should follow intent.</p>
      <span class="card-16__foot">— READ THE ESSAY</span>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist+Mono:wght@400;500&display=swap');

.card-16,
.card-16 *,
.card-16 *::before,
.card-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-16 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #08080a;
  font-family: 'Geist Mono', monospace;
  padding: 2rem;
}

.card-16__card {
  --card-16-x: 50%;
  --card-16-y: 50%;
  position: relative;
  width: 340px;
  height: 440px;
  border-radius: 18px;
  background: #101014;
  cursor: pointer;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.06);
}

.card-16__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(
      300px circle at var(--card-16-x) var(--card-16-y),
      rgba(120, 200, 255, 0.18),
      transparent 60%
    );
  opacity: 0;
  transition: opacity 0.4s ease;
  z-index: 1;
}

.card-16__card:hover::before {
  opacity: 1;
}

.card-16__card::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: radial-gradient(
      250px circle at var(--card-16-x) var(--card-16-y),
      rgba(120,200,255,0.6),
      transparent 50%
    );
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.4s ease;
  z-index: 2;
}

.card-16__card:hover::after {
  opacity: 1;
}

.card-16__inner {
  position: relative;
  z-index: 3;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #d7dbe2;
}

.card-16__row {
  display: flex;
  justify-content: space-between;
  font-size: 0.72rem;
  letter-spacing: 0.1em;
  color: #6a7080;
}

.card-16__title {
  font-family: 'Instrument Serif', serif;
  font-size: 3.4rem;
  line-height: 0.95;
  color: #f3f5f9;
}

.card-16__title em {
  color: #78c8ff;
}

.card-16__desc {
  font-size: 0.82rem;
  line-height: 1.65;
  color: #8e94a3;
}

.card-16__foot {
  font-size: 0.72rem;
  color: #6a7080;
  letter-spacing: 0.12em;
}

@media (prefers-reduced-motion: reduce) {
  .card-16__card::before,
    .card-16__card::after {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.card-16');
  if (!root) return;
  const c = root.querySelector('[data-card-16="root"]');
  if (!c) return;
  c.addEventListener('mousemove', (e) => {
    const r = c.getBoundingClientRect();
    c.style.setProperty('--card-16-x', `${e.clientX - r.left}px`);
    c.style.setProperty('--card-16-y', `${e.clientY - r.top}px`);
  });
})();
```
