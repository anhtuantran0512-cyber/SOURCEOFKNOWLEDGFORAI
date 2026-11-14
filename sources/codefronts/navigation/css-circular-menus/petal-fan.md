---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/petal-fan/"
title: "Petal Reveal Flower Navigation"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A navigation that blooms: five petal-shaped links unfold from a bud, each petal cut with nothing more than an asymmetric border-radius."
has_js: "false"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Petal Reveal Flower Navigation
Source: https://codefronts.com/navigation/css-circular-menus/petal-fan/

A navigation that blooms: five petal-shaped links unfold from a bud, each petal cut with nothing more than an asymmetric border-radius. Organic, playful, zero JavaScript — the whole flower is driven by a checkbox and :has(). Perfect for florists, wellness brands, kids' products and anything that should feel alive.
## HTML
```html
<section class="ccm-10" aria-label="Petal flower navigation demo">
  <div class="ccm-10__stage">
    <div class="ccm-10__flower" style="--n:5">
      <input type="checkbox" id="ccm10-t" class="ccm-10__state">
      <ul class="ccm-10__petals">
        <li class="ccm-10__slot" style="--i:0"><a class="ccm-10__petal" href="#shop"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 8h12l-1 12H7zM9 8a3 3 0 0 1 6 0"/></svg>Shop</span></a></li>
        <li class="ccm-10__slot" style="--i:1"><a class="ccm-10__petal" href="#care"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.6-9.5-9A5.4 5.4 0 0 1 12 6.5 5.4 5.4 0 0 1 21.5 12C19 16.4 12 21 12 21z"/></svg>Care</span></a></li>
        <li class="ccm-10__slot" style="--i:2"><a class="ccm-10__petal" href="#gifts"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9h16v4H4zM6 13h12v8H6zM12 9v12M12 9C9 9 7.5 7.5 7.5 6A2.5 2.5 0 0 1 12 4.5 2.5 2.5 0 0 1 16.5 6C16.5 7.5 15 9 12 9z"/></svg>Gifts</span></a></li>
        <li class="ccm-10__slot" style="--i:3"><a class="ccm-10__petal" href="#events"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5h14v15H5zM5 9h14M9 3v4M15 3v4"/></svg>Events</span></a></li>
        <li class="ccm-10__slot" style="--i:4"><a class="ccm-10__petal" href="#visit"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21c4-4.5 7-7.8 7-11.5a7 7 0 1 0-14 0C5 13.2 8 16.5 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>Visit</span></a></li>
      </ul>
      <label for="ccm10-t" class="ccm-10__bud"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.2"/><path d="M12 8.8C10 7 10 4.5 12 3c2 1.5 2 4-0 5.8zM15.2 12c1.8-2 4.3-2 5.8 0-1.5 2-4 2-5.8 0zM12 15.2c2 1.8 2 4.3 0 5.8-2-1.5-2-4 0-5.8zM8.8 12c-1.8 2-4.3 2-5.8 0 1.5-2 4-2 5.8 0z"/></svg><span class="ccm-10__sr">Toggle flower menu</span></label>
    </div>
    <p class="ccm-10__note">Pure CSS bloom · border-radius petals</p>
  </div>
</section>
```
## CSS
```css
.ccm-10,
.ccm-10 *,
.ccm-10 *::before,
.ccm-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-10 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,oklch(0.97 0.01 120),oklch(0.93 0.025 130));
  --petal: oklch(0.72 0.15 350);
  --petal2: oklch(0.63 0.19 355);
  --leaf: oklch(0.55 0.12 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.ccm-10__stage {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(180deg,oklch(0.97 0.01 120),oklch(0.93 0.025 130));
  border: 1px solid oklch(0.89 0.02 130);
  overflow: hidden;
}

.ccm-10__flower {
  position: relative;
  width: 76px;
  height: 76px;
}

.ccm-10__state,
.ccm-10__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.ccm-10__petals {
  position: absolute;
  inset: 0;
  list-style: none;
}

.ccm-10__slot {
  position: absolute;
  inset: 0;
  rotate: calc((360deg / var(--n)) * var(--i));
}

.ccm-10__petal {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 96px;
  height: 96px;
  margin: -48px;
  display: block;
  border-radius: 50% 50% 50% 6px;
  background: linear-gradient(145deg,var(--petal),var(--petal2));
  box-shadow: 0 10px 26px -12px oklch(0.55 0.18 350 / .55),inset 0 1px 0 oklch(1 0 0 / .35);
  rotate: 45deg;
  transform-origin: 50% 50%;
  translate: 0 0;
  scale: 0;
  opacity: 0;
  visibility: hidden;
  text-decoration: none;
  transition: translate .55s cubic-bezier(.35,1.3,.4,1),scale .55s cubic-bezier(.35,1.3,.4,1),opacity .3s,visibility 0s .55s;
  transition-delay: calc(var(--i) * 50ms);
}

.ccm-10__flower:has(:checked) .ccm-10__petal {
  translate: 0 -92px;
  scale: 1;
  opacity: 1;
  visibility: visible;
  transition: translate .55s cubic-bezier(.35,1.3,.4,1),scale .55s cubic-bezier(.35,1.3,.4,1),opacity .3s,visibility 0s;
  transition-delay: calc(var(--i) * 60ms);
}

.ccm-10__petal span {
  position: absolute;
  inset: 0;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 4px;
  rotate: calc(-45deg - (360deg / var(--n)) * var(--i));
  color: #fff;
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: .03em;
  text-shadow: 0 1px 2px oklch(0.4 0.15 350 / .5);
}

.ccm-10__petal svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.ccm-10__petal:hover,
.ccm-10__petal:focus-visible {
  filter: brightness(1.08);
  outline: none;
}

.ccm-10__petal:focus-visible {
  outline: 3px solid var(--petal2);
  outline-offset: 4px;
}

.ccm-10__bud {
  position: absolute;
  inset: 0;
  z-index: 2;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,oklch(0.65 0.13 150),var(--leaf));
  color: #fff;
  cursor: pointer;
  box-shadow: 0 12px 28px -10px oklch(0.45 0.12 150 / .7);
  transition: rotate .6s cubic-bezier(.35,1.3,.4,1),scale .3s;
}

.ccm-10__bud:hover {
  scale: 1.06;
}

.ccm-10__bud svg {
  width: 34px;
  height: 34px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linejoin: round;
}

.ccm-10__flower:has(:checked) .ccm-10__bud {
  rotate: 180deg;
}

.ccm-10__flower:has(.ccm-10__state:focus-visible) .ccm-10__bud {
  outline: 3px solid var(--leaf);
  outline-offset: 4px;
}

.ccm-10__note {
  position: absolute;
  bottom: 20px;
  font-size: 12px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.55 0.06 140 / .6);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-10 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
