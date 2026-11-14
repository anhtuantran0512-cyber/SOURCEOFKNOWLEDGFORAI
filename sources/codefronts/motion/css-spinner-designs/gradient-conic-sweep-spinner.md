---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/gradient-conic-sweep-spinner/"
title: "Gradient Conic Sweep Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A conic-gradient disk sweeps through deep violet-to-cyan colours with a transparent cutout tail, creating a smooth colour-wheel spinner with a bright…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Conic Sweep Spinner
Source: https://codefronts.com/motion/css-spinner-designs/gradient-conic-sweep-spinner/

A conic-gradient disk sweeps through deep violet-to-cyan colours with a transparent cutout tail, creating a smooth colour-wheel spinner with a bright leading-edge tip.
## HTML
```html
<div class="sp-04">
  <div class="sp-04__wrap">
    <div class="sp-04__spinner">
      <div class="sp-04__conic"></div>
      <div class="sp-04__hole"></div>
      <div class="sp-04__tip"></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sp-04,
.sp-04 *,
.sp-04 *::before,
.sp-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-04 {
  --bg: #050510;
  --c1: #00e5ff;
  --c2: #1976d2;
  --c3: #6200ea;
  --hole: #050510;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-04__wrap {
  position: relative;
  width: 80px;
  height: 80px;
}

.sp-04__spinner {
  position: absolute;
  inset: 0;
  animation: sp-04-spin 1s linear infinite;
}

.sp-04__conic {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  /*
      Bright cyan tip lands at 360deg (= 0deg = 12 o'clock). Arc fades
      BACKWARD (counter-clockwise from the tip): purple → blue → cyan
      arriving at the tip. Transparent gap from 0-60deg = clean cutoff
      after the tip in the rotation direction. Tail points CCW from
      head = correct comet physics for CLOCKWISE rotation (tail trails
      behind the direction of motion). Same direction as Demo 09 so
      they read consistently.
    */
  background: conic-gradient(
      transparent   0deg,
      transparent  60deg,
      var(--c3)   120deg,
      var(--c2)   240deg,
      var(--c1)   360deg
    );
  filter: drop-shadow(0 0 6px var(--c1));
}

.sp-04__hole {
  position: absolute;
  inset: 10px;
  border-radius: 50%;
  background: var(--hole);
}
/* Tip at 12-o'clock (0deg) = exact bright start of the arc. The
   conic disc is 80px and the donut hole is inset:10px so the ring
   spans outer-radius 40 → inner-radius 30 → midline at radius 35
   (= 5px from the outer top edge). The tip dot's CENTER must land
   on that midline, so we offset the 10x10 dot up by half its size
   via the translateY(-50%) trick. left:50% + translateX(-50%)
   centers it horizontally on the same axis. */

.sp-04__tip {
  position: absolute;
  top: 5px;
  left: 50%;
  width: 10px;
  height: 10px;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  background: var(--c1);
  box-shadow: 0 0 12px var(--c1),0 0 24px var(--c1);
}

@keyframes sp-04-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-04__spinner {
    animation: none;
  }
}
```
