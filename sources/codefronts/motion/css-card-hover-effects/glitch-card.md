---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/glitch-card/"
title: "Glitch Card"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "An event/music card with RGB channel-split text, datamosh slice bars, and stepped jitter animation on hover."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Card
Source: https://codefronts.com/motion/css-card-hover-effects/glitch-card/

An event/music card with RGB channel-split text, datamosh slice bars, and stepped jitter animation on hover. Built for cyberpunk, electronic music, gaming, and edgy brands that want controlled digital chaos.
## HTML
```html
<div class="card-20">
  <article class="card-20__card">
    <div class="card-20__bars"></div>
    <div class="card-20__inner">
      <span class="card-20__tag">// SIGNAL_LOST</span>
      <h2 class="card-20__title">
        <span class="card-20__ghost card-20__ghost-r" aria-hidden="true">NULL<br>CITY</span>
        <span class="card-20__ghost card-20__ghost-c" aria-hidden="true">NULL<br>CITY</span>
        <span class="card-20__real">NULL<br>CITY</span>
      </h2>
      <p class="card-20__desc">A cyberpunk audio-visual set. Corrupted frames, datamoshed visuals, bass you feel in your teeth.</p>
      <span class="card-20__foot">FRI · WAREHOUSE 7 · 23:00</span>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Space+Mono:wght@400;700&display=swap');

.card-20,
.card-20 *,
.card-20 *::before,
.card-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-20 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #08080a;
  font-family: 'Space Mono', monospace;
  padding: 2rem;
}

.card-20__card {
  position: relative;
  width: 340px;
  height: 440px;
  border-radius: 4px;
  background: #0f0f12;
  cursor: pointer;
  overflow: hidden;
  border: 1px solid #1c1c22;
}

.card-20__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #e8e8ee;
}

.card-20__tag {
  font-size: 0.72rem;
  letter-spacing: 0.25em;
  color: #00e0ff;
}

.card-20__title {
  font-family: 'Anton', sans-serif;
  font-size: 4rem;
  line-height: 0.85;
  text-transform: uppercase;
  position: relative;
  color: #fff;
  display: inline-block;
}

.card-20__ghost {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.card-20__ghost.card-20__ghost-r {
  color: #ff003c;
}

.card-20__ghost.card-20__ghost-c {
  color: #00e0ff;
}

.card-20__card:hover .card-20__ghost.card-20__ghost-r {
  opacity: 0.85;
  animation: card-20-shift-a 0.35s steps(2) infinite;
}

.card-20__card:hover .card-20__ghost.card-20__ghost-c {
  opacity: 0.85;
  animation: card-20-shift-b 0.35s steps(2) infinite;
}

@keyframes card-20-shift-a {
  0% {
    transform: translate(0,0);
    clip-path: inset(0 0 70% 0);
  }

  50% {
    transform: translate(-4px,2px);
    clip-path: inset(40% 0 20% 0);
  }

  100% {
    transform: translate(3px,-2px);
    clip-path: inset(70% 0 0 0);
  }
}

@keyframes card-20-shift-b {
  0% {
    transform: translate(0,0);
    clip-path: inset(60% 0 10% 0);
  }

  50% {
    transform: translate(4px,-2px);
    clip-path: inset(10% 0 60% 0);
  }

  100% {
    transform: translate(-3px,2px);
    clip-path: inset(30% 0 40% 0);
  }
}

.card-20__real {
  position: relative;
  z-index: 1;
  display: block;
}

.card-20__desc {
  font-size: 0.82rem;
  line-height: 1.6;
  color: #888;
}

.card-20__foot {
  font-size: 0.72rem;
  letter-spacing: 0.15em;
  color: #555;
}

.card-20__bars {
  position: absolute;
  inset: 0;
  z-index: 3;
  pointer-events: none;
  opacity: 0;
}

.card-20__card:hover .card-20__bars {
  opacity: 1;
  animation: card-20-bars 0.4s steps(3) infinite;
}

.card-20__bars::before,
.card-20__bars::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  height: 2px;
  background: rgba(0,224,255,0.5);
}

.card-20__bars::before {
  top: 32%;
}

.card-20__bars::after {
  top: 68%;
  background: rgba(255,0,60,0.5);
}

@keyframes card-20-bars {
  0%,
    100% {
    transform: translateX(0);
  }

  50% {
    transform: translateX(6px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-20__ghost,
    .card-20__bars {
    animation: none !important;
  }
}
```
