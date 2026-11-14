---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/mobile-feed-horizontal-scroll/"
title: "Mobile Feed (Horizontal Scroll)"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A stories-rail skeleton on near-black: an overflow-x scroller of square tiles, each wrapped in a sunset conic-gradient ring, with a caption line beneath."
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile Feed (Horizontal Scroll)
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/mobile-feed-horizontal-scroll/

A stories-rail skeleton on near-black: an overflow-x scroller of square tiles, each wrapped in a sunset conic-gradient ring, with a caption line beneath. Tiles are flex-shrink:0 so they never squash, the rail scroll-snaps, and its edges fade out with a CSS mask — the premium overflow hint big social apps use.
## HTML
```html
<section class="ssc-08" aria-label="Mobile horizontal feed skeleton demo">
  <div class="ssc-08__phone" role="status" aria-busy="true">
    <span class="ssc-sr">Loading feed…</span>
    <div class="ssc-08__rail" aria-hidden="true">
      <div class="ssc-08__story"><div class="ssc-08__ring"><div class="ssc-sk ssc-08__tile"></div></div><div class="ssc-sk ssc-08__cap" style="width:70%"></div></div>
      <div class="ssc-08__story"><div class="ssc-08__ring"><div class="ssc-sk ssc-08__tile"></div></div><div class="ssc-sk ssc-08__cap" style="width:55%"></div></div>
      <div class="ssc-08__story"><div class="ssc-08__ring"><div class="ssc-sk ssc-08__tile"></div></div><div class="ssc-sk ssc-08__cap" style="width:80%"></div></div>
      <div class="ssc-08__story"><div class="ssc-08__ring"><div class="ssc-sk ssc-08__tile"></div></div><div class="ssc-sk ssc-08__cap" style="width:62%"></div></div>
      <div class="ssc-08__story"><div class="ssc-08__ring"><div class="ssc-sk ssc-08__tile"></div></div><div class="ssc-sk ssc-08__cap" style="width:74%"></div></div>
      <div class="ssc-08__story"><div class="ssc-08__ring"><div class="ssc-sk ssc-08__tile"></div></div><div class="ssc-sk ssc-08__cap" style="width:48%"></div></div>
      <div class="ssc-08__story"><div class="ssc-08__ring"><div class="ssc-sk ssc-08__tile"></div></div><div class="ssc-sk ssc-08__cap" style="width:66%"></div></div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-08,
.ssc-08 *,
.ssc-08 *::before,
.ssc-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-08 {
  --ring-a: oklch(0.75 0.17 45);
  --ring-b: oklch(0.62 0.24 350);
  --sk-bg: rgba(255,255,255,.07);
  --sk-shine: rgba(255,255,255,.13);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% -10%,oklch(0.24 0.05 330 / .8),transparent 60%),oklch(0.14 0.015 320);
}

.ssc-08 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 10px;
}

.ssc-08 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-08-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-08-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-08 .ssc-sr {
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

.ssc-08 .ssc-08__phone {
  position: relative;
  width: min(380px,100%);
  background: rgba(255,255,255,.04);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 24px;
  padding: 18px 0;
  box-shadow: 0 24px 54px -30px rgba(0,0,0,.8);
}

.ssc-08 .ssc-08__rail {
  display: flex;
  gap: 14px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: 0 20px 6px;
  scrollbar-width: none;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 24px,#000 calc(100% - 24px),transparent);
  mask-image: linear-gradient(90deg,transparent,#000 24px,#000 calc(100% - 24px),transparent);
}

.ssc-08 .ssc-08__rail::-webkit-scrollbar {
  height: 0;
}

.ssc-08 .ssc-08__story {
  flex-shrink: 0;
  width: 92px;
  scroll-snap-align: start;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.ssc-08 .ssc-08__story:nth-child(2) .ssc-sk::after {
  animation-delay: .08s;
}

.ssc-08 .ssc-08__story:nth-child(3) .ssc-sk::after {
  animation-delay: .16s;
}

.ssc-08 .ssc-08__story:nth-child(4) .ssc-sk::after {
  animation-delay: .24s;
}

.ssc-08 .ssc-08__story:nth-child(5) .ssc-sk::after {
  animation-delay: .32s;
}

.ssc-08 .ssc-08__story:nth-child(6) .ssc-sk::after {
  animation-delay: .4s;
}

.ssc-08 .ssc-08__story:nth-child(7) .ssc-sk::after {
  animation-delay: .48s;
}

.ssc-08 .ssc-08__ring {
  padding: 2px;
  border-radius: 16px;
  background: conic-gradient(from 210deg,var(--ring-a),var(--ring-b),var(--ring-a));
}

.ssc-08 .ssc-08__tile {
  width: 100%;
  aspect-ratio: 1;
  border-radius: 14px;
  border: 2px solid oklch(0.16 0.02 320);
  background: linear-gradient(var(--sk-bg),var(--sk-bg)) padding-box,oklch(0.2 0.025 320);
}

.ssc-08 .ssc-08__cap {
  height: 9px;
  border-radius: 999px;
  margin: 0 auto;
}

.ssc-08 .ssc-08__cap {
  width: 70%;
}

@media (prefers-reduced-motion: reduce) {
  .ssc-08 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — flex-shrink:0 keeps tiles rigid, conic rings brand them, and a mask-image edge fade invites the swipe. */
```
