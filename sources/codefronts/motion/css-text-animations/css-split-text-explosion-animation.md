---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-split-text-explosion-animation/"
title: "CSS Text Hover Scatter Gather Letters"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Letters as loose particles: a word that idles as blurred, scattered debris and springs into crisp alignment on hover (with real linear() spring physics), and…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Hover Scatter Gather Letters
Source: https://codefronts.com/motion/css-text-animations/css-split-text-explosion-animation/

Letters as loose particles: a word that idles as blurred, scattered debris and springs into crisp alignment on hover (with real linear() spring physics), and its inverse — a tidy word that detonates apart under the cursor.
## HTML
```html
<div class="cat-19-group">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="cat-19a" aria-label="Scattered letters gather on hover">
  <div class="cat-19a__stage">
    <h1 class="cat-19a__word" aria-label="TOGETHER" tabindex="0">
      <span aria-hidden="true"><i style="--x:-44px;--y:-30px;--r:-22deg">T</i><i style="--x:26px;--y:38px;--r:14deg">O</i><i style="--x:-18px;--y:24px;--r:-9deg">G</i><i style="--x:40px;--y:-26px;--r:24deg">E</i><i style="--x:-32px;--y:-12px;--r:12deg">T</i><i style="--x:22px;--y:30px;--r:-18deg">H</i><i style="--x:-26px;--y:-34px;--r:8deg">E</i><i style="--x:38px;--y:16px;--r:-14deg">R</i></span>
    </h1>
    <p class="cat-19a__sub" aria-hidden="true">hover — every letter springs home from its own offset</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-19b" aria-label="Word explodes into letters on hover">
  <div class="cat-19b__stage">
    <h1 class="cat-19b__word" aria-label="SCATTER" tabindex="0">
      <span aria-hidden="true"><i style="--x:-60px;--y:-44px;--r:-38deg;--i:0">S</i><i style="--x:44px;--y:-58px;--r:26deg;--i:1">C</i><i style="--x:-38px;--y:50px;--r:-20deg;--i:2">A</i><i style="--x:60px;--y:34px;--r:34deg;--i:3">T</i><i style="--x:-52px;--y:-20px;--r:16deg;--i:4">T</i><i style="--x:36px;--y:56px;--r:-30deg;--i:5">E</i><i style="--x:-24px;--y:-60px;--r:22deg;--i:6">R</i></span>
    </h1>
    <p class="cat-19b__sub" aria-hidden="true">hover to detonate — release to reassemble</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-19-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-19-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-19a,
.cat-19a *,
.cat-19a *::before,
.cat-19a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-19a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f3efe6;
  font-family: 'Playfair Display',Georgia,serif;
}

.cat-19a__stage {
  text-align: center;
}

.cat-19a__word {
  display: inline-block;
  padding: 50px clamp(24px,5vw,70px);
  font-size: clamp(40px,7.6vw,96px);
  font-weight: 700;
  letter-spacing: .05em;
  color: #241f18;
  cursor: pointer;
}

.cat-19a__word i {
  display: inline-block;
  font-style: normal;
  opacity: .38;
  filter: blur(2.5px);
  transform: translate(var(--x),var(--y)) rotate(var(--r));
  transition: transform .75s,filter .55s,opacity .55s;
  transition-timing-function: cubic-bezier(.34,1.45,.5,1);
  transition-timing-function: linear(0,0.008 6.3%,0.235 20.4%,0.685 39.8%,1.02 58%,1.11 66.7%,1.03 82%,0.99 92%,1);
}

.cat-19a__word:hover i,
.cat-19a__word:focus-visible i {
  opacity: 1;
  filter: blur(0);
  transform: translate(0,0) rotate(0);
}

.cat-19a__word:focus-visible {
  outline: 2px dashed rgba(36,31,24,.5);
  outline-offset: 8px;
}

.cat-19a__sub {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .15em;
  color: rgba(36,31,24,.42);
}

@media (prefers-reduced-motion: reduce) {
  .cat-19a__word i {
    opacity: 1;
    filter: none;
    transform: none;
    transition: none;
  }
}

.cat-19b,
.cat-19b *,
.cat-19b *::before,
.cat-19b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-19b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0e1015;
}

.cat-19b__stage {
  text-align: center;
}

.cat-19b__word {
  display: inline-block;
  padding: 60px clamp(24px,5vw,80px);
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
  font-size: clamp(40px,7.6vw,96px);
  font-weight: 900;
  letter-spacing: .03em;
  cursor: crosshair;
}

.cat-19b__word i {
  display: inline-block;
  font-style: normal;
  color: oklch(0.82 0.17 calc(var(--i)*52));
  transition: transform .55s cubic-bezier(.2,.8,.25,1.15),filter .55s;
  transition-delay: calc(var(--i)*28ms);
}

.cat-19b__word:hover i,
.cat-19b__word:focus-visible i {
  transform: translate(var(--x),var(--y)) rotate(var(--r));
  filter: blur(.8px);
}

.cat-19b__word:focus-visible {
  outline: 2px dashed rgba(240,244,255,.4);
  outline-offset: 8px;
}

.cat-19b__sub {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .15em;
  color: rgba(190,205,235,.4);
}

@media (prefers-reduced-motion: reduce) {
  .cat-19b__word i {
    transition: none;
  }

  .cat-19b__word:hover i,
    .cat-19b__word:focus-visible i {
    transform: none;
    filter: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — inline --x/--y/--r map each letter's scatter pose; hovering the word transitions all of them to identity with a linear() spring. */

/* No JavaScript — the inverse gather: identity at rest, inline scatter poses on hover, with --i transition-delays rippling the blast outward. */
```
