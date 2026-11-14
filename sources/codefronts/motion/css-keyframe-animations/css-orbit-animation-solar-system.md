---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-orbit-animation-solar-system/"
title: "CSS Orbit Animation Solar System"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Animated solar system with Sun, Mercury, Venus, Earth, Mars, Jupiter and Saturn orbiting at variable speeds on a starfield background — pure CSS rotate…"
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Orbit Animation Solar System
Source: https://codefronts.com/motion/css-keyframe-animations/css-orbit-animation-solar-system/

Animated solar system with Sun, Mercury, Venus, Earth, Mars, Jupiter and Saturn orbiting at variable speeds on a starfield background — pure CSS rotate keyframes.
## HTML
```html
<div class="kf-12">
  <div class="kf-12__system">
    <!-- Sun -->
    <div class="kf-12__sun"></div>
    <!-- Orbits -->
    <div class="kf-12__orbit kf-12__o-mercury"><div class="kf-12__planet kf-12__p-mercury" data-name="MERCURY"></div></div>
    <div class="kf-12__orbit kf-12__o-venus"><div class="kf-12__planet kf-12__p-venus" data-name="VENUS"></div></div>
    <div class="kf-12__orbit kf-12__o-earth"><div class="kf-12__planet kf-12__p-earth" data-name="EARTH"></div></div>
    <div class="kf-12__orbit kf-12__o-mars"><div class="kf-12__planet kf-12__p-mars" data-name="MARS"></div></div>
    <div class="kf-12__orbit kf-12__o-jupiter"><div class="kf-12__planet kf-12__p-jupiter" data-name="JUPITER"></div></div>
    <div class="kf-12__orbit kf-12__o-saturn"><div class="kf-12__planet kf-12__p-saturn" data-name="SATURN"></div></div>
  </div>
  <div class="kf-12__label">CSS KEYFRAME ORBIT — SOLAR SYSTEM</div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');

.kf-12,
.kf-12 *,
.kf-12 *::before,
.kf-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-12 ::selection {
  background: #ffd166;
  color: #000;
}

.kf-12 {
  --bg: #04050f;
  --star: #fff;
  --sun: #ffd166;
  --mercury: #a8a8a8;
  --venus: #e5c07b;
  --earth: #4cc9f0;
  --mars: #e57373;
  --jupiter: #c99b5f;
  --saturn: #f0d080;
  font-family: 'Space Mono',monospace;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 24px;
  overflow: hidden;
  position: relative;
  color: #fff;
}
/* Starfield */

.kf-12::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: radial-gradient(1px 1px at 10% 15%,#fff,transparent), radial-gradient(1px 1px at 25% 60%,rgba(255,255,255,.8),transparent), radial-gradient(1.5px 1.5px at 55% 20%,#fff,transparent), radial-gradient(1px 1px at 75% 75%,rgba(255,255,255,.9),transparent), radial-gradient(1px 1px at 40% 90%,rgba(255,255,255,.7),transparent), radial-gradient(1px 1px at 88% 35%,#fff,transparent), radial-gradient(1.5px 1.5px at 18% 80%,rgba(255,255,255,.6),transparent), radial-gradient(1px 1px at 65% 50%,rgba(255,255,255,.8),transparent), radial-gradient(1px 1px at 92% 10%,#fff,transparent), radial-gradient(1px 1px at 5% 45%,rgba(255,255,255,.7),transparent);
}
/* ——— System ——— */

.kf-12__system {
  position: relative;
  width: min(560px,90vw);
  height: min(560px,90vw);
  display: flex;
  align-items: center;
  justify-content: center;
}
/* Sun */

.kf-12__sun {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: radial-gradient(circle at 38% 35%,#fff9c4,var(--sun) 60%,#e65100);
  box-shadow: 0 0 20px var(--sun),0 0 50px rgba(255,209,102,.4),0 0 80px rgba(255,209,102,.15);
  animation: kf-12-pulse 3s ease-in-out infinite;
  position: relative;
  z-index: 5;
  flex: 0 0 52px;
}

@keyframes kf-12-pulse {
  0%,
    100% {
    box-shadow: 0 0 20px var(--sun),0 0 50px rgba(255,209,102,.4);
  }

  50% {
    box-shadow: 0 0 30px var(--sun),0 0 70px rgba(255,209,102,.6),0 0 100px rgba(255,209,102,.2);
  }
}
/* Orbit rings + planets */

.kf-12__orbit {
  position: absolute;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,.06);
  display: flex;
  align-items: flex-start;
  justify-content: center;
}

.kf-12__planet {
  border-radius: 50%;
  margin-top: -1px;
  position: relative;
  box-shadow: inset -3px -2px 6px rgba(0,0,0,.6);
}

.kf-12__planet::after {
  content: attr(data-name);
  position: absolute;
  top: calc(100% + 6px);
  left: 50%;
  transform: translateX(-50%);
  font-size: 9px;
  white-space: nowrap;
  color: rgba(255,255,255,.5);
  letter-spacing: .1em;
}
/* Mercury */

.kf-12__o-mercury {
  width: 14%;
  height: 14%;
  animation: kf-12-orbit 2.4s linear infinite;
}

.kf-12__p-mercury {
  width: 10px;
  height: 10px;
  background: radial-gradient(circle at 38% 35%,#ddd,var(--mercury));
}
/* Venus */

.kf-12__o-venus {
  width: 24%;
  height: 24%;
  animation: kf-12-orbit 6s linear infinite;
}

.kf-12__p-venus {
  width: 14px;
  height: 14px;
  background: radial-gradient(circle at 38% 35%,#fff3c4,var(--venus));
}
/* Earth */

.kf-12__o-earth {
  width: 36%;
  height: 36%;
  animation: kf-12-orbit 10s linear infinite;
}

.kf-12__p-earth {
  width: 16px;
  height: 16px;
  background: radial-gradient(circle at 38% 35%,#90d8ff,var(--earth));
}
/* Mars */

.kf-12__o-mars {
  width: 50%;
  height: 50%;
  animation: kf-12-orbit 19s linear infinite;
}

.kf-12__p-mars {
  width: 12px;
  height: 12px;
  background: radial-gradient(circle at 38% 35%,#ff9e9e,var(--mars));
}
/* Jupiter */

.kf-12__o-jupiter {
  width: 68%;
  height: 68%;
  animation: kf-12-orbit 118s linear infinite;
}

.kf-12__p-jupiter {
  width: 26px;
  height: 26px;
  background: radial-gradient(circle at 38% 35%,#f5d9a8,var(--jupiter));
}
/* Saturn */

.kf-12__o-saturn {
  width: 86%;
  height: 86%;
  animation: kf-12-orbit 294s linear infinite;
}

.kf-12__p-saturn {
  width: 22px;
  height: 22px;
  background: radial-gradient(circle at 38% 35%,#fff5c0,var(--saturn));
  position: relative;
}

.kf-12__p-saturn::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 38px;
  height: 8px;
  transform: translate(-50%,-50%) rotateX(65deg);
  border: 3px solid rgba(240,208,128,.6);
  border-radius: 50%;
  box-shadow: 0 0 0 4px rgba(240,208,128,.15);
}

@keyframes kf-12-orbit {
  to {
    transform: rotate(360deg);
  }
}

.kf-12__label {
  font-size: .7rem;
  letter-spacing: .2em;
  color: rgba(255,255,255,.35);
}

@media (max-width: 420px) {
  .kf-12__system {
    width: 320px;
    height: 320px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-12 * {
    animation: none!important;
  }
}
```
