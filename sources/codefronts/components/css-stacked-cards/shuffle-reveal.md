---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/shuffle-reveal/"
title: "Shuffle Reveal"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "An eye-catching loop where cards rapidly swap depth layers and translate in and out, mimicking a deck being shuffled by hand."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shuffle Reveal
Source: https://codefronts.com/components/css-stacked-cards/shuffle-reveal/

An eye-catching loop where cards rapidly swap depth layers and translate in and out, mimicking a deck being shuffled by hand. On hover the shuffle pauses and fans the cards so you can actually read them — motion as an invitation.
## HTML
```html
<section class="scd-17" aria-label="Shuffling card deck">
  <div class="scd-17__deck" tabindex="0">
    <div class="scd-17__card" style="--i:0;--c:oklch(0.64 0.16 20)">♦</div>
    <div class="scd-17__card" style="--i:1;--c:oklch(0.66 0.15 150)">♣</div>
    <div class="scd-17__card" style="--i:2;--c:oklch(0.64 0.16 250)">♥</div>
    <div class="scd-17__card" style="--i:3;--c:oklch(0.64 0.16 300)">♠</div>
  </div>
</section>
```
## CSS
```css
.scd-17,
.scd-17 *,
.scd-17 *::before,
.scd-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-17 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #131620;
}

.scd-17__deck {
  position: relative;
  width: 150px;
  height: 200px;
  outline: none;
}

.scd-17__card {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: 52px;
  color: #fff;
  border-radius: 16px;
  background: var(--c);
  box-shadow: 0 16px 32px -16px rgba(0,0,0,.8);
  animation: scd-17-riffle 1.6s ease-in-out infinite;
  animation-delay: calc(var(--i) * -.4s);
}

@keyframes scd-17-riffle {
  0%,
    100% {
    transform: translateX(0) rotate(0);
    z-index: 2;
  }

  25% {
    transform: translateX(70px) rotate(10deg);
    z-index: 5;
  }

  50% {
    transform: translateX(0) rotate(0);
    z-index: 2;
  }

  75% {
    transform: translateX(-70px) rotate(-10deg);
    z-index: 1;
  }
}

.scd-17__deck:hover .scd-17__card,
.scd-17__deck:focus-visible .scd-17__card {
  animation-play-state: paused;
  transform: translateX(calc((var(--i) - 1.5) * 54px)) rotate(calc((var(--i) - 1.5) * 6deg));
}

.scd-17__deck:focus-visible {
  outline: 3px solid oklch(0.66 0.15 150);
  outline-offset: 12px;
  border-radius: 22px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-17__card {
    animation: none;
    transform: translateX(calc((var(--i) - 1.5) * 54px)) rotate(calc((var(--i) - 1.5) * 6deg));
  }
}
```

## JavaScript
```js
/* No JavaScript — every card runs the same riffle keyframe offset by a negative animation-delay; :hover pauses the loop and fans the deck for reading. */
```
