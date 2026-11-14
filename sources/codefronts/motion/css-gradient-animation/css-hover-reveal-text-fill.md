---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-hover-reveal-text-fill/"
title: "CSS Hover Reveal Text Fill"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "Plain text that reveals a flowing gradient fill on hover — using background-clip: text with a CSS transition that expands background-size from 0% to full…"
has_js: "false"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hover Reveal Text Fill
Source: https://codefronts.com/motion/css-gradient-animation/css-hover-reveal-text-fill/

Plain text that reveals a flowing gradient fill on hover — using background-clip: text with a CSS transition that expands background-size from 0% to full width, plus a per-character stagger variant where each letter fills individually.
## HTML
```html
<div class="ga-10">

  <p class="ga-10__hint">↓ Hover each line to reveal the gradient fill</p>

  <div style="display:flex;flex-direction:column;align-items:center;gap:16px;">
    <span class="ga-10__reveal">Ship Faster.</span>
    <span class="ga-10__reveal ga-10__v2">Build Smarter.</span>
    <span class="ga-10__reveal ga-10__v3">Scale Effortlessly.</span>
    <span class="ga-10__reveal ga-10__v4">Design Better.</span>
  </div>

  <div style="display:flex;flex-direction:column;align-items:center;gap:12px;">
    <p class="ga-10__hint">Character stagger — hover the word below</p>
    <div class="ga-10__stagger" aria-label="INNOVATION">
      <span class="ga-10__char">I</span>
      <span class="ga-10__char">N</span>
      <span class="ga-10__char">N</span>
      <span class="ga-10__char">O</span>
      <span class="ga-10__char">V</span>
      <span class="ga-10__char">A</span>
      <span class="ga-10__char">T</span>
      <span class="ga-10__char">I</span>
      <span class="ga-10__char">O</span>
      <span class="ga-10__char">N</span>
    </div>
  </div>

</div>
```
## CSS
```css
.ga-10,
.ga-10 *,
.ga-10 *::before,
.ga-10 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-10 ::selection {
  background: rgba(245,158,11,.35);
  color: #fff;
}

.ga-10 {
  --bg: #09090f;
  --plain: rgba(255,255,255,.25);
  --dur: 3s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 56px;
  padding: 56px 24px;
}
/* ── Core technique: layered backgrounds, clip to text ──
   The gradient is always there but background-size is 0% → 100%
   driven by a CSS transition on hover, revealing the fill left-to-right. */
/* Variant A — reveal fill sweeps left to right on hover */

.ga-10__reveal {
  position: relative;
  display: inline-block;
  font-size: clamp(2rem, 5vw, 3.2rem);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1.1;
  cursor: default;
  /* Base colour */
  color: var(--plain);
  /* Gradient overlay via background-clip */
  background-image: linear-gradient(var(--grad-angle, 90deg),
      var(--g1, #f97316),
      var(--g2, #ec4899),
      var(--g3, #a855f7),
      var(--g4, #06b6d4)
    );
  background-size: var(--fill, 0%) 100%;
  background-clip: text;
  -webkit-background-clip: text;
  /* The text colour itself is not transparent yet — we use a
       clip-path on a pseudo-element to overlay the gradient version */
  -webkit-text-fill-color: var(--plain);
}
/* Gradient layer rides on the parent's background-clip */

.ga-10__reveal:hover {
  --fill: 100%;
  -webkit-text-fill-color: transparent;
  transition: background-size .55s cubic-bezier(.22,1,.36,1);
  animation: ga-10-flow var(--dur) linear infinite;
  background-size: 300% 100%;
}

@keyframes ga-10-flow {
  0% {
    background-position: 0% 50%;
  }

  100% {
    background-position: -200% 50%;
  }
}
/* Reset when not hovered */

.ga-10__reveal {
  transition: background-size .4s ease, -webkit-text-fill-color .1s .38s;
  background-position: 0% 50%;
}
/* Variant styles */

.ga-10__v2 {
  --g1: #10b981;
  --g2: #06b6d4;
  --g3: #818cf8;
  --g4: #a855f7;
}

.ga-10__v3 {
  --g1: #eab308;
  --g2: #f97316;
  --g3: #ef4444;
  --g4: #ec4899;
}

.ga-10__v4 {
  --g1: #c084fc;
  --g2: #818cf8;
  --g3: #38bdf8;
  --g4: #34d399;
}
/* ── Variant B — character-split stagger ── */

.ga-10__stagger {
  display: flex;
  gap: 0;
  flex-wrap: wrap;
  justify-content: center;
}

.ga-10__char {
  display: inline-block;
  font-size: clamp(2.6rem, 6vw, 4rem);
  font-weight: 900;
  letter-spacing: -.025em;
  color: rgba(255,255,255,.18);
  background-image: linear-gradient(90deg, #a855f7, #ec4899, #f97316, #eab308);
  background-size: 200% 100%;
  background-position: 0% 0;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: inherit;
  transition: color .01s, -webkit-text-fill-color .01s;
}

.ga-10__stagger:hover .ga-10__char {
  -webkit-text-fill-color: transparent;
  animation: ga-10-char-fill .4s forwards, ga-10-flow-char 2s .4s linear infinite;
}

@keyframes ga-10-char-fill {
  to {
    background-position: -100% 0;
  }
}

@keyframes ga-10-flow-char {
  0% {
    background-position: 0% 0;
  }

  100% {
    background-position: -200% 0;
  }
}
/* Stagger delay */

.ga-10__stagger:hover .ga-10__char:nth-child(1) {
  animation-delay: 0s, .4s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(2) {
  animation-delay: .04s, .44s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(3) {
  animation-delay: .08s, .48s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(4) {
  animation-delay: .12s, .52s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(5) {
  animation-delay: .16s, .56s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(6) {
  animation-delay: .20s, .60s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(7) {
  animation-delay: .24s, .64s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(8) {
  animation-delay: .28s, .68s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(9) {
  animation-delay: .32s, .72s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(10) {
  animation-delay: .36s, .76s;
}

.ga-10__stagger:hover .ga-10__char:nth-child(11) {
  animation-delay: .40s, .80s;
}
/* Space character */

.ga-10__char--sp {
  background: none !important;
  -webkit-text-fill-color: transparent !important;
}
/* Sub-hint */

.ga-10__hint {
  font-size: .72rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: rgba(255,255,255,.2);
}

@media (prefers-reduced-motion: reduce) {
  .ga-10__reveal:hover,
    .ga-10__stagger:hover .ga-10__char {
    animation: none;
  }

  .ga-10__reveal:hover {
    background-size: 100% 100%;
  }
}
```
