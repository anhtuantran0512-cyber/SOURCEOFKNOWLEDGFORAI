---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-heartbeat-pulse-loader/"
title: "CSS Heartbeat Pulse Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Four heart and pulse CSS loaders — an SVG heartbeat, expanding ring pulse, animated ECG line, and sonar ping — perfect for health, wellness, and real-time…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Heartbeat Pulse Loader
Source: https://codefronts.com/motion/css-loader-designs/css-heartbeat-pulse-loader/

Four heart and pulse CSS loaders — an SVG heartbeat, expanding ring pulse, animated ECG line, and sonar ping — perfect for health, wellness, and real-time data UI contexts.
## HTML
```html
<div class="ld-08">
  <div class="ld-08__stage">
    <div class="ld-08__cell">
      <div class="ld-08__heart">
        <svg viewBox="0 0 24 24" fill="var(--c1)" xmlns="http://www.w3.org/2000/svg" style="filter:drop-shadow(0 0 8px var(--c1))">
          <path d="M12 21.593c-5.63-5.539-11-10.297-11-14.402 0-3.791 3.068-5.191 5.281-5.191 1.312 0 4.151.501 5.719 4.457 1.59-3.968 4.464-4.447 5.726-4.447 2.54 0 5.274 1.621 5.274 5.181 0 4.069-5.136 8.625-11 14.402z"/>
        </svg>
      </div>
      <span class="ld-08__label">Heartbeat</span>
    </div>
    <div class="ld-08__cell">
      <div class="ld-08__rings"><span></span><span></span><i></i></div>
      <span class="ld-08__label">Ring Pulse</span>
    </div>
    <div class="ld-08__cell">
      <div class="ld-08__ecg">
        <svg viewBox="0 0 200 50" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
          <polyline points="0,25 20,25 30,25 35,5 40,45 45,25 55,25 65,25 70,10 75,40 80,25 100,25 120,25 125,5 130,45 135,25 145,25 155,25 160,10 165,40 170,25 190,25 200,25" fill="none" stroke="#ff4d6d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter:drop-shadow(0 0 4px #ff4d6d)"/>
        </svg>
      </div>
      <span class="ld-08__label">ECG Line</span>
    </div>
    <div class="ld-08__cell">
      <div class="ld-08__sonar"><span></span><span></span><span></span><i></i></div>
      <span class="ld-08__label">Sonar Ping</span>
    </div>
  </div>
```
## CSS
```css
.ld-08,
.ld-08 *,
.ld-08 *::before,
.ld-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-08 {
  --bg: #0d0014;
  --c1: #ff4d6d;
  --c2: #ff8fa3;
  --c3: #ffb3c1;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-08__stage {
  display: flex;
  gap: 80px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-08__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.ld-08__label {
  color: rgba(255,255,255,.4);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Heart SVG pulse */

.ld-08__heart {
  width: 60px;
  height: 60px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ld-08__heart svg {
  width: 50px;
  height: 50px;
  animation: ld-08-heartbeat .8s ease-in-out infinite;
}

@keyframes ld-08-heartbeat {
  0%,
    100% {
    transform: scale(1);
  }

  14% {
    transform: scale(1.3);
  }

  28% {
    transform: scale(1);
  }

  42% {
    transform: scale(1.15);
  }

  70% {
    transform: scale(1);
  }
}
/* Ring pulse */

.ld-08__rings {
  width: 80px;
  height: 80px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ld-08__rings::before,
.ld-08__rings::after {
  content: '';
  position: absolute;
  border-radius: 50%;
  border: 2px solid var(--c1);
}

.ld-08__rings::before {
  width: 30px;
  height: 30px;
  animation: ld-08-ring-pulse 1.5s ease-out infinite;
}

.ld-08__rings::after {
  width: 30px;
  height: 30px;
  animation: ld-08-ring-pulse 1.5s ease-out infinite .4s;
}

.ld-08__rings i {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--c1);
  box-shadow: 0 0 10px var(--c1);
  animation: ld-08-heartbeat .8s ease-in-out infinite;
}

@keyframes ld-08-ring-pulse {
  0% {
    transform: scale(1);
    opacity: .8;
  }

  100% {
    transform: scale(3.5);
    opacity: 0;
  }
}
/* ECG line */

.ld-08__ecg {
  width: 140px;
  height: 50px;
  position: relative;
  overflow: hidden;
}

.ld-08__ecg svg {
  position: absolute;
  width: 200%;
  height: 100%;
  animation: ld-08-ecg 1.5s linear infinite;
}

@keyframes ld-08-ecg {
  0% {
    transform: translateX(0);
  }

  100% {
    transform: translateX(-50%);
  }
}
/* Sonar */

.ld-08__sonar {
  width: 80px;
  height: 80px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ld-08__sonar span {
  position: absolute;
  border-radius: 50%;
  border: 2px solid var(--c2);
  animation: ld-08-sonar 2s ease-out infinite;
}

.ld-08__sonar span:nth-child(1) {
  width: 20px;
  height: 20px;
  animation-delay: 0s;
}

.ld-08__sonar span:nth-child(2) {
  width: 20px;
  height: 20px;
  animation-delay: .5s;
}

.ld-08__sonar span:nth-child(3) {
  width: 20px;
  height: 20px;
  animation-delay: 1s;
}

.ld-08__sonar i {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--c2);
  box-shadow: 0 0 8px var(--c2);
}

@keyframes ld-08-sonar {
  0% {
    width: 8px;
    height: 8px;
    opacity: 1;
  }

  100% {
    width: 70px;
    height: 70px;
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-08__heart svg,
    .ld-08__rings::before,
    .ld-08__rings::after,
    .ld-08__rings i,
    .ld-08__ecg svg,
    .ld-08__sonar span {
    animation: none;
  }
}
```
