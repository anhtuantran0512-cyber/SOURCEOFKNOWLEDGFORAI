---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/horizontal-scroll-section-fake-horizontal-scroller/"
title: "Horizontal Scroll Section (Fake Horizontal Scroller)"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The GSAP-ScrollTrigger showpiece, rebuilt in pure CSS: the user scrolls down normally, but inside a pinned full-viewport panel a wide gallery track glides…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Scroll Section (Fake Horizontal Scroller)
Source: https://codefronts.com/motion/css-animation-timeline/horizontal-scroll-section-fake-horizontal-scroller/

The GSAP-ScrollTrigger showpiece, rebuilt in pure CSS: the user scrolls down normally, but inside a pinned full-viewport panel a wide gallery track glides horizontally — vertical progress through a tall wrapper is mapped 1:1 onto the track's translateX via a named view-timeline.
## HTML
```html
<section class="sda-05" aria-label="Horizontal scrolling gallery section" role="region" tabindex="0">
  <div class="sda-05__intro"><h2>Scroll down.<br>Travel sideways.</h2><p>A named view-timeline maps vertical progress onto horizontal motion.</p></div>
  <div class="sda-05__wrap">
    <div class="sda-05__pin">
      <div class="sda-05__track">
        <article class="sda-05__panel" style="--c:oklch(0.62 0.17 264)"><span>01</span><h3>Named timelines</h3><p>view-timeline: --sda-05-h on the tall wrapper broadcasts progress to every descendant.</p></article>
        <article class="sda-05__panel" style="--c:oklch(0.62 0.15 210)"><span>02</span><h3>Sticky pinning</h3><p>position:sticky holds this stage on screen while the wrapper scrolls past behind it.</p></article>
        <article class="sda-05__panel" style="--c:oklch(0.63 0.16 150)"><span>03</span><h3>One transform</h3><p>translateX(0 → -100% + 100vw): the end value self-adjusts to any number of panels.</p></article>
        <article class="sda-05__panel" style="--c:oklch(0.66 0.17 60)"><span>04</span><h3>No pin-spacers</h3><p>No resize listeners, no recalculation, no scroll hijack — momentum stays native.</p></article>
        <article class="sda-05__panel" style="--c:oklch(0.6 0.19 20)"><span>05</span><h3>Exit clean</h3><p>Past contain 100% the panel un-pins and normal vertical flow resumes.</p></article>
      </div>
      <div class="sda-05__dots" aria-hidden="true"><div class="sda-05__thumb"></div></div>
    </div>
  </div>
  <div class="sda-05__outro"><p>…and you're back to vertical. No hijack, no jank.</p></div>
</section>
```
## CSS
```css
.sda-05,
.sda-05 *,
.sda-05 *::before,
.sda-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-05 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: oklch(0.16 0.015 270);
  color: #eef0f8;
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}

.sda-05__intro,
.sda-05__outro {
  min-height: 70vh;
  display: grid;
  place-content: center;
  text-align: center;
  gap: 14px;
  padding: 24px;
}

.sda-05__intro h2 {
  font-size: clamp(30px,5vw,52px);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -.025em;
}

.sda-05__intro p,
.sda-05__outro p {
  font-size: 16px;
  color: #9ca1bd;
}

.sda-05__wrap {
  height: 380vh;
  view-timeline: --sda-05-h block;
}

.sda-05__pin {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.sda-05__track {
  display: flex;
  gap: 4vw;
  padding: 0 6vw;
  width: max-content;
}

.sda-05__panel {
  flex: none;
  width: min(560px,76vw);
  height: min(400px,62vh);
  border-radius: 26px;
  padding: 38px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 10px;
  background: linear-gradient(150deg,var(--c),oklch(from var(--c) calc(l - 0.2) c calc(h + 25)));
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.7);
}

.sda-05__panel span {
  font: 800 15px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  opacity: .65;
}

.sda-05__panel h3 {
  font-size: clamp(24px,3vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.sda-05__panel p {
  font-size: 15.5px;
  line-height: 1.55;
  max-width: 44ch;
  opacity: .92;
  text-wrap: pretty;
}

.sda-05__dots {
  width: min(320px,60%);
  height: 4px;
  border-radius: 99px;
  background: rgba(255,255,255,.14);
  margin: 34px auto 0;
  display: none;
}

.sda-05__thumb {
  width: 25%;
  height: 100%;
  border-radius: 99px;
  background: #fff;
}

.sda-05:focus-visible {
  outline: 3px solid oklch(0.65 0.15 210);
  outline-offset: -3px;
}

@supports (animation-timeline: view()) {
  .sda-05__dots {
    display: block;
  }

  .sda-05__track {
    animation: sda-05-slide linear both;
    animation-timeline: --sda-05-h;
    animation-range: contain 0% contain 100%;
  }

  .sda-05__thumb {
    animation: sda-05-thumb linear both;
    animation-timeline: --sda-05-h;
    animation-range: contain 0% contain 100%;
  }
}

@supports not (animation-timeline: view()) {
  .sda-05__wrap {
    height: auto;
  }

  .sda-05__pin {
    position: static;
    height: auto;
    overflow-x: auto;
    padding: 40px 0;
    -webkit-overflow-scrolling: touch;
  }

  .sda-05__track {
    width: max-content;
  }
}

@keyframes sda-05-slide {
  to {
    transform: translateX(calc(-100% + 100vw));
  }
}

@keyframes sda-05-thumb {
  to {
    transform: translateX(300%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-05__track,
    .sda-05__thumb {
    animation-timing-function: steps(4);
  }
}
```

## JavaScript
```js
/* No JavaScript — a named view-timeline on the 380vh wrapper drives the pinned track's translateX; the end value calc(-100% + 100vw) self-adapts to any panel count. */
```
