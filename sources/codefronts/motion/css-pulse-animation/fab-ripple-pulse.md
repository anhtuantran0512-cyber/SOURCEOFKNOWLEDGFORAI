---
source: "codefronts"
url: "https://codefronts.com/motion/css-pulse-animation/fab-ripple-pulse/"
title: "FAB Ripple Pulse"
section: "motion"
category: "css-pulse-animation"
category_name: "CSS Pulse Animations"
description: "A floating action button (FAB) with an outward ripple pulse for mobile app dashboards — the sticky bottom-right \"+\" or \"chat support\" button that draws…"
has_js: "false"
---

Here's a working CSS Pulse Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: FAB Ripple Pulse
Source: https://codefronts.com/motion/css-pulse-animation/fab-ripple-pulse/

A floating action button (FAB) with an outward ripple pulse for mobile app dashboards — the sticky bottom-right "+" or "chat support" button that draws attention to the primary action hub. Warm off-white iOS consumer app palette with coral #ff6b6b FAB, mock dashboard content behind (feed cards, avatar bar), FAB positioned absolute; bottom: 24px; right: 24px. The ripple uses dual ::before and ::after pseudo-elements with staggered animation-delay for a continuous concentric outward wave.
## HTML
```html
<div class="pl-02">
  <div class="pl-02__header">
    <span class="pl-02__avatar" aria-hidden="true">A</span>
    <div class="pl-02__title">
      <strong>Today</strong>
      <span>Tue, Jul 8</span>
    </div>
    <span class="pl-02__bell" aria-hidden="true">🔔</span>
  </div>
  <div class="pl-02__feed">
    <div class="pl-02__card">
      <div class="pl-02__card-head">
        <span class="pl-02__dot pl-02__dot--pink" aria-hidden="true"></span>
        <span>Design review</span>
      </div>
      <p>Two comments on your mobile mockups — Sam and Priya.</p>
    </div>
    <div class="pl-02__card">
      <div class="pl-02__card-head">
        <span class="pl-02__dot pl-02__dot--amber" aria-hidden="true"></span>
        <span>Reminder</span>
      </div>
      <p>Standup at 10:00 · Zoom link auto-attached.</p>
    </div>
    <div class="pl-02__card">
      <div class="pl-02__card-head">
        <span class="pl-02__dot pl-02__dot--mint" aria-hidden="true"></span>
        <span>Task done</span>
      </div>
      <p>Onboarding flow shipped — 4 tickets closed.</p>
    </div>
  </div>
  <button class="pl-02__fab" type="button" aria-label="Create new post">
    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true">
      <line x1="12" y1="5" x2="12" y2="19"/>
      <line x1="5" y1="12" x2="19" y2="12"/>
    </svg>
  </button>
</div>
```
## CSS
```css
.pl-02 {
  --bg: #faf7f0;
  --surface: #ffffff;
  --ink: #1c1917;
  --sub: #78716c;
  --accent: #ff6b6b;
  --accent-dark: #e05252;
  --line: #eee8dc;
  font-family: -apple-system,BlinkMacSystemFont,'SF Pro Display','Segoe UI',sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 32px;
  background: var(--bg);
  color: var(--ink);
}

.pl-02 *,
.pl-02 *::before,
.pl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pl-02 ::selection {
  background: var(--accent);
  color: #fff;
}

.pl-02__header {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 18px;
  border-radius: 14px;
  background: var(--surface);
  box-shadow: 0 4px 12px -6px rgba(28,25,23,.12);
  margin-bottom: 16px;
}

.pl-02__avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: linear-gradient(135deg,#f472b6,#e879f9);
  color: #fff;
  font-size: .9rem;
  font-weight: 700;
}

.pl-02__title {
  flex: 1;
  display: flex;
  flex-direction: column;
  line-height: 1.15;
}

.pl-02__title strong {
  font-size: 1rem;
  font-weight: 700;
}

.pl-02__title span {
  font-size: .75rem;
  color: var(--sub);
  margin-top: 1px;
}

.pl-02__bell {
  font-size: 18px;
}

.pl-02__feed {
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}

.pl-02__card {
  padding: 14px 16px;
  border-radius: 14px;
  background: var(--surface);
  box-shadow: 0 2px 8px -4px rgba(28,25,23,.08);
}

.pl-02__card-head {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .02em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 6px;
}

.pl-02__dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  flex-shrink: 0;
}

.pl-02__dot--pink {
  background: #ec4899;
}

.pl-02__dot--amber {
  background: #f59e0b;
}

.pl-02__dot--mint {
  background: #10b981;
}

.pl-02__card p {
  font-size: .85rem;
  color: var(--ink);
  line-height: 1.45;
}
/* FAB — pinned bottom-right with ripple pulse */

.pl-02__fab {
  position: absolute;
  bottom: 24px;
  right: 24px;
  width: 56px;
  height: 56px;
  border: none;
  border-radius: 50%;
  background: var(--accent);
  color: #fff;
  cursor: pointer;
  box-shadow: 0 8px 24px -6px rgba(255,107,107,.55),0 2px 4px rgba(28,25,23,.12);
  transition: transform .15s ease,background .18s ease;
  z-index: 2;
}

.pl-02__fab:hover {
  background: var(--accent-dark);
  transform: translateY(-1px);
}

.pl-02__fab:active {
  transform: translateY(1px);
}

.pl-02__fab:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.pl-02__fab svg {
  position: relative;
  z-index: 1;
}
/* Ripple rings — two pseudo-elements, staggered animation-delay */

.pl-02__fab::before,
.pl-02__fab::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: var(--accent);
  pointer-events: none;
  z-index: 0;
  animation: pl-02-ripple 1.8s ease-out infinite;
}

.pl-02__fab::after {
  animation-delay: .9s;
}

@keyframes pl-02-ripple {
  0% {
    transform: scale(1);
    opacity: .5;
  }

  70% {
    transform: scale(2);
    opacity: 0;
  }

  100% {
    transform: scale(2.2);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pl-02__fab::before,
    .pl-02__fab::after {
    animation: none!important;
  }
}
```
