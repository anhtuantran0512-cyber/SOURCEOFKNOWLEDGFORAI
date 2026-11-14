---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/fade-reveal-elements-on-scroll/"
title: "Fade & Reveal Elements on Scroll"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The IntersectionObserver killer: feature cards fade, slide, scale and un-blur into place as they enter the scrollport — four reveal flavours driven by…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fade & Reveal Elements on Scroll
Source: https://codefronts.com/motion/css-animation-timeline/fade-reveal-elements-on-scroll/

The IntersectionObserver killer: feature cards fade, slide, scale and un-blur into place as they enter the scrollport — four reveal flavours driven by animation-timeline: view() and animation-range, with reveal progress tied to the element's own position, not a one-shot class toggle.
## HTML
```html
<section class="sda-02" aria-label="Scroll to reveal feature cards" role="region" tabindex="0">
  <header class="sda-02__head"><p class="sda-02__kicker">view() + animation-range</p><h2>Everything reveals itself.<br>Nothing observes anything.</h2><p class="sda-02__sub">Scroll down — each card scrubs into place on its own view timeline.</p></header>
  <div class="sda-02__grid">
    <article class="sda-02__card sda-02__card--up"><span class="sda-02__badge">fade-up</span><h3>Entrance, not appearance</h3><p>The card slides 40px up while fading in, mapped to its first 35% of viewport travel.</p></article>
    <article class="sda-02__card sda-02__card--left"><span class="sda-02__badge">fade-left</span><h3>Directional context</h3><p>Sliding in from the side reads as “new information arriving”, useful for alternating layouts.</p></article>
    <article class="sda-02__card sda-02__card--scale"><span class="sda-02__badge">scale-in</span><h3>Weight and presence</h3><p>Scaling from 0.85 gives cards physical weight — pair it with a soft shadow ramp.</p></article>
    <article class="sda-02__card sda-02__card--blur"><span class="sda-02__badge">blur-in</span><h3>Focus pull</h3><p>Un-blurring mimics a camera rack focus. Expensive — reserve it for hero moments.</p></article>
    <article class="sda-02__card sda-02__card--up"><span class="sda-02__badge">fade-up</span><h3>Scrubbed, reversible</h3><p>Scroll back up: the animation runs backwards. Try that with a class-toggling observer.</p></article>
    <article class="sda-02__card sda-02__card--scale"><span class="sda-02__badge">scale-in</span><h3>Zero JavaScript</h3><p>No thresholds, no rootMargin math, no unobserve bookkeeping. One declaration per flavour.</p></article>
  </div>
</section>
```
## CSS
```css
.sda-02,
.sda-02 *,
.sda-02 *::before,
.sda-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-02 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: oklch(0.22 0.03 265);
  color: #eef0f8;
  width: 100%;
  height: 100vh;
  overflow-y: auto;
  padding: 0 22px;
}

.sda-02__head {
  width: min(680px,100%);
  margin: 0 auto;
  padding: 16vh 0 10vh;
  text-align: center;
}

.sda-02__kicker {
  font: 700 11px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: oklch(0.75 0.14 200);
  margin-bottom: 16px;
}

.sda-02__head h2 {
  font-size: clamp(28px,4.5vw,44px);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -.02em;
  text-wrap: pretty;
}

.sda-02__sub {
  margin-top: 16px;
  font-size: 16px;
  color: #a7abc4;
}

.sda-02__grid {
  width: min(760px,100%);
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(280px,1fr));
  gap: 26px;
  padding-bottom: 24vh;
}

.sda-02__card {
  background: oklch(0.28 0.035 265);
  border: 1px solid oklch(0.36 0.04 265);
  border-radius: 18px;
  padding: 28px;
  min-height: 190px;
}

.sda-02__badge {
  display: inline-block;
  font: 700 10.5px ui-monospace,Menlo,monospace;
  letter-spacing: .1em;
  color: oklch(0.8 0.13 200);
  background: oklch(0.32 0.05 220);
  padding: 5px 9px;
  border-radius: 6px;
  margin-bottom: 14px;
}

.sda-02__card h3 {
  font-size: 19px;
  font-weight: 700;
  margin-bottom: 8px;
  letter-spacing: -.01em;
}

.sda-02__card p {
  font-size: 14.5px;
  line-height: 1.6;
  color: #b9bdd4;
  text-wrap: pretty;
}

.sda-02:focus-visible {
  outline: 3px solid oklch(0.75 0.14 200);
  outline-offset: -3px;
}

@supports (animation-timeline: view()) {
  .sda-02__card {
    animation: linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 35%;
  }

  .sda-02__card--up {
    animation-name: sda-02-up;
  }

  .sda-02__card--left {
    animation-name: sda-02-left;
  }

  .sda-02__card--scale {
    animation-name: sda-02-scale;
  }

  .sda-02__card--blur {
    animation-name: sda-02-blur;
  }
}

@keyframes sda-02-up {
  from {
    opacity: 0;
    transform: translateY(40px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes sda-02-left {
  from {
    opacity: 0;
    transform: translateX(-48px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes sda-02-scale {
  from {
    opacity: 0;
    transform: scale(.85);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes sda-02-blur {
  from {
    opacity: 0;
    filter: blur(10px);
  }

  to {
    opacity: 1;
    filter: blur(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-02__card {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each card's reveal is scrubbed by its own anonymous view() timeline; animation-range: entry 0% cover 35% defines exactly where the tween lives. */
```
