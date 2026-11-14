---
source: "codefronts"
url: "https://codefronts.com/components/css-star-ratings/animated-bursting-svg-star-rating/"
title: "Animated Bursting SVG Star Rating"
section: "components"
category: "css-star-ratings"
category_name: "CSS Star Ratings"
description: "A tactile dark-mode star widget where clicking a star triggers an elastic pop, an expanding ring burst, and six radial spark particles — all driven by CSS…"
has_js: "false"
---

Here's a working CSS Star Rating from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Bursting SVG Star Rating
Source: https://codefronts.com/components/css-star-ratings/animated-bursting-svg-star-rating/

A tactile dark-mode star widget where clicking a star triggers an elastic pop, an expanding ring burst, and six radial spark particles — all driven by CSS @keyframes on :checked.
## HTML
```html
<div class="sr-04">
  <div class="sr-04__card">
    <span class="sr-04__emoji">🎮</span>
    <div class="sr-04__title">Rate Your Session</div>
    <div class="sr-04__sub">Tap a star — watch the burst!</div>

    <div class="sr-04__stars">
      <!-- star 1 -->
      <div class="sr-04__star-wrap">
        <input type="radio" id="sr-04-s1" name="sr-04-r" value="1">
        <label for="sr-04-s1">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path class="sr-04__star-path" d="M12 2l2.9 6.1L22 9.3l-5 4.9 1.2 6.8L12 17.8l-6.2 3.2L7 14.2 2 9.3l7.1-1.2z"/>
          </svg>
        </label>
        <div class="sr-04__ring"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
      </div>
      <!-- star 2 -->
      <div class="sr-04__star-wrap">
        <input type="radio" id="sr-04-s2" name="sr-04-r" value="2">
        <label for="sr-04-s2">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path class="sr-04__star-path" d="M12 2l2.9 6.1L22 9.3l-5 4.9 1.2 6.8L12 17.8l-6.2 3.2L7 14.2 2 9.3l7.1-1.2z"/>
          </svg>
        </label>
        <div class="sr-04__ring"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
      </div>
      <!-- star 3 -->
      <div class="sr-04__star-wrap">
        <input type="radio" id="sr-04-s3" name="sr-04-r" value="3">
        <label for="sr-04-s3">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path class="sr-04__star-path" d="M12 2l2.9 6.1L22 9.3l-5 4.9 1.2 6.8L12 17.8l-6.2 3.2L7 14.2 2 9.3l7.1-1.2z"/>
          </svg>
        </label>
        <div class="sr-04__ring"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
      </div>
      <!-- star 4 -->
      <div class="sr-04__star-wrap">
        <input type="radio" id="sr-04-s4" name="sr-04-r" value="4">
        <label for="sr-04-s4">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path class="sr-04__star-path" d="M12 2l2.9 6.1L22 9.3l-5 4.9 1.2 6.8L12 17.8l-6.2 3.2L7 14.2 2 9.3l7.1-1.2z"/>
          </svg>
        </label>
        <div class="sr-04__ring"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
      </div>
      <!-- star 5 -->
      <div class="sr-04__star-wrap">
        <input type="radio" id="sr-04-s5" name="sr-04-r" value="5">
        <label for="sr-04-s5">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path class="sr-04__star-path" d="M12 2l2.9 6.1L22 9.3l-5 4.9 1.2 6.8L12 17.8l-6.2 3.2L7 14.2 2 9.3l7.1-1.2z"/>
          </svg>
        </label>
        <div class="sr-04__ring"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
        <div class="sr-04__spark"></div>
      </div>
    </div>

    <div class="sr-04__tagline">Stars burst with <strong>CSS @keyframes</strong> magic ✨</div>
  </div>
</div>
```
## CSS
```css
.sr-04,
.sr-04 *,
.sr-04 *::before,
.sr-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sr-04 ::selection {
  background: #f59e0b;
  color: #1a1a1a;
}

.sr-04 {
  --amber: #f59e0b;
  --amber-light: #fcd34d;
  --amber-dark: #d97706;
  --spark1: #ef4444;
  --spark2: #f97316;
  --spark3: #84cc16;
  --spark4: #06b6d4;
  --bg-dark: #0c0a09;
  --bg-card: #1c1917;
  --border: #292524;
  --text: #fafaf9;
  --text-muted: #78716c;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg-dark);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
}

.sr-04__card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 36px 40px 32px;
  max-width: 420px;
  width: 100%;
  text-align: center;
  box-shadow: 0 30px 80px rgba(0,0,0,0.6);
}

.sr-04__emoji {
  font-size: 48px;
  margin-bottom: 12px;
  display: block;
  animation: sr-04-float 3s ease-in-out infinite;
}

.sr-04__title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
}

.sr-04__sub {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-bottom: 28px;
}
/* Burst star widget */

.sr-04__stars {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 24px;
}

.sr-04__stars input[type="radio"] {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.sr-04__star-wrap {
  position: relative;
  width: 56px;
  height: 56px;
}

.sr-04__star-wrap label {
  display: block;
  width: 56px;
  height: 56px;
  cursor: pointer;
  position: relative;
  z-index: 2;
}
/* SVG star in label. overflow: visible is critical — the inner
   path has filter: drop-shadow which would otherwise be clipped to
   the SVG's intrinsic viewBox bounds (24×24 units mapped to 56px)
   and render as a square halo around the star instead of glowing
   the star's silhouette. */

.sr-04__star-wrap label svg {
  width: 56px;
  height: 56px;
  overflow: visible;
  transition: transform 0.35s cubic-bezier(.34,1.8,.64,1), filter 0.25s ease;
}

.sr-04__star-wrap label svg .sr-04__star-path {
  fill: var(--border);
  transition: fill 0.25s ease;
}
/* Hover state — the hovered star scales up and glows; all lower
   stars also fill with amber so the hover preview matches what
   clicking will produce. Pattern mirrors the :has()-driven checked
   state below: when .sr-04__star-wrap:nth-child(N) is hovered, fill
   stars 1..N. The :has() lives on .sr-04__stars so it can look
   inside any of its 5 .sr-04__star-wrap children. */

.sr-04__star-wrap label:hover svg {
  transform: scale(1.2);
}

.sr-04__stars:has(.sr-04__star-wrap:nth-child(1) label:hover) .sr-04__star-wrap:nth-child(1) label svg .sr-04__star-path,
.sr-04__stars:has(.sr-04__star-wrap:nth-child(2) label:hover) .sr-04__star-wrap:nth-child(-n+2) label svg .sr-04__star-path,
.sr-04__stars:has(.sr-04__star-wrap:nth-child(3) label:hover) .sr-04__star-wrap:nth-child(-n+3) label svg .sr-04__star-path,
.sr-04__stars:has(.sr-04__star-wrap:nth-child(4) label:hover) .sr-04__star-wrap:nth-child(-n+4) label svg .sr-04__star-path,
.sr-04__stars:has(.sr-04__star-wrap:nth-child(5) label:hover) .sr-04__star-wrap:nth-child(-n+5) label svg .sr-04__star-path {
  fill: var(--amber-light);
  filter: drop-shadow(0 0 8px var(--amber));
}
/* Burst ring — hidden circle that expands on checked */

.sr-04__ring {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 4px;
  height: 4px;
  margin: -2px 0 0 -2px;
  border-radius: 50%;
  border: 3px solid var(--amber);
  opacity: 0;
  transform: scale(0);
  pointer-events: none;
}
/* Spark particles */

.sr-04__spark {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  opacity: 0;
  pointer-events: none;
}
/* When radio checked: animate the matching star and its siblings */

.sr-04__stars:has(#sr-04-s1:checked) .sr-04__star-wrap:nth-child(1) label svg .sr-04__star-path,
.sr-04__stars:has(#sr-04-s2:checked) .sr-04__star-wrap:nth-child(-n+2) label svg .sr-04__star-path,
.sr-04__stars:has(#sr-04-s3:checked) .sr-04__star-wrap:nth-child(-n+3) label svg .sr-04__star-path,
.sr-04__stars:has(#sr-04-s4:checked) .sr-04__star-wrap:nth-child(-n+4) label svg .sr-04__star-path,
.sr-04__stars:has(#sr-04-s5:checked) .sr-04__star-wrap:nth-child(-n+5) label svg .sr-04__star-path {
  fill: var(--amber);
  filter: drop-shadow(0 0 6px var(--amber));
}
/* The specific checked star gets the burst */

.sr-04__stars:has(#sr-04-s1:checked) .sr-04__star-wrap:nth-child(1) label svg,
.sr-04__stars:has(#sr-04-s2:checked) .sr-04__star-wrap:nth-child(2) label svg,
.sr-04__stars:has(#sr-04-s3:checked) .sr-04__star-wrap:nth-child(3) label svg,
.sr-04__stars:has(#sr-04-s4:checked) .sr-04__star-wrap:nth-child(4) label svg,
.sr-04__stars:has(#sr-04-s5:checked) .sr-04__star-wrap:nth-child(5) label svg {
  animation: sr-04-pop 0.5s cubic-bezier(.34,1.8,.64,1) forwards;
}

.sr-04__stars:has(#sr-04-s1:checked) .sr-04__star-wrap:nth-child(1) .sr-04__ring,
.sr-04__stars:has(#sr-04-s2:checked) .sr-04__star-wrap:nth-child(2) .sr-04__ring,
.sr-04__stars:has(#sr-04-s3:checked) .sr-04__star-wrap:nth-child(3) .sr-04__ring,
.sr-04__stars:has(#sr-04-s4:checked) .sr-04__star-wrap:nth-child(4) .sr-04__ring,
.sr-04__stars:has(#sr-04-s5:checked) .sr-04__star-wrap:nth-child(5) .sr-04__ring {
  animation: sr-04-ring 0.6s ease-out forwards;
}

.sr-04__stars:has(#sr-04-s1:checked) .sr-04__star-wrap:nth-child(1) .sr-04__spark,
.sr-04__stars:has(#sr-04-s2:checked) .sr-04__star-wrap:nth-child(2) .sr-04__spark,
.sr-04__stars:has(#sr-04-s3:checked) .sr-04__star-wrap:nth-child(3) .sr-04__spark,
.sr-04__stars:has(#sr-04-s4:checked) .sr-04__star-wrap:nth-child(4) .sr-04__spark,
.sr-04__stars:has(#sr-04-s5:checked) .sr-04__star-wrap:nth-child(5) .sr-04__spark {
  animation: sr-04-spark 0.7s ease-out forwards;
}

.sr-04__spark:nth-child(3) {
  background: var(--spark1);
  animation-delay: 0.05s;
}

.sr-04__spark:nth-child(4) {
  background: var(--spark2);
  animation-delay: 0.1s;
  transform-origin: center;
}

.sr-04__spark:nth-child(5) {
  background: var(--spark3);
  animation-delay: 0s;
}

.sr-04__spark:nth-child(6) {
  background: var(--spark4);
  animation-delay: 0.07s;
}

.sr-04__spark:nth-child(7) {
  background: var(--amber);
  animation-delay: 0.03s;
}

.sr-04__spark:nth-child(8) {
  background: var(--amber-light);
  animation-delay: 0.12s;
}

@keyframes sr-04-float {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-6px);
  }
}
/* Scale + rotate only — no filter here. drop-shadow on the
   <svg> wrapper renders from its rectangular bounding box,
   producing a square halo around each star. The glow is
   applied on the inner <path> instead (rule below + the
   :checked fill rule already applies it correctly there)
   so the shadow follows the star's silhouette. */

@keyframes sr-04-pop {
  0% {
    transform: scale(1);
  }

  40% {
    transform: scale(1.5) rotate(-5deg);
  }

  70% {
    transform: scale(0.9) rotate(3deg);
  }

  100% {
    transform: scale(1.15);
  }
}

@keyframes sr-04-ring {
  0% {
    opacity: 1;
    transform: scale(1);
    border-width: 3px;
  }

  100% {
    opacity: 0;
    transform: scale(5);
    border-width: 0px;
  }
}

@keyframes sr-04-spark {
  0% {
    opacity: 1;
    transform: translate(0,0) scale(1);
  }

  100% {
    opacity: 0;
    transform: translate(var(--dx, 20px), var(--dy, -30px)) scale(0);
  }
}
/* Assign random directions per spark */

.sr-04__spark:nth-child(3) {
  --dx: 28px;
  --dy: -28px;
}

.sr-04__spark:nth-child(4) {
  --dx: -28px;
  --dy: -28px;
}

.sr-04__spark:nth-child(5) {
  --dx: 0px;
  --dy: -36px;
}

.sr-04__spark:nth-child(6) {
  --dx: 36px;
  --dy: 0px;
}

.sr-04__spark:nth-child(7) {
  --dx: -36px;
  --dy: 0px;
}

.sr-04__spark:nth-child(8) {
  --dx: 20px;
  --dy: 30px;
}

.sr-04__tagline {
  font-size: 0.88rem;
  color: var(--text-muted);
}

.sr-04__tagline strong {
  color: var(--amber);
}

@media (prefers-reduced-motion: reduce) {
  .sr-04__emoji {
    animation: none;
  }

  .sr-04__stars label svg,
    .sr-04__ring,
    .sr-04__spark {
    animation: none !important;
  }
}
```
