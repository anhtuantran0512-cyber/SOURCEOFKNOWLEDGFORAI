---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/dna-double-helix-spinner/"
title: "DNA Double Helix Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Eight nucleotide pairs animate as two interweaving dot chains — one cyan, one pink — translating horizontally in opposing directions to simulate a rotating…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: DNA Double Helix Spinner
Source: https://codefronts.com/motion/css-spinner-designs/dna-double-helix-spinner/

Eight nucleotide pairs animate as two interweaving dot chains — one cyan, one pink — translating horizontally in opposing directions to simulate a rotating DNA double helix.
## HTML
```html
<div class="sp-10">
  <div class="sp-10__dna">
    <div class="sp-10__pair"><div class="sp-10__dot-a"></div><div class="sp-10__bridge"></div><div class="sp-10__dot-b"></div></div>
    <div class="sp-10__pair"><div class="sp-10__dot-a"></div><div class="sp-10__bridge"></div><div class="sp-10__dot-b"></div></div>
    <div class="sp-10__pair"><div class="sp-10__dot-a"></div><div class="sp-10__bridge"></div><div class="sp-10__dot-b"></div></div>
    <div class="sp-10__pair"><div class="sp-10__dot-a"></div><div class="sp-10__bridge"></div><div class="sp-10__dot-b"></div></div>
    <div class="sp-10__pair"><div class="sp-10__dot-a"></div><div class="sp-10__bridge"></div><div class="sp-10__dot-b"></div></div>
    <div class="sp-10__pair"><div class="sp-10__dot-a"></div><div class="sp-10__bridge"></div><div class="sp-10__dot-b"></div></div>
    <div class="sp-10__pair"><div class="sp-10__dot-a"></div><div class="sp-10__bridge"></div><div class="sp-10__dot-b"></div></div>
    <div class="sp-10__pair"><div class="sp-10__dot-a"></div><div class="sp-10__bridge"></div><div class="sp-10__dot-b"></div></div>
  </div>
</div>
```
## CSS
```css
.sp-10,
.sp-10 *,
.sp-10 *::before,
.sp-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-10 {
  --bg: #040d1a;
  --ca: #00bcd4;
  --cb: #f06292;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-10__dna {
  display: flex;
  flex-direction: column;
  gap: 0;
  align-items: center;
}

.sp-10__pair {
  display: flex;
  align-items: center;
  gap: 0;
  height: 9px;
}

.sp-10__dot-a,
.sp-10__dot-b {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.sp-10__dot-a {
  background: var(--ca);
  box-shadow: 0 0 6px var(--ca);
}

.sp-10__dot-b {
  background: var(--cb);
  box-shadow: 0 0 6px var(--cb);
}

.sp-10__bridge {
  width: 28px;
  height: 1px;
  background: linear-gradient(to right,var(--ca),var(--cb));
  /* The bridge represents the base-pair connection between the two
       strands. As the strands cross (50% of the cycle, dots meeting at
       center), the visible distance between them shrinks to zero —
       so the bridge should ALSO shrink to invisible at that moment.
       A symmetric scaleX keyframe makes the bridge "breathe" between
       full-width (when strands are spread) and zero-width (when they
       cross). transform-origin:center keeps the bridge centered as it
       scales. */
  transform-origin: center;
  animation: sp-10-bridge 1.4s ease-in-out infinite;
}

.sp-10__pair:nth-child(1) .sp-10__bridge {
  animation-delay: calc(0 * 0.14s);
}

.sp-10__pair:nth-child(2) .sp-10__bridge {
  animation-delay: calc(1 * 0.14s);
}

.sp-10__pair:nth-child(3) .sp-10__bridge {
  animation-delay: calc(2 * 0.14s);
}

.sp-10__pair:nth-child(4) .sp-10__bridge {
  animation-delay: calc(3 * 0.14s);
}

.sp-10__pair:nth-child(5) .sp-10__bridge {
  animation-delay: calc(4 * 0.14s);
}

.sp-10__pair:nth-child(6) .sp-10__bridge {
  animation-delay: calc(5 * 0.14s);
}

.sp-10__pair:nth-child(7) .sp-10__bridge {
  animation-delay: calc(6 * 0.14s);
}

.sp-10__pair:nth-child(8) .sp-10__bridge {
  animation-delay: calc(7 * 0.14s);
}

@keyframes sp-10-bridge {
  /* 0%/100% = strands at extremes → bridge full width visible. */

  0%,
    100% {
    transform: scaleX(1);
    opacity: 0.4;
  }
  /* 50% = strands crossing at center → bridge collapsed + invisible. */

  50% {
    transform: scaleX(0.05);
    opacity: 0;
  }
}
/* Two strands run the SAME keyframe but at OPPOSITE PHASE so they
   cross each other. The trick: dot-A's keyframe goes right→left→right,
   dot-B's keyframe goes left→right→left. With opposite phase, when
   strand A is pushed +16, strand B is pushed -16 — they meet and cross
   at the center every half-cycle, producing the X-shape that reads as
   a helix projection.

   Why not animation-direction:reverse? Because the keyframe is symmetric
   (0% and 100% are identical), so reverse plays the SAME visual sequence.
   Reverse only flips things visually if 0% ≠ 100%. Two distinct keyframes
   (helix-a and helix-b that start at opposite x positions) is the
   reliable approach.

   The per-pair animation-delay staggers the crossing motion vertically
   so it propagates downward in a wave (~0.14s per row). */

.sp-10__pair:nth-child(1) .sp-10__dot-a {
  animation: sp-10-helix-a 1.4s ease-in-out infinite;
  animation-delay: calc(0 * 0.14s);
}

.sp-10__pair:nth-child(2) .sp-10__dot-a {
  animation: sp-10-helix-a 1.4s ease-in-out infinite;
  animation-delay: calc(1 * 0.14s);
}

.sp-10__pair:nth-child(3) .sp-10__dot-a {
  animation: sp-10-helix-a 1.4s ease-in-out infinite;
  animation-delay: calc(2 * 0.14s);
}

.sp-10__pair:nth-child(4) .sp-10__dot-a {
  animation: sp-10-helix-a 1.4s ease-in-out infinite;
  animation-delay: calc(3 * 0.14s);
}

.sp-10__pair:nth-child(5) .sp-10__dot-a {
  animation: sp-10-helix-a 1.4s ease-in-out infinite;
  animation-delay: calc(4 * 0.14s);
}

.sp-10__pair:nth-child(6) .sp-10__dot-a {
  animation: sp-10-helix-a 1.4s ease-in-out infinite;
  animation-delay: calc(5 * 0.14s);
}

.sp-10__pair:nth-child(7) .sp-10__dot-a {
  animation: sp-10-helix-a 1.4s ease-in-out infinite;
  animation-delay: calc(6 * 0.14s);
}

.sp-10__pair:nth-child(8) .sp-10__dot-a {
  animation: sp-10-helix-a 1.4s ease-in-out infinite;
  animation-delay: calc(7 * 0.14s);
}

.sp-10__pair:nth-child(1) .sp-10__dot-b {
  animation: sp-10-helix-b 1.4s ease-in-out infinite;
  animation-delay: calc(0 * 0.14s);
}

.sp-10__pair:nth-child(2) .sp-10__dot-b {
  animation: sp-10-helix-b 1.4s ease-in-out infinite;
  animation-delay: calc(1 * 0.14s);
}

.sp-10__pair:nth-child(3) .sp-10__dot-b {
  animation: sp-10-helix-b 1.4s ease-in-out infinite;
  animation-delay: calc(2 * 0.14s);
}

.sp-10__pair:nth-child(4) .sp-10__dot-b {
  animation: sp-10-helix-b 1.4s ease-in-out infinite;
  animation-delay: calc(3 * 0.14s);
}

.sp-10__pair:nth-child(5) .sp-10__dot-b {
  animation: sp-10-helix-b 1.4s ease-in-out infinite;
  animation-delay: calc(4 * 0.14s);
}

.sp-10__pair:nth-child(6) .sp-10__dot-b {
  animation: sp-10-helix-b 1.4s ease-in-out infinite;
  animation-delay: calc(5 * 0.14s);
}

.sp-10__pair:nth-child(7) .sp-10__dot-b {
  animation: sp-10-helix-b 1.4s ease-in-out infinite;
  animation-delay: calc(6 * 0.14s);
}

.sp-10__pair:nth-child(8) .sp-10__dot-b {
  animation: sp-10-helix-b 1.4s ease-in-out infinite;
  animation-delay: calc(7 * 0.14s);
}
/* Strand A starts pushed RIGHT then swings LEFT (front of the helix at 50%). */

@keyframes sp-10-helix-a {
  0%,
    100% {
    transform: translateX(16px);
    opacity: 0.2;
  }

  50% {
    transform: translateX(-16px);
    opacity: 1;
  }
}
/* Strand B starts pushed LEFT then swings RIGHT — opposite phase, so
   strands A and B cross at the center every half-cycle (the X pattern). */

@keyframes sp-10-helix-b {
  0%,
    100% {
    transform: translateX(-16px);
    opacity: 1;
  }

  50% {
    transform: translateX(16px);
    opacity: 0.2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-10__dot-a,
    .sp-10__dot-b {
    animation: none;
    transform: none;
  }
}
```
