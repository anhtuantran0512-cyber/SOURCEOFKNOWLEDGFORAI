---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-metallic-shimmer-skeleton-loader/"
title: "CSS Metallic Shimmer Skeleton Loader"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "Three skeleton loader patterns — a social card, a list component, and a data table — all sharing a single shimmer keyframe that sweeps a diagonal highlight…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Metallic Shimmer Skeleton Loader
Source: https://codefronts.com/motion/css-gradient-animation/css-metallic-shimmer-skeleton-loader/

Three skeleton loader patterns — a social card, a list component, and a data table — all sharing a single shimmer keyframe that sweeps a diagonal highlight across each bone element to indicate an active loading state.
## HTML
```html
<div class="ga-07" data-speed="normal">

  <!-- Card skeleton -->
  <div class="ga-07__card">
    <div class="ga-07__header">
      <div class="ga-07__bone ga-07__avatar"></div>
      <div class="ga-07__header-lines">
        <div class="ga-07__bone ga-07__line ga-07__line--lg"></div>
        <div class="ga-07__bone ga-07__line ga-07__line--md"></div>
      </div>
    </div>
    <div class="ga-07__bone ga-07__thumb"></div>
    <div class="ga-07__bone ga-07__line ga-07__line--lg"></div>
    <div class="ga-07__bone ga-07__line ga-07__line--md"></div>
    <div style="display:flex;gap:8px;">
      <div class="ga-07__bone ga-07__tag"></div>
      <div class="ga-07__bone ga-07__tag" style="width:80px;"></div>
    </div>
  </div>

  <!-- List skeleton -->
  <div class="ga-07__list">
    <div class="ga-07__list-row">
      <div class="ga-07__bone ga-07__icon"></div>
      <div class="ga-07__list-lines">
        <div class="ga-07__bone ga-07__line ga-07__line--lg"></div>
        <div class="ga-07__bone ga-07__line ga-07__line--sm"></div>
      </div>
    </div>
    <div class="ga-07__list-row">
      <div class="ga-07__bone ga-07__icon"></div>
      <div class="ga-07__list-lines">
        <div class="ga-07__bone ga-07__line" style="width:55%;"></div>
        <div class="ga-07__bone ga-07__line ga-07__line--sm"></div>
      </div>
    </div>
    <div class="ga-07__list-row">
      <div class="ga-07__bone ga-07__icon"></div>
      <div class="ga-07__list-lines">
        <div class="ga-07__bone ga-07__line ga-07__line--md"></div>
        <div class="ga-07__bone ga-07__line" style="width:30%;"></div>
      </div>
    </div>
    <div class="ga-07__list-row">
      <div class="ga-07__bone ga-07__icon"></div>
      <div class="ga-07__list-lines">
        <div class="ga-07__bone ga-07__line" style="width:65%;"></div>
        <div class="ga-07__bone ga-07__line ga-07__line--sm"></div>
      </div>
    </div>
    <div style="display:flex;gap:8px;margin-top:4px;">
      <div class="ga-07__bone" style="height:34px;width:100%;border-radius:8px;"></div>
    </div>
  </div>

  <!-- Table skeleton -->
  <div class="ga-07__table">
    <div class="ga-07__thead">
      <div class="ga-07__bone ga-07__th" style="width:50%;"></div>
      <div class="ga-07__bone ga-07__th" style="width:60%;"></div>
      <div class="ga-07__bone ga-07__th" style="width:70%;"></div>
      <div class="ga-07__bone ga-07__th" style="width:45%;"></div>
    </div>
    <div class="ga-07__tbody-row">
      <div class="ga-07__td--name">
        <div class="ga-07__bone ga-07__td--avatar"></div>
        <div class="ga-07__bone ga-07__td" style="flex:1;"></div>
      </div>
      <div class="ga-07__bone ga-07__td" style="width:55%;"></div>
      <div class="ga-07__bone ga-07__td" style="width:70%;"></div>
      <div class="ga-07__bone ga-07__td" style="width:40%;"></div>
    </div>
    <div class="ga-07__tbody-row">
      <div class="ga-07__td--name">
        <div class="ga-07__bone ga-07__td--avatar"></div>
        <div class="ga-07__bone ga-07__td" style="flex:1;width:65%;"></div>
      </div>
      <div class="ga-07__bone ga-07__td" style="width:80%;"></div>
      <div class="ga-07__bone ga-07__td" style="width:50%;"></div>
      <div class="ga-07__bone ga-07__td" style="width:60%;"></div>
    </div>
    <div class="ga-07__tbody-row">
      <div class="ga-07__td--name">
        <div class="ga-07__bone ga-07__td--avatar"></div>
        <div class="ga-07__bone ga-07__td" style="flex:1;width:45%;"></div>
      </div>
      <div class="ga-07__bone ga-07__td" style="width:65%;"></div>
      <div class="ga-07__bone ga-07__td" style="width:45%;"></div>
      <div class="ga-07__bone ga-07__td" style="width:75%;"></div>
    </div>
  </div>

  <div class="ga-07__controls">
    <button class="ga-07__toggle" data-s="slow">Slow</button>
    <button class="ga-07__toggle active" data-s="normal">Normal</button>
    <button class="ga-07__toggle" data-s="fast">Fast</button>
  </div>
</div>
```
## CSS
```css
.ga-07,
.ga-07 *,
.ga-07 *::before,
.ga-07 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-07 ::selection {
  background: rgba(99,102,241,.4);
  color: #fff;
}

.ga-07 {
  --bg: #0f111a;
  --skel: #1c1e2e;
  --shine-from: rgba(255,255,255,0);
  --shine-mid: rgba(255,255,255,.07);
  --shine-to: rgba(255,255,255,0);
  --dur: 1.6s;
  width: 100%;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  flex-wrap: wrap;
  padding: 48px 24px;
}
/* ── Base skeleton bone ── */

.ga-07__bone {
  position: relative;
  background: var(--skel);
  border-radius: 6px;
  overflow: hidden;
}
/* Shimmer wave — single pseudo-element slides across */

.ga-07__bone::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
      105deg,
      var(--shine-from) 0%,
      var(--shine-from) 35%,
      var(--shine-mid)  50%,
      var(--shine-to)   65%,
      var(--shine-to)   100%
    );
  background-size: 300% 100%;
  background-position: 100% 0;
  animation: ga-07-shimmer var(--dur) ease-in-out infinite;
}

@keyframes ga-07-shimmer {
  0% {
    background-position: 150% 0;
  }

  100% {
    background-position: -50% 0;
  }
}
/* ── Card skeleton ── */

.ga-07__card {
  width: 280px;
  background: #13151f;
  border: 1px solid rgba(255,255,255,.05);
  border-radius: 16px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ga-07__avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
}

.ga-07__line {
  height: 10px;
}

.ga-07__line--lg {
  width: 70%;
}

.ga-07__line--md {
  width: 50%;
}

.ga-07__line--sm {
  width: 35%;
}

.ga-07__thumb {
  width: 100%;
  height: 140px;
  border-radius: 10px;
}

.ga-07__tag {
  width: 60px;
  height: 22px;
  border-radius: 999px;
}

.ga-07__header {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ga-07__header-lines {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
/* ── List skeleton ── */

.ga-07__list {
  width: 280px;
  background: #13151f;
  border: 1px solid rgba(255,255,255,.05);
  border-radius: 16px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ga-07__list-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ga-07__icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  flex-shrink: 0;
}

.ga-07__list-lines {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 7px;
}
/* ── Table skeleton ── */

.ga-07__table {
  width: 560px;
  max-width: 100%;
  background: #13151f;
  border: 1px solid rgba(255,255,255,.05);
  border-radius: 16px;
  overflow: hidden;
}

.ga-07__thead {
  background: rgba(255,255,255,.03);
  padding: 14px 20px;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 16px;
  border-bottom: 1px solid rgba(255,255,255,.05);
}

.ga-07__tbody-row {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 16px;
  padding: 14px 20px;
  border-bottom: 1px solid rgba(255,255,255,.04);
  align-items: center;
}

.ga-07__tbody-row:last-child {
  border-bottom: none;
}

.ga-07__th {
  height: 8px;
  border-radius: 4px;
}

.ga-07__td {
  height: 9px;
  border-radius: 4px;
}

.ga-07__td--name {
  display: flex;
  align-items: center;
  gap: 10px;
}

.ga-07__td--avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  flex-shrink: 0;
}
/* Toggle loaded state */

.ga-07__controls {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
  z-index: 10;
}

.ga-07 {
  position: relative;
}

.ga-07__toggle {
  padding: 6px 16px;
  border-radius: 8px;
  font-size: .78rem;
  font-weight: 700;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,.1);
  background: rgba(255,255,255,.06);
  color: rgba(255,255,255,.5);
  transition: all .2s;
}

.ga-07__toggle:hover,
.ga-07__toggle.active {
  background: rgba(99,102,241,.2);
  border-color: rgba(99,102,241,.4);
  color: #a5b4fc;
}
/* Fast/slow speed variants */

.ga-07[data-speed="fast"] {
  --dur: .9s;
}

.ga-07[data-speed="slow"] {
  --dur: 2.8s;
}

@media (prefers-reduced-motion: reduce) {
  .ga-07__bone::after {
    animation: none;
    background-position: -50% 0;
  }
}
```

## JavaScript
```js
(function() {
  const w = document.querySelector('.ga-07');
  w.querySelectorAll('.ga-07__toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      w.querySelectorAll('.ga-07__toggle').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      w.dataset.speed = btn.dataset.s;
    });
  });
})();
```
