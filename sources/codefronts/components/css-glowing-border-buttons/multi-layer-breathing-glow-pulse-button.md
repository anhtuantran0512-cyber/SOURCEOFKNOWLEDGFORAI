---
source: "codefronts"
url: "https://codefronts.com/components/css-glowing-border-buttons/multi-layer-breathing-glow-pulse-button/"
title: "Multi-Layer Breathing Glow Pulse Button"
section: "components"
category: "css-glowing-border-buttons"
category_name: "CSS Glowing Border Buttons"
description: "The attention magnet for live demos and expiring offers: with no interaction at all, a sonar ring expands and dissolves from the button's edge every 2.2…"
has_js: "false"
---

Here's a working CSS Glowing Border Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Layer Breathing Glow Pulse Button
Source: https://codefronts.com/components/css-glowing-border-buttons/multi-layer-breathing-glow-pulse-button/

The attention magnet for live demos and expiring offers: with no interaction at all, a sonar ring expands and dissolves from the button's edge every 2.2 seconds while the border glow breathes underneath on an offset rhythm. Two desynchronized loops read as 'alive', not 'blinking'.
## HTML
```html
<section class="gbb-09" aria-label="Breathing pulse glow button demo">
  <div class="gbb-09__stack">
    <span class="gbb-09__badge">2 seats left</span>
    <button class="gbb-09__btn" type="button">Claim Your Spot</button>
  </div>
</section>
```
## CSS
```css
.gbb-09,
.gbb-09 *,
.gbb-09 *::before,
.gbb-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gbb-09 {
  --pulse: oklch(0.7 0.19 35);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(60% 70% at 50% 100%,oklch(0.2 0.05 35 / .5),transparent 60%),oklch(0.13 0.015 270);
}

.gbb-09 .gbb-09__stack {
  display: grid;
  justify-items: center;
  gap: 14px;
}

.gbb-09 .gbb-09__badge {
  font: 700 11px/1 'Segoe UI',system-ui,sans-serif;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--pulse);
  border: 1px solid color-mix(in oklab,var(--pulse) 45%,transparent);
  border-radius: 999px;
  padding: 6px 12px;
  background: color-mix(in oklab,var(--pulse) 10%,transparent);
}

.gbb-09 .gbb-09__btn {
  position: relative;
  cursor: pointer;
  border: 2px solid var(--pulse);
  border-radius: 999px;
  padding: 16px 38px;
  font: 700 15px/1 'Segoe UI',system-ui,sans-serif;
  color: #fff;
  background: color-mix(in oklab,var(--pulse) 16%,oklch(0.16 0.02 270));
  animation: gbb09-breathe 3.4s ease-in-out infinite;
  transition: box-shadow .25s ease;
}

.gbb-09 .gbb-09__btn::after {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: inherit;
  border: 2px solid var(--pulse);
  pointer-events: none;
  animation: gbb09-ping 2.2s cubic-bezier(.2,.6,.35,1) infinite;
}

.gbb-09 .gbb-09__btn:hover,
.gbb-09 .gbb-09__btn:focus-visible {
  animation: none;
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--pulse) 25%,transparent),0 0 44px color-mix(in oklab,var(--pulse) 55%,transparent);
}

.gbb-09 .gbb-09__btn:hover::after,
.gbb-09 .gbb-09__btn:focus-visible::after {
  animation-play-state: paused;
  opacity: 0;
}

.gbb-09 .gbb-09__btn:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 5px;
}

.gbb-09 .gbb-09__btn:active {
  transform: scale(.97);
}

@keyframes gbb09-breathe {
  0%,
    100% {
    box-shadow: 0 0 14px color-mix(in oklab,var(--pulse) 35%,transparent);
  }

  50% {
    box-shadow: 0 0 34px color-mix(in oklab,var(--pulse) 55%,transparent);
  }
}

@keyframes gbb09-ping {
  0% {
    transform: scale(1);
    opacity: .8;
  }

  70%,
    100% {
    transform: scale(1.28);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gbb-09 .gbb-09__btn {
    animation: none;
    box-shadow: 0 0 24px color-mix(in oklab,var(--pulse) 45%,transparent);
  }

  .gbb-09 .gbb-09__btn::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — a compositor-only sonar ring (scale+opacity) and a slower box-shadow breath run at co-prime durations so the rhythm never mechanizes. */
```
