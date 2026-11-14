---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/css-text-fill-liquid-fill-effect/"
title: "CSS Text Fill / Liquid Fill Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "A headline that fills with water on hover — pure CSS, no canvas, no SVG library."
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Fill / Liquid Fill Effect
Source: https://codefronts.com/motion/css-text-hover-effects/css-text-fill-liquid-fill-effect/

A headline that fills with water on hover — pure CSS, no canvas, no SVG library. Two stacked copies of the word: the base is a hollow 1px text-stroke, the overlay is gradient-filled via background-clip:text and revealed bottom-up by a clip-path driven by ONE registered @property, so the browser tweens the water level for you. While hovered, a 3s keyframe rocks the clip's wave crest so the surface never sits still. Below it, the classic nav-pill variant fills its background bottom-to-top with nothing but background-size.
## HTML
```html
<section class="cth-02" aria-label="Liquid text fill on hover demo">
  <div class="cth-02__stage">
    <div class="cth-02__scene">
      <p class="cth-02__eyebrow">Tidewater Swim Co. &mdash; Summer '26</p>
      <a class="cth-02__word" href="#cth02-top" id="cth02-top">
        <span class="cth-02__hollow">TIDEWATER</span>
        <span class="cth-02__liquid" aria-hidden="true">TIDEWATER</span>
      </a>
      <p class="cth-02__sub">Hold the cursor on the wordmark and let it flood. The level is one typed <code>@property</code>; the wave is a 3s keyframe on the clip edge.</p>
      <nav class="cth-02__nav" aria-label="Collection">
        <a href="#cth02-top">Swimwear</a>
        <a href="#cth02-top">Wetsuits</a>
        <a href="#cth02-top">Open water</a>
        <a href="#cth02-top">Journal</a>
      </nav>
      <p class="cth-02__hint">Nav pills fill bottom-up with <code>background-size</code> alone &mdash; the one-element version of the same idea.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --cth02-fill {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

@property --cth02-bob {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

.cth-02,
.cth-02 *,
.cth-02 *::before,
.cth-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-02 {
  --bg: oklch(0.17 0.03 250);
  --ink: oklch(0.95 0.01 230);
  --mut: oklch(0.66 0.03 240);
  --water-hi: oklch(0.85 0.11 220);
  --water-lo: oklch(0.55 0.19 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-02__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(120% 90% at 50% 0%,oklch(0.22 0.045 255),var(--bg) 60%);
  padding: clamp(20px,4vw,56px);
  container: cth02/inline-size;
}

.cth-02__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(18px,3cqi,26px);
  width: min(100%,820px);
}

.cth-02__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-02__word {
  --cth02-fill: 0%;
  position: relative;
  display: inline-block;
  text-decoration: none;
  font-size: clamp(48px,12cqi,124px);
  font-weight: 900;
  letter-spacing: -.03em;
  line-height: 1.04;
  padding: .06em .04em;
  transition: --cth02-fill .9s cubic-bezier(.3,.9,.2,1);
}

.cth-02__word:hover,
.cth-02__word:focus-visible {
  --cth02-fill: 104%;
}

.cth-02__word:focus-visible {
  outline: 2px solid var(--water-hi);
  outline-offset: 8px;
  border-radius: 4px;
}

.cth-02__hollow {
  display: block;
  color: transparent;
  -webkit-text-stroke: 1.5px color-mix(in oklch,var(--ink) 55%,transparent);
}

.cth-02__liquid {
  position: absolute;
  inset: 0;
  padding: .06em .04em;
  display: block;
  background: linear-gradient(180deg,var(--water-hi) 0%,var(--water-hi) 6%,var(--water-lo) 60%,oklch(0.4 0.16 262) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  clip-path: inset(calc(100% - var(--cth02-fill) + var(--cth02-bob)) -6% -6% -6%);
}

.cth-02__word:hover .cth-02__liquid,
.cth-02__word:focus-visible .cth-02__liquid {
  animation: cth02-bob 3s ease-in-out .9s infinite;
}

@keyframes cth02-bob {
  0%,
    100% {
    --cth02-bob: 0%;
  }

  50% {
    --cth02-bob: 1.6%;
  }
}

.cth-02__sub {
  font-size: 14.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 52ch;
}

.cth-02__sub code,
.cth-02__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.26 0.04 250);
  padding: 1px 6px;
  border-radius: 5px;
  color: var(--water-hi);
}

.cth-02__nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-top: 6px;
}

.cth-02__nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 22px;
  border: 1.5px solid color-mix(in oklch,var(--ink) 30%,transparent);
  border-radius: 99px;
  color: var(--ink);
  text-decoration: none;
  font-size: 14px;
  font-weight: 650;
  background-image: linear-gradient(180deg,var(--water-hi),var(--water-lo));
  background-repeat: no-repeat;
  background-position: 0 100%;
  background-size: 100% 0%;
  transition: background-size .45s cubic-bezier(.3,.9,.2,1),color .3s,border-color .3s;
}

.cth-02__nav a:hover,
.cth-02__nav a:focus-visible {
  background-size: 100% 100%;
  color: oklch(0.15 0.03 255);
  border-color: transparent;
}

.cth-02__nav a:focus-visible {
  outline: 2px solid var(--water-hi);
  outline-offset: 3px;
}

.cth-02__hint {
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cth-02 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
