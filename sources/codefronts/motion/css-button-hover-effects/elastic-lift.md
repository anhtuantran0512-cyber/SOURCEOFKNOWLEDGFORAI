---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/elastic-lift/"
title: "Elastic Lift"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A bouncy delightful CTA that springs up on hover — it lifts, squashes slightly and overshoots before settling, using a springy easing curve."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Elastic Lift
Source: https://codefronts.com/motion/css-button-hover-effects/elastic-lift/

A bouncy delightful CTA that springs up on hover — it lifts, squashes slightly and overshoots before settling, using a springy easing curve.
## HTML
```html
<div class="bhe-21-group">
<section class="bhe-21a" aria-label="Elastic lift button">
  <button class="bhe-21a__btn" type="button">Join the fun</button>
</section>
<section class="bhe-21b" aria-label="Wobble tilt button">
  <button class="bhe-21b__btn" type="button">Say cheese</button>
</section>
</div>
```
## CSS
```css
.bhe-21-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-21-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-21a,
.bhe-21a *,
.bhe-21a *::before,
.bhe-21a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-21a {
  --accent: oklch(0.68 0.19 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #fff5ec;
}

.bhe-21a__btn {
  font-size: 17px;
  font-weight: 800;
  color: #fff;
  padding: 18px 42px;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  background: var(--accent);
  box-shadow: 0 8px 16px -8px color-mix(in oklab,var(--accent) 70%,transparent);
  transform: translateY(0) scale(1);
  transition: transform .45s cubic-bezier(.68,-.6,.32,1.6),box-shadow .45s cubic-bezier(.68,-.6,.32,1.6);
}

.bhe-21a__btn:hover,
.bhe-21a__btn:focus-visible {
  transform: translateY(-6px) scale(1.04,.96);
  box-shadow: 0 22px 30px -12px color-mix(in oklab,var(--accent) 65%,transparent);
}

.bhe-21a__btn:active {
  transform: translateY(-1px) scale(.97);
  transition-duration: .12s;
}

.bhe-21a__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .bhe-21a__btn {
    transition: box-shadow .2s;
  }

  .bhe-21a__btn:hover,
    .bhe-21a__btn:focus-visible {
    transform: translateY(-3px);
  }
}

.bhe-21b,
.bhe-21b *,
.bhe-21b *::before,
.bhe-21b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-21b {
  --accent: oklch(0.66 0.18 320);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #fbeffa;
}

.bhe-21b__btn {
  font-size: 17px;
  font-weight: 800;
  color: #fff;
  padding: 18px 42px;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  background: var(--accent);
  box-shadow: 0 10px 20px -10px var(--accent);
  transition: transform .2s;
}

.bhe-21b__btn:hover,
.bhe-21b__btn:focus-visible {
  animation: bhe-21b-wob .5s cubic-bezier(.36,.07,.19,.97);
}

.bhe-21b__btn:active {
  transform: scale(.96);
}

.bhe-21b__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

@keyframes bhe-21b-wob {
  0% {
    transform: rotate(0) scale(1);
  }

  25% {
    transform: rotate(-4deg) scale(1.05);
  }

  50% {
    transform: rotate(3deg) scale(1.03);
  }

  75% {
    transform: rotate(-2deg) scale(1.02);
  }

  100% {
    transform: rotate(0) scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-21b__btn:hover,
    .bhe-21b__btn:focus-visible {
    animation: none;
    transform: scale(1.03);
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
