---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-loading-skeleton/"
title: "Liquid Glass Loading Skeleton"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A profile-card skeleton that upgrades dull grey blocks to glass: translucent placeholder shapes with a diagonal liquid-light shimmer sweeping across them,…"
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Loading Skeleton
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-loading-skeleton/

A profile-card skeleton that upgrades dull grey blocks to glass: translucent placeholder shapes with a diagonal liquid-light shimmer sweeping across them, keeping users engaged while data loads. Pure CSS, zero layout shift when the real content swaps in.
## HTML
```html
<section class="lg-19" aria-label="Liquid glass loading skeleton">
  <div class="lg-19__card" aria-busy="true">
    <span class="lg-19__sr">Loading profile…</span>
    <div class="lg-19__head"><div class="lg-19__avatar"></div><div class="lg-19__hlines"><div class="lg-19__bar lg-19__bar--title"></div><div class="lg-19__bar lg-19__bar--sub"></div></div></div>
    <div class="lg-19__bar lg-19__bar--line"></div>
    <div class="lg-19__bar lg-19__bar--line"></div>
    <div class="lg-19__bar lg-19__bar--line lg-19__bar--short"></div>
    <div class="lg-19__foot"><div class="lg-19__chip"></div><div class="lg-19__btn"></div></div>
  </div>
</section>
```
## CSS
```css
.lg-19,
.lg-19 *,
.lg-19 *::before,
.lg-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-19 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: url('https://picsum.photos/seed/lgskel/1100/800') center/cover fixed,#161225;
}

.lg-19__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.lg-19__card {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  width: min(360px,92vw);
  padding: 26px;
  border-radius: 24px;
  background: color-mix(in oklab,white 9%,transparent);
  border: 1px solid rgba(255,255,255,.24);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35),0 30px 60px -30px rgba(0,0,0,.6);
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
}

.lg-19__card::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(105deg,transparent 30%,rgba(255,255,255,.28) 48%,transparent 66%);
  transform: translateX(-100%);
  animation: lg-19-sweep 1.6s ease-in-out infinite;
  pointer-events: none;
  z-index: 2;
}

.lg-19__head {
  display: flex;
  gap: 16px;
  align-items: center;
  margin-bottom: 22px;
}

.lg-19__avatar {
  width: 60px;
  height: 60px;
  flex: none;
  border-radius: 50%;
}

.lg-19__hlines {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.lg-19__avatar,
.lg-19__bar,
.lg-19__chip,
.lg-19__btn {
  background: color-mix(in oklab,white 16%,transparent);
  border: 1px solid rgba(255,255,255,.15);
  border-radius: 8px;
}

.lg-19__bar {
  height: 12px;
}

.lg-19__bar--title {
  width: 65%;
  height: 16px;
}

.lg-19__bar--sub {
  width: 40%;
  height: 12px;
}

.lg-19__bar--line {
  margin-bottom: 12px;
  border-radius: 6px;
}

.lg-19__bar--short {
  width: 55%;
}

.lg-19__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 18px;
}

.lg-19__chip {
  width: 84px;
  height: 28px;
  border-radius: 999px;
}

.lg-19__btn {
  width: 110px;
  height: 40px;
  border-radius: 12px;
}

@keyframes lg-19-sweep {
  0% {
    transform: translateX(-100%);
  }

  60%,
    100% {
    transform: translateX(100%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-19__card::after {
    animation: none;
    opacity: .15;
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — placeholders mirror the final layout (zero CLS) and one card-wide diagonal ::after gradient sweeps on a transform loop for the liquid-light shimmer; aria-busy announces loading. */
```
