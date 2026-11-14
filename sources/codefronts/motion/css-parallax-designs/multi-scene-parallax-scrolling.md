---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/multi-scene-parallax-scrolling/"
title: "Multi Scene Parallax Scrolling Journey"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "Three pinned scenes that take you through one day of travel — dawn, midday, dusk — each with its own palette, photograph and copy, and each with a photo…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi Scene Parallax Scrolling Journey
Source: https://codefronts.com/motion/css-parallax-designs/multi-scene-parallax-scrolling/

Three pinned scenes that take you through one day of travel — dawn, midday, dusk — each with its own palette, photograph and copy, and each with a photo plane that pushes in while its scene holds the frame. Built for trip pages and brand stories where the sequence itself is the argument.
## HTML
```html
<div class="plx-16">
  <header class="plx-16__intro">
    <p class="plx-16__brand">Northbound · Trip 12</p>
    <h1 class="plx-16__h1">One day, three light conditions, no rush</h1>
    <p class="plx-16__lede">Dawn on the plateau, midday on the water, dusk at the pass. Scroll through the day.</p>
  </header>
  <section class="plx-16__scene plx-16__scene--dawn" aria-labelledby="plx-16-s1">
    <img class="plx-16__plate" src="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?w=1600&auto=format&fit=crop" alt="Low sun over open farmland at first light" loading="eager" decoding="async">
    <div class="plx-16__copy">
      <p class="plx-16__time">05:40 · Dawn</p>
      <h2 class="plx-16__h2" id="plx-16-s1">Leave before the valley wakes up</h2>
      <p class="plx-16__p">Forty minutes of gravel to the plateau edge. Bring gloves — it is eleven degrees colder up here than at the guesthouse.</p>
    </div>
  </section>
  <section class="plx-16__scene plx-16__scene--noon" aria-labelledby="plx-16-s2">
    <img class="plx-16__plate" src="https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=1600&auto=format&fit=crop" alt="Turquoise mountain lake under midday sun" loading="lazy" decoding="async">
    <div class="plx-16__copy">
      <p class="plx-16__time">12:15 · Midday</p>
      <h2 class="plx-16__h2" id="plx-16-s2">The water is colder than it looks</h2>
      <p class="plx-16__p">Four degrees, glacier-fed, and worth it for about ninety seconds. Boats can be hired by the hour from the hut on the north shore.</p>
    </div>
  </section>
  <section class="plx-16__scene plx-16__scene--dusk" aria-labelledby="plx-16-s3">
    <img class="plx-16__plate" src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=1600&auto=format&fit=crop" alt="Mountain lake reflecting a pink and orange sunset" loading="lazy" decoding="async">
    <div class="plx-16__copy">
      <p class="plx-16__time">20:05 · Dusk</p>
      <h2 class="plx-16__h2" id="plx-16-s3">Stay for the second colour</h2>
      <p class="plx-16__p">Everyone leaves after the sun goes. Fifteen minutes later the whole basin turns pink for about four minutes, and then it is over.</p>
    </div>
  </section>
  <footer class="plx-16__foot">
    <h2 class="plx-16__h3">Practical</h2>
    <dl class="plx-16__facts">
      <div class="plx-16__fact"><dt>Getting there</dt><dd>Two hours from the airport, one bus</dd></div>
      <div class="plx-16__fact"><dt>Season</dt><dd>June to late September</dd></div>
      <div class="plx-16__fact"><dt>Guide</dt><dd>Sam Rivera, six people maximum</dd></div>
    </dl>
  </footer>
</div>
```
## CSS
```css
.plx-16 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "SF Pro Rounded", ui-rounded, "Nunito", "Trebuchet MS", system-ui, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --paper: #fff9f2;
  --base-ink: #2c2119;
  background: var(--paper);
  color: var(--base-ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-16 * {
  box-sizing: border-box;
}

.plx-16__intro {
  padding: clamp(40px, 8vw, 104px) clamp(20px, 5vw, 68px) clamp(30px, 6vw, 64px);
  max-inline-size: 50rem;
}

.plx-16__brand {
  margin: 0 0 16px;
  font: 700 10px/1 var(--font-body);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: #c4622f;
}

.plx-16__h1 {
  margin: 0 0 14px;
  font-family: var(--font-display);
  font-size: clamp(30px, 6.4vw, 58px);
  font-weight: 700;
  line-height: 1.04;
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.plx-16__lede {
  margin: 0;
  max-inline-size: 30rem;
  font-size: clamp(15px, 3.2vw, 18px);
  line-height: 1.62;
  color: #7c6555;
}

.plx-16__scene {
  position: sticky;
  top: 0;
  block-size: 100svh;
  overflow: clip;
  display: flex;
  align-items: flex-end;
  isolation: isolate;
}

.plx-16__scene--dawn {
  --accent: #ff9e4f;
  --scrim: rgba(48,22,10,0.72);
  z-index: 1;
}

.plx-16__scene--noon {
  --accent: #35c8d8;
  --scrim: rgba(6,34,44,0.68);
  z-index: 2;
}

.plx-16__scene--dusk {
  --accent: #ff7ab0;
  --scrim: rgba(34,12,38,0.74);
  z-index: 3;
}

.plx-16__plate {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 116%;
  object-fit: cover;
  will-change: transform;
  z-index: -1;
}

.plx-16__copy {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  max-inline-size: 44rem;
  padding: clamp(70px, 18vh, 200px) clamp(22px, 5vw, 64px) clamp(28px, 6vw, 62px);
  background: linear-gradient(to top, var(--scrim) 0%, var(--scrim) 34%, rgba(0,0,0,0) 100%);
  color: #fffaf4;
}

.plx-16__time {
  margin: 0 0 14px;
  display: inline-flex;
  align-items: center;
  padding: 7px 12px;
  border-radius: 999px;
  background: var(--accent);
  color: #1c1108;
  font: 700 11px/1 var(--font-body);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  box-shadow: 0 0 34px -6px var(--accent);
}

.plx-16__h2 {
  margin: 0 0 12px;
  max-inline-size: 26rem;
  font-family: var(--font-display);
  font-size: clamp(26px, 5.8vw, 50px);
  font-weight: 700;
  line-height: 1.04;
  letter-spacing: -0.03em;
}

.plx-16__p {
  margin: 0;
  max-inline-size: 30rem;
  font-size: clamp(15px, 3.2vw, 17px);
  line-height: 1.66;
  color: rgba(255,250,244,0.86);
  text-wrap: pretty;
}

.plx-16__foot {
  position: relative;
  z-index: 4;
  background: var(--paper);
  padding: clamp(44px, 8vw, 100px) clamp(20px, 5vw, 68px) 130px;
}

.plx-16__h3 {
  margin: 0 0 22px;
  font-family: var(--font-display);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: #c4622f;
}

.plx-16__facts {
  margin: 0;
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr));
}

.plx-16__fact {
  min-inline-size: 0;
  padding-block-end: 14px;
  border-bottom: 1px solid #ece0d2;
}

.plx-16__fact dt {
  font: 700 10px/1 var(--font-body);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #9c8574;
}

.plx-16__fact dd {
  margin: 8px 0 0;
  font-family: var(--font-display);
  font-size: 17px;
  font-weight: 600;
}

@supports (animation-timeline: view()) {
  .plx-16__plate {
    animation: plx-16-push linear both;
    animation-timeline: view();
    animation-range: contain 0% contain 100%;
  }
}

@keyframes plx-16-push {
  from {
    transform: translateY(0) scale(1);
  }

  to {
    transform: translateY(-9%) scale(1.12);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-16__plate {
    animation: none !important;
    transform: none !important;
    block-size: 100%;
    will-change: auto;
  }
}
```
