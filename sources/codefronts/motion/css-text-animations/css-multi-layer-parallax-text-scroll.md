---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-multi-layer-parallax-text-scroll/"
title: "CSS Multi Layer Parallax Text Scroll"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Depth from speed difference, twice over: a scroll-timeline version where a giant outlined word, a photo card and the headline all scrub different distances,…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Multi Layer Parallax Text Scroll
Source: https://codefronts.com/motion/css-text-animations/css-multi-layer-parallax-text-scroll/

Depth from speed difference, twice over: a scroll-timeline version where a giant outlined word, a photo card and the headline all scrub different distances, and the classic perspective/translateZ trick that parallaxes in every browser shipped this decade.
## HTML
```html
<div class="cat-05-group">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-05a" aria-label="Multi layer parallax driven by scroll timeline">
  <div class="cat-05a__tall">
    <div class="cat-05a__pin">
      <span class="cat-05a__giant" aria-hidden="true">DEPTH</span>
      <figure class="cat-05a__card">
        <img src="https://picsum.photos/seed/altitude/900/640" alt="Atmospheric placeholder photograph" loading="lazy">
        <figcaption>layer 2 · drifts 40px</figcaption>
      </figure>
      <h1 class="cat-05a__front">Speed difference<br>is depth.</h1>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-05b" aria-label="Perspective translateZ parallax scroller">
  <div class="cat-05b__scroller" tabindex="0">
    <div class="cat-05b__scene">
      <span class="cat-05b__deep" aria-hidden="true">PARALLAX</span>
      <div class="cat-05b__fg">
        <h1>This inner pane scrolls.</h1>
        <p>The giant word behind sits at translateZ(-1px) scale(2) — the browser's own perspective projection moves it at half speed. Works in every engine since 2013.</p>
        <p class="cat-05b__tail">↑ scroll inside this pane ↑</p>
      </div>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.cat-05-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.cat-05-group > section {
  width: 100%;
}

.cat-05a,
.cat-05a *,
.cat-05a *::before,
.cat-05a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-05a {
  width: 100%;
  background: #101217;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-05a__tall {
  height: 250vh;
  view-timeline-name: --cat20a-par;
}

.cat-05a__pin {
  position: sticky;
  top: 0;
  height: 100vh;
  display: grid;
  place-items: center;
  overflow: hidden;
}

.cat-05a__giant {
  position: absolute;
  font-family: 'Anton',Impact,sans-serif;
  font-size: clamp(140px,30vw,380px);
  letter-spacing: .02em;
  color: transparent;
  -webkit-text-stroke: 1.5px rgba(150,170,210,.22);
  user-select: none;
}

.cat-05a__card {
  position: relative;
  width: min(400px,72vw);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 50px 100px -40px rgb(0 0 0/.8);
  transform: rotate(-3deg);
}

.cat-05a__card img {
  display: block;
  width: 100%;
  height: auto;
  filter: saturate(.85) contrast(1.05);
}

.cat-05a__card figcaption {
  position: absolute;
  left: 14px;
  bottom: 12px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10.5px;
  letter-spacing: .14em;
  color: rgba(255,255,255,.85);
  background: rgb(10 14 22/.55);
  padding: 6px 10px;
  border-radius: 6px;
  backdrop-filter: blur(6px);
}

.cat-05a__front {
  position: absolute;
  left: 50%;
  top: 58%;
  transform: translateX(-50%);
  font-size: clamp(30px,4.6vw,54px);
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: -.015em;
  color: #f0f3fa;
  text-align: center;
  text-shadow: 0 18px 50px rgb(0 0 0/.75);
}

@supports (animation-timeline: view()) {
  .cat-05a__giant {
    animation: cat-05a-drift linear both;
    animation-timeline: --cat20a-par;
    --d: 130px;
  }

  .cat-05a__card {
    animation: cat-05a-driftr linear both;
    animation-timeline: --cat20a-par;
    --d: 45px;
  }

  .cat-05a__front {
    animation: cat-05a-driftx linear both;
    animation-timeline: --cat20a-par;
    --d: -60px;
  }
}

@keyframes cat-05a-drift {
  from {
    transform: translateY(var(--d));
  }

  to {
    transform: translateY(calc(var(--d)*-1));
  }
}

@keyframes cat-05a-driftr {
  from {
    transform: rotate(-3deg) translateY(var(--d));
  }

  to {
    transform: rotate(-3deg) translateY(calc(var(--d)*-1));
  }
}

@keyframes cat-05a-driftx {
  from {
    transform: translateX(-50%) translateY(var(--d));
  }

  to {
    transform: translateX(-50%) translateY(calc(var(--d)*-1));
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-05a__giant,
    .cat-05a__card,
    .cat-05a__front {
    animation: none;
  }
}

.cat-05b,
.cat-05b *,
.cat-05b *::before,
.cat-05b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-05b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #0d0f0b;
  padding: 0;
}

.cat-05b__scroller {
  width: 100%;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
  perspective: 1px;
  perspective-origin: 50% 50%;
}

.cat-05b__scroller:focus-visible {
  outline: 3px solid oklch(0.88 0.2 130);
  outline-offset: -3px;
}

.cat-05b__scene {
  position: relative;
  min-height: 220vh;
  transform-style: preserve-3d;
}

.cat-05b__deep {
  position: absolute;
  top: 26%;
  left: 50%;
  transform: translate(-50%,0) translateZ(-1px) scale(2);
  font-family: 'Anton',Impact,sans-serif;
  font-size: clamp(90px,20vw,240px);
  color: transparent;
  -webkit-text-stroke: 1.5px rgba(190,230,140,.28);
  white-space: nowrap;
  user-select: none;
}

.cat-05b__fg {
  position: relative;
  margin: 120vh auto 12vh;
  width: min(620px,88%);
  background: #161a12;
  border: 1px solid rgba(190,230,140,.2);
  border-radius: 20px;
  padding: 44px 46px;
  display: grid;
  gap: 16px;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
  color: #eef4e2;
  box-shadow: 0 40px 90px -40px rgb(0 0 0/.9);
}

.cat-05b__fg h1 {
  font-size: clamp(24px,3.4vw,36px);
  font-weight: 700;
  letter-spacing: -.01em;
}

.cat-05b__fg p {
  font-size: 15.5px;
  line-height: 1.65;
  color: rgba(238,244,226,.72);
}

.cat-05b__tail {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(190,230,140,.5);
}

@media (prefers-reduced-motion: reduce) {
  .cat-05b__deep {
    transform: translate(-50%,0);
    position: absolute;
    opacity: .35;
  }
}
```

## JavaScript
```js
/* No JavaScript — three layers scrub the same view-timeline across different --d distances: giant word 130px, photo 45px, headline -60px. Swap the picsum placeholder for your own image. */

/* No JavaScript — the inner pane owns perspective:1px; the background word at translateZ(-1px) scale(2) is projected at half scroll speed. Pure geometry, universal support. */
```
