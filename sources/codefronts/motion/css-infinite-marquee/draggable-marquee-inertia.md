---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/draggable-marquee-inertia/"
title: "Draggable Marquee with Inertia — Grab, Throw, Auto-Resume"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "The tactile showpiece: a project-card marquee you can grab with mouse or touch and throw — it coasts with real inertia, decays back to cruising speed, and…"
has_js: "true"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Draggable Marquee with Inertia — Grab, Throw, Auto-Resume
Source: https://codefronts.com/motion/css-infinite-marquee/draggable-marquee-inertia/

The tactile showpiece: a project-card marquee you can grab with mouse or touch and throw — it coasts with real inertia, decays back to cruising speed, and never shows a seam because position wraps with modulo math. One requestAnimationFrame loop drives everything; CSS keyframes are deliberately NOT used, and the demo explains why that trade is correct here.
## HTML
```html
<section class="mqs-11" aria-label="Draggable marquee demo">
  <div class="mqs-11__inner">
    <h3 class="mqs-11__title">Selected work <span class="mqs-11__hint">— grab and throw</span></h3>
    <div class="mqs-11__viewport" id="mqs-11-vp">
      <div class="mqs-11__track" id="mqs-11-track">
        <span class="mqs-11__card" style="--c:#c2410c"><b>01</b>Meridian rebrand</span>
        <span class="mqs-11__card" style="--c:#4338ca"><b>02</b>Harbourly app</span>
        <span class="mqs-11__card" style="--c:#0f766e"><b>03</b>Fernwork design system</span>
        <span class="mqs-11__card" style="--c:#9d174d"><b>04</b>Baseline site</span>
        <span class="mqs-11__card" style="--c:#a16207"><b>05</b>Quill identity</span>
        <span class="mqs-11__card" style="--c:#c2410c" aria-hidden="true"><b>01</b>Meridian rebrand</span>
        <span class="mqs-11__card" style="--c:#4338ca" aria-hidden="true"><b>02</b>Harbourly app</span>
        <span class="mqs-11__card" style="--c:#0f766e" aria-hidden="true"><b>03</b>Fernwork design system</span>
        <span class="mqs-11__card" style="--c:#9d174d" aria-hidden="true"><b>04</b>Baseline site</span>
        <span class="mqs-11__card" style="--c:#a16207" aria-hidden="true"><b>05</b>Quill identity</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mqs-11,
.mqs-11 *,
.mqs-11 *::before,
.mqs-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-11 {
  min-height: 100vh;
  width: 100%;
  --gap: 18px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fafaf9;
  padding: 64px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow-x: clip;
}

.mqs-11__inner {
  width: min(940px,100%);
  margin-inline: auto;
}

.mqs-11__title {
  font-size: clamp(19px,3vw,24px);
  font-weight: 800;
  color: #1c1917;
  letter-spacing: -.02em;
  text-align: center;
  margin-bottom: 28px;
}

.mqs-11__hint {
  font-size: .6em;
  font-weight: 600;
  color: #a8a29e;
  letter-spacing: .02em;
  vertical-align: middle;
}

.mqs-11__viewport {
  overflow: hidden;
  cursor: grab;
  touch-action: pan-y;
  user-select: none;
  -webkit-user-select: none;
  padding-block: 8px;
  mask-image: linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent);
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent);
}

.mqs-11__viewport.is-dragging {
  cursor: grabbing;
}

.mqs-11__track {
  display: flex;
  gap: var(--gap);
  width: max-content;
  will-change: transform;
}

.mqs-11__card {
  flex: none;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 26px;
  width: 250px;
  min-height: 130px;
  background: #fff;
  border: 1.5px solid #e7e5e4;
  border-radius: 16px;
  padding: 18px 20px;
  font-size: 16px;
  font-weight: 700;
  color: #292524;
  letter-spacing: -.01em;
  transition: border-color .2s;
}

.mqs-11__card b {
  font-size: 12px;
  font-weight: 800;
  color: var(--c);
  letter-spacing: .1em;
}

.mqs-11__card:hover {
  border-color: var(--c);
}

@media (prefers-reduced-motion: reduce) {
  .mqs-11__viewport {
    overflow-x: auto;
  }
}
```

## JavaScript
```js
// One rAF loop owns position; CSS keyframes are deliberately not used (you can't hand a keyframe's clock to a pointer).
const vp = document.getElementById('mqs-11-vp');
const track = document.getElementById('mqs-11-track');
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
const CRUISE = 55;            // auto-scroll px/s
const FRICTION = 0.94;        // per-frame velocity decay after a throw
let x = 0, vel = 0, half = 0, dragging = false, moved = 0;
let lastPX = 0, lastT = 0, prev = performance.now();

const measure = () => { half = (track.scrollWidth + parseFloat(getComputedStyle(track).gap)) / 2; };
new ResizeObserver(measure).observe(track); measure();

function frame(now) {
  const dt = Math.min((now - prev) / 1000, 0.05); prev = now;
  if (!dragging) {
    if (Math.abs(vel) > CRUISE) { vel *= FRICTION; }                    // inertia decays…
    else { vel = REDUCED ? 0 : (vel < 0 ? -CRUISE : CRUISE); }          // …into cruise (or rest, if reduced motion)
    x += vel * dt;
  }
  if (half > 0) x = ((x % half) + half) % half;                         // modulo wrap = the seamless loop
  track.style.transform = 'translate3d(' + (-x) + 'px,0,0)';
  requestAnimationFrame(frame);
}
vel = REDUCED ? 0 : CRUISE;
requestAnimationFrame(frame);

vp.addEventListener('pointerdown', e => {
  dragging = true; moved = 0; vel = 0;
  lastPX = e.clientX; lastT = performance.now();
  vp.setPointerCapture(e.pointerId);                                    // drag survives leaving the viewport
  vp.classList.add('is-dragging');
});
vp.addEventListener('pointermove', e => {
  if (!dragging) return;
  const dx = e.clientX - lastPX, now = performance.now();
  x -= dx; moved += Math.abs(dx);
  if (now - lastT > 0) vel = (-dx / (now - lastT)) * 1000;              // sample velocity for the throw
  lastPX = e.clientX; lastT = now;
});
const release = e => {
  if (!dragging) return;
  dragging = false; vp.classList.remove('is-dragging');
  if (moved > 5) { const stop = ev => { ev.preventDefault(); ev.stopPropagation(); vp.removeEventListener('click', stop, true); }; vp.addEventListener('click', stop, true); } // drag ≠ click
};
vp.addEventListener('pointerup', release);
vp.addEventListener('pointercancel', release);
```
