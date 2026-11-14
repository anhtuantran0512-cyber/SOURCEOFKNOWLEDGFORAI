---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-elastic-bounce-text-animation/"
title: "CSS Rotating Text Wheel Vertical Loop"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "The rotating value-prop, both flavors: a masked vertical wheel that steps through four words with hold-and-snap pacing (fifth item duplicates the first for a…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Rotating Text Wheel Vertical Loop
Source: https://codefronts.com/motion/css-text-animations/css-elastic-bounce-text-animation/

The rotating value-prop, both flavors: a masked vertical wheel that steps through four words with hold-and-snap pacing (fifth item duplicates the first for a seamless wrap), and a true 3D drum where words turn on a cylinder under perspective.
## HTML
```html
<div class="cat-30-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-30a" aria-label="Rotating word wheel headline">
  <div class="cat-30a__stage">
    <h1 class="cat-30a__line" aria-label="We build websites, apps, brands, futures">We build
      <span class="cat-30a__win" aria-hidden="true"><span class="cat-30a__col"><em>websites</em><em>apps</em><em>brands</em><em>futures</em><em>websites</em></span></span>
    </h1>
    <p class="cat-30a__sub" aria-hidden="true">hold 70% · snap 30% · fifth row duplicates the first</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-30b" aria-label="3D drum of rotating words">
  <div class="cat-30b__stage">
    <h1 class="cat-30b__line" aria-label="Design, develop, deploy, delight">
      <span class="cat-30b__scene" aria-hidden="true"><span class="cat-30b__drum"><span class="cat-30b__face" style="--n:0">DESIGN</span><span class="cat-30b__face" style="--n:1">DEVELOP</span><span class="cat-30b__face" style="--n:2">DEPLOY</span><span class="cat-30b__face" style="--n:3">DELIGHT</span></span></span>
    </h1>
    <p class="cat-30b__sub" aria-hidden="true">four faces · rotateX(n·90°) translateZ(.68em) · perspective 900px</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-30-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-30-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-30a,
.cat-30a *,
.cat-30a *::before,
.cat-30a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-30a {
  --accent: oklch(0.8 0.16 165);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0e1116;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-30a__stage {
  text-align: center;
}

.cat-30a__line {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: baseline;
  gap: .34em;
  font-size: clamp(32px,5.8vw,68px);
  font-weight: 600;
  color: #edf2fa;
  letter-spacing: -.015em;
}

.cat-30a__win {
  display: inline-block;
  height: 1.2em;
  line-height: 1.2;
  overflow: hidden;
  vertical-align: baseline;
  -webkit-mask-image: linear-gradient(180deg,transparent 0,#000 18%,#000 82%,transparent 100%);
  mask-image: linear-gradient(180deg,transparent 0,#000 18%,#000 82%,transparent 100%);
}

.cat-30a__col {
  display: flex;
  flex-direction: column;
  animation: cat-30a-wheel 8s cubic-bezier(.6,-0.2,.35,1.2) infinite;
}

.cat-30a__col em {
  font-style: normal;
  font-weight: 700;
  height: 1.2em;
  color: var(--accent);
  border-bottom: 3px solid color-mix(in oklab,var(--accent) 45%,transparent);
  text-align: left;
}

.cat-30a__sub {
  margin-top: 22px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(180,200,230,.4);
}

@keyframes cat-30a-wheel {
  0%,
    17% {
    transform: translateY(0);
  }

  25%,
    42% {
    transform: translateY(-1.2em);
  }

  50%,
    67% {
    transform: translateY(-2.4em);
  }

  75%,
    92% {
    transform: translateY(-3.6em);
  }

  100% {
    transform: translateY(-4.8em);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-30a__col {
    animation: none;
  }
}

.cat-30b,
.cat-30b *,
.cat-30b *::before,
.cat-30b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-30b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(165deg,#151018,#0c0a10);
}

.cat-30b__stage {
  text-align: center;
}

.cat-30b__line {
  display: grid;
  justify-items: center;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.cat-30b__scene {
  display: inline-block;
  perspective: 900px;
  height: 1.35em;
  font-size: clamp(44px,8.4vw,104px);
  line-height: 1.35;
  font-weight: 900;
  letter-spacing: .02em;
}

.cat-30b__drum {
  position: relative;
  display: inline-block;
  min-width: 6.2ch;
  height: 100%;
  transform-style: preserve-3d;
  animation: cat-30b-roll 9s cubic-bezier(.65,-0.25,.3,1.25) infinite;
}

.cat-30b__face {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  backface-visibility: hidden;
  transform: rotateX(calc(var(--n)*90deg)) translateZ(.68em);
  background: linear-gradient(180deg,oklch(0.85 0.17 330),oklch(0.7 0.2 290));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.cat-30b__sub {
  margin-top: 24px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .15em;
  color: rgba(215,195,235,.4);
}

@keyframes cat-30b-roll {
  0%,
    17% {
    transform: rotateX(0);
  }

  25%,
    42% {
    transform: rotateX(-90deg);
  }

  50%,
    67% {
    transform: rotateX(-180deg);
  }

  75%,
    92% {
    transform: rotateX(-270deg);
  }

  100% {
    transform: rotateX(-360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-30b__drum {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a 1.2em masked window over a five-row column (last row = first row); the keyframe holds each word ~70% of its segment then snaps exactly one line-height. */

/* No JavaScript — a preserve-3d drum with four gradient-clipped faces at rotateX(n·90deg) translateZ(.68em) rolls one face per hold-and-snap segment. */
```
