---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-split-text-hover-effect/"
title: "CSS Split Text Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four split-text hover effects where words or characters divide and separate on hover — vertical halve, top-bottom reveal, left-right push-apart, and diagonal…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Split Text Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-split-text-hover-effect/

Four split-text hover effects where words or characters divide and separate on hover — vertical halve, top-bottom reveal, left-right push-apart, and diagonal slash — all achieved with CSS clip-path on layered pseudo-elements.
## HTML
```html
<div class="hv-05">
  <div class="hv-05__grid">
    <div class="hv-05__cell">
      <span class="hv-05__split hv-05__split--vert" data-text="DIVIDE">DIVIDE</span>
      <span class="hv-05__label">top / bottom split</span>
    </div>
    <div class="hv-05__cell">
      <span class="hv-05__split hv-05__split--lr" data-text="SCHISM">SCHISM</span>
      <span class="hv-05__label">left / right push</span>
    </div>
    <div class="hv-05__cell">
      <span class="hv-05__split hv-05__split--diag" data-text="SLASH">SLASH</span>
      <span class="hv-05__label">diagonal polygon</span>
    </div>
    <div class="hv-05__cell">
      <span class="hv-05__split hv-05__split--fade" data-text="RIFT">RIFT</span>
      <span class="hv-05__label">split + fade</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-05,
.hv-05 *,
.hv-05 *::before,
.hv-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-05 ::selection {
  background: #0891b2;
  color: #fff;
}

.hv-05 {
  --bg: #020917;
  --text: #e0f2fe;
  --dim: #475569;
  --cyan: #06b6d4;
  --rose: #f43f5e;
  --violet: #8b5cf6;
  --amber: #f59e0b;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-05__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 48px;
  max-width: 800px;
  width: 100%;
}

.hv-05__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  padding: 60px 32px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 14px;
}

.hv-05__label {
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--dim);
}
/* shared split base */

.hv-05__split {
  font-size: clamp(2rem,6vw,3rem);
  font-weight: 900;
  letter-spacing: .1em;
  position: relative;
  cursor: default;
  display: inline-block;
  color: transparent;
  overflow: hidden;
}

.hv-05__split::before,
.hv-05__split::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transition: transform .45s cubic-bezier(.4,0,.2,1),opacity .45s;
  pointer-events: none;
}
/* 1 — vertical top/bottom */

.hv-05__split--vert::before {
  color: var(--cyan);
  clip-path: inset(0 0 50% 0);
}

.hv-05__split--vert::after {
  color: var(--cyan);
  clip-path: inset(50% 0 0 0);
}

.hv-05__split--vert:hover::before {
  transform: translateY(-.55em);
}

.hv-05__split--vert:hover::after {
  transform: translateY(.55em);
}
/* 2 — left/right */

.hv-05__split--lr::before {
  color: var(--rose);
  clip-path: inset(0 50% 0 0);
}

.hv-05__split--lr::after {
  color: var(--amber);
  clip-path: inset(0 0 0 50%);
}

.hv-05__split--lr:hover::before {
  transform: translateX(-.4em);
}

.hv-05__split--lr:hover::after {
  transform: translateX(.4em);
}
/* 3 — diagonal */

.hv-05__split--diag::before {
  color: var(--violet);
  clip-path: polygon(0 0,100% 0,60% 100%,0 100%);
}

.hv-05__split--diag::after {
  color: var(--cyan);
  clip-path: polygon(60% 0,100% 0,100% 100%,0 100%);
  /* small intentional gap at clip edge */
}

.hv-05__split--diag:hover::before {
  transform: translate(-.3em,-.3em);
}

.hv-05__split--diag:hover::after {
  transform: translate(.3em,.3em);
}
/* 4 — split + fade */

.hv-05__split--fade::before {
  color: var(--amber);
  clip-path: inset(0 0 50% 0);
}

.hv-05__split--fade::after {
  color: var(--rose);
  clip-path: inset(50% 0 0 0);
}

.hv-05__split--fade:hover::before {
  transform: translateY(-.6em) rotate(-3deg);
  opacity: 0;
}

.hv-05__split--fade:hover::after {
  transform: translateY(.6em) rotate(3deg);
  opacity: 0;
}

@media (max-width: 520px) {
  .hv-05__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-05__split::before,
    .hv-05__split::after {
    transition: none!important;
  }
}
```
