---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-gradient-text-animation/"
title: "CSS Animated Gradient Text Color Wave"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Two takes on the gradient-clipped headline: an oversized aurora that drifts through the glyphs on background-position, and a hue engine that animates a…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Gradient Text Color Wave
Source: https://codefronts.com/motion/css-text-animations/css-gradient-text-animation/

Two takes on the gradient-clipped headline: an oversized aurora that drifts through the glyphs on background-position, and a hue engine that animates a registered @property angle straight through oklch() for a perfectly even color wave.
## HTML
```html
<div class="cat-09-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-09a" aria-label="Aurora gradient text wave">
  <div class="cat-09a__stage">
    <h1 class="cat-09a__title">AURORA</h1>
    <p class="cat-09a__sub">a 300%-wide gradient drifting behind the glyphs</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-09b" aria-label="oklch hue cycling gradient text">
  <div class="cat-09b__stage">
    <h1 class="cat-09b__title">HUE ENGINE</h1>
    <p class="cat-09b__sub">@property --hue&nbsp;·&nbsp;oklch(0.78 0.17 calc(--hue + offset))</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-09-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-09-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-09a,
.cat-09a *,
.cat-09a *::before,
.cat-09a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-09a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #07090f;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-09a__stage {
  text-align: center;
}

.cat-09a__title {
  font-size: clamp(56px,11vw,150px);
  font-weight: 700;
  letter-spacing: .02em;
  line-height: 1;
  background: linear-gradient(100deg,oklch(0.75 0.18 330),oklch(0.8 0.16 250),oklch(0.87 0.15 180),oklch(0.8 0.18 300),oklch(0.75 0.18 330)) 0 0/300% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: cat-09a-drift 7s linear infinite;
  filter: drop-shadow(0 0 26px rgba(120,140,255,.25));
}

.cat-09a__sub {
  margin-top: 20px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  letter-spacing: .18em;
  color: rgba(170,190,225,.42);
}

@keyframes cat-09a-drift {
  to {
    background-position: 300% 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-09a__title {
    animation: none;
  }
}

@property --cat04b-hue {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: true;
}

.cat-09b,
.cat-09b *,
.cat-09b *::before,
.cat-09b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-09b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0d0b12;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-09b__stage {
  text-align: center;
  --cat04b-hue: 0deg;
  animation: cat-09b-spin 8s linear infinite;
}

.cat-09b__title {
  font-size: clamp(44px,9vw,120px);
  font-weight: 700;
  line-height: 1;
  letter-spacing: -.01em;
  background: linear-gradient(90deg,oklch(0.78 0.17 var(--cat04b-hue)),oklch(0.78 0.17 calc(var(--cat04b-hue) + 70deg)),oklch(0.78 0.17 calc(var(--cat04b-hue) + 140deg)));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.cat-09b__sub {
  margin-top: 20px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  color: rgba(200,195,230,.4);
}

@keyframes cat-09b-spin {
  to {
    --cat04b-hue: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-09b__stage {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a 300%-wide 5-stop gradient (last stop repeats the first) slides via background-position for a seamless aurora. */

/* No JavaScript — @property registers --hue as a real <angle>, so one keyframe (0→360deg) re-resolves every oklch() stop each frame. */
```
