---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/pure-css-parallax-image-hero/"
title: "Pure CSS Parallax Image Hero"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "Parallax that finally works on iOS: the hero photograph drifts upward at roughly half the speed of the foreground headline as the user scrolls away — modern…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Parallax Image Hero
Source: https://codefronts.com/motion/css-animation-timeline/pure-css-parallax-image-hero/

Parallax that finally works on iOS: the hero photograph drifts upward at roughly half the speed of the foreground headline as the user scrolls away — modern scroll-driven transforms replacing the broken background-attachment:fixed hack, fully composited, zero jitter on mobile.
## HTML
```html
<section class="sda-06" aria-label="Parallax hero demo" role="region" tabindex="0">
  <header class="sda-06__hero">
    <img class="sda-06__img" src="https://picsum.photos/seed/parallax-ridge/1600/1000" width="1600" height="1000" alt="Mountain ridge under drifting cloud" loading="eager">
    <div class="sda-06__scrim" aria-hidden="true"></div>
    <div class="sda-06__fg"><p class="sda-06__kicker">Est. 4,102 m</p><h2>The Ridge Line</h2><p class="sda-06__sub">Two planes, two speeds, one scroll.</p></div>
  </header>
  <div class="sda-06__body">
    <h3>Depth without the fixed-attachment hack</h3>
    <p>For a decade the go-to parallax was <code>background-attachment: fixed</code> — and for a decade iOS Safari has refused to composite it, silently downgrading to a static image or, worse, repainting every frame on Android. This version animates a real, composited transform instead, so the parallax is identical on every modern device.</p>
    <p>Scroll up and down across the hero boundary and watch the seam: the image plane moves at roughly half scroll speed, the type at three-quarters against it, and the scrim eases in to hand off contrast to this text block.</p>
    <p>Because the timeline is the hero's own <code>view()</code> progress, the effect needs no measurements — resize the window, rotate the phone, nothing recalculates because nothing was ever measured.</p>
  </div>
</section>
```
## CSS
```css
.sda-06,
.sda-06 *,
.sda-06 *::before,
.sda-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-06 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #101318;
  color: #e8eaf2;
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}

.sda-06__hero {
  position: relative;
  height: 86vh;
  overflow: clip;
  display: grid;
  place-content: center;
  text-align: center;
}

.sda-06__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 130%;
  object-fit: cover;
  top: -15%;
}

.sda-06__scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(10,12,18,.25),rgba(10,12,18,.9));
  opacity: .35;
}

.sda-06__fg {
  position: relative;
  padding: 24px;
  text-shadow: 0 2px 24px rgba(0,0,0,.55);
}

.sda-06__kicker {
  font: 700 12px ui-monospace,Menlo,monospace;
  letter-spacing: .24em;
  text-transform: uppercase;
  opacity: .85;
  margin-bottom: 12px;
}

.sda-06__fg h2 {
  font-size: clamp(40px,8vw,84px);
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1;
}

.sda-06__sub {
  margin-top: 14px;
  font-size: 16px;
  opacity: .9;
}

.sda-06__body {
  width: min(620px,100%);
  margin: 0 auto;
  padding: 60px 24px 40vh;
}

.sda-06__body h3 {
  font-size: 23px;
  font-weight: 700;
  letter-spacing: -.01em;
  margin-bottom: 16px;
}

.sda-06__body p {
  font-size: 16px;
  line-height: 1.75;
  margin-bottom: 20px;
  color: #c3c7d4;
  text-wrap: pretty;
}

.sda-06__body code {
  font: 600 13.5px ui-monospace,Menlo,monospace;
  background: #1d222c;
  padding: 2px 6px;
  border-radius: 5px;
}

.sda-06:focus-visible {
  outline: 3px solid oklch(0.7 0.13 220);
  outline-offset: -3px;
}

@supports (animation-timeline: view()) {
  .sda-06__img {
    animation: sda-06-bg linear both;
    animation-timeline: view();
    animation-range: exit;
  }

  .sda-06__fg {
    animation: sda-06-fg linear both;
    animation-timeline: view();
    animation-range: exit;
  }

  .sda-06__scrim {
    animation: sda-06-scrim linear both;
    animation-timeline: view();
    animation-range: exit;
  }
}

@keyframes sda-06-bg {
  to {
    transform: translateY(12%);
  }
}

@keyframes sda-06-fg {
  to {
    transform: translateY(-34%);
    opacity: 0;
  }
}

@keyframes sda-06-scrim {
  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-06__img,
    .sda-06__fg,
    .sda-06__scrim {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the image, headline and scrim ride the hero's own view() exit range at three different speeds; composited transforms replace the iOS-broken background-attachment:fixed hack. */
```
