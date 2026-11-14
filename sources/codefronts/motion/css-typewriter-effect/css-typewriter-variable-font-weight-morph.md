---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-variable-font-weight-morph/"
title: "CSS Typewriter Variable Font Weight Morph"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "Each character of a variable font headline morphs from ultra-light to black weight as it \"types in\", using staggered font-variation-settings animations — no…"
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Variable Font Weight Morph
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-variable-font-weight-morph/

Each character of a variable font headline morphs from ultra-light to black weight as it "types in", using staggered font-variation-settings animations — no width tricks required.
## HTML
```html
<div class="tw-08">
  <div class="tw-08__stage">
    <p class="tw-08__pre">Variable font axis animation</p>
    <h1 class="tw-08__word" aria-label="EVOLVE">
      <span style="--i:0">E</span>
      <span style="--i:1">V</span>
      <span style="--i:2">O</span>
      <span style="--i:3">L</span>
      <span style="--i:4">V</span>
      <span style="--i:5">E</span>
    </h1>
    <p class="tw-08__post">font-variation-settings "wght" morph</p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:[email protected]&display=swap');

.tw-08,
.tw-08 *,
.tw-08 *::before,
.tw-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-08 ::selection {
  background: #f59e0b;
  color: #1a0e00;
}

.tw-08 {
  --amber: #f59e0b;
  --gold: #fcd34d;
  --bg: #0d0900;
  font-family: 'Inter', system-ui, sans-serif;
  background: radial-gradient(ellipse at 50% 40%, #1a1000 0%, var(--bg) 65%);
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tw-08__stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.tw-08__pre,
.tw-08__post {
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #4a3500;
  animation: tw-08-fadein 0.5s 0.2s both;
}

.tw-08__word {
  display: flex;
  gap: 0.02em;
  font-size: clamp(3rem, 12vw, 7rem);
  line-height: 1;
}

.tw-08__word span {
  display: inline-block;
  opacity: 0;
  font-variation-settings: 'wght' 100;
  color: var(--amber);
  letter-spacing: 0.05em;
  text-shadow: 0 0 0px transparent;
  animation: tw-08-stamp 0.6s cubic-bezier(0.2, 0, 0, 1) calc(var(--i) * 0.12s + 0.5s) both;
}

@keyframes tw-08-stamp {
  0% {
    opacity: 0;
    font-variation-settings: 'wght' 100;
    letter-spacing: 0.3em;
    text-shadow: 0 0 0 transparent;
  }

  60% {
    opacity: 1;
    font-variation-settings: 'wght' 950;
    letter-spacing: -0.02em;
    text-shadow: 0 0 30px rgba(245,158,11,0.6);
  }

  100% {
    opacity: 1;
    font-variation-settings: 'wght' 700;
    letter-spacing: 0.02em;
    text-shadow: 0 0 8px rgba(245,158,11,0.2);
  }
}

@keyframes tw-08-fadein {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-08__word span {
    opacity: 1;
    font-variation-settings: 'wght' 700;
    letter-spacing: 0.02em;
    animation: none;
  }
}
```
