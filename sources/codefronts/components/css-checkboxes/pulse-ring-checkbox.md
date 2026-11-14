---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/pulse-ring-checkbox/"
title: "Pulse Ring Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "An attention-grabbing 'live' state: once checked, the box radiates soft, fading concentric rings outward, like a sonar ping."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pulse Ring Checkbox
Source: https://codefronts.com/components/css-checkboxes/pulse-ring-checkbox/

An attention-grabbing 'live' state: once checked, the box radiates soft, fading concentric rings outward, like a sonar ping. Ideal for onboarding cues, active-task indicators and 'you're all set' confirmations.
## HTML
```html
<section class="cb-23" aria-label="Pulse ring checkboxes">
  <div class="cb-23__panel">
    <label class="cb-23__row"><input type="checkbox" class="cb-23__input" checked><span class="cb-23__box" aria-hidden="true"><span class="cb-23__r1"></span><span class="cb-23__r2"></span></span><span class="cb-23__label">Go live now</span></label>
    <label class="cb-23__row"><input type="checkbox" class="cb-23__input"><span class="cb-23__box" aria-hidden="true"><span class="cb-23__r1"></span><span class="cb-23__r2"></span></span><span class="cb-23__label">Broadcast status</span></label>
    <label class="cb-23__row"><input type="checkbox" class="cb-23__input"><span class="cb-23__box" aria-hidden="true"><span class="cb-23__r1"></span><span class="cb-23__r2"></span></span><span class="cb-23__label">Ping teammates</span></label>
  </div>
</section>
```
## CSS
```css
.cb-23,
.cb-23 *,
.cb-23 *::before,
.cb-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-23 ::selection {
  background: oklch(0.62 0.17 15);
  color: #fff;
}

.cb-23 {
  --accent: oklch(0.6 0.19 15);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #faf4f4;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-23__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #f0dddd;
  border-radius: 14px;
  padding: 14px 16px;
}

.cb-23__row {
  display: flex;
  align-items: center;
  gap: 18px;
  cursor: pointer;
  padding: 15px 8px;
}

.cb-23__input {
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

.cb-23__box {
  position: relative;
  flex: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 2px solid #e2b6b6;
  background: #fff;
  display: grid;
  place-items: center;
  transition: background .25s,border-color .25s;
}

.cb-23__box::after {
  content: "";
  width: 14px;
  height: 14px;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .22s,transform .22s cubic-bezier(.2,.9,.3,1.3);
  -webkit-mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-23__r1,
.cb-23__r2 {
  position: absolute;
  inset: -2px;
  border-radius: 50%;
  border: 2px solid var(--accent);
  opacity: 0;
  transform: scale(1);
  z-index: -1;
  pointer-events: none;
}

.cb-23__input:checked ~ .cb-23__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-23__input:checked ~ .cb-23__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-23__input:checked ~ .cb-23__box .cb-23__r1 {
  animation: cb-23-pulse 2s ease-out infinite;
}

.cb-23__input:checked ~ .cb-23__box .cb-23__r2 {
  animation: cb-23-pulse 2s ease-out infinite 1s;
}

.cb-23__input:focus-visible ~ .cb-23__box {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

.cb-23__label {
  font-size: 14.5px;
  color: #3a2727;
}

@keyframes cb-23-pulse {
  0% {
    opacity: .5;
    transform: scale(1);
  }

  100% {
    opacity: 0;
    transform: scale(2.4);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-23__box,
    .cb-23__box::after {
    transition: none;
  }

  .cb-23__r1,
    .cb-23__r2 {
    animation: none!important;
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — checked rings scale out + fade on an infinite staggered loop. */
```
