---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/pure-css-scroll-driven-text-reveal-timeline/"
title: "Pure CSS Scroll Driven Text Reveal Timeline"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Zero-JS scrubbing with CSS scroll-driven animations: a pinned manifesto whose words ink in as you read down (the karaoke effect), and a headline whose…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Scroll Driven Text Reveal Timeline
Source: https://codefronts.com/motion/css-text-animations/pure-css-scroll-driven-text-reveal-timeline/

Zero-JS scrubbing with CSS scroll-driven animations: a pinned manifesto whose words ink in as you read down (the karaoke effect), and a headline whose letters fly home from scattered poses — both wired to a named view-timeline, no observers, no scroll listeners.
## HTML
```html
<div class="cat-02-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-02a" aria-label="Scroll driven karaoke text highlight">
  <div class="cat-02a__tall">
    <div class="cat-02a__pin">
      <div class="cat-02a__inner">
        <p class="cat-02a__kicker">Scroll to read — the scrollbar is the timeline</p>
        <p class="cat-02a__copy">We stopped animating on timers. The scroll position is the clock now — every word inks in exactly as fast as you read, pauses when you pause, and rewinds when you change your mind.</p>
        <p class="cat-02a__more" aria-hidden="true">↓ keep scrolling</p>
      </div>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-02b" aria-label="Letters assemble while scrolling">
  <div class="cat-02b__tall">
    <div class="cat-02b__pin">
      <div class="cat-02b__inner">
        <h1 class="cat-02b__word" aria-label="ASSEMBLED">
          <span aria-hidden="true"><i style="--sx:-140;--sy:-90;--sr:-40deg">A</i><i style="--sx:110;--sy:-140;--sr:28deg">S</i><i style="--sx:-70;--sy:120;--sr:-16deg">S</i><i style="--sx:160;--sy:60;--sr:38deg">E</i><i style="--sx:-160;--sy:30;--sr:20deg">M</i><i style="--sx:60;--sy:150;--sr:-32deg">B</i><i style="--sx:-40;--sy:-150;--sr:14deg">L</i><i style="--sx:140;--sy:-50;--sr:-24deg">E</i><i style="--sx:-110;--sy:80;--sr:30deg">D</i></span>
        </h1>
        <p class="cat-02b__sub" aria-hidden="true">scroll scrubs every letter home — scroll back up to shatter it</p>
      </div>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.cat-02-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.cat-02-group > section {
  width: 100%;
}

.cat-02a,
.cat-02a *,
.cat-02a *::before,
.cat-02a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-02a {
  width: 100%;
  background: #f6f3ec;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-02a__tall {
  height: 240vh;
  view-timeline-name: --cat16a-read;
}

.cat-02a__pin {
  position: sticky;
  top: 0;
  height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
}

.cat-02a__inner {
  max-width: 820px;
}

.cat-02a__kicker {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: rgba(30,28,24,.45);
  margin-bottom: 26px;
}

.cat-02a__copy {
  font-size: clamp(26px,4.2vw,44px);
  font-weight: 500;
  line-height: 1.42;
  letter-spacing: -.01em;
  color: #1e1c18;
  text-wrap: pretty;
}

.cat-02a__more {
  margin-top: 34px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  letter-spacing: .18em;
  color: rgba(30,28,24,.4);
}

@supports (animation-timeline: view()) {
  .cat-02a__copy {
    background: linear-gradient(90deg,#1e1c18 50%,rgba(30,28,24,.16) 50%) 100% 0/200% 100% no-repeat;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: cat-02a-ink linear both;
    animation-timeline: --cat16a-read;
    animation-range: contain 8% contain 85%;
  }
}

@keyframes cat-02a-ink {
  to {
    background-position: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-02a__copy {
    animation: none;
    background-position: 0 0;
  }
}

.cat-02b,
.cat-02b *,
.cat-02b *::before,
.cat-02b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-02b {
  width: 100%;
  background: #0c0e13;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.cat-02b__tall {
  height: 230vh;
  view-timeline-name: --cat16b-asm;
}

.cat-02b__pin {
  position: sticky;
  top: 0;
  height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  overflow: hidden;
}

.cat-02b__inner {
  text-align: center;
}

.cat-02b__word {
  font-size: clamp(40px,8.4vw,110px);
  font-weight: 900;
  letter-spacing: .02em;
  color: #eef2fa;
}

.cat-02b__word i {
  display: inline-block;
  font-style: normal;
}

.cat-02b__word i:nth-child(even) {
  color: oklch(0.8 0.16 200);
}

.cat-02b__sub {
  margin-top: 26px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(180,200,230,.4);
}

@supports (animation-timeline: view()) {
  .cat-02b__word i {
    animation: cat-02b-home linear both;
    animation-timeline: --cat16b-asm;
    animation-range: contain 5% contain 70%;
  }
}

@keyframes cat-02b-home {
  from {
    transform: translate(calc(var(--sx)*1px),calc(var(--sy)*1px)) rotate(var(--sr));
    opacity: .15;
    filter: blur(3px);
  }

  to {
    transform: translate(0,0) rotate(0);
    opacity: 1;
    filter: blur(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-02b__word i {
    animation: none;
    transform: none;
    opacity: 1;
    filter: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the 240vh wrapper names a view-timeline; the pinned paragraph's two-color gradient wipes from faded to ink as background-position scrubs with scroll. */

/* No JavaScript — one keyframe, per-letter inline start poses; scroll progress through the wrapper scrubs every letter from its scatter pose to identity. */
```
