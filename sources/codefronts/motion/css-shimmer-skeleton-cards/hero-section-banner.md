---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/hero-section-banner/"
title: "Hero Section Banner"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A full-width hero skeleton with cinema presence: a massive banner slab breathing a dark aurora gradient, overlaid by centred headline, subline and CTA-pill…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hero Section Banner
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/hero-section-banner/

A full-width hero skeleton with cinema presence: a massive banner slab breathing a dark aurora gradient, overlaid by centred headline, subline and CTA-pill placeholders swept by a wider, softer shimmer. This is the loading state for landing pages where the hero IS the first impression — it must feel designed, not broken.
## HTML
```html
<section class="ssc-11" aria-label="Hero banner skeleton demo">
  <div class="ssc-11__hero" role="status" aria-busy="true">
    <span class="ssc-sr">Loading hero…</span>
    <div class="ssc-11__stack" aria-hidden="true">
      <div class="ssc-sk ssc-11__kicker"></div>
      <div class="ssc-sk ssc-11__headline"></div>
      <div class="ssc-sk ssc-11__subline"></div>
      <div class="ssc-11__ctas">
        <div class="ssc-sk ssc-11__cta"></div>
        <div class="ssc-sk ssc-11__cta ssc-11__cta--ghost"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-11,
.ssc-11 *,
.ssc-11 *::before,
.ssc-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-11 {
  --drift: 9s;
  --sk-bg: rgba(255,255,255,.1);
  --sk-shine: rgba(255,255,255,.2);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 24px;
  background: oklch(0.15 0.02 280);
}

.ssc-11 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 9px;
}

.ssc-11 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 25%,var(--sk-shine) 50%,transparent 75%);
  animation: ssc-11-shimmer 2.1s ease-in-out infinite;
}

@keyframes ssc-11-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-11 .ssc-sr {
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

.ssc-11 .ssc-11__hero {
  position: relative;
  width: 100%;
  min-height: 280px;
  display: grid;
  place-items: center;
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,.1);
  background: radial-gradient(60% 90% at 20% 20%,oklch(0.42 0.16 300 / .75),transparent 60%),radial-gradient(55% 80% at 80% 30%,oklch(0.45 0.14 220 / .7),transparent 60%),radial-gradient(70% 70% at 55% 100%,oklch(0.4 0.15 350 / .6),transparent 60%),oklch(0.2 0.04 290);
  background-size: 180% 180%;
  animation: ssc-11-aurora var(--drift) ease-in-out infinite alternate;
}

@keyframes ssc-11-aurora {
  to {
    background-position: 100% 100%;
  }
}

.ssc-11 .ssc-11__stack {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  width: min(520px,86%);
  padding: 44px 0;
}

.ssc-11 .ssc-11__kicker {
  width: 120px;
  height: 10px;
  border-radius: 999px;
}

.ssc-11 .ssc-11__headline {
  width: 78%;
  height: 34px;
  border-radius: 12px;
}

.ssc-11 .ssc-11__subline {
  width: 52%;
  height: 13px;
}

.ssc-11 .ssc-11__ctas {
  display: flex;
  gap: 12px;
  margin-top: 10px;
}

.ssc-11 .ssc-11__cta {
  width: 132px;
  height: 44px;
  border-radius: 999px;
  background: rgba(255,255,255,.18);
}

.ssc-11 .ssc-11__cta--ghost {
  background: transparent;
  box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.22);
}

@media (prefers-reduced-motion: reduce) {
  .ssc-11 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }

  .ssc-11__hero {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a slow aurora drifts on ONE big element while translucent bars sweep with the standard translateX shine. */
```
