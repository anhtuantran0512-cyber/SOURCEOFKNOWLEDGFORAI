---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/dark-mode-toggle/"
title: "Dark Mode Toggle"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "The instantly-recognisable theme switch: a sun that glides across and morphs into a crescent moon as the sky shifts from day-blue to starry night."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Toggle
Source: https://codefronts.com/components/css-checkboxes/dark-mode-toggle/

The instantly-recognisable theme switch: a sun that glides across and morphs into a crescent moon as the sky shifts from day-blue to starry night. A global-layout staple that must feel smooth and read at a glance.
## HTML
```html
<section class="cb-22" aria-label="Dark mode toggle">
  <label class="cb-22__row">
    <span class="cb-22__name">Dark mode</span>
    <input type="checkbox" class="cb-22__input" checked>
    <span class="cb-22__track"><span class="cb-22__stars" aria-hidden="true"></span><span class="cb-22__thumb"></span></span>
  </label>
</section>
```
## CSS
```css
.cb-22,
.cb-22 *,
.cb-22 *::before,
.cb-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-22 ::selection {
  background: #ffd76b;
  color: #20242e;
}

.cb-22 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #e9edf3;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-22__row {
  display: flex;
  align-items: center;
  gap: 22px;
  cursor: pointer;
  background: #fff;
  border: 1px solid #e0e5ec;
  border-radius: 16px;
  padding: 20px 26px;
  box-shadow: 0 18px 40px -30px rgba(16,24,40,.5);
}

.cb-22__name {
  font-size: 16px;
  font-weight: 600;
  color: #2a3140;
}

.cb-22__input {
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

.cb-22__track {
  --w: 76px;
  --h: 36px;
  position: relative;
  flex: none;
  width: var(--w);
  height: var(--h);
  border-radius: 999px;
  background: linear-gradient(#7ec8ff,#cdeeff);
  overflow: hidden;
  transition: background .5s ease;
}

.cb-22__stars {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity .5s;
  background: radial-gradient(1.5px 1.5px at 18px 12px,#fff 99%,transparent), radial-gradient(1.5px 1.5px at 30px 24px,#fff 99%,transparent), radial-gradient(1px 1px at 24px 8px,#fff 99%,transparent), radial-gradient(1.5px 1.5px at 40px 16px,#fff 99%,transparent);
}

.cb-22__thumb {
  position: absolute;
  top: 4px;
  left: 4px;
  width: calc(var(--h) - 8px);
  height: calc(var(--h) - 8px);
  border-radius: 50%;
  background: #ffd76b;
  box-shadow: 0 0 10px rgba(255,200,60,.9),inset 0 0 0 0 #d7dde8;
  transition: transform .5s cubic-bezier(.4,.8,.3,1),background .5s,box-shadow .5s;
}

.cb-22__input:checked ~ .cb-22__track {
  background: linear-gradient(#1b2542,#2a3766);
}

.cb-22__input:checked ~ .cb-22__track .cb-22__stars {
  opacity: 1;
}

.cb-22__input:checked ~ .cb-22__track .cb-22__thumb {
  transform: translateX(calc(var(--w) - var(--h)));
  background: #e6ecf5;
  box-shadow: inset -8px 2px 0 0 #b9c4d6;
}

.cb-22__input:focus-visible ~ .cb-22__track {
  outline: 3px solid #4d7fff;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-22__track,
    .cb-22__thumb,
    .cb-22__stars {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the sun thumb translates + an inset shadow carves it into a moon. */
```
