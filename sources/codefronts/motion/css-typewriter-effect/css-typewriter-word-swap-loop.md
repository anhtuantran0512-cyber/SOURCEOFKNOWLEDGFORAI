---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-word-swap-loop/"
title: "CSS Typewriter Word Swap Loop"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "A hero headline cycles through swappable highlight words using a single CSS keyframe that animates width and color on a looping overflow-hidden container."
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Word Swap Loop
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-word-swap-loop/

A hero headline cycles through swappable highlight words using a single CSS keyframe that animates width and color on a looping overflow-hidden container.
## HTML
```html
<div class="tw-03">
  <div class="tw-03__hero">
    <h1 class="tw-03__headline">
      We design
      <span class="tw-03__slot">
        <span class="tw-03__words">
          <span>websites</span>
          <span>products</span>
          <span>systems</span>
          <span>futures</span>
          <span>websites</span>
        </span>
      </span>
    </h1>
    <p class="tw-03__sub">Digital craftsmanship for ambitious brands.</p>
  </div>
</div>
```
## CSS
```css
.tw-03,
.tw-03 *,
.tw-03 *::before,
.tw-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-03 ::selection {
  background: #f97316;
  color: #1a0800;
}

.tw-03 {
  --orange: #f97316;
  --amber: #fbbf24;
  --bg: #0c0802;
  --text: #fef3c7;
  --muted: #92400e;
  font-family: 'Georgia', serif;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.tw-03__hero {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.tw-03__headline {
  font-size: clamp(1.8rem, 5vw, 3.2rem);
  color: var(--text);
  font-weight: 300;
  line-height: 1.3;
  display: flex;
  align-items: baseline;
  gap: 0.3em;
  flex-wrap: wrap;
  justify-content: center;
}

.tw-03__slot {
  display: inline-block;
  overflow: hidden;
  height: 1.2em;
  vertical-align: bottom;
  border-right: 3px solid var(--orange);
  background: linear-gradient(135deg, rgba(249,115,22,0.15), rgba(251,191,36,0.08));
  border-radius: 4px;
  padding: 0 6px;
  animation: tw-03-width 8s steps(1) infinite, tw-03-blink 0.65s steps(2) infinite;
}

.tw-03__words {
  display: flex;
  flex-direction: column;
  animation: tw-03-scroll 8s steps(4) infinite;
}

.tw-03__words span {
  font-style: italic;
  font-weight: 600;
  color: var(--orange);
  flex-shrink: 0;
  height: 1.2em;
  line-height: 1.2;
  white-space: nowrap;
}

.tw-03__sub {
  font-size: 1rem;
  color: var(--muted);
  letter-spacing: 0.05em;
}

@keyframes tw-03-scroll {
  0% {
    transform: translateY(0);
  }

  25% {
    transform: translateY(-1.2em);
  }

  50% {
    transform: translateY(-2.4em);
  }

  75% {
    transform: translateY(-3.6em);
  }

  100% {
    transform: translateY(0);
  }
}

@keyframes tw-03-width {
  0%,
    100% {
    width: 7.5ch;
  }

  25% {
    width: 8ch;
  }

  50% {
    width: 7.5ch;
  }

  75% {
    width: 7.5ch;
  }
}

@keyframes tw-03-blink {
  0%,
    100% {
    border-color: var(--orange);
  }

  50% {
    border-color: transparent;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-03__slot {
    animation: none;
    border-right-color: var(--orange);
  }

  .tw-03__words {
    animation: none;
  }
}
```
