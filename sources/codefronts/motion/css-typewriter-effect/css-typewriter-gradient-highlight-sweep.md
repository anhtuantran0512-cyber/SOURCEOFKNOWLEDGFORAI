---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-gradient-highlight-sweep/"
title: "CSS Typewriter Gradient Highlight Sweep"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "Text is revealed by a travelling gradient mask that sweeps left-to-right, creating a spotlight-highlight typewriter where unread text sits invisible and…"
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Gradient Highlight Sweep
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-gradient-highlight-sweep/

Text is revealed by a travelling gradient mask that sweeps left-to-right, creating a spotlight-highlight typewriter where unread text sits invisible and highlighted text glows into view.
## HTML
```html
<div class="tw-07">
  <div class="tw-07__scene">
    <p class="tw-07__label">INCOMING TRANSMISSION</p>
    <h2 class="tw-07__text" data-text="The future is already here.">The future is already here.</h2>
    <div class="tw-07__bar"></div>
  </div>
</div>
```
## CSS
```css
.tw-07,
.tw-07 *,
.tw-07 *::before,
.tw-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-07 ::selection {
  background: #06b6d4;
  color: #00090f;
}

.tw-07 {
  --cyan: #06b6d4;
  --blue: #3b82f6;
  --bg: #00090f;
  --dim: #0e2830;
  font-family: 'Courier New', monospace;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 32px;
}

.tw-07__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  text-align: center;
  max-width: 560px;
}

.tw-07__label {
  font-size: 0.72rem;
  letter-spacing: 0.3em;
  color: #0e4a5a;
  animation: tw-07-fadein 0.5s 0.3s both;
}

.tw-07__text {
  font-size: clamp(1.6rem, 5vw, 2.6rem);
  font-weight: 700;
  position: relative;
  white-space: nowrap;
  color: var(--dim);
}

.tw-07__text::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  background: linear-gradient(
      90deg,
      transparent 0%,
      var(--cyan) 48%,
      #ffffff 50%,
      transparent 52%,
      transparent 100%
    );
  background-size: 220% 100%;
  background-position: 140% center;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: tw-07-sweep 2.4s steps(26) 0.8s forwards;
}

.tw-07__bar {
  height: 2px;
  width: 0;
  background: linear-gradient(90deg, var(--blue), var(--cyan));
  box-shadow: 0 0 12px var(--cyan);
  animation: tw-07-bar 2.4s steps(26) 0.8s forwards;
  border-radius: 1px;
  align-self: flex-start;
  margin-left: calc(50% - 13ch);
}

@keyframes tw-07-sweep {
  from {
    background-position: 140% center;
  }

  to {
    background-position: -20% center;
  }
}

@keyframes tw-07-bar {
  from {
    width: 0;
  }

  to {
    width: 26ch;
  }
}

@keyframes tw-07-fadein {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-07__text::after {
    background-position: -20% center;
    animation: none;
  }

  .tw-07__bar {
    width: 26ch;
    animation: none;
  }

  .tw-07__label {
    opacity: 1;
    animation: none;
  }
}
```
