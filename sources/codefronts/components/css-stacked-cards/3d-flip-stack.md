---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/3d-flip-stack/"
title: "3D Flip Stack"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "The active card turns a crisp 180° around its Y-axis on hover to reveal hidden utility buttons or pricing on its reverse, with the rest of the deck peeking…"
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Stack
Source: https://codefronts.com/components/css-stacked-cards/3d-flip-stack/

The active card turns a crisp 180° around its Y-axis on hover to reveal hidden utility buttons or pricing on its reverse, with the rest of the deck peeking behind. A classic flip-to-reveal, hardware-accelerated and pure CSS.
## HTML
```html
<section class="scd-23" aria-label="3D flip card stack">
  <div class="scd-23__scene">
    <div class="scd-23__back" aria-hidden="true" style="--i:2"></div>
    <div class="scd-23__back" aria-hidden="true" style="--i:1"></div>
    <div class="scd-23__flip" tabindex="0">
      <div class="scd-23__inner">
        <div class="scd-23__face scd-23__front"><p class="scd-23__k">Pro plan</p><h3>$24<small>/mo</small></h3><p class="scd-23__d">Hover to see what's inside →</p></div>
        <div class="scd-23__face scd-23__rear"><ul><li>Unlimited projects</li><li>Priority support</li><li>SSO &amp; audit log</li></ul><button>Start trial</button></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.scd-23,
.scd-23 *,
.scd-23 *::before,
.scd-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-23 {
  --accent: oklch(0.66 0.16 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #0f1119;
}

.scd-23__scene {
  position: relative;
  width: min(280px,90vw);
  height: 240px;
  perspective: 1200px;
}

.scd-23__back {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  background: #1c1f2b;
  border: 1px solid #2b2f3d;
  transform: translate(calc(var(--i) * 10px),calc(var(--i) * 10px)) scale(calc(1 - var(--i) * .04));
  box-shadow: 0 18px 34px -22px rgba(0,0,0,.8);
}

.scd-23__flip {
  position: absolute;
  inset: 0;
  z-index: 5;
  outline: none;
}

.scd-23__inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform .6s cubic-bezier(.3,.9,.3,1);
}

.scd-23__flip:hover .scd-23__inner,
.scd-23__flip:focus-visible .scd-23__inner {
  transform: rotateY(180deg);
}

.scd-23__face {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  padding: 26px;
  backface-visibility: hidden;
  box-shadow: 0 24px 48px -26px rgba(0,0,0,.85);
}

.scd-23__front {
  background: linear-gradient(155deg,#242838,#181b28);
  color: #fff;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.scd-23__k {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.scd-23__front h3 {
  font-size: 44px;
  font-weight: 900;
  margin: 6px 0;
}

.scd-23__front h3 small {
  font-size: 16px;
  font-weight: 600;
  color: #9aa0b4;
}

.scd-23__d {
  font-size: 14px;
  color: #c3c7de;
}

.scd-23__rear {
  background: linear-gradient(155deg,var(--accent),oklch(0.56 0.16 285));
  color: #fff;
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 14px;
}

.scd-23__rear ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.scd-23__rear li {
  font-size: 14px;
  font-weight: 600;
  padding-left: 22px;
  position: relative;
}

.scd-23__rear li::before {
  content: "✓";
  position: absolute;
  left: 0;
  font-weight: 900;
}

.scd-23__rear button {
  padding: 11px;
  border: none;
  border-radius: 11px;
  background: #fff;
  color: oklch(0.5 0.16 285);
  font-weight: 800;
  font-size: 14px;
  cursor: pointer;
}

.scd-23__flip:focus-visible .scd-23__inner {
  box-shadow: none;
}

.scd-23__flip:focus-visible {
  border-radius: 20px;
  box-shadow: 0 0 0 3px var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .scd-23__inner {
    transition: none;
  }

  .scd-23__flip:hover .scd-23__inner,
    .scd-23__flip:focus-visible .scd-23__inner {
    transform: none;
  }

  .scd-23__flip:hover .scd-23__front,
    .scd-23__flip:focus-visible .scd-23__front {
    opacity: 0;
  }

  .scd-23__rear {
    transform: none;
    opacity: 0;
  }

  .scd-23__flip:hover .scd-23__rear,
    .scd-23__flip:focus-visible .scd-23__rear {
    opacity: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — a preserve-3d inner element rotates 180deg on hover/focus, swapping two backface-hidden faces of the top card. */
```
