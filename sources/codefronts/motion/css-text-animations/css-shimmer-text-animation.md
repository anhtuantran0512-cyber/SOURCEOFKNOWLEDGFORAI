---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-shimmer-text-animation/"
title: "CSS Metallic Shimmer Text Animation"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Precious-metal typography: engraved gold serif caps with a light streak that passes, pauses, then passes again — like a display case being walked past — and…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Metallic Shimmer Text Animation
Source: https://codefronts.com/motion/css-text-animations/css-shimmer-text-animation/

Precious-metal typography: engraved gold serif caps with a light streak that passes, pauses, then passes again — like a display case being walked past — and a platinum fintech lockup whose sheen answers only to hover, with embossed edge shadows selling the metal.
## HTML
```html
<div class="cat-25-group">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&display=swap" rel="stylesheet">
<section class="cat-25a" aria-label="Gold shimmer text">
  <div class="cat-25a__stage">
    <p class="cat-25a__over" aria-hidden="true">ÉTABLI 1897</p>
    <h1 class="cat-25a__word">HERITAGE</h1>
    <p class="cat-25a__under" aria-hidden="true">— HORLOGERIE FINE —</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-25b" aria-label="Platinum sheen on hover">
  <div class="cat-25b__card">
    <p class="cat-25b__tier">MEMBERS ONLY</p>
    <h1 class="cat-25b__word" tabindex="0">PLATINUM</h1>
    <div class="cat-25b__row" aria-hidden="true"><span>✦</span><span>hover the metal</span><span>✦</span></div>
  </div>
</section>
</div>
```
## CSS
```css
.cat-25-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-25-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-25a,
.cat-25a *,
.cat-25a *::before,
.cat-25a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-25a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 85% at 50% 8%,#17130c,#0c0a06 72%);
}

.cat-25a__stage {
  text-align: center;
  display: grid;
  gap: 20px;
}

.cat-25a__over,
.cat-25a__under {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 10.5px;
  letter-spacing: .5em;
  color: rgba(214,183,110,.55);
}

.cat-25a__word {
  font-family: 'Cormorant Garamond',Georgia,serif;
  font-size: clamp(50px,9.4vw,124px);
  font-weight: 600;
  letter-spacing: .12em;
  margin-right: -.12em;
  line-height: 1.05;
  background: linear-gradient(115deg,transparent 42%,rgba(255,252,240,.9) 50%,transparent 58%) -180% 0/220% 100% no-repeat,linear-gradient(105deg,#8a6a26,#f8e7ae 28%,#a67c28 52%,#e8cf8f 74%,#7a5b1e);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: cat-25a-streak 4.4s ease-in-out 1s infinite;
}

.cat-25a__under {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}

@keyframes cat-25a-streak {
  0% {
    background-position: -180% 0,0 0;
  }

  44%,
    100% {
    background-position: 180% 0,0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-25a__word {
    animation: none;
  }
}

.cat-25b,
.cat-25b *,
.cat-25b *::before,
.cat-25b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-25b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101114;
}

.cat-25b__card {
  text-align: center;
  display: grid;
  gap: 16px;
  padding: 60px clamp(30px,8vw,100px);
  border: 1px solid rgba(220,226,235,.12);
  border-radius: 22px;
  background: linear-gradient(165deg,#16181d,#101114 60%);
  box-shadow: 0 40px 90px -50px rgb(0 0 0/.9),inset 0 1px 0 rgba(255,255,255,.06);
}

.cat-25b__tier {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10px;
  letter-spacing: .44em;
  color: rgba(210,218,230,.45);
}

.cat-25b__word {
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
  font-size: clamp(40px,7.6vw,96px);
  font-weight: 700;
  letter-spacing: .08em;
  margin-right: -.08em;
  background: linear-gradient(115deg,transparent 44%,rgba(255,255,255,.95) 50%,transparent 56%) -180% 0/240% 100% no-repeat,linear-gradient(100deg,#7d838d,#f4f7fb 30%,#9aa1ac 52%,#dfe5ec 72%,#6f7680);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  transition: background-position 1.1s cubic-bezier(.25,.75,.3,1);
  cursor: default;
}

.cat-25b__word:hover,
.cat-25b__word:focus-visible {
  background-position: 180% 0,0 0;
}

.cat-25b__word:focus-visible {
  outline: 2px solid rgba(220,230,245,.5);
  outline-offset: 8px;
}

.cat-25b__row {
  display: flex;
  justify-content: center;
  gap: 12px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10.5px;
  letter-spacing: .2em;
  color: rgba(210,218,230,.4);
}

@media (prefers-reduced-motion: reduce) {
  .cat-25b__word {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the gold body and the light streak are two background layers under one text clip; the keyframe crosses the streak then rests until the next loop. */

/* No JavaScript — same dual-layer clip, but the streak's background-position transitions only on hover/focus; the metal reads via alternating gradient stops. */
```
