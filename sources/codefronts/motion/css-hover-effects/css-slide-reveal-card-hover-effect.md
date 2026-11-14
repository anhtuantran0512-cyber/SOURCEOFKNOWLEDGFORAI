---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-slide-reveal-card-hover-effect/"
title: "CSS Slide Reveal Card Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Five card hover effects that reveal hidden content through directional sliding panels — bottom-up overlay, left-push reveal, curtain wipe, inner-slide CTA,…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Slide Reveal Card Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-slide-reveal-card-hover-effect/

Five card hover effects that reveal hidden content through directional sliding panels — bottom-up overlay, left-push reveal, curtain wipe, inner-slide CTA, and overlay dissolve — all using CSS translate transforms and overflow hidden on nested containers.
## HTML
```html
<div class="hv-17">
  <div class="hv-17__grid">
    <div class="hv-17__card hv-17__card--up">
      <div class="hv-17__base">
        <div class="hv-17__icon">♟</div>
        <h3 class="hv-17__title">Strategy Kit</h3>
        <p class="hv-17__text">Modern approach to product design.</p>
      </div>
      <div class="hv-17__overlay hv-17__overlay--up">
        <h3 class="hv-17__title">Revealed!</h3>
        <p class="hv-17__text">Bottom-up slide reveals hidden details on hover.</p>
        <span class="hv-17__cta">Explore →</span>
      </div>
    </div>
    <div class="hv-17__card hv-17__card--push">
      <div class="hv-17__push-wrap">
        <div class="hv-17__push-face">
          <div class="hv-17__icon">⬡</div>
          <h3 class="hv-17__title">Design System</h3>
          <p class="hv-17__text">Components that scale.</p>
        </div>
        <div class="hv-17__push-back">
          <h3 class="hv-17__title">Left Push</h3>
          <p class="hv-17__text">Content slides out, reveal slides in.</p>
          <span class="hv-17__cta">Open →</span>
        </div>
      </div>
    </div>
    <div class="hv-17__card hv-17__card--curtain">
      <div class="hv-17__base">
        <div class="hv-17__icon">◈</div>
        <h3 class="hv-17__title">Brand Guide</h3>
        <p class="hv-17__text">Visual language at scale.</p>
      </div>
      <div class="hv-17__curtain"></div>
      <div class="hv-17__overlay hv-17__overlay--curtain">
        <h3 class="hv-17__title">Curtain!</h3>
        <p class="hv-17__text">Wipe reveals content beneath.</p>
        <span class="hv-17__cta">View →</span>
      </div>
    </div>
    <div class="hv-17__card hv-17__card--fade">
      <div class="hv-17__base">
        <div class="hv-17__icon">✦</div>
        <h3 class="hv-17__title">Case Study</h3>
        <p class="hv-17__text">Process and outcomes detailed.</p>
      </div>
      <div class="hv-17__overlay hv-17__overlay--fade">
        <h3 class="hv-17__title">Dissolve</h3>
        <p class="hv-17__text">Opacity fade with translateY settle.</p>
        <span class="hv-17__cta">Read →</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-17,
.hv-17 *,
.hv-17 *::before,
.hv-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-17 ::selection {
  background: #b45309;
  color: #fff;
}

.hv-17 {
  --bg: #0c0700;
  --text: #fef3c7;
  --dim: #78716c;
  --amber: #f59e0b;
  --orange: #f97316;
  --warm: #fbbf24;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-17__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 32px;
  max-width: 720px;
  width: 100%;
}
/* shared card */

.hv-17__card {
  position: relative;
  overflow: hidden;
  min-height: 220px;
  border-radius: 16px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.08);
  cursor: pointer;
}

.hv-17__base,
.hv-17__overlay {
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.hv-17__icon {
  font-size: 1.8rem;
  color: var(--amber);
}

.hv-17__title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text);
}

.hv-17__text {
  font-size: .82rem;
  color: var(--dim);
  line-height: 1.5;
}

.hv-17__cta {
  font-size: .85rem;
  font-weight: 600;
  color: var(--amber);
  margin-top: 4px;
}
/* 1 — bottom-up overlay */

.hv-17__overlay--up {
  position: absolute;
  inset: 0;
  background: var(--amber);
  transform: translateY(100%);
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.hv-17__overlay--up .hv-17__title {
  color: #000;
}

.hv-17__overlay--up .hv-17__text {
  color: rgba(0,0,0,.7);
}

.hv-17__overlay--up .hv-17__cta {
  color: #000;
}

.hv-17__card--up:hover .hv-17__overlay--up {
  transform: translateY(0);
}
/* 2 — left push */

.hv-17__push-wrap {
  position: absolute;
  inset: 0;
  display: flex;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.hv-17__push-face,
.hv-17__push-back {
  flex: 0 0 100%;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.hv-17__push-back {
  background: var(--orange);
}

.hv-17__push-back .hv-17__title {
  color: #fff;
}

.hv-17__push-back .hv-17__text {
  color: rgba(255,255,255,.8);
}

.hv-17__push-back .hv-17__cta {
  color: #fff;
}

.hv-17__card--push:hover .hv-17__push-wrap {
  transform: translateX(-50%);
}
/* 3 — curtain wipe */

.hv-17__curtain {
  position: absolute;
  inset: 0;
  background: var(--warm);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
  z-index: 1;
}

.hv-17__overlay--curtain {
  position: absolute;
  inset: 0;
  background: var(--warm);
  opacity: 0;
  transition: opacity .2s .3s;
  z-index: 2;
}

.hv-17__overlay--curtain .hv-17__title,
.hv-17__overlay--curtain .hv-17__text,
.hv-17__overlay--curtain .hv-17__cta {
  color: #000;
}

.hv-17__card--curtain:hover .hv-17__curtain {
  transform: scaleX(1);
}

.hv-17__card--curtain:hover .hv-17__overlay--curtain {
  opacity: 1;
}
/* 4 — fade dissolve */

.hv-17__overlay--fade {
  position: absolute;
  inset: 0;
  background: rgba(15,12,5,.92);
  -webkit-backdrop-filter: blur(4px);
  backdrop-filter: blur(4px);
  opacity: 0;
  transform: translateY(8px);
  transition: opacity .4s,transform .4s cubic-bezier(.4,0,.2,1);
}

.hv-17__card--fade:hover .hv-17__overlay--fade {
  opacity: 1;
  transform: translateY(0);
}

@media (max-width: 520px) {
  .hv-17__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-17__overlay,
    .hv-17__push-wrap,
    .hv-17__curtain {
    transition: none!important;
  }
}
```
