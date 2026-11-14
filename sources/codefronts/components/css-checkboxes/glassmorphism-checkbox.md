---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/glassmorphism-checkbox/"
title: "Glassmorphism Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "Frosted-glass controls that float over vibrant, colourful backgrounds: translucent fills, thin white borders and a real backdrop blur."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Checkbox
Source: https://codefronts.com/components/css-checkboxes/glassmorphism-checkbox/

Frosted-glass controls that float over vibrant, colourful backgrounds: translucent fills, thin white borders and a real backdrop blur. The look every modern lock-screen, music player and premium settings sheet reaches for.
## HTML
```html
<section class="cb-11" aria-label="Glassmorphism checkboxes">
  <div class="cb-11__panel">
    <label class="cb-11__row"><input type="checkbox" class="cb-11__input" checked><span class="cb-11__box" aria-hidden="true"></span><span class="cb-11__label">Ambient sounds</span></label>
    <label class="cb-11__row"><input type="checkbox" class="cb-11__input"><span class="cb-11__box" aria-hidden="true"></span><span class="cb-11__label">Auto-brightness</span></label>
    <label class="cb-11__row"><input type="checkbox" class="cb-11__input" checked><span class="cb-11__box" aria-hidden="true"></span><span class="cb-11__label">Reduce transparency</span></label>
  </div>
</section>
```
## CSS
```css
.cb-11,
.cb-11 *,
.cb-11 *::before,
.cb-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-11 ::selection {
  background: rgba(255,255,255,.6);
  color: #2a1e4a;
}

.cb-11 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: linear-gradient(135deg,oklch(0.7 0.2 300),oklch(0.72 0.18 210) 55%,oklch(0.78 0.19 40));
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-11__panel {
  width: min(400px,100%);
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 16px;
  border-radius: 20px;
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.35);
  -webkit-backdrop-filter: blur(16px) saturate(140%);
  backdrop-filter: blur(16px) saturate(140%);
  box-shadow: 0 20px 50px -24px rgba(30,10,60,.5);
}

.cb-11__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 11px 12px;
  border-radius: 12px;
}

.cb-11__input {
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

.cb-11__box {
  position: relative;
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 8px;
  border: 1.5px solid rgba(255,255,255,.6);
  background: rgba(255,255,255,.18);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  box-shadow: inset 0 1px 2px rgba(255,255,255,.6),inset 0 -2px 4px rgba(80,40,120,.2);
  transition: background .25s,border-color .25s;
}

.cb-11__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .22s,transform .22s cubic-bezier(.2,.9,.3,1.3);
  -webkit-mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-11__input:checked ~ .cb-11__box {
  background: rgba(255,255,255,.6);
  border-color: rgba(255,255,255,.85);
}

.cb-11__input:checked ~ .cb-11__box::after {
  opacity: 1;
  transform: scale(1);
  background: #5b2ea6;
}

.cb-11__input:focus-visible ~ .cb-11__box {
  outline: 3px solid rgba(255,255,255,.9);
  outline-offset: 3px;
}

.cb-11__label {
  font-size: 14.5px;
  font-weight: 500;
  color: #fff;
  text-shadow: 0 1px 2px rgba(40,10,70,.35);
}

@media (prefers-reduced-motion: reduce) {
  .cb-11__box,
    .cb-11__box::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — backdrop-filter frosted glass, :checked brightens the fill. */
```
