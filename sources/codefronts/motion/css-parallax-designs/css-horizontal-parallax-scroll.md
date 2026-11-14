---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/css-horizontal-parallax-scroll/"
title: "Horizontal Parallax Scroll Panels"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "Vertical scrolling drives a horizontal track: four panels slide across a pinned viewport while the art inside each panel counter-moves, so the sequence has…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Parallax Scroll Panels
Source: https://codefronts.com/motion/css-parallax-designs/css-horizontal-parallax-scroll/

Vertical scrolling drives a horizontal track: four panels slide across a pinned viewport while the art inside each panel counter-moves, so the sequence has depth as well as direction. Useful for process explainers and product stories where the steps want to read left to right without hijacking the wheel.
## HTML
```html
<div class="plx-18">
  <header class="plx-18__head">
    <p class="plx-18__brand">Halide Film Lab</p>
    <h1 class="plx-18__h1">Four steps from roll to print</h1>
    <p class="plx-18__lede">Scroll down — the track moves sideways.</p>
  </header>
  <div class="plx-18__runway">
    <div class="plx-18__viewport">
      <div class="plx-18__track">
        <section class="plx-18__panel">
          <div class="plx-18__art" aria-hidden="true"><span class="plx-18__disc"></span><span class="plx-18__strip"></span></div>
          <div class="plx-18__copy">
            <p class="plx-18__num">01</p>
            <h2 class="plx-18__h2">Intake</h2>
            <p class="plx-18__p">Rolls are logged by hand, one card per roll, before anything is opened. The card follows the film through every bath and ends up in the envelope with your negatives.</p>
          </div>
        </section>
        <section class="plx-18__panel">
          <div class="plx-18__art" aria-hidden="true"><span class="plx-18__disc plx-18__disc--b"></span><span class="plx-18__strip"></span></div>
          <div class="plx-18__copy">
            <p class="plx-18__num">02</p>
            <h2 class="plx-18__h2">Develop</h2>
            <p class="plx-18__p">C-41 at 38 degrees, replenished daily and tested against a control strip every morning. Push and pull to plus or minus two stops on request.</p>
          </div>
        </section>
        <section class="plx-18__panel">
          <div class="plx-18__art" aria-hidden="true"><span class="plx-18__disc plx-18__disc--c"></span><span class="plx-18__strip"></span></div>
          <div class="plx-18__copy">
            <p class="plx-18__num">03</p>
            <h2 class="plx-18__h2">Scan</h2>
            <p class="plx-18__p">Flat scans at 3600 dpi with no automatic correction, plus a corrected set if you want one. You get both, always, at no extra cost.</p>
          </div>
        </section>
        <section class="plx-18__panel">
          <div class="plx-18__art" aria-hidden="true"><span class="plx-18__disc plx-18__disc--d"></span><span class="plx-18__strip"></span></div>
          <div class="plx-18__copy">
            <p class="plx-18__num">04</p>
            <h2 class="plx-18__h2">Print</h2>
            <p class="plx-18__p">Optical prints up to 30 by 40 centimetres, wet-mounted. Turnaround is four working days, or same-week for standing accounts.</p>
          </div>
        </section>
      </div>
    </div>
  </div>
  <footer class="plx-18__foot">
    <p class="plx-18__p">Drop-off Tuesday to Saturday. Mail-in envelopes are free — ask for one with your next order.</p>
  </footer>
</div>
```
## CSS
```css
.plx-18 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Avenir Next Condensed", "Oswald", "Arial Narrow", system-ui, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --char: #211f1c;
  --char-2: #2b2824;
  --ink: #f6f1e6;
  --muted: #a89e8c;
  --accent: #ffb703;
  background: var(--char);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-18 * {
  box-sizing: border-box;
}

.plx-18__head {
  padding: clamp(32px, 6vw, 76px) clamp(18px, 4vw, 54px) clamp(22px, 4vw, 44px);
  max-inline-size: 46rem;
}

.plx-18__brand {
  margin: 0 0 14px;
  font: 700 10px/1 var(--font-body);
  letter-spacing: 0.32em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-18__h1 {
  margin: 0 0 10px;
  font-family: var(--font-display);
  font-size: clamp(28px, 6.2vw, 56px);
  font-weight: 600;
  line-height: 1.02;
  letter-spacing: 0.01em;
  text-transform: uppercase;
}

.plx-18__lede {
  margin: 0;
  font-size: 14px;
  line-height: 1.55;
  color: var(--muted);
}

.plx-18__runway {
  block-size: 360svh;
}

.plx-18__viewport {
  position: sticky;
  top: 0;
  block-size: 100svh;
  overflow: clip;
}

.plx-18__track {
  display: flex;
  block-size: 100%;
  inline-size: 400%;
  will-change: transform;
}

.plx-18__panel {
  inline-size: 25%;
  block-size: 100%;
  min-inline-size: 0;
  padding: clamp(16px, 3vw, 40px);
  display: grid;
  align-content: center;
  gap: clamp(14px, 2.4vw, 26px);
  border-inline-end: 1px solid #3a352e;
  background: var(--char-2);
  overflow: clip;
}

.plx-18__panel:nth-child(even) {
  background: #262320;
}

.plx-18__art {
  position: relative;
  block-size: clamp(120px, 26vh, 240px);
  will-change: transform;
}

.plx-18__disc {
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 4%;
  inline-size: clamp(90px, 18vh, 170px);
  aspect-ratio: 1;
  border-radius: 50%;
  border: clamp(8px, 2vh, 16px) solid var(--accent);
  box-shadow: 8px 8px 0 0 #12100e;
}

.plx-18__disc--b {
  border-color: #f27e3f;
}

.plx-18__disc--c {
  border-color: #6fd3c7;
}

.plx-18__disc--d {
  border-color: #f6f1e6;
}

.plx-18__strip {
  position: absolute;
  inset-block-end: 6%;
  inset-inline: 12% 4%;
  block-size: clamp(28px, 6vh, 52px);
  background: repeating-linear-gradient(90deg, #12100e 0 10px, transparent 10px 26px) top / 100% 6px repeat-x, repeating-linear-gradient(90deg, #12100e 0 10px, transparent 10px 26px) bottom / 100% 6px repeat-x, #4a443b;
  box-shadow: 8px 8px 0 0 #12100e;
}

.plx-18__copy {
  min-inline-size: 0;
  max-inline-size: 34rem;
}

.plx-18__num {
  margin: 0 0 8px;
  font-family: var(--font-display);
  font-size: clamp(30px, 6vw, 58px);
  font-weight: 600;
  line-height: 1;
  color: var(--accent);
}

.plx-18__h2 {
  margin: 0 0 10px;
  font-family: var(--font-display);
  font-size: clamp(22px, 4.6vw, 38px);
  font-weight: 600;
  letter-spacing: 0.01em;
  text-transform: uppercase;
}

.plx-18__p {
  margin: 0;
  font-size: clamp(14px, 3vw, 16px);
  line-height: 1.66;
  color: #cdc4b3;
  text-wrap: pretty;
}

.plx-18__foot {
  padding: clamp(34px, 6vw, 80px) clamp(18px, 4vw, 54px) 120px;
  border-top: 1px solid #3a352e;
}

.plx-18__foot .plx-18__p {
  max-inline-size: 34rem;
  color: var(--muted);
}

@supports (animation-timeline: scroll()) {
  .plx-18__track {
    animation: plx-18-slide linear both;
    animation-timeline: scroll(root);
    animation-range: 6% 92%;
  }

  .plx-18__art {
    animation: plx-18-counter linear both;
    animation-timeline: scroll(root);
    animation-range: 6% 92%;
  }
}

@keyframes plx-18-slide {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-75%);
  }
}

@keyframes plx-18-counter {
  from {
    transform: translateX(40px);
  }

  to {
    transform: translateX(-40px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-18__runway {
    block-size: auto;
  }

  .plx-18__viewport {
    position: static;
    block-size: auto;
  }

  .plx-18__track {
    animation: none !important;
    transform: none !important;
    display: grid;
    inline-size: 100%;
    will-change: auto;
  }

  .plx-18__panel {
    inline-size: 100%;
    block-size: auto;
    min-block-size: 70svh;
    border-inline-end: 0;
    border-bottom: 1px solid #3a352e;
  }

  .plx-18__art {
    animation: none !important;
    transform: none !important;
  }
}
```
