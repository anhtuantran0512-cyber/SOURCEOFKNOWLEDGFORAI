---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/parallax-landing-page-hero-with-depth-layers/"
title: "Parallax Landing Page Hero with Depth Layers"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A five-plane marketing hero — sky, clouds, ridge, hills, grass — with the product card floating in front of them all."
has_js: "true"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Landing Page Hero with Depth Layers
Source: https://codefronts.com/motion/css-parallax-designs/parallax-landing-page-hero-with-depth-layers/

A five-plane marketing hero — sky, clouds, ridge, hills, grass — with the product card floating in front of them all. Scroll-timeline drives it wherever it exists; a fourteen-line requestAnimationFrame loop takes over only when CSS.supports says the timeline is missing, so both paths ship from the same set of layer declarations.
## HTML
```html
<div class="plx-12" id="plx-12-root">
  <header class="plx-12__hero">
    <div class="plx-12__layer plx-12__sky" style="--k: 0.1" aria-hidden="true"></div>
    <svg class="plx-12__layer plx-12__clouds" style="--k: 0.3" viewBox="0 0 290 260" preserveAspectRatio="none" aria-hidden="true">
      <path d="M90 150c0-26 22-42 46-38 8-24 40-34 60-18 16-20 52-16 60 10 26-2 40 18 34 40Z" fill="#ffffff" opacity="0.9"/>
      <path d="M700 108c0-22 18-36 40-32 6-20 34-28 50-14 14-16 44-14 50 10 22-2 34 14 28 34Z" fill="#ffffff" opacity="0.72"/>
      <path d="M980 186c0-18 16-30 34-26 6-16 28-24 42-12 12-14 38-12 42 8 18-2 28 12 24 28Z" fill="#ffffff" opacity="0.55"/>
    </svg>
    <svg class="plx-12__layer plx-12__ridge" style="--k: 0.5" viewBox="0 0 1000 300" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 300V168l124-72 96 58 130-86 118 92 126-66 140 82 128-58 138 74v88Z" fill="#1f6f6b"/>
    </svg>
    <svg class="plx-12__layer plx-12__hills" style="--k: 0.75" viewBox="0 0 1000 240" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 240V148c96-38 168 14 250-16s150-62 244-24 148 74 244 40 168-52 262-16v108Z" fill="#12514f"/>
    </svg>
    <svg class="plx-12__layer plx-12__grass" style="--k: 1.1" viewBox="0 0 1200 160" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0 160V96c110 22 190-30 300-14s170 44 292 18 190-42 306-14 190 20 302-2v76Z" fill="#0a3634"/>
    </svg>
    <div class="plx-12__content">
      <p class="plx-12__badge">Now in open beta</p>
      <h1 class="plx-12__h1">Plan the trip once. Bring everyone with you.</h1>
      <p class="plx-12__lede">Shared itineraries, offline maps and a bag list that argues with you when you overpack. Free for groups up to six.</p>
      <div class="plx-12__actions">
        <a class="plx-12__cta" href="#plx-12-more">Start a trip</a>
        <a class="plx-12__link" href="#plx-12-more">See how it works</a>
      </div>
      <div class="plx-12__card">
        <div class="plx-12__cardhead"><span class="plx-12__dot"></span><p class="plx-12__cardtitle">Aurel Valley · 11 days</p></div>
        <ul class="plx-12__rows">
          <li><span>Day 1</span><span>Gate hut, 6 km</span></li>
          <li><span>Day 4</span><span>Gorge crossing</span></li>
          <li><span>Day 9</span><span>Flatwater paddle</span></li>
        </ul>
        <p class="plx-12__cardfoot">4 of 6 travellers packed</p>
      </div>
    </div>
  </header>
  <main class="plx-12__body" id="plx-12-more">
    <section class="plx-12__section">
      <h2 class="plx-12__h2">Offline first, genuinely</h2>
      <p class="plx-12__p">Maps, permits and the whole itinerary are on the device before you leave the trailhead. Sync resolves conflicts by timestamp, not by whoever reconnects first.</p>
    </section>
    <section class="plx-12__section">
      <h2 class="plx-12__h2">One list, six packs</h2>
      <p class="plx-12__p">Shared gear is assigned, not duplicated. If two people pack a stove the list says so before you are carrying both up a hill.</p>
    </section>
    <section class="plx-12__section">
      <h2 class="plx-12__h2">Built by people who forgot the tent poles</h2>
      <p class="plx-12__p">Once. In 2021. The feature exists because of it. Team notes by Jordan Lee and Sam Rivera.</p>
    </section>
  </main>
</div>
```
## CSS
```css
.plx-12 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Optima", "Candara", "Gill Sans", "Trebuchet MS", system-ui, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --cream: #fbf6ec;
  --ink: #123330;
  --muted: #5c7a76;
  --accent: #0f8f86;
  --rule: #e4dccb;
  --sy: 0;
  background: var(--cream);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-12 * {
  box-sizing: border-box;
}

.plx-12__hero {
  position: relative;
  min-height: 104svh;
  overflow: clip;
  display: flex;
  align-items: center;
  padding: clamp(80px, 14vh, 150px) clamp(20px, 5vw, 72px) clamp(120px, 26vh, 260px);
  background: linear-gradient(178deg, #cdeef2 0%, #e6f4ea 52%, #fbf6ec 100%);
}

.plx-12__layer {
  position: absolute;
  left: -2%;
  right: -2%;
  /* SVG layers need an explicit inline-size — left/right alone leaves SVGs
       falling back to their viewBox aspect ratio, which shrinks them to ~51-70%
       root width. inline-size:104% covers the -2%/-2% inset explicitly. */
  inline-size: 104%;
  will-change: transform;
  pointer-events: none;
}

.plx-12__sky {
  inset: -4% -2%;
  background: radial-gradient(70% 50% at 22% 12%, rgba(255,255,255,0.9), rgba(255,255,255,0) 70%);
}

.plx-12__clouds {
  top: 8%;
  block-size: 22vh;
}

.plx-12__ridge {
  bottom: 18%;
  block-size: 34vh;
}

.plx-12__hills {
  bottom: 6%;
  block-size: 26vh;
}

.plx-12__grass {
  bottom: -2px;
  block-size: 18vh;
}

.plx-12__content {
  position: relative;
  z-index: 3;
  inline-size: 100%;
  max-inline-size: 62rem;
  min-inline-size: 0;
  display: grid;
  gap: 18px;
}

.plx-12__badge {
  margin: 0;
  justify-self: start;
  padding: 7px 12px;
  border-radius: 999px;
  background: rgba(15,143,134,0.12);
  border: 1px solid rgba(15,143,134,0.3);
  font: 600 11px/1 var(--font-body);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #0b6b64;
}

.plx-12__h1 {
  margin: 0;
  max-inline-size: 34rem;
  font-family: var(--font-display);
  font-size: clamp(30px, 6.4vw, 62px);
  font-weight: 600;
  line-height: 1.04;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.plx-12__lede {
  margin: 0;
  max-inline-size: 30rem;
  font-size: clamp(15px, 3.2vw, 18px);
  line-height: 1.62;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-12__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
}

.plx-12__cta {
  display: inline-flex;
  align-items: center;
  min-height: 48px;
  padding: 0 24px;
  border-radius: 999px;
  background: var(--accent);
  color: #f2fffd;
  font: 600 15px/1 var(--font-body);
  text-decoration: none;
  box-shadow: 0 10px 24px -14px rgba(10,70,66,0.8);
}

.plx-12__cta:hover {
  background: #0b7a72;
}

.plx-12__link {
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  font: 600 14px/1 var(--font-body);
  color: #0b6b64;
  text-decoration: underline;
  text-underline-offset: 4px;
}

.plx-12__cta:focus-visible,
.plx-12__link:focus-visible {
  outline: 2px solid #0b3d3a;
  outline-offset: 3px;
}

.plx-12__card {
  margin-top: 10px;
  inline-size: 100%;
  max-inline-size: 22rem;
  min-inline-size: 0;
  padding: 16px;
  border-radius: 18px;
  border: 1px solid var(--rule);
  background: #fffdf8;
  box-shadow: 0 26px 50px -30px rgba(12,60,56,0.55);
}

.plx-12__cardhead {
  display: flex;
  align-items: center;
  gap: 9px;
  margin-bottom: 12px;
  min-inline-size: 0;
}

.plx-12__dot {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: var(--accent);
  flex: none;
}

.plx-12__cardtitle {
  margin: 0;
  font: 600 13px/1.3 var(--font-body);
  min-inline-size: 0;
}

.plx-12__rows {
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 8px;
}

.plx-12__rows li {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-size: 13px;
  color: var(--muted);
  padding-block-end: 8px;
  border-bottom: 1px solid var(--rule);
  min-inline-size: 0;
}

.plx-12__cardfoot {
  margin: 0;
  font-size: 12px;
  color: #0b6b64;
}

.plx-12__body {
  position: relative;
  z-index: 4;
  background: var(--cream);
  padding: clamp(40px, 8vw, 96px) clamp(20px, 5vw, 72px) 130px;
  display: grid;
  gap: clamp(34px, 6vw, 64px);
  border-top: 1px solid var(--rule);
}

.plx-12__section {
  max-inline-size: 38rem;
  min-inline-size: 0;
}

.plx-12__h2 {
  margin: 0 0 12px;
  font-family: var(--font-display);
  font-size: clamp(21px, 4.4vw, 32px);
  font-weight: 600;
  line-height: 1.14;
}

.plx-12__p {
  margin: 0;
  font-size: clamp(15px, 3.2vw, 17px);
  line-height: 1.72;
  color: #33544f;
  text-wrap: pretty;
}

@supports (animation-timeline: scroll()) {
  .plx-12__layer {
    animation: plx-12-drift linear both;
    animation-timeline: scroll(root);
  }
}

@keyframes plx-12-drift {
  /* Foreground moves ~55vh over full-page scroll, background barely shifts
       — the perceptible parallax range for a landing-page hero without
       triggering vestibular reduce-motion needs. Original -220px was too
       subtle to read as depth at typical 1080p+ page scroll distance. */

  to {
    transform: translate3d(0, calc(var(--k) * -8vh), 0);
  }
}

.plx-12.is-js .plx-12__layer {
  transform: translate3d(0, calc(var(--sy) * var(--k) * -0.22px), 0);
}

@media (prefers-reduced-motion: reduce) {
  .plx-12__layer,
    .plx-12.is-js .plx-12__layer {
    animation: none !important;
    transform: none !important;
    will-change: auto;
  }
}
```

## JavaScript
```js
const root = document.getElementById('plx-12-root');
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const native = window.CSS && CSS.supports && CSS.supports('animation-timeline', 'scroll()');
if (root && !native && !reduce) {
  root.classList.add('is-js');
  let queued = false;
  const write = () => {
    root.style.setProperty('--sy', String(window.scrollY));
    queued = false;
  };
  window.addEventListener('scroll', () => {
    if (!queued) { queued = true; requestAnimationFrame(write); }
  }, { passive: true });
  write();
}
```
