---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/svg-organic-blob-morph/"
title: "SVG Organic Blob Morph"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A playful CTA that starts as a soft organic blob and, on hover, resolves into a clean structured pill — great for creative studios and friendly product pages."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SVG Organic Blob Morph
Source: https://codefronts.com/motion/css-button-hover-effects/svg-organic-blob-morph/

A playful CTA that starts as a soft organic blob and, on hover, resolves into a clean structured pill — great for creative studios and friendly product pages. Pure CSS using an animatable multi-point border-radius.
## HTML
```html
<div class="bhe-04-group">
<section class="bhe-04a" aria-label="Blob morph button">
  <button class="bhe-04a__btn" type="button">Say hello</button>
</section>
<section class="bhe-04b" aria-label="Squircle morph button">
  <button class="bhe-04b__btn" type="button" aria-label="Play"><span aria-hidden="true">▶</span></button>
</section>
</div>
```
## CSS
```css
.bhe-04-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-04-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-04a,
.bhe-04a *,
.bhe-04a *::before,
.bhe-04a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-04a {
  --accent: oklch(0.68 0.17 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: radial-gradient(120% 120% at 30% 0%,#fff3ec,#ffe1d3);
}

.bhe-04a__btn {
  display: grid;
  place-items: center;
  min-width: 180px;
  font-size: 17px;
  font-weight: 800;
  color: #fff;
  padding: 24px 40px;
  border: none;
  cursor: pointer;
  background: linear-gradient(150deg,color-mix(in oklab,var(--accent) 82%,white),var(--accent));
  box-shadow: 0 18px 36px -16px color-mix(in oklab,var(--accent) 70%,transparent);
  border-radius: 42% 58% 63% 37% / 45% 38% 62% 55%;
  animation: bhe-04a-breathe 7s ease-in-out infinite;
  transition: border-radius .6s cubic-bezier(.2,.9,.2,1),transform .3s;
}

.bhe-04a__btn:hover,
.bhe-04a__btn:focus-visible {
  border-radius: 9999px;
  transform: translateY(-3px);
  animation-play-state: paused;
}

.bhe-04a__btn:active {
  transform: translateY(0) scale(.97);
}

.bhe-04a__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

@keyframes bhe-04a-breathe {
  0%,
    100% {
    border-radius: 42% 58% 63% 37% / 45% 38% 62% 55%;
  }

  50% {
    border-radius: 60% 40% 38% 62% / 55% 62% 38% 45%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-04a__btn {
    animation: none;
    transition: transform .2s;
  }
}

.bhe-04b,
.bhe-04b *,
.bhe-04b *::before,
.bhe-04b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-04b {
  --accent: oklch(0.62 0.18 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #141020;
}

.bhe-04b__btn {
  display: grid;
  place-items: center;
  width: 96px;
  height: 96px;
  font-size: 26px;
  color: #fff;
  border: none;
  cursor: pointer;
  background: linear-gradient(150deg,color-mix(in oklab,var(--accent) 80%,white),var(--accent));
  box-shadow: 0 18px 40px -16px var(--accent);
  border-radius: 34% 66% 62% 38% / 40% 42% 58% 60%;
  transition: border-radius .55s cubic-bezier(.2,.9,.2,1),transform .35s;
}

.bhe-04b__btn:hover,
.bhe-04b__btn:focus-visible {
  border-radius: 50%;
  transform: scale(1.08);
}

.bhe-04b__btn:active {
  transform: scale(.96);
}

.bhe-04b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-04b__btn {
    transition: transform .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
