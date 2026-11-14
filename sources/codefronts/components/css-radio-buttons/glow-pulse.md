---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/glow-pulse/"
title: "Outer Glow Pulse Radio"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "A focused, calm signal: the checked radio emits soft glow rings that swell outward and dissolve, like a sonar ping at rest — one ring, then another, on a…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Outer Glow Pulse Radio
Source: https://codefronts.com/components/css-radio-buttons/glow-pulse/

A focused, calm signal: the checked radio emits soft glow rings that swell outward and dissolve, like a sonar ping at rest — one ring, then another, on a slow four-second cycle. Perfect for status pickers and live/recording toggles where the selected state should feel gently alive, not busy.
## HTML
```html
<div class="crb-24-group">
<section class="crb-24a" aria-label="Outer glow pulse radio buttons">
  <fieldset class="crb-24a__group">
    <legend class="crb-24a__legend">Set your status</legend>
    <div class="crb-24a__list">
      <label class="crb-24a__row" style="--c:oklch(0.72 0.19 150)">
        <input class="crb-24a__input" type="radio" name="crb-24a" value="online" checked>
        <span class="crb-24a__well" aria-hidden="true"><span class="crb-24a__ping"></span><span class="crb-24a__ping crb-24a__ping--late"></span><span class="crb-24a__dot"></span></span>
        <span class="crb-24a__text">Online <span class="crb-24a__sub">Visible to everyone</span></span>
      </label>
      <label class="crb-24a__row" style="--c:oklch(0.8 0.15 85)">
        <input class="crb-24a__input" type="radio" name="crb-24a" value="away">
        <span class="crb-24a__well" aria-hidden="true"><span class="crb-24a__ping"></span><span class="crb-24a__ping crb-24a__ping--late"></span><span class="crb-24a__dot"></span></span>
        <span class="crb-24a__text">Away <span class="crb-24a__sub">Back in a bit</span></span>
      </label>
      <label class="crb-24a__row" style="--c:oklch(0.62 0.21 25)">
        <input class="crb-24a__input" type="radio" name="crb-24a" value="busy">
        <span class="crb-24a__well" aria-hidden="true"><span class="crb-24a__ping"></span><span class="crb-24a__ping crb-24a__ping--late"></span><span class="crb-24a__dot"></span></span>
        <span class="crb-24a__text">Do not disturb <span class="crb-24a__sub">Mute all notifications</span></span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-24-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-24-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-24a,
.crb-24a *,
.crb-24a *::before,
.crb-24a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-24a {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 120% at 50% 0%,#151a26,#0b0e16);
}

.crb-24a__group {
  border: none;
  width: min(380px,100%);
}

.crb-24a__legend {
  font-size: 24px;
  font-weight: 750;
  color: #eef1fa;
  letter-spacing: -.02em;
}

.crb-24a__list {
  display: grid;
  gap: 10px;
  margin-top: 20px;
}

.crb-24a__row {
  position: relative;
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: 60px;
  padding: 0 18px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 14px;
  cursor: pointer;
  transition: border-color .25s,background .25s;
}

.crb-24a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-24a__well {
  position: relative;
  width: 22px;
  height: 22px;
  flex: none;
  display: grid;
  place-items: center;
}

.crb-24a__ping {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: var(--c);
  opacity: 0;
  transform: scale(1);
  pointer-events: none;
}

.crb-24a__dot {
  position: relative;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  border: 2.5px solid #47506b;
  background: transparent;
  transition: border-color .25s,background .25s,box-shadow .25s;
}

.crb-24a__text {
  display: grid;
  font-size: 15px;
  font-weight: 650;
  color: #dde2f0;
}

.crb-24a__sub {
  font-size: 12.5px;
  font-weight: 450;
  color: #707a96;
}

.crb-24a__row:hover {
  border-color: color-mix(in oklab,var(--c) 45%,transparent);
}

.crb-24a__row:has(.crb-24a__input:checked) {
  border-color: color-mix(in oklab,var(--c) 60%,transparent);
  background: color-mix(in oklab,var(--c) 6%,transparent);
}

.crb-24a__row:has(.crb-24a__input:checked) .crb-24a__dot {
  border-color: var(--c);
  background: var(--c);
  box-shadow: 0 0 8px color-mix(in oklab,var(--c) 70%,transparent);
}

.crb-24a__row:has(.crb-24a__input:checked) .crb-24a__ping {
  animation: crb-24a-ping 4s cubic-bezier(.2,.6,.4,1) infinite;
}

.crb-24a__row:has(.crb-24a__input:checked) .crb-24a__ping--late {
  animation-delay: 2s;
}

.crb-24a__row:has(.crb-24a__input:focus-visible) {
  outline: 3px solid var(--c);
  outline-offset: 2px;
}

@keyframes crb-24a-ping {
  0% {
    transform: scale(1);
    opacity: .45;
  }

  70% {
    transform: scale(2.4);
    opacity: 0;
  }

  100% {
    transform: scale(2.4);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .crb-24a__row:has(.crb-24a__input:checked) .crb-24a__ping {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two ring spans share a scale/fade keyframe offset by half the cycle, so a new sonar ping departs as the old one dissolves; :has() gates the pulse to the checked row only. */
```
