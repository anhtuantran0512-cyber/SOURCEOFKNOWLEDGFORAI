---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/pure-css-parallax-hero-with-scroll-timeline/"
title: "Pure CSS Parallax Hero with Scroll Timeline"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A four-plane alpine hero where sky, far range, mid hills and foreground trees each drift at their own rate as the page scrolls — driven entirely by…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Parallax Hero with Scroll Timeline
Source: https://codefronts.com/motion/css-parallax-designs/pure-css-parallax-hero-with-scroll-timeline/

A four-plane alpine hero where sky, far range, mid hills and foreground trees each drift at their own rate as the page scrolls — driven entirely by animation-timeline: scroll(root), with no scroll listener anywhere. Reach for this when a marketing or editorial header needs real depth on the first screen and you do not want a rAF loop competing with the rest of the page.
## HTML
```html
<div class="plx-01">
  <header class="plx-01__hero">
    <div class="plx-01__sky plx-01__layer" aria-hidden="true"></div>
    <div class="plx-01__sun plx-01__layer" aria-hidden="true"></div>
    <svg class="plx-01__range plx-01__layer" viewBox="0 0 1440 380" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 380V214l128-64 96 52 118-88 122 96 132-62 148 84 126-58 136 70 114-46 120 62v120Z" fill="#3b2a63"/>
    </svg>
    <svg class="plx-01__hills plx-01__layer" viewBox="0 0 1440 300" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 300V196l150 44 140-72 168 78 152-52 174 66 156-44 178 62 162-34v56Z" fill="#26173f"/>
    </svg>
    <svg class="plx-01__trees plx-01__layer" viewBox="0 0 1440 220" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 220v-58l34 14 22-52 26 46 30-70 28 62 34-38 30 52 40-64 26 70 34-44 30 40 38-58 30 62 42-46 26 54 34-66 32 60 38-40 28 48 40-58 30 64 36-44 30 40 40-60 28 58 38-42 30 50 42-62 26 66 36-44 30 42 40-58 28 60 38-40 30 46 42-56 26 62 34-42 30 44 40-56 30 58 36-38 28 44 42-54 26 60 34-40 30 42 40-52 28 56 38-36 30 42 40-50 24 54V220Z" fill="#140b24"/>
    </svg>
    <div class="plx-01__copy">
      <p class="plx-01__eyebrow">Northridge Traverse · Field journal 04</p>
      <h1 class="plx-01__title">Four ridges<br>before the light</h1>
      <p class="plx-01__lede">Twenty-two kilometres on the high route, told in the order the ranges appear. Words and photographs by Alex Chen.</p>
      <a class="plx-01__cta" href="#plx-01-read">
        Start reading
        <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M8 2v10.2M3.6 8.2 8 12.6l4.4-4.4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </a>
    </div>
  </header>
  <main class="plx-01__body" id="plx-01-read">
    <section class="plx-01__section">
      <h2 class="plx-01__h2">The approach</h2>
      <p class="plx-01__p">The trail leaves the valley floor at four in the morning, which means the first two hours are spent inside a treeline you cannot see. The ranges only sort themselves into layers once you are above them — near hills first, then the long grey wall behind, then the sky.</p>
      <p class="plx-01__p">Depth on a screen works the same way. Nothing about a single silhouette says "far"; the distance is created by the difference in how fast one edge moves against another.</p>
    </section>
    <section class="plx-01__section">
      <h2 class="plx-01__h2">The high route</h2>
      <p class="plx-01__p">Above the saddle the path becomes scree for a kilometre and a half. Poles help. The wind arrives from the west at about the time the sun clears the far range, and the whole composition warms by two stops in under ten minutes.</p>
      <dl class="plx-01__facts">
        <div class="plx-01__fact"><dt>Distance</dt><dd>22.4 km</dd></div>
        <div class="plx-01__fact"><dt>Ascent</dt><dd>1,480 m</dd></div>
        <div class="plx-01__fact"><dt>Moving time</dt><dd>7 h 05</dd></div>
      </dl>
    </section>
    <section class="plx-01__section">
      <h2 class="plx-01__h2">Descent</h2>
      <p class="plx-01__p">Coming down, the layers collapse back into one another in reverse order until the treeline swallows the view again. Scroll back up and the hero does the same thing — the planes converge because their travel distances converge.</p>
    </section>
  </main>
</div>
```
## CSS
```css
.plx-01 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Avenir Next Condensed", "Oswald", "Haettenschweiler", system-ui, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --ink: #f4ecff;
  --muted: #a99bc4;
  --accent: #ff5da8;
  --deep: #0d0718;
  --plx-depth: 0.55;
  background: var(--deep);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-01 * {
  box-sizing: border-box;
}

@media (min-width: 760px) {
  .plx-01 {
    --plx-depth: 0.78;
  }
}

@media (min-width: 1180px) {
  .plx-01 {
    --plx-depth: 1;
  }
}

.plx-01__hero {
  position: relative;
  min-height: 100svh;
  display: flex;
  align-items: flex-end;
  overflow: clip;
  isolation: isolate;
}

.plx-01__layer {
  position: absolute;
  left: 0;
  right: 0;
  will-change: transform;
  pointer-events: none;
}

.plx-01__sky {
  top: -6%;
  bottom: -6%;
  background: linear-gradient(178deg, #170b2c 0%, #2c1350 34%, #6b2a63 68%, #c4536f 88%, #f0956c 100%);
}

.plx-01__sun {
  top: 42%;
  left: 50%;
  right: auto;
  inline-size: clamp(120px, 22vw, 260px);
  aspect-ratio: 1;
  translate: -50% 0;
  border-radius: 50%;
  background: radial-gradient(circle, #ffd9a8 0%, #ff9d6b 46%, rgba(255,120,110,0) 72%);
}

.plx-01__range {
  bottom: 26%;
  block-size: 44vh;
}

.plx-01__hills {
  bottom: 12%;
  block-size: 38vh;
}

.plx-01__trees {
  bottom: -1px;
  block-size: 30vh;
}

.plx-01__copy {
  position: relative;
  z-index: 3;
  inline-size: 100%;
  min-inline-size: 0;
  padding: clamp(28px, 6vw, 72px);
  padding-block-start: clamp(120px, 26vh, 300px);
  background: linear-gradient(to top, rgba(10,5,20,0.92) 0%, rgba(10,5,20,0.72) 52%, rgba(10,5,20,0) 100%);
}

.plx-01__eyebrow {
  margin: 0 0 14px;
  font: 600 11px/1 var(--font-body);
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-01__title {
  margin: 0 0 18px;
  font-family: var(--font-display);
  font-size: clamp(38px, 11vw, 108px);
  font-weight: 600;
  line-height: 0.92;
  letter-spacing: -0.01em;
  text-transform: uppercase;
}

.plx-01__lede {
  margin: 0 0 26px;
  max-inline-size: 34rem;
  font-size: clamp(15px, 3.6vw, 18px);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-01__cta {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 46px;
  padding: 0 22px;
  border-radius: 999px;
  background: var(--accent);
  color: #1b0413;
  font: 600 14px/1 var(--font-body);
  letter-spacing: 0.04em;
  text-decoration: none;
}

.plx-01__cta:hover {
  background: #ff86bf;
}

.plx-01__cta:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.plx-01__body {
  position: relative;
  z-index: 4;
  background: var(--deep);
  padding: clamp(48px, 9vw, 110px) clamp(24px, 6vw, 72px) 120px;
  display: grid;
  gap: clamp(48px, 8vw, 96px);
}

.plx-01__section {
  max-inline-size: 40rem;
  min-inline-size: 0;
}

.plx-01__h2 {
  margin: 0 0 16px;
  font-family: var(--font-display);
  font-size: clamp(24px, 5.4vw, 40px);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.01em;
}

.plx-01__p {
  margin: 0 0 16px;
  font-size: clamp(15px, 3.4vw, 17px);
  line-height: 1.72;
  color: #cdc0e2;
  text-wrap: pretty;
}

.plx-01__facts {
  margin: 26px 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: 12px 40px;
}

.plx-01__fact {
  min-inline-size: 0;
}

.plx-01__fact dt {
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-01__fact dd {
  margin: 8px 0 0;
  font-family: var(--font-display);
  font-size: 26px;
  color: var(--accent);
}

@supports (animation-timeline: scroll()) {
  .plx-01__sky {
    animation: plx-01-sky linear both;
    animation-timeline: scroll(root);
  }

  .plx-01__sun {
    animation: plx-01-sun linear both;
    animation-timeline: scroll(root);
  }

  .plx-01__range {
    animation: plx-01-range linear both;
    animation-timeline: scroll(root);
  }

  .plx-01__hills {
    animation: plx-01-hills linear both;
    animation-timeline: scroll(root);
  }

  .plx-01__trees {
    animation: plx-01-trees linear both;
    animation-timeline: scroll(root);
  }
}

@keyframes plx-01-sky {
  to {
    transform: translateY(calc(-40px * var(--plx-depth)));
  }
}

@keyframes plx-01-sun {
  to {
    transform: translateY(calc(-150px * var(--plx-depth))) scale(0.9);
  }
}

@keyframes plx-01-range {
  to {
    transform: translateY(calc(-120px * var(--plx-depth)));
  }
}

@keyframes plx-01-hills {
  to {
    transform: translateY(calc(-260px * var(--plx-depth)));
  }
}

@keyframes plx-01-trees {
  to {
    transform: translateY(calc(-420px * var(--plx-depth)));
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-01__layer {
    animation: none !important;
    transform: none !important;
    will-change: auto;
  }
}

@media (max-width: 640px) {
  .plx-01__range {
    block-size: 32vh;
  }

  .plx-01__hills {
    block-size: 28vh;
  }

  .plx-01__trees {
    block-size: 22vh;
  }
}
```
