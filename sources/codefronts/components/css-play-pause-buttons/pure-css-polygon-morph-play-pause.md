---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/pure-css-polygon-morph-play-pause/"
title: "Pure CSS Polygon Morph Play Pause"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "The purest expression of the pattern: two rectangles that morph into a triangle with nothing but clip-path and a flex gap — no JavaScript, no SVG, no icon font."
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Polygon Morph Play Pause
Source: https://codefronts.com/components/css-play-pause-buttons/pure-css-polygon-morph-play-pause/

The purest expression of the pattern: two rectangles that morph into a triangle with nothing but clip-path and a flex gap — no JavaScript, no SVG, no icon font. Each bar is clipped to one half of the play triangle, and the gap between them animates to zero, so the pause icon literally folds into the play icon along a single interpolated path. A visually-hidden checkbox holds the state, which means keyboard, focus and toggle semantics are native.
## HTML
```html
<section class="pp-01" aria-label="Pure CSS polygon morph play pause demo">
  <div class="pp-01__stage">
    <div class="pp-01__unit">
      <input class="pp-01__chk" type="checkbox" id="pp-01-toggle" aria-label="Play or pause the track">
      <label class="pp-01__btn" for="pp-01-toggle">
        <span class="pp-01__bars" aria-hidden="true"><i></i><i></i></span>
      </label>
      <div class="pp-01__meta">
        <p class="pp-01__title">Midnight Interval</p>
        <p class="pp-01__sub">Kilobyte Orchestra — 3:42</p>
        <span class="pp-01__line" aria-hidden="true"><b></b></span>
      </div>
    </div>
    <p class="pp-01__chip" aria-hidden="true">clip-path polygon interpolation · animatable flex gap · :checked ~ sibling</p>
  </div>
</section>
```
## CSS
```css
.pp-01,
.pp-01 *,
.pp-01 *::before,
.pp-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-01-bg);
  --pp-01-bg: oklch(0.16 0.02 265);
  --pp-01-card: oklch(0.22 0.025 265);
  --pp-01-ink: oklch(0.97 0.005 260);
  --pp-01-mut: oklch(0.68 0.02 265);
  --pp-01-acc: oklch(0.78 0.16 155);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--pp-01-ink);
}

.pp-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% 8%,oklch(0.28 0.06 165/.45),transparent 70%);
}

.pp-01__unit {
  display: flex;
  align-items: center;
  gap: 22px;
  padding: 20px 30px 20px 20px;
  border-radius: 22px;
  background: var(--pp-01-card);
  box-shadow: 0 0 0 1px oklch(1 0 0/.07),0 24px 60px oklch(0 0 0/.45);
}

.pp-01__chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-01__btn {
  display: grid;
  place-items: center;
  width: 76px;
  height: 76px;
  border-radius: 50%;
  background: var(--pp-01-acc);
  color: oklch(0.2 0.04 165);
  cursor: pointer;
  transition: transform .28s cubic-bezier(.34,1.4,.5,1),box-shadow .28s;
}

.pp-01__btn:hover {
  transform: scale(1.06);
}

.pp-01__btn:active {
  transform: scale(.95);
}

.pp-01__chk:focus-visible+.pp-01__btn {
  box-shadow: 0 0 0 3px var(--pp-01-card),0 0 0 6px var(--pp-01-acc);
}

.pp-01__bars {
  display: flex;
  gap: 0;
  width: 30px;
  height: 34px;
  transform: translateX(2px);
  transition: gap .42s cubic-bezier(.65,0,.35,1),transform .42s cubic-bezier(.65,0,.35,1);
}

.pp-01__bars i {
  flex: 1;
  background: currentColor;
  transition: clip-path .42s cubic-bezier(.65,0,.35,1);
}

.pp-01__bars i:nth-child(1) {
  clip-path: polygon(0 0,100% 25%,100% 75%,0 100%);
}

.pp-01__bars i:nth-child(2) {
  clip-path: polygon(0 25%,100% 50%,100% 50%,0 75%);
}

.pp-01__chk:checked+.pp-01__btn .pp-01__bars {
  gap: 9px;
  transform: translateX(0);
}

.pp-01__chk:checked+.pp-01__btn .pp-01__bars i {
  clip-path: polygon(0 0,100% 0,100% 100%,0 100%);
}

.pp-01__meta {
  min-width: min(52vw,220px);
}

.pp-01__title {
  font-size: 17px;
  font-weight: 650;
  letter-spacing: -.01em;
}

.pp-01__sub {
  font-size: 13px;
  color: var(--pp-01-mut);
  margin-top: 3px;
}

.pp-01__line {
  display: block;
  height: 4px;
  margin-top: 14px;
  border-radius: 99px;
  background: oklch(1 0 0/.13);
  overflow: hidden;
}

.pp-01__line b {
  display: block;
  height: 100%;
  width: 0;
  border-radius: 99px;
  background: var(--pp-01-acc);
  animation: pp-01-fill 14s linear infinite;
  animation-play-state: paused;
}

.pp-01__unit:has(.pp-01__chk:checked) .pp-01__line b {
  animation-play-state: running;
}

@keyframes pp-01-fill {
  from {
    width: 0;
  }

  to {
    width: 100%;
  }
}

.pp-01__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-01-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-01 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
