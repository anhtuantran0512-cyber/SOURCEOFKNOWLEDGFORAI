---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-clip-path-reveal/"
title: "CSS Typewriter clip-path Reveal"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "Text is revealed character-by-character using an animated clip-path inset that travels left-to-right — giving a hard-edged paint-stroke reveal instead of the…"
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter clip-path Reveal
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-clip-path-reveal/

Text is revealed character-by-character using an animated clip-path inset that travels left-to-right — giving a hard-edged paint-stroke reveal instead of the usual overflow trick.
## HTML
```html
<div class="tw-05">
  <div class="tw-05__stage">
    <div class="tw-05__eyebrow">Award-winning studio</div>
    <h1 class="tw-05__heading">
      <span class="tw-05__line tw-05__line--1">Craft that</span>
      <span class="tw-05__line tw-05__line--2">moves people.</span>
    </h1>
    <div class="tw-05__cursor"></div>
  </div>
</div>
```
## CSS
```css
.tw-05,
.tw-05 *,
.tw-05 *::before,
.tw-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-05 ::selection {
  background: #ec4899;
  color: #1a0010;
}

.tw-05 {
  --pink: #ec4899;
  --rose: #fb7185;
  --bg: #0d0008;
  --text: #fdf2f8;
  --muted: #831843;
  font-family: 'Georgia', 'Times New Roman', serif;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 32px;
}

.tw-05__stage {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 480px;
}

.tw-05__eyebrow {
  font-size: 0.72rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--pink);
  clip-path: inset(0 100% 0 0);
  animation: tw-05-reveal 0.6s steps(1) 0.3s forwards;
}

.tw-05__heading {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.tw-05__line {
  display: block;
  position: relative;
  font-size: clamp(2rem, 6vw, 3.8rem);
  font-weight: 700;
  color: var(--text);
  line-height: 1.1;
  clip-path: inset(0 100% 0 0);
  overflow: hidden;
}

.tw-05__line::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, var(--pink), var(--rose));
  opacity: 0.25;
  clip-path: inset(0 100% 0 0);
}

.tw-05__line--1 {
  animation: tw-05-reveal 0.9s steps(10) 0.8s forwards;
}

.tw-05__line--1::before {
  animation: tw-05-reveal 0.9s steps(10) 0.6s forwards;
}

.tw-05__line--2 {
  animation: tw-05-reveal 1.1s steps(13) 2s forwards;
}

.tw-05__line--2::before {
  animation: tw-05-reveal 1.1s steps(13) 1.8s forwards;
}

.tw-05__cursor {
  width: 3px;
  height: 2.4rem;
  background: var(--pink);
  box-shadow: 0 0 12px var(--pink);
  animation: tw-05-blink 0.8s steps(2) 2.8s infinite;
  opacity: 0;
}

@keyframes tw-05-reveal {
  from {
    clip-path: inset(0 100% 0 0);
  }

  to {
    clip-path: inset(0 0% 0 0);
  }
}

@keyframes tw-05-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-05__eyebrow,
    .tw-05__line,
    .tw-05__line::before {
    clip-path: none;
    animation: none;
  }

  .tw-05__cursor {
    opacity: 1;
    animation: none;
  }
}
```
