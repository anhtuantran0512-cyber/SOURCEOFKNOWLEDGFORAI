---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-mask-wipe-text-reveal-animation/"
title: "CSS Text Fill on Hover Left to Right"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Hollow display type that floods with ink on hover: a two-layer clip-path sweep where a gradient clone wipes across outlined caps, and the single-element…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Fill on Hover Left to Right
Source: https://codefronts.com/motion/css-text-animations/css-mask-wipe-text-reveal-animation/

Hollow display type that floods with ink on hover: a two-layer clip-path sweep where a gradient clone wipes across outlined caps, and the single-element trick — one background-size declaration filling stroked text with zero extra markup.
## HTML
```html
<div class="cat-17-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-17a" aria-label="Outlined text fill sweep on hover">
  <div class="cat-17a__stage">
    <h1 class="cat-17a__word" tabindex="0">PORTFOLIO<span class="cat-17a__fill" aria-hidden="true">PORTFOLIO</span></h1>
    <p class="cat-17a__sub" aria-hidden="true">hover — a filled clone un-clips left → right</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-17b" aria-label="Single element text fill on hover">
  <nav class="cat-17b__list" aria-label="Index">
    <a class="cat-17b__item" href="#">Work</a>
    <a class="cat-17b__item" href="#">About</a>
    <a class="cat-17b__item" href="#">Contact</a>
  </nav>
  <p class="cat-17b__sub" aria-hidden="true">one element · background-size 0% → 100% clipped to text</p>
</section>
</div>
```
## CSS
```css
.cat-17-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-17-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-17a,
.cat-17a *,
.cat-17a *::before,
.cat-17a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-17a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101318;
}

.cat-17a__stage {
  text-align: center;
}

.cat-17a__word {
  position: relative;
  display: inline-block;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
  font-size: clamp(38px,7.8vw,100px);
  font-weight: 900;
  letter-spacing: .01em;
  color: transparent;
  -webkit-text-stroke: 1.5px rgba(235,242,255,.85);
  cursor: pointer;
}

.cat-17a__fill {
  position: absolute;
  inset: 0;
  color: transparent;
  -webkit-text-stroke: 0;
  background: linear-gradient(92deg,oklch(0.8 0.17 200),oklch(0.75 0.19 300));
  -webkit-background-clip: text;
  background-clip: text;
  clip-path: inset(-5% 100% -5% 0);
  transition: clip-path .55s cubic-bezier(.2,.8,.2,1);
  pointer-events: none;
}

.cat-17a__word:hover .cat-17a__fill,
.cat-17a__word:focus-visible .cat-17a__fill {
  clip-path: inset(-5% 0% -5% 0);
}

.cat-17a__word:focus-visible {
  outline: 2px solid oklch(0.8 0.17 200);
  outline-offset: 10px;
}

.cat-17a__sub {
  margin-top: 22px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(170,190,225,.4);
}

@media (prefers-reduced-motion: reduce) {
  .cat-17a__fill {
    transition: clip-path .1s;
  }
}

.cat-17b,
.cat-17b *,
.cat-17b *::before,
.cat-17b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-17b {
  --fill: oklch(0.87 0.17 95);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 30px;
  padding: 48px 24px;
  background: #15130e;
}

.cat-17b__list {
  display: grid;
  gap: 4px;
  text-align: center;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-17b__item {
  display: block;
  font-size: clamp(44px,8vw,92px);
  font-weight: 700;
  line-height: 1.14;
  letter-spacing: -.01em;
  text-decoration: none;
  color: transparent;
  -webkit-text-stroke: 1.25px rgba(240,232,210,.55);
  background: linear-gradient(90deg,var(--fill),var(--fill)) no-repeat 0 0/0% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  transition: background-size .5s cubic-bezier(.2,.8,.2,1);
}

.cat-17b__item:hover,
.cat-17b__item:focus-visible {
  background-size: 100% 100%;
}

.cat-17b__item:focus-visible {
  outline: 2px solid var(--fill);
  outline-offset: 6px;
}

.cat-17b__sub {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(240,232,210,.35);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .cat-17b__item {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a gradient-filled aria-hidden clone sits over stroked transparent text; hover transitions its clip-path window from inset(0 100% 0 0) to fully open. */

/* No JavaScript — stroked transparent text carries its own gradient background clipped to the glyphs; hover tweens background-size 0%→100% so the ink pours through. */
```
