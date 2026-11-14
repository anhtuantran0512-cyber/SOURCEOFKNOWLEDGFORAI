---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/backdrop-filter-blur-cross-fade-parallax/"
title: "Backdrop Filter Blur Cross Fade Parallax"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A focus-pull between two marketing sections: as the incoming panel rises, a glass veil over the outgoing scene ramps its backdrop-filter blur from zero to…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Backdrop Filter Blur Cross Fade Parallax
Source: https://codefronts.com/motion/css-parallax-designs/backdrop-filter-blur-cross-fade-parallax/

A focus-pull between two marketing sections: as the incoming panel rises, a glass veil over the outgoing scene ramps its backdrop-filter blur from zero to full while the scene behind it drifts back. The outgoing section stays pinned and legible until the moment it defocuses, which is what makes the handoff feel filmic rather than abrupt.
## HTML
```html
<div class="plx-05">
  <section class="plx-05__pin" aria-labelledby="plx-05-a">
    <div class="plx-05__scene">
      <div class="plx-05__plane" aria-hidden="true">
        <span class="plx-05__orb plx-05__orb--1"></span>
        <span class="plx-05__orb plx-05__orb--2"></span>
        <span class="plx-05__grid"></span>
      </div>
      <div class="plx-05__sceneCopy">
        <p class="plx-05__eyebrow">Northwind Platform</p>
        <h2 class="plx-05__h1" id="plx-05-a">Every event, in order, forever</h2>
        <p class="plx-05__lede">An append-only log your services can replay from any point in the last ninety days.</p>
      </div>
      <div class="plx-05__veil" aria-hidden="true"></div>
    </div>
  </section>
  <section class="plx-05__incoming" aria-labelledby="plx-05-b">
    <div class="plx-05__card">
      <p class="plx-05__eyebrow plx-05__eyebrow--alt">Now in the same pipeline</p>
      <h2 class="plx-05__h2" id="plx-05-b">Replay, not reprocessing</h2>
      <p class="plx-05__p">Point a consumer at any offset and it rebuilds its own state. No backfill scripts, no separate batch path, no second copy of the data to keep honest.</p>
      <ul class="plx-05__list">
        <li>Ordered delivery per partition key</li>
        <li>Ninety days of retention, configurable per topic</li>
        <li>Exactly-once sinks for Postgres and ClickHouse</li>
      </ul>
      <a class="plx-05__cta" href="#plx-05-b">Read the architecture note</a>
    </div>
  </section>
  <section class="plx-05__after">
    <p class="plx-05__p">Scroll back up and the focus pull runs in reverse — the veil's blur is bound to scroll position, not to a one-shot trigger.</p>
  </section>
</div>
```
## CSS
```css
.plx-05 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Geist", "Inter", system-ui, -apple-system, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --bg: #070d1c;
  --surface: #0d1730;
  --ink: #e9eefb;
  --muted: #8fa1c7;
  --accent: #4cc4ff;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-05 * {
  box-sizing: border-box;
}

.plx-05__pin {
  position: sticky;
  top: 0;
  block-size: 100svh;
  overflow: clip;
  z-index: 0;
}

.plx-05__scene {
  position: relative;
  block-size: 100%;
  display: flex;
  align-items: center;
}

.plx-05__plane {
  position: absolute;
  inset: -10% -5%;
  will-change: transform;
}

.plx-05__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(30px);
}

.plx-05__orb--1 {
  inline-size: 44vmax;
  aspect-ratio: 1;
  top: -12%;
  right: -8%;
  background: radial-gradient(circle, rgba(76,196,255,0.45), rgba(76,196,255,0) 68%);
}

.plx-05__orb--2 {
  inline-size: 34vmax;
  aspect-ratio: 1;
  bottom: -14%;
  left: -6%;
  background: radial-gradient(circle, rgba(120,86,255,0.4), rgba(120,86,255,0) 70%);
}

.plx-05__grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(160,190,255,0.09) 1px, transparent 1px), linear-gradient(90deg, rgba(160,190,255,0.09) 1px, transparent 1px);
  background-size: 64px 64px;
  mask-image: radial-gradient(70% 60% at 50% 45%, #000 30%, transparent 100%);
}

.plx-05__sceneCopy {
  position: relative;
  z-index: 2;
  padding: clamp(24px, 6vw, 88px);
  max-inline-size: 44rem;
  min-inline-size: 0;
}

.plx-05__eyebrow {
  margin: 0 0 16px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-05__eyebrow--alt {
  color: #6f86b6;
}

.plx-05__h1 {
  margin: 0 0 18px;
  font-family: var(--font-display);
  font-size: clamp(32px, 7vw, 72px);
  font-weight: 620;
  line-height: 1.02;
  letter-spacing: -0.03em;
}

.plx-05__lede {
  margin: 0;
  max-inline-size: 30rem;
  font-size: clamp(15px, 3.4vw, 19px);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-05__veil {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: rgba(7,13,28,0.34);
  pointer-events: none;
}

@supports (backdrop-filter: blur(2px)) {
  .plx-05__veil {
    background: rgba(7,13,28,0.12);
    backdrop-filter: blur(0px);
  }
}

.plx-05__incoming {
  position: relative;
  z-index: 4;
  min-block-size: 100svh;
  display: flex;
  align-items: center;
  padding: clamp(28px, 6vw, 88px);
  background: linear-gradient(180deg, rgba(9,16,34,0.2) 0%, #091022 26%, #091022 100%);
  will-change: transform;
}

.plx-05__card {
  inline-size: 100%;
  max-inline-size: 40rem;
  min-inline-size: 0;
  padding: clamp(22px, 4vw, 40px);
  border-radius: 22px;
  border: 1px solid rgba(158,196,255,0.18);
  background: linear-gradient(180deg, rgba(30,48,90,0.62), rgba(13,23,48,0.72));
  box-shadow: inset 0 1px 0 rgba(226,240,255,0.22), 0 30px 70px -40px rgba(0,0,0,0.9);
}

@supports (backdrop-filter: blur(2px)) {
  .plx-05__card {
    backdrop-filter: blur(14px);
  }
}

.plx-05__h2 {
  margin: 0 0 14px;
  font-family: var(--font-display);
  font-size: clamp(24px, 5vw, 40px);
  font-weight: 620;
  line-height: 1.08;
  letter-spacing: -0.02em;
}

.plx-05__p {
  margin: 0 0 20px;
  font-size: clamp(15px, 3.2vw, 17px);
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-05__list {
  margin: 0 0 26px;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 10px;
  font-size: 15px;
  color: #c6d5f2;
}

.plx-05__list li {
  padding-inline-start: 18px;
  position: relative;
  min-inline-size: 0;
}

.plx-05__list li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  top: 0.55em;
  inline-size: 7px;
  block-size: 7px;
  border-radius: 50%;
  background: var(--accent);
}

.plx-05__cta {
  display: inline-flex;
  align-items: center;
  min-height: 46px;
  padding: 0 22px;
  border-radius: 12px;
  background: var(--accent);
  color: #04121f;
  font: 600 14px/1 var(--font-body);
  text-decoration: none;
}

.plx-05__cta:hover {
  background: #86d8ff;
}

.plx-05__cta:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.plx-05__after {
  position: relative;
  z-index: 4;
  padding: clamp(40px, 8vw, 96px) clamp(28px, 6vw, 88px) 130px;
  background: #091022;
}

.plx-05__after .plx-05__p {
  max-inline-size: 32rem;
  margin: 0;
}

@supports (animation-timeline: scroll()) {
  .plx-05__plane {
    animation: plx-05-plane linear both;
    animation-timeline: scroll(root);
  }

  .plx-05__incoming {
    animation: plx-05-rise linear both;
    animation-timeline: scroll(root);
    animation-range: 18% 60%;
  }

  @supports (backdrop-filter: blur(2px)) {
    .plx-05__veil {
      animation: plx-05-pull linear both;
      animation-timeline: scroll(root);
      animation-range: 22% 62%;
    }
  }
}

@keyframes plx-05-plane {
  to {
    transform: translateY(-90px) scale(1.06);
  }
}

@keyframes plx-05-rise {
  from {
    transform: translateY(12vh);
  }

  to {
    transform: translateY(0);
  }
}

@keyframes plx-05-pull {
  from {
    backdrop-filter: blur(0px);
    background: rgba(7,13,28,0.05);
  }

  to {
    backdrop-filter: blur(18px);
    background: rgba(7,13,28,0.55);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-05__plane,
    .plx-05__incoming,
    .plx-05__veil {
    animation: none !important;
    transform: none !important;
    will-change: auto;
  }

  .plx-05__veil {
    backdrop-filter: none !important;
    background: rgba(7,13,28,0.1);
  }
}
```
