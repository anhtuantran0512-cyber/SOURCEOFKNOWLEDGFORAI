---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/typewriter-reveal/"
title: "Typewriter Reveal"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A field-journal card that types out its quote line-by-line with a blinking caret on hover, on aged paper with grain."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Typewriter Reveal
Source: https://codefronts.com/motion/css-card-hover-effects/typewriter-reveal/

A field-journal card that types out its quote line-by-line with a blinking caret on hover, on aged paper with grain. Perfect for storytelling, blogs, narrative brands, and editorial content with a literary voice.
## HTML
```html
<div class="card-24">
  <article class="card-24__card">
    <div class="card-24__inner">
      <div class="card-24__meta">Dispatch No. 14 — Field Log</div>
      <h2 class="card-24__title">The Cartographer's<br>Last Letter</h2>
      <p class="card-24__line card-24__l1">They said the river had no end —</p>
      <p class="card-24__line card-24__l2">so I followed it anyway.</p>
      <div class="card-24__foot">— hover to type the entry —</div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=Courier+Prime:wght@400;700&display=swap');

.card-24,
.card-24 *,
.card-24 *::before,
.card-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-24 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #ddd6c7;
  background-image: radial-gradient(circle at 50% 50%, #e8e1d2, #c9c0ad);
  font-family: 'Courier Prime', monospace;
  padding: 2rem;
}

.card-24__card {
  position: relative;
  width: 350px;
  height: 440px;
  border-radius: 4px;
  background: #f7f2e7;
  cursor: pointer;
  overflow: hidden;
  box-shadow: 0 16px 36px rgba(60,50,30,0.25);
  border: 1px solid #d8cfba;
}

.card-24__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(120,100,70,0.06) 0.5px, transparent 0.6px);
  background-size: 4px 4px;
  pointer-events: none;
}

.card-24__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  color: #2c2419;
}

.card-24__meta {
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #8a7a5a;
  border-bottom: 1px solid #d8cfba;
  padding-bottom: 0.8rem;
  margin-bottom: 1.6rem;
}

.card-24__title {
  font-family: 'Special Elite', cursive;
  font-size: 2rem;
  line-height: 1.15;
  margin-bottom: 1.4rem;
  min-height: 4.6rem;
}

.card-24__line {
  font-family: 'Special Elite', cursive;
  font-size: 0.95rem;
  line-height: 1.7;
  white-space: nowrap;
  overflow: hidden;
  width: 0;
  border-right: 2px solid #2c2419;
}

.card-24__card:hover .card-24__line {
  animation: card-24-type 2.2s steps(34) forwards, card-24-caret 0.6s steps(1) infinite;
}

.card-24__card:hover .card-24__line.card-24__l2 {
  animation: card-24-type 1.8s steps(28) 2.2s forwards, card-24-caret 0.6s steps(1) infinite;
  border-right-color: transparent;
}

.card-24__card:hover .card-24__line.card-24__l1 {
  border-right-color: transparent;
}

@keyframes card-24-type {
  to {
    width: 100%;
  }
}

@keyframes card-24-caret {
  50% {
    border-right-color: transparent;
  }
}

.card-24__foot {
  margin-top: auto;
  font-size: 0.75rem;
  color: #8a7a5a;
  letter-spacing: 0.1em;
}

@media (prefers-reduced-motion: reduce) {
  .card-24__card:hover .card-24__line {
    animation: none !important;
  }
}
```
