---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/skeleton-loading-shimmer-profile-card/"
title: "Skeleton Loading Shimmer Profile Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "The placeholder state of a profile card, with grey blocks for avatar, name, bio and buttons swept by a looping shimmer while data loads."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skeleton Loading Shimmer Profile Card
Source: https://codefronts.com/components/css-profile-cards/skeleton-loading-shimmer-profile-card/

The placeholder state of a profile card, with grey blocks for avatar, name, bio and buttons swept by a looping shimmer while data loads.
## HTML
```html
<div class="pc-06">
  <div class="pc-06__card">
    <div class="pc-06__shimmer pc-06__pfp"></div>
    <div class="pc-06__lines">
      <div class="pc-06__shimmer pc-06__l1"></div>
      <div class="pc-06__shimmer pc-06__l2"></div>
    </div>
    <div class="pc-06__block pc-06__shimmer"></div>
    <div class="pc-06__chips">
      <div class="pc-06__shimmer pc-06__chip"></div>
      <div class="pc-06__shimmer pc-06__chip"></div>
      <div class="pc-06__shimmer pc-06__chip"></div>
    </div>
    <div class="pc-06__foot">
      <div class="pc-06__shimmer pc-06__btn"></div>
      <div class="pc-06__shimmer pc-06__btn pc-06__btn--sm"></div>
    </div>
    <span class="pc-06__tag">Loading profile&#8230;</span>
  </div>
</div>
```
## CSS
```css
.pc-06,
.pc-06 *,
.pc-06 *::before,
.pc-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-06 ::selection {
  background: #3a4a6a;
  color: #fff;
}

.pc-06 {
  --skel: #1b2130;
  --hi: #2d3750;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #0c0f16;
  color: #7a879f;
}

.pc-06__card {
  width: 300px;
  border-radius: 22px;
  padding: 26px;
  background: #111623;
  border: 1px solid #1c2333;
  box-shadow: 0 24px 60px -26px rgba(0,0,0,.8);
  position: relative;
}

.pc-06__shimmer {
  position: relative;
  overflow: hidden;
  background: var(--skel);
  border-radius: 10px;
}

.pc-06__shimmer::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,transparent,var(--hi),transparent);
  transform: translateX(-100%);
  animation: pc-06-shim 1.5s ease-in-out infinite;
}

@keyframes pc-06-shim {
  100% {
    transform: translateX(100%);
  }
}

.pc-06__pfp {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  margin-bottom: 18px;
}

.pc-06__lines {
  display: flex;
  flex-direction: column;
  gap: 9px;
  margin-bottom: 20px;
}

.pc-06__l1 {
  height: 16px;
  width: 65%;
}

.pc-06__l2 {
  height: 12px;
  width: 42%;
}

.pc-06__block {
  height: 56px;
  width: 100%;
  margin-bottom: 18px;
}

.pc-06__chips {
  display: flex;
  gap: 8px;
  margin-bottom: 22px;
}

.pc-06__chip {
  height: 26px;
  width: 60px;
  border-radius: 8px;
}

.pc-06__foot {
  display: flex;
  gap: 10px;
}

.pc-06__btn {
  height: 42px;
  flex: 1;
  border-radius: 12px;
}

.pc-06__btn--sm {
  flex: 0 0 46px;
}

.pc-06__tag {
  display: block;
  text-align: center;
  margin-top: 18px;
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #3f4a63;
  animation: pc-06-pulse 1.5s ease-in-out infinite;
}

@keyframes pc-06-pulse {
  0%,
    100% {
    opacity: .4;
  }

  50% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pc-06__shimmer::after {
    animation: none;
    opacity: .3;
  }

  .pc-06__tag {
    animation: none;
  }
}
```
