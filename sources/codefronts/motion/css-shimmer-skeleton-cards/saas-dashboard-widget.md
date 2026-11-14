---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/saas-dashboard-widget/"
title: "SaaS Dashboard Widget"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "KPI stat-card skeletons on an indigo aurora: three glass widgets, each with an icon slot, a metric label line, a tall electric-violet value bar and a slim…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Dashboard Widget
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/saas-dashboard-widget/

KPI stat-card skeletons on an indigo aurora: three glass widgets, each with an icon slot, a metric label line, a tall electric-violet value bar and a slim trend line. The size hierarchy is deliberate — the value bar is visibly heavier and tinted with the accent, so users already know where the big number lands before the API answers.
## HTML
```html
<section class="ssc-04" aria-label="SaaS dashboard widget skeleton demo">
  <div class="ssc-04__row" role="status" aria-busy="true">
    <span class="ssc-sr">Loading dashboard metrics…</span>
    <div class="ssc-04__widget" aria-hidden="true">
      <div class="ssc-04__head">
        <div class="ssc-sk ssc-04__icon"></div>
        <div class="ssc-sk ssc-04__label" style="width:64%"></div>
      </div>
      <div class="ssc-sk ssc-04__value" style="width:58%"></div>
      <div class="ssc-sk ssc-04__trend" style="width:42%"></div>
    </div>
    <div class="ssc-04__widget" aria-hidden="true">
      <div class="ssc-04__head">
        <div class="ssc-sk ssc-04__icon"></div>
        <div class="ssc-sk ssc-04__label" style="width:50%"></div>
      </div>
      <div class="ssc-sk ssc-04__value" style="width:70%"></div>
      <div class="ssc-sk ssc-04__trend" style="width:34%"></div>
    </div>
    <div class="ssc-04__widget" aria-hidden="true">
      <div class="ssc-04__head">
        <div class="ssc-sk ssc-04__icon"></div>
        <div class="ssc-sk ssc-04__label" style="width:58%"></div>
      </div>
      <div class="ssc-sk ssc-04__value" style="width:48%"></div>
      <div class="ssc-sk ssc-04__trend" style="width:52%"></div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-04,
.ssc-04 *,
.ssc-04 *::before,
.ssc-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-04 {
  --violet: oklch(0.68 0.2 295);
  --sk-bg: rgba(255,255,255,.08);
  --sk-shine: rgba(255,255,255,.14);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(80% 100% at 10% 0%,oklch(0.3 0.11 290 / .9),transparent 55%),radial-gradient(70% 90% at 95% 100%,oklch(0.28 0.1 250 / .9),transparent 55%),oklch(0.17 0.03 280);
}

.ssc-04 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 8px;
}

.ssc-04 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-04-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-04-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-04 .ssc-sr {
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

.ssc-04 .ssc-04__row {
  position: relative;
  width: min(640px,100%);
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(170px,1fr));
  gap: 16px;
}

.ssc-04 .ssc-04__widget {
  background: rgba(255,255,255,.05);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255,255,255,.11);
  border-radius: 18px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: 0 20px 44px -26px rgba(0,0,0,.7);
}

.ssc-04 .ssc-04__widget:nth-child(3) .ssc-sk::after {
  animation-delay: .09s;
}

.ssc-04 .ssc-04__widget:nth-child(4) .ssc-sk::after {
  animation-delay: .18s;
}

.ssc-04 .ssc-04__head {
  display: flex;
  align-items: center;
  gap: 10px;
}

.ssc-04 .ssc-04__icon {
  width: 38px;
  height: 38px;
  flex-shrink: 0;
  border-radius: 11px;
}

.ssc-04 .ssc-04__label {
  height: 10px;
}

.ssc-04 .ssc-04__value {
  height: 30px;
  border-radius: 9px;
  background: color-mix(in oklab,var(--violet) 26%,transparent);
}

.ssc-04 .ssc-04__trend {
  height: 9px;
}

@media (prefers-reduced-motion: reduce) {
  .ssc-04 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — skeleton geometry (tall tinted value bar vs. slim lines) previews the widget's hierarchy before data lands. */
```
