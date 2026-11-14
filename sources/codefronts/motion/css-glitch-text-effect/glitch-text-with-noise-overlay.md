---
source: "codefronts"
url: "https://codefronts.com/motion/css-glitch-text-effect/glitch-text-with-noise-overlay/"
title: "Glitch Text with Noise Overlay"
section: "motion"
category: "css-glitch-text-effect"
category_name: "CSS Glitch Text Effects"
description: "Animated pixel noise generated every frame by a canvas element fills the background, while the overlaid headline uses mix-blend-mode:screen to cut through…"
has_js: "true"
---

Here's a working CSS Glitch Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Text with Noise Overlay
Source: https://codefronts.com/motion/css-glitch-text-effect/glitch-text-with-noise-overlay/

Animated pixel noise generated every frame by a canvas element fills the background, while the overlaid headline uses mix-blend-mode:screen to cut through the grain with a warm orange channel-split glitch that erupts periodically.
## HTML
```html
<div class="gt-13">
  <canvas class="gt-13__noise" id="gt-13-noise"></canvas>
  <div class="gt-13__stage">
    <div class="gt-13__word" data-text="FRACTAL">FRACTAL</div>
    <div class="gt-13__sub">noise · signal · entropy</div>
  </div>
</div>
```
## CSS
```css
.gt-13,
.gt-13 *,
.gt-13 *::before,
.gt-13 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-13 ::selection {
  background: #f97316;
  color: #000;
}

.gt-13 {
  --orange: #f97316;
  --yellow: #fbbf24;
  --bg: #09060a;
  --text: #fff9f0;
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0;
  padding: 48px 20px;
  font-family: 'Inter', system-ui, sans-serif;
  position: relative;
  overflow: hidden;
}
/* Noise canvas fills the bg. opacity bumped 0.18 -> 0.35 so the
   warm-grain texture is clearly visible behind the title even in
   static thumbnails; the live demo still feels atmospheric, the
   gallery card now actually advertises the noise overlay effect. */

.gt-13__noise {
  position: absolute;
  inset: 0;
  opacity: 0.35;
  pointer-events: none;
  z-index: 0;
}

.gt-13__stage {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
/* Main word cuts through noise. Font scaled up clamp min 64px (was
   48px) and max 120px (was 96px) so the title fills more of the
   capture frame. Permanent dual-shadow (orange offset left, yellow
   offset right) gives a baseline chromatic split so the gallery
   thumbnail reads as a glitch even when caught between the slice
   keyframes; the animated slice pseudos still layer on top during
   live playback. */

.gt-13__word {
  position: relative;
  font-size: clamp(64px, 12vw, 120px);
  font-weight: 900;
  letter-spacing: 4px;
  text-transform: uppercase;
  color: var(--text);
  /* Text cuts through noise via mix-blend-mode */
  mix-blend-mode: screen;
  text-shadow: -3px 0 0 rgba(249,115,22,0.85), 3px 0 0 rgba(251,191,36,0.85), 0 0 20px rgba(249,115,22,0.4);
  animation: gt-13-main-glitch 4s steps(1) infinite;
}

.gt-13__word::before {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  letter-spacing: inherit;
  color: var(--orange);
  mix-blend-mode: screen;
  clip-path: polygon(0 15%, 100% 15%, 100% 38%, 0 38%);
  animation: gt-13-slice-a 4s steps(1) infinite;
}

.gt-13__word::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  font: inherit;
  letter-spacing: inherit;
  color: var(--yellow);
  mix-blend-mode: screen;
  clip-path: polygon(0 62%, 100% 62%, 100% 85%, 0 85%);
  animation: gt-13-slice-b 4s steps(1) infinite;
}

@keyframes gt-13-main-glitch {
  0%,
    80%,
    100% {
    transform: translateX(0);
  }

  82% {
    transform: translateX(-6px) skewX(-2deg);
  }

  84% {
    transform: translateX(5px);
  }

  86% {
    transform: translateX(-2px) skewX(1deg);
  }

  88% {
    transform: translateX(0);
  }
}

@keyframes gt-13-slice-a {
  0%,
    80%,
    100% {
    opacity: 0;
    transform: translateX(0);
  }

  82% {
    opacity: 1;
    transform: translateX(-14px);
    clip-path: polygon(0 10%, 100% 10%, 100% 35%, 0 35%);
  }

  84% {
    opacity: 1;
    transform: translateX(10px);
    clip-path: polygon(0 18%, 100% 18%, 100% 40%, 0 40%);
  }

  86% {
    opacity: 0.6;
    transform: translateX(-4px);
  }

  88% {
    opacity: 0;
  }
}

@keyframes gt-13-slice-b {
  0%,
    80%,
    100% {
    opacity: 0;
    transform: translateX(0);
  }

  82% {
    opacity: 1;
    transform: translateX(16px);
    clip-path: polygon(0 65%, 100% 65%, 100% 88%, 0 88%);
  }

  84% {
    opacity: 1;
    transform: translateX(-10px);
    clip-path: polygon(0 58%, 100% 58%, 100% 82%, 0 82%);
  }

  86% {
    opacity: 0.6;
    transform: translateX(5px);
  }

  88% {
    opacity: 0;
  }
}

.gt-13__sub {
  font-size: 12px;
  letter-spacing: 5px;
  color: rgba(249,115,22,0.5);
  text-transform: uppercase;
  mix-blend-mode: screen;
}

@media (prefers-reduced-motion: reduce) {
  .gt-13__word,
    .gt-13__word::before,
    .gt-13__word::after {
    animation: none;
  }

  .gt-13__word::before,
    .gt-13__word::after {
    opacity: 0;
  }

  .gt-13__noise {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const canvas = document.getElementById('gt-13-noise');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let animId;

  function resize() {
    const parent = canvas.parentElement;
    canvas.width  = parent.offsetWidth;
    canvas.height = parent.offsetHeight;
  }

  function drawNoise() {
    const w = canvas.width;
    const h = canvas.height;
    const imageData = ctx.createImageData(w, h);
    const data = imageData.data;
    for (let i = 0; i < data.length; i += 4) {
      const v = Math.random() * 255 | 0;
      data[i]   = v;
      data[i+1] = (v * 0.6) | 0; // warmer grain
      data[i+2] = (v * 0.3) | 0;
      data[i+3] = 255;
    }
    ctx.putImageData(imageData, 0, 0);
    animId = requestAnimationFrame(drawNoise);
  }

  resize();
  drawNoise();
  window.addEventListener('resize', resize);

  /* Pause when off-screen for perf */
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) { cancelAnimationFrame(animId); animId = null; }
      else if (!animId) drawNoise();
    });
  });
  obs.observe(canvas);
})();
```
