---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/single-satellite-orbit/"
title: "Single Satellite Orbiting Menu Toggle"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "One satellite button endlessly circles a planet-sized CTA, riding a CSS Motion Path — offset-path: circle() — with no keyframe math at all."
has_js: "false"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Single Satellite Orbiting Menu Toggle
Source: https://codefronts.com/navigation/css-circular-menus/single-satellite-orbit/

One satellite button endlessly circles a planet-sized CTA, riding a CSS Motion Path — offset-path: circle() — with no keyframe math at all. Hover the system and the satellite eases to a stop at 12 o'clock, ready to click. A striking attention magnet for a single secondary action: 'What's new', a chat bubble, a promo.
## HTML
```html
<section class="ccm-17" aria-label="Orbiting satellite toggle demo">
  <div class="ccm-17__stage">
    <div class="ccm-17__system">
      <span class="ccm-17__track" aria-hidden="true"></span>
      <button type="button" class="ccm-17__planet">Start free trial</button>
      <a class="ccm-17__sat" href="#whats-new"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4l1.8 4.6L18.5 10l-4.7 1.4L12 16l-1.8-4.6L5.5 10l4.7-1.4z"/></svg><span class="ccm-17__sr">What's new</span></a>
    </div>
    <p class="ccm-17__note">offset-path: circle() · hover to dock the satellite</p>
  </div>
</section>
```
## CSS
```css
.ccm-17,
.ccm-17 *,
.ccm-17 *::before,
.ccm-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-17 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(circle at 50% 40%,oklch(0.3 0.05 280),oklch(0.19 0.035 290) 75%);
  --brand: oklch(0.62 0.19 265);
  --star: oklch(0.8 0.16 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ccm-17__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: radial-gradient(circle at 50% 40%,oklch(0.3 0.05 280),oklch(0.19 0.035 290) 75%);
  overflow: hidden;
}

.ccm-17__system {
  position: relative;
  width: 240px;
  height: 240px;
  display: grid;
  place-items: center;
}

.ccm-17__track {
  position: absolute;
  inset: 28px;
  border-radius: 50%;
  border: 1px dashed oklch(0.65 0.08 280 / .35);
}

.ccm-17__planet {
  padding: 20px 30px;
  border: none;
  border-radius: 999px;
  background: linear-gradient(140deg,var(--brand),oklch(0.52 0.21 290));
  color: #fff;
  font: 700 16px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .01em;
  cursor: pointer;
  box-shadow: 0 18px 44px -14px oklch(0.5 0.2 275 / .8),inset 0 1px 0 oklch(1 0 0 / .25);
  transition: scale .25s;
}

.ccm-17__planet:hover {
  scale: 1.04;
}

.ccm-17__planet:focus-visible {
  outline: 3px solid var(--star);
  outline-offset: 4px;
}

.ccm-17__sat {
  position: absolute;
  left: 50%;
  top: calc(50% - 92px);
  margin: -23px;
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,oklch(0.88 0.14 85),oklch(0.72 0.16 70));
  color: oklch(0.3 0.06 70);
  box-shadow: 0 0 0 4px oklch(0.8 0.16 85 / .2),0 10px 24px -8px oklch(0.7 0.16 75 / .8);
  offset-path: circle(92px at 50% 50%);
  offset-rotate: 0deg;
  offset-distance: var(--park,0%);
  animation: ccm17-orbit 10s linear infinite;
  transition: offset-distance .8s cubic-bezier(.3,1,.35,1),scale .25s;
}

.ccm-17__sat svg {
  width: 22px;
  height: 22px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.6;
  stroke-linejoin: round;
}

.ccm-17__system:hover .ccm-17__sat,
.ccm-17__system:focus-within .ccm-17__sat {
  animation-play-state: paused;
  offset-distance: 0%;
  scale: 1.12;
}

.ccm-17__sat:focus-visible {
  outline: 3px solid var(--star);
  outline-offset: 3px;
}

.ccm-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-17__note {
  position: absolute;
  bottom: 20px;
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.7 0.06 280 / .55);
}

@keyframes ccm17-orbit {
  from {
    offset-distance: 0%;
  }

  to {
    offset-distance: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ccm-17__sat {
    animation: none;
  }
}
```
