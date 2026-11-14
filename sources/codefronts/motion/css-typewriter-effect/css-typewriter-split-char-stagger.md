---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-split-char-stagger/"
title: "CSS Typewriter Split Char Stagger"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "Individual characters pop in sequentially using staggered translateY + opacity keyframes, creating a kinetic editorial type-in effect used in modern agency…"
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Split Char Stagger
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-split-char-stagger/

Individual characters pop in sequentially using staggered translateY + opacity keyframes, creating a kinetic editorial type-in effect used in modern agency hero sections.
## HTML
```html
<div class="tw-09">
  <div class="tw-09__canvas">
    <div class="tw-09__kicker">New collection 2025</div>
    <h1 class="tw-09__headline" aria-label="MOTION">
      <span class="tw-09__char" style="--i:0"><span>M</span></span>
      <span class="tw-09__char" style="--i:1"><span>O</span></span>
      <span class="tw-09__char" style="--i:2"><span>T</span></span>
      <span class="tw-09__char" style="--i:3"><span>I</span></span>
      <span class="tw-09__char" style="--i:4"><span>O</span></span>
      <span class="tw-09__char" style="--i:5"><span>N</span></span>
    </h1>
    <p class="tw-09__sub" aria-label="Design Studio">
      <span class="tw-09__word" style="--i:6"><span>Design</span></span>
      <span class="tw-09__word" style="--i:10"><span>Studio</span></span>
    </p>
  </div>
</div>
```
## CSS
```css
.tw-09,
.tw-09 *,
.tw-09 *::before,
.tw-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-09 ::selection {
  background: #10b981;
  color: #001a10;
}

.tw-09 {
  --green: #10b981;
  --emerald: #34d399;
  --bg: #020e09;
  --text: #ecfdf5;
  font-family: 'Georgia', serif;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tw-09__canvas {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.tw-09__kicker {
  font-size: 0.72rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--green);
  opacity: 0;
  animation: tw-09-fade 0.4s 0.1s both;
}

.tw-09__headline {
  display: flex;
  font-size: clamp(3.5rem, 14vw, 8rem);
  font-weight: 700;
  line-height: 1;
  gap: 0;
  letter-spacing: -0.03em;
}

.tw-09__char {
  display: inline-block;
  overflow: hidden;
  padding-bottom: 0.1em;
}

.tw-09__char > span,
.tw-09__word > span {
  display: inline-block;
  color: var(--text);
  opacity: 0;
  transform: translateY(0.8em);
  animation: tw-09-up 0.7s cubic-bezier(0.16, 1, 0.3, 1) calc(var(--i) * 0.05s + 0.2s) both;
}

.tw-09__sub {
  display: flex;
  gap: 0.5em;
  font-size: 1.1rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  font-style: italic;
  color: var(--green);
  overflow: hidden;
}

.tw-09__word {
  display: inline-block;
  overflow: hidden;
}

@keyframes tw-09-up {
  from {
    opacity: 0;
    transform: translateY(0.8em);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes tw-09-fade {
  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-09__char > span,
    .tw-09__word > span {
    opacity: 1;
    transform: none;
    animation: none;
  }

  .tw-09__kicker {
    opacity: 1;
    animation: none;
  }
}
```
