---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/before-after-image-comparison-slider/"
title: "Before / After Image Comparison Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Before/after image comparison slider in vanilla CSS — a native range input drives a clip-path reveal with one line of JavaScript, so it stays lightweight and…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Before / After Image Comparison Slider
Source: https://codefronts.com/components/css-image-slider/before-after-image-comparison-slider/

Before/after image comparison slider in vanilla CSS — a native range input drives a clip-path reveal with one line of JavaScript, so it stays lightweight and keyboard-accessible. Copy-paste ready for dental cosmetic before/after pages, plastic surgery portfolios, home renovation showcases, and photo-retouching demos. Alternative to img-comparison-slider (12KB), react-compare-image (28KB), and the classic jQuery TwentyTwenty plugin — zero dependencies, works in every framework.
## HTML
```html
<div class="cis-03" style="--pos:50%">
  <div class="cis-03__frame">
    <img class="cis-03__img" src="https://picsum.photos/seed/cis03a/1100/750?grayscale" alt="Before — ungraded, desaturated">
    <div class="cis-03__after">
      <img class="cis-03__img" src="https://picsum.photos/seed/cis03a/1100/750" alt="After — colour graded">
    </div>
    <span class="cis-03__tag cis-03__tag--b">Before</span>
    <span class="cis-03__tag cis-03__tag--a">After</span>
    <div class="cis-03__divider" aria-hidden="true"><span class="cis-03__handle"></span></div>
    <input class="cis-03__range" type="range" min="0" max="100" value="50"
      aria-label="Reveal after image"
      oninput="this.closest('.cis-03').style.setProperty('--pos', this.value + '%')">
  </div>
</div>
```
## CSS
```css
@property --pos {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 50%;
}

.cis-03,
.cis-03 *,
.cis-03 *::before,
.cis-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-03 ::selection {
  background: #ffd23f;
  color: #1a1400;
}

.cis-03 {
  --line: #ffffff;
  --accent: oklch(0.83 0.17 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 44px 20px;
  background: radial-gradient(120% 120% at 80% 10%,#1a1710,#0a0906);
}

.cis-03__frame {
  position: relative;
  width: min(720px,94vw);
  aspect-ratio: 11/7.5;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid #2a2620;
  box-shadow: 0 40px 90px -44px rgba(0,0,0,.9);
  user-select: none;
}

.cis-03__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-03__after {
  position: absolute;
  inset: 0;
  clip-path: inset(0 0 0 var(--pos));
}

.cis-03__tag {
  position: absolute;
  top: 14px;
  padding: 6px 12px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  border-radius: 999px;
  color: #fff;
  background: color-mix(in oklab,#000 42%,transparent);
  border: 1px solid rgba(255,255,255,.22);
  backdrop-filter: blur(8px);
}

.cis-03__tag--b {
  left: 14px;
}

.cis-03__tag--a {
  right: 14px;
  color: #1a1400;
  background: var(--accent);
  border-color: transparent;
}

.cis-03__divider {
  position: absolute;
  top: 0;
  bottom: 0;
  left: var(--pos);
  width: 2px;
  background: var(--line);
  transform: translateX(-1px);
  box-shadow: 0 0 14px rgba(255,255,255,.5);
}

.cis-03__handle {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 46px;
  height: 46px;
  transform: translate(-50%,-50%);
  border-radius: 50%;
  background: var(--line);
  display: grid;
  place-items: center;
  box-shadow: 0 6px 20px rgba(0,0,0,.45);
}

.cis-03__handle::before,
.cis-03__handle::after {
  content: "";
  position: absolute;
  width: 8px;
  height: 8px;
  border-top: 2.4px solid #1a1400;
  border-right: 2.4px solid #1a1400;
}

.cis-03__handle::before {
  transform: rotate(-135deg);
  margin-left: -9px;
}

.cis-03__handle::after {
  transform: rotate(45deg);
  margin-right: -9px;
}

.cis-03__range {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  cursor: ew-resize;
  opacity: 0;
  appearance: none;
}

.cis-03__range:focus-visible {
  opacity: 1;
  background: transparent;
  outline: none;
}

.cis-03__range:focus-visible ~ .cis-03__divider {
  box-shadow: 0 0 0 3px var(--accent),0 0 14px rgba(255,255,255,.5);
}

.cis-03__range::-webkit-slider-thumb {
  appearance: none;
  width: 46px;
  height: 100%;
}

.cis-03__range::-moz-range-thumb {
  width: 46px;
  height: 100%;
  border: 0;
  background: transparent;
}

@media (prefers-reduced-motion: reduce) {
  .cis-03__divider {
    transition: none;
  }
}
```

## JavaScript
```js
/* The only script is the inline oninput on the range:
   oninput="this.closest('.cis-03').style.setProperty('--pos', this.value + '%')"
   It writes the slider value into the --pos custom property that drives both the
   clip-path and the divider. No listeners, no pointer maths, fully keyboard-driven. */
```
