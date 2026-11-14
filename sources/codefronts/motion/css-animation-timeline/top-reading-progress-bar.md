---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/top-reading-progress-bar/"
title: "Top Reading Progress Bar"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The 'Hello World' of scroll-driven animations, finished to production standard: a gradient progress bar pinned to the top of the article scales from 0 → 100%…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Top Reading Progress Bar
Source: https://codefronts.com/motion/css-animation-timeline/top-reading-progress-bar/

The 'Hello World' of scroll-driven animations, finished to production standard: a gradient progress bar pinned to the top of the article scales from 0 → 100% width as the reader moves through the page, plus a live percentage counter — both pure CSS, driven by animation-timeline: scroll(), no scroll listener, no layout thrash.
## HTML
```html
<section class="sda-01" aria-label="Article with reading progress bar" role="region" tabindex="0">
  <div class="sda-01__rail" aria-hidden="true"><div class="sda-01__bar"></div><div class="sda-01__pct"></div></div>
  <article class="sda-01__page">
    <p class="sda-01__kicker">Motions / Reading UX</p>
    <h2>Why scroll listeners are quietly taxing your INP score</h2>
    <p>Every <code>scroll</code> event handler you attach runs on the main thread — the same thread that must stay free to answer the user's next tap. During a fast flick a browser can fire dozens of scroll events per second, and each one re-enters your JavaScript.</p>
    <p>Scroll-driven animations invert the model. You declare the relationship — "this bar's scale equals the page's scroll progress" — once, in CSS. The compositor owns the mapping and updates it frame-perfectly, even while the main thread is busy parsing, hydrating, or blocked entirely.</p>
    <p>The practical difference shows up in profiling: a JS progress bar keeps a long purple ribbon of style/layout work alive for the whole scroll; the CSS version shows a flat, idle main thread with the animation running on the compositor track.</p>
    <p>It also degrades better. If the animation can't run, nothing is subscribed, nothing leaks, and there is no half-initialised widget — the article simply renders.</p>
    <p>Reader-facing benefits compound too: the bar never lags the thumb on mobile, never rubber-bands after the scroll settles, and never causes the layout shift that a late-hydrating JS bar can.</p>
    <p>Scroll to the end and the counter lands on exactly 100 — the timeline is mathematically bound to scroll range, not sampled from events, so there is no drift to correct.</p>
    <p class="sda-01__fin">— End of article —</p>
  </article>
</section>
```
## CSS
```css
.sda-01,
.sda-01 *,
.sda-01 *::before,
.sda-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --sda-01-p {
  syntax: '<integer>';
  inherits: true;
  initial-value: 0;
}

.sda-01 {
  --bar: linear-gradient(90deg,oklch(0.65 0.19 264),oklch(0.7 0.17 330));
  font-family: Georgia,'Times New Roman',serif;
  background: #faf8f4;
  color: #241f1a;
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}

.sda-01__rail {
  position: sticky;
  top: 0;
  z-index: 5;
  height: 0;
  display: none;
}

.sda-01__bar {
  height: 5px;
  background: var(--bar);
  transform: scaleX(0);
  transform-origin: left;
}

.sda-01__pct {
  position: absolute;
  top: 12px;
  right: 14px;
  font: 700 12px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .06em;
  color: #fff;
  background: oklch(0.35 0.06 270);
  padding: 6px 10px;
  border-radius: 999px;
  counter-reset: sda01 var(--sda-01-p);
}

.sda-01__pct::after {
  content: counter(sda01) '% read';
}

.sda-01__page {
  width: min(640px,100%);
  margin: 0 auto;
  padding: 56px 24px 80px;
}

.sda-01__kicker {
  font: 700 11px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: oklch(0.55 0.17 264);
  margin-bottom: 14px;
}

.sda-01 h2 {
  font-size: clamp(26px,4vw,34px);
  line-height: 1.2;
  letter-spacing: -.01em;
  margin-bottom: 24px;
  text-wrap: pretty;
}

.sda-01__page p {
  font-size: 17px;
  line-height: 1.75;
  margin-bottom: 22px;
  text-wrap: pretty;
}

.sda-01__page code {
  font: 600 14px ui-monospace,Menlo,monospace;
  background: #efe9df;
  padding: 2px 6px;
  border-radius: 5px;
}

.sda-01__fin {
  text-align: center;
  font-style: italic;
  color: #8b8378;
  padding-top: 24px;
}

.sda-01:focus-visible {
  outline: 3px solid oklch(0.65 0.19 264);
  outline-offset: -3px;
}

@supports (animation-timeline: scroll()) {
  .sda-01__rail {
    display: block;
  }

  .sda-01__bar {
    animation: sda-01-grow linear both;
    animation-timeline: scroll();
  }

  .sda-01__pct {
    animation: sda-01-count linear both;
    animation-timeline: scroll();
  }
}

@keyframes sda-01-grow {
  to {
    transform: scaleX(1);
  }
}

@keyframes sda-01-count {
  from {
    --sda-01-p: 0;
  }

  to {
    --sda-01-p: 100;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-01__bar,
    .sda-01__pct {
    animation-duration: 1ms;
  }
}
```

## JavaScript
```js
/* No JavaScript — animation-timeline: scroll() binds the bar's scaleX and a @property-driven counter() directly to the scroller's progress, entirely on the compositor. */
```
