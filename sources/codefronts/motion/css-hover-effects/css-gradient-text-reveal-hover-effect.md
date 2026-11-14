---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-gradient-text-reveal-hover-effect/"
title: "CSS Gradient Text Reveal Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Six gradient text hover techniques — background-clip reveal, linear wipe, conic sweep, radial burst, rainbow shift, and masked shimmer — each using CSS…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Text Reveal Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-gradient-text-reveal-hover-effect/

Six gradient text hover techniques — background-clip reveal, linear wipe, conic sweep, radial burst, rainbow shift, and masked shimmer — each using CSS background-clip: text to paint a gradient directly onto letterforms on hover.
## HTML
```html
<div class="hv-04">
  <div class="hv-04__grid">
    <div class="hv-04__cell">
      <span class="hv-04__text hv-04__text--wipe">AURORA</span>
      <span class="hv-04__label">gradient position wipe</span>
    </div>
    <div class="hv-04__cell">
      <span class="hv-04__text hv-04__text--burst">RADIAL</span>
      <span class="hv-04__label">radial-gradient burst</span>
    </div>
    <div class="hv-04__cell">
      <span class="hv-04__text hv-04__text--rainbow">SPECTRUM</span>
      <span class="hv-04__label">rainbow hue-shift</span>
    </div>
    <div class="hv-04__cell">
      <span class="hv-04__text hv-04__text--shimmer">SHIMMER</span>
      <span class="hv-04__label">shimmer keyframe</span>
    </div>
    <div class="hv-04__cell">
      <span class="hv-04__text hv-04__text--duotone">DUOTONE</span>
      <span class="hv-04__label">dual-tone color swap</span>
    </div>
    <div class="hv-04__cell">
      <span class="hv-04__text hv-04__text--diagonal">PRISM</span>
      <span class="hv-04__label">diagonal sweep</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-04,
.hv-04 *,
.hv-04 *::before,
.hv-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-04 ::selection {
  background: #6d28d9;
  color: #fff;
}

.hv-04 {
  --bg: #06040f;
  --text: #d4d4f7;
  --dim: #555;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-04__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 32px;
  max-width: 900px;
  width: 100%;
}

.hv-04__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 48px 24px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 14px;
}

.hv-04__label {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--dim);
  text-align: center;
}
/* shared text base */

.hv-04__text {
  font-size: clamp(1.6rem,4vw,2.4rem);
  font-weight: 900;
  letter-spacing: .06em;
  cursor: default;
  display: inline-block;
  -webkit-background-clip: text;
  background-clip: text;
}
/* 1 — position wipe */

.hv-04__text--wipe {
  color: var(--text);
  background-image: linear-gradient(90deg,#7c3aed,#06b6d4,#10b981);
  background-size: 200% auto;
  background-position: right center;
  transition: background-position .5s cubic-bezier(.4,0,.2,1),color .5s;
}

.hv-04__text--wipe:hover {
  color: transparent;
  background-position: left center;
}
/* 2 — radial burst */

.hv-04__text--burst {
  color: var(--text);
  background-image: radial-gradient(circle at 50% 50%,#f59e0b,#ef4444,#7c3aed);
  background-size: 0% 0%;
  background-position: center;
  transition: background-size .5s cubic-bezier(.4,0,.2,1),color .5s;
}

.hv-04__text--burst:hover {
  color: transparent;
  background-size: 200% 200%;
}
/* 3 — rainbow shift */

.hv-04__text--rainbow {
  color: var(--text);
  background-image: linear-gradient(90deg,#f43f5e,#f59e0b,#10b981,#06b6d4,#6d28d9,#f43f5e);
  background-size: 400% auto;
  background-position: 0% center;
  transition: background-position .6s,color .4s;
}

.hv-04__text--rainbow:hover {
  color: transparent;
  background-position: 100% center;
}
/* 4 — shimmer keyframe */

.hv-04__text--shimmer {
  color: var(--text);
  background-image: linear-gradient(105deg,#c4b5fd 0%,#fff 40%,#7c3aed 55%,#c4b5fd 100%);
  background-size: 200% auto;
  transition: color .3s;
}

.hv-04__text--shimmer:hover {
  color: transparent;
  animation: hv-04-shimmer .8s linear infinite;
}

@keyframes hv-04-shimmer {
  0% {
    background-position: -100% center;
  }

  100% {
    background-position: 200% center;
  }
}
/* 5 — duotone swap */

.hv-04__text--duotone {
  color: var(--text);
  background-image: linear-gradient(135deg,#f43f5e,#f97316);
  background-size: 100% 100%;
  transition: color .4s,filter .4s;
}

.hv-04__text--duotone:hover {
  color: transparent;
  filter: hue-rotate(120deg) saturate(1.4);
}
/* 6 — diagonal sweep */

.hv-04__text--diagonal {
  color: var(--text);
  background-image: linear-gradient(135deg,#06b6d4 0%,#a21caf 50%,#06b6d4 100%);
  background-size: 200% 200%;
  background-position: bottom right;
  transition: background-position .6s cubic-bezier(.4,0,.2,1),color .4s;
}

.hv-04__text--diagonal:hover {
  color: transparent;
  background-position: top left;
}

@media (max-width: 640px) {
  .hv-04__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 400px) {
  .hv-04__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-04__text {
    transition: none!important;
    animation: none!important;
  }
}
```
