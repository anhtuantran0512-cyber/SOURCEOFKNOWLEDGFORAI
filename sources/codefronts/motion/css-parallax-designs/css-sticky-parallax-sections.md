---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/css-sticky-parallax-sections/"
title: "Sticky Parallax Sections Stripe Linear Style"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "Full-viewport sections that pin as they arrive, animate their own content while they hold the frame, then release as the next section slides over them."
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Parallax Sections Stripe Linear Style
Source: https://codefronts.com/motion/css-parallax-designs/css-sticky-parallax-sections/

Full-viewport sections that pin as they arrive, animate their own content while they hold the frame, then release as the next section slides over them. Each panel owns a view() timeline, so the internal choreography restarts per section — the pattern behind most modern SaaS product tours.
## HTML
```html
<div class="plx-15">
  <header class="plx-15__intro">
    <p class="plx-15__brand">Cadence</p>
    <h1 class="plx-15__h1">Three things your on-call rotation should already do</h1>
    <p class="plx-15__lede">Scroll — each section pins, plays, and hands off to the next.</p>
  </header>
  <section class="plx-15__panel plx-15__panel--1" style="--accent: #8b7cff">
    <div class="plx-15__inner">
      <div class="plx-15__copy">
        <p class="plx-15__step">01</p>
        <h2 class="plx-15__h2">Route by service, not by human</h2>
        <p class="plx-15__p">Ownership lives with the service definition. When a team splits, the routing follows the code, so nobody inherits pages for something they no longer run.</p>
      </div>
      <div class="plx-15__media" aria-hidden="true">
        <div class="plx-15__pane"><span class="plx-15__row"></span><span class="plx-15__row plx-15__row--short"></span><span class="plx-15__row"></span><span class="plx-15__row plx-15__row--short"></span></div>
      </div>
    </div>
  </section>
  <section class="plx-15__panel plx-15__panel--2" style="--accent: #4bd6b0">
    <div class="plx-15__inner">
      <div class="plx-15__copy">
        <p class="plx-15__step">02</p>
        <h2 class="plx-15__h2">Escalate on silence</h2>
        <p class="plx-15__p">No acknowledgement in four minutes moves the page up a level. The timer runs from delivery, not from the alert firing, so a slow push does not cost you the window.</p>
      </div>
      <div class="plx-15__media" aria-hidden="true">
        <div class="plx-15__pane"><span class="plx-15__bar"></span><span class="plx-15__bar plx-15__bar--tall"></span><span class="plx-15__bar"></span><span class="plx-15__bar plx-15__bar--tall"></span><span class="plx-15__bar"></span></div>
      </div>
    </div>
  </section>
  <section class="plx-15__panel plx-15__panel--3" style="--accent: #ffa94d">
    <div class="plx-15__inner">
      <div class="plx-15__copy">
        <p class="plx-15__step">03</p>
        <h2 class="plx-15__h2">Close the loop in the incident</h2>
        <p class="plx-15__p">The retro doc is created when the incident opens, not after it closes. Timeline, graphs and the chat transcript are attached automatically.</p>
      </div>
      <div class="plx-15__media" aria-hidden="true">
        <div class="plx-15__pane"><span class="plx-15__dot"></span><span class="plx-15__row"></span><span class="plx-15__row plx-15__row--short"></span><span class="plx-15__dot"></span><span class="plx-15__row"></span></div>
      </div>
    </div>
  </section>
  <footer class="plx-15__foot">
    <p class="plx-15__p">Cadence is used by 340 engineering teams. Pricing per service, not per seat.</p>
  </footer>
</div>
```
## CSS
```css
.plx-15 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Geist", "Inter", system-ui, -apple-system, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --bg: #080d1f;
  --panel: #101736;
  --ink: #eaf0ff;
  --muted: #93a1c9;
  --edge: rgba(150,175,255,0.16);
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-15 * {
  box-sizing: border-box;
}

.plx-15__intro {
  padding: clamp(40px, 9vw, 110px) clamp(20px, 5vw, 70px) clamp(30px, 6vw, 70px);
  max-inline-size: 52rem;
}

.plx-15__brand {
  margin: 0 0 18px;
  font: 620 12px/1 var(--font-display);
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #8b7cff;
}

.plx-15__h1 {
  margin: 0 0 14px;
  font-family: var(--font-display);
  font-size: clamp(28px, 6.2vw, 58px);
  font-weight: 620;
  line-height: 1.04;
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.plx-15__lede {
  margin: 0;
  font-size: clamp(15px, 3.2vw, 18px);
  line-height: 1.6;
  color: var(--muted);
}

.plx-15__panel {
  position: sticky;
  top: 0;
  min-block-size: 96svh;
  display: grid;
  align-items: center;
  padding: clamp(24px, 5vw, 64px);
  background: var(--panel);
  border: 1px solid var(--edge);
  border-bottom: 0;
  border-radius: 26px 26px 0 0;
  box-shadow: 0 -24px 60px -30px rgba(0,0,0,0.8);
}

.plx-15__panel--1 {
  z-index: 1;
}

.plx-15__panel--2 {
  z-index: 2;
  background: #0d1a30;
}

.plx-15__panel--3 {
  z-index: 3;
  background: #121427;
}

.plx-15__inner {
  inline-size: 100%;
  max-inline-size: 68rem;
  margin-inline: auto;
  display: grid;
  gap: clamp(24px, 4vw, 54px);
  align-items: center;
}

.plx-15__copy {
  min-inline-size: 0;
  will-change: transform, opacity;
}

.plx-15__step {
  margin: 0 0 16px;
  font-family: var(--font-display);
  font-size: 13px;
  font-weight: 620;
  letter-spacing: 0.2em;
  color: var(--accent);
}

.plx-15__h2 {
  margin: 0 0 14px;
  font-family: var(--font-display);
  font-size: clamp(24px, 5vw, 44px);
  font-weight: 620;
  line-height: 1.06;
  letter-spacing: -0.03em;
}

.plx-15__p {
  margin: 0;
  max-inline-size: 32rem;
  font-size: clamp(15px, 3.2vw, 17px);
  line-height: 1.68;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-15__media {
  min-inline-size: 0;
  will-change: transform;
}

.plx-15__pane {
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: clamp(180px, 34vh, 300px);
  padding: clamp(16px, 3vw, 28px);
  border-radius: 18px;
  border: 1px solid var(--edge);
  background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
  box-shadow: 0 24px 50px -34px rgba(0,0,0,0.9);
}

.plx-15__row {
  display: block;
  block-size: 12px;
  border-radius: 999px;
  background: rgba(190,205,255,0.22);
}

.plx-15__row--short {
  inline-size: 58%;
  background: var(--accent);
  opacity: 0.7;
}

.plx-15__pane:has(.plx-15__bar) {
  grid-auto-flow: column;
  align-items: end;
  gap: 10px;
}

.plx-15__bar {
  display: block;
  inline-size: 100%;
  block-size: 40%;
  border-radius: 8px 8px 2px 2px;
  background: rgba(190,205,255,0.2);
}

.plx-15__bar--tall {
  block-size: 88%;
  background: var(--accent);
  opacity: 0.8;
}

.plx-15__dot {
  inline-size: 14px;
  block-size: 14px;
  border-radius: 50%;
  background: var(--accent);
}

.plx-15__foot {
  position: relative;
  z-index: 4;
  background: var(--bg);
  padding: clamp(44px, 8vw, 100px) clamp(20px, 5vw, 70px) 130px;
}

.plx-15__foot .plx-15__p {
  color: var(--muted);
}

@media (min-width: 860px) {
  .plx-15__inner {
    grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr);
  }
}

@supports (animation-timeline: view()) {
  .plx-15__copy {
    animation: plx-15-copy linear both;
    animation-timeline: view();
    animation-range: entry 30% contain 40%;
  }

  .plx-15__media {
    animation: plx-15-media linear both;
    animation-timeline: view();
    animation-range: entry 10% exit 100%;
  }
}

@keyframes plx-15-copy {
  from {
    transform: translateY(26px);
    opacity: 0.3;
  }

  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes plx-15-media {
  from {
    transform: translateY(46px) scale(0.97);
  }

  to {
    transform: translateY(-40px) scale(1.02);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-15__copy,
    .plx-15__media {
    animation: none !important;
    transform: none !important;
    opacity: 1 !important;
    will-change: auto;
  }
}
```
