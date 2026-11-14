---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/css-zoom-in-depth-parallax-on-scroll/"
title: "Zoom In Depth Parallax on Scroll"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A film-title opening: the frame starts wide and the camera flies into the image as you scroll, while the title, credits and letterbox bars resolve on top of it."
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Zoom In Depth Parallax on Scroll
Source: https://codefronts.com/motion/css-parallax-designs/css-zoom-in-depth-parallax-on-scroll/

A film-title opening: the frame starts wide and the camera flies into the image as you scroll, while the title, credits and letterbox bars resolve on top of it. Scale and opacity are the only animated properties, and a pure-CSS switch flips between a black-cinema and a bone-cinema grade.
## HTML
```html
<div class="plx-21">
  <div class="plx-21__runway">
    <div class="plx-21__stage">
      <img class="plx-21__plate" src="https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1600&auto=format&fit=crop" alt="Snow-covered peak under the Milky Way" loading="eager" decoding="async">
      <span class="plx-21__bar plx-21__bar--top" aria-hidden="true"></span>
      <span class="plx-21__bar plx-21__bar--bottom" aria-hidden="true"></span>
      <div class="plx-21__switch">
        <input class="plx-21__box" type="checkbox" id="plx-21-grade">
        <label class="plx-21__label" for="plx-21-grade">
          <span class="plx-21__dot" aria-hidden="true"></span>
          <span class="plx-21__g plx-21__g--night">Night grade</span><span class="plx-21__g plx-21__g--bone">Bone grade</span>
        </label>
      </div>
      <div class="plx-21__title">
        <p class="plx-21__studio">Meridian Pictures presents</p>
        <h1 class="plx-21__h1">The Cold Return</h1>
        <span class="plx-21__rule" aria-hidden="true"></span>
        <p class="plx-21__credits">Photography Alex Chen · Sound Sam Rivera · Edited by Priya Sharma</p>
      </div>
    </div>
  </div>
  <main class="plx-21__body">
    <section class="plx-21__section">
      <h2 class="plx-21__h2">Synopsis</h2>
      <p class="plx-21__p">A survey team returns to a station that has been unmanned for eleven winters, and finds the log continued in someone's handwriting. Shot over four weeks at 2,900 metres with a crew of nine.</p>
    </section>
    <section class="plx-21__section">
      <h2 class="plx-21__h2">Format</h2>
      <p class="plx-21__p">2.39:1, 4-perf 35mm, no digital intermediate beyond the grade. Runs 114 minutes.</p>
    </section>
    <section class="plx-21__section">
      <h2 class="plx-21__h2">Screenings</h2>
      <p class="plx-21__p">Festival run opens in March; a limited 35mm tour follows in eleven cities. Scroll back up and the camera pulls out again — the zoom is bound to position, not to a trigger.</p>
    </section>
  </main>
</div>
```
## CSS
```css
.plx-21 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Didot", "Hoefler Text", "Palatino Linotype", Georgia, serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --void: #000000;
  --ink: #f7f2e7;
  --muted: #9c948a;
  --gold: #d9a94a;
  --bar: #000000;
  background: var(--void);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-21 * {
  box-sizing: border-box;
}

.plx-21__runway {
  block-size: 300svh;
}

.plx-21__stage {
  position: sticky;
  top: 0;
  block-size: 100svh;
  overflow: clip;
  display: grid;
  place-items: center;
  background: var(--void);
}

.plx-21__plate {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  transform-origin: 52% 44%;
  will-change: transform;
  opacity: 0.92;
}

.plx-21__bar {
  position: absolute;
  inset-inline: 0;
  block-size: 12svh;
  background: var(--bar);
  z-index: 3;
  pointer-events: none;
}

.plx-21__bar--top {
  inset-block-start: 0;
}

.plx-21__bar--bottom {
  inset-block-end: 0;
}

.plx-21__switch {
  position: absolute;
  z-index: 5;
  inset-block-start: calc(12svh + 14px);
  inset-inline-end: 16px;
}

.plx-21__box {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: clip;
}

.plx-21__label {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 15px;
  border-radius: 2px;
  border: 1px solid rgba(217,169,74,0.55);
  background: rgba(0,0,0,0.45);
  color: var(--ink);
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  cursor: pointer;
}

.plx-21__box:focus-visible + .plx-21__label {
  outline: 2px solid var(--gold);
  outline-offset: 3px;
}

.plx-21__dot {
  inline-size: 8px;
  block-size: 8px;
  border-radius: 50%;
  background: currentColor;
  opacity: 0.8;
}

.plx-21__g--bone {
  display: none;
}

.plx-21__title {
  position: relative;
  z-index: 4;
  padding: clamp(20px, 5vw, 60px);
  text-align: center;
  display: grid;
  justify-items: center;
  gap: 14px;
  max-inline-size: 42rem;
  min-inline-size: 0;
}

.plx-21__studio {
  margin: 0;
  font: 500 10px/1 var(--font-body);
  letter-spacing: 0.4em;
  text-transform: uppercase;
  color: var(--gold);
  text-shadow: 0 1px 12px rgba(0,0,0,0.9);
}

.plx-21__h1 {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(32px, 8.4vw, 92px);
  font-weight: 400;
  line-height: 1;
  letter-spacing: 0.02em;
  text-shadow: 0 2px 30px rgba(0,0,0,0.85);
}

.plx-21__rule {
  inline-size: clamp(60px, 18vw, 150px);
  block-size: 1px;
  background: var(--gold);
}

.plx-21__credits {
  margin: 0;
  font-size: clamp(11px, 2.6vw, 13px);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: rgba(247,242,231,0.86);
  text-shadow: 0 1px 12px rgba(0,0,0,0.9);
  text-wrap: pretty;
}

.plx-21__body {
  position: relative;
  background: var(--void);
  padding: clamp(44px, 8vw, 104px) clamp(22px, 6vw, 76px) 130px;
  display: grid;
  gap: clamp(32px, 6vw, 62px);
  border-top: 1px solid #191919;
}

.plx-21__section {
  max-inline-size: 38rem;
  min-inline-size: 0;
}

.plx-21__h2 {
  margin: 0 0 12px;
  font-family: var(--font-display);
  font-size: clamp(19px, 4vw, 28px);
  font-weight: 400;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--gold);
}

.plx-21__p {
  margin: 0;
  font-size: clamp(15px, 3.4vw, 17px);
  line-height: 1.76;
  color: #c9c2b7;
  text-wrap: pretty;
}

.plx-21:has(.plx-21__box:checked) {
  --void: #f2ece0;
  --ink: #14120f;
  --muted: #6b6357;
  --gold: #8a5a1f;
  --bar: #e2d9c8;
}

.plx-21:has(.plx-21__box:checked) .plx-21__plate {
  filter: sepia(0.24) brightness(1.06);
}

.plx-21:has(.plx-21__box:checked) .plx-21__label {
  background: rgba(255,255,255,0.6);
}

.plx-21:has(.plx-21__box:checked) .plx-21__h1,
.plx-21:has(.plx-21__box:checked) .plx-21__studio,
.plx-21:has(.plx-21__box:checked) .plx-21__credits {
  text-shadow: 0 1px 10px rgba(255,255,255,0.8);
}

.plx-21:has(.plx-21__box:checked) .plx-21__credits {
  color: #2c261d;
}

.plx-21:has(.plx-21__box:checked) .plx-21__p {
  color: #3b342b;
}

.plx-21:has(.plx-21__box:checked) .plx-21__g--night {
  display: none;
}

.plx-21:has(.plx-21__box:checked) .plx-21__g--bone {
  display: inline;
}

.plx-21[data-theme="light"] {
  --void: #f2ece0;
  --ink: #14120f;
  --gold: #8a5a1f;
  --bar: #e2d9c8;
}

.plx-21[data-theme="dark"] {
  --void: #000000;
  --ink: #f7f2e7;
  --gold: #d9a94a;
  --bar: #000000;
}

@media (prefers-color-scheme: light) {
  .plx-21 {
    --void: #000000;
    --ink: #f7f2e7;
    --gold: #d9a94a;
    --bar: #000000;
  }

  .plx-21 .plx-21__g--night {
    display: inline;
  }

  .plx-21 .plx-21__g--bone {
    display: none;
  }

  .plx-21:has(.plx-21__box:checked) {
    --void: #f2ece0;
    --ink: #14120f;
    --gold: #8a5a1f;
    --bar: #e2d9c8;
  }

  .plx-21:has(.plx-21__box:checked) .plx-21__g--night {
    display: none;
  }

  .plx-21:has(.plx-21__box:checked) .plx-21__g--bone {
    display: inline;
  }
}

@media (prefers-color-scheme: dark) {
  .plx-21 {
    --void: #000000;
    --ink: #f7f2e7;
    --gold: #d9a94a;
    --bar: #000000;
  }

  .plx-21 .plx-21__g--night {
    display: inline;
  }

  .plx-21 .plx-21__g--bone {
    display: none;
  }

  .plx-21:has(.plx-21__box:checked) {
    --void: #f2ece0;
    --ink: #14120f;
    --gold: #8a5a1f;
    --bar: #e2d9c8;
  }

  .plx-21:has(.plx-21__box:checked) .plx-21__g--night {
    display: none;
  }

  .plx-21:has(.plx-21__box:checked) .plx-21__g--bone {
    display: inline;
  }
}

@supports (animation-timeline: scroll()) {
  .plx-21__title > * {
    opacity: 0;
  }

  .plx-21__plate {
    animation: plx-21-fly linear both;
    animation-timeline: scroll(root);
    animation-range: 0 74%;
  }

  .plx-21__bar {
    animation: plx-21-aperture linear both;
    animation-timeline: scroll(root);
    animation-range: 0 40%;
  }

  .plx-21__studio {
    animation: plx-21-in linear both;
    animation-timeline: scroll(root);
    animation-range: 4% 22%;
  }

  .plx-21__h1 {
    animation: plx-21-in linear both;
    animation-timeline: scroll(root);
    animation-range: 8% 28%;
  }

  .plx-21__rule {
    animation: plx-21-wide linear both;
    animation-timeline: scroll(root);
    animation-range: 20% 36%;
  }

  .plx-21__credits {
    animation: plx-21-in linear both;
    animation-timeline: scroll(root);
    animation-range: 30% 48%;
  }
}

@keyframes plx-21-fly {
  from {
    transform: scale(1);
  }

  to {
    transform: scale(1.65);
  }
}

@keyframes plx-21-aperture {
  from {
    block-size: 12svh;
  }

  to {
    block-size: 6svh;
  }
}

@keyframes plx-21-in {
  from {
    opacity: 0;
    transform: translateY(14px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes plx-21-wide {
  from {
    opacity: 0;
    transform: scaleX(0.2);
  }

  to {
    opacity: 1;
    transform: scaleX(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-21__plate,
    .plx-21__bar,
    .plx-21__title > * {
    animation: none !important;
    transform: none !important;
    opacity: 1 !important;
    will-change: auto;
  }

  .plx-21__bar {
    block-size: 8svh;
  }
}
```
