---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/fire-heat-wave-glow-text/"
title: "Fire / Heat Wave Glow Text"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Type that catches fire the physically-plausible way: flames only burn UP, so the shadow stack builds vertically — white-yellow heat tight under the glyphs,…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fire / Heat Wave Glow Text
Source: https://codefronts.com/motion/css-text-hover-effects/fire-heat-wave-glow-text/

Type that catches fire the physically-plausible way: flames only burn UP, so the shadow stack builds vertically — white-yellow heat tight under the glyphs, orange above, red higher, smoke-dark at the top — and a three-frame flicker keyframe jitters those offsets so the fire licks instead of glows. A 0.5deg skew wobble on a fast alternate loop adds the heat-haze shimmer. At rest the wordmark idles as cooling embers (faint amber pulse); hover is ignition. All text-shadow + transform: no images, no canvas, one element.
## HTML
```html
<section class="cth-24" aria-label="Fire heat wave text demo">
  <div class="cth-24__stage">
    <div class="cth-24__scene">
      <p class="cth-24__eyebrow">Small-batch hot sauce &middot; Carolina Reaper edition</p>
      <a class="cth-24__blaze" href="#cth24-top" id="cth24-top">SCORCH</a>
      <p class="cth-24__sub">Bottled at 1.2 million Scoville. Hover the name; decide if you're serious.</p>
      <div class="cth-24__row">
        <a class="cth-24__btn" href="#cth24-top">Dare the sauce</a>
        <span class="cth-24__note">ships with a waiver, mostly as a joke</span>
      </div>
      <p class="cth-24__hint">Five <code>text-shadow</code> layers stacked upward &mdash; yellow to smoke &mdash; jittered by <code>steps(3)</code>; a &plusmn;.5deg skew loop is the heat haze.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-24,
.cth-24 *,
.cth-24 *::before,
.cth-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-24 {
  --bg: oklch(0.14 0.01 30);
  --ink: oklch(0.9 0.04 75);
  --mut: oklch(0.58 0.03 45);
  --hot: oklch(0.78 0.17 55);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-24__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(90% 60% at 50% 100%,oklch(0.24 0.06 35/.8),transparent 60%),radial-gradient(90% 70% at 50% 20%,oklch(0.17 0.012 30),var(--bg) 75%);
  padding: clamp(20px,4vw,56px);
  container: cth24/inline-size;
}

.cth-24__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(16px,3cqi,26px);
}

.cth-24__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-24__blaze {
  display: inline-block;
  text-decoration: none;
  font-size: clamp(60px,14cqi,150px);
  font-weight: 900;
  letter-spacing: .01em;
  line-height: 1;
  padding: .35em .2em .12em;
  color: oklch(0.82 0.12 65);
  text-shadow: 0 -.04em .06em oklch(0.7 0.14 55/.35),0 -.12em .16em oklch(0.55 0.15 35/.25),0 -.2em .25em oklch(0.4 0.12 28/.2),0 -.3em .3em transparent,0 -.4em .35em transparent;
  animation: cth24-ember 2.8s ease-in-out infinite;
}

@keyframes cth24-ember {
  0%,
    100% {
    text-shadow: 0 -.04em .06em oklch(0.7 0.14 55/.35),0 -.12em .16em oklch(0.55 0.15 35/.25),0 -.2em .25em oklch(0.4 0.12 28/.2),0 -.3em .3em transparent,0 -.4em .35em transparent;
  }

  50% {
    text-shadow: 0 -.05em .07em oklch(0.7 0.14 55/.5),0 -.14em .18em oklch(0.55 0.15 35/.35),0 -.22em .27em oklch(0.4 0.12 28/.28),0 -.32em .32em transparent,0 -.42em .37em transparent;
  }
}

.cth-24__blaze:hover,
.cth-24__blaze:focus-visible {
  color: oklch(0.95 0.08 95);
  animation: cth24-flick .55s steps(3,jump-none) infinite,cth24-haze .18s ease-in-out infinite alternate;
}

.cth-24__blaze:focus-visible {
  outline: 2px solid var(--hot);
  outline-offset: 8px;
  border-radius: 8px;
}

@keyframes cth24-flick {
  0%,
    100% {
    text-shadow: 0 -.04em .02em oklch(0.93 0.15 95),0 -.13em .06em oklch(0.78 0.17 55),0 -.26em .12em oklch(0.62 0.21 32),0 -.42em .2em oklch(0.45 0.16 25),.02em -.6em .3em oklch(0.3 0.05 25/.8);
  }

  38% {
    text-shadow: 0 -.05em .02em oklch(0.93 0.15 95),.01em -.16em .07em oklch(0.78 0.17 55),-.02em -.3em .13em oklch(0.62 0.21 32),.02em -.48em .22em oklch(0.45 0.16 25),-.03em -.66em .32em oklch(0.3 0.05 25/.8);
  }

  72% {
    text-shadow: 0 -.035em .02em oklch(0.93 0.15 95),-.015em -.11em .05em oklch(0.78 0.17 55),.02em -.22em .11em oklch(0.62 0.21 32),-.02em -.38em .19em oklch(0.45 0.16 25),.03em -.55em .28em oklch(0.3 0.05 25/.8);
  }
}

@keyframes cth24-haze {
  from {
    transform: skewX(-.5deg);
  }

  to {
    transform: skewX(.5deg);
  }
}

.cth-24__sub {
  font-size: 14.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 44ch;
}

.cth-24__row {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  margin-top: 4px;
}

.cth-24__btn {
  display: grid;
  place-items: center;
  min-height: 54px;
  padding: 0 30px;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 850;
  text-decoration: none;
  color: oklch(0.98 0.01 85);
  background: linear-gradient(180deg,oklch(0.62 0.21 40),oklch(0.5 0.19 30));
  box-shadow: 0 0 0 transparent,0 0 0 transparent;
  transition: box-shadow .4s ease,translate .3s ease;
}

.cth-24__btn:hover,
.cth-24__btn:focus-visible {
  translate: 0 -2px;
  box-shadow: 0 -6px 22px oklch(0.62 0.21 40/.5),0 8px 26px oklch(0.4 0.15 30/.55);
}

.cth-24__btn:focus-visible {
  outline: 2px solid oklch(0.93 0.15 95);
  outline-offset: 3px;
}

.cth-24__note {
  font-size: 11.5px;
  color: var(--mut);
  font-style: italic;
}

.cth-24__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 54ch;
}

.cth-24__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.22 0.015 35);
  padding: 1px 6px;
  border-radius: 4px;
  color: var(--hot);
}

@media (prefers-reduced-motion: reduce) {
  .cth-24 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }

  .cth-24__blaze:hover,
    .cth-24__blaze:focus-visible {
    text-shadow: 0 -.06em .1em oklch(0.85 0.15 75/.7),0 -.16em .22em oklch(0.65 0.18 45/.5),0 -.28em .3em oklch(0.5 0.15 30/.35),0 -.4em .34em transparent,0 -.5em .38em transparent;
  }
}
```
