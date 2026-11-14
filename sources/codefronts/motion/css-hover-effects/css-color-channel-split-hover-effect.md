---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-color-channel-split-hover-effect/"
title: "CSS Color Channel Split Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four color channel separation effects on image containers — RGB duotone split, chromatic aberration text, green-screen channel extract, and full-color…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Color Channel Split Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-color-channel-split-hover-effect/

Four color channel separation effects on image containers — RGB duotone split, chromatic aberration text, green-screen channel extract, and full-color separation with mix-blend-mode — using CSS filter, mix-blend-mode, and pseudo-element tinting to deconstruct color into channels on hover.
## HTML
```html
<div class="hv-20">
  <div class="hv-20__grid">
    <div class="hv-20__cell">
      <div class="hv-20__box hv-20__box--rgb" data-text="SIGNAL">
        <span class="hv-20__box-label">SIGNAL</span>
      </div>
      <span class="hv-20__label">RGB channel split</span>
    </div>
    <div class="hv-20__cell">
      <div class="hv-20__box hv-20__box--chroma">
        <span class="hv-20__chroma" data-text="CHROMATIC">CHROMATIC</span>
      </div>
      <span class="hv-20__label">text shadow aberration</span>
    </div>
    <div class="hv-20__cell">
      <div class="hv-20__box hv-20__box--duo">
        <span class="hv-20__box-label">DUOTONE</span>
      </div>
      <span class="hv-20__label">color grade shift</span>
    </div>
    <div class="hv-20__cell">
      <div class="hv-20__box hv-20__box--screen">
        <div class="hv-20__screen-r"></div>
        <div class="hv-20__screen-b"></div>
        <span class="hv-20__box-label">COMPOSITE</span>
      </div>
      <span class="hv-20__label">screen blend channels</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-20,
.hv-20 *,
.hv-20 *::before,
.hv-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-20 ::selection {
  background: #dc2626;
  color: #fff;
}

.hv-20 {
  --bg: #050505;
  --dim: #4b5563;
  --red: #ff0040;
  --green: #00ff88;
  --blue: #0040ff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-20__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 40px;
  max-width: 720px;
  width: 100%;
}

.hv-20__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.hv-20__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}

.hv-20__box {
  width: 100%;
  aspect-ratio: 4/3;
  border-radius: 12px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  background: linear-gradient(135deg,#1a1a2e,#16213e,#0f3460,#533483);
  display: flex;
  align-items: center;
  justify-content: center;
}

.hv-20__box-label {
  position: relative;
  z-index: 2;
  font-size: 1.2rem;
  font-weight: 900;
  letter-spacing: .15em;
  color: #fff;
}
/* 1 — RGB channel split via text-shadow ghosts on the label */

.hv-20__box--rgb {
  background: radial-gradient(circle at 30% 30%,#1e3a8a 0%,transparent 50%), radial-gradient(circle at 70% 70%,#4c1d95 0%,transparent 50%), linear-gradient(135deg,#0a0a1a,#1a0a2e);
}

.hv-20__box--rgb .hv-20__box-label {
  transition: text-shadow .45s cubic-bezier(.4,0,.2,1),letter-spacing .45s;
  text-shadow: 0 0 0 transparent;
}

.hv-20__box--rgb:hover .hv-20__box-label {
  letter-spacing: .22em;
  text-shadow: -6px 0 0 var(--red), 6px 0 0 var(--blue), 0 4px 0 var(--green);
}
/* 2 — chromatic text shadow (now in a card to match siblings) */

.hv-20__box--chroma {
  background: radial-gradient(circle at 50% 50%,#1a1a2e 0%,#050505 100%);
  cursor: default;
}

.hv-20__chroma {
  font-size: clamp(1.4rem,4vw,1.8rem);
  font-weight: 900;
  letter-spacing: .12em;
  color: #fff;
  position: relative;
  display: inline-block;
  z-index: 2;
  transition: text-shadow .4s cubic-bezier(.4,0,.2,1),letter-spacing .4s;
}

.hv-20__box--chroma:hover .hv-20__chroma {
  letter-spacing: .18em;
  text-shadow: 5px 0 0 var(--red), -5px 0 0 var(--blue), 0 4px 0 rgba(0,255,136,.6);
}
/* 3 — duotone grade (bright varied base so hue-rotate is visible) */

.hv-20__box--duo {
  background: radial-gradient(circle at 25% 30%,#fbbf24 0%,transparent 35%), radial-gradient(circle at 75% 70%,#dc2626 0%,transparent 40%), linear-gradient(135deg,#7c3aed,#ec4899,#f59e0b);
  transition: filter .5s cubic-bezier(.4,0,.2,1);
}

.hv-20__box--duo:hover {
  filter: hue-rotate(180deg) saturate(1.6);
}

.hv-20__box--duo .hv-20__box-label {
  text-shadow: 0 2px 8px rgba(0,0,0,.8);
}
/* 4 — screen composite */

.hv-20__screen-r,
.hv-20__screen-b {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  width: 60%;
  height: 60%;
  opacity: 0;
  transition: opacity .4s,transform .5s cubic-bezier(.4,0,.2,1);
  z-index: 1;
}

.hv-20__screen-r {
  background: var(--red);
  mix-blend-mode: screen;
  top: 10%;
  left: 10%;
}

.hv-20__screen-b {
  background: var(--blue);
  mix-blend-mode: screen;
  top: 10%;
  right: 10%;
  left: auto;
}

.hv-20__box--screen:hover .hv-20__screen-r {
  opacity: .7;
  transform: translateX(-10px);
}

.hv-20__box--screen:hover .hv-20__screen-b {
  opacity: .7;
  transform: translateX(10px);
}

@media (max-width: 520px) {
  .hv-20__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-20__layer,
    .hv-20__screen-r,
    .hv-20__screen-b,
    .hv-20__box {
    transition: none!important;
  }

  .hv-20__chroma {
    transition: none!important;
  }
}
```
