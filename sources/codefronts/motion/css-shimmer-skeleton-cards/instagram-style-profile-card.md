---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/instagram-style-profile-card/"
title: "Instagram-Style Profile Card"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A social profile header skeleton on dark glass: a large avatar wrapped in a live conic-gradient story ring, beside staggered-width text lines and a…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Instagram-Style Profile Card
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/instagram-style-profile-card/

A social profile header skeleton on dark glass: a large avatar wrapped in a live conic-gradient story ring, beside staggered-width text lines and a follower-stats row. The frosted card floats on an oklch aurora mesh — proof that a loading state can carry brand personality instead of defaulting to gray-on-white.
## HTML
```html
<section class="ssc-01" aria-label="Instagram-style profile card skeleton demo">
  <div class="ssc-01__card" role="status" aria-busy="true">
    <span class="ssc-sr">Loading profile…</span>
    <div aria-hidden="true">
      <div class="ssc-01__top">
        <div class="ssc-01__ring"><div class="ssc-sk ssc-01__avatar"></div></div>
        <div class="ssc-01__lines">
          <div class="ssc-sk ssc-01__line" style="width:60%"></div>
          <div class="ssc-sk ssc-01__line ssc-01__line--thin" style="width:90%"></div>
          <div class="ssc-sk ssc-01__line ssc-01__line--thin" style="width:40%"></div>
        </div>
      </div>
      <div class="ssc-01__stats">
        <div class="ssc-sk ssc-01__stat"></div>
        <div class="ssc-sk ssc-01__stat"></div>
        <div class="ssc-sk ssc-01__stat"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-01,
.ssc-01 *,
.ssc-01 *::before,
.ssc-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-01 {
  --ring-a: oklch(0.72 0.19 350);
  --ring-b: oklch(0.65 0.2 290);
  --sk-bg: rgba(255,255,255,.07);
  --sk-shine: rgba(255,255,255,.13);
  --avatar: 72px;
  --ring-speed: 6s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(90% 90% at 12% 8%,oklch(0.28 0.09 320 / .9),transparent 60%),radial-gradient(80% 90% at 92% 92%,oklch(0.26 0.08 260 / .9),transparent 60%),oklch(0.16 0.02 300);
}

.ssc-01 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 8px;
}

.ssc-01 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-01-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-01-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-01 .ssc-sr {
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

.ssc-01 .ssc-01__card {
  position: relative;
  width: min(360px,100%);
  background: rgba(255,255,255,.05);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 22px;
  padding: 24px;
  box-shadow: 0 24px 60px -24px rgba(0,0,0,.6);
}

.ssc-01 .ssc-01__top {
  display: flex;
  align-items: center;
  gap: 18px;
}

.ssc-01 .ssc-01__ring {
  width: calc(var(--avatar) + 8px);
  height: calc(var(--avatar) + 8px);
  flex-shrink: 0;
  padding: 3px;
  border-radius: 50%;
  background: conic-gradient(from var(--a,0deg),var(--ring-a),var(--ring-b),var(--ring-a));
  animation: ssc-01-ring var(--ring-speed) linear infinite;
  display: grid;
  place-items: center;
}

@property --a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@keyframes ssc-01-ring {
  100% {
    --a: 360deg;
  }
}

.ssc-01 .ssc-01__avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 3px solid oklch(0.18 0.03 300);
  background: linear-gradient(var(--sk-bg),var(--sk-bg)) padding-box,oklch(0.22 0.03 300);
}

.ssc-01 .ssc-01__lines {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ssc-01 .ssc-01__line {
  height: 14px;
}

.ssc-01 .ssc-01__line--thin {
  height: 10px;
}

.ssc-01 .ssc-01__stats {
  display: flex;
  gap: 12px;
  margin-top: 22px;
}

.ssc-01 .ssc-01__stat {
  flex: 1;
  height: 36px;
  border-radius: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .ssc-01 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }

  .ssc-01__ring {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one .ssc-sk base class + a translateX keyframe shimmers every block; @property animates the conic ring's angle. */
```
