---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-text-reveal-clip-animation/"
title: "CSS Text Reveal Animation on Page Load"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Two load-time entrances for landing-page titles: an editorial word-by-word rise out of masked line boxes, and a cinematic blur-to-focus settle where the…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Reveal Animation on Page Load
Source: https://codefronts.com/motion/css-text-animations/css-text-reveal-clip-animation/

Two load-time entrances for landing-page titles: an editorial word-by-word rise out of masked line boxes, and a cinematic blur-to-focus settle where the headline sharpens as its letter-spacing tightens.
## HTML
```html
<div class="cat-07-group">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="cat-07a" aria-label="Word by word rise reveal">
  <div class="cat-07a__stage">
    <p class="cat-07a__kicker" style="--i:0"><i>Est. 2027 — Issue 04</i></p>
    <h1 class="cat-07a__title" aria-label="Make something people remember">
      <span aria-hidden="true"><span class="cat-07a__w" style="--i:1"><i>Make</i></span> <span class="cat-07a__w" style="--i:2"><i>something</i></span> <span class="cat-07a__w" style="--i:3"><i>people</i></span> <span class="cat-07a__w cat-07a__w--em" style="--i:4"><i>remember</i></span></span>
    </h1>
    <p class="cat-07a__rule" style="--i:5" aria-hidden="true"></p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-07b" aria-label="Blur to focus text reveal">
  <div class="cat-07b__stage">
    <h1 class="cat-07b__title">Crystal clear by design</h1>
    <p class="cat-07b__sub">blur 14px → 0 · tracking 0.4em → normal · one keyframe</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-07-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-07-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-07a,
.cat-07a *,
.cat-07a *::before,
.cat-07a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-07a {
  --ink: #221d18;
  --accent: oklch(0.58 0.15 40);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f6f1e7;
  font-family: 'Playfair Display',Georgia,serif;
}

.cat-07a__stage {
  text-align: center;
  max-width: 900px;
}

.cat-07a__kicker {
  overflow: hidden;
  margin-bottom: 26px;
}

.cat-07a__kicker i {
  display: inline-block;
  font-style: normal;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: rgba(34,29,24,.5);
  transform: translateY(120%);
  animation: cat-07a-up .8s cubic-bezier(.2,.7,.2,1) calc(var(--i)*90ms + .2s) both;
}

.cat-07a__title {
  font-size: clamp(38px,6.4vw,84px);
  font-weight: 600;
  line-height: 1.08;
  color: var(--ink);
  letter-spacing: -.015em;
  text-wrap: balance;
}

.cat-07a__w {
  display: inline-block;
  overflow: hidden;
  vertical-align: bottom;
  padding-bottom: .08em;
  margin-bottom: -.08em;
}

.cat-07a__w i {
  display: inline-block;
  font-style: normal;
  transform: translateY(120%);
  animation: cat-07a-up .9s cubic-bezier(.2,.7,.2,1) calc(var(--i)*90ms + .2s) both;
}

.cat-07a__w--em i {
  font-style: italic;
  color: var(--accent);
}

.cat-07a__rule {
  width: 64px;
  height: 2px;
  background: var(--ink);
  margin: 30px auto 0;
  transform: scaleX(0);
  animation: cat-07a-rule .7s cubic-bezier(.2,.7,.2,1) calc(var(--i)*90ms + .3s) both;
}

@keyframes cat-07a-up {
  to {
    transform: translateY(0);
  }
}

@keyframes cat-07a-rule {
  to {
    transform: scaleX(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-07a__kicker i,
    .cat-07a__w i,
    .cat-07a__rule {
    animation: none;
    transform: none;
  }
}

.cat-07b,
.cat-07b *,
.cat-07b *::before,
.cat-07b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-07b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(90% 80% at 50% 20%,#182030,#0a0d14 70%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-07b__stage {
  text-align: center;
}

.cat-07b__title {
  font-size: clamp(32px,5.6vw,68px);
  font-weight: 500;
  color: #eef3fc;
  letter-spacing: -.02em;
  filter: blur(0);
  animation: cat-07b-focus 1.4s cubic-bezier(.16,.84,.3,1) .3s both;
}

.cat-07b__sub {
  margin-top: 20px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  color: rgba(170,190,225,.42);
  opacity: 0;
  animation: cat-07b-fade .9s ease 1.5s forwards;
}

@keyframes cat-07b-focus {
  from {
    opacity: 0;
    letter-spacing: .4em;
    filter: blur(14px);
    transform: scale(1.04);
  }
}

@keyframes cat-07b-fade {
  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-07b__title {
    animation: cat-07b-fadeonly .4s ease both;
  }

  .cat-07b__sub {
    animation-delay: .4s;
  }
}

@keyframes cat-07b-fadeonly {
  from {
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — each word rises out of its own overflow:hidden shell, staggered by an inline --i index feeding animation-delay. */

/* No JavaScript — opacity, blur(), scale and letter-spacing tween together in one keyframe, reading as a camera pulling focus. */
```
