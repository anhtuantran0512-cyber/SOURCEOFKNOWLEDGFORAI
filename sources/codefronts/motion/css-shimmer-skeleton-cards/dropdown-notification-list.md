---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/dropdown-notification-list/"
title: "Dropdown Notification List"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A notification-tray skeleton as a floating dark glass dropdown — pointer notch included: a compact header row, then four tight rows of avatar circle + text…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dropdown Notification List
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/dropdown-notification-list/

A notification-tray skeleton as a floating dark glass dropdown — pointer notch included: a compact header row, then four tight rows of avatar circle + text line, one carrying an unread accent dot. Built with flex gap end-to-end so the rows stay crisply separated at trays of any density.
## HTML
```html
<section class="ssc-14" aria-label="Notification dropdown skeleton demo">
  <div class="ssc-14__panel" role="status" aria-busy="true">
    <span class="ssc-sr">Loading notifications…</span>
    <div aria-hidden="true">
      <div class="ssc-14__head">
        <div class="ssc-sk ssc-14__title" style="width:44%"></div>
        <div class="ssc-sk ssc-14__action" style="width:20%"></div>
      </div>
      <div class="ssc-14__row">
        <div class="ssc-14__dotwrap"><div class="ssc-sk ssc-14__avatar"></div><i class="ssc-14__unread"></i></div>
        <div class="ssc-sk ssc-14__line" style="width:82%"></div>
      </div>
      <div class="ssc-14__row">
        <div class="ssc-14__dotwrap"><div class="ssc-sk ssc-14__avatar"></div></div>
        <div class="ssc-sk ssc-14__line" style="width:64%"></div>
      </div>
      <div class="ssc-14__row">
        <div class="ssc-14__dotwrap"><div class="ssc-sk ssc-14__avatar"></div></div>
        <div class="ssc-sk ssc-14__line" style="width:74%"></div>
      </div>
      <div class="ssc-14__row">
        <div class="ssc-14__dotwrap"><div class="ssc-sk ssc-14__avatar"></div></div>
        <div class="ssc-sk ssc-14__line" style="width:56%"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-14,
.ssc-14 *,
.ssc-14 *::before,
.ssc-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-14 {
  --accent: oklch(0.7 0.19 25);
  --sk-bg: rgba(255,255,255,.08);
  --sk-shine: rgba(255,255,255,.13);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px 48px;
  background: radial-gradient(90% 100% at 50% 0%,oklch(0.25 0.04 260 / .8),transparent 65%),oklch(0.16 0.02 255);
}

.ssc-14 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 7px;
}

.ssc-14 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-14-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-14-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-14 .ssc-sr {
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

.ssc-14 .ssc-14__panel {
  position: relative;
  width: min(320px,100%);
  background: rgba(30,34,48,.75);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 16px;
  padding: 16px;
  box-shadow: 0 28px 60px -28px rgba(0,0,0,.85);
}

.ssc-14 .ssc-14__panel::before {
  content: "";
  position: absolute;
  top: -7px;
  left: 36px;
  width: 13px;
  height: 13px;
  transform: rotate(45deg);
  background: rgba(30,34,48,.75);
  border-left: 1px solid rgba(255,255,255,.12);
  border-top: 1px solid rgba(255,255,255,.12);
}

.ssc-14 .ssc-14__panel>div[aria-hidden] {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ssc-14 .ssc-14__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255,255,255,.09);
}

.ssc-14 .ssc-14__title {
  height: 12px;
}

.ssc-14 .ssc-14__action {
  height: 9px;
  border-radius: 999px;
}

.ssc-14 .ssc-14__row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ssc-14 .ssc-14__row:nth-child(3) .ssc-sk::after {
  animation-delay: .08s;
}

.ssc-14 .ssc-14__row:nth-child(4) .ssc-sk::after {
  animation-delay: .16s;
}

.ssc-14 .ssc-14__row:nth-child(5) .ssc-sk::after {
  animation-delay: .24s;
}

.ssc-14 .ssc-14__dotwrap {
  position: relative;
  flex-shrink: 0;
}

.ssc-14 .ssc-14__avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
}

.ssc-14 .ssc-14__unread {
  position: absolute;
  top: -2px;
  right: -2px;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--accent);
  border: 2px solid rgba(30,34,48,1);
}

.ssc-14 .ssc-14__line {
  height: 10px;
  border-radius: 999px;
}

@media (prefers-reduced-motion: reduce) {
  .ssc-14 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — a rotated ::before square draws the dropdown notch; flex gap keeps the tray rhythm; the unread dot stays steady. */
```
