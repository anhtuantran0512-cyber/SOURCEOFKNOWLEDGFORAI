---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/neon-arc-css-spinner/"
title: "Neon Arc CSS Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A single glowing cyan arc rotates on a deep-dark background, with a luminous leading-edge dot that amplifies the neon effect via CSS drop-shadow filters."
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Arc CSS Spinner
Source: https://codefronts.com/motion/css-spinner-designs/neon-arc-css-spinner/

A single glowing cyan arc rotates on a deep-dark background, with a luminous leading-edge dot that amplifies the neon effect via CSS drop-shadow filters.
## HTML
```html
<div class="sp-01">
  <div class="sp-01__ring">
    <div class="sp-01__track"></div>
    <div class="sp-01__spinner">
      <div class="sp-01__arc"></div>
      <div class="sp-01__dot"></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sp-01,
.sp-01 *,
.sp-01 *::before,
.sp-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-01 {
  --bg: #0a0a0f;
  --arc: #00f5ff;
  --glow: rgba(0,245,255,0.4);
  --track: rgba(0,245,255,0.12);
  --size: 72px;
  --thickness: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui,sans-serif;
}

.sp-01__ring {
  position: relative;
  width: var(--size);
  height: var(--size);
}

.sp-01__track {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: var(--thickness) solid var(--track);
}
/* The arc and dot-arm share one rotating parent so they move together */

.sp-01__spinner {
  position: absolute;
  inset: 0;
  animation: sp-01-spin 1s cubic-bezier(0.6,0.2,0.4,0.8) infinite;
}

.sp-01__arc {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: var(--thickness) solid transparent;
  border-top-color: var(--arc);
  border-right-color: var(--arc);
  filter: drop-shadow(0 0 8px var(--glow)) drop-shadow(0 0 16px var(--glow));
}
/* Leading-edge dot — a glowing tip at the LEADING END of the arc.
   The arc is built from border-top + border-right, so visually it
   spans ~135° (top-left corner) through 12 → 3 → ~225° (bottom-right
   corner). The END of border-right is at the bottom-right corner of
   the box (4:30 clock position), which is the LEADING tip during
   clockwise rotation.

   To position the dot at 4:30 on a 72×72 spinner: rotate 135° around
   the center via transform: rotate(135deg) translateY(-r), where r =
   (size/2 - thickness/2). Using a CSS custom property for r keeps
   this responsive to --size + --thickness changes.

   The dot is anchored at the spinner center (top:50%, left:50%) then
   rotated outward by 135° (= 4:30 clock direction = the leading-end
   of the arc), with translateY(-r) moving it to the arc's stroke
   midline radius. Sized 1.75× the arc thickness for a visible glowing
   tip without a chunky-bump look. */

.sp-01__dot {
  position: absolute;
  top: 50%;
  left: 50%;
  width: calc(var(--thickness) * 1.75);
  height: calc(var(--thickness) * 1.75);
  transform: translate(-50%, -50%) rotate(135deg) translateY(calc(var(--size) / -2 + var(--thickness) / 2));
  background: var(--arc);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--arc),0 0 16px var(--glow);
}

@keyframes sp-01-spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-01__spinner {
    animation: none;
  }
}
```
