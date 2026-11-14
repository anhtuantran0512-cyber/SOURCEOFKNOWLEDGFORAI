---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-dot-trail-cursor-hover-effect/"
title: "CSS Dot Trail Cursor Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "A trail of fading dot particles follows the cursor inside a container — four trail styles including color rainbow, size decay, and comet tail."
has_js: "true"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Dot Trail Cursor Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-dot-trail-cursor-hover-effect/

A trail of fading dot particles follows the cursor inside a container — four trail styles including color rainbow, size decay, and comet tail.
## HTML
```html
<div class="hv-29">
  <p class="hv-29__label">Dot Trail Cursor — 4 Styles</p>
  <div class="hv-29__grid">

    <div class="hv-29__zone hv-29__zone--classic" data-trail="classic">
      <span class="hv-29__hint">Classic Fade</span>
    </div>

    <div class="hv-29__zone hv-29__zone--rainbow" data-trail="rainbow">
      <span class="hv-29__hint">Rainbow</span>
    </div>

    <div class="hv-29__zone hv-29__zone--comet" data-trail="comet">
      <span class="hv-29__hint">Comet Tail</span>
    </div>

    <div class="hv-29__zone hv-29__zone--sparkle" data-trail="sparkle">
      <span class="hv-29__hint">Sparkle</span>
    </div>

  </div>
</div>
```
## CSS
```css
.hv-29,
.hv-29 *,
.hv-29 *::before,
.hv-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-29 {
  font-family: system-ui, sans-serif;
  background: #080810;
  padding: 2rem;
  min-height: 100vh;
  user-select: none;
}

.hv-29__label {
  text-align: center;
  color: #444;
  font-size: .72rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}

.hv-29__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  max-width: 700px;
  margin: 0 auto;
}

.hv-29__zone {
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  aspect-ratio: 4/3;
  border: 1px solid #1a1a2a;
  cursor: none;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hv-29__zone--classic {
  background: #0d0d18;
}

.hv-29__zone--rainbow {
  background: #0d0d18;
}

.hv-29__zone--comet {
  background: #0a0a14;
}

.hv-29__zone--sparkle {
  background: #0c0c18;
}

.hv-29__hint {
  color: #2a2a40;
  font-size: .75rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  pointer-events: none;
}
/* ── Dot base ── */

.hv-29__dot {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  transform: translate(-50%, -50%);
  will-change: transform, opacity;
}
/* ── Classic: white dots fade & shrink ── */

@keyframes hv-29-classic {
  0% {
    opacity: .9;
    transform: translate(-50%,-50%) scale(1);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) scale(0);
  }
}

.hv-29__zone--classic .hv-29__dot {
  width: 8px;
  height: 8px;
  background: #fff;
  animation: hv-29-classic .6s ease-out forwards;
}
/* ── Rainbow: hue-rotated dots ── */

@keyframes hv-29-rainbow {
  0% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(1.1);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) scale(0.1);
  }
}

.hv-29__zone--rainbow .hv-29__dot {
  width: 10px;
  height: 10px;
  animation: hv-29-rainbow .7s ease-out forwards;
  /* background set inline via JS */
}
/* ── Comet: elongated fade to right ── */

@keyframes hv-29-comet {
  0% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(1, 1);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) scale(3, .3);
  }
}

.hv-29__zone--comet .hv-29__dot {
  width: 12px;
  height: 4px;
  background: linear-gradient(90deg, rgba(100,180,255,0), rgba(100,180,255,1));
  border-radius: 2px;
  animation: hv-29-comet .5s ease-out forwards;
}
/* ── Sparkle: star-like burst ── */

@keyframes hv-29-sparkle {
  0% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(0) rotate(0deg);
  }

  60% {
    opacity: 1;
    transform: translate(-50%,-50%) scale(1.3) rotate(60deg);
  }

  100% {
    opacity: 0;
    transform: translate(-50%,-50%) scale(0.4) rotate(90deg);
  }
}

.hv-29__zone--sparkle .hv-29__dot {
  width: 10px;
  height: 10px;
  clip-path: polygon(50% 0%,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%);
  background: #f7d060;
  animation: hv-29-sparkle .65s ease-out forwards;
}

@media (prefers-reduced-motion: reduce) {
  .hv-29__dot {
    animation-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function () {
  const zones = document.querySelectorAll('.hv-29__zone');
  const RAINBOW = ['#ff6b6b','#ffa94d','#ffd43b','#69db7c','#4dabf7','#cc5de8','#f783ac'];
  let hueIndex = 0;
  let rafId = null;
  let pendingZone = null;
  let pendingX = 0;
  let pendingY = 0;

  function spawnDot(zone, x, y) {
    const trail = zone.dataset.trail;
    const dot = document.createElement('span');
    dot.className = 'hv-29__dot';
    dot.style.left = x + 'px';
    dot.style.top  = y + 'px';
    if (trail === 'rainbow') {
      dot.style.background = RAINBOW[hueIndex % RAINBOW.length];
      hueIndex++;
    }
    zone.appendChild(dot);
    dot.addEventListener('animationend', () => dot.remove(), { once: true });
  }

  function onMove(e) {
    const zone = e.currentTarget;
    const rect = zone.getBoundingClientRect();
    pendingX = e.clientX - rect.left;
    pendingY = e.clientY - rect.top;
    pendingZone = zone;
    if (!rafId) {
      rafId = requestAnimationFrame(() => {
        if (pendingZone) spawnDot(pendingZone, pendingX, pendingY);
        rafId = null;
      });
    }
  }

  zones.forEach(zone => {
    zone.addEventListener('mousemove', onMove);
    zone.addEventListener('mouseleave', () => { pendingZone = null; });
  });
})();
```
