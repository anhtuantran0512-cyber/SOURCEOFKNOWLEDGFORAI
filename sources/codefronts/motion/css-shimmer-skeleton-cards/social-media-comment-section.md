---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/social-media-comment-section/"
title: "Social Media Comment Section"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A threaded comment skeleton on soft lavender glass: each comment pairs a gradient-tinted circular avatar with a short name line and a two-line paragraph…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Social Media Comment Section
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/social-media-comment-section/

A threaded comment skeleton on soft lavender glass: each comment pairs a gradient-tinted circular avatar with a short name line and a two-line paragraph block, cascading in with staggered shimmer. The avatar sits aligned to the name's baseline zone — the micro-detail that separates a polished skeleton from an obviously fake one.
## HTML
```html
<section class="ssc-06" aria-label="Comment section skeleton demo">
  <div class="ssc-06__panel" role="status" aria-busy="true">
    <span class="ssc-sr">Loading comments…</span>
    <div aria-hidden="true">
      <div class="ssc-06__comment">
        <div class="ssc-sk ssc-06__avatar"></div>
        <div class="ssc-06__body">
          <div class="ssc-sk ssc-06__name" style="width:30%"></div>
          <div class="ssc-sk ssc-06__line" style="width:100%"></div>
          <div class="ssc-sk ssc-06__line" style="width:85%"></div>
        </div>
      </div>
      <div class="ssc-06__comment">
        <div class="ssc-sk ssc-06__avatar"></div>
        <div class="ssc-06__body">
          <div class="ssc-sk ssc-06__name" style="width:24%"></div>
          <div class="ssc-sk ssc-06__line" style="width:100%"></div>
          <div class="ssc-sk ssc-06__line" style="width:62%"></div>
        </div>
      </div>
      <div class="ssc-06__comment">
        <div class="ssc-sk ssc-06__avatar"></div>
        <div class="ssc-06__body">
          <div class="ssc-sk ssc-06__name" style="width:36%"></div>
          <div class="ssc-sk ssc-06__line" style="width:94%"></div>
          <div class="ssc-sk ssc-06__line" style="width:74%"></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-06,
.ssc-06 *,
.ssc-06 *::before,
.ssc-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-06 {
  --tint: oklch(0.62 0.14 300);
  --sk-bg: oklch(0.9 0.025 300 / .8);
  --sk-shine: rgba(255,255,255,.8);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 120% at 80% 0%,oklch(0.93 0.04 320),transparent 60%),radial-gradient(90% 110% at 5% 100%,oklch(0.92 0.045 260),transparent 55%),oklch(0.96 0.015 290);
}

.ssc-06 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 6px;
}

.ssc-06 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-06-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-06-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-06 .ssc-sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.ssc-06 .ssc-06__panel {
  position: relative;
  width: min(460px,100%);
  background: rgba(255,255,255,.55);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255,255,255,.8);
  border-radius: 20px;
  padding: 8px 22px;
  box-shadow: 0 20px 44px -30px oklch(0.4 0.1 295 / .6);
}

.ssc-06 .ssc-06__comment {
  display: flex;
  gap: 12px;
  padding: 16px 0;
  border-bottom: 1px solid oklch(0.9 0.02 295 / .7);
}

.ssc-06 .ssc-06__comment:last-child {
  border-bottom: none;
}

.ssc-06 .ssc-06__comment:nth-child(2) .ssc-sk::after {
  animation-delay: .15s;
}

.ssc-06 .ssc-06__comment:nth-child(3) .ssc-sk::after {
  animation-delay: .3s;
}

.ssc-06 .ssc-06__comment:nth-child(2) .ssc-06__avatar {
  background: color-mix(in oklab,oklch(0.62 0.14 220) 22%,var(--sk-bg));
}

.ssc-06 .ssc-06__comment:nth-child(3) .ssc-06__avatar {
  background: color-mix(in oklab,oklch(0.62 0.14 20) 22%,var(--sk-bg));
}

.ssc-06 .ssc-06__avatar {
  width: 36px;
  height: 36px;
  flex-shrink: 0;
  border-radius: 50%;
  margin-top: 2px;
  margin-bottom: 4px;
  background: color-mix(in oklab,var(--tint) 22%,var(--sk-bg));
}

.ssc-06 .ssc-06__body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.ssc-06 .ssc-06__name {
  height: 11px;
  border-radius: 999px;
}

.ssc-06 .ssc-06__line {
  height: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .ssc-06 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — top-aligned avatars, per-user color-mix tints and staggered delays make the thread feel alive while loading. */
```
