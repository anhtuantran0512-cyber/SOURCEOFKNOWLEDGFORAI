---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-card-flip-hover-effect/"
title: "CSS Card Flip Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four CSS 3D card flip hover effects — horizontal flip, vertical flip, diagonal corner-peel flip, and reverse accordion fan — using rotateY/rotateX on…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Card Flip Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-card-flip-hover-effect/

Four CSS 3D card flip hover effects — horizontal flip, vertical flip, diagonal corner-peel flip, and reverse accordion fan — using rotateY/rotateX on preserve-3d containers with backface-visibility to reveal a styled back face on hover.
## HTML
```html
<div class="hv-14">
  <div class="hv-14__grid">
    <div class="hv-14__scene">
      <div class="hv-14__card hv-14__card--h">
        <div class="hv-14__face hv-14__face--front">
          <span class="hv-14__icon">♦</span>
          <span class="hv-14__label">Hover Me</span>
          <span class="hv-14__sub">horizontal flip →</span>
        </div>
        <div class="hv-14__face hv-14__face--back hv-14__back--rose">
          <span class="hv-14__icon">✦</span>
          <span class="hv-14__label">Revealed!</span>
          <span class="hv-14__sub">back face content</span>
        </div>
      </div>
    </div>
    <div class="hv-14__scene hv-14__scene--v">
      <div class="hv-14__card hv-14__card--v">
        <div class="hv-14__face hv-14__face--front hv-14__front--teal">
          <span class="hv-14__icon">◈</span>
          <span class="hv-14__label">Vertical</span>
          <span class="hv-14__sub">↓ flip over top</span>
        </div>
        <div class="hv-14__face hv-14__face--back hv-14__back--indigo">
          <span class="hv-14__icon">❋</span>
          <span class="hv-14__label">Back Face</span>
          <span class="hv-14__sub">rotateX flip</span>
        </div>
      </div>
    </div>
    <div class="hv-14__scene">
      <div class="hv-14__card hv-14__card--diag">
        <div class="hv-14__face hv-14__face--front hv-14__front--amber">
          <span class="hv-14__icon">◬</span>
          <span class="hv-14__label">Diagonal</span>
          <span class="hv-14__sub">corner-peel axis</span>
        </div>
        <div class="hv-14__face hv-14__face--back hv-14__back--orange">
          <span class="hv-14__icon">⟡</span>
          <span class="hv-14__label">Peeled!</span>
          <span class="hv-14__sub">rotate3d(1,1,0)</span>
        </div>
      </div>
    </div>
    <div class="hv-14__fan-wrap">
      <div class="hv-14__fan-card hv-14__fan-card--1">
        <span class="hv-14__fan-label">Fan</span>
      </div>
      <div class="hv-14__fan-card hv-14__fan-card--2"></div>
      <div class="hv-14__fan-card hv-14__fan-card--3"></div>
      <span class="hv-14__fan-hint">hover the stack</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-14,
.hv-14 *,
.hv-14 *::before,
.hv-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-14 ::selection {
  background: #be123c;
  color: #fff;
}

.hv-14 {
  --bg: #0a0008;
  --text: #ffe4e6;
  --dim: #6b7280;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-14__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 40px;
  max-width: 720px;
  width: 100%;
}
/* scene wrapper */

.hv-14__scene {
  perspective: 800px;
}

.hv-14__scene--v {
  perspective: 800px;
}
/* card */

.hv-14__card {
  position: relative;
  width: 100%;
  height: 220px;
  transform-style: preserve-3d;
  transition: transform .65s cubic-bezier(.4,0,.2,1);
  cursor: pointer;
}

.hv-14__face {
  position: absolute;
  inset: 0;
  border-radius: 14px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 24px;
}

.hv-14__icon {
  font-size: 2rem;
}

.hv-14__label {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text);
}

.hv-14__sub {
  font-size: .75rem;
  color: var(--dim);
  letter-spacing: .05em;
}
/* faces */

.hv-14__face--front {
  background: rgba(190,18,60,.2);
  border: 1px solid rgba(190,18,60,.4);
  color: var(--text);
}

.hv-14__back--rose {
  background: #be123c;
  color: #fff;
  transform: rotateY(180deg);
}

.hv-14__front--teal {
  background: rgba(13,148,136,.2);
  border: 1px solid rgba(13,148,136,.4);
}

.hv-14__back--indigo {
  background: #4338ca;
  color: #fff;
  transform: rotateX(180deg);
}

.hv-14__front--amber {
  background: rgba(180,83,9,.2);
  border: 1px solid rgba(180,83,9,.4);
}

.hv-14__back--orange {
  background: #c2410c;
  color: #fff;
  transform: rotate3d(1,1,0,180deg);
}
/* flip triggers */

.hv-14__card--h:hover {
  transform: rotateY(180deg);
}

.hv-14__card--v:hover {
  transform: rotateX(180deg);
}

.hv-14__card--diag:hover {
  transform: rotate3d(1,1,0,180deg);
}
/* fan accordion */

.hv-14__fan-wrap {
  position: relative;
  height: 220px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  cursor: pointer;
}

.hv-14__fan-card {
  position: absolute;
  width: 100%;
  height: 220px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.1);
  display: flex;
  align-items: center;
  justify-content: center;
  transform-origin: bottom center;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.hv-14__fan-card--1 {
  background: rgba(139,92,246,.25);
  z-index: 3;
}

.hv-14__fan-card--2 {
  background: rgba(109,40,217,.2);
  z-index: 2;
}

.hv-14__fan-card--3 {
  background: rgba(91,33,182,.15);
  z-index: 1;
}

.hv-14__fan-label {
  font-size: 1.1rem;
  font-weight: 700;
  color: #c4b5fd;
}

.hv-14__fan-hint {
  position: relative;
  z-index: 4;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
  margin-top: 8px;
}

.hv-14__fan-wrap:hover .hv-14__fan-card--2 {
  transform: rotateY(-30deg);
}

.hv-14__fan-wrap:hover .hv-14__fan-card--3 {
  transform: rotateY(-55deg);
}

@media (max-width: 520px) {
  .hv-14__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-14__card,
    .hv-14__fan-card {
    transition: none!important;
  }
}
```
