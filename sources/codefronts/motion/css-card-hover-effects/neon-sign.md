---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/neon-sign/"
title: "Neon Sign"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A bar/nightlife card on a dim brick wall where the sign text ignites into a flickering neon glow on hover using layered text-shadows."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Sign
Source: https://codefronts.com/motion/css-card-hover-effects/neon-sign/

A bar/nightlife card on a dim brick wall where the sign text ignites into a flickering neon glow on hover using layered text-shadows. Suited to restaurants, bars, music venues, and any brand with after-dark personality.
## HTML
```html
<div class="card-13">
  <article class="card-13__card">
    <div class="card-13__inner">
      <span class="card-13__open">— open till late —</span>
      <h2 class="card-13__title">Lola's</h2>
      <p class="card-13__sub">cocktail bar</p>
      <p class="card-13__desc">Hover to light the sign. Hand-bent tubes, mezcal flights, and a back room you have to ask about.</p>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Monoton&family=Major+Mono+Display&family=Oxanium:wght@400;600&display=swap');

.card-13,
.card-13 *,
.card-13 *::before,
.card-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-13 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 50% 120%, #1a1430 0%, #050308 70%);
  font-family: 'Oxanium', sans-serif;
  padding: 2rem;
}

.card-13__card {
  --card-13-c1: #ff2d95;
  --card-13-c2: #29f5ff;
  position: relative;
  width: 330px;
  height: 430px;
  border-radius: 16px;
  background: #0a0712;
  cursor: pointer;
  overflow: hidden;
  border: 2px solid rgba(255,255,255,0.04);
  transition: box-shadow 0.5s ease;
}

.card-13__card:hover {
  box-shadow: 0 0 50px rgba(255,45,149,0.25);
}

.card-13__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(10,7,18,0.85), rgba(10,7,18,0.92)), repeating-linear-gradient(0deg, #181020 0 24px, transparent 24px 26px), repeating-linear-gradient(90deg, #181020 0 48px, transparent 48px 50px);
  opacity: 0.7;
}

.card-13__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  text-align: center;
}

.card-13__open {
  font-family: 'Major Mono Display', monospace;
  font-size: 0.85rem;
  letter-spacing: 0.3em;
  color: var(--card-13-c2);
  opacity: 0.4;
  transition: all 0.4s ease;
}

.card-13__card:hover .card-13__open {
  opacity: 1;
  text-shadow: 0 0 8px var(--card-13-c2), 0 0 18px var(--card-13-c2);
}

.card-13__title {
  font-family: 'Monoton', cursive;
  font-size: 3.4rem;
  line-height: 0.95;
  color: #2a1a35;
  transition: all 0.5s ease;
}

.card-13__card:hover .card-13__title {
  color: var(--card-13-c1);
  text-shadow: 0 0 6px var(--card-13-c1), 0 0 14px var(--card-13-c1), 0 0 30px var(--card-13-c1), 0 0 60px var(--card-13-c1);
  animation: card-13-flicker 3s infinite;
}

@keyframes card-13-flicker {
  0%,
    18%,
    22%,
    25%,
    53%,
    57%,
    100% {
    text-shadow: 0 0 6px var(--card-13-c1), 0 0 14px var(--card-13-c1), 0 0 30px var(--card-13-c1), 0 0 60px var(--card-13-c1);
    opacity: 1;
  }

  20%,
    24%,
    55% {
    text-shadow: none;
    opacity: 0.6;
  }
}

.card-13__desc {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #8a7a9a;
  max-width: 90%;
}

.card-13__sub {
  font-family: 'Major Mono Display', monospace;
  font-size: 1.1rem;
  color: #2a1a35;
  transition: all 0.5s ease 0.1s;
}

.card-13__card:hover .card-13__sub {
  color: var(--card-13-c2);
  text-shadow: 0 0 6px var(--card-13-c2), 0 0 16px var(--card-13-c2);
}

@media (prefers-reduced-motion: reduce) {
  .card-13__card:hover .card-13__title {
    animation: none !important;
  }
}
```
