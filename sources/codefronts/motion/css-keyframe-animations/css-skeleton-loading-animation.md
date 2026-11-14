---
source: "codefronts"
url: "https://codefronts.com/motion/css-keyframe-animations/css-skeleton-loading-animation/"
title: "CSS Skeleton Loading Animation"
section: "motion"
category: "css-keyframe-animations"
category_name: "CSS Keyframe Animations"
description: "Shimmer skeleton loading placeholders for blog cards, profile layouts, list rows and dashboard stat cards using a scoped linear-gradient sweep keyframe."
has_js: "false"
---

Here's a working CSS Keyframe Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Skeleton Loading Animation
Source: https://codefronts.com/motion/css-keyframe-animations/css-skeleton-loading-animation/

Shimmer skeleton loading placeholders for blog cards, profile layouts, list rows and dashboard stat cards using a scoped linear-gradient sweep keyframe.
## HTML
```html
<div class="kf-10">
  <div class="kf-10__title">Skeleton <span>Loading</span> Screens</div>
  <div class="kf-10__grid">

    <!-- Blog card skeletons -->
    <div class="kf-10__card">
      <div class="kf-10__skel kf-10__img-skel"></div>
      <div class="kf-10__skel kf-10__line"></div>
      <div class="kf-10__skel kf-10__line--sm"></div>
      <div class="kf-10__skel kf-10__line--xs"></div>
      <div class="kf-10__avatar-row">
        <div class="kf-10__skel kf-10__av-skel"></div>
        <div class="kf-10__skel kf-10__name-skel"></div>
      </div>
    </div>
    <div class="kf-10__card">
      <div class="kf-10__skel kf-10__img-skel"></div>
      <div class="kf-10__skel kf-10__line"></div>
      <div class="kf-10__skel kf-10__line--sm"></div>
      <div class="kf-10__skel kf-10__line--xs"></div>
      <div class="kf-10__avatar-row">
        <div class="kf-10__skel kf-10__av-skel"></div>
        <div class="kf-10__skel kf-10__name-skel"></div>
      </div>
    </div>

    <!-- Profile skeleton -->
    <div class="kf-10__profile">
      <div class="kf-10__skel kf-10__profile-av"></div>
      <div class="kf-10__skel kf-10__profile-name"></div>
      <div class="kf-10__skel kf-10__profile-sub"></div>
      <div class="kf-10__profile-bars">
        <div class="kf-10__skel" style="height:11px"></div>
        <div class="kf-10__skel" style="height:11px;width:85%"></div>
        <div class="kf-10__skel" style="height:11px;width:70%"></div>
        <div class="kf-10__skel" style="height:11px;width:90%"></div>
      </div>
    </div>

    <!-- List skeleton -->
    <div class="kf-10__list" style="grid-column:span 2">
      <div class="kf-10__list-item"><div class="kf-10__skel kf-10__li-icon"></div><div class="kf-10__li-body"><div class="kf-10__skel kf-10__li-t"></div><div class="kf-10__skel kf-10__li-s"></div></div></div>
      <div class="kf-10__list-item"><div class="kf-10__skel kf-10__li-icon"></div><div class="kf-10__li-body"><div class="kf-10__skel kf-10__li-t"></div><div class="kf-10__skel kf-10__li-s"></div></div></div>
      <div class="kf-10__list-item"><div class="kf-10__skel kf-10__li-icon"></div><div class="kf-10__li-body"><div class="kf-10__skel kf-10__li-t"></div><div class="kf-10__skel kf-10__li-s"></div></div></div>
    </div>

    <div class="kf-10__card">
      <div class="kf-10__skel kf-10__img-skel"></div>
      <div class="kf-10__skel kf-10__line"></div>
      <div class="kf-10__skel kf-10__line--sm"></div>
    </div>

    <!-- Dashboard -->
    <div class="kf-10__dash">
      <div class="kf-10__stat-card"><div class="kf-10__skel kf-10__stat-num"></div><div class="kf-10__skel kf-10__stat-label"></div><div class="kf-10__skel kf-10__stat-bar"></div></div>
      <div class="kf-10__stat-card"><div class="kf-10__skel kf-10__stat-num"></div><div class="kf-10__skel kf-10__stat-label"></div><div class="kf-10__skel kf-10__stat-bar"></div></div>
      <div class="kf-10__stat-card"><div class="kf-10__skel kf-10__stat-num"></div><div class="kf-10__skel kf-10__stat-label"></div><div class="kf-10__skel kf-10__stat-bar"></div></div>
      <div class="kf-10__stat-card"><div class="kf-10__skel kf-10__stat-num"></div><div class="kf-10__skel kf-10__stat-label"></div><div class="kf-10__skel kf-10__stat-bar"></div></div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

.kf-10,
.kf-10 *,
.kf-10 *::before,
.kf-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.kf-10 ::selection {
  background: #7c3aed;
  color: #fff;
}

.kf-10 {
  --bg: #f5f3ff;
  --card: #fff;
  --base: #e5e7eb;
  --shine: rgba(255,255,255,.9);
  --purple: #7c3aed;
  --purple-light: #ede9fe;
  font-family: 'Inter',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 40px;
  color: #1f2937;
}

.kf-10__title {
  font-size: 1.6rem;
  font-weight: 600;
  color: #1f2937;
  letter-spacing: -.02em;
}

.kf-10__title span {
  color: var(--purple);
}

.kf-10__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 24px;
  max-width: 900px;
  width: 100%;
}
/* Shimmer core */

.kf-10__skel {
  background: var(--base);
  border-radius: 6px;
  position: relative;
  overflow: hidden;
}

.kf-10__skel::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,transparent 0%,var(--shine) 50%,transparent 100%);
  animation: kf-10-shimmer 1.6s ease-in-out infinite;
}

@keyframes kf-10-shimmer {
  0% {
    transform: translateX(-100%);
  }

  100% {
    transform: translateX(100%);
  }
}
/* 1 — Blog card skeleton */

.kf-10__card {
  background: var(--card);
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0,0,0,.08);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.kf-10__img-skel {
  height: 140px;
  border-radius: 10px;
}

.kf-10__line {
  height: 14px;
}

.kf-10__line--sm {
  height: 12px;
  width: 70%;
}

.kf-10__line--xs {
  height: 10px;
  width: 50%;
}

.kf-10__avatar-row {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-top: 4px;
}

.kf-10__av-skel {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  flex: 0 0 32px;
}

.kf-10__name-skel {
  height: 11px;
  flex: 0 0 90px;
}
/* 2 — Profile skeleton */

.kf-10__profile {
  background: var(--card);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0,0,0,.08);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}

.kf-10__profile-av {
  width: 72px;
  height: 72px;
  border-radius: 50%;
}

.kf-10__profile-name {
  height: 16px;
  width: 120px;
}

.kf-10__profile-sub {
  height: 12px;
  width: 80px;
}

.kf-10__profile-bars {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
/* 3 — List skeleton */

.kf-10__list {
  background: var(--card);
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0,0,0,.08);
  display: flex;
  flex-direction: column;
  gap: 0;
}

.kf-10__list-item {
  display: flex;
  gap: 12px;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid var(--bg);
}

.kf-10__list-item:last-child {
  border: 0;
  padding-bottom: 0;
}

.kf-10__li-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  flex: 0 0 40px;
}

.kf-10__li-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.kf-10__li-t {
  height: 13px;
}

.kf-10__li-s {
  height: 10px;
  width: 65%;
}
/* 4 — Dashboard skeleton */

.kf-10__dash {
  grid-column: span 3;
  background: var(--card);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0,0,0,.08);
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 20px;
}

.kf-10__stat-card {
  background: var(--purple-light);
  border-radius: 12px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.kf-10__stat-num {
  height: 28px;
  width: 80px;
}

.kf-10__stat-label {
  height: 11px;
  width: 60%;
}

.kf-10__stat-bar {
  height: 5px;
  border-radius: 3px;
  margin-top: 4px;
}
/* Stagger delays for variety */

.kf-10__card:nth-child(2) .kf-10__skel::after {
  animation-delay: .2s;
}

.kf-10__card:nth-child(3) .kf-10__skel::after {
  animation-delay: .4s;
}

.kf-10__list-item:nth-child(2) .kf-10__skel::after {
  animation-delay: .15s;
}

.kf-10__list-item:nth-child(3) .kf-10__skel::after {
  animation-delay: .3s;
}

.kf-10__stat-card:nth-child(2) .kf-10__skel::after {
  animation-delay: .1s;
}

.kf-10__stat-card:nth-child(3) .kf-10__skel::after {
  animation-delay: .2s;
}

.kf-10__stat-card:nth-child(4) .kf-10__skel::after {
  animation-delay: .3s;
}

@media (max-width: 700px) {
  .kf-10__grid {
    grid-template-columns: 1fr;
  }

  .kf-10__dash {
    grid-column: span 1;
    grid-template-columns: repeat(2,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .kf-10__skel::after {
    animation: none;
  }
}
```
