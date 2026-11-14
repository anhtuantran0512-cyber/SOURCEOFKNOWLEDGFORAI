---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/scroll-driven-svg-path-draw-parallax/"
title: "Scroll Driven SVG Path Draw Parallax"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A line-art route that draws itself into the hills as you scroll: the road is one SVG path whose stroke-dashoffset is bound to scroll(root), while the ridges,…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Driven SVG Path Draw Parallax
Source: https://codefronts.com/motion/css-parallax-designs/scroll-driven-svg-path-draw-parallax/

A line-art route that draws itself into the hills as you scroll: the road is one SVG path whose stroke-dashoffset is bound to scroll(root), while the ridges, treeline and milestone markers around it parallax at three separate rates. Useful for route maps, process walkthroughs and any explainer where the line itself carries the narrative.
## HTML
```html
<div class="plx-03">
  <section class="plx-03__scene" aria-labelledby="plx-03-title">
    <svg class="plx-03__art" viewBox="0 0 800 600" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
      <g class="plx-03__far">
        <path d="M0 300 90 236l72 40 96-64 84 52 108-74 96 62 84-44 160 82v46H0Z" fill="none" stroke="#a9b6a2" stroke-width="1.5" vector-effect="non-scaling-stroke"/>
        <circle cx="614" cy="150" r="46" fill="none" stroke="#a9b6a2" stroke-width="1.5" vector-effect="non-scaling-stroke"/>
      </g>
      <g class="plx-03__mid">
        <path d="M0 400l120-56 96 44 120-62 108 56 132-70 124 66 100-40v62H0Z" fill="none" stroke="#7d8f77" stroke-width="1.5" vector-effect="non-scaling-stroke"/>
      </g>
      <path class="plx-03__road" d="M398 268c0 34-52 46-52 82s86 44 86 84-124 48-124 88 148 46 148 78" pathLength="1" fill="none" stroke="#31432f" stroke-width="2.25" stroke-linecap="butt" vector-effect="non-scaling-stroke"/>
      <g class="plx-03__near">
        <path d="M0 560l60-22 54 18 66-26 58 22 70-30 62 26 66-22 60 24 70-28 62 26 60-20 62 24v40H0Z" fill="none" stroke="#31432f" stroke-width="1.75" vector-effect="non-scaling-stroke"/>
        <path d="M120 540v-46m-14 24 14-16 14 16M660 548v-52m-16 26 16-18 16 18" fill="none" stroke="#31432f" stroke-width="1.75" vector-effect="non-scaling-stroke"/>
      </g>
    </svg>
    <div class="plx-03__intro">
      <p class="plx-03__eyebrow">Ridgeline Supply Co. · Route notes</p>
      <h1 class="plx-03__h1" id="plx-03-title">The old service road, drawn as you go</h1>
      <p class="plx-03__lede">Eleven kilometres from the gate to the upper hut. The line finishes drawing at the same moment the ridges settle.</p>
    </div>
  </section>
  <main class="plx-03__notes">
    <section class="plx-03__note">
      <p class="plx-03__km">KM 0 – 3.4</p>
      <h2 class="plx-03__h2">Gate to the first switchback</h2>
      <p class="plx-03__p">Gravel, gently graded, wide enough for a supply truck until the second bridge. The route was cut in 1948 and has been resurfaced twice; the camber still favours the uphill side.</p>
    </section>
    <section class="plx-03__note">
      <p class="plx-03__km">KM 3.4 – 7.1</p>
      <h2 class="plx-03__h2">The long traverse</h2>
      <p class="plx-03__p">Where the drawn line doubles back on itself. On the ground it feels like one continuous curve; on the map it is four, and the elevation gain hides inside them.</p>
    </section>
    <section class="plx-03__note">
      <p class="plx-03__km">KM 7.1 – 11.0</p>
      <h2 class="plx-03__h2">Upper hut</h2>
      <p class="plx-03__p">Above the treeline the surface turns to compacted shale. Radio contact from the saddle only. Water at the hut is snowmelt from June through September.</p>
    </section>
  </main>
</div>
```
## CSS
```css
.plx-03 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Rockwell", "Roboto Slab", "Bookman Old Style", Georgia, serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --cream: #f3f1e6;
  --ink: #26311f;
  --muted: #61705a;
  --accent: #31432f;
  background: var(--cream);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-03 * {
  box-sizing: border-box;
}

.plx-03__scene {
  position: relative;
  min-height: 100svh;
  display: flex;
  align-items: flex-end;
  overflow: clip;
}

.plx-03__art {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
}

.plx-03__far,
.plx-03__mid,
.plx-03__near {
  will-change: transform;
}

.plx-03__intro {
  position: relative;
  z-index: 2;
  padding: clamp(26px, 5vw, 64px);
  padding-block-start: clamp(140px, 30vh, 340px);
  inline-size: 100%;
  min-inline-size: 0;
  background: linear-gradient(to top, var(--cream) 0%, rgba(243,241,230,0.9) 58%, rgba(243,241,230,0) 100%);
}

.plx-03__eyebrow {
  margin: 0 0 16px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-03__h1 {
  margin: 0 0 16px;
  max-inline-size: 26rem;
  font-family: var(--font-display);
  font-size: clamp(30px, 6.6vw, 60px);
  font-weight: 700;
  line-height: 1.04;
  letter-spacing: -0.015em;
}

.plx-03__lede {
  margin: 0;
  max-inline-size: 30rem;
  font-size: clamp(15px, 3.4vw, 17px);
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-03__notes {
  position: relative;
  z-index: 3;
  background: var(--cream);
  padding: clamp(40px, 8vw, 96px) clamp(26px, 5vw, 64px) 130px;
  display: grid;
  gap: clamp(40px, 7vw, 80px);
  border-top: 1px solid #d8d5c3;
}

.plx-03__note {
  max-inline-size: 38rem;
  min-inline-size: 0;
  padding-block-start: 22px;
  border-top: 1px solid #d8d5c3;
}

.plx-03__km {
  margin: 0 0 12px;
  font: 700 11px/1 var(--font-display);
  letter-spacing: 0.18em;
  color: var(--accent);
}

.plx-03__h2 {
  margin: 0 0 12px;
  font-family: var(--font-display);
  font-size: clamp(22px, 4.6vw, 34px);
  font-weight: 700;
  line-height: 1.12;
}

.plx-03__p {
  margin: 0;
  font-size: clamp(15px, 3.4vw, 17px);
  line-height: 1.72;
  color: #47533f;
  text-wrap: pretty;
}

@supports (animation-timeline: scroll()) {
  .plx-03__road {
    stroke-dasharray: 1;
    animation: plx-03-draw linear both;
    animation-timeline: scroll(root);
    animation-range: 0 78%;
  }

  .plx-03__far {
    animation: plx-03-far linear both;
    animation-timeline: scroll(root);
  }

  .plx-03__mid {
    animation: plx-03-mid linear both;
    animation-timeline: scroll(root);
  }

  .plx-03__near {
    animation: plx-03-near linear both;
    animation-timeline: scroll(root);
  }
}

@keyframes plx-03-draw {
  from {
    stroke-dashoffset: 1;
  }

  to {
    stroke-dashoffset: 0;
  }
}

@keyframes plx-03-far {
  to {
    transform: translateY(-26px);
  }
}

@keyframes plx-03-mid {
  to {
    transform: translateY(-72px);
  }
}

@keyframes plx-03-near {
  to {
    transform: translateY(-180px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-03__road {
    animation: none !important;
    stroke-dasharray: none !important;
    stroke-dashoffset: 0 !important;
  }

  .plx-03__far,
    .plx-03__mid,
    .plx-03__near {
    animation: none !important;
    transform: none !important;
    will-change: auto;
  }
}
```
