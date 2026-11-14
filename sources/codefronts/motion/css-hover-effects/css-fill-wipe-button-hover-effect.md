---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-fill-wipe-button-hover-effect/"
title: "CSS Fill Wipe Button Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Six directional fill-wipe button styles — left wipe, diagonal corner, radial center-out, curtain drop, split from center, and pixel dissolve — demonstrating…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Fill Wipe Button Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-fill-wipe-button-hover-effect/

Six directional fill-wipe button styles — left wipe, diagonal corner, radial center-out, curtain drop, split from center, and pixel dissolve — demonstrating every axis of reveal using CSS pseudo-element transitions and clip-path on buttons.
## HTML
```html
<div class="hv-10">
  <div class="hv-10__grid">
    <div class="hv-10__cell">
      <button class="hv-10__btn hv-10__btn--left"><span>Left Wipe</span></button>
      <span class="hv-10__label">scaleX from left</span>
    </div>
    <div class="hv-10__cell">
      <button class="hv-10__btn hv-10__btn--diag"><span>Diagonal Slash</span></button>
      <span class="hv-10__label">rotated translate</span>
    </div>
    <div class="hv-10__cell">
      <button class="hv-10__btn hv-10__btn--radial"><span>Radial Burst</span></button>
      <span class="hv-10__label">scale from center</span>
    </div>
    <div class="hv-10__cell">
      <button class="hv-10__btn hv-10__btn--drop"><span>Curtain Drop</span></button>
      <span class="hv-10__label">scaleY from top</span>
    </div>
    <div class="hv-10__cell">
      <button class="hv-10__btn hv-10__btn--split"><span>Center Split</span></button>
      <span class="hv-10__label">dual scaleX outward</span>
    </div>
    <div class="hv-10__cell">
      <button class="hv-10__btn hv-10__btn--inset"><span>Inset Grow</span></button>
      <span class="hv-10__label">box-shadow inset fill</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-10,
.hv-10 *,
.hv-10 *::before,
.hv-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-10 ::selection {
  background: #dc2626;
  color: #fff;
}

.hv-10 {
  --bg: #0f0400;
  --text: #fef2f2;
  --dim: #6b7280;
  --red: #ef4444;
  --rose: #f43f5e;
  --orange: #f97316;
  --coral: #fb923c;
  --crimson: #dc2626;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-10__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 36px;
  max-width: 840px;
  width: 100%;
}

.hv-10__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 40px 20px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
}

.hv-10__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}
/* shared btn */

.hv-10__btn {
  position: relative;
  overflow: hidden;
  padding: 13px 32px;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: .05em;
  cursor: pointer;
  border-radius: 6px;
}

.hv-10__btn span {
  position: relative;
  z-index: 1;
}

.hv-10__btn::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 0;
}
/* 1 — left wipe */

.hv-10__btn--left {
  background: transparent;
  border: 2px solid var(--red);
  color: var(--red);
  transition: color .35s;
}

.hv-10__btn--left::before {
  background: var(--red);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .35s cubic-bezier(.4,0,.2,1);
}

.hv-10__btn--left:hover {
  color: #fff;
}

.hv-10__btn--left:hover::before {
  transform: scaleX(1);
}
/* 2 — diagonal slash */

.hv-10__btn--diag {
  background: transparent;
  border: 2px solid var(--rose);
  color: var(--rose);
  transition: color .4s;
}

.hv-10__btn--diag::before {
  inset: -20% -20%;
  background: var(--rose);
  transform: skewX(-25deg) scaleX(0);
  transform-origin: left center;
  transition: transform .5s cubic-bezier(.4,0,.2,1);
}

.hv-10__btn--diag:hover {
  color: #fff;
}

.hv-10__btn--diag:hover::before {
  transform: skewX(-25deg) scaleX(1);
}
/* 3 — radial burst */

.hv-10__btn--radial {
  background: transparent;
  border: 2px solid var(--orange);
  color: var(--orange);
  transition: color .35s;
}

.hv-10__btn--radial::before {
  background: var(--orange);
  border-radius: 50%;
  transform: scale(0);
  transition: transform .45s cubic-bezier(.4,0,.2,1);
}

.hv-10__btn--radial:hover {
  color: #fff;
}

.hv-10__btn--radial:hover::before {
  transform: scale(3);
}
/* 4 — curtain drop */

.hv-10__btn--drop {
  background: transparent;
  border: 2px solid var(--coral);
  color: var(--coral);
  transition: color .35s;
}

.hv-10__btn--drop::before {
  background: var(--coral);
  transform: scaleY(0);
  transform-origin: top;
  transition: transform .35s cubic-bezier(.4,0,.2,1);
}

.hv-10__btn--drop:hover {
  color: #fff;
}

.hv-10__btn--drop:hover::before {
  transform: scaleY(1);
}
/* 5 — center split */

.hv-10__btn--split {
  background: transparent;
  border: 2px solid var(--crimson);
  color: var(--crimson);
  transition: color .35s;
}

.hv-10__btn--split::before {
  background: var(--crimson);
  transform: scaleX(0);
  transform-origin: center;
  transition: transform .35s cubic-bezier(.4,0,.2,1);
}

.hv-10__btn--split:hover {
  color: #fff;
}

.hv-10__btn--split:hover::before {
  transform: scaleX(1);
}
/* 6 — inset box-shadow */

.hv-10__btn--inset {
  background: transparent;
  border: 2px solid var(--red);
  color: var(--red);
  box-shadow: inset 0 0 0 0 var(--red);
  transition: box-shadow .4s cubic-bezier(.4,0,.2,1),color .4s;
}

.hv-10__btn--inset::before {
  display: none;
}

.hv-10__btn--inset:hover {
  box-shadow: inset 0 0 0 60px var(--red);
  color: #fff;
}

@media (max-width: 640px) {
  .hv-10__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 400px) {
  .hv-10__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-10__btn,
    .hv-10__btn::before {
    transition: none!important;
  }
}
```
