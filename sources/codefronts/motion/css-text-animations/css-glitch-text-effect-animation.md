---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-glitch-text-effect-animation/"
title: "CSS Text Hover Glitch Effect Keyframes"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Broadcast-corruption typography for gaming and cyber brands: a data-text double-layer glitch with clip-path slice storms and RGB fringes, and a scanline tear…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Hover Glitch Effect Keyframes
Source: https://codefronts.com/motion/css-text-animations/css-glitch-text-effect-animation/

Broadcast-corruption typography for gaming and cyber brands: a data-text double-layer glitch with clip-path slice storms and RGB fringes, and a scanline tear where a sweep bar drags the word into stepped chromatic shivers.
## HTML
```html
<div class="cat-15-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-15a" aria-label="Glitch slice text hover">
  <div class="cat-15a__stage">
    <h1 class="cat-15a__word" data-text="OVERDRIVE" tabindex="0">OVERDRIVE</h1>
    <p class="cat-15a__sub" aria-hidden="true">hover / focus to corrupt the signal</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="cat-15b" aria-label="Scanline glitch text hover">
  <div class="cat-15b__stage">
    <h1 class="cat-15b__word" tabindex="0">LEVEL&nbsp;UP<span class="cat-15b__scan" aria-hidden="true"></span></h1>
    <p class="cat-15b__sub" aria-hidden="true">a sweep bar drags stepped chromatic shivers</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-15-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-15-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-15a,
.cat-15a *,
.cat-15a *::before,
.cat-15a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-15a {
  --cyan: #22e3ff;
  --mag: #ff2bd6;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #07060f;
  background-image: repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 1px,transparent 1px 3px);
}

.cat-15a__stage {
  text-align: center;
}

.cat-15a__word {
  position: relative;
  display: inline-block;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
  font-size: clamp(40px,8.4vw,104px);
  font-weight: 900;
  letter-spacing: .01em;
  color: #f2f6ff;
  cursor: crosshair;
}

.cat-15a__word::before,
.cat-15a__word::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  opacity: 0;
  pointer-events: none;
}

.cat-15a__word::before {
  text-shadow: -2.5px 0 var(--cyan);
  clip-path: inset(0 0 55% 0);
}

.cat-15a__word::after {
  text-shadow: 2.5px 0 var(--mag);
  clip-path: inset(55% 0 0 0);
}

.cat-15a__word:hover::before,
.cat-15a__word:focus-visible::before {
  opacity: .95;
  animation: cat-15a-s1 .55s steps(5) infinite;
}

.cat-15a__word:hover::after,
.cat-15a__word:focus-visible::after {
  opacity: .95;
  animation: cat-15a-s2 .45s steps(4) infinite;
}

.cat-15a__word:focus-visible {
  outline: 2px solid var(--cyan);
  outline-offset: 8px;
}

.cat-15a__sub {
  margin-top: 22px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .2em;
  color: rgba(170,190,230,.4);
}

@keyframes cat-15a-s1 {
  0% {
    clip-path: inset(0 0 62% 0);
    transform: translate(-3px,0);
  }

  33% {
    clip-path: inset(38% 0 28% 0);
    transform: translate(2px,-2px);
  }

  66% {
    clip-path: inset(72% 0 4% 0);
    transform: translate(-2px,1px);
  }

  100% {
    clip-path: inset(10% 0 74% 0);
    transform: translate(3px,0);
  }
}

@keyframes cat-15a-s2 {
  0% {
    clip-path: inset(64% 0 6% 0);
    transform: translate(3px,0);
  }

  33% {
    clip-path: inset(6% 0 70% 0);
    transform: translate(-2px,2px);
  }

  66% {
    clip-path: inset(42% 0 34% 0);
    transform: translate(2px,-1px);
  }

  100% {
    clip-path: inset(78% 0 2% 0);
    transform: translate(-3px,0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-15a__word:hover::before,
    .cat-15a__word:hover::after,
    .cat-15a__word:focus-visible::before,
    .cat-15a__word:focus-visible::after {
    animation: none;
    opacity: .5;
    clip-path: none;
    transform: none;
  }
}

.cat-15b,
.cat-15b *,
.cat-15b *::before,
.cat-15b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-15b {
  --lime: oklch(0.9 0.23 135);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0a0f0a;
}

.cat-15b__stage {
  text-align: center;
}

.cat-15b__word {
  position: relative;
  display: inline-block;
  overflow: hidden;
  font-family: 'JetBrains Mono',ui-monospace,Menlo,monospace;
  font-size: clamp(38px,7.6vw,92px);
  font-weight: 800;
  letter-spacing: .04em;
  color: var(--lime);
  padding: .1em .2em;
  cursor: crosshair;
}

.cat-15b__scan {
  position: absolute;
  left: 0;
  right: 0;
  top: -30%;
  height: 22%;
  background: linear-gradient(180deg,transparent,rgba(190,255,160,.28),transparent);
  opacity: 0;
  pointer-events: none;
}

.cat-15b__word:hover,
.cat-15b__word:focus-visible {
  animation: cat-15b-shiver .4s steps(2) infinite;
}

.cat-15b__word:hover .cat-15b__scan,
.cat-15b__word:focus-visible .cat-15b__scan {
  opacity: 1;
  animation: cat-15b-sweep .7s linear infinite;
}

.cat-15b__word:focus-visible {
  outline: 2px solid var(--lime);
  outline-offset: 6px;
}

.cat-15b__sub {
  margin-top: 20px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(170,220,170,.4);
}

@keyframes cat-15b-sweep {
  to {
    top: 110%;
  }
}

@keyframes cat-15b-shiver {
  0% {
    transform: translateX(0);
    text-shadow: 2px 0 rgba(255,60,120,.6),-2px 0 rgba(60,200,255,.6);
  }

  50% {
    transform: translateX(2px);
    text-shadow: -2px 0 rgba(255,60,120,.6),2px 0 rgba(60,200,255,.6);
  }

  100% {
    transform: translateX(-2px);
    text-shadow: 2px 0 rgba(255,60,120,.6),-2px 0 rgba(60,200,255,.6);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-15b__word:hover,
    .cat-15b__word:focus-visible {
    animation: none;
    text-shadow: 2px 0 rgba(255,60,120,.4),-2px 0 rgba(60,200,255,.4);
  }

  .cat-15b__word:hover .cat-15b__scan,
    .cat-15b__word:focus-visible .cat-15b__scan {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — two attr(data-text) pseudo clones carry cyan/magenta shadows; steps() keyframes snap different clip-path:inset() bands per frame while the base text holds still. */

/* No JavaScript — a gradient scan bar sweeps top-to-bottom while the word micro-translates on steps(2) with alternating RGB text-shadows. */
```
