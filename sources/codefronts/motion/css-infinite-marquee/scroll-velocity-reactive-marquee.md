---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/scroll-velocity-reactive-marquee/"
title: "Scroll-Velocity Reactive Marquee — Speed & Skew Follow the Page"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "The award-site flourish: a giant outlined-text marquee that idles at a lazy drift, then accelerates, skews and even reverses with the user's scroll — scroll…"
has_js: "true"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Velocity Reactive Marquee — Speed & Skew Follow the Page
Source: https://codefronts.com/motion/css-infinite-marquee/scroll-velocity-reactive-marquee/

The award-site flourish: a giant outlined-text marquee that idles at a lazy drift, then accelerates, skews and even reverses with the user's scroll — scroll down fast and the words whip left with a speed-lean; flick up and they swing back. One rAF loop, one scroll listener, and lerp smoothing doing all the choreography.
## HTML
```html
<section class="mqs-12" aria-label="Scroll velocity marquee demo">
  <p class="mqs-12__hint">Scroll this page — fast, slow, then back up ↑</p>
  <div class="mqs-12__stage">
    <div class="mqs-12__viewport">
      <div class="mqs-12__track" id="mqs-12-track">
        <span class="mqs-12__word">Velocity</span><span class="mqs-12__word mqs-12__word--ghost">Motion</span><span class="mqs-12__word">Design</span><span class="mqs-12__word mqs-12__word--ghost">Craft</span>
        <span class="mqs-12__word" aria-hidden="true">Velocity</span><span class="mqs-12__word mqs-12__word--ghost" aria-hidden="true">Motion</span><span class="mqs-12__word" aria-hidden="true">Design</span><span class="mqs-12__word mqs-12__word--ghost" aria-hidden="true">Craft</span>
      </div>
    </div>
  </div>
  <p class="mqs-12__hint">Notice it reverses when you scroll up</p>
</section>
```
## CSS
```css
.mqs-12,
.mqs-12 *,
.mqs-12 *::before,
.mqs-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-12 {
  width: 100%;
  min-height: 100vh;
  --gap: 48px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #101014;
  padding-block: 0 200vh;
}

.mqs-12__hint {
  text-align: center;
  font-size: 12px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #52525b;
  padding-block: 24px;
}

.mqs-12__stage {
  position: sticky;
  top: 15vh;
  padding-block: 30px;
  border-block: 1px solid #27272a;
  background: #101014;
}

.mqs-12__viewport {
  overflow: hidden;
}

.mqs-12__track {
  display: flex;
  align-items: baseline;
  gap: var(--gap);
  width: max-content;
  will-change: transform;
}

.mqs-12__word {
  flex: none;
  font-size: clamp(56px,9vw,120px);
  font-weight: 800;
  letter-spacing: -.04em;
  line-height: 1;
  color: #f4f4f5;
}

.mqs-12__word--ghost {
  color: transparent;
  -webkit-text-stroke: 2px #3f3f46;
}

@media (prefers-reduced-motion: reduce) {
  .mqs-12 {
    width: 100%;
    padding-block: 64px;
  }
}
```

## JavaScript
```js
// The scroll listener only RECORDS velocity; rAF does all the writing (never write transforms in a scroll handler).
const track = document.getElementById('mqs-12-track');
const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
const BASE = 60;      // idle drift px/s
const FACTOR = 0.25;  // how hard page scroll drives the marquee
let x = 0, half = 0, velocity = 0, smooth = 0;
let lastScroll = window.scrollY, prev = performance.now();

const measure = () => { half = (track.scrollWidth + parseFloat(getComputedStyle(track).gap)) / 2; };
new ResizeObserver(measure).observe(track); measure();

if (!REDUCED) {
  window.addEventListener('scroll', () => {
    velocity += (window.scrollY - lastScroll) * 12;   // signed: up-scroll reverses the marquee
    lastScroll = window.scrollY;
  }, { passive: true });

  requestAnimationFrame(function frame(now) {
    const dt = Math.min((now - prev) / 1000, 0.05); prev = now;
    velocity *= 0.9;                                   // decay: effect relaxes when scrolling stops
    smooth += (velocity - smooth) * 0.08;              // lerp: spiky wheel events become liquid motion
    x += (BASE + smooth * FACTOR) * dt;
    if (half > 0) x = ((x % half) + half) % half;      // modulo wrap = no seam at any speed
    const skew = Math.max(-12, Math.min(12, smooth * -0.02));
    track.style.transform = 'translate3d(' + (-x) + 'px,0,0) skewX(' + skew + 'deg)';
    requestAnimationFrame(frame);
  });
}
```
