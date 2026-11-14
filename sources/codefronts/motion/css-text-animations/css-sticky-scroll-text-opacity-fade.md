---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-sticky-scroll-text-opacity-fade/"
title: "CSS Sticky Scroll Text Opacity Fade"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "The pinned-hero exit, scrubbed by scroll alone: a full-bleed photographic hero whose title blurs, lifts and fades exactly in step with the panel sliding over…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Scroll Text Opacity Fade
Source: https://codefronts.com/motion/css-text-animations/css-sticky-scroll-text-opacity-fade/

The pinned-hero exit, scrubbed by scroll alone: a full-bleed photographic hero whose title blurs, lifts and fades exactly in step with the panel sliding over it, and a chapter sequence where three pinned lines crossfade through ranges of one shared timeline.
## HTML
```html
<div class="cat-03-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-03a" aria-label="Sticky hero that fades as you scroll">
  <div class="cat-03a__tall">
    <div class="cat-03a__pin">
      <img class="cat-03a__bg" src="https://picsum.photos/seed/ridgeline/1600/1000" alt="" loading="lazy">
      <div class="cat-03a__veil" aria-hidden="true"></div>
      <div class="cat-03a__content">
        <h1 class="cat-03a__title">Built to outlast<br>the scroll</h1>
        <p class="cat-03a__sub">↓ the title exits in lockstep with your thumb</p>
      </div>
    </div>
    <article class="cat-03a__panel">
      <h2>…and the story continues</h2>
      <p>This panel slides over the pinned hero. In browsers with scroll-driven animations the title above blurred, lifted and faded against exactly this hand-off — scroll back up and it reassembles.</p>
    </article>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-03b" aria-label="Pinned chapters crossfading on scroll">
  <div class="cat-03b__tall">
    <div class="cat-03b__pin">
      <p class="cat-03b__count" aria-hidden="true">scroll — three chapters, one timeline</p>
      <div class="cat-03b__stack">
        <h2 class="cat-03b__line" style="--from:cover 2%;--to:cover 38%">We started small.</h2>
        <h2 class="cat-03b__line" style="--from:cover 33%;--to:cover 69%">We shipped daily.</h2>
        <h2 class="cat-03b__line" style="--from:cover 64%;--to:cover 100%">Now we're everywhere.</h2>
      </div>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.cat-03-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.cat-03-group > section {
  width: 100%;
}

.cat-03a,
.cat-03a *,
.cat-03a *::before,
.cat-03a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-03a {
  width: 100%;
  background: #101318;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.cat-03a__tall {
  position: relative;
  height: 230vh;
  view-timeline-name: --cat18a-hero;
}

.cat-03a__pin {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: hidden;
  display: grid;
  place-items: center;
}

.cat-03a__bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.cat-03a__veil {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,rgb(10 13 20/.5),rgb(10 13 20/.78));
}

.cat-03a__content {
  position: relative;
  text-align: center;
  padding: 0 24px;
}

.cat-03a__title {
  font-size: clamp(44px,8vw,104px);
  font-weight: 900;
  line-height: 1.02;
  letter-spacing: -.02em;
  color: #f4f6fb;
  text-shadow: 0 20px 60px rgb(0 0 0/.5);
}

.cat-03a__sub {
  margin-top: 22px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  letter-spacing: .16em;
  color: rgba(230,238,252,.65);
}

.cat-03a__panel {
  position: relative;
  min-height: 100vh;
  background: #f4f1ea;
  color: #1d1a15;
  display: grid;
  place-content: center;
  gap: 16px;
  padding: 80px clamp(24px,8vw,120px);
  border-radius: 28px 28px 0 0;
}

.cat-03a__panel h2 {
  font-size: clamp(26px,3.6vw,40px);
  font-weight: 800;
  letter-spacing: -.01em;
}

.cat-03a__panel p {
  max-width: 560px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 16.5px;
  line-height: 1.65;
  color: rgba(29,26,21,.75);
}

@supports (animation-timeline: view()) {
  .cat-03a__content {
    animation: cat-03a-exit linear both;
    animation-timeline: --cat18a-hero;
    animation-range: contain 15% contain 70%;
  }

  .cat-03a__bg {
    animation: cat-03a-zoom linear both;
    animation-timeline: --cat18a-hero;
    animation-range: contain 0% contain 100%;
  }
}

@keyframes cat-03a-exit {
  to {
    opacity: 0;
    filter: blur(10px);
    transform: translateY(-46px) scale(.96);
  }
}

@keyframes cat-03a-zoom {
  to {
    transform: scale(1.12);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-03a__content,
    .cat-03a__bg {
    animation: none;
  }
}

.cat-03b,
.cat-03b *,
.cat-03b *::before,
.cat-03b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-03b {
  width: 100%;
  background: linear-gradient(180deg,#0e1018,#141020 50%,#0e1018);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-03b__tall {
  height: 260vh;
  view-timeline-name: --cat18b-story;
}

.cat-03b__pin {
  position: sticky;
  top: 0;
  height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 34px;
  padding: 48px 24px;
}

.cat-03b__count {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .2em;
  color: rgba(190,200,235,.4);
}

.cat-03b__stack {
  position: relative;
  display: grid;
  place-items: center;
  min-height: 2.4em;
  font-size: clamp(34px,6vw,72px);
}

.cat-03b__line {
  position: absolute;
  font-size: inherit;
  font-weight: 700;
  letter-spacing: -.015em;
  color: #eef1fb;
  text-align: center;
  text-wrap: balance;
}

.cat-03b__line:nth-child(2) {
  color: oklch(0.8 0.15 300);
}

.cat-03b__line:nth-child(3) {
  color: oklch(0.85 0.14 165);
}

.cat-03b__line {
  opacity: 0;
}

.cat-03b__line:first-child {
  opacity: 1;
}

@supports (animation-timeline: view()) {
  .cat-03b__line {
    animation: cat-03b-chapter linear both;
    animation-timeline: --cat18b-story;
    animation-range: var(--from) var(--to);
    opacity: 0;
  }
}

@keyframes cat-03b-chapter {
  0% {
    opacity: 0;
    transform: translateY(30px) scale(.97);
    filter: blur(6px);
  }

  22%,
    78% {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
  }

  100% {
    opacity: 0;
    transform: translateY(-30px) scale(.97);
    filter: blur(6px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-03b__line {
    animation: none;
  }

  .cat-03b__line:first-child {
    opacity: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — the 230vh wrapper names a view-timeline; the pinned title scrubs an opacity/blur/lift keyframe across contain 15–70% while the photo slowly zooms. Swap the picsum placeholder for your own imagery. */

/* No JavaScript — three stacked lines share one fade-in/out keyframe but slice different animation-range windows (via inline --from/--to) of the same view-timeline. */
```
