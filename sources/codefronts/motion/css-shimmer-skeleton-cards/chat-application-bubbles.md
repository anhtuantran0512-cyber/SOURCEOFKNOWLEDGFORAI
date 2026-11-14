---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/chat-application-bubbles/"
title: "Chat Application Bubbles"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A midnight messenger skeleton: incoming rows pair an avatar with a bubble cornered 18px 18px 18px 4px, outgoing rows float right with the mirrored 18px 18px…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Chat Application Bubbles
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/chat-application-bubbles/

A midnight messenger skeleton: incoming rows pair an avatar with a bubble cornered 18px 18px 18px 4px, outgoing rows float right with the mirrored 18px 18px 4px 18px radius and an accent-tinted fill. The asymmetric corners alone tell users which side is "them" before a single message arrives.
## HTML
```html
<section class="ssc-12" aria-label="Chat bubbles skeleton demo">
  <div class="ssc-12__thread" role="status" aria-busy="true">
    <span class="ssc-sr">Loading conversation…</span>
    <div aria-hidden="true">
      <div class="ssc-12__row">
        <div class="ssc-sk ssc-12__avatar"></div>
        <div class="ssc-sk ssc-12__bubble ssc-12__bubble--in" style="width:55%"></div>
      </div>
      <div class="ssc-12__row ssc-12__row--out">
        <div class="ssc-sk ssc-12__bubble ssc-12__bubble--out" style="width:44%"></div>
      </div>
      <div class="ssc-12__row">
        <div class="ssc-sk ssc-12__avatar"></div>
        <div class="ssc-sk ssc-12__bubble ssc-12__bubble--in ssc-12__bubble--tall" style="width:62%"></div>
      </div>
      <div class="ssc-12__row ssc-12__row--out">
        <div class="ssc-sk ssc-12__bubble ssc-12__bubble--out" style="width:34%"></div>
      </div>
      <div class="ssc-12__row">
        <div class="ssc-sk ssc-12__avatar"></div>
        <div class="ssc-12__typing"><i></i><i></i><i></i></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-12,
.ssc-12 *,
.ssc-12 *::before,
.ssc-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-12 {
  --accent: oklch(0.6 0.19 265);
  --sk-bg: rgba(255,255,255,.08);
  --sk-shine: rgba(255,255,255,.13);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 120% at 90% 0%,oklch(0.22 0.05 275 / .9),transparent 60%),oklch(0.15 0.02 265);
}

.ssc-12 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
}

.ssc-12 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-12-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-12-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-12 .ssc-sr {
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

.ssc-12 .ssc-12__thread {
  position: relative;
  width: min(420px,100%);
  background: rgba(255,255,255,.04);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255,255,255,.1);
  border-radius: 22px;
  padding: 22px;
  box-shadow: 0 24px 54px -30px rgba(0,0,0,.75);
}

.ssc-12 .ssc-12__thread>div[aria-hidden] {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ssc-12 .ssc-12__row {
  display: flex;
  align-items: flex-end;
  gap: 10px;
}

.ssc-12 .ssc-12__row--out {
  justify-content: flex-end;
}

.ssc-12 .ssc-12__row:nth-child(2) .ssc-sk::after {
  animation-delay: .12s;
}

.ssc-12 .ssc-12__row:nth-child(3) .ssc-sk::after {
  animation-delay: .24s;
}

.ssc-12 .ssc-12__row:nth-child(4) .ssc-sk::after {
  animation-delay: .36s;
}

.ssc-12 .ssc-12__avatar {
  width: 30px;
  height: 30px;
  flex-shrink: 0;
  border-radius: 50%;
}

.ssc-12 .ssc-12__bubble {
  height: 38px;
}

.ssc-12 .ssc-12__bubble--tall {
  height: 56px;
}

.ssc-12 .ssc-12__bubble--in {
  border-radius: 18px 18px 18px 4px;
}

.ssc-12 .ssc-12__bubble--out {
  border-radius: 18px 18px 4px 18px;
  background: color-mix(in oklab,var(--accent) 30%,rgba(255,255,255,.08));
}

.ssc-12 .ssc-12__typing {
  display: flex;
  gap: 5px;
  padding: 12px 16px;
  border-radius: 18px 18px 18px 4px;
  background: var(--sk-bg);
}

.ssc-12 .ssc-12__typing i {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: rgba(255,255,255,.35);
  animation: ssc-12-dot 1.2s ease-in-out infinite;
}

.ssc-12 .ssc-12__typing i:nth-child(2) {
  animation-delay: .15s;
}

.ssc-12 .ssc-12__typing i:nth-child(3) {
  animation-delay: .3s;
}

@keyframes ssc-12-dot {
  30% {
    transform: translateY(-4px);
    opacity: 1;
  }

  0%,
    60%,
    100% {
    transform: translateY(0);
    opacity: .5;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ssc-12 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }

  .ssc-12__typing i {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — border-radius asymmetry draws the bubble tails; color-mix tints the outgoing side; CSS dots type away. */
```
