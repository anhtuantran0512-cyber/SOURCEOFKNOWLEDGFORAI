---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/split-column-reverse-scrolling/"
title: "Split Column Reverse Scrolling"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The 'expensive agency site' look: as the user scrolls down, the left editorial column rises normally while the right image column glides DOWN in the opposite…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split Column Reverse Scrolling
Source: https://codefronts.com/motion/css-animation-timeline/split-column-reverse-scrolling/

The 'expensive agency site' look: as the user scrolls down, the left editorial column rises normally while the right image column glides DOWN in the opposite direction — an asymmetric split-screen built from one negative translateY hooked to a scroll() timeline.
## HTML
```html
<section class="sda-08" aria-label="Split columns scrolling in opposite directions" role="region" tabindex="0">
  <div class="sda-08__cols">
    <div class="sda-08__left">
      <p class="sda-08__kicker">FW/26 Collection</p>
      <h2>Counter<br>current</h2>
      <p class="sda-08__copy">Scroll down. The words rise, the imagery sinks. Two flows, one gesture — the asymmetry is the message.</p>
      <p class="sda-08__copy">Under the hood it's a single negative <code>translateY</code> bound to the scroller's timeline: the column doesn't scroll backwards, it just out-runs the scroll in paint space.</p>
      <p class="sda-08__copy">No wheel hijack. No inverted wheel math. Native momentum, native accessibility — the DOM never moves, only pixels do.</p>
      <p class="sda-08__copy">Because the browser owns the mapping, fast flicks, rubber-banding and scroll-snap all keep working exactly as the OS intends.</p>
      <p class="sda-08__end">— fin —</p>
    </div>
    <div class="sda-08__right" aria-hidden="false">
      <div class="sda-08__strip">
        <figure class="sda-08__fig"><img src="https://picsum.photos/seed/rev-a/460/560" width="460" height="560" alt="Model in oversized wool coat"><figcaption>Look 01 — Wool, oversized</figcaption></figure>
        <figure class="sda-08__fig"><img src="https://picsum.photos/seed/rev-b/460/560" width="460" height="560" alt="Detail of pleated fabric"><figcaption>Look 02 — Pleats, close</figcaption></figure>
        <figure class="sda-08__fig"><img src="https://picsum.photos/seed/rev-c/460/560" width="460" height="560" alt="Silhouette against concrete"><figcaption>Look 03 — Concrete study</figcaption></figure>
        <figure class="sda-08__fig"><img src="https://picsum.photos/seed/rev-d/460/560" width="460" height="560" alt="Layered knitwear texture"><figcaption>Look 04 — Layered knit</figcaption></figure>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.sda-08,
.sda-08 *,
.sda-08 *::before,
.sda-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-08 {
  font-family: Georgia,'Times New Roman',serif;
  background: oklch(0.97 0.005 90);
  color: oklch(0.22 0.01 60);
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}

.sda-08__cols {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(24px,5vw,72px);
  width: min(1020px,100%);
  margin: 0 auto;
  padding: 0 24px;
  overflow: clip;
}

.sda-08__left {
  padding: 16vh 0 30vh;
}

.sda-08__kicker {
  font: 700 11px 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: oklch(0.5 0.1 40);
  margin-bottom: 20px;
}

.sda-08__left h2 {
  font-size: clamp(40px,6vw,72px);
  line-height: .98;
  letter-spacing: -.02em;
  font-weight: 400;
  font-style: italic;
  margin-bottom: 36px;
}

.sda-08__copy {
  font-size: 16.5px;
  line-height: 1.8;
  margin-bottom: 26px;
  max-width: 42ch;
  text-wrap: pretty;
}

.sda-08__copy code {
  font: 600 13.5px ui-monospace,Menlo,monospace;
  background: oklch(0.92 0.01 90);
  padding: 2px 6px;
  border-radius: 5px;
}

.sda-08__end {
  font-style: italic;
  color: oklch(0.55 0.02 60);
  padding-top: 8vh;
}

.sda-08__right {
  position: relative;
}

.sda-08__strip {
  display: flex;
  flex-direction: column;
  gap: 28px;
  padding: 6vh 0;
}

.sda-08__fig img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 6px;
  filter: saturate(.85);
}

.sda-08__fig figcaption {
  font: italic 13px Georgia,serif;
  color: oklch(0.5 0.02 60);
  padding-top: 8px;
}

.sda-08:focus-visible {
  outline: 3px solid oklch(0.5 0.1 40);
  outline-offset: -3px;
}

@supports (animation-timeline: scroll()) {
  .sda-08__strip {
    transform: translateY(-42%);
    animation: sda-08-sink linear both;
    animation-timeline: scroll();
  }
}

@keyframes sda-08-sink {
  from {
    transform: translateY(-42%);
  }

  to {
    transform: translateY(0);
  }
}

@media (max-width: 640px) {
  .sda-08__cols {
    grid-template-columns: 1fr;
  }

  .sda-08__strip {
    transform: none;
    animation: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-08__strip {
    transform: none;
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the image strip is pre-translated up and animated back to 0 on a scroll() timeline; scroll moves it up, the animation pushes it down, and the net motion reads as reverse scrolling. */
```
