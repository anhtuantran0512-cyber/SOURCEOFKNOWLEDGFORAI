---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-svg-stroke-dashoffset/"
title: "CSS Typewriter SVG stroke-dashoffset"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "SVG text paths are drawn stroke-first using an animated stroke-dashoffset, revealing each letter as a hand-lettered signature — a technique impossible with…"
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter SVG stroke-dashoffset
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-svg-stroke-dashoffset/

SVG text paths are drawn stroke-first using an animated stroke-dashoffset, revealing each letter as a hand-lettered signature — a technique impossible with HTML alone.
## HTML
```html
<div class="tw-06">
  <div class="tw-06__stage">
    <svg class="tw-06__svg" viewBox="0 0 500 160" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="tw-06-grad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%"   stop-color="#818cf8"/>
          <stop offset="100%" stop-color="#c084fc"/>
        </linearGradient>
      </defs>
      <text class="tw-06__word tw-06__word--1"
        x="50%" y="90" text-anchor="middle"
        font-family="Georgia, serif" font-size="72" font-weight="700"
        stroke="url(#tw-06-grad)" stroke-width="2" fill="url(#tw-06-grad)"
        style="--dash:1400">Signature</text>
    </svg>
    <p class="tw-06__caption">SVG stroke-dashoffset draw technique</p>
  </div>
</div>
```
## CSS
```css
.tw-06,
.tw-06 *,
.tw-06 *::before,
.tw-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-06 ::selection {
  background: #818cf8;
  color: #0a0820;
}

.tw-06 {
  --indigo: #818cf8;
  --purple: #c084fc;
  --bg: #0a0820;
  font-family: Georgia, serif;
  background: radial-gradient(ellipse at 50% 60%, #12103a 0%, var(--bg) 70%);
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
}

.tw-06__stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  width: 100%;
  max-width: 520px;
}

.tw-06__svg {
  width: 100%;
  height: auto;
  overflow: visible;
  filter: drop-shadow(0 0 20px rgba(129,140,248,0.3));
}

.tw-06__word {
  stroke-dasharray: var(--dash, 1400);
  stroke-dashoffset: var(--dash, 1400);
  fill-opacity: 0;
  animation: tw-06-draw 2.4s cubic-bezier(0.4, 0, 0.2, 1) 0.5s forwards, tw-06-fill 0.5s ease 2.7s forwards;
}

.tw-06__caption {
  font-size: 0.75rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #4338ca;
}

@keyframes tw-06-draw {
  from {
    stroke-dashoffset: var(--dash, 1400);
  }

  to {
    stroke-dashoffset: 0;
  }
}

@keyframes tw-06-fill {
  from {
    fill-opacity: 0;
  }

  to {
    fill-opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-06__word {
    stroke-dashoffset: 0;
    fill-opacity: 1;
    animation: none;
  }
}
```
