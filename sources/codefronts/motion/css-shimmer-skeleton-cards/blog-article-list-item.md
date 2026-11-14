---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/blog-article-list-item/"
title: "Blog Article List Item"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "An editorial media-object skeleton on warm ivory paper: a rectangular thumbnail with an inset hairline, beside three text lines at 80%, 100% and 40% — title,…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blog Article List Item
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/blog-article-list-item/

An editorial media-object skeleton on warm ivory paper: a rectangular thumbnail with an inset hairline, beside three text lines at 80%, 100% and 40% — title, excerpt, metadata. The uneven widths are the whole trick: they read as natural paragraph text, and the sepia-tinted bars feel like a magazine, not a wireframe.
## HTML
```html
<section class="ssc-05" aria-label="Blog article list skeleton demo">
  <div class="ssc-05__list" role="status" aria-busy="true">
    <span class="ssc-sr">Loading articles…</span>
    <div class="ssc-05__item" aria-hidden="true">
      <div class="ssc-sk ssc-05__thumb"></div>
      <div class="ssc-05__lines">
        <div class="ssc-sk ssc-05__title" style="width:80%"></div>
        <div class="ssc-sk ssc-05__text" style="width:100%"></div>
        <div class="ssc-sk ssc-05__meta" style="width:40%"></div>
      </div>
    </div>
    <div class="ssc-05__item" aria-hidden="true">
      <div class="ssc-sk ssc-05__thumb"></div>
      <div class="ssc-05__lines">
        <div class="ssc-sk ssc-05__title" style="width:70%"></div>
        <div class="ssc-sk ssc-05__text" style="width:96%"></div>
        <div class="ssc-sk ssc-05__meta" style="width:34%"></div>
      </div>
    </div>
    <div class="ssc-05__item" aria-hidden="true">
      <div class="ssc-sk ssc-05__thumb"></div>
      <div class="ssc-05__lines">
        <div class="ssc-sk ssc-05__title" style="width:86%"></div>
        <div class="ssc-sk ssc-05__text" style="width:100%"></div>
        <div class="ssc-sk ssc-05__meta" style="width:46%"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-05,
.ssc-05 *,
.ssc-05 *::before,
.ssc-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-05 {
  --sk-bg: oklch(0.91 0.018 80);
  --sk-shine: rgba(255,253,248,.85);
  font-family: Georgia,'Times New Roman',serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.97 0.01 85),oklch(0.95 0.016 80));
}

.ssc-05 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 6px;
}

.ssc-05 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-05-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-05-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-05 .ssc-sr {
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

.ssc-05 .ssc-05__list {
  position: relative;
  width: min(560px,100%);
  background: oklch(0.99 0.005 85);
  border: 1px solid oklch(0.88 0.02 80);
  border-radius: 4px;
  padding: 6px 22px;
  box-shadow: 0 18px 40px -28px oklch(0.4 0.04 70 / .55);
}

.ssc-05 .ssc-05__item {
  display: flex;
  gap: 16px;
  padding: 17px 0;
  border-bottom: 1px dotted oklch(0.85 0.025 80);
}

.ssc-05 .ssc-05__item:last-child {
  border-bottom: none;
}

.ssc-05 .ssc-05__item:nth-child(3) .ssc-sk::after {
  animation-delay: .12s;
}

.ssc-05 .ssc-05__item:nth-child(4) .ssc-sk::after {
  animation-delay: .24s;
}

.ssc-05 .ssc-05__thumb {
  width: 120px;
  height: 82px;
  flex-shrink: 0;
  border-radius: 3px;
  box-shadow: inset 0 0 0 1px oklch(0.82 0.03 75);
}

.ssc-05 .ssc-05__lines {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 11px;
  padding-top: 4px;
}

.ssc-05 .ssc-05__title {
  height: 16px;
}

.ssc-05 .ssc-05__text {
  height: 11px;
}

.ssc-05 .ssc-05__meta {
  height: 9px;
  background: oklch(0.88 0.03 75);
}

@media (prefers-reduced-motion: reduce) {
  .ssc-05 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — 80/100/40% line widths mimic paragraph rhythm; an inset box-shadow ring gives the thumb a print plate mark. */
```
