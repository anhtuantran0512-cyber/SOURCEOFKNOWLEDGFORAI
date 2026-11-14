---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/gradient-rotate/"
title: "Gradient Rotate"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A creative-suite card framed by a blurred conic gradient that rotates behind a masked inner panel, leaving a glowing animated ring."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Rotate
Source: https://codefronts.com/motion/css-card-hover-effects/gradient-rotate/

A creative-suite card framed by a blurred conic gradient that rotates behind a masked inner panel, leaving a glowing animated ring. Great for AI tools, creative apps, and SaaS landing cards needing an energetic, "alive" aura.
## HTML
```html
<div class="card-21">
  <article class="card-21__card">
    <div class="card-21__inner">
      <span class="card-21__eyebrow">AI · CREATIVE SUITE</span>
      <h2 class="card-21__title">Spectra<br>Studio</h2>
      <p class="card-21__desc">Generate, remix, and color-grade in one canvas. The aura rotates while the engine warms up.</p>
      <span class="card-21__cta">→ START FREE TRIAL</span>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&family=Azeret+Mono:wght@400;500&display=swap');

@property --card-21-gr {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.card-21,
.card-21 *,
.card-21 *::before,
.card-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-21 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #0a0a0f;
  font-family: 'Outfit', sans-serif;
  padding: 2rem;
}

.card-21__card {
  position: relative;
  width: 330px;
  height: 430px;
  border-radius: 24px;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
  background: #111118;
}

.card-21__card::before {
  content: "";
  position: absolute;
  inset: -40%;
  z-index: 0;
  background: conic-gradient(
      from var(--card-21-gr),
      #ff4d6d, #ffa64d, #ffe14d, #4dffa6, #4dd2ff, #b04dff, #ff4d6d
    );
  filter: blur(40px) saturate(1.2);
  opacity: 0.65;
  transition: opacity 0.5s ease;
  animation: card-21-spin 6s linear infinite paused;
}

@keyframes card-21-spin {
  to {
    --card-21-gr: 360deg;
  }
}

.card-21__card:hover::before {
  opacity: 1;
  animation-play-state: running;
}

.card-21__card::after {
  content: "";
  position: absolute;
  inset: 2px;
  z-index: 1;
  border-radius: 22px;
  background: linear-gradient(160deg, #15151e, #0c0c12);
}

.card-21__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #f2f2f7;
}

.card-21__eyebrow {
  font-family: 'Azeret Mono', monospace;
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  color: #9a9ab0;
}

.card-21__title {
  font-weight: 700;
  font-size: 2.6rem;
  line-height: 1;
  background: linear-gradient(120deg, #ff8aa0, #ffd24d, #6ad6ff);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-21__desc {
  font-size: 0.88rem;
  line-height: 1.6;
  color: #a6a6bc;
  font-weight: 300;
}

.card-21__cta {
  font-family: 'Azeret Mono', monospace;
  font-size: 0.78rem;
  letter-spacing: 0.1em;
  color: #ffd24d;
}

@media (prefers-reduced-motion: reduce) {
  .card-21__card::before {
    animation: none !important;
  }
}
```
