---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/comet-trail-css-spinner/"
title: "Comet Trail CSS Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A conic-gradient comet with a long fading purple tail sweeps around a dark ring, with a bright glowing tip dot that precisely tracks the leading edge of the…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Comet Trail CSS Spinner
Source: https://codefronts.com/motion/css-spinner-designs/comet-trail-css-spinner/

A conic-gradient comet with a long fading purple tail sweeps around a dark ring, with a bright glowing tip dot that precisely tracks the leading edge of the arc.
## HTML
```html
<div class="sp-09">
  <div class="sp-09__wrap">
    <div class="sp-09__spinner">
      <div class="sp-09__comet"></div>
      <div class="sp-09__hole"></div>
      <div class="sp-09__tip"></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sp-09,
.sp-09 *,
.sp-09 *::before,
.sp-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-09 {
  --bg: #030a1a;
  --c: #e040fb;
  --glow: rgba(224,64,251,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-09__wrap {
  position: relative;
  width: 80px;
  height: 80px;
}

.sp-09__spinner {
  position: absolute;
  inset: 0;
  animation: sp-09-spin 1s linear infinite;
}

.sp-09__comet {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  /*
      Bright tip lands at 360deg (= 0deg = 12 o'clock). Tail fades
      BACKWARD (counter-clockwise from the tip) through the 180-360
      range. The 0-180 range is empty so there's a clean gap before
      the tip. Reversing the gradient direction (vs the simpler
      "bright at 0deg, fade to 180deg" layout) makes the tail point
      CCW from the head — correct comet physics for CLOCKWISE
      rotation, where the tail trails behind the direction of motion.
    */
  background: conic-gradient(
      transparent                 0deg,
      transparent               180deg,
      rgba(224,64,251,0.15)     240deg,
      rgba(224,64,251,0.4)      300deg,
      var(--c)                  360deg
    );
  filter: drop-shadow(0 0 4px var(--glow));
}

.sp-09__hole {
  position: absolute;
  inset: 10px;
  border-radius: 50%;
  background: var(--bg);
}
/* Tip at 12-o'clock = 0deg = bright head of the comet. The conic
   disc is 80px with donut hole inset:10px so the ring midline is
   at radius 35 (= 5px from the outer top edge). The tip dot's
   CENTER must land on that midline. translate(-50%, -50%) on
   top:5px + left:50% places the dot center exactly on the ring
   stroke at the 12 o'clock position. */

.sp-09__tip {
  position: absolute;
  top: 5px;
  left: 50%;
  width: 8px;
  height: 8px;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  background: var(--c);
  box-shadow: 0 0 10px var(--c),0 0 20px var(--c);
}

@keyframes sp-09-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-09__spinner {
    animation: none;
  }
}
```
