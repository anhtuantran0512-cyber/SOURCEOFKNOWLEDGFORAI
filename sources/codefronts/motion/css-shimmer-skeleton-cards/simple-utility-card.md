---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/simple-utility-card/"
title: "Simple Utility Card"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "The default, most reusable skeleton — reimagined: a 16:9 media slot whose surface carries a slow-breathing oklch gradient under the shimmer, a title line and…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Simple Utility Card
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/simple-utility-card/

The default, most reusable skeleton — reimagined: a 16:9 media slot whose surface carries a slow-breathing oklch gradient under the shimmer, a title line and two text blocks, inside a mint-glass card. Maps onto blog cards, link previews, docs tiles and pricing teasers with nothing but width tweaks.
## HTML
```html
<section class="ssc-09" aria-label="Simple utility card skeleton demo">
  <div class="ssc-09__card" role="status" aria-busy="true">
    <span class="ssc-sr">Loading content…</span>
    <div aria-hidden="true">
      <div class="ssc-sk ssc-09__media"></div>
      <div class="ssc-09__body">
        <div class="ssc-sk ssc-09__title" style="width:72%"></div>
        <div class="ssc-09__block">
          <div class="ssc-sk ssc-09__line" style="width:100%"></div>
          <div class="ssc-sk ssc-09__line" style="width:88%"></div>
        </div>
        <div class="ssc-09__block">
          <div class="ssc-sk ssc-09__line" style="width:96%"></div>
          <div class="ssc-sk ssc-09__line" style="width:100%"></div>
          <div class="ssc-sk ssc-09__line" style="width:54%"></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-09,
.ssc-09 *,
.ssc-09 *::before,
.ssc-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-09 {
  --sk-bg: oklch(0.92 0.02 175 / .8);
  --sk-shine: rgba(255,255,255,.85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 120% at 85% 0%,oklch(0.93 0.05 175),transparent 55%),radial-gradient(100% 110% at 10% 100%,oklch(0.93 0.04 220),transparent 55%),oklch(0.96 0.012 190);
}

.ssc-09 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 8px;
}

.ssc-09 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-09-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-09-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-09 .ssc-sr {
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

.ssc-09 .ssc-09__card {
  position: relative;
  width: min(340px,100%);
  background: rgba(255,255,255,.6);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255,255,255,.85);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 22px 48px -30px oklch(0.4 0.08 190 / .6);
}

.ssc-09 .ssc-09__media {
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 0;
  background: linear-gradient(120deg,oklch(0.9 0.04 175),oklch(0.9 0.035 250),oklch(0.9 0.04 175));
  background-size: 300% 300%;
  animation: ssc-09-drift 7s ease-in-out infinite;
}

@keyframes ssc-09-drift {
  50% {
    background-position: 100% 100%;
  }
}

.ssc-09 .ssc-09__body {
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ssc-09 .ssc-09__title {
  height: 16px;
}

.ssc-09 .ssc-09__block {
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.ssc-09 .ssc-09__line {
  height: 11px;
}

@media (prefers-reduced-motion: reduce) {
  .ssc-09 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }

  .ssc-09__media {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a slow hue-drifting gradient on the media slot layers under the fast translateX sweep. */
```
