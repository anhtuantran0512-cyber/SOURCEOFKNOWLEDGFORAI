---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-skeleton-screen-loader/"
title: "CSS Skeleton Screen Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Three shimmer-based CSS skeleton screens — a profile card, an article card, and a dashboard widget — using a single shared shimmer keyframe scoped per wrapper."
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Skeleton Screen Loader
Source: https://codefronts.com/motion/css-loader-designs/css-skeleton-screen-loader/

Three shimmer-based CSS skeleton screens — a profile card, an article card, and a dashboard widget — using a single shared shimmer keyframe scoped per wrapper.
## HTML
```html
<div class="ld-03">
  <div class="ld-03__stage">
    <!-- Profile card -->
    <div class="ld-03__card">
      <div class="ld-03__meta">
        <div class="ld-03__skel ld-03__avatar"></div>
        <div class="ld-03__lines">
          <div class="ld-03__skel ld-03__line"></div>
          <div class="ld-03__skel ld-03__line ld-03__line--short"></div>
        </div>
```
## CSS
```css
.ld-03,
.ld-03 *,
.ld-03 *::before,
.ld-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-03 {
  --bg: #111827;
  --card: #1f2937;
  --shine: rgba(255,255,255,.06);
  --line: #374151;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
  padding: 40px;
}

.ld-03__stage {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(280px,1fr));
  gap: 24px;
  max-width: 900px;
  width: 100%;
}

.ld-03__card {
  background: var(--card);
  border-radius: 16px;
  padding: 20px;
  overflow: hidden;
}

.ld-03__skel {
  background: var(--line);
  border-radius: 8px;
  position: relative;
  overflow: hidden;
}

.ld-03__skel::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,transparent 0%,var(--shine) 50%,transparent 100%);
  animation: ld-03-shimmer 1.5s ease-in-out infinite;
  transform: translateX(-100%);
}

@keyframes ld-03-shimmer {
  to {
    transform: translateX(100%);
  }
}
/* Profile card skeleton */

.ld-03__avatar {
  width: 56px;
  height: 56px;
  border-radius: 50%;
}

.ld-03__meta {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 16px;
}

.ld-03__lines {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.ld-03__line {
  height: 10px;
}

.ld-03__line--short {
  width: 60%;
}

.ld-03__image-skel {
  height: 140px;
  border-radius: 10px;
  margin-bottom: 16px;
}

.ld-03__text-block {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
/* Article skeleton */

.ld-03__article-img {
  height: 160px;
  border-radius: 10px;
  margin-bottom: 16px;
}

.ld-03__tag {
  height: 20px;
  width: 60px;
  border-radius: 20px;
  margin-bottom: 12px;
}

.ld-03__title-line {
  height: 14px;
  margin-bottom: 8px;
}

.ld-03__title-line--half {
  width: 55%;
}

.ld-03__para-line {
  height: 10px;
  margin-bottom: 6px;
}

.ld-03__para-line--short {
  width: 70%;
}
/* Dashboard skeleton */

.ld-03__stat-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 16px;
}

.ld-03__stat {
  background: var(--bg);
  border-radius: 10px;
  padding: 14px;
}

.ld-03__stat-num {
  height: 28px;
  width: 50%;
  margin-bottom: 8px;
  border-radius: 6px;
}

.ld-03__stat-lbl {
  height: 10px;
  width: 80%;
  border-radius: 4px;
}

.ld-03__chart {
  height: 100px;
  border-radius: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .ld-03__skel::after {
    animation: none;
  }
}
```
