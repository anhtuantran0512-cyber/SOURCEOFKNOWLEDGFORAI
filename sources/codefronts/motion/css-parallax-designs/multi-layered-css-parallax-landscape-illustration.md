---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/multi-layered-css-parallax-landscape-illustration/"
title: "Multi Layer Parallax Landscape Illustration"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "Five vector planes — deep sky, distant range, mid hills, treeline and foreground grass — each drifting at its own rate to build an illustrated landscape with…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi Layer Parallax Landscape Illustration
Source: https://codefronts.com/motion/css-parallax-designs/multi-layered-css-parallax-landscape-illustration/

Five vector planes — deep sky, distant range, mid hills, treeline and foreground grass — each drifting at its own rate to build an illustrated landscape with real depth. All artwork is inline SVG path data, so the scene scales to any viewport, weighs nothing, and recolours from six custom properties.
## HTML
```html
<div class="plx-14">
  <section class="plx-14__scene" aria-labelledby="plx-14-title">
    <div class="plx-14__sun" aria-hidden="true"></div>
    <svg class="plx-14__layer plx-14__sky" viewBox="0 0 1050 420" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 420V210l150-42 130 30 160-56 150 44 170-52 150 40 140-30v276Z" fill="var(--l1)"/>
    </svg>
    <svg class="plx-14__layer plx-14__range" viewBox="0 0 1100 340" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 340V178l128-88 92 66 118-96 122 104 130-72 148 92 126-64 136 78 100-46v188Z" fill="var(--l2)"/>
    </svg>
    <svg class="plx-14__layer plx-14__hills" viewBox="0 0 1000 260" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 260V158c104-44 176 18 262-12s148-58 240-22 152 70 244 36 166-48 254-14v114Z" fill="var(--l3)"/>
    </svg>
    <svg class="plx-14__layer plx-14__trees" viewBox="0 0 970 200" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 200v-64l26 10 18-40 22 34 24-56 22 50 28-30 24 42 32-52 22 56 28-36 24 32 30-46 24 50 34-38 22 44 28-54 26 48 30-32 22 38 32-46 24 52 28-36 24 32 32-46 22 48 30-32 24 38 34-46 22 50 28-34 24 30 32-44 22 46 30-30 24 36 32-42 20 44V200Z" fill="var(--l4)"/>
    </svg>
    <svg class="plx-14__layer plx-14__grass" viewBox="0 0 1200 220" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 220V96c120 26 200-26 320-8s176 40 300 16 200-38 320-8 180 16 260-4v128Z" fill="var(--l5)"/>
    </svg>
    <div class="plx-14__caption">
      <p class="plx-14__label">Plate 07 · Five planes</p>
      <h1 class="plx-14__h1" id="plx-14-title">Distant range,<br>then everything nearer</h1>
      <p class="plx-14__lede">Sky 8px. Range 16. Hills 28. Trees 40. Grass 60. The ratios do the work, not the drawing.</p>
    </div>
  </section>
  <main class="plx-14__notes">
    <section class="plx-14__note">
      <h2 class="plx-14__h2">Why vector</h2>
      <p class="plx-14__p">Five paths, under two kilobytes, no crop decisions and no art direction breakpoints. The scene recolours from six custom properties, so dawn, dusk and monochrome are three overrides rather than three exports.</p>
    </section>
    <section class="plx-14__note">
      <h2 class="plx-14__h2">Doubling, not stepping</h2>
      <p class="plx-14__p">Each plane travels roughly twice as far as the one behind it. Evenly spaced values look like sliding panels; doubled values read as recession, because that is closer to how distance actually behaves.</p>
    </section>
    <section class="plx-14__note">
      <h2 class="plx-14__h2">Recolour</h2>
      <p class="plx-14__p">Set the five fills toward a single hue with decreasing lightness for a monochrome print look, or run cool at the back and warm at the front to imply a low sun. Illustration by Jordan Lee.</p>
    </section>
  </main>
</div>
```
## CSS
```css
.plx-14 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: ui-sans-serif, system-ui, "Helvetica Neue", "Segoe UI", sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --paper: #f4f2e9;
  --ink: #2b3327;
  --muted: #6b7864;
  --accent: #5f7a4a;
  --l1: #d8e0cf;
  --l2: #b3c2a5;
  --l3: #8aa07c;
  --l4: #5d7551;
  --l5: #3b4c33;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-14 * {
  box-sizing: border-box;
}

.plx-14__scene {
  position: relative;
  min-height: 100svh;
  overflow: clip;
  display: flex;
  align-items: flex-start;
  background: linear-gradient(180deg, #fbfaf3 0%, #eef1e6 62%, #e4e9da 100%);
}

.plx-14__sun {
  position: absolute;
  inset-block-start: 14%;
  inset-inline-start: 18%;
  inline-size: clamp(90px, 16vw, 200px);
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle, #f7e7b8 0%, #f1dda4 52%, rgba(241,221,164,0) 74%);
  will-change: transform;
}

.plx-14__layer {
  position: absolute;
  inset-inline: -2%;
  inset-block-end: 0;
  /* SVG layers need an explicit inline-size — inset-inline alone leaves SVGs
       falling back to their viewBox aspect ratio, which shrinks them to ~55-84%
       root width. inline-size:104% covers the -2%/-2% inset explicitly. */
  inline-size: 104%;
  will-change: transform;
  pointer-events: none;
}

.plx-14__sky {
  block-size: 58vh;
}

.plx-14__range {
  block-size: 46vh;
}

.plx-14__hills {
  block-size: 34vh;
}

.plx-14__trees {
  block-size: 24vh;
}

.plx-14__grass {
  block-size: 20vh;
  inset-block-end: -2px;
}

.plx-14__caption {
  position: relative;
  z-index: 6;
  padding: clamp(28px, 6vw, 76px);
  max-inline-size: 42rem;
  min-inline-size: 0;
}

.plx-14__label {
  margin: 0 0 18px;
  font: 700 10px/1 var(--font-display);
  letter-spacing: 0.34em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-14__h1 {
  margin: 0 0 16px;
  font-family: var(--font-display);
  font-size: clamp(28px, 5.8vw, 54px);
  font-weight: 700;
  line-height: 1.06;
  letter-spacing: -0.025em;
  text-transform: uppercase;
}

.plx-14__lede {
  margin: 0;
  max-inline-size: 26rem;
  font-size: clamp(14px, 3.2vw, 16px);
  line-height: 1.66;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-14__notes {
  position: relative;
  z-index: 7;
  background: var(--paper);
  padding: clamp(40px, 8vw, 96px) clamp(22px, 6vw, 76px) 130px;
  display: grid;
  gap: clamp(30px, 5vw, 56px);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr));
}

.plx-14__note {
  min-inline-size: 0;
}

.plx-14__h2 {
  margin: 0 0 10px;
  font-family: var(--font-display);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-14__p {
  margin: 0;
  font-size: 15px;
  line-height: 1.72;
  color: #3f4a39;
  text-wrap: pretty;
}

@supports (animation-timeline: scroll()) {
  .plx-14__sun {
    animation: plx-14-sun linear both;
    animation-timeline: scroll(root);
  }

  .plx-14__sky {
    animation: plx-14-l1 linear both;
    animation-timeline: scroll(root);
  }

  .plx-14__range {
    animation: plx-14-l2 linear both;
    animation-timeline: scroll(root);
  }

  .plx-14__hills {
    animation: plx-14-l3 linear both;
    animation-timeline: scroll(root);
  }

  .plx-14__trees {
    animation: plx-14-l4 linear both;
    animation-timeline: scroll(root);
  }

  .plx-14__grass {
    animation: plx-14-l5 linear both;
    animation-timeline: scroll(root);
  }
}
/* Parallax offsets scaled 2.5-3× from original (-20/-55/-110/-190/-300px)
   to give visible depth over full-page scroll. Sun offset preserved as
   subtle drift (celestial object stays high in the frame). */

@keyframes plx-14-sun {
  to {
    transform: translateY(-8px) scale(0.96);
  }
}

@keyframes plx-14-l1 {
  to {
    transform: translateY(-8px);
  }
}

@keyframes plx-14-l2 {
  to {
    transform: translateY(-16px);
  }
}

@keyframes plx-14-l3 {
  to {
    transform: translateY(-28px);
  }
}

@keyframes plx-14-l4 {
  to {
    transform: translateY(-40px);
  }
}

@keyframes plx-14-l5 {
  to {
    transform: translateY(-60px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-14__layer,
    .plx-14__sun {
    animation: none !important;
    transform: none !important;
    will-change: auto;
  }
}

@media (max-width: 620px) {
  .plx-14__sky {
    block-size: 44vh;
  }

  .plx-14__range {
    block-size: 34vh;
  }

  .plx-14__hills {
    block-size: 26vh;
  }

  .plx-14__trees {
    block-size: 18vh;
  }

  .plx-14__grass {
    block-size: 15vh;
  }
}
```
