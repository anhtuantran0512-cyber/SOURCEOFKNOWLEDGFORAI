---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/neon-glow-checkbox/"
title: "Neon Glow Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A dark-mode favourite: on check the box lights up like a neon tube, blooming layered box-shadows in an electric cyan."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Checkbox
Source: https://codefronts.com/components/css-checkboxes/neon-glow-checkbox/

A dark-mode favourite: on check the box lights up like a neon tube, blooming layered box-shadows in an electric cyan. Clean opacity handling keeps the glow smooth, never pixelated — perfect for gaming UIs, crypto dashboards and dark control panels.
## HTML
```html
<section class="cb-08" aria-label="Neon glow checkboxes">
  <div class="cb-08__panel">
    <label class="cb-08__row"><input type="checkbox" class="cb-08__input" checked><span class="cb-08__box" aria-hidden="true"></span><span class="cb-08__label">Enable RGB sync</span></label>
    <label class="cb-08__row"><input type="checkbox" class="cb-08__input"><span class="cb-08__box" aria-hidden="true"></span><span class="cb-08__label">Overclock profile</span></label>
    <label class="cb-08__row"><input type="checkbox" class="cb-08__input" checked><span class="cb-08__box" aria-hidden="true"></span><span class="cb-08__label">Low-latency mode</span></label>
  </div>
</section>
```
## CSS
```css
.cb-08,
.cb-08 *,
.cb-08 *::before,
.cb-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-08 ::selection {
  background: #00ffcc;
  color: #001b17;
}

.cb-08 {
  --neon: #00ffcc;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: radial-gradient(120% 120% at 50% 0%,#141b22 0%,#0a0d11 70%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-08__panel {
  width: min(400px,100%);
  display: flex;
  flex-direction: column;
  gap: 6px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 16px;
  padding: 14px;
}

.cb-08__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 12px 14px;
  border-radius: 10px;
}

.cb-08__input {
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

.cb-08__box {
  position: relative;
  flex: none;
  width: 24px;
  height: 24px;
  border-radius: 7px;
  border: 2px solid #3a4652;
  background: rgba(255,255,255,.02);
  transition: border-color .25s,background .25s;
}

.cb-08__box::before {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: 7px;
  opacity: 0;
  box-shadow: 0 0 6px var(--neon),0 0 14px var(--neon),0 0 26px var(--neon),inset 0 0 8px rgba(0,255,204,.5);
  transition: opacity .3s ease;
  pointer-events: none;
}

.cb-08__box::after {
  content: "";
  position: absolute;
  inset: 0;
  opacity: 0;
  transform: scale(.5);
  background: var(--neon);
  transition: opacity .22s,transform .22s cubic-bezier(.2,.9,.3,1.3);
  -webkit-mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-08__input:checked ~ .cb-08__box {
  border-color: var(--neon);
  background: rgba(0,255,204,.08);
}

.cb-08__input:checked ~ .cb-08__box::before {
  opacity: 1;
  animation: cb-08-pulse 2.4s ease-in-out infinite;
}

.cb-08__input:checked ~ .cb-08__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-08__input:focus-visible ~ .cb-08__box {
  outline: 3px solid var(--neon);
  outline-offset: 3px;
}

.cb-08__label {
  font-size: 14.5px;
  color: #c9d2da;
  letter-spacing: .01em;
}

@keyframes cb-08-pulse {
  0%,
    100% {
    opacity: .7;
  }

  50% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-08__box,
    .cb-08__box::before,
    .cb-08__box::after {
    transition: none;
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :checked reveals layered box-shadow glow via opacity. */
```
